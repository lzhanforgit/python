# 函数
0. 为什么要用函数？
1. 定义一个函数

    你可以定义一个由自己想要功能的函数，以下是简单的规则：

    * 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
    * 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    * 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    * 函数内容以冒号起始，并且缩进。
    * return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
2. 可更改(mutable)与不可更改(immutable)对象


    在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    
    1. 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。    
    3. 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
    
    python 函数的参数传递：
    
    1. 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。  
    3. 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
    
    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
    
3. pip换源

	pip国内的一些镜像
	
	  阿里云 http://mirrors.aliyun.com/pypi/simple/ 
	  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
	  豆瓣(douban) http://pypi.douban.com/simple/ 
	  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
	  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
	
	修改源方法：
	
	临时使用： 
	可以在使用pip的时候在后面加上-i参数，指定pip源 
	eg: pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple

3. 参数

   以下是调用函数时可使用的正式参数类型：

    *    必备参数
    *    默认参数
    *    不定长参数
    *    关键字参数
    *	  命名关键字参数

    ```
    def show(name,age=12):
    print('name is:',name,'and age is',age)
    return
   
    # show()   #error
    
    show('tom',22)
    
    show(name='jack',age=32)
    show(name='rose')
    show(age=32,name='nick')
    ```

	python的默认值参数只会在函数定义处被解析一次，此后每次调用函数的时候，默认值参数都会是这个值了。碰到一些不可变的数据类型比如：整型，字符串，元祖之类的还好，但如果碰到可变类型的数据比如数组的话，就会有发生一些意想不到的事情。
	
		def add_to(num, target=[]):
		    target.append(num)
		    print id(target), target


		改进：
		
		def add_to(num, target=None):
		    if target is None:
		        target = []
		        ...
		        
	>可变的数据类型，函数局部作用域里面的任何改变会保留在数据上；不可变的数据类型，发生的任何改变都只会体现在新生成的局部变量上    
	
	**不定长参数**

	    ```
	    def printinfo( arg1, *vartuple ):
	        #"打印任何传入的参数"
	       print "输出: "
	       print arg1
	       for var in vartuple:
	          print var
	       return;
	    
	    # 调用printinfo 函数
	    printinfo( 10 );
	    printinfo( 70, 60, 50 );
	    ```

    **关键字参数**

		```
    		def person(name, age,*args, **kw):
    			print('name:', name, 'age:', age,'args',args, 'other:', kw)
    			person('Bob', 35,'苏州', city='Beijing')
   ​				
   ​				person('Adam', 45, gender='M', job='Engineer')
			   	
			   	#也可以这么些
			   	extra = {'city': 'Beijing', 'job': 'Engineer'}
			   	person('Adam', 45, **extra)
		```

   \*\*extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

   **命名关键字参数**

   如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

	   	def person(name, age, *, city, job):
	   	    print(name, age, city, job)
   和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

   **如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：**

	   	def person(name, age, *args, city, job):
	   	    print(name, age, args, city, job)
   >命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
   命名关键字参数可以有缺省值，从而简化调用：

	   	def person(name, age, *, city='Beijing', job,**kargs):
	   	    print(name, age, city, job)
   由于命名关键字参数city具有默认值，调用时，可不传入city参数：

   总结：

   在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
4. 函数返回值

    ```
        def show(a,b):
            return a+b,a-b
        res=show(10,20)
        print(res) #(30,-10)
    ```
    >实际是利用的元组的特性

9. 匿名函数-lambda


    python 使用 lambda 来创建匿名函数。

    lambda只是一个表达式，函数体比def简单很多。
    
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    
    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
    
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。


    ```
    nation='china'
    show=lambda name,age=12: print('name is:',name,'and age is',age,nation)
    
    ```


    ```
        arr=[1,2,3,4,5,6]
    
        lam=lambda array:[i for i in array if i%2==0]
        
        arr2=lam(arr)
        
        print(arr2)
    ```
    
    字典排序
    
    	infors = [{"name":"wang","age":10},{"name":"xiaoming","age":20},{"name":"banzhang","age":10}]

		infors.sort(key=lambda x:x['age']) #根据age对字典排序

    函数嵌套

    ```
    def func():
        x=4
        action = (lambda n: x**n)      # Pass x in lIlanllally return action
        return action
    
    
    def makeAction():
        acts=[]
        for i in range(5):
            acts.append((lambda x:i**x))
        return acts
    
    atcs=makeAction()
    
    print(atcs[1](3))
    print(atcs[3](3))
    
    
    def makeActionB():
        acts=[]
        for i in range(5):
            acts.append((lambda x,i=i:i**x))  # i=i
        return acts
    
    atcsb=makeActionB()
    
    print(atcsb[1](3))
    print(atcsb[3](3))
    
    ```
    
    匿名函数优点

	* 使用Python写一些脚本时，使用lambda可以省去定义函数的过程，让代码更加精简。
	* 对于一些抽象的，不会被别的地方再重复使用的函数，有时候函数起个名字也是个难题，使用lambda不需要考虑命名的问题
	* 使用lambda在某些时候然后代码更容易理解

