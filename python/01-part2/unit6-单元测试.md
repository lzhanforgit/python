# 单元测试
1. unittest核心工作原理

	unittest中最核心的四个概念是：test case, test suite, test runner, test fixture。
	* 一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。元测试(unit test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。
	* 而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。
TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法，就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例。
	* TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法。 
测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。
	* 而对一个测试用例环境的搭建和销毁，是一个fixture。

2. 先上一段代码

	calculate_func.py
		
		def add(a, b):
		    return a+b
		
		def minus(a, b):
		    return a-b
		
		def multi(a, b):
		    return a*b
		
		def divide(a, b):
		    return a/b
		    
	test_calculate_func.py
		
		#导入unittest模块
		import unittest
		from calculate_func import *
		
		
		class TestCalculateFunc(unittest.TestCase):
		    """Test calculate_func.py"""
			#每个测试方法均以 test 开头，否则是不被unittest识别的。
		    def test_add(self):
		        """Test method add(a, b)"""
		        self.assertEqual(3, add(1, 2))
		        self.assertNotEqual(2, add(2, 2))
		
		    def test_minus(self):
		        """Test method minus(a, b)"""
		        self.assertEqual(1, minus(3, 2))
		
		    def test_multi(self):
		        """Test method multi(a, b)"""
		        self.assertEqual(6, multi(2, 3))
		
		    def test_divide(self):
		        """Test method divide(a, b)"""
		        self.assertEqual(2, divide(6, 3))
		        self.assertEqual(2.5, divide(5, 2))
		
		if __name__ == '__main__':
		    unittest.main()
		 
	一个class继承了unittest.TestCase，便是一个测试用例，但如果其中有多个以 test 开头的方法，那么每有一个这样的方法，在load的时候便会生成一个TestCase实例，如：一个class中有四个test_xxx方法，最后在load到suite中时也有四个测试用例。
	
	写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。这里加个说明，在Runner执行时，默认将执行结果输出到控制台，我们可以设置其输出到文件，在文件中查看结果（HTMLTestRunner，通过它可以将结果输出到HTML中，生成漂亮的报告，它跟TextTestRunner是一样的，从名字就能看出来，这个我们后面再说）。
	
3. TestSuite

	上面的代码示例了如何编写一个简单的测试，但有两个问题，我们怎么控制用例执行的顺序呢？（这里的示例中的几个测试方法并没有一定关系，但之后你写的用例可能会有先后关系，需要先执行方法A，再执行方法B），我们就要用到TestSuite了。我们添加到TestSuite中的case是会按照添加的顺序执行的。

	问题二是我们现在只有一个测试文件，我们直接执行该文件即可，但如果有多个测试文件，怎么进行组织，总不能一个个文件执行吧，答案也在TestSuite中。
	
		import unittest
		from test_calculate_func import TestCalculateFunc
		
		if __name__ == '__main__':
		    suite = unittest.TestSuite()
		
		    tests = [TestCalculateFunc("test_add"), TestCalculateFunc("test_minus"), TestCalculateFunc("test_divide")]
		    suite.addTests(tests)
		
		    runner = unittest.TextTestRunner(verbosity=2)
		    runner.run(suite)
		    
	下面方法也可以传入测试用例
	
		# tests = [TestCalculateFunc("test_add"), TestCalculateFunc("test_minus"), TestCalculateFunc("test_divide")]
	    # suite.addTests(tests)
	    # # 直接用addTest方法添加单个TestCase
	    # suite.addTest(TestCalculateFunc("test_multi"))
	
	    # 用addTests + TestLoader
	    # loadTestsFromName()，传入'模块名.TestCase名'
	    # suite.addTests(unittest.TestLoader().loadTestsFromName('test_calculate_func.TestCalculateFunc'))
	    # suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_calculate_func.TestCalculateFunc']))
	
	    # loadTestsFromTestCase()，传入TestCase
	    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculateFunc))
	    runner = unittest.TextTestRunner(verbosity=2)
	    runner.run(suite)
	    
	**用TestLoader的方法是无法对case进行排序的，同时，suite中也可以套suite。**

3. 将测试结果写入文件

		if __name__ == '__main__':
	    suite = unittest.TestSuite()
	    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculateFunc))
	
	    with open('UnittestTextReport.txt', 'a') as f:
	        runner = unittest.TextTestRunner(stream=f, verbosity=2)
	        runner.run(suite)
4. unittest中的参数化

		pip3 install nose_parameterized
	
	--
		def login(username, password):
		    if username == 'xiaogang' and password == '123456':
		        return True
		    else:
		        return False
	
	测试用例模块
	
		from parameterized import parameterized
		
		class TestCalculateFunc(unittest.TestCase):
		    """Test mathfuc.py"""
		    # num = 1
		    @parameterized.expand(
		        [
		            ['xiaogang', '123456', True],  # 可以是list，也可以是元祖
		            ['', '123456', True],
		            ['xiaogang', '', False],
		            ['adgadg', '123456', False]
		        ]
		    )
		
		  
		    # @classmethod
		    # def tearDownClass(cls):
		    #     print("This tearDownClass() method only called once too.")
		    #     # cls.num=2
	
	
		    def test_login(self, username, passwd, flag):  # 这里的参数对应上述列表里的元素，运行的时候会遍历上述列表里的二维列表直到所有元素都调用运行完成
		        '''登录'''
		        res = login(username, passwd)
		        self.assertEqual(res, flag)
