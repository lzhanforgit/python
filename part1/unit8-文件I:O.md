# 文件I/O

1. raw_input() 和 input()

    nput([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
    
    ```
    #!/usr/bin/python
    # -*- coding: UTF-8 -*- 
     
    str = input("请输入：")
    print "你输入的内容是: ", str
    ```
    
    这会产生如下的对应着输入的结果：

    
    ```
    请输入：[x*5 for x in range(2,10,2)]
    你输入的内容是:  [10, 20, 30, 40]
    ```
2. 打开和关闭文件-open()

    ```
    file object = open(file_name [, access_mode][, buffering])
    ```
    各个参数的细节如下：

    * file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
    * access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    * buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
3. File对象的属性

    ```
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
 
    # 打开一个文件
    fo = open("foo.txt", "w")
    print "文件名: ", fo.name
    
    #返回true如果文件已被关闭，否则返回false。
    print "是否已关闭 : ", fo.closed
    #返回被打开文件的访问模式。
    print "访问模式 : ", fo.mode
    #如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
    print "末尾是否强制加空格 : ", fo.softspace
    
    fo.close()
    ```
4. write()

    write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

    write()方法不会在字符串的结尾添加换行符('\n')：
    
    ```
    fo=open('content2.txt','a+')
fo.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
fo.write( "Python 是一个非常好的语言。\n是的，的确非常好!!???????????\n" )

    fo.close()
    ```
    
    如果要写入一些不是字符串的东西, 那么将需要先进行转换:
    
    ```
    f = open("/tmp/foo1.txt", "w")

    value = ('www.runoob.com', 14)
    s = str(value)
    f.write(s)
    
    f.flush()
    
    # 关闭打开的文件
    f.close()
    ```
5. read()

    ```
    fo=open('content2.txt','r+')
    str=fo.read()
    print(str)
    
    fo.close()
    ```
6. readline() readlines()

    ```
    fo=open('content2.txt','r+')
    str1=fo.readline()
    #指针移动到第二行，读出所有行放到一个数组中
    str2=fo.readlines()
    print(str1)
    print(str2)
    
    fo.close()
    ```
    
    ```
    for line in fo:
        print(line, end='')
    ```
7. tell()
    返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
    ```
    fo.tell()
    ```
8. seek()

    如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
    
    from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

    * seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    * seek(x,1) ： 表示从当前位置往后移动x个字符
    * seek(-x,2)：表示从文件的结尾往前移动x个字符

9. pickle 模块
    python的pickle模块实现了基本的数据序列和反序列化。
    
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
    
    基本接口：

    
    ```
    pickle.dump(obj, file, [,protocol])
    ```
    
    write_file.py
    
    ```
    #!/usr/bin/python3
import pickle

    # 使用pickle模块将数据对象保存到文件
    data1 = {'a': [1, 2.0, 3, 4+6j],
             'b': ('string', u'Unicode string'),
             'c': None}
    
    selfref_list = [1, 2, 3]
    selfref_list.append(selfref_list)
    
    output = open('data.pkl', 'wb')
    
    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)
    
    # Pickle the list using the highest protocol available.
    pickle.dump(selfref_list, output, -1)
    
    output.close()
    ```
    
    read_file.py
    
        ```
        #!/usr/bin/python3
            import pprint, pickle
            
            #使用pickle模块从文件中重构python对象
            pkl_file = open('data.pkl', 'rb')
            
            data1 = pickle.load(pkl_file)
            print(data1['a'])
            pprint.pprint(data1)
            
            data2 = pickle.load(pkl_file)
            pprint.pprint(data2)
            
            pkl_file.close()
        ``` 
1. flush()

    flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。

    一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。


