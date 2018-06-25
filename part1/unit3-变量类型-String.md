# 变量类型-String   
1. 类型
    python变量分为可变性和不可变性两种，数字、字符串和元组是不可变性；列表和字典是可变性变量。
    
    ```
        s='python'
        s[0]='P' #error
    ```
2. 引号

    单引号和双引号等价，可以嵌套使用
    
    ```
        print('tom say:\"how are you\"')
        print('tom say:"how are you"')
    ```
    
    **三引号**
    三引号包含多行字符串常量，所有行和合并在一起，并在每行末尾增加一个换行符。
    **__doc__**
    当把三引号字符串放在代码开始时，可以通过下面两种方式输出：
    
        ```
            """
                  line 1 hello
                  line2
                  line3'''line3-content'''
                  <html>
                        <body></body>
                  </html>

            """
            #命令行
            python test.py __doc__
            
            #代码文件中
            
            print(__doc__)
        ```
        
    >必须放在第一行；
    每个文件只能有一条
    
1. 转义字符

    ```
    # \(在行尾时)	续行符
    a=12
    b=12
    c=10
    d=a+\
      b+\
      c
    
    print(d)
    
    # \\	反斜杠符号
    
    ```
    ##raw 字符串##
    ```
        myfile=open('c:\new\text.dat')
        #这里\n \t 会被认为是转义字符，为了解决可以这么写
        myfile=open(r'c:\new\text.dat')
        myfile=open('c:\\new\\text.dat')
        
        #也支持反斜杠的方式
         myfile=open('c:/new/text.dat')
         
    ```
    >ord('a')用于测定‘a’的ASCII值。
2. Python字符串运算符

    |操作符	|描述	|实例|
    |---|---|---|
    |r/R	|原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。|	print r'\n'  \n  print R'\n'  \n|
4. Python字符串

    python的字串列表有2种取值顺序:

    1. 从左到右索引默认0开始的，最大范围是字符串长度少1
    2. 从右到左索引默认-1开始的，最大范围是字符串开头
如果你要实现从字符串中获取一段子字符串的话，可以使用变量 [头下标:尾下标]，就可以截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。

    比如:
    
        ```
            s = 'ilovepython'
            # s[1:5]的结果是love。
            # print s[-6:]的结果就是python
            # print s[-6:-2]
            
            str='0123456789'
            print(str[1:10:2])          #1,3,5,7,9 第三个参数表示步长
            print(str[::2])             #02468  
            print(str[::-1])            #9876543210 反转
        ```

    >当使用以冒号分隔的字符串，python返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。

    >上面的结果包含了s[1]的值l，而取到的最大范围不包括上边界，就是s[5]的值p。
    
    **加号（+）是字符串连接运算符，星号（*）是重复操作**
    
        ```
        print s*2
        结果为：ilovepythonilovepython
        ```
3. 字符串输出

    语法说明

    格式化符号说明备注 %s 字符串输出 string%10s 右对齐，占位符 10位%-10s 左对齐，占位符 10 位 %.2s 截取 2 位字符串 %10.2s10 位占位符，截取两位字符串。
    
    举个栗子：
    
    ```
    print('%s' % 'hello world')       # 字符串输出hello world
    print('%20s' % 'hello world')     # 右对齐，取20位，不够则补位         hello world
    print('%-20s' % 'hello world')    # 左对齐，取20位，不够则补位hello world         
    print('%.2s' % 'hello world')     # 取2位he
    print('%10.2s' % 'hello world')   # 右对齐，取2位        he
    print('%-10.2s' % 'hello world')  # 左对齐，取2位he
    ```

3. 格式输出

    ```
    import math
    s='hello,world'
    
    print(str(s))
    print(repr(s))
    
    print ('name is:'+repr(s))
    print ('name is:',repr(s))
    
    for x in range(1, 11):
        # print(repr(x).rjust(2), repr(x * x).rjust(3),repr(x*x*x).rjust(4))
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
    
    str01='12.3'
    print(str01.zfill(2))
    
    print('{1} and {0}'.format('spam', 'eggs'))
    
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
    
    print('The value of PI is approximately {0:.3f}.'.format(math.pi))
    ```
    
    >一种是通过str函数，他会把值转换为合理形式的字符串，以便用户可以理解；另一种是通过repr函数，她会创建一个字符串，以合法的Python表达式的形式来表示值。

    repr也可以做``反引号的实现。如果希望答应一个包含数字的句子，那么反引号就很有用了。比如：

    ```
    temp = 100
    print('hello'+temp)  //error
    print('hello'+`temp`)  //等价 print('hello'+repr(temp))
    ```
    ```
    s='''hello
    world'''

    print(s)
    print(repr(s))   # 'hello\nworld'
    ```
    >三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
