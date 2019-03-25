# python shell
**作者：詹亮**


1. 选择器

	|  | CSS<span class="Apple-tab-span" style="white-space:pre"></span> | Xpath | 备注 |
	| --- | --- | --- | --- |
	| 含有属性 | response.css('div[class]') | response.xpath('//div[@class]') | css可以简写为 div.class 甚至 .class，div#abc 或 #abc 则对应于id=abc |
	| 匹配属性值 | response.css('div[class="quote"]') | response.xpath('//div[@class="quote"]') |  <div>response.xpath('//small[text()="Albert Einstein"]')</div>
	|
	| 匹配部分属性值 | response.css('div[class*="quo"]') | response.xpath('//div[contains(@class,"quo")]')  | response.xpath('//small[contains(text(),"Einstein")]')  |
	| 提取属性值 | response.css('small::attr(class)') | response.xpath('//small/@class')  | css里面text排除在attr以外，所以不支持上面两个过滤text？？？ |
	| 提取文字 | response.css('small::text') | response.xpath('//small/text()') |  |

2. scrapy shell

	Scrapy终端是一个交互终端，供您在未启动spider的情况下尝试及调试您的爬取代码。 其本意是用来测试提取数据的代码，不过您可以将其作为正常的Python终端，在上面测试任何的Python代码。
	
	该终端是用来测试XPath或CSS表达式，查看他们的工作方式及从爬取的网页中提取的数据。 在编写您的spider时，该终端提供了交互性测试您的表达式代码的功能，免去了每次修改后运行spider的麻烦。
	
	一旦熟悉了Scrapy终端后，您会发现其在开发和调试蜘蛛时发挥的巨大作用。
	
	如果您安装了IPython中，Scrapy终端将使用IPython的（替代标准的Python终端）。 IPython的终端与其他相比更为强大，提供智能的自动补全，高亮输出，及其他特性。
	
	我们强烈推荐您安装IPython，特别是如果您使用Unix系统（IPython在Unix下工作的很好）。详情请参考IPython安装指南。

		```
		pip install ipython
		```

	启动终端
		
		```
		    scrapy  shell  < url >
		    
		```

	**使用终端**

	Scrapy终端仅仅是一个普通的Python终端（或IPython）。其提供了一些额外的快捷方式。

	可用的快捷命令（快捷方式）
	
	* shelp() - 打印可用对象及快捷命令的帮助列表
	* fetch(request_or_url) - 根据给定的请求（请求）或URL获取一个新的回复，并更新相关的对象
	* view(response)- 在本机的浏览器打开给定的响应。其会在响应的身体中添加一个<base>标记，使得外部链接（例如图片和css）能正确显示。注意，该操作会在本地创建一个临时文件，且该文件不会被自动删除。

	**可用的Scrapy对象**
	Scrapy终端根据下载的页面会自动创建一些方便使用的对象，例如 Response对象及 Selector对象（对HTML及XML内容）。

	这些对象有：
	
	* crawler- 当前Crawler对象。
	* spider- 处理URL的蜘蛛。对当前URL没有处理的Spider时则为一个Spider对象。
	* request- 最近获取到的页面的Request对象。您可以使用replace()修改该请求。或者使用fetch快捷方式来获取新的请求。
	* response- 包含最近获取到的页面的Response对象。
	* sel- 根据最近获取到的响应构造的Selector对象(ipython已经废弃)。
	* settings- 当前的Scrapy设置
	
	Scrapy Selectors 内置 XPath 和 CSS Selector 表达式机制


	Selector有四个基本的方法，最常用的还是xpath:

	* xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表
	* extract(): 序列化该节点为Unicode字符串并返回list
	* css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表，语法同 BeautifulSoup4
	* re(): 根据传入的正则表达式对数据进行提取，返回Unicode字符串list列表
	* getall():返回Unicode字符串list列表

	操作对象(选择器方法( .xpath() or .css() )返回相同类型的选择器列表):
	
		```
		#xpath
		#div的所有超链接直接子元素
		response.xpath('//div/a').extract()[0]
		
		#div的所有超链接子元素
		response.xpath('//div//a').extract()[0]
		#获取超链接的内容文本
		response.xpath('//div/a/text()').extract()[0]
		
		#获取超链接href的值
		response.xpath('//div/a/@href').extract()[0]
		response.xpath('//div/a/@href').extract_first()
		
		#查找href属性中包含image
		response.xpath('//a[contains(@href, "image")]/@href').extract()
		
		#获取同时具有title和data-id属性的超链接元素
		response.xpath('//ul/li/a[@title][@data-id]').extract()

		
		response.xpath('//ul/li/a[@href="javascript:;"]/text()').extract()[0]
		
		
		#css
		#获取超链接的内容文本
		response.css('ul li a[href]::text').extract()
		
		#获取超链接href的值
		response.css('ul li a::attr(href)').extract()
		
		response.css('a[href*=image]::attr(href)').extract()
		response.css('ul li a[href^="java"]::attr(href)').extract()
		
		#超链接包含 href,title,data-id属性的
		response.css('ul li a[href][title][data-id]::attr(href)').extract()

		
		
		```
	
	**在实际操作中我们要结合正则表达式使用选择器(selectors)**
	
		response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
		
---
	
		```
		#重新抓取另一个页面
		fetch('http://127.0.0.1:63343/Test/test2.html?_ijt=o3iv4mthvqaq609l51a5c1p6b')
		
		#查看url
		response.url
		
		#改变请求方式
		request = request.replace(method="POST")
		#重新抓取
		fetch(request)
		
		#退出终端
		
		exit
		
		```


	
##思考

		for p in divs.xpath('.//p'):  # extracts all <p> inside
		    print p.extract()
		    
		for p in divs.xpath('p'):
		    print p.extract()