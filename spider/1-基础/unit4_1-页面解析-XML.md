# spider-页面解析-XML	
**作者：詹亮**


2. XML

	1. 什么是XML

		* XML 指可扩展标记语言（EXtensible Markup Language）
		* XML 是一种标记语言，很类似 HTML
		* XML 的设计宗旨是传输数据，而非显示数据
		* XML 的标签需要我们自行定义。
		* XML 被设计为具有自我描述性。
		* XML 是 W3C 的推荐标准

	2. 什么是XPath？

		XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历。
		
		XPath 开发工具

		- 开源的XPath表达式编辑工具:XMLQuire(XML格式文件可用)
		- Chrome插件 XPath Helper
		- Firefox插件 XPath Checker

	3. 示例文档

			<?xml version="1.0" encoding="utf-8"?>

			<bookstore> 
			
			  <book category="cooking"> 
			    <title lang="en">Everyday Italian</title>  
			    <author>Giada De Laurentiis</author>  
			    <year>2005</year>  
			    <price>30.00</price> 
			  </book>  
			
			  <book category="children"> 
			    <title lang="en">Harry Potter</title>  
			    <author>J K. Rowling</author>  
			    <year>2005</year>  
			    <price>29.99</price> 
			  </book>  
			
			  <book category="web"> 
			    <title lang="en">XQuery Kick Start</title>  
			    <author>James McGovern</author>  
			    <author>Per Bothner</author>  
			    <author>Kurt Cagle</author>  
			    <author>James Linn</author>  
			    <author>Vaidyanathan Nagarajan</author>  
			    <year>2003</year>  
			    <price>49.99</price> 
			  </book> 
			
			  <book category="web" cover="paperback"> 
			    <title lang="en">Learning XML</title>  
			    <author>Erik T. Ray</author>  
			    <year>2003</year>  
			    <price>39.95</price> 
			  </book> 
			
			</bookstore>
	4. 安装lxml

			pip install lxml
	4. 常用方法

		1. etree.parse()

			读取xml文件，结果为**xml对象**（不是字符串）
		2. etree.HTML(string_html)

			将字符串形势的html文件转换为xml对象
		3. etree.tostring(htmlelement, encoding="utf-8").decode("utf-8")

				etree.tostring(html,encoding="utf-8", pretty_print=True).decode()

			按字符串序列化HTML文档
	5. 选择器

		|表达式|	描述|
		|---|---|---|
		|nodename|	选取此节点的所有子节点。|
		|/	|从根节点选取。|
		|//	|从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。|
		|.	|选取当前节点。|
		|..	|选取当前节点的父节点。|
		|@	|选取属性。|
		
		范例
		
			bookstore	选取 bookstore 元素的所有子节点(如果只有一个的话)。
			/bookstore	选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
			bookstore/book	选取属于 bookstore 的直接子元素的所有 book 元素。
			//book	选取所有 book 子元素，而不管它们在文档中的位置。
			bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
			bookstore//book/@lang	选取book元素的lang属性值。
			bookstore//book[@class="book-css"]/title	选取class属性值为“book-css”的book元素的title。
			//*[@class="bold"] 获取 class 值为 bold 的标签名
		
		**使用属性时，不要忘记@符号**
		> /表示直接子元素，//表示所有子孙元素
		
		
		读取案例-xml
		
			#from lxml import etree #这样写后面会出现红色波浪线
			
			import lxml.html
			etree = lxml.html.etree
			# 读取文件：这个时候只时候读取xml格式的文件，显然局限性太强！！！！！
			html = etree.parse('data.xml')
			# 转化为字节字符串
			# result = etree.tostring(html, pretty_print=True)
			# print(type(html))  # 显示etree.parse() 返回类型
			# print(result)
			titles = html.xpath('/bookstore/book/title')
			
			for tt in titles:
			    print(tt.text)
			
			# 如果不是直接子元素就要用//
	
			titles = html.xpath('/bookstore//title')
			
			for tt in titles:
			    print(tt.text)
	6. lxml读取html文件
		​	
		自己创建html解析器，增加parser参数
		
			import lxml.html
			etree = lxml.html.etree
			parser = etree.HTMLParser(encoding="utf-8")
			htmlelement = etree.parse("liepin.html", parser=parser)
			print(htmlelement)
			html_string=etree.tostring(htmlelement, encoding="utf-8").decode("utf-8")
			
			#读取innerText
			links=htmlelement.xpath('//div/div/span/a')
	
			for link in links:
			    print(link.text)
			    
			#读取属性的值
			
			with open('liepin.html','r+') as fp:
			    content=fp.read()
			    html=etree.HTML(content)
			    links = html.xpath('//div/div/span/@title')
			    for title in titles:
			        print(title)
	
		不缓存文件，直接读取爬取的html字符串
		
			response=requests.get(url)
			etree = lxml.html.etree
			parser = etree.HTMLParser(encoding="utf-8")
			#<!--读取字符串-->
			htmlelement = etree.HTML(response.text)