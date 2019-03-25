#unit5 mysql- SQLAlchemy
**作者：詹亮**

http://www.pythondoc.com/flask-sqlalchemy/quickstart.html
1. 安装

		pip install Flask-SQLAlchemy
	
2. 使用SQLAlchemy创建表

	1. 新建models包__init__.py配置
			
			#导入SQLAlchemy模块
			from flask_sqlalchemy import SQLAlchemy
			
			#导入应用对象,代码在下面有
			from app import app
			db = SQLAlchemy()
			
			#将当app对象加入上下文
			app.app_context().push()
			print('models app is{}'.format(id(app)))
			
			配置连接数据库
			app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
			app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@127.0.0.1:3306/pythondb'
			#初始化连接，此时会默认生成一个数据库连接池，里面有很多连接对象session
			#可以使用语句db.session
			db.init_app(app)
			
			
		app.py
		
			from flask import Flask
			app=Flask(__name__)
			
	2. model
			
			#.表示当前包的__init__模块
			from . import db
			class Person(db.Model):
			    id = db.Column(db.Integer, primary_key=True)
			    username = db.Column(db.String(80), unique=True)
			    email = db.Column(db.String(120), unique=True)
			
			    def __init__(self, username, email):
			        self.username = username
			        self.email = email
			
			    def __repr__(self):
			        return '<User %r>' % self.username
			
			class Address(db.Model):
			    id = db.Column(db.Integer, primary_key=True)
			    province = db.Column(db.String(80), unique=True)
			    city = db.Column(db.String(120), unique=True)
			
			    def __init__(self, province, city):
			        self.province = province
			        self.city = city
			
			    def __repr__(self):
			        return '<Address %r>' % self.province
			        
			        
			#如果从当前文件新建表则可以：
			
			if __name__ == '__main__':
    			db.create_all()
    3. 根据模型新建表 db.create_all()

    	setup.py
    	
			from models.Person import db
			if __name__ == '__main__':
			    db.create_all()
