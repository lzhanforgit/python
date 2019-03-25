# 中间件

1. 哪里有

	settings.py
	
		MIDDLEWARE = [
		    'django.middleware.security.SecurityMiddleware',
		    'django.contrib.sessions.middleware.SessionMiddleware',
		    'django.middleware.common.CommonMiddleware',
		    # 'django.middleware.csrf.CsrfViewMiddleware',
		    'django.contrib.auth.middleware.AuthenticationMiddleware',
		    'django.contrib.messages.middleware.MessageMiddleware',
		    'django.middleware.clickjacking.XFrameOptionsMiddleware',
		]
	
			
2. 说明

	django为用户实现防止跨站请求伪造的功能，通过中间件 django.middleware.csrf.CsrfViewMiddleware 来完成。而对于django中设置防跨站请求伪造功能有分为全局和局部。
	
	全局：
	
	　　中间件 django.middleware.csrf.CsrfViewMiddleware
	
	局部：
	
	@csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。
	
	@csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
	**注：from django.views.decorators.csrf import csrf_exempt,csrf_protect**