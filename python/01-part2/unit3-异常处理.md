# 异常处理

===
1. 异常的定义

	程序执行过程中出现问题导致程序无法执行

	异常的分类：
	
	* 程序遇到逻辑或算法错误
		
	* 运行过程中计算机错误：内存不够或者io错误
	
	异常的步骤：
	
	* 异常产生，检查到错误且解释器认为是异常，抛出异常
		
	* 异常处理，异常处理，截获异常，系统忽略或者终止程序处理异常
2. 常见的异常

	* 	AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
	* 
	* 	IOError 输入/输出异常；基本上是无法打开文件
	* 	
	* 	ImportError 无法引入模块或包；基本上是路径问题或名称错误
	* 	
	* 	IndentationError 语法错误（的子类） ；代码没有正确对齐
	* 	
	* 	IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
	* 	
	* 	KeyError 试图访问字典里不存在的键
	* 	
	* 	KeyboardInterrupt Ctrl+C被按下
	* 	
	* 	NameError 尝试访问一个没有申明的变量
	* 	
	* 	SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
	* 	
	* 	TypeError 传入对象类型与要求的不符合
	* 	
	* 	UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
	* 	
	* 	ValueError 传入一个调用者不期望的值，即使值的类型是正确的
3. 所有的异常

	```
		异常名称    			描述
		BaseException    	所有异常的基类
		SystemExit    		解释器请求退出
		KeyboardInterrupt   用户中断执行(通常是输入^C)
		Exception    			常规错误的基类
		StopIteration    	迭代器没有更多的值
		GeneratorExit    	生成器(generator)发生异常来通知退出
		StandardError    	所有的内建标准异常的基类
		ArithmeticError    	所有数值计算错误的基类
		FloatingPointError    浮点计算错误
		OverflowError    	数值运算超出最大限制
		ZeroDivisionError    除(或取模)零 (所有数据类型)
		AssertionError    	断言语句失败
		AttributeError    	对象没有这个属性
		EOFError    			没有内建输入,到达EOF 标记
		EnvironmentError    操作系统错误的基类
		IOError    			输入/输出操作失败
		OSError    			操作系统错误
		WindowsError    		系统调用失败
		ImportError    		导入模块/对象失败
		LookupError   		无效数据查询的基类
		IndexError    		序列中没有此索引(index)
		KeyError    			映射中没有这个键
		MemoryError    		内存溢出错误(对于Python 解释器不是致命的)
		NameError    			未声明/初始化对象 (没有属性)
		UnboundLocalError    访问未初始化的本地变量
		ReferenceError    	弱引用(Weak reference)试图访问已经垃圾回收了的对象
		RuntimeError    		一般的运行时错误
		NotImplementedError    尚未实现的方法
		SyntaxError    		Python 语法错误
		IndentationError    缩进错误
		TabError    			Tab 和空格混用
		SystemError    		一般的解释器系统错误
		TypeError    			对类型无效的操作
		ValueError    		传入无效的参数
		UnicodeError    		Unicode 相关的错误
		UnicodeDecodeError  Unicode 解码时的错误
		UnicodeEncodeError  Unicode 编码时错误
		UnicodeTranslateError    Unicode 转换时错误
		Warning    警告的基类
		DeprecationWarning  关于被弃用的特征的警告
		FutureWarning    	关于构造将来语义会有改变的警告
		OverflowWarning    	旧的关于自动提升为长整型(long)的警告
		PendingDeprecationWarning    关于特性将会被废弃的警告
		RuntimeWarning    	可疑的运行时行为(runtime behavior)的警告
		SyntaxWarning    	可疑的语法的警告
		UserWarning    		用户代码生成的警告
	```
3. 如何处理异常

	```
		num2=input('>>: ') #输入一个字符串试试
		int(num2)
	```
	
	用常规方法解决
	
	```
		num1=input('>>: ') #输入一个字符串试试
		if num1.isdigit():
		    int(num1) #我们的正统程序放到了这里,其余的都属于异常处理范畴
		elif num1.isspace():
		    print('输入的是空格,就执行我这里的逻辑')
		elif len(num1) == 0:
		    print('输入的是空,就执行我这里的逻辑')
		else:
		    print('其他情情况,执行我这里的逻辑')
	```
	
	
	
