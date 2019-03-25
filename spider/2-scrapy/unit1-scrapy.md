# scrapy
**作者：詹亮**



### 安装环境
1. 站点

	[Scrapy框架官方网址](http://doc.scrapy.org/en/latest)

	[Scrapy中文维护站点](http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html)
2. 安装

		pip install Scrapy

	>安装后，只要在命令终端输入 scrapy可以检验是否安装成功。
	
	windows安装错误：
	
	[Scrapy安装错误：](MicrosoftVisualC++14.0isrequired...
https://blog.csdn.net/nima1994/article/details/74931621)
	
	下载地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
	
### 1.命令



1. 创建项目

	```
	    scrapy startproject myproject
	```
	
	项目目录结构：
	下面来简单介绍一下各个主要文件的作用：

	- scrapy.cfg ：项目的配置文件
	
	- mySpider/ ：项目的Python模块，将会从这里引用代码
	
	- mySpider/items.py ：项目的目标文件
	
	- mySpider/pipelines.py ：项目的管道文件
	
	- mySpider/settings.py ：项目的设置文件
	
	- mySpider/spiders/ ：存储爬虫代码目录
2. 创建一个新的spider

	```
	    scrapy genspider mydomain mydomain.com
	```
	
	要建立一个Spider， 你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性 和 一个方法。

	1. name = "" ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
	
	2. allow_domains = [] 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
	
	3. start_urls = () ：爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
	
	4. parse(self, response) ：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
	
		负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
	生成需要下一页的URL请求。
	
3. 查看所有爬虫

	```
	    scrapy list
	```
	执行爬虫
	
	```
	    scrapy crawl <spider>
	```
	执行爬虫，并把结果保存到指定文件
	
	```
	    scrapy crawl runoob  -o taobo.json
	```
	利用命令行，抓取指定URL的代码
	
	```
	    scrapy fetch https://s.taobao.com/list?q=iphone
	```
	>备注的部分

4. DEMO

	1. 构建item模型
		打开mySpider目录下的items.py
	
		Item 定义结构化数据字段，用来保存爬取到的数据，有点像Python中的dict，但是提供了一些额外的保护减少错误。
	
		可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field的类属性来定义一个Item（可以理解成类似于ORM的映射关系）。
	
		接下来，创建一个ItcastItem 类，和构建item模型（model）。
		
			import scrapy
			from scrapy.item import Item, Field
			
			class MyteachspiderItem(scrapy.Item):
			    # define the fields for your item here like:
			    # name = scrapy.Field()
			    pass
			
			class Website(Item):
			
			    title = Field()
			    link = Field()
			    desc = Field()

	2. 新建爬虫

			scrapy genspider runoob runoob.com

	3. 定义爬虫

			# -*- coding: utf-8 -*-
			import scrapy
			
			from myTeachSpider.items import Website
			class RunoobSpider(scrapy.Spider):
			    name = "runoob"
			    allowed_domains = ["runoob.com"]
			    start_urls = [
			        "http://www.runoob.com/html/html-tutorial.html",
			        "http://www.runoob.com/css/css-tutorial.html",
			    ]
			
			    def parse(self, response):
			    		
			    	 items=[]
			    	  
			        for sel in response.xpath('//ul/li'):
			            item = Website()
			            # extract()方法返回的都是unicode字符串
			            # xpath返回的是包含一个元素的列表
			            item['title'] = sel.xpath('a/text()').extract()
			            item['link'] = sel.xpath('a/@href').extract()
			            item['desc'] = sel.xpath('text()').extract()
							
						  items.append(item)
			            # 将获取的数据交给pipelines
			            # yield item
			
			            # 返回数据，不经过pipeline
			            return items

	4. 执行爬虫并保存到指定文件

			scrapy crawl runoob  -o runoob.json
			
		新建run.py
		
			from scrapy.cmdline import execute
			execute(['scrapy', 'crawl', 'runoobSpider'])
			
			#execute('scrapy crawl runoobSpider -o items.csv -t csv'.split())
