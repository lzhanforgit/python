# Urllib基础
**作者：詹亮**

1. urlopen()

    在python2.x版本中可以直接使用import urllib来进行操作，但是python3.x版本中使用的是import urllib.request来进行操作

    ```
    from urllib import request
    
    with request.urlopen('http://localhost:8080/spider-test.html') as f:
        data = f.read()
        #f.status 状态码，f.reason 
        print('Status:', f.status, f.reason) #Status: 200 OK
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))
    ```

       

2. get请求

    如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
     >浏览器 就是互联网世界上公认被允许的身份，如果我们希望我们的爬虫程序更像一个真实用户，那我们第一步，就是需要伪装成一个被公认的浏览器。用不同的浏览器在发送请求的时候，会有不同的User-Agent头。 urllib2默认的User-Agent头为：Python-urllib/x.y（x和y是Python主版本和次版本号,例如 Python-urllib/3.6）

    ```
    from urllib import request
    
    req = request.Request('http://localhost:8080/spider-test.html')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    ```

3. 随机添加/修改User-Agent

		   ​	from urllib import request
		   ​	
		   ​	import random
	
	   	#IE 9.0 的 User-Agent，包含在 ua_header里
	   	
	   	ua_list = [
	   	    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
	   	    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
	   	    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
	   	    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
	   	]
	   	
	   	user_agent = random.choice(ua_list)
	   			
	   	ua_header = {"User-Agent" : user_agent}
	   	
	   	req=request.Request(url,headers=ua_header)
	   	#获得请求方法 get
	   	print(req.get_method())
	   	#获取请求url
	   	print(req.get_full_url())
	   	
	   	with request.urlopen(req) as f:
	   	    data = f.read()
	   	    print('Status:', f.status, f.reason)
	   	    for k, v in f.getheaders():
	   	        print('%s: %s' % (k, v))
	   	    print('Data:', data.decode('utf-8'))

4. get提交数据-urlencode()

   ```
   from urllib import request,parse
   
   #当前urllib放在在parse模块中
   query={"q":"python","id":"001"}
   query=parse.urlencode(query)
   ...
   url='http://www.bootcss.com/'+'?'+query
   ```


5. 案例：批量爬取淘宝数据

  **解决https无法爬取的问题**

		  	import ssl
		  	ssl._create_default_https_context = ssl._create_unverified_context
		  	
		  	#解决url中有中文的问题
		  	from urllib import parse
		  	import string
		  	url='https://s.taobao.com/search?q=手机&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=' \
		  	        'tbindexz_20170306&p4ppushleft=5%2C48&'
		  	
		  	url=parse.quote(url,safe=string.printable)
		
		
		  ​	
		  	print(url)
	
	    	url = "https://s.taobao.com/list?spm=a217f.8051907.312344.2.7e383308OlmjDv&q=T%E6%81%A4&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&"

3. post请求

    如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

    我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
    
    ```
    from urllib import request, parse

    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    
    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    ```
    
    >关于user-agent
    >http://www.fynas.com/ua
    
7. AJAX请求json数据

  如果网站采用c/s模式，那么页面数据是返回json这个时候，我们要找到该页面后台接口地址，然后手动去爬取数据。

  具体查看数据方式为：chrome-->检查->network-->找到json文件（可以根据页面内容利用左面的搜索框搜索哦）-->点击右面的preview预览-->点击右面的headers查看地址然后给爬虫爬取。
  ajax请求数据都是XMLHttpRequest对象请求的，我们可以直接通过XHR筛选出文件（search_subjects?type.....）

	  	from urllib import request,parse
	  	import urllib
	  	import ssl
	  	ssl._create_default_https_context = ssl._create_unverified_context
	  	# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
	  	# https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
	  	url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%' \
	  	    '83%AD%E9%97%A8&sort=recommend&'
	  	headers={"User-Agent": "Mozilla...."}
	  	
	  	# 变动的是这两个参数，从start开始往后显示limit个
	  	formdata = {
	  	    'page_limit':20,
	  	    'page_start':20*8
	  	}
	  	data = parse.urlencode(formdata).encode()
	  	
	  	url=url+data.decode()
	  	
	  	req = request.Request(url, headers = headers)
	  	
	  	response = request.urlopen(req)
	  	
	  	print(response.read().decode())

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
	
	    
	

