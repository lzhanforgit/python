# 函数装饰器
0. 为什么要用装饰器？

	装饰器本质上是一个函数，该函数用来处理其他函数，它可以让其他函数在不需要修改代码的前提下增加额外的功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等应用场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用.概括的讲，**装饰器的作用就是为已经存在的对象添加额外的功能。**

	
	1. 先定义两个个函数

			def addUser():
    			print('添加用户成功！')

			def registUser():
			    print('添加用户成功！')
		如果用户想要知道是哪个函数添加了用户，怎么办？（略...）
		
		改进方法
		
			def debug():
			    import inspect
			    caller_name = inspect.stack()[1][3]
			    print("[DEBUG]: enter {}()".format(caller_name))
			
			def addUser():
			    debug()
			    print('添加用户成功！')
			
			def registUser():
			    debug()
			    print('添加用户成功！')
			    
		但是如果再想要取消这个功能，则需要改变两个函数：addUser，registUser
		
		**装饰器的作用很明显**
			
			def debug(func):
			    def wrapper():
			        print("[DEBUG]: enter {}()".format(func.__name__))
			        return func()
			    return wrapper
			
			@debug
			def addUser():
			    print('添加用户成功！')
			    return 'ok'
			
			@debug
			def registUser():
			    print('添加用户成功！')
2. 装饰器传参
	
	参数先传给装饰器，装饰器传给函数
		
		def debug(func):
		    def wrapper(name):
		        print("[DEBUG]: enter {}()".format(func.__name__))
		        func(name)
		    return wrapper
		
		@debug
		def addUser(name):
		    print('添加用户{0}成功！'.format(name))
		
		@debug
		def registUser(name):
		    print('添加用户{0}成功！'.format(name))
		
		addUser('tom')
		registUser('jack')
		
	如果函数是有返回值的，则加上return 语句即可
		
		def debug(func):
		    def wrapper(name):
		        print("[DEBUG]: enter {}()".format(func.__name__))
		        return func(name)  #此处加上return
		    return wrapper
	
3. 传递可变参数

		def debug(func):
		    def wrapper(*args,**other):
		        print("[DEBUG]: enter {}()".format(func.__name__))
		        print(other)
		        # 可以在此处对 args和other数据进行处理
		        return func(args)
		    return wrapper
		
		@debug
		def addUser(user):
		    print('添加用户{0}成功！'.format(user))
		    return user
		
		@debug
		def registUser(user):
		    print('添加用户{0}成功！'.format(user))
		    return user
		
		n1=addUser('tom',12,other={'gender': 'M', 'job': 'Engineer'})
		n2=registUser('jack')
