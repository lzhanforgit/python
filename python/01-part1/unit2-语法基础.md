# 基础语法
1. python全景

    1. 程序由模块组成
    2. 模块包含语句
    3. 语句包含表达式
    4. 表达式建立并处理对象

2. hello world
3. 注释
	4. 单行注释

		```
			#注释的内容
		```
	5. 多行注释

		python 中多行注释使用三个单引号(''')或三个双引号(""")

		```
			'''
				注释内容第一行
				注释内容第二行
			'''
		```
1. 中文编码

    只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
    
    ```
        # -*- coding: UTF-8 -*-
    ```
    >Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。
    
    >如果你使用编辑器，同时需要设置 py 文件存储的格式为 UTF-8.设置路径：file / setting / editor / file encodings
2. 交互式编程

    在命令行中输入python即可
4. 行和缩进

    学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。

    缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
    >建议你在每个缩进层次使用 单个制表符 或 两个空格 或 四个空格 , 切记不能混用
5. 多行语句

    Python语句中一般以新行作为语句的结束符。

    但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：

    ```
    total = item_one + \
        item_two + \
        item_three

    ```
    语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：

    ```
    days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
    ```    
7. 输入和输出

	输入
	
    ```
    #python2.x
    raw_input("按下 enter 键退出，其他任意键显示...\n") 
    
    #python3.x
    input("按下 enter 键退出，其他任意键显示...\n")
    ```
	**注意在python2.x中**
    *     input返回的是数值类型，如int,float
    *     input会计算在字符串中的数字表达式，而raw_input不会
    *     raw_inpout返回的是字符串类型，string类型’

    
    输出
    
    print() 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
    
    ```
    	age = 18
    	name = "xiaoming"
    	print("我的姓名是%s,年龄是%d"%(name,age))
    	print("我的姓名是',name,'年龄是',age)
    	
    ```
    常用的格式符号
    	
    	格式符号|转换|
    	---|---|
		%s|	通过str() 字符串转换来格式化|
		%d|	有符号十进制整数|
		%f|	浮点实数|
		
9. demo

	输出一张个人名片
	
	```
		'''
		# 用户名输入姓名
		name=input('请输入你的姓名')
		# 用户名输入电话
		tel=input('请输入你的电话号码')
		# 用户输入公司名称
		com=input('请输入你的公司名称')
		
		# 打印名片
		print('=======================')
		print('姓   名：%s'%name)
		print('电   话：%s'%tel)
		print('公司名称：%s'%com)
		print('=======================')
		'''
	```
	
8. 执行脚本传入参数

    ```
    import sys
    sys.path
    print sys.argv
    ```
    >sys.argv[0] 代表文件本身路径，所带参数从 sys.argv[1] 开始。
    
    脚本语言的第一行，目的就是指出，你想要你的这个文件中的代码用什么可执行程序去运行它，就这么简单。

    * \#!/usr/bin/python : 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器；
    
    * \#!/usr/bin/env python(推荐）: 这种用法是为了防止操作系统用户没有将 python 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。
    
    * \#!/usr/bin/python 相当于写死了python路径;
    
    * \#!/usr/bin/env python 会去环境设置寻找 python 目录,推荐这种写法
 

