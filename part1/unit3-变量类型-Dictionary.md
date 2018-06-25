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
    
    

