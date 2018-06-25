# 运算符&表达式
1. 赋值运算符

    ```
        str='spam'
        m,n=10,20
        [s1,s2]=['hello','python']
        a,b,c,d='spam'
        x,*y='spam' #等价于x,y='spam'[0],'spam'[1:]
        #x,*y,z='spam'
        e=f=20
        g+=20
    ```
    demo
    
    ```
        l=[1,2,3,4,5]
        while l:
            front,*l=l
            print(front)
    ```
    >注意： *l每次得到的都是一个列表，如果没有数据就是空列表。
1. 算术运算符    

    ```
        **	幂 - 返回x的y次幂	a**b 为10的20次方， 输出结果 100000000000000000000

        //	取整除 - 返回商的整数部分
        import math

        f=-3.89
        
        print(f//1)
        
        print(math.floor(f))
        print(math.trunc(f))
        # 9//2 输出结果 4 ,             
        9.0//2.0 输出结果 4.0
    ```
   

2. 比较运算符
    
    == 等于 - 比较对象是否相等
    <>或者！= 两者相同 #在python3中<>被移除
    
    比较预算符 x<y<z 等价于 x<y and  y<z

3. Python逻辑运算符

    *     and
    *     not
    *     or
4. Python成员运算符

    |运算符	|描述	|实例|
    |---|---|---|
    |in	|如果在指定的序列中找到值返回 True，否则返回 False。	|x 在 y 序列中 , 如果 x 在 y 序列中返回 True。|
    |not in	|如果在指定的序列中没有找到值返回 True，否则返回 False。	|x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。|

    ```
        arr=['python','java','c++']
        print('c++' in arr)
        print('c' not in arr)
    ```
5. Python身份运算符

    |运算符	|描述	|实例|
    |---|---|---|
    |is	|is 是判断两个标识符是不是引用自一个对象	|x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False|
    |is not	|is not 是判断两个标识符是不是引用自不同对象	|x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。|
    
    >is 与 == 区别：
    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

    ```
    a=20
    b=20
    c=30
    print(a is b) #True
    print(id(a)==id(b)) #True
    print(b is c) #False
    ```
    
    >
    python中会为每个出现的对象分配内存，哪怕他们的值完全相等（注意是相等不是相同）。如执行a=2.0，b=2.0这两个语句时会先后为2.0这个Float类型对象分配内存，然后将a与b分别指向这两个对象。所以a与b指向的不是同一对象：

    >但是为了提高内存利用效率对于一些简单的对象，如一些数值较小的int对象，python采取重用对象内存的办法，如指向a=2，b=2时，由于2作为简单的int类型且数值小，python不会两次为其分配内存，而是只分配一次，然后将a与b同时指向已分配的对象：

    **Python 中没有 ++ 或 -- 自运算符**


6. 强制类型转换

    ```
        int(3.1415)
        float(3)
    ```
    
    >python中类型转换仅限于数字，比如数字加上字符串则报错。
    
    ```
        res=3+'2.5' #error
        res=3+float('2.5')
    ```

