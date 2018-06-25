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
3. 


