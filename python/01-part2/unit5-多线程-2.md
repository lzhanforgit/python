# 多线程-2

1. 多线程的几个概念

	
	1. 并行、并发
		并行, parallel
	
	   互不干扰的在同一时刻做多件事;
	
	   如,同一时刻,同时有多辆车在多条车道上跑,即同时发生的概念.

 

	2. 并发, concurrency

    	同时做某些事,但是强调同一时段做多件事.

    	如,同一路口,发生了车辆要同时通过路面的事件.

 

	3. 队列, 缓冲区

    	类似排队,是一种天然解决并发的办法.排队区域就是缓冲区.

 

		解决并发:

   		【 "食堂打饭模型", 中午12点,大家都涌向食堂,就是并发.人很多就是高并发.】

 

	    1. 队列, 缓冲区:
	
	       队列: 即排队.
	
	       缓冲区: 排成的队列.
	
	       优先队列: 如果有男生队伍和女生队伍,女生队伍优先打饭,就是优先队列.

 

	    2. 争抢:
	
	      	锁机制: 争抢打饭,有人抢到,该窗口在某一时刻就只能为这个人服务,锁定窗口,即锁机制.
	
	   		争抢也是一种高并发解决方案,但是有可能有人很长时间抢不到,所以不推荐.

 

    	3. 预处理:

        	统计大家爱吃的菜品,最爱吃的80%热门菜提前做好,20%冷门菜现做,这样即使有人锁定窗口,也能很快释放.

        	这是一种提前加载用户需要的数据的思路,预处理思想,缓存常用.

 

    	4. 并行:

        	开多个打饭窗口,同时提供服务.

        	IT日常可以通过购买更多服务器,或多开线程,进程实现并行处理,解决并发问题.

        	这是一种水平扩展的思路.

        	注: 如果线程在单CPU上处理,就不是并行了.

 

    	5. 提速:

        	通过提高单个窗口的打饭速度,也是解决并发的方式.

        	IT方面提高单个CPU性能,或单个服务器安装更多的CPU.   

        	这是一种垂直扩展的思想.

 

    	6. 消息中间件:

        	如上地地铁站的九曲回肠的走廊,缓冲人流.

        	常见消息中间件: RabbitMQ, ActiveMQ(Apache), RocketMQ(阿里Apache), kafka(Apache)等.

2. 多线程案例

		import threading

		import time
		
		
		def worker():
		    count = 0
		
		    while True:
		
		        if (count >= 5):
		            break
		
		        time.sleep(1)
		
		        count += 1
		        print(threading.current_thread())
		        print('worker running')
		
		
		class MyThread(threading.Thread):
		
		    def start(self):
		        print('start~~~~~~~~~~~~~')
		
		        super().start()
		
		    def run(self):
		        print('run~~~~~~~~~~~~~~~~~')
		
		        super().run()
		
		
		t1 = MyThread(name='worker', target=worker)
		t2 = MyThread(name='boss', target=worker)
		
		t1.start()
		t2.start()
		
		# t1.run()
		# t2.run()

	>没有开新的线程，这就是普通函数调用，所以执行完t1.run(),然后执行t2.run(),这里就不是多线程。

	>当使用start方法启动线程后，进程内有多个活动的线程并行的工作，就是多线程。

	>一个进程中至少有一个线程，并作为程序的入口，这个线程就是主线程。一个进程至少有一个主线程。

	>其他线程称为工作线程。
5. 后台线程和前台线程
	
	is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）
	
	1. 如果是后台线程(当我们使用setDaemon(True)方法，设置子线程为守护线程时)，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
	
	1. 如果是前台线程（其实就是setDaemon(False))，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止

	
			if __name__ == '__main__':
			    for i in range(4):
			        t = MyThread(i)
			        t.setDaemon(True)
			        t.start()
			
			    print('main thread end!')
	
3. 线程安全

		import threading
		import time
		i=1
		def worker():
		    global i
		    print('当前的线程是{0},i等于{1}'.format(threading.current_thread(),i))
		    time.sleep(1)
		    i=i+1
		
		    print('-------{0},i等于{1}'.format(threading.current_thread(), i))
		
		for x in range(1, 5):
		    name = 'worker{}'.format(x)
		
		    t = threading.Thread(name=name, target=worker)
		
		    t.start()
	perfect:https://www.cnblogs.com/amesy/p/8067583.html

6. join()

	 join()阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout，即使设置了setDeamon（True）主线程依然要等待子线程结束。
	 
	 线程必须先start()然后再join()
	 
	 **错误的做法是**
	 
	 	if __name__ == '__main__':
		    for i in range(4):
		        t = MyThread(i)
		        t.start()
		        t.join()
	>可以看出此时，程序只能顺序执行，每个线程都被上一个线程的join阻塞，使得“多线程”失去了多线程意义。
	
	**☝️这样**
		
		if __name__ == '__main__':
		    th=[]
		    for i in range(4):
		        t = MyThread(i)
		        th.append(t)
		        t.start()
		
		
		    for tt in th:
		        tt.join()
		    #设置join之后，主线程等待子线程全部执行完成后或者子线程超时后，主线程才结束
		    print('main thread end!')
