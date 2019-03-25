# 逻辑控制语句-for
2. 循环语句
	0. 循环

		```
			i = 0
		    while i<10000:
		        print("媳妇儿，我错了")
		        i+=1
		```
    1.  while

        ```
        count = 0
        while count < 5:
           print(count, " is  less than 5")
           count = count + 1
        else:
           print(count, " is not less than 5")
        ```
    3. 练习

    	计算1~100之间偶数的累积和（包含1和100）
    	
    4. 嵌套循环
    
		
		```
			i = 1
		    while i<=5:
		
		        j = 1
		        while j<=5:
		            print("* ",end='')
		            j+=1
		
		        print("\n")
		        i+=1
		```
   		 
    5. 练习
   			
   			```
   				 *
			    * *
			    * * *
			    * * * *
			    * * * * *
   			```
   			
   		九九乘法表
   			
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

	* break/continue只能用在循环中，除此以外不能单独使用

	* break/continue在嵌套循环中，只对最近的一层循环起作用
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
5. 课后练习

	选做题：

	1. 根据以下信息提示，请帮小明计算，他每月乘坐地铁支出的总费用
	
	提示信息:
	
	北京公交地铁新票价确定
	
	据北京市发改委网站消息称，北京市将从2015年12月28起实施公共交通新票价：地铁6公里(含)内3元，公交车10公里(含)内2元，使用市政交通一卡通刷卡乘公交车普通卡5折，学生卡2.5折。
	
	　　具体实施方案如下：
	
	　　一、城市公共电汽车价格调整为：10公里(含)内2元，10公里以上部分，每增加1元可乘坐5公里。使用市政交通一卡通刷卡乘坐城市公共电汽车，市域内路段给予普通卡5折，学生卡2.5折优惠;市域外路段维持现行折扣优惠不变。享受公交政策的郊区客运价格，由各区、县政府按照城市公共电汽车价格制定。
	
	　　二、轨道交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元;22公里至32公里(含)6元;32公里以上部分，每增加1元可乘坐20公里。使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;满150元以后的乘次，价格给予5折优惠;支出累计达到400元以后的乘次，不再享受打折优惠。
	
	要求：
	
	假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁；每月月初小明第一次刷公交卡时，扣款5元；编写程序，帮小明完成每月乘坐地铁需要的总费用



