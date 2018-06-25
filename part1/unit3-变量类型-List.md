# 变量类型-List
1. list

    列表的数据项不需要具有相同的类型
    List（列表） 是 Python 中使用最频繁的数据类型。
    
    列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套。
5. 列表取值
    列表用 [ ] 标识，是 python 最通用的复合数据类型。
    
    列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
    
    加号 + 是列表连接运算符，星号 * 是重复操作。
    
    ```
    list=[1,3,5,7,9,11]
    print list               # 输出完整列表
    print list[:]
    print list[0]            # 输出列表的第一个元素
    print list[1:3]          # 输出第二个至第三个元素 
    print list[2:]           # 输出从第三个开始至列表末尾的所有元素
    print list[:5]
    print tinylist * 2       # 输出列表两次
    print list + tinylist    # 打印组合的列表
    
    for item in range(len(arr)):   
	   print(arr(item))        
	
	 for item in arr:   
	   print(item)               
    ```
2. list 操作

    ```
    fruits = ['orange', 'apple', 'pear', 'banana']

    # 统计
    # print (fruits.count('apple'))
    # 判断是否存在
    # print (fruits.index('apple'))
    # 从第三个位置开始寻找
    # print (fruits.index('apple',3))
    # fruits.reverse()
    # fruits.sort()
    
    # 增加元素
    # fruits.append('kiwi')
    # 增加集合
    # fruits.extend(['kiwi','water'])
    # 合并两个列表
    # new_fruits=fruits+['kiwi','water']
    # 插入元素
    # fruits.insert(0,'pick');
    
    # 删除元素
    # fruits.remove('apple')
    # del fruits[1]
    # 删除单个元素
    # fruits[1:2]=[]
    # 删除多个元素
    # fruits[2:4]=[]
    # 删除聊表末尾的元素
    # fruits.pop()
    
    # 替换元素
    # fruits[0:3]=['橙子','苹果','梨']
    
    # 清空元素
    # fruits.clear()
    # del fruits[:]  #不同于del fruits
    # fruits[ : ]=[]
    
    # 判断是否存在
    # print('apple' in fruits)
    
    # 最大最小值
    # print(max(fruits))
    # print(min(fruits))    
    ```
    
3. 栈和队列
    
    ```
    #!/Users/lzhan/Lzhan/python/project/unit2
    # -*- coding: UTF-8 -*-
    from collections import deque
    fruits = ['orange', 'apple', 'pear', 'banana']
    # from collections import deque
    #
    queue = deque(fruits)
    
    # 先进先出
    queue.appendleft('haha')
    queue.popleft()
    
    # 先进后出
    queue.append('')
    queue.pop()
    
    print(list(queue))
    ```

4. 列表初始化

    ```
        squares=[]
        squares=[x**2 for x in range(10)]
        vec = [-4, -2, 0, 2, 4]
        vec2=[x*2 for x in vec]
        vec3=[x for x in vec if x >= 0]
        vec4=[abs(x) for x in vec]
        
        print ([(x, x**2) for x in range(6)])
    ```
    
    ```
        squares=[]
        squares=list(map(lambda x: x**3, range(10)))
        lists=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
        # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    ```
    **补充：map()**
    
    map() 会根据提供的函数对指定序列做映射。

    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    
    
    ```
        map(function, iterable, ...)
    ```
    
    返回值
    Python 2.x 返回列表。
    
    Python 3.x 返回迭代器。
    
    ```
        arr=[1,2,3,4]

        mm=map(lambda x:x ** 2,arr)
        print(next(mm))
        
        for res in mm:
            print(res)

    ```
    去掉列表元素单词左右空格
    
    
    ```
        # freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
        #
        # # 去掉单词左右空格
        # freshfruit=[weapon.strip() for weapon in freshfruit]
    ```
    
    读取二维数组
    
    ```
        vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        list1=[num for elem in vec for num in elem]
        list2=[[elem[i] for elem in vec] for i in range(3)]
        print(list2)
    ```
5. 