6. 变量作用域
    一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。

    变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
    2. 全局变量
    3. 局部变量
    全局变量和局部变量
    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

    小结：
    * 在函数外边定义的变量叫做全局变量
    * 全局变量能够在所有的函数中进行访问
    * 如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
    * 如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，"强龙不压地头蛇"
7. 全局变量想作用于函数内，需加 global

    ```
    nation='china'
    def show(name,age=12):
    
        #nation='hello'+nation #error
        global nation
        nation='usa'
        print('name is:',name,'and age is',age,'and nation is',nation)
        return
    
    # show()
    
    show('tom',22)
    
    
    print(nation)
    ```

    ```
    def add_b():
        global  b
        b = 42
        def do_global():
            global  b
            b = b + 10
            print(b)
        do_global()
        print(b)
    add_b()
    print(b)
    ```

    ```
    def add_b():
        #global  b
        b = 42
        def do_global():
            global  b
            b =  10
            print(b)
        do_global()
        print(b)
    add_b()
    print(" b = %s " % b)
    ```

    * 在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
    * 对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
    * 对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。
8. 内置作用域（LEBG）

    ```
        import builtins
        print(dir(builtins  ))
    ```
    >内置文件中前一部分是内置异常，后一部分是内置函数。
10. nonlocal

    nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。

    ```
    def outer():
        x=100
        def inner():
            nonlocal x
            x=x+1000
            print(x)
    
        return inner
    
    inner=outer()
    
    inner()
    ```

11. 内置函数补充

	0. sum() 方法对系列进行求和计算。

			sum([0,1,2])  
			sum((2, 3, 4), 1)    #元组计算总和后再加 1
			sum([0,1,2,3,4], 2)

   1. map()

   			把所有列表元素字符串化
   	
   			list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
   2. reduce

   		reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
   		在Python 3里，reduce()函数已经被从全局名字空间里移除了，它现在被放置在fucntools模块里

   		用的话要 先引入from functools import reduce
   	
	   		from functools import reduce
	   		arr=[2,3,4]
	   		
	   		def total(x,y):
	   		    return x*2+y*2
	   		print(reduce(total,arr))
	   		
	   		
	   	案例：实现字符串反转
	   	
	   		result = reduce(lambda x,y:y+x,s)
   3. filter

	   		arr=[2,3,4]
	
	   		res=filter(lambda x:x%2==0,arr)
	   		
	   		print(list(res))
	   		
	   		??arr=['张晓明','张三丰','王重阳']
	   		#找出姓张而且单名的人
   4. sorted

   		sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
   	​	
   		users=[
   		    {'id':'008','user_name':'admin','user_password':'888','type':0},
   		    {'id':'002','user_name':'joke','user_password':'777','type':1},
   		    {'id':'001','user_name':'nose','user_password':'777','type':1}
   		]
   		
   		res=sorted(users,key=lambda u:u['id'])
   		
   		res=sorted(users,key=lambda user:user['id'],reverse=True)
   
   5. zip()

   		zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

		如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
		
			a = [1,2,3]
			b = [4,5,6]
			c = [4,5,6,7,8]
			zipped = zip(a,b)     # 打包为元组的列表
				#[(1, 4), (2, 5), (3, 6)]
			zip(a,c)              # 元素个数与最短的列表一致
				#[(1, 4), (2, 5), (3, 6)]
			zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
				#[(1, 2, 3), (4, 5, 6)]
				
	6. enumerate() 

		函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
		
			seasons = ['Spring', 'Summer', 'Fall', 'Winter']
			list(enumerate(seasons))
				#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
			list(enumerate(seasons, start=1))       # 小标从 1 开始
				#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

			
			seq = ['one', 'two', 'three']
			for i, element in enumerate(seq):
				print(i, seq[i])
	7. vars() 函数返回对象object的属性和属性值的字典对象。
	8. reversed 函数返回一个反转的迭代器。
12. 查看系统内置函数

   print(dir(__builtins__))

