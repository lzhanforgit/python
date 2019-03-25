# uint3 server对象
**作者：詹亮**

1. request
	1. method 属性
	
		```
			from flask import request
	
			@app.route('/login', methods=['GET', 'POST'])
			def login():
			    if request.method == 'POST':
			        return do_the_login()
			    else:
			        return show_the_login_form()
		```
	
	2. form 属性
	
		```
			@app.route('/login', methods=['POST', 'GET'])
			def login():
			    error = None
			    if request.method == 'POST':
			        if valid_login(request.form['username'],
			                       request.form['password']):
			            return log_the_user_in(request.form['username'])
			        else:
			            error = 'Invalid username/password'
			    # the code below is executed if the request method
			    # was GET or the credentials were invalid
			    return render_template('login.html', error=error)
		```
		
		form的enctype属性为编码方式，常用有两种：application/x-www-form-urlencoded和multipart/form-data，默认为application/x-www-form-urlencoded。
	
		1. x-www-form-urlencoded
		
			当action为get时候，浏览器用x-www-form-urlencoded的编码方式把form数据转换成一个字串（name1=value1&name2=value2…），然后把这个字串append到url后面，用?分割，加载这个新的url。
			
		2. multipart/form-data
		
			当action为post时候，浏览器把form数据封装到http body中，然后发送到server。 如果没有type=file的控件，用默认的application/x-www-form-urlencoded就可以了。 但是如果有type=file的话，就要用到multipart/form-data了。浏览器会把整个表单以控件为单位分割，并为每个部分加上Content-Disposition(form-data或者file),Content-Type(默认为text/plain),name(控件name)等信息，并加上分割符(boundary)。
			
		>enctype="multipart/form-data"是上传二进制数据;它告诉我们传输的数据要用到多媒体传输协议，由于多媒体传输的都是大量的数据，所以规定上传文件必须是post方法
	3. args 属性
	
		
		获取get路由中的数据
		要访问在URL（?key=value）中提交的参数，您可以使用 args属性：
		
		```
		searchword = request.args.get('key', '')
		#request.query_string
		#request.args['id']
		```
	4. values 属性
	
		一个werkzeug.datastructures.CombinedMultiDict结合 args和form。
		
		```
			request.values
		```
	4. url 属性
	
		request.url			获取当前请求的完整路径，包括查询字符串
		
		request.base_url		获取基本路径
	5. json 属性和get_json(),get_data()
	
		```
			        if request.is_json:
			            json_data=request.get_json()
			            print(json_data['userid'])
			        else:
			        	#当ajax提交数据不是json类型是默认是bytes
			        	#将bytes数据转化为dict
			            data=str(request.get_data(),encoding='utf-8')
			            dict_data=eval(data)
			            print(dict_data['userid'])
		```
		>如果前端提交的数据为表单（类型为form-data和application/x-www-form-urlencoded）,则可以使用request.form或者request.values
		
	5. 提交数据的方式

		1. get
			通过url: url?key=value&key2=value2
			数据编码：x-www-form-urlencoded
			数据类型（data-type）:application/text
		2. post

			1. form-data

				数据编码：字节码
			2. x-www-form-urlencoded
			3. text/plain
			3. json
				
				数据类型（data-type）:application/json
				
			
	6. headers 属性
	
		```
			request.headers['token']
		```
2. response

	方法或属性	描述
	
	1. headers		#response服务器传输数据包的头部
	2. status	
	3. status_code	 #服务器的状态码（常用200，404，500）
	4. data			#response的body,就是 return  ‘success’   ==response.data='success'
	5. get_json(force=False, silent=False, cache=True)
	6. is_json	
	7. max_cookie_size	
	8. mimetype	
	9. set_cookie(key, value=”, max_age=None, expires=None, path=’/’, domain=None, secure=False, httponly=False, samesite=None)
	
	
			from flask import Flask, json, make_response
			app = Flask(__name__)
			
			@app.route('/1')
			def hello1():
			    return 'Hello'#当只有一个字符串返回，会自动转换为状态码为200， MIME 类型是text/html的response对象
			
			@app.route('/2')
			def hello11():
			    test={'key1':'value1','key2':'value2'}
			    return json.dumps(test)#返回json格式文件
			
			@app.route('/3')
			def hello2():
			    return 'Hello3',200,{"key":"value"}#当返回多个字段时,会智能对照,MIME 类型是text/html的response对象,字典里的东西会被当成headers
			
			@app.route('/4')
			def hello3():
			 rsp = make_response('hello4') #这个方法生成了一个response对象
			 rsp.mimetype = 'text/plain'
			 rsp.headers['key'] = 'value'
			 rsp.set_cookie('user','wang')#这个值可以用接下来访问的request.cookies来取得
			 rsp.data='返回的内容'
			 return rsp #使用make_response来处理response
			
			if __name__ == '__main__':
			    app.run(debug=True)
	**return 语句的格式为 return body,statuscode,headers**
