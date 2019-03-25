## 垃圾回收
1. 小对象对象池

	整数在程序中的使用非常广泛，Python为了优化速度，使用了小整数对象池， 避免为整数频繁申请和销毁内存空间。

	Python 对小整数的定义是 [-5, 256] 这些整数对象是提前建立好的，不会被垃圾回收。在一个 Python 的程序中，无论这个整数处于LEGB中的哪个位置，

	所有位于这个范围内的整数使用的都是同一个对象。同理，单个字母也是这样的。
	
	我们可以通过引用计数查看：
	
		import sys
		a=2
		b=2
		print(sys.getrefcount(a))
		
		print(id(a))
		print(id(b))
		
		print(a is b)  #true
		print(a==b)	  #true

	简单字符串（由数字、字母、下划线组成）也会加入小对象对象池
	
		s1='hello'
		s2='hello'
		
		s1 is s2 #true
		
		s3='hello world'
		s4='hello world'
		
		s4 is s3 #false
		
		s5='hello_world'
		s6='hello_world'
		
		s5 is s6 #true

	intern机制处理空格一个单词的复用机会大，所以创建一次，有空格创建多次，但是字符串长度大于20，就不是创建一次了。
	
		s1 = "abcd"
		s2 = "abcd"
		print(s1 is s2)# True
		
		s1 = "a" * 20
		s2 = "a" * 20
		print(s1 is s2)# True
		
		s1 = "a" * 21
		s2 = "a" * 21
		print(s1 is s2)# False
		
		s1 = "ab" * 10
		s2 = "ab" * 10
		print(s1 is s2)# True
		
		s1 = "ab" * 11
		s2 = "ab" * 11
		print(s1 is s2)# False
		
			
2. 大整数对象池。

	说明：
	
	终端是每次执行一次，所以每次的大整数都重新创建，而在pycharm中，每次运行是所有代码都加载都内存中，属于一个整体，所以

 	这个时候会有一个大整数对象池，即处于一个代码块的大整数是同一个对象。c1 和d1 处于一个代码块，而c1.b和c2.b分别有自己的代码块，所以不相等。
 	
 	大数据对象不公用内存，引用计数为0则销毁。
 	
 		c1 = 1000
		d1 = 1000
		print(c1 is d1)  # True
		
		class C1(object):
		    a = 100
		    b = 100
		    c = 1000
		    d = 1000
		
		
		class C2(object):
		    a = 100
		    b = 1000
		
		
		print(C1.a is C1.b)  # True
		print(C1.a is C2.a)  # True
		print(C1.c is C1.d)  # True
		print(C1.b is C2.b)  # False

