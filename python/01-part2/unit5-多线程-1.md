# 多线程
1. 什么是线程,进程
	
	a. 在实现了线程的操作系统中,线程是操作系统能够运算调度的最小单位.
	
	b. 线程被包含在进程中,是进程的实际运作单位.
	
	c. 一个程序的执行实例就是一个进程.
	
	进程(Process)是计算机中的程序关于某数据集合上的一次运行活动,是系统进行资源分配和调度的基本单位,是操作系统结构的基础.

    进程和程序的关系: 进程是线程的容器.

  	Linux进程有父进程和子进程之分,windows的进程是平等关系.

  	线程有时称为轻量级进程,一个标准的线程由线程ID,当前指令指针,寄存器集合和堆栈组成.

	当运行一个程序时,OS会创建一个进程。它会使用系统资源（CPU、内存和磁盘空间）和OS内核中的数据结构（文件、网络连接、用量统计等）。

	进程之间是互相隔离的，即一个进程既无法访问其他进程的内容，也无法操作其他进程。

	操作系统会跟踪所有正在运行的进程，给每个进程一小段运行时间，然后切换到其他进程，这样既可以做到公平又可以响应用户操作。

	可以在图形界面中查看进程状态，在在Windows上可以使用任务管理器。也可以自己编写程序来获取进程信息。
	
1. 总结

	对线程、线程的理解:

	1. 进程是独立的王国,进程间不能随便共享数据.
	
	1. 线程是省份,同一进程内的线程可以共享进程的资源,每一个线程有自己独立的堆栈.       
   
   线程的状态: 

	1. 就绪(Ready): 线程一旦运行,就在等待被调度.
	1. 运行(Running): 线程正在运行.
	1. 阻塞(Blocked): 线程等待外部事件发生而无法运行,如I/O操作.
	1. 终止(Terminated): 线程完成或退出,或被取消.

2. 单线程

		from time import ctime,sleep

		def music():
		    for i in range(2):
		        print("I was listening to music. %s" %ctime())
		        sleep(1)
		
		def move():
		    for i in range(2):
		        print("I was at the movies! %s" %ctime())
		        sleep(5)
		
		if __name__ == '__main__':
		    music()
		    move()
		    print("all over {}".format(ctime()))
1. 什么是多线程

	多线程类似于同时执行多个不同程序，多线程运行有如下优点：
	
	* 使用线程可以把占据长时间的程序中的任务放到后台去处理。
	* 用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度
	* 程序的运行速度可能加快
	* 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。

	>每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。
指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。
	
	Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
	
	由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
	
	threading用于提供线程相关的操作，线程是应用程序中工作的最小单元。python当前版本的多线程库没有实现优先级、线程组，线程也不能被停止、暂停、恢复、中断。

	threading模块提供的类：  
	
	　　Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local。
	
		
	threading 模块提供的常量：
	
	　　threading.TIMEOUT_MAX 	#设置threading全局超时时间。
	
	threading的属性和方法
		
	1. current_thread()  # 返回当前线程对象.
		
	2. main_thread()  # 返回主线程对象.
		
	3. active_count()  # 当前处于alive状态的线程个数.
		
	4. enumerate()  # 返回所有活着的线程的列表,不包括已经终止的线程和未开始的线程.
		
	5. get_ident()  # 返回当前线程ID,非0整数.

	thread实例(线程对象)的属性和方法（下面还有补充哦）
	
	1. name: 只是一个名称标识,可以重名, getName()、setName()来获取、设置这个名词。

	2. ident: 线程ID, 它是非0整数。线程启动后才会有ID，否则为None。线程退出，此ID依旧可以访问。此ID可以重复使用。

	3. is_alive(): 返回线程是否活着。
2. 开启线程的两种方式-函数


		def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)
　

	* target: 线程调用的对象,就是目标函数.
	* name: 为线程起个名字.
	* args: 为目标函数传递实参, 元组.
	* kwargs: 为目标函数关键字传参, 字典.

	demo 1:
		
		import threading
		def worker():
			
			#打印正在执行的线程
		    print(threading.current_thread())
		    print("I'm working")
		    print("Finished")
		
		
		if __name__ == '__main__':
		    t = threading.Thread(target=worker, name='worker')  # 线程对象.
		    print(threading.current_thread())
		    t.start()
		
	demo 2:
	
			import threading
			import time
			#方法一：将要执行的方法作为参数传给Thread的构造方法
			
			def action(arg):
			    time.sleep(1)
			    print(threading.current_thread())
			
			    print('the arg is:{0}'.format(arg))
			
			for i in range(4):
			    t =threading.Thread(target=action,args=(i,))
			    t.start()
			
			if __name__ == '__main__':
			    print(threading.current_thread())
			    print('main thread end!')
			    
	**线程退出**

	python没有提供线程退出的方法,在下面情况时会退出:
		
	1. 线程函数内语句执行完毕.
	2. 线程函数中抛出未处理的异常.

			import threading
			import time
			def worker():
			    count = 0
			
			    try:
			        while True:
			            if (count > 5):
			                raise RuntimeError('error happened')
			
			                # return
			
			            time.sleep(1)
			
			            print("I'm working")
			
			            count += 1
			    except RuntimeError as ex:
			        print(ex)
			
			
			t = threading.Thread(target=worker, name='worker')  # 线程对象.
			
			t.start()  # 启动.		
3. 开启线程的两种方式-用类来包装线程对象

	start(): 启动线程。每一个线程必须且只能执行该方法一次。

	run(): 运行线程函数。
	
	**start()方法会调用run()方法，而run()方法可以运行函数。**


	demo 1:
	
		class MyThread(threading.Thread):
		    def __init__(self,arg):
		        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
		        self.arg=arg
		    def run(self):#定义每个线程要运行的函数
		        time.sleep(1)
		        print 'the arg is:%s\r' % self.arg
		
		for i in xrange(4):
		    t =MyThread(i)
		    t.start()

	demo 2:
		
		import threading

		import time
		
		
		def worker():
		    count = 0
		
		    while True:
		
		        if (count >= 5):
		            break
		
		        time.sleep(1)
		
		        count += 1
		
		        print('worker running')
		
		
		class MyThread(threading.Thread):
		
		    def start(self):
		        print('start~~~~~~~~~~~~~')
		
		        super().start()
		
		    def run(self):
		        print('run~~~~~~~~~~~~~~~~~')
		
		        super().run()
		
		
		t = MyThread(name='worker', target=worker)
	
		#t.strat()
		t.run()
		
	**注意**
	
	**使用start方法启动线程，启动了一个新的线程，名字叫做worker running,但是使用run方法启动的线程，并没有启动新的线程，只是在主线程中调用了一个普通的函数而已。**

	**因此,启动线程要使用start方法，才能启动多个线程。**
	Thread类
	
	构造方法： 
	* Thread(group=None, target=None, name=None, args=(), kwargs={}) 
	
	* group: 线程组，目前还没有实现，库引用中提示必须是None；
	　　 
	* target: 要执行的方法； 
	　　
	* name: 线程名； 
	　　
	* args/kwargs: 要传入方法的参数。
	
	实例方法： 
	
	* isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。 
	* get/setName(name): 获取/设置线程名。 
	* start():  启动线程。每一个线程必须且只能执行该方法一次。线程准备就绪，等待CPU调度
	* run(): 运行线程函数。
	* join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
4. threading 模块提供的常用方法： 
	
	* threading.currentThread(): 返回当前的线程变量。 
	* threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
	* threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。