4. setUp() tearDown()

	setUp() 和 tearDown() 两个方法（其实是重写了TestCase的这两个方法），这两个方法在每个测试方法执行前以及执行后执行一次，setUp用来为测试准备环境，tearDown用来清理环境，已备之后的测试。
	**setUp和tearDown在每次执行case前后都执行了一次。**
	
		def setUp(self):
        print "do something before test.Prepare environment."

	    def tearDown(self):
	        print "do something after test.Clean up."
	        
	 如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们可以用类方法 setUpClass() 与 tearDownClass() (此处可以用类属性测试):
	 
	 	#导入unittest模块
		import unittest
		from calculate_func import *
		
		
		class TestCalculateFunc(unittest.TestCase):
		    """Test mathfuc.py"""
		    num=1
		    # def setUp(self):
		    #     print("do something before test.Prepare environment.")
		    #
		    # def tearDown(self):
		    #     print("do something after test.Clean up.")
		    @classmethod
		    def setUpClass(cls):
		        print("This setUpClass() method only called once.")
		        cls.num=0
		
		    @classmethod
		    def tearDownClass(cls):
		        print("This tearDownClass() method only called once too.")
		        cls.num=2
		    def test_add(self):
		        """Test method add(a, b)"""
		        self.assertEqual(3, add(1, 2))
		        self.assertNotEqual(2, add(2, 2))
		        print(TestCalculateFunc.num)
		
		    def test_minus(self):
		        """Test method minus(a, b)"""
		        self.assertEqual(1, minus(3, 2))
		        print(TestCalculateFunc.num)
		    def test_multi(self):
		        """Test method multi(a, b)"""
		        self.assertEqual(6, multi(2, 3))
		        print(TestCalculateFunc.num)
		    def test_divide(self):
		        """Test method divide(a, b)"""
		        self.assertEqual(2, divide(6, 3))
		        self.assertEqual(2.5, divide(5, 2))
		        print(TestCalculateFunc.num)

		if __name__ == '__main__':
		    unittest.main(verbosity=2)
5. 跳过某个case

	1. skip装饰器

			@unittest.skip("I don't want to run this case.")
	    	def test_divide(self):
	    		...
	    		
	    skip装饰器一共有三个 
	    
	    1. unittest.skip(reason)
	    
	    2. unittest.skipIf(condition, reason)		
	    3. unittest.skipUnless(condition, reason)
	    
	    skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
	    
	    	@unittest.skipIf(num>0,"num的值没有大于零")  #此处调用类属性不需要加类名
    		def test_add(self):
    			。。。
6. 用HTMLTestRunner输出漂亮的HTML报告

	我们能够输出txt格式的文本执行报告了，但是文本报告太过简陋，是不是想要更加高大上的HTML报告？但unittest自己可没有带HTML报告，我们只能求助于外部的库了。

	HTMLTestRunner是一个第三方的unittest HTML报告库，首先我们下载HTMLTestRunner.py，并放到当前目录下，或者你的’C:\Python27\Lib’下，就可以导入运行了。

	下载地址：

	[官方原版](http://tungwaiyip.info/software/HTMLTestRunner.html)
	
	[修改版](HTMLTestRunner.py已调整格式，中文显示)
	
	[Python3.x版本：](http://pan.baidu.com/s/1tp3Ts​)
	
7. 总结

	1. unittest是Python自带的单元测试框架，我们可以用其来作为我们自动化测试框架的用例组织执行框架。
	1. unittest的流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。
	1. 一个class继承unittest.TestCase即是一个TestCase，其中以 test 开头的方法在load时被加载为一个真正的TestCase。
	1. verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。
	1. 可以通过addTest和addTests向suite中添加case或suite，可以用TestLoader的loadTestsFrom__()方法。
	1. 用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境
	1. 我们可以通过skip，skipIf，skipUnless装饰器跳过某个case，或者用TestCase.skipTest方法。
	1. 参数中加stream，可以将报告输出到文件：可以用TextTestRunner输出txt报告，以及可以用HTMLTestRunner输出html报告。

8. unittest处理关联接口
	
	源文件
	
		def login(username, password):
		    if username == 'vip001' and password == '123456':
		        return 'vip'
		    else:
		        return False
		def buy(token):
		    if token == 'vip':
		        return True
		    else:
		        return False
		
		
	--
	测试用例
		
		    def login(self):  # 注意，这里不以test开头命名，就是一普通方法，在执行测试用例的时候并不会运行，调用的时候才会
		        res = login('vip001', '123456')
		        self.assertEqual(res, 'vip')
		        return res
		
		    def test_login_cj(self):
		        res = self.login()  # 调用登录方法，获取sign
		        self.jp = buy(res)
		        self.assertEqual(self.jp, True)
8. 进阶

	
	https://blog.csdn.net/column/details/12694.html?&page=2