6. 	线程同步-Lock、Rlock类

	由于线程之间随机调度：某线程可能在执行n条后，CPU接着执行其他线程。为了多个线程同时操作一个内存中的资源时不产生混乱，我们使用锁。

	Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

	可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

	RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。

	可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。
	
	实例方法： 
		
	* acquire([timeout]): 尝试获得锁定。使线程进入同步阻塞状态。 
	　　
	* release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

	
		```
		import threading
		import time
		
		
		# 方法一：将要执行的方法作为参数传给Thread的构造方法
		count=0
		lock = threading.RLock()
		def action(arg):
		    lock.acquire()
		    time.sleep(1)
		    global count
		    count+=1
		    
		    print(threading.current_thread())
		    count-=1
		    print('the arg is:{0},count is:{1}'.format(arg,count))
		    lock.release()
		ths=[]
		for i in range(4):
		
		    t =threading.Thread(target=action,args=(i,))
		    # t.setDaemon(True)
		    ths.append(t)
		
		for tt in ths:
		    tt.start()
		
		for tt in ths:
		    tt.join()
		
		if __name__ == '__main__':
		    # print(threading.current_thread())
		    # print(threading.enumerate())
		    # print(threading.activeCount())
		    print('main thread end!')
		```
1. Lock对比Rlock

		import threading
		lock = threading.Lock() #Lock对象
		lock.acquire()
		lock.acquire()  #产生了死锁。
		lock.release()
		lock.release()
		print lock.acquire()
		 
		 
		import threading
		rLock = threading.RLock()  #RLock对象
		rLock.acquire()
		rLock.acquire() #在同一线程内，程序不会堵塞。
		rLock.release()
		rLock.release()
2. Condition类

	Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。
	
	可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。
	
	构造方法： 
	Condition([lock/rlock])
	
	实例方法： 
	
	* acquire([timeout])/release(): 调用关联的锁的相应方法。 
	* wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。 
	* notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。 
	* notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

			# encoding: UTF-8
			import threading
			import time
			
			# 商品
			product = None
			# 条件变量
			con = threading.Condition()
			
			
			# 生产者方法
			def produce():
			    global product
			
			    if con.acquire():
			        while True:
			            if product is None:
			                print ('produce...')
			                product = 'anything'
			
			                # 通知消费者，商品已经生产
			                con.notify()
			
			            # 等待通知
			            # con.wait()
			            time.sleep(2)
			
			
			# 消费者方法
			def consume():
			    global product
			
			    if con.acquire():
			        while True:
			            if product is not None:
			                print('consume...')
			                product = None
			
			                # 通知生产者，商品已经没了
			                con.notify()
			
			            # 等待通知
			            con.wait()
			            time.sleep(2)
			
			
			t1 = threading.Thread(target=produce)
			t2 = threading.Thread(target=consume)
			t2.start()
			t1.start()
	
		生产者消费者模型
			
			import threading
			import time
			
			condition = threading.Condition()
			products = 0
			
			class Producer(threading.Thread):
			    def run(self):
			        global products
			        while True:
			            if condition.acquire():
			                if products < 10:
			                    products += 1
			                    print("Producer(%s):deliver one, now products:%s" %(self.name, products))
			                    condition.notify()#不释放锁定，因此需要下面一句
			                    condition.release()
			                else:
			                    print("Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products))
			                    condition.wait()#自动释放锁定
			                time.sleep(2)
			
			class Consumer(threading.Thread):
			    def run(self):
			        global products
			        while True:
			            if condition.acquire():
			                if products > 1:
			                    products -= 1
			                    print("Consumer(%s):consume one, now products:%s" %(self.name, products))
			                    condition.notify()
			                    condition.release()
			                else:
			                    print("Consumer(%s):only 1, stop consume, products:%s" %(self.name, products))
			                    condition.wait()
			                time.sleep(2)
			
			if __name__ == "__main__":
			    for p in range(0, 2):
			        p = Producer()
			        p.start()
			
			    for c in range(0, 3):
			        c = Consumer()
			        c.start()
		condition.notifyAll()
		
			import threading
	
			alist = None
			condition = threading.Condition()
			
			
			def doSet():
			    if condition.acquire():
			        while alist is None:
			            condition.wait()
			        for i in range(len(alist))[::-1]:
			            alist[i] = 1
			            print(alist[i])
			        condition.notify()
			        condition.release()
			
			
			def doPrint():
			    if condition.acquire():
			        while alist is None:
			            condition.wait()
			        for i in alist:
			            print(i)
			
			        print()
			        condition.notify()
			        condition.release()
			
			
			def doCreate():
			    global alist
			    if condition.acquire():
			        if alist is None:
			            alist = [0 for i in range(10)]
			            condition.notifyAll()
			        condition.release()
			
			
			tset = threading.Thread(target=doSet, name='tset')
			tprint = threading.Thread(target=doPrint, name='tprint')
			tcreate = threading.Thread(target=doCreate, name='tcreate')
			tset.start()
			tprint.start()
			tcreate.start()

