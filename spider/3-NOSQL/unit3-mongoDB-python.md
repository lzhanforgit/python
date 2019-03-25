###pymongo

1. 安装连接驱动

		pip install pymongo
		
2. 连接

	连接方式：

	1）默认client = MongoClient()
	
	2) 通过host+port的方式：client = MongoClient(host,port)
	
	3) 通过uri的方式：client = MongoClient(uri)
	
	示例：
		
		from pymongo import MongoClient
		#conn = MongoClient('127.0.0.1', 27017)
		
		uri = 'mongodb://lili:123456@127.0.0.1:27017/liepin'
		conn = MongoClient(uri)
		db = conn.liepin  #连接liepin数据库，没有则自动创建
		col_user = db.user
		for u in col_user.find():
		    print(u['name'])
3. 数据库连接uri

	mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
	
	1. mongodb:// 这是固定的格式，必须要指定。

	1. username:password@ 可选项，如果设置，在连接数据库服务器之后，驱动都会尝试登陆这个数据库
	
	1. host1 必须的指定至少一个host, host1 是这个URI唯一要填写的。它指定了要连接服务器的地址。如果要连接复制集，请指定多个主机地址。
	
	1. portX 可选的指定端口，如果不填，默认为27017
	
	1. /database 如果指定username:password@，连接并验证登陆指定数据库。若不指定，默认打开 test 数据库。
	
	1. ?options 是连接选项。如果不使用/database，则前面需要加上/。所有连接选项都是键值对name=value，键值对之间通过&或;（分号）隔开

4. 添加数据

	插入数据（insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入,save通常用来更新数据....）

		my_set.insert({"name":"zhangsan","age":18})
		#或
		my_set.save({"name":"zhangsan","age":18})
		
	案例：
	
		from pymongo import MongoClient
		import json
		uri = 'mongodb://lzhan:123456@127.0.0.1:27017/jumei'
		try:
		    conn = MongoClient(uri)
		    db = conn.jumei  # 连接jumei数据库，没有则自动创建
		    col_user = db.user
		    with open('data/users.json') as fp:
		        users=json.load(fp)
		    #   添加用户
		        col_user.insert(users)
		    conn.close()
		except Exception as ex:
		    print(ex)
5. 修改数据

		my_set.update(
		   <query>,    #查询条件
		   <update>,    #update的对象和一些更新的操作符
		   {
		     upsert: <boolean>,    #如果不存在update的记录，是否插入
		     multi: <boolean>,        #可选，mongodb 默认是false,只更新找到的第一条记录
		     writeConcern: <document>    #可选，抛出异常的级别。
		   }
		)
		
	案例
	
		result=col_user.update({"name":"python"},{"$set":{"age":40}})
		
6. 删除数据

		my_set.remove(
		   <query>,    #（可选）删除的文档的条件
		   {
		     justOne: <boolean>,    #（可选）如果设为 true 或 1，则只删除一个文档
		     writeConcern: <document>    #（可选）抛出异常的级别
		   }
		)
		
7. 查询数据

		my_set.find(）
		
8. 模块化案例

		#-*-coding:utf-8-*-
		import logging
		import setting
		import time,datetime
		from setting import mongo_host,mongo_port,mongo_db_name_data,mongo_db_name_linkbase,mongo_db_name_task
		import pymongo
		
		logging.basicConfig(filename='log',level=logging.INFO)
		
		
		class Connect_mongo(object):
		    def __init__(self):
		        self.mongo_host = mongo_host
		        self.mongo_port = mongo_port
		        self.conn()
		
		    def conn(self):
		        self.client = pymongo.MongoClient(host=self.mongo_host,port=self.mongo_port)
		        self.db_data = self.client[mongo_db_name_data]
		        self.db_linkbase = self.client[mongo_db_name_linkbase]
		        self.db_linkbase_collection = self.db_linkbase.linkbase
		        self.db_task = self.client[mongo_db_name_task]
		
		    def insert_db(self,item):
		        setting.my_logger.info('当前插入数据库的最终数据为%s'%item)
		        self.db_data.xxx_data.update({"car_id":item['car_id']},item,True)
		        self.client.close()
		
		    def save_linkbase(self,response_result,spider_name,hash_url,item_type):
		        if item_type == 'carinfo_item':
		            linkinfo = {}
		            linkinfo['status'] = response_result.status_code
		            linkinfo['url'] = response_result.url
		            linkinfo['spider_name'] = spider_name
		            linkinfo['hash_url'] = hash_url
		            #保存到linkbase
		            self.db_linkbase_collection.update({"status":linkinfo['status'],"hash_url":hash_url},linkinfo,True)
		            self.client.close()
		        else:
		            self.db_linkbase_collection.create_index([("over_time", pymongo.ASCENDING)], expireAfterSeconds=7200)
		            linkinfo = {}
		            linkinfo['status'] = response_result.status_code
		            linkinfo['url'] = response_result.url
		            linkinfo['spider_name'] = spider_name
		            linkinfo['hash_url'] = hash_url
		            linkinfo['over_time'] = datetime.datetime.utcnow()
		            #保存到linkbase
		            self.db_linkbase_collection.update({"status":linkinfo['status'],"hash_url":hash_url},linkinfo,True)
		            self.client.close()
		
		    def save_task(self,task):
		        setting.my_logger.info('当前插入数据库的task信息为%s'%task)
		        self.db_task.xxx_task.update({'url':task['url']},task,True)
		        self.client.close()
		
		    def get_task(self,max_requests=10):
		        task = []
		        for i in range(max_requests):
		            result = self.db_task.xxx_task.find_one_and_delete({})
		            task.append(result)
		        return task
		
		    def duplicate_removal(self,hash_data):
		        result = self.db_linkbase.linkbase.find_one({'hash_url':hash_data})
		        if result == None:
		            return True
		        else:
		            return False
		
		
		mongo_insert = Connect_mongo()