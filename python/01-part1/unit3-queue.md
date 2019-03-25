# queue

    
1. 特性

    Queue是python中的标准库，可以直接
    
    	import queue
    
    队列是线程间最常用的交换数据的形式
    
2. 方法

	1. 初始化
	
			import queue
			q=queue.Queue(10) 构建长度为10的队列
			
			q = queue.Queue(maxsize=3)
		
	2. 包中的常用方法:

		    Queue.qsize() 返回队列的大小
		
		    Queue.empty() 如果队列为空，返回True,反之False
		
		    Queue.full() 如果队列满了，返回True,反之False
		
		    Queue.full 与 maxsize 大小对应
		
		    Queue.get([block[, timeout]])获取队列，timeout等待时间
		    
	3. 将一个值放入队列中

    		myqueue.put(10)
    		put(item[, block[, timeout]])
    		
		将item放入队列中。
		
		如果可选的参数block为True且timeout为空对象（默认的情况，阻塞调用，无超时）。
		
		如果timeout是个正整数，阻塞调用进程最多timeout秒，如果一直无空空间可用，抛出Full异常（带超时的阻塞调用）。
		
		如果block为False，如果有空闲空间可用将数据放入队列，否则立即抛出Full异常
		其非阻塞版本为put_nowait等同于put(item, False)
	


	4. 将一个值从队列中取出

    		myqueue.get()


		demo
			
			import queue

			q = queue.Queue(maxsize=3)
			
			for i in range(3):
			    q.put(i)
			
			while not q.empty():
			    print(q.get())


	5. task_done()
	
		意味着之前入队的一个任务已经完成。由队列的消费者线程调用。每一个get()调用得到一个任务，接下来的task_done()调用告诉队列该任务已经处理完毕。

		如果当前一个join()正在阻塞，它将在队列中的所有任务都处理完时恢复执行（即每一个由put()调用入队的任务都有一个对应的task_done()调用）。