# 路由
1. 路由
	
	1. 简单路由
		
		1. 单一路由
			
				path('index/', views.index,name='index')
			
			**注意index/最后面的/不能省略**
			
			
		
		1. 通过路由传参数
		
				path('getuser/<int:id>', views.getuser,name='getuser') 
				
				path('getuser/', views.getuser,name='getuser',{'id':12o})
			views.py
				
					def getuser(request,id):
	    				return HttpResponse('HELLO WORLD--->'+str(id))
	    **建议复习函数**
		    *    必备参数
		    *    默认参数
		    *    不定长参数
		    *    关键字参数
		    *    命名关键字参数

	3. path(route, view, kwargs=None, name=None, Pattern=None)

	    1. route
	
	        模式不搜索GET和POST参数或域名。例如，在请求中https://www.example.com/myapp/，URLconf将查找 myapp/。在请求中https://www.example.com/myapp/?page=3，URLconf也将查找myapp/。
	    2. view
	        当Django找到一个匹配的模式时，它会以一个HttpRequest对象作为第一个参数以及路由中的任何“捕获”值作为关键字参数来调用指定的视图函数。
	    3. kwargs
	
	        任意关键字参数可以在字典中传递给目标视图。
	    4. name
	
	        命名您的URL可以让您从Django其他地方明确地引用它，特别是在模板中。这个强大的功能允许您在只触摸单个文件的情况下对项目的URL模式进行全局更改。

2. 基于正则的路由

	from django.conf.urls import url,include
		
		路由以特定字符串开头
		
			urlpatterns = [
				url(r'^getuser\w*/', views.getuser,name='getuser'),
				url(r'^index/(\d*)', views.index)
			]
		
		利用正则表达式传递参数
				
			#此时id的类型为str
			url(r'^getuser\w*/(?P<id>\w*)', views.getuser,name='getuser')

	    urls.py
	    
	    ```
	    from django.conf.urls import url
	    from django.contrib import admin
	    from . import view
	    from . import personal
	    
	    urlpatterns = [
	    	 #匹配空路由相当于path(r'', view.hello),
	        url(r'^$', view.hello),
	        url(r'^person\w*$', personal.login)
	    ]
	    ```
    
2. 路由重定向(同一模块中)

	在路由中我们定义了name="xxx",那么在views.py函数中，我们可以通过reverse来获取路由；但是路由中如果有参数，则要传递参数
	
	以下两个路由
	
		url(r'^getuser\w*/(?P<id>\w*)', views.getuser,name='getuser'),
    	url(r'^login\w*/(?P<userid>\w*)', views.login,name='login')
    	
    在views.login方法中获取getuser的路径，并实现跳转
    		
    		#路由名反向
    		from django.urls import reverse
    		
    		#路由跳转
    		from django.shortcuts import render,redirect
    		
    		uurl=reverse('getuser',args=(userid+'111',))
    		
    		return redirect(uurl)
    		
    		
2. 导入其他应用路由文件（子模块子路由）

	1. 新建子模块
	
			python manage.py startapp position
	
	2. 修改配置文件
	
			INSTALLED_APPS = [
			    'django.contrib.admin',
			    'django.contrib.auth',
			    'django.contrib.contenttypes',
			    'django.contrib.sessions',
			    'django.contrib.messages',
			    'django.contrib.staticfiles',
			    'position',
			    'jobapp'
			
			]

	
	3. 在新模块中新建urls.py
	
			from django.urls import path
	
			from . import views
			app_name = 'position'
			urlpatterns = [
			    
			    path('', views.index, name='index'),
			   	 path('<int:position_id>/', views.detail, name='detail'),
			    path('<int:condition>/search/', views.search, name='search'),
			    path('add/', views.addPosition, name='addPos'),
			    path('apply/', views.applyPosition, name='applyPos'),
			
			
	4. 修改主路由，包含新模块
	
		```
			    from django.conf.urls import url
			    from django.contrib import admin
			    from django.urls import path,include
			    
			    urlpatterns = [
			        path('polls/', include('position.urls')),
			        url('detail/(?p<pid>\d+)',postion.detail,name='detail')
			        path('admin/', admin.site.urls),
			    ]
	    
	    ```
    在include子路由时，可以加命名空间
    		
    		path('polls/', include('position.urls',namespace='jobapp-position')),
    	
    
    
    **模板中可以使用路由名称**
    
    	{% url 'detail'%}
5. 跨模块路由跳转（注意冒号）
	
	reverse('模块名：路由名')
	
		 myurl=reverse('position:getall')
		 myurl=reverse('position:getall'，kwargs={'id':110})
    	 return redirect(myurl)

	        
4. migrate

    迁移非常强大，随着时间的推移，您可以随时更改模型，而无需删除数据库或表并创建新的数据库 - 它专门用于实时升级数据库，而不会丢失数据。我们将在本教程的后面部分更深入地介绍它们，但现在请记住进行模型更改的三步指南：

    * 改变你的模型（in models.py）。
    * 运行以为这些更改创建迁移python manage.py makemigrations
    * 运行以将这些更改应用于数据库。python manage.py migrate
5. 


