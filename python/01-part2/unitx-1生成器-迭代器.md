## 迭代器
1. 概述

    迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

2. 可迭代对象

	迭代器提供了一个统一的访问集合的接口。只要是实现了__iter__()或    __getitem__()方法的对象，就可以使用迭代器进行访问。
  
    序列：字符串、列表、元组
  
    非序列：字典、文件
  
    自定义类：用户自定义的类实现了__iter__()或__getitem__()方法的对象
  
    迭代字典

　　		d = {'a': 1, 'b': 2, 'c': 3}
​			
			for k in d:
			    print(k)
			
			for k in d.keys():
			    print(k)
			
			for v in d.values():
			    print(v)
			
			for (k,v) in d.items():
			    print(k,v)

3. 迭代基础

    ```
        f1=open('data.txt')

        # for line in f1.readlines(): #把所有行读入内存，遇到大文件效率差
        #     print(line)
        
        # for line in f1:
        #     print(line)
        
        # 文件对象就是自己的迭代器
        
        print(f1.__next__())
        print(f1.__next__())
        
        # 为了手动支持迭代，python3.0提供了一个next（）方法，他会自动调用对象的_next_()
        
        print(next(f1))
    ```
    
4. iter() 和 next()

	
    字符串/数组本身没有迭代对象
    
    ```
    	s='hello'

		iter01=iter(s)
		print(next(iter01))
		print(next(iter01))
		
		
        arr=[1,2,3,4]
        E=iter(arr)
        # print(E.__next__())
        # print(next(E))
        
        while True:
            try:
                X=E.__next__()
            except StopIteration:
                break
            print(X) 
    ```
    >字典对象有一个迭代器，每次返回字典的key
    
    ```
        params={'name':'tom','age':12}
        for key in params:
            ...
        #所以不要下面的写法
        for key in params.keys():
            ...
        
    ```
5. range()
  
    range()支持多个迭代器，而其他内置函数不支持
    ```
        arr=list(range(20))
        print(arr)
        
        R=iter(range(100))
        
        print(next(R))
        print(next(R))
        print(next(R))
        
        
    ```
5. enumerate函数

	Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
	
		mylist=['A', 'B', 'C']
		for i, value in enumerate(mylist):
		    print(i,value)
  
6. map() zip() filter()
    和range()不同，以上三个函数都是自己的迭代器
    
    ```
        M=map(abs,[2,-3,-1,3])
        print(next(M))
    ```


## 生成器

1. 什么是生成器

	通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

	所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。
	
2. 创建一个generator:方式一

  只要把一个列表生成式的[]改成()，就创建了一个generator：

  	L = [x * x for x in range(10)]
  	#改为
  	g = (x * x for x in range(10))

  如果要一个一个打印出来，可以通过generator的next()方法：

  	print(g.__next__())
  	
  	#或者
  	
  	print(next(g))

  简单的方式
  ​	
  	for i in g:

    		print(i)
3. 创建一个generator:方式二

	generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

	比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
	
		def fib(max):
		    n, a, b = 0, 0, 1
		    while n < max:
		        print(b)
		        a, b = b, a + b
		        n = n + 1
		
		fib(10)
	
	>仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

	>也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print b改为yield b就可以了：
	
		def fib(max):
		    n, a, b = 0, 0, 1
		    while n < max:
		        yield b
		        a, b = b, a + b
		        n = n + 1
		
		nums=fib(10)
		
		for n in nums:
		    print(n)


## 闭包
1. 闭包设计范式

    # def counter(index=0):
    		#     count=[index]
    		#     def incr():
    		#         count[0]+=1
    		#         return count[0]
    		#     return incr


    ​		
    		def counter(index=0):
    		    count=index
    		    def incr():
    		        nonlocal count
    		        count+=1
    		        del count
    		        return count
    		    return incr
    		
    		inc=counter(5)
    		
    		print(inc())
    		print(inc())


    ​		
    		inc2=counter(50)


    ​		
    		print(inc2())
    		print(inc2())
    		
    		print(inc())
    		print(inc())

    **注意**

    1. 闭包优化了变量，原本需要类对象完成的工作，闭包就可以完成
    2. 由于闭包引用了外部函数的局部变量，则外部函数的局部变量不会被及时释放，所以消耗内存。