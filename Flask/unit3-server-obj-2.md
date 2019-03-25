# uint3 server对象
**作者：詹亮**

1. 数据加密-sha1

		import hashlib

		pwd='a123456'
		
		temp=hashlib.sha1(pwd.encode())
		
		print(temp.hexdigest())
2. hash加盐加密

	1. 导入加密函数
	
			from werkzeug.security import generate_password_hash,check_password_hash
	
	2. 密码生成函数：generate_password_hash
		
			werkzeug.security.generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
			
		参数说明：

		* password：明文密码
		* method：哈希加密的方法（需要hashlib库支持的），格式为pdpdf2:<method>[:iterations] 
		* method：哈希的方式，一般为SHA1
		* iterations：（可选参数）迭代次数，默认为1000
		* salt_length：盐值的长度，默认为8
	
		加密之后的字符串格式：

			method$salt$hash
	
	3. 密码验证函数：check_password_hash
		函数定义：
		
			werkzeug.security.check_password_hash(pwhash, password)
		参数定义：
		
		pwhash：generate_password_hash生成的哈希字符串
		password：需要验证的明文密码

		>check_password_hash函数用于验证经过generate_password_hash哈希的密		码 。若密码匹配，则返回真，否则返回假。 
3. token(jwt)

	现在很多框架都实现前后端分离，主要为了适应以下几个目的：

	1，前后端的分离，可以使前端开发和后端开发更加分工明确，而不是后端还需要在视图模板中加入很多{% XXXX %}标签
		
	2，是为了适应跨域调用或者多客户端调用，如你的手机应用调用某个接口，大都是调用第三方api等
		
	所以在整合JWT，让框架具有更多的适应性。JWT 说简单就是基于token的权限验证；flask 有提供json的支持，可是对象转化是一个大问题；
4. 什么是token

	 Json web token（JWT）是为了网络应用环境间传递声明而执行的一种基于JSON的开发标准（RFC 7519），该token被设计为紧凑且安全的，特别适用于分布式站点的单点登陆（SSO）场景。JWT的声明一般被用来在身份提供者和服务提供者间传递被认证的用户身份信息，以便于从资源服务器获取资源，也可以增加一些额外的其它业务逻辑所必须的声明信息，该token也可直接被用于认证，也可被加密。
	 
	 **流程是这样的**

	1. 用户使用用户名密码请求服务器
	1. 服务器进行验证用户信息
	1. 服务器通过验证发送给用户一个token
	1. 客户端存储token，并在每次请求时附加这个token值
	1. 服务器验证token，并返回数据
	      这个token必须要在每次请求时发送给服务器，它应该保存在请求头中，另外，服务器要支持CORS（跨来源资源共享）策略，一般我们在服务端这么做就可以了 Access-Control-Allow-Origin：*
	      
5. JWT构成

	JWT是由三部分构成，将这三段信息文本用链接构成了JWT字符串。就像这样

		eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySWQiOjEyMywiVXNlck5hbWUiOiJhZG1pbiJ9.Qjw1epD5P6p4Yy2yju3-fkq28PddznqRj3ESfALQy_U
		
	第一部分我们称它为头部（header）第二部分我们称其为载荷（payload，类似于飞机上承载的物品），第三部分是签证（signature）
	
	1. header
	
	   	JWT的头部承载的两部分信息：
	
		声明类型，这里是jwt
		声明加密的算法，通常直接使用HMAC SHA256
			
	   完整的头部就像下面这样的JSON	      
	   
	   		{
		     'typ':'JWT',
		     'alg':'HS256'  
			}
			
		然后将头部进行base64加密（该加密是可以对称解密的），构成了第一部分
	
			eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
			
	2. plyload

		载荷就是存放有效信息的地方。这个名字像是特指飞机上承载的货品，这些有效信息包含三个部分
	
		标准中注册的声明
		公共的声明
		私有的声明 
			标注中注册的声明（建议不强制使用）
			
			iss：jwt签发者
			sub：jwt所面向的用户
			aud：接收jwt的一方
			exp：jwt的过期时间，这个过期时间必须大于签发时间
			nbf：定义在什么时间之前，该jwt都是不可用的
			iat：jwt的签发时间
			jti：jwt的唯一身份标识，主要用来作为一次性token，从而回避重放攻击 
			公共的声明：
			
			公共的声明可以添加任何的信息，一般添加用户的相关信息或其它业务需要的必要信息，但不建议添加敏感信息，因为该部分在客户端可解密；
			
			私有的声明
			
			私有的声明是提供者和消费者功能定义的声明，一般不建议存放敏感信息，因为base64是对称解密的，意味着该部分信息可以归类为名文信息。
			
			定义一个payload
	
				{
				  "sub": "1234567890",
				  "name": "John Doe",
				  "admin": true
				}
	    然后将其base64加密，得到jwt的一部分
	
				eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9
	Signature
	
	    jwt的第三部分是一个签证信息，这个签证信息由三部分组成：
	
		header(base64后的)
		payload(base64后的)
		secred     
		
		这个部分需要base64加密后的header和base64加密后的payload使用“.”连接组成的字符串，然后通过header中声明的加密方式进行加secret组合加密，然后就构成了jwt的第三部分
	
	      
	
			var encodedString = base64UrlEncode(header) + '.' + base64UrlEncode(payload);
			var signature = HMACSHA256(encodedString, 'secret'); // TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
	    将这三部分用“.”连接成一个完整的字符串，构成了最终的jwt：
	
			eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ
			
	     注意：secret是保存在服务器端的，jwt的签发也是在服务端的，secret就是用来进行jwt的签发和jwt的验证，所以它就是你服务端的私钥，在任何场景都不应该流露出去，一旦客户端得知这个secret，那就意味着客户端可以自我签发jwt了
     
	3. 总结

      优点：

		因为json的通用性，所以JWT是可以跨语言支持的，像C#，JavaScript，NodeJS，PHP等许多语言都可以使用
		因为由了payload部分，所以JWT可以在自身存储一些其它业务逻辑所必要的非敏感信息
		便于传输，jwt的构成非常简单，字节占用很小，所以它是非常便于传输的
		它不需要在服务端保存会话信息，所以它易于应用的扩展
       安全相关

		不应该在jwt的payload部分存储敏感信息，因为该部分是客户端可解密的部分
		保护好secret私钥。该私钥非常重要
		如果可以，请使用https协议
		
