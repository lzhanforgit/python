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
2. 练习

	用户输入年龄，如果大于18岁，显示“成年”；否则显示“未成年”
3. 多条件
    
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

3. 练习

	商品价格100元，用户账户余额150元，请用户输入购买商品数量，如果数量大于1，显示用户余额不足，否则购买成功，并显示购买后的余额。
	
4. if嵌套

	```
		if 条件1:

        满足条件1 做的事情1
        满足条件1 做的事情2
        ...(省略)...

        if 条件2:
            满足条件2 做的事情1
            满足条件2 做的事情2
            ...(省略)...
	```
5. 练习

	商品价格100元，数量为5，用户账户余额150元，请用户输入购买商品数量，如果数量大于5,则显示库存不足；如果数量大于1，显示用户余额不足，否则购买成功，并显示购买后的余额。
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

4. 补充（**可以跳过**）

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
6. 课后练习

	石头剪刀布游戏：剪刀(0) 石头(1) 布(2)
	
	```
		import random

	    player = input('请输入：剪刀(0)  石头(1)  布(2):')
	
	    player = int(player)
	
	    computer = random.randint(0,2)
	
	    # 用来进行测试
	    #print('player=%d,computer=%d',(player,computer))
	
	    if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
	        print('获胜，哈哈，你太厉害了')
	    elif player == computer:
	        print('平局，要不再来一局')
	    else:
	        print('输了，不要走，洗洗手接着来，决战到天亮')
	```