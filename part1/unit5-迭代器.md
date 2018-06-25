# 迭代器
1. 概述

    迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

2. 可迭代对象

    迭代器提供了一个统一的访问集合的接口。只要是实现了__iter__()或    __getitem__()方法的对象，就可以使用迭代器进行访问。
    
    　　  序列：字符串、列表、元组
    
    　　  非序列：字典、文件
    
    　　  自定义类：用户自定义的类实现了__iter__()或__getitem__()方法的对象
　　
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

    数组本身没有迭代对象
    
    ```
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
    
    
6. map() zip() filter()
    和range()不同，以上三个函数都是自己的迭代器
    
    ```
        M=map(abs,[2,-3,-1,3])
        print(next(M))
    ```