=====
# pyjwt
	
1. 安装

			pip install pyjwt -i https://pypi.tuna.tsinghua.edu.cn/simple

2. 生成token

		import jwt
		import datetime
		import hashlib
		
		#当前时间加上180秒，意味着token过期时间为3分钟以后
		datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
		SECRECT_KEY = 'secret'
		option = {
				  'iss':'jobapp.com', #token的签发者
		        'exp':datetimeInt, #过期时间
		        ‘iat’:datetime.datetime.utcnow(),
		        'aud': 'webkit',   #token的接收者，这里指定为浏览器
		        'user_id': '001'   #放入用户信息，唯一标识，解析后可以使用该消息
		    }
		# encoded2 = jwt.encode(payload=option,key= SECRECT_KEY, algorithm='HS256',options= {'verify_exp':True})
		#这时token类型为字节类型，如果传个前端要进行token.decode()
		token = jwt.encode(option,SECRECT_KEY, 'HS256')
		print(token)
		
3. 解析token

		decoded = jwt.decode(token, SECRECT_KEY,audience='webkit', algorithms=['HS256'])

		print(decoded)
		
4. 代码封装

			
			# 生成jwt 信息
			def  jwtEncoding(some,aud='webkit'):
			    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
			    print(datetimeInt)
			    option = {
			        'exp':datetimeInt,
			        'aud': aud,
			        'some': some
			    }
			    encoded2 = jwt.encode(option, SECRECT_KEY, algorithm='HS256')
			    return encoded2
			    
			# 解析jwt 信息
			def  jwtDecoding(token,aud='webkit'):
			    decoded = None
			    try:
			        decoded = jwt.decode(token, SECRECT_KEY, audience=aud, algorithms=['HS256'])
			    except jwt.ExpiredSignatureError :
			        print("erroing.................")
			        decoded = {"error_msg":"is timeout !!","some":None}
			    except Exception:
			        decoded ={"error_msg":"noknow exception!!","some":None}
			        print("erroing2.................")
			    return decoded
			    
5. 代码中可以把解析token放在方法装饰器中


		from functools import wraps
		import jwt
		import datetime
		#因为调用装饰器代码在接口外面，这是时候你不能使用request对象。
		from flask import Blueprint,request 
		datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
		SECRECT_KEY = 'secret'
		def checkToken(*request):
		    def decorated(func):
		        @wraps(func)
		        def wrapper():
		            print("[DEBUG]: enter {}()".format(func.__name__))
		            try:
		            		#获取用户请求数据中token
		                token=request.headers['token']
		                print('token 是：')
		                print(token)
		                #解析token
		                decoded = jwt.decode(token, SECRECT_KEY, audience='webkit', algorithms=['HS256'])
		                #能执行到这个地方，说明解析成功。接下来执行请求的接口
		                return func(decoded['telephone'])
		                
		            #如果解析出错，调用异常处理模块
		            except jwt.ExpiredSignatureError as err:
		            <!--不需要进入路由接口，直接返回数据给前端-->
		               	  return json.dumps({"status_code": "10007", "status_text": "未登录...."})

		            except Exception:
		               	 return json.dumps({"status_code": "10007", "status_text": "未登录...."})

		
		        return wrapper
		
		    return decorated
		
		
		def jwtEncoding(some, aud='webkit'):
		    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
		    print(datetimeInt)
		    option = {
		        'iss': 'jobapp.com',
		        'exp': datetimeInt,
		        'aud': 'webkit',
		        'some':some
		    }
		    encoded2 = jwt.encode(option, SECRECT_KEY, algorithm='HS256')
		    print(encoded2.decode())
		    return encoded2.decode()
		
		if __name__ == '__main__':
		    res=jwtEncoding('{"userid","889"}')
		
		    print(res)
		
	在路由方法中调用
	
		@resume_app.route('/add')  #/user/add
		@checkToken()  #此处需要用户权限调用
		#@checkToken(request)  #此处需要用户权限调用
		def add():
		    return '添加简历'