# 正则表达式
**作者：詹亮**


https://www.cnblogs.com/tina-python/p/5508402.html

1. 简介


     正则表达式本身是一种小型的、高度专业化的编程语言，而在python中，
     通过内嵌集成re模块，程序媛们可以直接调用来实现正则匹配。
     正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行。
2. 语法规则

    1. 普通字符和11个元字符：

        普通字符|匹配自身|abc|abc|
        ---|---|---|---|
        .|匹配任意除换行符"\n"外的字符(在DOTALL模式中也能匹配换行符|a.c|abc|
        \\|转义字符，使后一个字符改变原来的意思|a\.c;a\\c|a.c;a\c|
        \*|匹配前一个字符0或多次|abc*|ab;abccc|
        +|匹配前一个字符1次或无限次|abc+|abc;abccc|
        ?|匹配一个字符0次或1次|abc?|ab;abc|
        ^|匹配字符串开头。在多行模式中匹配每一行的开头|	^abc|abc|
        $|匹配字符串末尾，在多行模式中匹配每一行的末尾|	abc$|abc|
        \||	或。匹配|左右表达式任意一个，从左到右匹配，如果|没有包括在()中，则它的范围是整个正则表达式|abc|defabcdef|
        {}|	{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次|ab{1,2}c|abc abbc|
        []|字符集。对应的位置可以是字符集中任意字符。字符集中的字符可以逐个列出，也可以给出范围，如[abc]或[a-c]。[^abc]表示取反，即非abc。所有特殊字符在字符集中都失去其原有的特殊含义。用\反斜杠转义恢复特殊字符的特殊含义。|a[bcd]e|abe ace ade|
        ()|被括起来的表达式将作为分组，从表达式左边开始没遇到一个分组的左括号“（”，编号+1.分组表达式作为一个整体，可以后接数量词。表达式中的|仅在该组中有效。|	(abc){2}a(123|456)c|abcabc a456c|

        这里需要强调一下反斜杠\的作用：

        * 反斜杠后边跟元字符去除特殊功能；（即将特殊字符转义成普通字符）
        * 反斜杠后边跟普通字符实现特殊功能；（即预定义字符）
        * 引用序号对应的字组所匹配的字符串。

        ```
            a=re.search(r'(tina)(fei)haha\2','tinafeihahafei tinafeihahatina').group()
            print(a)
            结果：
            tinafeihahafei
        ```

    2. 预定义字符集（可以写在字符集[...]中）

        * \d  数字:[0-9]

        * \D  非数字:[^\d]
        * \s  匹配任何空白字符:[<空格>\t\r\n\f\v]

        * \S	非空白字符:[^\s]
        * \w  匹配包括下划线在内的任何字字符:[A-Za-z0-9_]

        * \W  匹配非字母字符，即匹配特殊字符

        * \A  仅匹配字符串开头,同^	\Aabc
        * \Z  仅匹配字符串结尾，同$
        * \b  匹配\w和\W之间，即匹配单词边界匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。	\babc\b
            a\b!bc	空格abc空格
            a!bc
        * \B  [^\b]

        ```
            import re
            w = re.findall(r'\bzhan','zhan liang')
            print(w)
            s = re.findall(r'\btina','tiana tinaaaa')
            print(s)
            v = re.findall(r'\btina','tian#tinaaaa')
            print(v)
            a = re.findall(r'\btina\b','tian#tina@aaa')
            print(a)
        ```
    3. 特殊分组用法：

        (?P\<name>)|分组，除了原有的编号外再指定一个额外的别名|	(?P<id>abc){2}	|abcabc|
        ---|---|---|---|
        (?P=name)|引用别名为<name>的分组匹配到字符串|	(?P<id>\d)abc(?P=id)|1abc15abc5|
        \\\<number>|引用编号为<number>的分组匹配到字符串|	(\d)abc\1|1abc15abc5|

        1. (?P<tag>abc)就是把abc这个匹配项取个别名，这样后面用到abc的时候就用tag来代替了，比如

           ```
           import re
           
           str2='<li>aaa</li><li>bbb</li><li>ccc</li><a>eeee</a>'
           
           # 找出格式为<xxx>..</xxx>的元素，因为我们把\w+取名为dd，那么意味着后面的结束标签中的内容也必须和dd变量的内容一模一样
           reg2=re.compile(r'\<(?P<dd>\w+)\>(\w+)\</(?P=dd)\>')
           
           print(reg2.findall(str2))
           
           #找出单词格式为AABB 的词语
           
           str1='aabb is a word,and ccdd is a word too'
           
           # reg1=re.compile(r'(?P<tt>\w)(?P=tt)(?P<ee>\w)(?P=ee)')
           reg1=re.compile(r'((?P<tt>\w)(?P=tt)(?P<ee>\w)(?P=ee))')
           
           print(reg1.findall(str1))
           
           #\1 \2表示的是位置，类似于‘hello {0},i am {1}’.format(n,m)
           reg3=re.compile(r'(\w)\1(\w)\2')
           
           print(reg3.findall(str1))
           ```


4. re模块中常用功能函数

    1. compile()

        编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，
        这样可以提高一点效率。）

        ```
            regex01=re.compile(r'^李\w{1,2}$')
            # regex01=re.compile(r'李\w{1,2}')
            #如果不加上开始和结束标志，其实就是匹配部分数据，下面的字符串就会匹配'李小飞'

            str01='李小飞龙'

            res01=regex01.findall(str01)
            print(res01)
        ```
    2. match()

        决定re是否在字符串刚开始的位置匹配。//注：这个方法并不是完全匹配。
        当pattern结束时若string还有剩余字符，
        仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'

        ```
            #匹配模式
            #如果单纯是测定字符串是否匹配正则表达式的规则，则不需要用到"()"
            #如果没有匹配结果为none
            m = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
            #分组 一定要用到分组符号"()"

            m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
            print(m.group(0))
            print(m.group(1))
            print(m.group(2))
            print(m.groups())
            #提取时间

            t = '19:05:30'
            rt = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
            print(rt.groups())
        ```

        **没有（）就是匹配模式，匹配模式就是从开始第一个字符进行匹配，如果匹配成功，那么后面的内容就不会匹配。有了（）就是分组查找模式,有了分组就是把匹配到的内容分组存放**

    3. search()

         格式：

        ```
        re.search(pattern, string, flags=0)
        
        re.search函数会在字符串内查找模式匹配,只要找到第一个匹配然后返回，如果字符串没有匹配，则返回None。
        
        print(re.search('\dcom','www.4comrunoob.5com').group())
        执行结果如下：
        4com
        
        ```
        
        **没有（）就是查找模式，查找模式就是在当前字符串中查找符合规则的子串，如果找到则停止找找。有了（）就是分组查找模式,有了分组就是把匹配到的内容分组存放**
    4. findall()

        re.findall遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表。

         格式：

        ```
             re.findall(pattern, string, flags=0)
        ```

        ```
            p = re.compile(r'\d+')
            print(p.findall('o1n2m3k4'))
            执行结果如下：
            ['1', '2', '3', '4']
            复制代码
            import re
            tt = "Tina is a good girl, she is cool, clever, and so on..."
            rr = re.compile(r'\w*oo\w*')
            print(rr.findall(tt))
            print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式
            执行结果如下：
            ['good', 'cool']
            [('g', 'd'), ('c', 'l')]
        ```

        简单爬虫

        ```
            regex=re.compile(r'<li>(.+?)</li>')
            str01='
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Title</title>
                    </head>
                    <body>
                        <li>001</li>
                        <li>002</li>
                        <li>003</li>
                        <li>004</li>
                    </body>
                    </html>
                '

                # str01=re.sub(r"\r|\n", "",str01)
                # print(str01)
                res01=regex.findall(str01)
                
                #不区分大小写
                regex=re.compile(r'<li id=(.+)>(\w+)</li>',flags=re.IGNORECASE)
                print(res01)
        ```

    5. split()

        按照能够匹配的子串将string分割后返回列表。

        可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。

        格式：

        ```
        re.split(pattern, string[, maxsplit])

        maxsplit用于指定最大分割次数，不指定将全部分割。

        print(re.split('\d+','one1two2three3four4five5'))
        执行结果如下：
        ['one', 'two', 'three', 'four', 'five', '']

        ```

    6. sub()

        使用re替换string中每一个匹配的子串后返回替换后的字符串。

        格式：

            re.sub(pattern, repl, string, count)
            
            复制代码
            import re
            text = "JGood is a handsome boy, he is cool, clever, and so on..."
            print(re.sub(r'\s+', '-', text))
            执行结果如下：
            JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...
            其中第二个函数是替换后的字符串；本例中为'-'
            
            第四个参数指替换个数。默认为0，表示每个匹配项都替换。


        re.sub还允许使用函数对匹配项的替换进行复杂的处理。
    
        如：re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0)；将字符串中的空格' '替换为'[ ]'。
    
            import re
            text = "JGood is a handsome boy, he is cool, clever, and so on..."
            print(re.sub(r'\s+', lambda m:'['+m.group(0)+']', text,0))
            执行结果如下：
            JGood[ ]is[ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...


### 一些注意点

   1. re.match与re.search与re.findall的区别：

        re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
        则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。


            a=re.search('[\d]',"abc33").group()
            print(a)
            p=re.match('[\d]',"abc33")
            print(p)
            b=re.findall('[\d]',"abc33")
            print(b)
            执行结果：
            3
            None
            ['3', '3']
   2. 贪婪匹配与非贪婪匹配
		
		 1. 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配 ( * )；

		 
		 2. 非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配 ( ? )；
    
	   *?  ,+?     ,??  ,{m,n}?
	   
	   前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
			
	
	   
			
			```
			str4='ababbbbbab'
	
			#reg4=re.compile(r'ab+?')
			reg4=re.compile(r'ab+')
	
			print(reg4.findall(str4))
			```
			
			
			```
				aa<div>test1</div>bb<div>test2</div>cc
	
				使用贪婪的数量词的正则表达式：<div>.*</div>
	
				匹配结果：<div>test1</div>bb<div>test2</div>
				使用非贪婪的数量词的正则表达式：<div>.*?</div>
	
				匹配结果：<div>test1</div>
	
			```
	        demo1
	
	            a = re.findall(r"a(\d+?)",'a23b')
	            print(a)
	            b = re.findall(r"a(\d+)",'a23b')
	            print(b)
	            执行结果：
	            ['2']
	            ['23']
	            
	            a = re.match('<(.*)>','<H1>title<H1>').group()
	            print(a)
	            b = re.match('<(.*?)>','<H1>title<H1>').group()
	            print(b)
	            执行结果：
	            <H1>title<H1>
	            <H1>
	
	        demo2
	
	            a = re.findall(r"a(\d+)b",'a3333b')
	            print(a)
	            b = re.findall(r"a(\d+?)b",'a3333b')
	            print(b)
	            执行结果如下：
	            ['3333']
	            ['3333']
	            #######################
	            这里需要注意的是如果前后均有限定条件的时候，就不存在什么贪婪模式了，非匹配模式失效。
	            
# 爬虫页面解析
1. 正则表达式解析

	1. 实际上爬虫一共就四个主要步骤：

		1. 明确目标 (要知道你准备在哪个范围或者网站去搜索)
		1. 爬 (将所有的网站的内容全部爬下来)
		1. 取 (去掉对我们没用处的数据)
		1. 处理数据（按照我们想要的方式存储和使用）

	2. 匹配中文

		在某些情况下，我们想匹配文本中的汉字，有一点需要注意的是，中文的 unicode 编		码范围 主要在 [u4e00-u9fa5]，这里说主要是因为这个范围并不完整，比如没有包		括全角（中文）标点，不过，在大部分情况下，应该是够用的。

		假设现在想把字符串 title = u'你好，hello，世界' 中的中文提取出来，可以这		么做：
		
			import re
	
			title = u'你好，hello，世界'
			pattern = re.compile(ur'[\u4e00-\u9fa5]+')
			result = pattern.findall(title)
			
			print(result)
		注意到，我们在正则表达式前面加上了两个前缀 ur，其中 r 表示使用原始字符串，u 表示是 unicode 字符串。但是在python3中默认编码为unicode所以u必须省略。
		
		执行结果:

			['你好', '世界']
		
		**如果爬取的网页中有中文，可能会出现乱码。原因是网页的编码格式可能是GBK,我们可以这样**
		
			gbk_html = html.decode('gbk').encode('utf-8')	              
1. 案例一：解析淘宝数据

		import re
		li=[]
		with open('taopage0.html','r+') as fp:
		    data=fp.read()
		
		    plt = re.findall(r'\"view_price\"\: \"[\d\.]*\"', data)
		
		    # 在爬取下来的网页中查找物品
		    tlt = re.findall(r'\"raw_title\"\: \".*?\"', data)
		
		    loc=re.findall(r'\"item_loc\"\: \".*?\"', data)
		    
		    for i in range(len(plt)):
		        price = eval(plt[i].split(':')[1])
		        title = eval(tlt[i].split(':')[1])
		        location = eval(loc[i].split(':')[1])
		
		        li.append([price,title,location])
		
		
		print(li)
		
2. 案例二：解析猎聘网








	            