4. **请求拦截**

			
			@app.before_request
			def all():
			    print('必须经过这里')
			    
			
			
			
			
			@app.after_request
			def after_request(response):
			    print('请求结束的时候')
			    #通常这里用来解决跨域的问题
			    
				response.headers.add('Access-Control-Allow-Origin', '*')
		       if request.method == 'OPTIONS':
		            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
		            headers = request.headers.get('Access-Control-Request-Headers')
		            if headers:
		                response.headers['Access-Control-Allow-Headers'] = headers
		        return response
			    
5. jsonify和json.dumps的区别

	jsonify的作用实际上就是将我们传入的json形式数据序列化成为json字符串，作为响应的body，并且设置响应的Content-Type为application/json，构造出响应返回至客户端。
	
	而使用json.dumps时该字段值为text/html。
7. session
	1. 在flask项目中，Session, Cookies以及一些第三方扩展都会用到SECRET_KEY值，这是一个比较重要的配置值。
	
			app = Flask(__name__)
			app.config['SECRET_KEY'] = '123456'
			# or
			app.secret_key = '123456'
			# or
			app.config.update(SECRET_KEY='123456')	
		如果需要设置一个随机的SECRET_KEY值。我们可以使用os模块的urandom函数来获得随机值。
	
			import os
			byte_str=os.urandom(12)	  #12表示产生的字节数量

	
		>secret_key设置成os.urandom(12)这样的写法再项目中不合适，因为没次启动服务器这个值都会改变，所以所有保存的session都失效。现在只是学习阶段，所以就可以随机产生。
	
	2. 设置session过期时间
		
			#开启session持久化存储
			session.permanent = True
			#app.permanent_session_lifetime = timedelta(seconds=1)
			app.permanent_session_lifetime = timedelta(hours=1)
			#这个uid就会用app.secret_key = '123456'来进行加密，然后会通过cookie发送到客户端
			session['uid'] = '1'
		
		启用 permanent 之后 session lifetime 才会被应用，否则 session 在浏览器关闭时过期（在浏览器端就是 cookies 过期）；
		
	3. 获取session
			
			from flask import session
			session.get('uid')
			
	4. 删除session

			session.clear()
	
	
6. cookie

	服务器要识别来自同一个用户的请求 依赖与cookie 访问者在第一次请求 服务器的时候 服务器会在其cookie中 设置唯一的sessionId值 服务器就可以通过唯一的sessionid来去区分不同用户的请求(访问)

	需要使用secret_key 进行加密

	1. 主体结构


			Response.set_cookie(
			    key,
			    value,
			    max_age=None,设置过期时间 单位为秒
			    expires=None,以秒为单位的寿命
			    path = '/'
			)
	2. 设置cookie 存活时间为当期浏览结束
			
			from flask import Blueprint, render_template, redirect,session,make_response
			#设置cookie 不设置过期时间
			@app.route('/set_cookie/')
			def setCookie():
			    res = make_response('设置cookie')
			    res.set_cookie('name','zhangsan')
			    return res
	3. 设置cookie并设置过期时间

			#设置cookie 并设置过期时间
			@app.route('/set_cookie/')
			def setCookie():
			    res = make_response('设置cookie')
			    # res.set_cookie('name','zhangsan',max_age=60) #设置当期cookie存活时间为1分钟
			    life_time = time.time()+60
			    res.set_cookie('name','zhangsan',expires=life_time) #设置当期cookie存活时间为1分钟
			    return res
			    
	4. 获取cookie

			#查看cookie
			@app.route('/get_cookie/')
			def get_cookie():
			    myCookie = request.cookies #获取所有cookie
			    print(myCookie)
			    return 'key为name的值为{}'.format(myCookie.get('name'))
	5. 删除cookie

			#删除cookie
			@app.route('/del_cookie/')
			def del_cookie():
			    res = make_response('删除cookie')
			    res.delete_cookie('name') #删除key为name的cookie
			    return res
			    
			    
	案例 
	
		设置Cookie
		
		@user.route('/login')
		def login():
		    session.permanent = True
		    app.permanent_session_lifetime = timedelta(seconds=120)
		    session['flag']='yes'
		    session['uid']='0008'
		    session['token']='这个是令牌'
		    response=make_response()
		    life_time = time() + 60
		    response.set_cookie('name', 'zhangsan', expires=life_time)  # 设置当期cookie存活时间为1分钟
		    return 'ok yes!!'
7. 跨域
    跨域提交方式只能是get
    
    ```
    	pip install flask_cors
    ```
    ```
        from flask_cors import *
        app = Flask(__name__)
        CORS(app, supports_credentials=True)
    ```
    
    ```
    	response.headers['Access-Control-Allow-Origin'] = '*'
    	response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    	response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    ```