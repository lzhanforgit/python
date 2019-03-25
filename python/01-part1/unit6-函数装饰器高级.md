# 函数装饰器高级


0. 最新版本
		
	最新版本的python导入了functools模块
	
		from functools import wraps
		def debug(func):
		    @wraps(func)
		    def wrapper(name):
		        print("[DEBUG]: enter {}()".format(func.__name__))
		        return func(name)  #此处加上return
		    return wrapper
		@debug
		
		def show(s):
		    print(s)
		
		show('ppyth')
1. 带参数的装饰器

	```
		from functools import wraps
		def debug(*text):
		    def decorated(func):
		        @wraps(func)
		        def wrapper(name):
		            print("[DEBUG]: enter {}()".format(func.__name__))
		            return func(name)  # 此处加上return
		
		        return wrapper
		    return decorated
		
		@debug()  #此处的（）不可以删略
		def show(s):
		    print(s)
		
		show('ppyth')
	```
	
3. \_\_call__()

	所有的函数都是可调用对象。
	一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
	
		class Person(object):
		    def __init__(self,name):
		        self.name=name
		
		    def __call__(self, *args, **kwargs):
		        print('my name is ',self.name)
		        print('my hobby is ',args)
		
		p1=Person('tom')
		
		p1('reading')
	>所以，在Python中，函数也是对象，对象和函数的区别并不显著。
2. 类装饰器(待续.....)
	
		from functools import wraps
		from datetime import datetime
		
		#类的装饰器写法，日志
		class log(object):
		    def __init__(self, logfile='out.log'):
		        self.logfile = logfile
		
		    def __call__(self, func):
		        @wraps(func)
		        def wrapped_func(*args, **kwargs):                     
		            self.writeLog(*args, **kwargs)    # 先调用 写入日志         
		            return func(*args, **kwargs)     # 正式调用主要处理函数       
		        return wrapped_func
		
		   #写入日志    
		    def writeLog(self, *args, **kwargs):
		        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		        log_str = time+' 操作人:{0[0]} 进行了【{0[1]}】操作'.format(args)           
		        with open(self.logfile, 'a',encoding='utf8') as file:
		            file.write(log_str + '\n')
		
		@log()
		def myfunc(name,age):
		    print('姓名：{0},年龄：{1}'.format(name,age))
		
		if __name__ == '__main__':
		    myfunc('小白', '查询')
		    myfunc('root', '添加人员')
		    myfunc('小小', '修改数据')


	[参考](https://www.cnblogs.com/cicaday/p/python-decorator.html)
	
	[参考](https://www.jianshu.com/p/9e9726055bbe)