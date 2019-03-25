# unit2 路由
**作者：詹亮**

1. 简单入门

	```
		@app.route('/')
		def index():
		    return 'Index Page'
		
		@app.route('/hello/')
		#路由会执行下面的第一个方法，方法名不必和路由相同
		def hello(): 
		    return 'Hello, World'
	```
	**projects端点的规范URL 具有尾部斜杠。它类似于文件系统中的文件夹。如果您访问的URL没有斜杠，则Flask会将您重定向到带有斜杠的规范URL。**
2. 路由参数

	可以通过标记部分将可变部分添加到URL <variable_name>。您的函数然后接收<variable_name> 作为关键字参数。或者，您可以使用转换器来指定参数类型<converter:variable_name>。
	
	```
		@app.route('/user/<username>')
		def show_user_profile(username): #这里不要忘了哦
	    # show the user profile for that user
	    	return 'User %s' % username
	
		@app.route('/post/<int:post_id>')
		def show_post(post_id):
		    # show the post with the given id, the id is an integer
		    return 'Post %d' % post_id
		
		@app.route('/path/<path:subpath>')
		def show_subpath(subpath):
		    # show the subpath after /path/
		    return 'Subpath %s' % subpath
	```
	
	转换器类型：

		string	（默认）接受不带斜杠的文本
		int		接受正整数
		float	接受正浮点值
		path	喜欢，string但也接受斜线
		uuid	接受UUID字符串
3. url_for

	url_for() 函数最简单的用法是以视图函数名作为参数， 返回对应的 URL。
	
	```
		@app.route('/allusers/')

		def getAllUsers():
		    return json.dumps(data)
		
		@app.route('/user/<username>')
		def show_user_profile(username):
		   #返回函数getAllUsers所对应的路由
		    s=url_for('getAllUsers')
		    #/allusers/
	```
	
		from flask import Flask, url_for
	
		app = Flask(__name__)
		
		@app.route('/')
		def index():
		    return 'index'
		
		@app.route('/login')
		def login():
		    return 'login'
		
		@app.route('/user/<username>')
		def profile(username):
		    return '{}\'s profile'.format(username)
		
		with app.test_request_context():
		    print(url_for('index'))
		    print(url_for('login'))
		    print(url_for('login', next='/'))
		    print(url_for('profile', username='John Doe'))
		
		/
		/login
		/login?next=/
		/user/John%20Doe
4. redirect

	```
		from flask import Flask,url_for,redirect
		...
		@app.route('/user/<username>')
		def show_user_profile(username):
		   #返回函数getAllUsers所对应的路由
		    s=url_for('getAllUsers')
		    #/allusers/
		    
		    #重定向到/allusers/
		    return redirect(s)
	```
	
5. 蓝图

	什么是蓝图？
	
	一个蓝图定义了可用于单个应用的视图，模板，静态文件等等的集合。
	
	我什么时候会用到蓝图？
	蓝图的杀手锏是将你的应用组织成不同的组件，比如把admin，user相关的视图方法分为两个组件，一个是admin组件，一个是user组件.这时我们可以
	
	创建两个蓝图实现这两个独立的组件.
6. 创建蓝图

	要想创建一个蓝图对象，你需要import flask.Blueprint()类并用参数name和import_name初始化。import_name通常用__name__，一个表示当前模块的特殊的Python变量，作为import_name的取值。
	
	user.py和admin.py模块
	
		from flask import Blueprint, render_template, redirect
		
		#用参数name和import_name初始化
		user = Blueprint('user',__name__)
		
		@user.route('/index')
		def index():
		    return render_template('user/index.html')
		
		@user.route('/add')
		def add():
		    return 'user_add'
		
		@user.route('/show')
		def show():
		    return 'user_show'
	---
		    
		from flask import Blueprint,render_template, request
		admin = Blueprint('admin',__name__)
		
		@admin.route('/index')
		def index():
		    return render_template('admin/index.html')
		
		@admin.route('/add')
		def add():
		    return 'admin_add'
		
		@admin.route('/show')
		def show():
		    return 'admin_show'
		    
	run.py 路由入口
	
		from flask import Flask, render_template
		from admin import admin
		from user import user
		
		app = Flask(__name__)
		
		#这里分别给app注册了两个蓝图admin,user
		#参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
		#即当request.url是以/admin或者/user的情况下才会通过注册的蓝图的视图方法处理请求并返回
		app.register_blueprint(admin,url_prefix='/admin')
		app.register_blueprint(user, url_prefix='/user')
		
		
		@app.route('/')
		def index():
		    return 'index'
		
		@app.errorhandler(404)
		def miss(e):
		    return render_template('404.html'), 404
		
		
		@app.errorhandler(500)
		def error(e):
		    return render_template('500.html'), 500


		if __name__ == '__main__':
		    print(app.url_map)
		    app.run()