4. 内建函数

    
    1. 统计单词出现的次数
    
        ```
            str='hello world hello china'
    
            num=str.count('hello',0,len(str))
    
            print(num)
        ```
    
    2. find()

        ```
            word='hello python,hello,world'

            res01=word.find('hello',4,8)
        ```
    3. replace

        ```
            word='hello python,hello,world'
            res02=word.replace('hello','hi',2)
        ```
    4. split()
    5. join()

        ```
            arr=list(word)

            str_arr=','.join(arr)
            print(str_arr)
            str2='python'.join(['_one_','_two_','_three_'])
        ```
    5. upper() lower()
    6. strip() lstrip() rstrip() len(s)

    |方法	|描述|
    |---|---|
    |string.capitalize()|把字符串的第一个字符大写|
    |string.center(width)|返回一个原字符串居中,并使用空格填充至长度 width 的新字符串|
    |string.count(str, beg=0, end=len(string))|返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数|
    |string.decode(encoding='UTF-8', errors='strict')|以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'string.encode(encoding='UTF-8', errors='strict')以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'|
    |string.endswith(obj, beg=0, end=len(string))|检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.|
    |string.expandtabs(tabsize=8)|把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。|
    |string.find(str, beg=0, end=len(string))|检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1|
    |string.format()|格式化字符串string.index(str,beg=0,end=len(string))|跟find()方法一样，只不过如果str不在 string中会报一个异常.|
    |string.isalnum()|如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False|
    |string.isalpha()|如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False|
    |string.isdigit()|如果 string 只包含数字则返回 True 否则返回 False.|
    |string.islower()|如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False|
    |string.isnumeric()|如果 string 中只包含数字字符，则返回 True，否则返回 False|
    |string.isspace()|如果 string 中只包含空格，则返回 True，否则返回 False.|
    |string.istitle()|如果 string 是标题化的(见 title())则返回 True，否则返回 False|
    |string.isupper()|如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False|
    |string.join(seq)|以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串|
    |string.ljust(width)|返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串|
    |string.lower()|转换 string 中所有大写字符为小写.、
    |string.lstrip()|截掉 string 左边的空格
    |max(str)|返回字符串 str 中最大的字母。|
    |min(str)|返回字符串 str 中最小的字母。|
    |string.partition(str)|有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
    |string.replace(str1, str2,  num=string.count(str1))|把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.|
    |string.rfind(str, beg=0,end=len(string) )|类似于 find()函数，不过是从右边开始查找.|
    |string.rindex( str, beg=0,end=len(string))|类似于 index()，不过是从右边开始.|
    |string.rjust(width)|返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串|
    |string.rpartition(str)|类似于 partition()函数,不过是从右边开始查找.|
    |string.rstrip()|删除 string 字符串末尾的空格.|
    |string.split(str="", num=string.count(str))|以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串|
    |string.splitlines([keepends])|按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。|
    |string.startswith(obj, beg=0,end=len(string))|检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.|
    |string.strip([obj])|在 string 上执行 lstrip()和 rstrip()|
    |string.swapcase()|翻转 string 中的大小写|
    |string.title()|返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())|
    |string.upper()|转换 string 中的小写字母为大写|
    |string.zfill(width)|返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0|
    |string.isdecimal()|isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。|


3. 浮点数输出

    语法说明
    
    格式化符号说明备注 %f 保留小数点后面六位有效数字 float%e 保留小数点后面六位有效数字 %g 在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法。

    举个栗子：
    
    ```
        print('%f' % 1.11)         # 默认保留6位小数1.110000
        print('%.1f' % 1.11)       # 取1位小数1.1
        print('%e' % 1.11)         # 默认6位小数，用科学计数法1.110000e+00
        print('%.3e' % 1.11)       # 取3位小数，用科学计数法1.110e+00
        print('%g' % 1111.1111)    # 默认6位有效数字1111.11
        print('%.7g' % 1111.1111)  # 取7位有效数字1111.111
        print('%.2g' % 1111.1111)  # 取2位有效数字，自动转换为科学计数法1.1e+03
    ```
    
3. 帮助文档
    
    在命令行中：
    ```
        s='hello'
        dir(s)
        help(s.replace) # 查看函数的作用 按q退出
    ```


