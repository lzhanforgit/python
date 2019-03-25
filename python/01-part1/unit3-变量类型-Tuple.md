# 变量类型-Tuple 

    
1. 特性

    和字符串一样，tuple一旦创建就不能改变。
    
    ```
        t1=(10)
        print(type(t1)) #<class 'int'>
        t2=(10,)
        print(type(t2)) #<class 'tuple'>
    ```


    ```
    tt=('python',['2.6','3.7'],'it')

    print(tt[1])

    tt[0]='java' #error
    
    tt[1][0]='2.5' #不会出错，因为引用没有改变                   
    ```

    任意无符号的对象，以逗号隔开，默认为元组

    ```
        x,y=1,2
        tup3 = "a", "b", "c", "d"
    ```
    
    ```
    	 x=(1)
	    y=(2,)
	    z=('a')
	    q=3,4,5
	
	    print(type(x))  #int
	    print(type(y))	#tuple
	    print(type(z))  #str
	    print(type(q))  #
    ```
2. 访问

    ```
        t2=(10,20,30,40)
        print(t2[0:2])
    ```
3. 修改

    修改元组是非法的
    元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
3. 删除

    ```
        del t2
    ```

4. 元组运算符

    与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

    Python| 表达式|	结果	描述|
    ---|---|---|
    len((1, 2, 3))|	3|	计算元素个数|
    (1, 2, 3) + (4, 5, 6)|	(1, 2, 3, 4, 5, 6)|	连接|
    ('Hi!',) * 4|	('Hi!', 'Hi!', 'Hi!', 'Hi!')|	复制|
    3 in (1, 2, 3)|	True|	元素是否存在|
    for x in (1, 2, 3): print (x,)|	1 2 3|	迭代|

5. index() count()

6. 和list比较

    ①、Tuple 与 list 的相同之处

    定义 tuple 与定义 list 的方式相同, 除了整个元素集是用小括号包围的而不是方括号。
    Tuple 的元素与 list 一样按定义的次序进行排序。 Tuples 的索引与 list 一样从 0 开始, 所以一个非空 tuple 的第一个元素总是 t[0]。
    负数索引与 list 一样从 tuple 的尾部开始计数。
    与 list 一样分片 (slice) 也可以使用。注意当分割一个 list 时, 会得到一个新的 list ；当分割一个 tuple 时, 会得到一个新的 tuple。

    ②、Tuple 不存在的方法

    您不能向 tuple 增加元素。Tuple 没有 append 或 extend 方法。
    您不能从 tuple 删除元素。Tuple 没有 remove 或 pop 方法。
    然而, 您可以使用 in 来查看一个元素是否存在于 tuple 中。

    ③、用 Tuple 的好处

    Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
    如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换。

    ④、Tuple 与 list 的转换

    Tuple 可以转换成 list，反之亦然。内置的 tuple 函数接收一个 list，并返回一个有着相同元素的 tuple。而 list 函数接收一个 tuple 返回一个 list。从效果上看，tuple 冻结一个 list，而 list 解冻一个 tuple。