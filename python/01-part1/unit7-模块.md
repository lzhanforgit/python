# 模块

1. 介绍

    Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

    模块让你能够有逻辑地组织你的 Python 代码段。
    
    把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
    
    模块能定义函数，类和变量，模块里也能包含可执行的代码。

2. import（导入模块）

	
    module_a.py
    
    ```
    #!/Users/lzhan/Lzhan/python/project/unit1 
    # -*- coding: UTF-8 -*-
    def add(a,b):
      return a+b
    version='1.0'
    print('add is end')
    # print __name__=="__main__" # 结果为false
    ```
    
    main.py
    
    ```
    # -*- coding:UTF-8 -*-
    # 第一种应用方式--导入模块
    
    # import module_a
    
    # print module_a.add(10,20)
    # dir(module_a) # get list of attributes for sys module
    # 第二种调用方式--从模块导入内部属性或方法
    from module_a import add,version
    print (add(10,20))
    print (version)
    
    print( __name__=='__main__')
    ```
    
    补充：
    
    ```
    #!/Users/lzhan/Lzhan/python/project/unit1 
    # -*- coding: UTF-8 -*-
    import sys
    print 'test import and arguments'
    for i in sys.argv:
      print(i)
    
    print (__name__=="__main__")
    
    print( 'end')
    
    print (__name__)
    
    print( sys.path)
    
    print (dir())    

    ```
    
    **当导入包文件夹的情况下,多级目录使用.作为分隔符,使用模块的时候，也要全部引入**
    
    ```
    	
    	import dir01.dir02.moudule
    	
    	#调用模块中的内容
    	dir01.dir02.moudule.func()
    	
    	或者
    	import dir01.dir02.moudule as m
    	
    	m.func()
    	
    	
    ```
3. from 模块 import *（模块内部的元素）

    ```
    from module_a import add,version
    ```
4. **搜索路径**
	
	当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

    1. 当前目录
    2. 如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
    3. 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

    
    模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
    
    查看系统目录
    
    	import sys
    	print(sys.path)
    	
    如果动态添加搜索路径可以这么做
    
    	sys.path.append('/Users/lzhan/AI/Python 1.x')
    	
    	
4. globals() 和 locals() 函数


    根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
    
    如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
    
    如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
    
    两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。


5. reload() 函数


    当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
    
    因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：

    ```
        reload(module_name)
        在这里，module_name要直接放模块的名字，而不是一个字符串形式。比如想重载 hello 模块，如下：
        
        reload(hello)
    ```
    
6. Python中的包


    包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
    
    简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包。

1. 