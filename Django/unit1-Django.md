# Django
1. 简介

    python下有许多款不同的 Web 框架。Django是重量级选手中最有代表性的一位。许多成功的网站和APP都基于Django。

    Django是一个开放源代码的Web应用框架，由Python写成。
    
    Django遵守BSD版权，初次发布于2005年7月, 并于2008年9月发布了第一个正式版本1.0 。
    
    [中文文档](https://docs.djangoproject.com/zh-hans/2.0/)

1. 安装

    1. windows

    
        下载 Django 压缩包，解压并和Python安装目录放在同一个根目录，进入 Django 目录，执行python setup.py install，然后开始安装，Django将要被安装到Python的Lib下site-packages。
        
        配置环境变量:
        将这几个目录添加到系统环境变量中： C:\Python33\Lib\site-packages\\..\django;C:\Python33\Scripts。 添加完成后就可以使用Django的django-admin.py命令新建工程了。
        
        检查是否安装成功
        输入以下命令进行检查:
        
        ```
            >>> import django
            >>> django.get_version()
        ```
        或者
        
        ```
            python3 -m django --version 
        ```
    2. mac
    
        下载安装包
        Django 下载地址：https://www.djangoproject.com/download/
        
        
        ```
        $ tar zxvf Django-1.x.y.tar.gz
        cd Django-1.x.y
        sudo python setup.py install
        ```
        
    >如果在独立的env中，则也需要pip install django命令来安装。
    
  	3. 查看是否安装成功

  			python -m django --version

2. 卸载

    如果您以前使用过Django ，卸载就像从Python中删除目录 一样简单。要找到需要删除的目录，可以在shell提示符（而不是交互式Python提示符）下运行以下命令：
    	

    	python setup.py installdjangosite-packages

2. 创建项目

    再进入我们的站点目录，创建 Django 项目：
    
    ```
    $ django-admin startproject testdj
    # $ django-admin.py startproject testdj //老版本使用
    ```
    **最新版的 Django 请使用 django-admin 命令**
    启动服务：
    
    ```
    cd testdj # 切换到我们创建的项目
    # python manage.py runserver 0.0.0.0:8000
    # python manage.py runserver 8080
    $ python manage.py runserver
    ```
    
    >启动django后，不能访问，报400错误。
    原因：没有开启允许访问
    处理：编辑HelloWorld目录下setting.py ，把其中的
    ALLOWED_HOSTS=[]改成ALLOWED_HOSTS=['*'] ##* 表示任意地址。

3. 项目目录分析

    *     HelloWorld: 项目的容器。
    * manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
    * HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
    * HelloWorld/settings.py: **该 Django 项目的设置/配置。**

        ```
            # 配置路由文件
            ROOT_URLCONF = 'HelloWorld.urls'

            TEMPLATES = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    # 配置模板文件目录
                    'DIRS': [BASE_DIR + "/templates", ],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.debug',
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ]
            
        ```
    * HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
    * HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
5. 在项目目录中创建应用

    要创建您的应用程序，请确保您位于相同的目录中manage.py 并键入此命令：

    ```
    $ python manage.py startapp polls
    ```

    >项目与应用程序

    >项目和应用程序有什么区别？应用程序是一种Web应用程序，它可以执行某些操作，例如Weblog系统，公共记录数据库或简单的轮询应用程序。项目是特定网站的配置和应用程序的集合。项目可以包含多个应用程序。一个应用程序可以在多个项目中。

    为这个应用创建路由：
    在该应用目录下新建urls.py文件

    ```
        from django.urls import path
    
        from . import views
        
        urlpatterns = [
            path('', views.index, name='index'),
        ]
    ```

4. 配置模板文件和静态文件

	2. 模版
		
			TEMPLATES = [
		    {
		        'BACKEND': 'django.template.backends.django.DjangoTemplates',
		        'DIRS': ['/templates/','position/templates/'],
		        
		___
		
			TEMPLATE_DIRS = (
	    	os.path.join(BASE_DIR,'templates'),
	    	)
	    
	3. 静态文件

			STATICFILES_DIRS = (
		        os.path.join(BASE_DIR,'static'),
		    )
		    
		   	<link rel="stylesheet" href="{% static "main.css" %}">

