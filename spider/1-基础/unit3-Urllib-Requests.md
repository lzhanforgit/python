# Requests
**作者：詹亮**


1. 介绍

	Requests 继承了urllib的所有特性。Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。

requests 的底层实现其实就是 urllib3

Requests的文档非常完备，中文文档也相当不错。Requests能完全满足当前网络的需求，支持Python 2.6—3.5，而且能在PyPy下完美运行。

[开源地址](https://github.com/kennethreitz/requests)

[中文文档 API](http://docs.python-requests.org/zh_CN/latest/index.html)

2. 安装

		pip install requests
	
3. get请求

		import requests

		url='https://www.liepin.com/sh/zhaopin/pn1/?' \
		    'd_pageSize=40&siTag=&d_headId=7523ef4c1e412df5e007f3cfd117447d&d_ckId=7523ef4c1e412df5e007f3cfd117447d&d_sfrom=' \
		    'search_city&'
		qs={
		    "key":"python",
		    "d_curPage":0
		
		}
		
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
		# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
		response = requests.get(url, params = qs, headers = headers)
		
		# 查看响应内容，response.text 返回的是Unicode格式的数据
		print(response.text)
		# 查看响应内容，response.content返回的字节流数据
		print(response.content.decode('gbk'))
		
		# 查看完整url地址
		print(response.url)
		
		# 查看响应头部字符编码
		print(response.encoding)
		
	### 解决乱码
	
		response.encoding=response.apparent_encoding
		
		# 查看响应码
		print(response.status_code)
		#查看以一个 Python 字典形式展示的服务器响应头
		
		print(response.headers)
	
	>但是这个字典比较特殊：它是仅为 HTTP 头部而生的。根据 RFC 2616， HTTP 头部是大小写不敏感的。

	因此，我们可以使用任意大写形式来访问这些响应头字段：
	
		r.headers['Content-Type']
		r.headers.get('content-type')
	
3. post 请求

		response = requests.post（url, data = data,headers=headers)
	
	如果是json文件可以直接显示
	
		print(response.json())
	
	>如果 JSON 解码失败， r.json() 就会抛出一个异常。例如，响应内容是 401 (Unauthorized)，尝试访问 r.json() 将会抛出 ValueError: No JSON object could be decoded 异常。

	>需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。这种 JSON 会被解码返回。要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。
	
4. 代理
	
	使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。

  	很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。

  	所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

  	免费的开放代理获取基本没有成本，我们可以在一些代理网站上收集这些免费代理，测试后如果可以用，就把它收集起来用在爬虫上面。

  	免费短期代理网站举例：

  [西刺免费代理IP](http://www.xicidaili.com/)

  [快代理免费代理](http://www.kuaidaili.com/free/inha/)

  [Proxy360代理](http://www.proxy360.cn/default.aspx)

  [全网代理IP](http://www.goubanjia.com/free/index.shtml)
	如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求
	
		import requests
	
		# 根据协议类型，选择不同的代理
		proxies = {
		  "http": "http://12.34.56.79:9527",
		  "https": "http://12.34.56.79:9527",
		}
		
		response = requests.get("http://www.baidu.com", proxies = proxies)
		print response.text
	
5. 处理HTTPS请求 SSL证书验证

	要想检查某个主机的SSL证书，你可以使用 verify 参数（也可以不写）
	
		import requests
		response = requests.get("https://www.baidu.com/", verify=True)
		
		# 也可以省略不写
		# response = requests.get("https://www.baidu.com/")
		print(r.text)
		
6. Cookies 和 Session

	1. cookies

		如果一个响应中包含了cookie，那么我们可以利用 cookies参数拿到：


			import requests
			
			response = requests.get("http://www.baidu.com/")
			
			# 7. 返回CookieJar对象:
			cookiejar = response.cookies
			
			# 8. 将CookieJar转为字典：
			cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
			
			print cookiejar
			
			print cookiedict
			运行结果：
			
			<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
			
			{'BDORZ': '27315'}
			
		如果准备发送一个cookies给服务器 
		
			response = requests.get("http://www.baidu.com/",cookies={'BDORZ': '27318'})
	2. Session

		在 requests 里，session对象是一个非常常用的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。
		
		会话能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 cookie 。
		
		模拟人人网登录
		
			import requests

			# 1. 创建session对象，可以保存Cookie值
			ssion = requests.session()
			
			# 2. 处理 headers
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
			
			# 3. 需要登录的用户名和密码
			data = {"email":"13812790420", "password":"zl321324"}
			
			# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
			ssion.post("http://www.renren.com/PLogin.do", data = data)
			
			# 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
			response = ssion.get("http://www.renren.com/969803141/profile")
			
			# 6. 打印响应内容
			print(response.text)
		
		
		模拟豆瓣登录。然后查看个人日志
		
			import requests
			s = requests.Session()
			# 登录接口
			url_login = 'https://accounts.douban.com/login'
			# 登录后查看日志
			url_note = 'https://www.douban.com/note/707553111/'
			
			formdata = {
			    'source': 'index_nav',
			    'redir': 'https://www.douban.com',
			    'form_email': '13812790420',
			    'form_password': '321324',
			    'login': u'登录'
			}
			headers = {
			    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
			
			r = s.post(url_login, data=formdata, headers=headers)
			
			response=s.get(url_note)
			
			print(response.text)
			