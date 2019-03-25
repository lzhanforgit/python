# spider-页面解析-CSS
**作者：詹亮**


## BeautifulSoup4
3. CSS 选择器：BeautifulSoup4

	lxml 只会局部遍历，而Beautiful Soup 是基于HTML DOM的，会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml。

	BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器。

	Beautiful Soup 3 目前已经停止开发，推荐现在的项目使用Beautiful Soup 4。使用 pip 安装即可：pip install beautifulsoup4
	
	1. 安装

			pip install beautifulsoup4
	2. tag (可以使用文档对象直接.标签名获取)

			from bs4 import BeautifulSoup

			# html='....'
			#创建 Beautiful Soup 对象
			# soup = BeautifulSoup(html)
			
			#打开本地 HTML 文件的方式来创建对象
			soup = BeautifulSoup(open('data.xml'),"lxml")
			
			#格式化输出 soup 对象的内容
			# print(soup.prettify())
			print(soup.book) 
		
		>我们可以利用 soup 加标签名轻松地获取这些标签的内容，这些对象的类型是bs4.element.Tag。但是注意，它查找的是在所有内容中的第一个符合要求的标签。
print(soup.book)
	3. 对于 Tag，它有两个重要的属性，是 name 和 attrs

			from bs4 import BeautifulSoup
			
			# html='....'
			#创建 Beautiful Soup 对象
			# soup = BeautifulSoup(html)
			
			#打开本地 HTML 文件的方式来创建对象
			soup = BeautifulSoup(open('liepin.html'),"lxml")
			
			#格式化输出 soup 对象的内容
			# print(soup.prettify())
			
			nodes=soup.select('div.company-info p a')
			
			nodes=soup.select('div#div01 div.company-info > p[name="pr"] a')
			
			for node in nodes:
			    #获取节点名称
			    print(node.name)
			
			    #获取节点所有属性
			    print(node.attrs)
			
			    #获取节点href属性的值
			    print(node['href'])
			    # print(node.get('href'))

			    
			    #获取节点的值
			    print(node.string)		

		
	
