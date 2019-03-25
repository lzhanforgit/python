# 面向对象
### 设计模式
===
1. 简单工厂模式

	设计一个商品类和苹果手机类，同时设计一个苹果手机专卖店类。苹果手机专卖店类可以下订单和出售手机。运行效果
	
		ip=IphoneShop()

		ip.order()
		ip.order()
		ip.order()
		
		print('库存中共有:',IphoneShop.iphone_count,'台手机')
		
		ip.sail()
		ip.sail()
		ip.sail()
		ip.sail()
		
		运行结果：
			iphone X 正在出库
			iphone X 正在出库
			iphone X 正在出库
			库存中共有: 3 台手机
			售出一台手机，库存还有2台手机
			售出一台手机，库存还有1台手机
			售出一台手机，库存还有0台手机
			手机已经售完！！请进货
			
	代码如下
	
		class Goods(object):
		    def __init__(self,brand,price):
		        self.price=price
		        self.brand=brand
		    def outGoods(self):
		        print(self.brand,'正在出库')
		
		class Iphone(Goods):
		    def __init__(self,brand,price,name):
		        super(Iphone, self).__init__(brand,price)
		        self.name=name
		        print(self.name, '正在出库')
		    def outGoods(self):
		        print(self.name,'正在出库')
		class Sasung(Goods):
		    def __init__(self,brand,price,name,pencil):
		        super(Sasung, self).__init__(brand,price)
		        self.name=name
		        self.pencil=pencil
		        print(self.name, '正在出库')
		    def outGoods(self):
		        print(self.name,'正在出库')
		
		def createMobile(brand):
		    if brand=='apple':
		        return Iphone('apple',5600,'iphone X')
		    elif brand=='sasung':
		        return Sasung('sasung',4600,'galaxy s6','black pencil')
		
		class IphoneShop(object):
		    iphone_count = 0
		    def __init__(self):
		        self.iphone_count = 0
		    def order(self):
		        IphoneShop.iphone_count += 1
		        return createMobile('apple')
		
		    def sail(self):
		        if IphoneShop.iphone_count>0:
		            IphoneShop.iphone_count -= 1
		            print('售出一台手机，库存还有{0}台手机'.format(IphoneShop.iphone_count))
		        else:
		            print('手机已经售完！！请进货')
		ip=IphoneShop()
		
		ip.order()
		ip.order()
		ip.order()
		
		print('库存中共有:',IphoneShop.iphone_count,'台手机')
		
		ip.sail()
		ip.sail()
		ip.sail()
		ip.sail()
		
	工厂模式：
		
		class Goods(object):
		    def __init__(self,brand,price):
		        self.price=price
		        self.brand=brand
		    def outGoods(self):
		        print(self.brand,'正在出库')
		
		class Iphone(Goods):
		    def __init__(self,brand,price,name):
		        super(Iphone, self).__init__(brand,price)
		        self.name=name
		        print(self.name, '正在出库')
		class Sasung(Goods):
		    def __init__(self,brand,price,name,pencil):
		        super(Sasung, self).__init__(brand,price)
		        self.name=name
		        self.pencil=pencil
		        print(self.name, '正在出库')
		
		
		# def createMobile(brand):
		#     if brand=='apple':
		#         return Iphone('apple',5600,'iphone X')
		#     elif brand=='sasung':
		#         return Sasung('sasung',4600,'galaxy s6','black pencil')
		
		
		class MobileFactory(object):
		    def createMobile(self,brand):
		        if brand=='apple':
		            return Iphone('apple',5600,'iphone X')
		        elif brand=='sasung':
		            return Sasung('sasung',4600,'galaxy s6','black pencil')
		class Shop(object):
		    iphone_count = 0
		    def __init__(self):
		        self.factory=MobileFactory()
		    def order(self,brand):
		        IphoneShop.iphone_count += 1
		        return self.factory.createMobile(brand)
		
		    def sail(self):
		        if IphoneShop.iphone_count>0:
		            IphoneShop.iphone_count -= 1
		            print('售出一台手机，库存还有{0}台手机'.format(IphoneShop.iphone_count))
		        else:
		            print('手机已经售完！！请进货')
		ip=Shop()
		
		ip.order('apple')
		ip.order('sasung')
		ip.order('apple')
		
		print('库存中共有:',IphoneShop.iphone_count,'台手机')
		
		ip.sail()
		ip.sail()
		ip.sail()
		ip.sail()
2. 工厂方法模式
	简单工厂模式中MobileFactory对象由Shop类初始化来创建，这就决定了Shop只能创建MobileFactory对象。我们把MobileFactory对象交给Shop子类来创建，这样就扩展了Shop的功能。如下：
		
		class Shop(object):
		    def createGoods(self,brand):
		        pass
		    def order(self,brand):
		        pass
		    def sail(self):
		        pass
		
		class MobileShop(Shop):
		    Mobile_count=0
		    def createGoods(self,brand):
		        MobileShop.Mobile_count +=1
		        return MobileFactory().createMobile(brand)
		    def order(self,brand):
		        mobile=self.createGoods(brand)
		        print(mobile.name,'手机到货，库存为', MobileShop.Mobile_count)
		        return mobile
		    def sail(self):
		        if MobileShop.Mobile_count>0:
		            MobileShop.Mobile_count -= 1
		            print('售出一台手机，库存还有{0}台手机'.format(MobileShop.Mobile_count))
		        else:
		            print('手机已经售完！！请进货')
		ip=MobileShop()
		
		ip.order('apple')
		ip.order('sasung')
		ip.order('apple')
		
		
		
		ip.sail()
		ip.sail()
		ip.sail()
		ip.sail()
	
3. 单例模式预备 __new__

	\_\_new\_\_()必须要有返回值，返回实例化出来的实例，需要注意的是，可以return父类\_\_new\_\_()出来的实例，也可以直接将object的\_\_new\_\_()出来的实例返回。
	
	__init__()有一个参数self，该self参数就是__new__()返回的实例，__init__()在__new__()的基础上可以完成一些其它初始化的动作，__init__()不需要返回值。
	
	若__new__()没有正确返回当前类cls的实例，那__init__()将不会被调用，即使是父类的实例也不行
	
	>我们可以将类比作制造商，__new__()方法就是前期的原材料购买环节，__init__()方法就是在有原材料的基础上，加工，初始化商品环节。
	
		class A(object):
		    def __new__(cls, name,age):
		        print('new')
		        return object.__new__(cls)
		
		    def __init__(self,name,age):
		        self.name=name
		        self.age=age
		a1=A('tom',12)
		a2=A('tt',16)
		a3=A('ff',16)
4. 单例模式

		class A(object):
		    __instance=None
		    __first=False
		    def __new__(cls, name,age):
		        if not cls.__instance:
		            cls.__instance=object.__new__(cls)
		
		        return  cls.__instance
		
		    def __init__(self,name,age):
		        if not A.__first:
		            self.name=name
		            self.age=age
		            A.__first=True
		a1=A('tom',12)
		a2=A('tt',16)
		a3=A('ff',16)
		
		print(id(a1))