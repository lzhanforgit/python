# 变量类型-Numbers
1. del

    ```
    num=1      
    mum=2      
    del num,mum    
    print(mum) 
    ```
2. Python math 模块、cmath 模块


    Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
    
    Python math 模块提供了许多对浮点数的数学运算函数。
    
    Python cmath 模块包含了一些用于复数运算的函数。
    
    cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
    
    要使用 math 或 cmath 函数必须先导入：
    
    ```
    import math
    #查看 math 查看包中的内容:
    dir(math)
    ```
    数学函数
    
    ```
        import math,cmath                    
        import random                        
        print(dir(math))                     
        print(dir(cmath))                    
        a=-12.57                             
        b=1.9                                
                                             
        print(math.fabs(a))                  
        print(math.floor(a))
        # 截断小数位
        print(math.trunc(a))               
        print(math.ceil(a))                  
        print(math.radians(a))               
                                             
        rana=random.choice(range(10))        
        print(rana)                          
                                             
        ranb=random.randrange(0,500,5)       
        print(ranb)                          
                                             
        ranc=random.random()                 
                                             
        print(ranc)                          
                                             
        arr=[1,2,3,4,5,6,7]                  
        #将序列的所有元素随机排序                        
        random.shuffle(arr)                  
                                             
        print(arr)                           
                                     
                                     
    ```
    ```
        >>> range(1,5)        # 代表从1到5(不包含5)
        [1, 2, 3, 4]
        >>> range(1,5,2)      # 代表从1到5，间隔2(不包含5)
        [1, 3]
        >>> range(5)          # 代表从0到5(不包含5)
        [0, 1, 2, 3, 4]
    ```
    >cmp(x, y) 函数在 python3.x 中不可用，可用以下函数替代：

    ```
    s='a'
    n=98
    print(ord(s)) # convert char to int 
    print(chr(n)) # convert int to char 
    ```

    >1、abs()是一个内置函数，而fabs()在math模块中定义的。
    >2、fabs()函数只适用于float和integer类型，而 abs() 也适用于复数。


3. decimal

    ```
        import decimal
        decimal.getcontext().prec=3
        m=2.0
        n=3.0

        d=decimal.Decimal(m)/decimal.Decimal(n)
        
        print(d)
    ```
4. 分数计算

    ```
        from fractions import Fraction
        f=Fraction(3,5)  #3/5
        f=f+1           #3/5+1=8/5

        f=f+Fraction(1,2)
        print(f)
    ```

5. bool

    ```
        x,y=3>2,3>5

        print(x,y) # True False
        
        print(bool('')) #False
        
    ```
6. None

    ```
        obj=None
        print(obj)
    ```

7. type()

    

