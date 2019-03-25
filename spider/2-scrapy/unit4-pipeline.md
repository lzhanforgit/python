# python items & spider  
**作者：詹亮**

          
4. Item Pipeline

	当Item在Spider中被收集之后，它将会被传递到Item Pipeline，一些组件会按照一定的顺序执行对Item的处理。
	
	每个item pipeline组件(有时称之为“Item Pipeline”)是实现了简单方法的Python类。他们接收到Item并通过它执行一些行为，同时也决定此Item是否继续通过pipeline，或是被丢弃而不再进行处理。
	
	以下是item pipeline的一些典型应用：
	
	* 清理HTML数据
	* 验证爬取的数据(检查item包含某些字段)
	* 查重(并丢弃)
	* 将爬取结果保存到数据库中

	**自定义pipeline**
	
	编写你自己的item pipeline很简单，每个item pipiline组件是一个独立的Python类，同时必须实现以下方法:
	
		```
		#每个item pipeline组件都需要调用该方法，这个方法必须返回一个 Item (或任何继承类)对象， 或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。
		process_item(item, spider)
		
		#当spider被开启时，这个方法被调用。
		open_spider(spider)
		
		#当spider被关闭时，这个方法被调用
		close_spider(spider)
		```
	**将item写入JSON文件**
	
	以下pipeline将所有(从所有spider中)爬取到的item，存储到一个独立地 items.jl 文件，每行包含一个序列化为JSON格式的item:

		```
		import json
		
		class JsonWriterPipeline(object):
		
		    def __init__(self):
		        self.file = open('items.jl', 'wb')
		
		    def process_item(self, item, spider):
		        # line = json.dumps(dict(item)) + "\n"
		        # 解决中文乱码的问题
		        line = json.dumps(dict(item),ensure_ascii=False,indent=2) + "\n"
		        self.file.write(line)
		        return item
		```


	改进版
		
		class MyspidersPipeline(object):

	    def __init__(self):
	        self.fp=open('jobs.json','a+')
	        self.jobs=[]
	    def process_item(self, item, spider):
	        line=dict(item)
	        self.jobs.append(line)
	        return item
	    def close_spider(self,spider):
	        json.dump(self.jobs,self.fp,ensure_ascii=False)
	**多个pipeline之间通过return itme 传递数据**
	
	**解决中文乱码的问题**
	
	因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：
	indent=2表示缩进几个字符，可以控制json输出的格式
	
		import json
		users=[{"name":"詹亮","nation":"中国"},{"name":"jacky","nation":"中国"}]
		
		print(json.dumps(users,ensure_ascii=False,indent=2))
	
	
	
	**去重**
	
	一个用于去重的过滤器，丢弃那些已经被处理过的item。让我们假设我们的item有一个唯一的id，但是我们spider返回的多个item中包含有相同的id:
	
		```
		from scrapy.exceptions import DropItem
		
		class DuplicatesPipeline(object):
		
		    def __init__(self):
		        self.ids_seen = set()
		
		    def process_item(self, item, spider):
		        if item['id'] in self.ids_seen:
		            raise DropItem("Duplicate item found: %s" % item)
		        else:
		            self.ids_seen.add(item['id'])
		            return item
		```
	***启用一个Item Pipeline组件***
	
	为了启用一个Item Pipeline组件，你必须将它的类添加到 ITEM_PIPELINES 配置，就像下面这个例子:

		```
		ITEM_PIPELINES = {
		    'myproject.pipelines.PricePipeline': 300,
		    'myproject.pipelines.JsonWriterPipeline': 800,
		}
		```
	分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内。

