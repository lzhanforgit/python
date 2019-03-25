# 模型

1. 介绍

	模型是有关数据的单一，明确的信息来源。它包含您要存储的数据的基本字段和行为。通常，每个模型都映射到单个数据库表。

	基础：

	* 每个模型都是一个子类的Python类 django.db.models.Model。
	* 模型的每个属性代表一个数据库字段。

2. ORM

	关系对象映射（Object Relational Mapping，简称ORM）。
	
	生成表结构(默认数据库为sqllite)
	
	1. 在引用下的models.py文件中（如果没有就新键）。创建类

			from django.db import models

			# Create your models here.
			class userinfo(models.Model):
			    # 自动创建一个id列，id为主键、自增长
			    telephone = models.CharField(max_length=30)
			    password = models.CharField(max_length=64)
			    email = models.EmailField()
			    # memo = models.TextField()
	2. 修改配置文件（settings.py），告诉应用从哪里应用模块中创建

			INSTALLED_APPS = [
		    'django.contrib.admin',
		    'django.contrib.auth',
		    'django.contrib.contenttypes',
		    'django.contrib.sessions',
		    'django.contrib.messages',
		    'django.contrib.staticfiles',
		    'jobapp'   #注意这里加上的是模块名称
		]
	3. 执行创建命令-python manage.py makemigrations
		
		**注意**
			
		该模块目录下必须有一个文件夹：migrations（如果没有就新键）
		
		
		执行python manage.py makemigrations生成临时文件：“0001_initial.py”
	
	4. python manage.py migrate 生成数据表

	
		默认表名：“jobapp01_uerinfo”
		
	5. 把数据库从sqllite改为mysql
	
		修改配置文件：
		
		之前为：
		
			DATABASES = {
			    'default': {
			        'ENGINE': 'django.db.backends.sqlite3',
			        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
			    }
			}
			
		修改为：
		
			DATABASES = {
			    'default': {
			    'ENGINE': 'django.db.backends.mysql',
			    'NAME':'jobapp_django',
			    'USER': 'root',
			    'PASSWORD': '12345678',
			    'HOST': '127.0.0.1',
			    'PORT': '3306',
			    }
			}
			
		**注意**
		
		由于Django内部连接MySQL时使用的是MySQLdb模块，而python3中还无此模块，所以需要使用pymysql来代替
  
		如下设置放置的与project同名的配置的 __init__.py文件中
  
			import pymysql
			pymysql.install_as_MySQLdb()　
			
		**所以啊，要先安装：pip install pymysql**
		
	1. **删除数据表重新生成，解决 python No migrations to apply 无法生成表**

		第一步：
			
			删除该app名字下的migrations文件。

		第二步：
			
			进入数据库，找到django_migrations的表，删除该app名字的所有记录。
			delete from django_migrations;
			
			或者删除数据库重新新建

		第三部:
			
			python manage.py makemigrations

			python manage.py migrate
	
3. 访问数据数据库

	1. 增加数据

		在views.py文件中，增加

			from . import models
	
		
			def regist(request):
				# uu返回数据库中刚加入的那个对象
			    uu=models.userinfo.objects.create(
			        telephone="root",
			        password="123456"
			    )
			    
			    #或者
			    
			    uu=models.userinfo.objects.create(**dict)
			    
			    
			    #或者
			    
			    user=models.userinfo(telephone="admin",password="6666")
    			user.save()
			
			    return HttpResponse('regist ok')
			    
			    #再者
			    
			    dic={"telephone":"alex","password":"888"}

    			models.userinfo(**dic).save() #当然了，				models.userinfo.objects.create（**dic）也可以
   
   		**force_update和force_insert**

		这两个参数一般较少用到，因为save()之后django执行的是UPDATE或者INSERT这两条SQL语句的哪一条，遵循如下算法：
		
		1.如果这个对象已经有主键而且主键的值是True的（即不是None或者空字符串等），就执行UPDATE。
		
		2.如果没有主键或者这条save()不会update任何字段,那么它就INSERT。
		
		只有在某些特定情况下，需要强制save()执行INSERT或UPDATE时才会使force_update=True或force_insert=True（比如我要求能UPDATE就UPDATE，不能我也不取INSERT，那么我就把这个force_update参数设置为True）。
   2. 关于自增长id

   		**id必须为models.AutoField**
   		
   			class userinfo(models.Model):
			    # id = models.IntegerField(primary_key=True)
			    id = models.AutoField(primary_key=True)
			
			    # 自动创建一个id列，id为主键、自增长
			    telephone = models.CharField(unique=True,max_length=30)
			    password = models.CharField(max_length=64)
			    email = models.EmailField()
			    # memo = models.TextFi	eld()
			    
		**save()之后直接拿**
		
			 dic={"telephone":"root","password":"999"}

		    comment=models.userinfo(**dic)
		    comment.save()
		
		    print(comment.id)
   
	2. 查询数据

		1. 查询所有数据

				users=models.userinfo.objects.all()
				
				# 返回的是对象列表
				for user in users:
        			print(user.id,user.telephone,user.password)
        			
        		#获取部分列
				users=models.userinfo.objects.all().values(‘id’,'telephone')
				#这个时候users为字典列表
				
				#获取部分列
				models.userinfo.objects.all().values_list(‘id’,'telephone')
				
				#这个时候users为元组列表

		2. 条件查询

			1. 单条件

			
					users=models.userinfo.objects.filter(telephone='root')
					#select * from userinfo where telephone='root'
	    			for user in users:
	        			print(user.id,user.telephone,user.password)


			2. and

				逗号表示and

				users=models.userinfo.objects.filter(telephone='root',password='123)

			
			1.  ....

		3. 删除

			affect_rows=models.userinfo.objects.all().delete()
			
			affect_rows=models.userinfo.objects.filter(id='4').delete()

		4. 更新

			affect_rows=models.userinfo.objects.all().update(password="666666")
		affect_rows=models.userinfo.objects.filter(id='4').update(password="666666")
		
		

4. demo 实现用户登录

	**注意**
	
	如果数据没有查到返回的是[]空列表
	
	如果user=models.userinfo.objects.filter(telephone='root').first()没有查到数据则结果为None
	
	如果num=models.userinfo.objects.filter(telephone='root').count()没有查到数据则结果为0
		