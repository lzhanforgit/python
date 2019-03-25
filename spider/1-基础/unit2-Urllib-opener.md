# Handler处理器 和 自定义Opener
**作者：詹亮**


1. 介绍

  opener是 urllib.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。

  但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：

  使用相关的 Handler处理器 来创建特定功能的处理器对象；
  然后通过 urllib.build_opener()方法使用这些处理器对象，创建自定义opener对象；
  使用自定义的opener对象，调用open()方法发送请求。
  如果程序里所有的请求都使用自定义的opener，可以使用urllib.install_opener() 	将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）

2. 新建opener



   ​	

	   	from urllib import request,parse
	   	import urllib
	   	import ssl
	   	ssl._create_default_https_context = ssl._create_unverified_context
	   	# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
	   	# http_handler = request.HTTPHandler()
	   	
	   	# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
	   	http_handler = request.HTTPSHandler()
	   	
	   	# 调用request.build_opener()方法，创建支持处理HTTP请求的opener对象
	   	opener = request.build_opener(http_handler)
	   	
	   	url='https://www.liepin.com/sh/zhaopin/pn1/?' \
	   	    'd_pageSize=40&siTag=&d_headId=7523ef4c1e412df5e007f3cfd117447d&d_ckId=7523ef4c1e412df5e007f3cfd117447d&d_sfrom=' \
	   	    'search_city&'
	   	str={
	   	    "key":"python",
	   	    "d_curPage":0
	   	
	   	}
	   	#
	   	url=url+parse.urlencode(str)
	   	
	   	print(url)
	   	# 构建 Request请求
	   	request = request.Request(url)
	   	
	   	# 调用自定义opener对象的open()方法，发送request请求
	   	f = opener.open(request)
	   	
	   	# 获取服务器响应内容
	   	with open('liepin.html','w+') as fp:
	   	    fp.write(f.read().decode())

   >如果在 HTTPHandler()增加 debuglevel=1参数，还会将 Debug Log 打开，这样程序在执行的时候，会把收包和发包的报头在屏幕上自动打印出来，方便调试，有时可以省去抓包的工作。

   		https_handler = urllib2.HTTPSHandler(debuglevel=1)

3. ProxyHandler处理器（代理设置）

  使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。

  很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。

  所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

  免费的开放代理获取基本没有成本，我们可以在一些代理网站上收集这些免费代理，测试后如果可以用，就把它收集起来用在爬虫上面。

  免费短期代理网站举例：

  [西刺免费代理IP](http://www.xicidaili.com/)

  [快代理免费代理](http://www.kuaidaili.com/free/inha/)

  [Proxy360代理](http://www.proxy360.cn/default.aspx)

  [全网代理IP](http://www.goubanjia.com/free/index.shtml)


  **新建代理opener**

	  	from urllib import request,parse
	  	import urllib
	  	import ssl
	  	ssl._create_default_https_context = ssl._create_unverified_context
	  	
	  	# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
	  	httpproxy_handler = request.ProxyHandler({"http" : "110.73.1.105:8123"})
	  	nullproxy_handler = request.ProxyHandler({})
	  	
	  	proxySwitch = True #定义一个代理开关
	  	
	  	# 通过 request.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
	  	# 根据代理开关是否打开，使用不同的代理模式
	  	if proxySwitch:
	  	    opener = request.build_opener(httpproxy_handler)
	  	else:
	  	    opener = request.build_opener(nullproxy_handler)
	  	
	  	request = request.Request("http://www.baidu.com/")
	  	
	  	# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
	  	response = opener.open(request)
	  	
	  	# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
	  	# urllib2.install_opener(opener)
	  	# response = urlopen(request)
	  	print(response.read())

  如果代理IP足够多，就可以像随机获取User-Agent一样，随机选择一个代理去访问网站。

	  	proxy_list = [
	  	    {"http" : "110.73.1.105:8123"},
	  	    {"http" : "110.73.40.20:8123"},
	  	    {"http" : "124.88.67.81:80"},
	  	    {"http" : "124.88.67.81:80"},
	  	    {"http" : "124.88.67.81:80"}
	  	]
  	
  		# 随机选择一个代理
	  	proxy = random.choice(proxy_list)
	  	httpproxy_handler = request.ProxyHandler(proxy)

4. handler

	    from urllib import request
	    from urllib.error import URLError
	    
	    
	    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
	    top_level_url = 'http://localhost:8080/users/login'
	    req = request.Request(top_level_url)
	    try:
	        # 创建一个密码管理者
	        # 如果知道 realm, 我们可以使用他代替 ``None``.
	        # password_mgr.add_password(None, top_level_url, username, password)
	        password_mgr.add_password(None, top_level_url, '13812790421', '123456')
	    
	        # 创建了一个新的handler
	        handler = request.HTTPBasicAuthHandler(password_mgr)
	    
	        # 创建 "opener" (OpenerDirector 实例)
	        opener = request.build_opener(handler)
	        a_url ='http://localhost:8080/users/getAllUsers'
	    
	        # 使用 opener 获取一个URL
	        response =opener.open(a_url)
	    
	        # 安装 opener.
	        # 现在所有调用 urllib2.urlopen 将用我们的 opener.
	        urllib.install_opener(opener)
	    except URLError as e:
	        if hasattr(e, 'code'):
	            print ('The server couldn\'t fulfill the request.')
	            print ('Error code: ', e.code)
	        elif hasattr(e, 'reason'):
	            print ('We failed to reach a server.')
	            print ('Reason: ', e.reason())
	        else:
	            print (response.read())
	    
   