5. 异常处理

	URLError 产生的原因主要有：

	* 没有网络连接
	* 服务器连接失败
	* 找不到指定的服务器

	HTTPError
	
	HTTPError是URLError的子类，我们发出一个请求时，服务器上都会对应一个response应答对象，其中它包含一个数字"响应状态码"。

	如果urlopen或opener.open不能处理的，会产生一个HTTPError，对应相应的状态码，	HTTP状态码表示HTTP协议所返回的响应的状态。

	注意，urllib2可以为我们处理重定向的页面（也就是3开头的响应码），100-299范围的	号码表示成功，所以我们只能看到400-599的错误号码。
	
		try:
		    pass
		except error.HTTPError as err:
		    pass
		except error.URLError as err:
		    pass
		except Exception as err:
		    pass

6. HTTP响应状态码参考：

   1xx:信息
   
		   ​	100 Continue
		   ​	服务器仅接收到部分请求，但是一旦服务器并没有拒绝该请求，客户端应该继续发送其余的请求。
		   ​	101 Switching Protocols
		   ​	服务器转换协议：服务器将遵从客户的请求转换到另外一种协议。


   ​	
   ​	
   	2xx:成功
   	
	   	200 OK
	   	请求成功（其后是对GET和POST请求的应答文档）
	   	201 Created
	   	请求被创建完成，同时新的资源被创建。
	   	202 Accepted
	   	供处理的请求已被接受，但是处理未完成。
	   	203 Non-authoritative Information
	   	文档已经正常地返回，但一些应答头可能不正确，因为使用的是文档的拷贝。
	   	204 No Content
	   	没有新文档。浏览器应该继续显示原来的文档。如果用户定期地刷新页面，而Servlet可以确定用户文档足够新，这个状态代码是很有用的。
	   	205 Reset Content
	   	没有新文档。但浏览器应该重置它所显示的内容。用来强制浏览器清除表单输入内容。
	   	206 Partial Content
	   	客户发送了一个带有Range头的GET请求，服务器完成了它。


   ​	
   ​	
   	3xx:重定向
   	
	   	300 Multiple Choices
	   	多重选择。链接列表。用户可以选择某链接到达目的地。最多允许五个地址。
	   	301 Moved Permanently
	   	所请求的页面已经转移至新的url。
	   	302 Moved Temporarily
	   	所请求的页面已经临时转移至新的url。
	   	303 See Other
	   	所请求的页面可在别的url下被找到。
	   	304 Not Modified
	   	未按预期修改文档。客户端有缓冲的文档并发出了一个条件性的请求（一般是提供If-Modified-Since头表示客户只想比指定日期更新的文档）。服务器告诉客户，原来缓冲的文档还可以继续使用。
	   	305 Use Proxy
	   	客户请求的文档应该通过Location头所指明的代理服务器提取。
	   	306 Unused
	   	此代码被用于前一版本。目前已不再使用，但是代码依然被保留。
	   	307 Temporary Redirect
	   	被请求的页面已经临时移至新的url。


   ​	
   ​	
   	4xx:客户端错误
	   	
	   	400 Bad Request
	   	服务器未能理解请求。
	   	401 Unauthorized
	   	被请求的页面需要用户名和密码。
	   	401.1
	   	登录失败。
	   	401.2
	   	服务器配置导致登录失败。
	   	401.3
	   	由于 ACL 对资源的限制而未获得授权。
	   	401.4
	   	筛选器授权失败。
	   	401.5
	   	ISAPI/CGI 应用程序授权失败。
	   	401.7
	   	访问被 Web 服务器上的 URL 授权策略拒绝。这个错误代码为 IIS 6.0 所专用。
	   	402 Payment Required
	   	此代码尚无法使用。
	   	403 Forbidden
	   	对被请求页面的访问被禁止。
	   	403.1
	   	执行访问被禁止。
	   	403.2
	   	读访问被禁止。
	   	403.3
	   	写访问被禁止。
	   	403.4
	   	要求 SSL。
	   	403.5
	   	要求 SSL 128。
	   	403.6
	   	IP 地址被拒绝。
	   	403.7
	   	要求客户端证书。
	   	403.8
	   	站点访问被拒绝。
	   	403.9
	   	用户数过多。
	   	403.10
	   	配置无效。
	   	403.11
	   	密码更改。
	   	403.12
	   	拒绝访问映射表。
	   	403.13
	   	客户端证书被吊销。
	   	403.14
	   	拒绝目录列表。
	   	403.15
	   	超出客户端访问许可。
	   	403.16
	   	客户端证书不受信任或无效。
	   	403.17
	   	客户端证书已过期或尚未生效。
	   	403.18
	   	在当前的应用程序池中不能执行所请求的 URL。这个错误代码为 IIS 6.0 所专用。
	   	403.19
	   	不能为这个应用程序池中的客户端执行 CGI。这个错误代码为 IIS 6.0 所专用。
	   	403.20
	   	Passport 登录失败。这个错误代码为 IIS 6.0 所专用。
	   	404 Not Found
	   	服务器无法找到被请求的页面。
	   	404.0
	   	没有找到文件或目录。
	   	404.1
	   	无法在所请求的端口上访问 Web 站点。
	   	404.2
	   	Web 服务扩展锁定策略阻止本请求。
	   	404.3
	   	MIME 映射策略阻止本请求。
	   	405 Method Not Allowed
	   	请求中指定的方法不被允许。
	   	406 Not Acceptable
	   	服务器生成的响应无法被客户端所接受。
	   	407 Proxy Authentication Required
	   	用户必须首先使用代理服务器进行验证，这样请求才会被处理。
	   	408 Request Timeout
	   	请求超出了服务器的等待时间。
	   	409 Conflict
	   	由于冲突，请求无法被完成。
	   	410 Gone
	   	被请求的页面不可用。
	   	411 Length Required
	   	"Content-Length" 未被定义。如果无此内容，服务器不会接受请求。
	   	412 Precondition Failed
	   	请求中的前提条件被服务器评估为失败。
	   	413 Request Entity Too Large
	   	由于所请求的实体的太大，服务器不会接受请求。
	   	414 Request-url Too Long
	   	由于url太长，服务器不会接受请求。当post请求被转换为带有很长的查询信息的get请求时，就会发生这种情况。
	   	415 Unsupported Media Type
	   	由于媒介类型不被支持，服务器不会接受请求。
	   	416 Requested Range Not Satisfiable
	   	服务器不能满足客户在请求中指定的Range头。
	   	417 Expectation Failed
	   	执行失败。
	   	423
	   	锁定的错误。


   ​	
   ​	
   	5xx:服务器错误
   	
	   	500 Internal Server Error
	   	请求未完成。服务器遇到不可预知的情况。
	   	500.12
	   	应用程序正忙于在 Web 服务器上重新启动。
	   	500.13
	   	Web 服务器太忙。
	   	500.15
	   	不允许直接请求 Global.asa。
	   	500.16
	   	UNC 授权凭据不正确。这个错误代码为 IIS 6.0 所专用。
	   	500.18
	   	URL 授权存储不能打开。这个错误代码为 IIS 6.0 所专用。
	   	500.100
	   	内部 ASP 错误。
	   	501 Not Implemented
	   	请求未完成。服务器不支持所请求的功能。
	   	502 Bad Gateway
	   	请求未完成。服务器从上游服务器收到一个无效的响应。
	   	502.1
	   	CGI 应用程序超时。　·
	   	502.2
	   	CGI 应用程序出错。
	   	503 Service Unavailable
	   	请求未完成。服务器临时过载或当机。
	   	504 Gateway Timeout
	   	网关超时。
	   	505 HTTP Version Not Supported
	   	服务器不支持请求中指明的HTTP协议版本