4. 异常处理格式

	```
		try:
			<语句>        #运行别的代码
		except <异常类型>：
			<语句>        #如果在try部份引发了'name'异常
		# python2 和 3 处理 except 子句的语法有点不同，需要注意；
		# python2 用的是‘，’ 而三用的是 ‘as’
		except <异常类型> as <数据>:
			<语句>        #如果引发了'name'异常，获得附加的数据
		else:
			<语句>        #如果没有异常发生
	```
	例如

	```
        try:
            print(y)
        except NameError as e:
            print("变量名没有定义的错误信息：",e)
        else:
            print('没有发生异常')
	```

	同时有else和finally语句


	```
	try:
        y=0
        print(y)
    except NameError as e:
        print("Oops!  That was no valid number.  Try again...",e)
    else:
        '''保护不抛出异常的代码'''
        print('我必须在finally 上面，没有发生异常就执行')
    finally:
        print('不管有没有发生异常都会执行')
	```

	**异常类只能用来处理指定的异常情况，如果非指定异常则无法处理。（异常是由程序的错误引起的，语法上的错误跟异常处理无关，必须在程序运行前就修正）**
5. 多分支结构

    ```
        try:
            print(y)
            print('ss'+y)
        except RuntimeError as e:
            print("Oops!  RuntimeError.  Try again...",e)
        except TypeError as e:
            print("Oops!  TypeError.  Try again...",e)
        except NameError as e:
            print("Oops!  NameError.  Try again...",e)
        except ValueError as e:
            print("Oops!  ValueError.  Try again...",e)
        except:
            print("Unexpected error:", sys.exc_info()[0])
    ```
    >异常只会捕获一次

    也可以这么写：

    ```
        try:
            x = int(input("Please enter a number: "))
            break
         except (RuntimeError, TypeError, NameError,ValueError):
            print("Oops!  That was no valid number.  Try again...")
    ```

	万能异常
    在python的异常中，有一个万能异常：Exception，他可以捕获任意异常

    ```
        s1 = 'hello'
        try:
            int(s1)
        except Exception as e:
            '丢弃或者执行其他逻辑'
            print(e)
    ```
6. raise主动触发异常
    我们可以使用raise语句自己触发异常

    raise语法格式如下：

    raise [Exception [, args [, traceback]]]
    语句中Exception是异常的类型（例如，NameError）参数是一个异常参数值。该参数是可选的，如果不提供，异常的参数是"None"。

    最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。

    ```
        try:
           raise TypeError('我是故意的')
        except RuntimeError as e:
            print("Oops!  RuntimeError.  Try again...",e)
        except TypeError as e:
            print("Oops!  TypeError.  Try again...",e)
        except NameError as e:
            print("Oops!  NameError.  Try again...",e)
        except ValueError as e:
            print("Oops!  ValueError.  Try again...",e)

    ```

7. 自定义异常

    ```
        class MyException(RuntimeError):
    def __index__(self,arg):
        self.args=arg

    try:
        raise MyException('OH,NO!')
    except MyException as e:
        print(e)
    ```

    ```
        class MyException(RuntimeError):
            def __index__(self,arg):
                self.args=arg

        try:
            print(y)
            raise MyException('OH,NO!')
        except MyException as e:
            print(e)
        except NameError as e:
            print(e)
    ```

    >自定义异常可以和系统异常一起工作

    异常被其他异常拦截

    ```
        class MyException(RuntimeError):
            def __index__(self,arg):
                self.args=arg

        try:
            # print(y)
            raise MyException('OH,NO!')
        except Exception as e:
            print('HERE',e)
        except MyException as e:
            print(e)
        except NameError as e:
            print(e)
    ```

    综合案例

    ```
        import sys
        #自定义异常处理类，继承Exception类
        class CustomInputException(Exception):
            '''a user-defined exception class '''
            def __init__(self,length,atleast):
                Exception.__init__(self)
                self.length=length
                self.atleast=atleast
        try:
            s = input('Enter something --> ')
            if len(s)<3:
                # raise可以触发自定义异常
                raise CustomInputException(len(s),3)

        except EOFError:
            print('\nWhy did you do an EOF on me?')
            sys.exit() # exit the program
        except CustomInputException as x:
            print ('\n自定义异常类被触发，原因：输入字长度为:%d,\
            输入字符串长度必须大于%d'%(x.length,x.atleast)) # here, we are not exiting the program
        except:
            print('\nSome error/exception occurred.')  # here, we are not exiting the program
        else:
            print('没有发生异常')
        print('Done')

    ```