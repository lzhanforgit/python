# 服务器端对象-跨域请求
1. 在接口函数中配置

		from django.http import HttpResponse,response,JsonResponse
		def login(request):
		    todo_list = [
		        {"id": "1", "content": "吃饭"},
		        {"id": "2", "content": "吃饭"},
		    ]
		    response = JsonResponse(todo_list, safe=False)
		    response["Access-Control-Allow-Origin"] = "*"
		    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
		    response["Access-Control-Max-Age"] = "1000"
		    response["Access-Control-Allow-Headers"] = "*"
		    return response

1. 安装CORS

		pip install django-cors-headers
2. 添加app

		INSTALLED_APPS = (
		    ...
		    'corsheaders',
		    ...
		)
3. 添加中间件

		MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
		    ...
		    'corsheaders.middleware.CorsMiddleware',
		    'django.middleware.common.CommonMiddleware',
		    ...
		]
		
4. 配置允许跨站访问本站

	1. 配置允许跨站访问本站的地址

			CORS_ORIGIN_ALLOW_ALL = False
			CORS_ORIGIN_WHITELIST = (
			      'localhost:63343',
			)
			
			# 默认值是全部:
			CORS_ORIGIN_WHITELIST = ()  # 或者定义允许的匹配路径正则表达式.
			
			CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+.)?>google.com$', )   # 默认值:
			
			CORS_ORIGIN_REGEX_WHITELIST = ()
			
	2. 设置允许访问的方法

			CORS_ALLOW_METHODS = (
			'GET',
			'POST',
			'PUT',
			'PATCH',
			'DELETE',
			'OPTIONS'
			)
			
	3. 设置允许的header：

			默认值:
			
			CORS_ALLOW_HEADERS = (
			'x-requested-with',
			'content-type',
			'accept',
			'origin',
			'authorization',
			'x-csrftoken',
			#当客户端通过header提交数据，比如token字段是，需要加上字段名。比如
			'token'
			)
5. ajax获取token

	###前端ajax代码
	
		 $.ajax(
                {
                    url:'http://localhost:8000/user/login/',
                    type:"POST",
                    data:user,
                    dataType:"json",
                    contentType:"application/json",
                    success:function (response,textStatus,request) {

                        console.log(response)
                        console.log(textStatus)
                        console.log(request.getAllResponseHeaders())
                    },
                    error:function (XMLHttpRequest,textStatus,errorThrown) {
                        console.log('nononon')
                        console.log(textStatus)
                    }

                }
            )
    **request.getAllResponseHeaders()负责取出数据**
    
    **但是不行啊，原因**
    
    1：W3C的 xhr 标准中做了限制，规定客户端无法获取 response 中的 Set-Cookie、Set-Cookie2这2个字段，无论是同域还是跨域请求；

	2：W3C 的 cors 标准对于跨域请求也做了限制，规定对于跨域请求，客户端允许获取的response header字段只限于“simple response header”和“Access-Control-Expose-Headers” ，在“Access-Control-Allow-Headers”中加了无效

	"simple response header"包括的 header 字段有：Cache-Control,Content-Language,Content-Type,Expires,Last-Modified,Pragma;
	
	"Access-Control-Expose-Headers"：首先得注意是"Access-Control-Expose-Headers"进行跨域请求时响应头部中的一个字段，对于同域请求，响应头部是没有这个字段的。这个字段中列举的 header 字段就是服务器允许暴露给客户端访问的字段。

    
   ###服务器端代码
   	
   			resp['token'] = '8888888888888'
       	resp["Access-Control-Expose-Headers"] = "token"