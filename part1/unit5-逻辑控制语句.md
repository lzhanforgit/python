# 逻辑控制语句
1. 语法规则

    ```
        a=12
        if a>10:
            a=a+10;b=a+1
            c=a+\
                10+20+\
                10
            d=(a+10
               +20
               +30)
            print('a=',a)
            print('b=',b)
            print('c=',c)
            print('d=',d)
    ```
    
    1. 行结束没有分号
    2. 没有语句块大括号，使用语句缩进
    3. 条件部分没有括号
    4. 分号用于多条简单的语句放在同一行，作为分隔符
    5. 跨行可以使用‘\’，或者（），当然[],{}等也适合。

    demo
    
    ```
         while True:
            reply =input('Enter text:')
            if reply == 'stop':
                break
            elif not reply.isdigit():
                print('Bad'*8)
            else:
                print(int(reply)**2)
        print('bye')

    ```
1. 条件语句    

    ```
    if 判断条件：
        执行语句……
    else：
        执行语句……
    ```
    
    多条件
    
    ```
    if 判断条件1:
        执行语句1……
    elif 判断条件2:
        执行语句2……
    elif 判断条件3:
        执行语句3……
    else:
        执行语句4……
    ```
    >由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。

    **备注**
    python 复合布尔表达式计算采用短路规则，即如果通过前面的部分已经计算出整个表达式的值，则后面的部分不再计算。如下面的代码将正常执行不会报除零错误，但是如果改为or则会出错
    
    ```
    a=0
    b=1
    if ( a > 0 ) and ( b / a > 2 ):
        print "yes"
    else :
        print "no"
    ```

    Python 没有 switch/case 语句，如果遇到很多中情况的时候，写很多的 if/else 不是很好维护，这时可以考虑用字典映射的方法替代：
    
    ```
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    import os
    def zero():
        return "zero"
    
    def one():
        return "one"
    
    def two():
        return "two"
    
    def num2Str(arg):
        switcher={
            0:zero,
            1:one,
            2:two,
            3:lambda:"three"
        }
        func=switcher.get(arg,lambda:"nothing")
        return func()
    
    if __name__ == '__main__':
        print num2Str(0)
    ```
3. 三元运算符

    ```
        x=1

        # if x>0:
        #     a=True
        # else:
        #     a=False
        
        f=True if x>0 else False
        
        print(a)
    ```
2. 循环语句

    1.  while

        ```
        count = 0
        while count < 5:
           print count, " is  less than 5"
           count = count + 1
        else:
           print count, " is not less than 5"
        ```
    2. for

        ```
        #!/usr/bin/python
        # -*- coding: UTF-8 -*-
         
        for letter in 'Python':     # 第一个实例
           print '当前字母 :', letter
         
        fruits = ['banana', 'apple',  'mango']
        for fruit in fruits:        # 第二个实例
           print '当前水果 :', fruit
         
        print "Good bye!"
        ```
        
        ```
        fruits = ['banana', 'apple',  'mango']
        for index in range(len(fruits)):
            print '当前水果 :', fruits[index]
        else:
            print('over')
        ```
    
3. break
4. continue
5. range() zip()

    ```
        arr=[1,2,3,4,5,6,7,8]

        print(arr[1::2])
        print(arr[::2])
        
        for i in range(0,len(arr),2):
            print(i)
    ```
    ```
        arr1=['a','b','c']
        arr2=[97,98,99]
        
        
        li=list(zip(arr1,arr2))
        print(li)
        #转化为字典
        dic=dict(zip(arr1,arr2))
        print(dic)
        for(x,y) in zip(arr1,arr2):
            print(x,':',y)
    ```
    
    ```
        x,y,z=(1,2,3),(4,5,6),(7,8,9)

        li=list(zip(x,y,z))
        print(li)
        
        #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    ```
    
6. enumerate()

    enumerate()返回一个生成器对象
    
    ```
        arr1=['a','b','c']

        e=enumerate(arr1)
        
        print(next(e))
        
        for (index,item) in enumerate(arr1):
            print(index,'--->',item)
    ```
5. pass

    Python pass是空语句，是为了保持程序结构的完整性。

    pass 不做任何事情，一般用做占位语句。

    Python 语言 pass 语句语法格式如下：
    
    ```
        pass
    ```



