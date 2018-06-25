# 模块

1. import如何工作

    **导入只发生一次**
    2. 找到模块文件
    3. 编译成位码（需要时）
    4. 执行模块的代码来创建其所定义的对象

    >Python把导入的模块存贮到sys.moudles表中，并在导入操作的时候检查该表，如果模块不存在，将会启动上面三个步骤。
2. 搜索

    大多数情况下，可以依赖模块导入的路径来搜索路径，不需要额外配置路径。但是，也可以自己预定义路径，那么搜索的顺序：
    1. 程序的主目录
    2. PYHONPATH目录（如果已经进行了设置）

        ```
            import sys
            print(list(sys.path))
            #手动添加目录
            sys.path.append('c:\\python\\modules')
            sys.path.append('c:/python/modules')

        ```
    3. 标准链接库目录

    4. 任何.pth文件的内容（如果存在的话）
    
        在python安装路径的site-packages目录下修建了PckPath.pth文件

    ```
        /Users/lzhan/AI/python/project_modules/modules
    ```
3. 编译

    >当文件导入时，就会进行编译。因此、通常不会看到程序顶层文件的.pyc字节码文件。除非这个文件也被其他文件导入：只有被导入的文件才会留下字节码文件。顶层文件的字节码是在内部使用后就丢弃了。
4. 执行

    和def一样，import和form是可执行语句，而不是在编译期间的声明。直到python执行到这些语句时，才会进行解析。
4. distutils
5. from

    from会把模块中的变量复制到另一个作用域，所以顶层文件中就可以直接使用该变量了。
    
    ```
        import modulea
        from modulea import * #等价
    ```
    >from语句智能用在模块文件的顶部，不能放在函数中。
    
    所以下面代码是等价的
    
    ```
        from module import name1,name2
        #等价于
        import module
        name1=module.name1
        name2=module.name2
        del module
    ```
    
    from语句有破坏命名空间的潜质！！
6. 查看模块命名空间

    ```
    import public_var as p                                          
    print(p.__dict__)              
    print(dir(p))                  
    ```
7. reload()

    1. reload是Python的内置函数，而不是语句
    2. reload只能重载已经存在的模块对象，而不是变量
    3. relaod必须手动导入

        ```
        import public_var as p
        from importlib import reload
        
        print(p.urls['first'])
        
        p.urls['first']='baidu.com'
        
        print(p.urls['first'])
        
        reload(p)
        print(p.urls['first'])
        ```

    
8. 包导入

    ```
        import modules.public_var
        from modules.public_var import *
    ```
    **注意**
    作为包的目录内必须存在__init__.py文件。
# 在保重隐藏数据


