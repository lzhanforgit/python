# 服务器端对象
1. request

	通过request.method可以查看提交方式
2. request 解析数据

	1. get
			
			request.environ
			request.GET
			
			#如果提交数据方式为：
			http://localhost:8080/position/12/?name=tom&pass=123
			
			获取方式：
			
			request.GET.get('name')
			request.GET['pass']
	2. post

	
		a. post数据为form-data或者x-www-urlencoded
			
			    if request.method=='POST':
			        id=request.POST.get('id')
					password=request.POST['password']
			        
			        #当客户端数据为{‘key’:[1,3,6,7]} 时（发送数据需加：traditional:true 防止深度序列化 ），
			        list=request.POST.getlist('do')
			        
			        
		b. post数据为json
		
			 if request.method=='POST':
				
				//注意，在AJAX请求是一定要把json类型转化为字符串 JSON.stringify(data)
		        data=json.loads(request.body)
				
		        id=data['id']
		        password=data['password']
2. 获取Header中的信息
			
			
	1. request.META.get("header key") 用于获取header的信息
	2. 注意的是header key必须增加前缀HTTP，同时大写，例如你的key为username，那么应该写成：request.META.get("HTTP_USERNAME")
	3. 另外就是当你的header key中带有中横线，那么自动会被转成下划线，例如my-user的写成： request.META.get("HTTP_MY_USER")


				token=request.META.get('HTTP_TOKEN')
        		print(token)

	
		
        	
	**注意post提交出错**
		
	1. url最后应该加/ 如：http://localhost:8080/position/add/
	2. settings.py中可能要注释掉：# 'django.middleware.csrf.CsrfViewMiddleware',
	**为什么要这样呢，因为django默认会验证token(每次请求django都会带回来一个token,m名字叫X-CSRFtoken).如果要顺利请求则要取出cookie中的token，然后ojax.setRequestHeader('X-CSRFtoken',token)。**
	4. cookie

			request.COOKIES：包含用户发来的所有数据，这个COOKIES就是一个字典，获			取方法有以下2种
			
			获取cookis,获取用户发来请求中的cookies
			
				request.COOKIES['username111']
				request.COOKIES.get('username111')
	4. 如果使用AJAX发送Cookie

		1. 前端

			xhrFields: {
                    withCredentials: true
                },
			
			前端方面：必须要注意的点是：浏览器的同源策略问题----》就是域名必须要一致，
			否则，ajax是不会携带非同源的cookie的。-----》怎样解决这个同源的问题呢？
			-----》如果前端同事懂的话，可以用node.js去配置代理---》如果是后台同事懂的话，可以用nginx去配置反向代理------》目的是：让域名保持一致！！！！！

		2. django 配置文件

			CORS_ALLOW_CREDENTIALS=True  //If True, cookies will be allowed to be included in cross-site HTTP requests. Defaults to False.

			参考：https://pypi.org/project/django-cors-headers/
3. HttpResponse
	1. HttpResponse(数据，状态码，cookie)

	
			from django.http import HttpResponse,response,JsonResponse
			#resp=response.HttpResponse('I AM LOGIN')
			return HttpResponse(json.dumps(content),
			status=200,charset='utf-8',content_type='application/json')

	2. cookie

			set_cookie(key, value='', max_age=None, expires=None)：设置Cookie
		1. key、value都是字符串类型
		2. max_age是一个整数，表示在指定秒数后过期
		3. expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
		4. max_age与expires二选一
		5. 如果不指定过期时间，则两个星期后过期

		
					from datetime import datetime,timedelta
					date_int=datetime.utcnow()+timedelta(hours=1)
		       	content=json.dumps({"id":"001","name":"天猫"})
		        	response = HttpResponse(content, content_type='application/json; charset=utf-8')
		
		        # response.write('<h1>' + 'ok' + '</h1>')
		        # response.set_cookie('h1', '你好', 604800)
		        # response.set_cookie('h1', '你好', max_age=None, expires=date_int)
		        response.set_cookie('h1', '你好'.encode('utf8'), expires=date_int)
		        return response
		        
		**注意**
		
			'你好'.encode('utf8')

