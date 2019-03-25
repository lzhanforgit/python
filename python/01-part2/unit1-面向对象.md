# 面向对象
### 基础
===
1. oop

    面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
    Python类提供了面向对象编程的所有标准功能：类继承机制允许多个基类，派生类可以重写其基类或类的任何方法，并且方法可以调用具有相同名称的基类的方法。对象可以包含任意数量和种类的数据。与模块一样，类也具有Python的动态特性：它们是在运行时创建的，并且可以在创建后进一步修改。
2. 定义类

    ```
        class Employee:
        '所有员工的基类'
        # empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
        empCount = 0
    
        # 方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            Employee.empCount += 1
    
        # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        def displayCount(self):
            print ("Total Employee %d" % Employee.empCount)
            print (self.__class__)
    
        def displayEmployee(self):
            print("Name : ", self.name, ", Salary: ", self.salary)
        ee1= Employee('NICK',100000)
        ee2= Employee('ROSE',100000)
        
        ee1.displayCount()
        ee2.displayEmployee()
    ```
	>类属性使用 类名.属性名 的方式去访问，对象也可以访问。但是如果对象修改，则只对当前对象适用（因为这是其实是增加对象属性）
3. 动态为对象添加、删除属性

    只会影响到当前操作的对象
    
    ```
        ee1= Employee('NICK',100000)
        ee2= Employee('ROSE',888888)
        
        ee1.age=22
        print(ee1.age)
        # del ee1.name
        ee1.displayEmployee()
        
        # print ee2.age   #error
        
        print (hasattr(ee1, 'age') )   # 如果存在 'age' 属性返回 True。
        print (getattr(ee1, 'age') )   # 返回 'age' 属性的值
        setattr(ee2, 'age', 8) # 添加属性 'age' 值为 8
        print(ee2.age)
        delattr(ee1, 'age')  # 删除属性 'age'
    ```
4. 析构函数

    ```
            def __del__(self):
                class_name = self.__class__.__name__
                print(class_name, "销毁")
    ```

5. 内置属性

    ```
        print (Employee.__dict__)
        print (Employee.__doc__)
        # 类的所有父类构成元素（包含了一个由所有父类组成的元组）
        print (Employee.__bases__)
        ee1=Employee('NICK',200)
        dd2=ee1
        dd2.name='dog'
        # del ee1
        # ee1.displayEmployee()
        dd2.displayEmployee()
        print(isinstance(ee1,Employee))
        print(isinstance(ee1,object))
    ```
### 高级
===
6. 继承


    类的继承
    
    1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
    
    2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数
    
    3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
        
    ```
        class Boss(Employee):
            def __init__(self,name,salary,jiangjin):
                super(Boss, self).__init__(name, salary)
                self.jiangjin = jiangjin
        
        
            def displayEmployee(self):
                print("Name : ", self.name, ", Salary: ", self.salary,'other jiangjin:',self.jiangjin)
            def __str__(self):
            		pass
    ```
    >python没有重载，因为函数名知识指向内存地址的变量。
7. 多重继承

    ```
    #-*- coding:UTF-8 -*-

    # 多重继承
    
    class A(object):
        __scope='a scope'
        def __init__(self, a):
            print('init A...')
            self.a = a
        def show(self):
            print('i am A')
    
    class B(A):
        def __init__(self, a):
            super(B, self).__init__(a)
            print( 'init B...')
        def show(self):
            super(B,self).show()
            print(' and i am B too')
    
    class C(A):
        def __init__(self, a):
            super(C, self).__init__(a)
            print('init C...')
    
        def show(self):
            super(C, self).show()
            print(' and i am C too too')
    
    class D(B, C):
        def __init__(self, a):
            super(D, self).__init__(a)
            print('init D...')
        def show(self):
            super(D, self).show()
            print(' and i am D too too...')
    
    d=D(12)
    # print B.scope
    d.show()
    
    
    #d多重继承时为了从多个类中提取多个方法
    
    # 查看对象信息
    
    # print(isinstance(d,D))
    # print(isinstance(d,A))
    #
    # print(type(d))
    # print(dir(d))
    ```
8. 你真的理解Python中MRO算法吗？

	MRO（Method Resolution Order）：方法解析顺序。
	Python语言包含了很多优秀的特性，其中多重继承就是其中之一，但是多重继承会引发很多问题，比如二义性，Python中一切皆引用，这使得他不会像C++一样使用虚基类处理基类对象重复的问题，但是如果父类存在同名函数的时候还是会产生二义性，Python中处理这种问题的方法就是MRO。
	
	http://python.jobbole.com/85685/
8. 使用接口的思想设计多重继承

	整体可以分为类型类和功能类两种类，类型类实现主体继承树形结构，功能类作为独立的功能接口存在。
	
	```
		#-*- coding:UTF-8 -*-
		
		# 多重继承
		
		class Animal(object):
		    def __init__(self,age):
		        self.age=age
		
		# 大类:
		class Mammal(Animal):
		    def __init__(self,age,foot):
		        super(Mammal,self).__init__(age)
		        self.foot=foot
		
		class Bird(Animal):
		    def __init__(self,age,fly):
		        super(Bird,self).__init__(age)
		        self.fly=fly
		
		
		
		class RunnableMixIn(object):
		    def run(self):
		        print('Running...')
		
		class FlyableMixIn(object):
		    def fly(self):
		        print('Flying...')
		
		# 各种动物:
		class Dog(Mammal,RunnableMixIn):
		    def __init__(self,age,foot,gender):
		        super(Dog,self).__init__(age,foot)
		        self.gender=gender
		    def show(self):
		        print('dog age is:',self.age,'ang have ',self.foot)
		class Bat(Mammal, RunnableMixIn, FlyableMixIn):
		    pass
		
		class Parrot(Bird,RunnableMixIn, FlyableMixIn):
		    pass
		
		class Ostrich(Bird,RunnableMixIn):
		    pass
		
		dog=Dog(3,4,'male')
		
		dog.show()
	```