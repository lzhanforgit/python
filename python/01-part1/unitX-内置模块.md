#内置模块

1. datetime
   1. time

        
        ```
            import time
            from datetime import datetime,timedelta
            # time不是用来取时间
            # for i in range(3):
            #     print(i)
            #     time.sleep(2)
        
        
        ```
    
    2. 获取当前时间  

        ```
                date_now=datetime.now()
                # print(date_now)
                
                # frm_date=date_now.strftime('%Y-%m-%d')
                #
                # print(frm_date)
        
        ```
        格式参数：

        %Y 带世纪部分的十制年份
        
        %m 十进制表示的月份
        
        %d 十进制表示的每月的第几天
        
        %H 24小时制的小时
        
        %M 十时制表示的分钟数
        
        %S 十进制的秒数
        
        %c  标准时间，如：04/25/17 14:35:14  类似于这种形式
       
    3. 获取昨天或者明天的时候：----------------------


        ```
        # yesday=date_now + timedelta(days=-1)
        # # temmorow=date_now + timedelta(days=1)
        # temmorow=date_now + timedelta(seconds=24*60*60*3)
        #
        # print(temmorow)
        ```

		世界标准时间
		
			datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    4. 时间格式的相互转换-------------------------


    ```# 1. 字符串转datetime
    string = '2017/11/10 02:29:58'.replace('/','-')
    # string = '2017-11-10 02:29:58'
    time1 = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    print(time1)
    print(type(time1))
    
    # 2. datetime转string
    time1_str = datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
    print(type(time1_str))
    print(time1_str)
    
    # 3. 时间戳转时间对象
    
    time2=time.time()  #时间戳
    time2_str = datetime.fromtimestamp(time2)
    
    print(time2_str)
    
    # 4. 时间对象转为时间戳
    timeStamp = int(time.mktime(date_now.timetuple()))
    print(timeStamp)
    
    # 5. 计算时间差
    
    days=(date_now-time1).days
    seconds=(date_now-time1).seconds
    print(seconds)
```
2. json

    JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。

    Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
    *     json.dumps	    将Python 字典类型转换为 JSON 对象
    *     json.loads	    将 JSON 对象转换为 Python 字典

    ```
    import json
    # 字典对象
    
    dict_lesson={
        "name":"python",
        "score":3
    }
    # json.dumps	    将Python 字典类型转换为 JSON 对象
    # json.loads	    将 JSON 对象转换为 Python 字典
    print(dict_lesson['score'])
    
    json_lesson=json.dumps(dict_lesson)
    
    print(type(json_lesson))   #str
    print(type(json.loads(json_lesson))) #dict
    ```
    
    如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
    
    ```
    content=[
      {"name":"nick","age":"12"},
      {"name":"tom","age":"13"},
      {"name":"helen","age":"22"},
      {"name":"tony","age":"32"}
    ]
    
    with open('users.json', 'w') as f:
        json.dump(content, f)
    
    with open('users.json','r+') as f:
        data = json.load(f)
        print(data)
        print(data[2]['name'])

    ```
3. collections

	我们都知道，Python拥有一些内置的数据类型，比如str, int, list, tuple, dict等， collections模块在这些内置数据类型的基础上，提供了几个额外的数据类型：

	* namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
	* deque: 双端队列，可以快速的从另外一侧追加和推出对象
	* Counter: 计数器，主要用来计数
	* OrderedDict: 有序字典
	* defaultdict: 带有默认值的字典

	
	1. namedtuple()

		namedtuple主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。
		
			from collections import namedtuple
		
			websites = [
			    ('Sohu', 'http://www.google.com/', u'张朝阳'),
			    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
			    ('163', 'http://www.163.com/', u'丁磊')
			]
			
			Website = namedtuple('Website', ['name', 'url', 'founder'])
			
			for website in websites:
			    website = Website._make(website)
			    print website


	2. deque

		deque其实是 double-ended queue 的缩写，翻译过来就是双端队列，它最大的好处就是实现了从队列 头部快速增加和取出对象: .popleft(), .appendleft() 。

		你可能会说，原生的list也可以从头部添加和取出对象啊？就像这样：
		
		l.insert(0, v)
		l.pop(0)
		但是值得注意的是，list对象的这两种用法的时间复杂度是 O(n) ，也就是说随着元素数量的增加耗时呈 线性上升。而使用deque对象则是 O(1) 的复杂度，所以当你的代码有这样的需求的时候， 一定要记得使用deque。
		
		作为一个双端队列，deque还提供了一些其他的好用方法，比如 rotate 等。
		
	3. Counter

		计数器是一个非常常用的功能需求，collections也贴心的为你提供了这个功能。
		
			from collections import Counter

			s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()
			
			c = Counter(s)
			# 获取出现频率最高的5个字符
			print c.most_common(5)
	4. OrderedDict

		在Python中，dict这个数据结构由于hash的特性，是无序的，这在有的时候会给我们带来一些麻烦， 幸运的是，collections模块为我们提供了OrderedDict，当你要获得一个有序的字典对象时，用它就对了。
		
			from collections import OrderedDict

			items = (
			    ('A', 1),
			    ('B', 2),
			    ('C', 3)
			)
			
			regular_dict = dict(items)
			ordered_dict = OrderedDict(items)
			
			print 'Regular Dict:'
			for k, v in regular_dict.items():
			    print k, v
			
			print 'Ordered Dict:'
			for k, v in ordered_dict.items():
			    print k, v

	5. more

		https://docs.python.org/3.7/library/collections.html#userdict-objects