# 变量类型-Dictionary   
1. 类型
    字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中.
    
    键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
    
2. 特性

    和list和tuple一样，dictionary也可以：
    
    ```
    char={item:ord(item) for item in 'python'}

    print(char)
    ```

3. 字典访问

    ```
        user={
        'name':{'firstName':'zhan','lastName':'liang'},
        'age':20,
        'address':'usa',
        'hobby':['film','sport']
        }

        print('user length:',len(user))

        print('user first property is :',user['name'])
        
        for key,value in user.items():
            print ('property %s value  %s' % (key,value))
        
        for kk in user.keys():
            print ('property %s' % (kk))
        
        for vv in user.values():
            print ('values %s' % (vv))

    ```
    
    如果想根据key的先后顺序遍历字典，则可以：
    
    ```
        for kk in sorted(user.keys()):
            print ('property %s' % (kk))
    ```
4. 针对不存在的键，如果访问会出现错误。

    ```
        nation=user['nation'] #error
        
        nation=user['nation'] if 'nation' in user else 'china'
    ```
5. dict,bytes,string之间的相互转化

    ```
        s='{"id":"001","name":"python"}'
        # s='http://www/163.com'
        #string to bytes
        s_bytes_utf8=s.encode('utf-8')
        print(s_bytes_utf8)
        
        # bytes to string
        s_string_utf8=s_bytes_utf8.decode('utf-8')
        print(s_string_utf8)
        
        # string to dict
        s_dict=eval(s_string_utf8)
        
        print(s_dict['id'])
        
        # dict to string
        
        s_string=str(s_dict)
        
        print(s_string)
        
        
        
    ```


6. 字典方法

	D.clear()                              #移除D中的所有项  
	D.copy()                               #返回D的副本  
	D.fromkeys(seq[,val])                  #返回从seq中获得的键和被设置为val的值的字典。可做类方法调用  
	D.get(key[,default])                   #如果D[key]存在，将其返回；否则返回给定的默认值None  
	D.has_key(key)                         #检查D是否有给定键key  
	D.items()                              #返回表示D项的(键，值)对列表  
	D.iteritems()                          #从D.items()返回的(键，值)对中返回一个可迭代的对象  
	D.iterkeys()                           #从D的键中返回一个可迭代对象  
	D.itervalues()                         #从D的值中返回一个可迭代对象  
	D.keys()                               #返回D键的列表  
	D.pop(key[,d])                         #移除并且返回对应给定键key或给定的默认值D的值  
	D.popitem()                            #从D中移除任意一项，并将其作为(键，值)对返回  
	D.setdefault(key[,default])            #如果D[key]存在则将其返回；否则返回默认值None  
	D.update(other)                        #将other中的每一项加入到D中。  
	D.values()                             #返回D中值的列表
	
	https://www.cnblogs.com/mxh1099/p/8512552.html