3. 案例图片下载

	items代码
	
		
		class JuMei(Item):
		    title=Field()
		    price=Field()
		    acount=Field()
		    img_url=Field()
	spider代码：jumei.py
	
		# -*- coding: utf-8 -*-
		import scrapy
		
		from myspiders.items import JuMei
		class JumeiSpider(scrapy.Spider):
		    name = 'jumei'
		    allowed_domains = ['jumei.com']
		    start_urls = ['http://search.jumei.com/?search=香水']
		
		    def parse(self, response):
		
		        all=[]
		        goods=response.xpath('//div[@class="products_wrap"]/ul/li[@pid][@bid][@cid]')
		        print(len(goods))
		
		        for good in goods:
		            obj=JuMei()
		            obj['title']=good.xpath('.//div[@class="s_l_name"]/a/text()').extract()[0].strip()
		            obj['img_url']=good.xpath('.//div[@class="s_l_pic"]/a/img/@src').extract()[0]
		            obj['price']=good.xpath('.//div[@class="search_list_price"]/span/text()').extract()[0]
		            obj['acount']=good.xpath('.//div[@class="search_pl"]/text()').extract()[0]
		
		            yield obj
		            # all.append(obj)
		
		        # return all


	pipeline代码：MyImagesPipeline
	
		from scrapy.exceptions import DropItem
		from scrapy import Request
		from scrapy.pipelines.images import ImagesPipeline
		import re
		
		class MyImagesPipeline(ImagesPipeline):
		    default_headers = {
		        'accept': 'image/webp,image/*,*/*;q=0.8',
		        'accept-encoding': 'gzip, deflate, sdch, br',
		        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
		        'cookie': 'bid=yQdC/AzTaCw',
		        'referer': '',
		        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
		    }
		    def file_path(self, request, response=None, info=None):
		        """
		        :param request: 每一个图片下载管道请求
		        :param response:
		        :param info:
		        :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
		        :return: 每套图的分类目录
		        """
		        item = request.meta['item']
		        folder = item['title']
		        # folder_strip = self.strip(folder)
		        image_guid = request.url.split('/')[-1]
		        filename = u'full/{0}/{1}'.format(folder, image_guid)
		        return filename
		    def get_media_requests(self, item, info):
		        print('11111111111111111111')
		        """
		        :param item: spider.py中返回的item
		        :param info:
		        :return:
		        """
		        referer = item['img_url']
		        self.default_headers['referer'] = referer
		        yield Request(item['img_url'],headers=self.default_headers,meta={'item': item,'referer': referer})
		
		    def item_completed(self, results, item, info):
		        print('999999999')
		        print(results)
		        image_paths = [x['path'] for ok, x in results if ok]
		        if not image_paths:
		            raise DropItem("Item contains no images")
		        return item
		
		
		    def strip(path):
		        """
		        :param path: 需要清洗的文件夹名字
		        :return: 清洗掉Windows系统非法文件夹名字的字符串
		        """
		        path = re.sub(r'[？\\*|“<>:/]', '', str(path))
		
		        return path
		
		
	settings.py
	
		ITEM_PIPELINES = {
		   # 'myspiders.pipelines.MyspidersPipeline': 300,
		   # 'myspiders.pipelines.TestPipeline': 400
		   'myspiders.imagespipelines.MyImagesPipeline': 300
		
		}
		IMAGES_STORE = 'images/'
		IMAGES_EXPIRES = 30  #过期时间为30天,30天内不会重复下载
		IMAGES_THUMBS = {
		    'big': (270, 270),
		    'small': (80, 80)
		}
		ROBOTSTXT_OBEY = False
		
	**记住一定要加上**
	
		ROBOTSTXT_OBEY = False
	
	在自定义ImagePipeline代码中，作为重要的是要重载get_media_requests(self, item, info)和item_completed(self, results, item, info)这两个函数。
	
		item_completed(self, results, item, info)：

	图片下载完毕后，处理结果会以二元组的方式返回给item_completed()函数。这个二元组定义如下：

		(success, image_info_or_failure)

	**注意**
		
		最新pyhotn3.x需要导入PL
		
		pip install -i https://pypi.douban.com/simple pillow
4. setting.py
		
			# Scrapy settings for dirbot project
			
			SPIDER_MODULES = ['dirbot.spiders']
			NEWSPIDER_MODULE = 'dirbot.spiders'
			# DEFAULT_ITEM_CLASS = 'dirbot.items.Website'
			DEFAULT_ITEM_CLASS = 'dirbot.items.TaobaoGoods'
			# DEFAULT_ITEM_CLASS = 'dirbot.items'
			
			# ##默认
			# DOWNLOAD_DELAY = 3
			# ##关闭cookie
			# COOKIES_ENABLED = False
			
			ITEM_PIPELINES = {
			    'dirbot.pipelines.FilterWordsPipeline': 1,
			    'dirbot.jsonwriterpipelines.JsonWriterPipeline': 2,
			    'dirbot.imagespipelines.MyImagesPipeline': 3
			}
			
			DEFAULT_REQUEST_HEADERS = {
			    'User-Agent': 'DYZB/1 CFNetwork/808.2.16 Darwin/16.3.0',
			}
			DOWNLOADER_MIDDLEWARES = {
			   'dirbot.middlewares.MeiZiTu': 543,
			}
		
		# ROBOTSTXT_OBEY = True
		
		# 观察代码可以发现，默认为True，就是要遵守robots.txt 的规则，那么 robots.txt 是个什么东西呢？
		#
		# 通俗来说， robots.txt 是遵循 Robot协议 的一个文件，它保存在网站的服务器中，
		# 它的作用是，告诉搜索引擎爬虫，本网站哪些目录下的网页 不希望 你进行爬取收录。
		# 在Scrapy启动后，会在第一时间访问网站的 robots.txt 文件，然后决定该网站的爬取范围。
		#
		# 当然，我们并不是在做搜索引擎，而且在某些情况下我们想要获取的内容恰恰是被 robots.txt
		# 所禁止访问的。所以，某些时候，我们就要将此配置项设置为 False ，拒绝遵守 Robot协议 ！
		
		IMAGES_STORE = 'images/'
		IMAGES_EXPIRES = 30
		
		##过滤图片
		# IMAGES_MIN_HEIGHT = 110
		# IMAGES_MIN_WIDTH = 110
		
		#配置缩略图参数
		IMAGES_THUMBS = {
		    'big': (270, 270),
		    'small': (80, 80)
		}
5. 向scrapy中的spider传递参数的几种方法


	第一种方法，在命令行用crawl控制spider爬取的时候，加上-a选项，例如：
	
	```
	scrapy crawl myspider -a category=electronics
	```
	然后在spider里这样写：
	
	```
	import scrapy
	
	class MySpider(scrapy.Spider):
	    name = 'myspider'
	
	    def __init__(self, category=None, *args, **kwargs):
	        super(MySpider, self).__init__(*args, **kwargs)
	        self.start_urls = ['http://www.example.com/categories/%s' % category]
	        # ...
	```




