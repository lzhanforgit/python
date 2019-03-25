# 面向对象
### 高级
===
1. 动态添加属性

	* python可以动态为对象绑定属性，但是不会影响到同类的其他对象。
	
		```
			class Person:
			    pass
			p1=Person()
			p2=Person()
			p1.gender='male'
			print(p1.gender)
			print(p2.gender) #'Person' object has no attribute 'gender'
		```
	* 动态为对象绑定方法

		```
			from types import MethodType
			class Person:
			    pass
			def displayMe(self):
			    print('my genderis:', self.gender)
			# 给一个实例绑定的方法，对另一个实例是不起作用的：
			p1.dispalyMe=MethodType(displayMe,p1)
			p1.dispalyMe()
		```
	* 通过动态给类增加属性和方法，可以实现所有对象都增加了属性和方法

		```
			Person.gender='male'
			
			#定义一个类方法
			@classmethod
			def displayMe(cls):
    			print('my genderis:', self.gender)
    		
    		#定义一个静态方法
    		
    		@staticmethod
    		def showMe():
    			print('呵呵...')
    		Person.displayMe=displayMe
		```
	* 使用__slots__限制实例的属性.比如，只允许对Student实例添加name和age属性。

		**使用__slots__限制实例的属性只对当前对象起作用，对子类的对象不起作用**

		```
			class Person(object):
			    __slots__=('name','age')
			
			p1=Person()
			print(dir(p1))
			# 这是看到p1对象里已经存在name和age属性了
			try:
			    p1.gender = 'female'
			except Exception:
			    print('使用__slots__限制实例的属性')
		```
2. 删除属性

	

	```
			class Person:
			        def __init__(self):
        				self.age=1
			p1=Person()
			p2=Person()
			p1.gender='male'
			
			Person.nation='china'
			
			del p1.gender
			
			del p1.nation #error nation属于类的，不可以通过对象删除
			
			del Person.nation
			
			del p1.age #这是可以的
		
	```
	
	类属性也可以通过del动态删除
	
3. 利用函数动态绑定

	```	
		#该语句只能添加属性，不能添加方法
		setattr(ee2, 'age', 8) # 添加属性 'age' 值为 8
		getattr(ee1, 'age')   	# 返回 'age' 属性的值
		hasattr(ee1, 'age')   	# 如果存在 'age' 属性返回 True。
		delattr(ee1, 'age')  	# 删除属性 'age'
	```
4. 私有属性

	1、 _xx 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入。
	
	Python中没有真正的私有属性或方法,可以在你想声明为私有的方法和属性前加上单下划线,以提示该属性和方法不应在外部调用.如果真的调用了也不会出错,但不符合规范.

	2、 \_\_xx 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）

	3、 \_\_xx__定义的是特列方法。用户控制的命名空间内的变量或是属性，如init , __import__或是file 。只有当文档有说明时使用，不要自己定义这类变量。 （就是说这些是python内部定义的变量名）
	
	>python默认的成员函数和成员变量都是公开的,没有像其他类似语言的public,private等关键字修饰.但是可以在变量前面加上两个下划线"_",这样的话函数或变量就变成私有的.这是python的私有变量轧压(这个翻译好拗口),英文是(private name mangling.) **情况就是当变量被标记为私有后,在变量的前端插入类名,再类名前添加一个下划线"_",即形成了_ClassName\_\_变量名.
	
	```
		class pub():
			# protected类型的变量和方法 在类的实例中可以获取和调用
		    _name = 'protected类型的变量'
		    __info = '私有类型的变量'
		    def _func(self):
		        print("这是一个protected类型的方法")
		    def __func2(self):
		        print('这是一个私有类型的方法')
		    # 如果想要在实例中获取到类的私有类形变量可以通过在类中声明普通方法，返回私有类形变量的方式获取
		    def get(self):
		        return(self.__info)
		        
		p=pub()
		p.__info # error 因为__info是私有变量只有在类内部才可见，所以要用内部方法
	```
	
	复习：
	
	Python内置类属性
	
		__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
		__doc__ :类的文档字符串
		__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
		__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
5. 只读属性

  @ property 作用就是采用访问属性的方式访问函数。

  	class Car:
  	    __wheels=4
  	
  	    @property
  	    def wheels(self):
  	        return self.__wheels

  @property可以把方法变为属性，

  	class Car:
  	    __wheels=4
  	    __voice='didi'
  	    def __init__(self,color):
  	        self.color=color
  	        self.speed=80
  	    @property
  	    def run(self):
  	        print('i can run %d speed'%self.speed)
  	
  	    @run.setter
  	    def run(self,wh):
  	        self.speed=wh


  ​	
  ​	
  	car1=Car('blue')
  	
  	print(car1.color)
  	car1.run=120
  	car1.run

  **这个属性是不可以通过del car1.run 来删除的。因为他本来就不是一个属性**
  ​	
  	@run.deleter
  	def run(self):
  	    del self.speed
  	    print("你的车轮已经被拆除...")
6. 静态方法

	普通的方法，可以在实例化后直接调用，并且在方法里可以通过self.调用实例变量或类变量，但静态方法是不可以访问实例变量或类变量的，一个不能访问实例变量和类变量的方法，其实相当于跟类本身已经没什么关系了，它与类唯一的关联就是需要通过类名来调用这个方法。
	
		class Car:
		__wheels=4
		__voice='didi'
		def __init__(self,color):
		    self.color=color
		@property
		def wheels(self):
		    return self.__wheels
	
	  	#静态方法在类中也不需要传入 self参数
	    @staticmethod
	    def wash():
	        print('i am washing')
	
7. 类方法

	通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
	
		class Car:
		__wheels=4
		__voice='didi'
		def __init__(self,color):
		    self.color=color
		@property
		def wheels(self):
		    return self.__wheels
		
		@classmethod
		def dudu(cls):
		    print(cls.__voice)
		    
		@staticmethod
		def wash():
		    print('i am washing')
##多态

1. 多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）
2. 声明抽象方法

		import abc
		@abc.abstractmethod
		
3. 声明抽象类
		
		import abc
		class Animal(metaclass=abc.ABCMeta):
2. 通过继承实现

		import abc
		class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
		    @abc.abstractmethod
		    def talk(self):
		        pass
		 
		class People(Animal): #动物的形态之一:人
		    def talk(self):
		        print('say hello')
		 
		class Dog(Animal): #动物的形态之二:狗
		    def talk(self):
		        print('say wangwang')
		 
		class Pig(Animal): #动物的形态之三:猪
		    def talk(self):
		        print('say aoao')
		        
3. 什么是多态性（注意：多态与多态性是两种概念）

	多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。
		
		##多态性：定义统一的接口，#对于使用者来说，自己的代码根本无需改动
		def run(obj):
		    if isinstance(obj, Animal):
		        obj.talk()


		run(per)
		run(dog)
		run(pig)

4. 多态的优势

	1. 增加了程序的灵活性
	
		以不变应万变，不论对象千变万化，使用者都是同一种形式去调用，如run(animal)
　　	
	2. 增加了程序额可扩展性

		通过继承animal类创建了一个新的类，使用者无需更改自己的代码，还是用run(animal)去调用
