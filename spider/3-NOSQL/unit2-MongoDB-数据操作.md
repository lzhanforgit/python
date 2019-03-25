### 数据库操作

1. 新建数据库


	use boke
	
2. 插入数据(表 > 行)

	```
	db.table_name.insert({“name”:"html5"}); WriteResult({“nInserted”:1});
    		capped collections
    	Capped collections 就是固定大小的collection。
    	它有很高的性能以及队列过期的特性(过期按照插入的顺序). 有点和 "RRD" 概念类似。
    	Capped collections是高性能自动的维护对象的插入顺序。它非常适合类似记录日志的功能 和标准的collection不同，你必须要显式的创建一个capped collection， 指定一个collection的大小，单位是字节。collection的数据存储空间值提前分配的。

    	要注意的是指定的存储大小包含了数据库的头信息。


    db.createCollection(“table_name", {capped:true, size:100000})
	```

3. 查看所有数据库

	```
    show dbs
	```
4. 删除数据库

	```
    use BOKE

    db.dropDatabase()
	```
5. 删除集合（表）

	```
    db.collection.drop()
	```
6. 插入文档

	```
    use blog
    db.articles.insert(
        {title: 'css3 教程',
        description: 'css3 是一个 脚本 语言',
        by: 'lzhan',
        url: 'http://www.lzhan.com',
        tags: ['mongodb', 'database', 'NoSQL'],
        likes: 3400
    })
	```

7. 更新数据

	a. update

	参数说明：

		query : update的查询条件，类似sql update查询内where后面的。

		update : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的

		upsert : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。

		multi : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。

		writeConcern :可选，抛出异常的级别。

    ```
    	db.articles.update({'查询字段':'查询条件’},{$set:{‘修改的字段’:'设置新值'}})
        db.articles.update({'title':'MongoDB 教程’},{$set:{‘by’:'lzhan'}})
    ```

    注：
	**语句只会修改第一条发现的文档，如果你要修改多条相同的文档，则需要设置 multi 参数为 true。
