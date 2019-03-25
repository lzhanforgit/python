# python items & spider
**作者：詹亮**



3. Items

	1. item值操作
			
			#获取item属性值
			item['title']
			item.get('title')
			
			item.keys()
			item.items()
			

2. spider

	对spider来说，爬取的循环类似下文:

	1. 以初始的URL初始化Request，并设置回调函数。 当该request下载完毕并返回时，将生成response，并作为参数传给该回调函数。

		>spider中初始的request是通过调用 start_requests() 来获取的。 
		start_requests() 读取 start_urls 中的URL， 并以 parse 为回调函数生成 Request 。
	
	3. 在回调函数内分析返回的(网页)内容，返回 Item 对象或者 Request 或者一个包括二者的可迭代容器。 返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数(函数可相同)。
	4. 在回调函数内，您可以使用 选择器(Selectors) (您也可以使用BeautifulSoup, lxml 或者您想用的任何解析器) 来分析网页内容，并根据分析的数据生成item。
	5. 最后，由spider返回的item将被存到数据库(由某些 Item Pipeline 处理)或使用 Feed exports 存入到文件中。
	
	虽然该循环对任何类型的spider都(多少)适用，但Scrapy仍然为了不同的需求提供了多种默认spider。 

2. allowed_domains


	可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。
	
3. start_urls

	URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 后续的URL将会从获取到的数据中提取。
	
	这个列表中的url会被依次取出并爬取。
3. start_requests()

	如果您想要修改最初爬取某个网站的Request对象，您可以重写(override)该方法。
	
		 start_url = ['']
	    def start_requests(self):
	        for i in range(100):  # 爬31页数据差不多了
	            url = self.start_url[0] + '&s=' + str(i * 44)
	            yield scrapy.FormRequest(url=url, callback=self.parse)
	            
	**回顾url**
	
		from urllib import parse
		import string
		
		#生成url
		
		qs={
		    "page_start":20*4
		}
		
		url=url+parse.urlencode(qs)
		
		#解决url中文的问题
		url='https://s.taobao.com/search?q=手机&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=' \
		        'tbindexz_20170306&p4ppushleft=5%2C48&'
		
		url=parse.quote(url,safe=string.printable)
		
		
		print(url)


	[动态爬虫](https://blog.csdn.net/sdulsj/article/details/52984824)