5. JsonResponse

		from django.http import HttpResponse,response,JsonResponse
		def login(request):
		    todo_list = [
		        {"id": "1", "content": "吃饭"},
		        {"id": "2", "content": "吃饭"},
		    ]
		    response = JsonResponse(todo_list, safe=False)
4. HttpResponseRedirect

	通过HttpResponseRedirect 和 reverse实现重定向
	
		from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
		from django.urls import reverse
		
		def search(request,condition):
    		# return HttpResponse('search')
    		return HttpResponseRedirect('/position/')
    		
    还可以通过reverse()对url的name进行解析：
    
    	return HttpResponseRedirect(reverse('index'))
    
    如果指定模块（即使当前模块跳转也要写明）
    	
    	return HttpResponseRedirect(reverse('position:index'))

   了解：
   
   1.	而如果url中包含参数，如下类型的url：

		url(r'^blog/(?P<blog_id>\d+)/$', BlogDetailView.as_view(), 		name='blog_id')

	2. 如果我们还采用上述方式实现重定向，则会提示缺少一个参数：blog_id。此时需要在reverse()中添加参数：

			blog_id = blog.id   #获取到博客的id号
			return HttpResponseRedirect(reverse('index', args=(blog_id)))

	3. 如果包含多个字段，可以采用如下形式：

		url(r'^blog/(?P<blog_id>\d+)/(?P<user_id>\d+)、$', BlogDetailView.as_view(), name='blog_id')
	
		return HttpResponseRedirect(reverse('index', kwargs={'blog_id': blog_id, 'user_id': us}
		
5. 序列化
	
	关于Django中的序列化主要应用在将数据库中检索的数据返回给客户端用户，特别的Ajax请求一般返回的为Json格式。

	1. serializers(以后再说，要记得......)

			from django.core import serializers
	 
			ret = models.BookType.objects.all()
	 
			data = serializers.serialize("json", ret)
			
	2. json.dumps时无法处理datetime日期，所以可以通过自定义处理器来做扩展，如：

			import json 
			from datetime import date 
			from datetime import datetime 
			   
			class JsonCustomEncoder(json.JSONEncoder): 
			    
			    def default(self, field): 
			     
			        if isinstance(field, datetime): 
			            return o.strftime('%Y-%m-%d %H:%M:%S') 
			        elif isinstance(field, date): 
			            return o.strftime('%Y-%m-%d') 
			        else: 
			            return json.JSONEncoder.default(self, field) 
			   
			   
			# ds = json.dumps(d, cls=JsonCustomEncoder) 
3. 文件上传

		request.FILS	
		
4. 中间件
	
	中间件中可以定义五个方法，分别是：

		process_request(self,request)
		process_view(self, request, callback, callback_args, callback_kwargs)
		process_template_response(self,request,response)
		process_exception(self, request, exception)
		process_response(self, request, response)
	
	前二个方法是从前往后执行的，后三个方法是从后往前执行的
	
	
	在根目录下建立：'mymiddleware.middleware.userauth.RequestAuth'
	
	方式一：
	
		from django.http import HttpResponse
		from django.utils.deprecation import MiddlewareMixin
		class RequestAuth(MiddlewareMixin):
		    def process_request(self, request):
		        print(request.GET.get('id'))
		        print('333')
		        # return HttpResponse('sorry')
		    def process_view(self, request, callback, callback_args, callback_kwargs):
		        i = 1
		        print('444')
		        pass
		    def process_exception(self, request, exception):
		        print('555')
		        return HttpResponse(exception)
		    def process_response(self, request, response):
		        print('666')
		        return response
	
	方式二
	
		from django.http import HttpResponse
		#from django.utils.deprecation import MiddlewareMixin
		class RequestAuth(object):
		    def __init__(self, get_response):
		        print('111')
		        self.get_response = get_response
		    
		    def __call__(self, request):
		        print('222')
		        print(request.GET.get('id'))
		        return self.get_response(request)
		    def process_request(self, request):
		        print(request.GET.get('id'))
		        print('333')
		        # return HttpResponse('sorry')
		
		    def process_view(self, request, callback, callback_args, callback_kwargs):
		        i = 1
		        print('444')
		        pass
			
		    def process_exception(self, request, exception):
		        print('555')
		        return HttpResponse(exception)
		
		    def process_response(self, request, response):
		        print('666')
		        return response
		        
	这种方式def process_request(self, request):不会执行