db.articles.update({“likes":100},{$set:{"by":"zhan"}},{multi:true})**

    b. save() 方法通过传入的文档来替换已有文档。语法格式如下：
    	替换的前提要是主键相同，否则会变成保存新的数据（插入数据）

    ```
    db.collection.save(
       <document>,
       {
         writeConcern: <document>
       }
    )
    ```
    c. 参数自加

    ```
    db.articles.update({“条件”:’值’},{$inc:{“自增字段":步长}，{multi:true})

    db.articles.update({“id”:’0001’},{$inc:{"like":1}},{multi:true})
    ```
8. 删除文档
	```
    db.collection.remove(
     <query>,
     {
        justOne: <boolean>,
        writeConcern: <document>
     }
    )
    query :（可选）删除的文档的条件。
    
    justOne : （可选）如果设为 true 或 1，则只删除一个文档。
    
    writeConcern :（可选）抛出异常的级别。
	```

    code:

	```
    db.articles.remove({“by”:”lzhan"},1)

    删除所有数据
    db.col.remove({})
	```


9. 查询文档

		db.articles.find().pretty()

	|操作	|语法	|示例	|RDBMS等效语句|
	---|---|---|---|
	|相等|	{\<key>:\<value>} |db.mycol.find({"by":"yiibai"}).pretty()|	where by = 'yiibai'|
	|相等|{ <field>: { $eq: <value> } }|db.mycol.find({"likes":{$eq:50}}).pretty()|
	|小于	|{\<key>:{$lt:<value>}}|	db.mycol.find({"likes":{$lt:50}}).pretty()|	where likes < 50|
	|小于等于|	{\<key>:{$lte:<value>}}|	db.mycol.find({"likes":{$lte:50}}).pretty()|	where likes <= 50|
	|大于|	{\<key>:{$gt:<value>}}|	db.mycol.find({"likes":{$gt:50}}).pretty()|	where likes > 50|
	|大于等于|	{\<key>:{$gte:<value>}}|	db.mycol.find({"likes":{$gte:50}}).pretty()|	where likes >= 50|
	|不等于|	{\<key>:{$ne:<value>}}|	db.mycol.find({"likes":{$ne:50}}).pretty()|	where likes != 50|
	|in|{ <field>: { $in: [value,value] } }|db.mycol.find({"likes":{$in:[50,51,52]}}).pretty()|where likes in[50,51,51]|
	|not in|{ <field>: { $nin: <value> } }|db.mycol.find({"likes":{$nin:[50,51,52]}}).pretty()|where likes not in[50,51,51]|

    ---
    
    ###表达式###
    
    1. and 语句

    	MongoDB 的 find() 方法可以传入多个键(key)，每个键(key)以逗号隔开，及常规SQL 的 AND 条件。
    	
    	语法：
    			{ $and: [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] }
    	
		释义：与 条件查询

		语法格式如下：

    	```
        db.col.find({key1:value1, key2:value2}).pretty()
        db.comments.find({'like':{$gte:5,$lte:100}}).pretty()
    	```
    	
    	也可以
    	
    		{ $and: [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] }


   

   2. or 语句
	
		语法：{ $or: [ { <expression1> }, { <expression2> }, ... , { <expressionN> } ] }
		
		释义：或 条件查询
		
		举例：


		MongoDB OR 条件语句使用了关键字 $or,语法格式如下：

	        ```
	        db.col.find(
	        {
	            $or: [
	                {key1: value1}, {key2:value2}
	                 ]
	        }
	        ).pretty()
	        ```

		code:
		
		        ```
		        db.articles.find({"likes":{$gt:100},"likes":{$lt:1000}}).pretty()
		
		        db.articles.find(
		            {
		                $or:[
		                    {“likes":100},
		                    {“likes”:{$gt:1000}}
		            	    ]
		            }
		        ).pretty()
		        ```
  	3. $not
  
	  	语法：{ field: { $not: { <operator-expression> } } }
	  	
	  	释义：查询与表达式不匹配的文档
	  	
	  	举例：
	  	
	  	查询age不大于20的文档：
	  	
			db.person.find( { age: { $not: { $gt: 20 } } } )

	1. $nor
		
		语法：{ $nor: [ { <expression1> }, { <expression2> }, ... { <expressionN> } ] }
		
		释义：查询与任一表达式都不匹配的文档
		
		举例：
		
		查询age既不等于20，sex也不是男的文档：
		
			db.person.find( { $nor: [ { age: 20 },{ sex: "男"} ] } )

	1. $exists
	
		语法：{ field: { $exists: <boolean> } }
		
		释义：查询存在指定字段的文档
		
		举例：
		
		查询存在phone字段的文档：
		
			db.person.find( { phone: { $exists: true } } )

	1. $mod
	
		语法：{ field: { $mod: [ 除数, 余数 ] } }
		
		释义：取余条件查询
		
		举例：
		
		查询age字段的值除以2余0的文档：
		
			db.person.find( { age: { $mod: [ 2, 0 ] } } )

	
	[更多内容轻参考](https://blog.csdn.net/qq_16313365/article/details/58599253)
10. 模糊查询（正则表达式）

		{field:{$regex:{/pattern/option}}},其中pattern是寻常的正则表达式，

	          option的值包含：
	
	             i(不区分大小写)，
	
	           	m(当使用^与$符号模糊匹配时，作用于屏蔽中间的换行符) ,
	
	             x(忽略注释，以#开头 /n结尾)，
	
	             s(允许所有字符包括换行符参与模糊匹配)
	             
	 ---  
	   
	    db.user.update({"name":{$regex:/\w*/}},{$inc:{"age":1}},{multi:true})
	    
	    db.user.update({"name":/^js/},{$set:{"age":40}},{"multi":true})
	    
	    db.user.find({"name":/java/im}).pretty()
	    
	查询name属性包含py开头的document
	    
	    db.getCollection('user').find({"name":/py/})
	    
	查询name属性以py开头的document
	    
	    db.getCollection('user').find({"name":/^py/})
	    
	查询nmae属性以on结尾的document
	    
	    db.getCollection('user').find({"name":/on$/})
	             
	支持直接写正则表达式
	
		 {field:/pattern/options},
		 
		 db.user.update({"name":/\w*/},{$inc:{"age":1}},{multi:true})

9. limit() & skip

		db.user.find().pretty().limit(2) #查询前两条数据
		
		#跳过前2条记录，查询两条记录。最终结果为3，4两条记录
		db.user.find().pretty().limit(2).skip(2)
10. sort()
		
	在 MongoDB 中使用 sort() 方法对数据进行排序，sort() 方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而 -1 是用于降序排列。
	
		#先根据name排序，然后取前两条
		db.user.find().sort({"name":1}).limit(2)
11. $type

	$type操作符是基于BSON类型来检索集合中匹配的数据类型，并返回结果。
	
	MongoDB 中可以使用的类型如下表所示：

	|类型|	数字|	
	---|---|
	|Double|	1|	 
	|String|	2|	 
	O|bject|	3|	 
	|Array|	4|	 
	|Binary| data	|5|	 
	|Object| id|	7|	 
	|Boolean|	8|	 
	|Date|	9|	 
	|Null|	10|	 
	|Regular| Expression|	11|	 
	|JavaScript|	13|	 
	|32-bit integer|	16	| 
	|Timestamp|	17|	 
	|64-bit integer|	18|	 
	
		db.nike.find({"acount":{$type:1}})
		
		db.nike.find({"acount":{$type:2}})
		#等价于
		db.nike.find({"acount":{$type:“string”}})
10. 索引

	[参考文献](http://www.mongoing.com/archives/2797)
	
	全文搜索是 mongodb的一个特性，正则表达是在效率上等同在该字段上进行全部扫描(除了在该字段上建立索引并使用^符号进行查找，该操作是会走索引的)，当需要正则搜索的文档到了一定的量级，模糊是查询的效率还是会很低的。

   全文搜索就是在需要搜索的字段上加上一个文本索引，**注意：一个集合只能支持建立一个全文索引，但该索引可以包含多个字段做联合索引。**

   该索引支持字段的值为string或者string类型的array,
   
	1. 新建索引

	
			db.collection.ensureIndex(keys, options)
			#为field字段设置索引，1表示升序，-1表示降序
			db.nike.ensureIndex({"title":1})
	
		options，可选参数，表示建立索引的设置。可选值如下：
		
		* background，Boolean，在后台建立索引，以便建立索引时不阻止其他数据库活动。默认值 false。
		* unique，Boolean，创建唯一索引。默认值 false。
		* name，String，指定索引的名称。如果未指定，MongoDB会生成一个索引字段的名称和排序顺序串联。
		* dropDups，Boolean，创建唯一索引时，如果出现重复删除后续出现的相同索引，只保留第一个。
		* sparse，Boolean，对文档中不存在的字段数据不启用索引。默认值是 false。
		* v，index version，索引的版本号。
			weights，document，索引权重值，数值在 1 到 99,999 之间，表示该索引相对于其他索引字段的得分权重。
	2. 重建索引

			db.COLLECTION_NAME.reIndex()
	3. 查看索引

			db.COLLECTION_NAME.getIndexes()
		查看索引的大小
		
			db.COLLECTION_NAME.totalIndexSize()

	4. 删除索引

			db.COLLECTION_NAME.dropIndex("INDEX-NAME")



	

11. MongoDB支持多种类型的索引，包括单字段索引、复合索引、多key索引、文本索引等，每种类型的索引有不同的使用场合。

	1. 单字段索引 （Single Field Index）
    
    		db.user.createIndex( {age: 1} ) 
	
		上述语句针对age创建了单字段索引，其能加速对age字段的各种查询请求，是最常见的索引形式，MongoDB默认创建的id索引也是这种类型。

	2. 复合索引 (Compound Index)

		复合索引是Single Field Index的升级版本，它针对多个字段联合创建索引，先按第一个字段排序，第一个字段相同的文档按第二个字段排序，依次类推，如下针对age, name这2个字段创建一个复合索引。

    		db.user.createIndex( {age: 1, name: 1} ) 
    3. 多key索引 （Multikey Index）

		当索引的字段为数组时，创建出的索引称为多key索引，多key索引会为数组的每个元素建立一条索引，比如person表加入一个habbit字段（数组）用于描述兴趣爱好，需要查询有相同兴趣爱好的人就可以利用habbit字段的多key索引。
		
			{"name" : "jack", "age" : 19, habbit: ["football, runnning"]}
			db.user.createIndex( {habbit: 1} )  // 自动创建多key索引
			db.user.find( {habbit: "football"} )	            
	