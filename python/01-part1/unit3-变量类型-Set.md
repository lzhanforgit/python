# 变量类型-Set

    
1. 特性

    set是一个无序且不重复的元素集合。

    集合对象是一组无序排列的可哈希的值，集合成员可以做字典中的键。集合支持用in和not in操作符检查成员，由len()内建函数得到集合的基数(大小)， 用 for 循环迭代集合的成员。但是因为集合本身是无序的，不可以为集合创建索引或执行切片(slice)操作，也没有键(keys)可用来获取集合中元素的值。

    set和dict一样，只是没有value，相当于dict的key集合，由于dict的key是不重复的，且key是不可变对象因此set也有如下特性：

    * 不重复

    * 元素为不可变对象

2. 创建

    ```
    s = set()
    s = {11,22,33,44}  #注意在创建空集合的时候只能使用s=set()，因为s={}创建的是空字典
    
    s1={}
    s2={1}
    s3=set()
    print(type(s1)) #dict
    print(type(s2)) #set
    print(type(s3)) #set
    ```

    ```
    a=set('body')
    b=set(['y', 'b', 'o','o'])
    c=set({"k1":'v1','k2':'v2'})
    d={'k1','k2','k2'}
    e={('k1', 'k2','k2')}
    ```
3. 基本操作

	 1. 添加

	 		se.add(1)

    1. discard()-移除不存的元素不会报错

    
        ```
            se = {11, 22, 33}
            se.discard(11)
            se.discard(44)  # 移除不存的元素不会报错
            print(se)
        ```

    2. remove(44)-移除不存的元素会报错

        ```
            se = {11, 22, 33}
            se.remove(11)
            se.remove(44)  # 移除不存的元素会报错
            print(se)
        ```
    3. pop()-移除末尾元素

        ```
            se = {11, 22, 33}  # 移除末尾元素并把移除的元素赋给新值
            temp = se.pop()
            print(temp)  # 33
        ```
    4. intersection() -取交集，赋给新值

        ```
            se = {11, 22, 33}
            be = {22, 55}

            temp1 = se.intersection(be)             #取交集，赋给新值
            print(temp1)  # 22
            print(se)  # {11, 22, 33}

            temp2 = se.intersection_update(be)      #取交集并更新自己
            print(temp2)  # None
            print(se)  # 22
        ```
4. 判断

    ```
        se = {11, 22, 33}
        be = {22}

        print(se.isdisjoint(be))        #False，判断是否不存在交集（有交集False，无交集True）
        print(se.issubset(be))          #False，判断se是否是be的子集合
        print(se.issuperset(be))        #True，判断se是否是be的父集合
    ```
5. 合并（se和be的并集 减去 se和be的交集）

    ```
        se = {11, 22, 33}
        be = {22,55}

        temp1 = se.symmetric_difference(be)  # 合并不同项，并赋新值
        print(temp1)    #{33, 11, 55}
        print(se)       #{33, 11, 22}

        temp2 = se.symmetric_difference_update(be)  # 合并不同项，并更新自己
        print(temp2)    #None
        print(se)             #{33, 11, 55}
    ```
6. 取并集

    ```
        se = {11, 22, 33}
        be = {22,44,55}

        temp=se.union(be)   #取并集，并赋新值
        print(se)       #{33, 11, 22}
        print(temp)     #{33, 22, 55, 11, 44}
    ```
	合并且更新

    ```
        se = {11, 22, 33}
        be = {22,44,55}

        se.update(be)  # 把se和be合并，得出的值覆盖se
        print(se)
        se.update([66, 77])  # 可增加迭代项
        print(se)
    ```

8. 类型转化

    ```
        se = set(range(4))
        li = list(se)
        tu = tuple(se)
        st = str(se)
    ```