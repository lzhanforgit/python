##1. 索引

1. 索引分类

	简介
	MySQL目前主要有以下几种索引类型：
	1. 普通索引
	2. 唯一索引
	3. 主键索引
	4. 组合索引
	5. 全文索引

2. 创建索引总览

		CREATE TABLE table_name[col_name data type]
		[unique|fulltext][index|key][index_name](col_name[length])[asc|desc]

	1. unique|fulltext为可选参数，分别表示唯一索引、全文索引
	2. index和key为同义词，两者作用相同，用来指定创建索引
	3. col_name为需要创建索引的字段列，该列必须从数据表中该定义的多个列中选择
	4. index_name指定索引的名称，为可选参数，如果不指定，默认col_name为索引值
	5. length为可选参数，表示索引的长度，只有字符串类型的字段才能指定索引长度
	6. asc或desc指定升序或降序的索引值存储
3. 索引类型
	3. 普通索引
	
			ALTER TABLE jobs ADD INDEX(salary_max);
			CREATE INDEX index_salary_max ON jobs(salary_max)
			#删除索引
			ALTER TABLE jobs DROP INDEX index_salary_max
			
			创建表的时候同时创建索引
	
			CREATE TABLE `table` (
			    `id` int(11) NOT NULL AUTO_INCREMENT ,
			    `title` char(255) CHARACTER NOT NULL ,
			    `content` text CHARACTER NULL ,
			    `time` int(10) NULL DEFAULT NULL ,
			    PRIMARY KEY (`id`),
			    INDEX index_name (title(length))
			)
	4. 唯一索引
	
		与前面的普通索引类似，不同的就是：索引列的值必须唯一(比如可以在主键上建立唯一索引)，但允许有空值。如果是组合索引，则列值的组合必须唯一。它有以下几种创建方式：
		
			CREATE UNIQUE INDEX unique_id ON jobs(id);
			ALTER TABLE jobs ADD UNIQUE(id);
		
	4. 主键索引
	
		是一种特殊的唯一索引，一个表只能有一个主键，不允许有空值。一般是在建表的时候同时创建主键索引：
	
			CREATE TABLE `table` (
			    `id` int(11) NOT NULL AUTO_INCREMENT ,
			    `title` char(255) NOT NULL ,
			    PRIMARY KEY (`id`)
			);
	4. 组合索引
	
		指多个字段上创建的索引，只有在查询条件中使用了创建索引时的第一个字段，索引才会被使用。使用组合索引时遵循最左前缀集合
	
			ALTER TABLE `table` ADD INDEX name_city_age (name,city,age); 
			
3. MYSQL order by排序与索引关系总结
	
	EXPLAIN sql 可以查看查询方式
	1. 场景一（比较在有索引的情况下时间）

			CREATE INDEX index_salary_max ON jobs(salary_max);
		
			# 没有索引
			select * from jobs where salary_min=12000;
			select id,title,com_name from jobs where salary_min=12000;

			
			# 有索引
			select * from jobs where salary_max=12000;
			select id,title,com_name from jobs where salary_max=12000;

			
		但是在下面两种情况下，查询就失去了索引的功能
		
			select * from jobs ORDER BY salary_max;
			select * from jobs ORDER BY salary_min;
			
		下面的情况速度就更慢了哦
		
			select salary_max,id,com_name from jobs ORDER BY salary_max;
			select salary_min,id,com_name from jobs ORDER BY salary_min;
			
	1. 如果索引了多列，要遵守最左前缀法则。所谓最左前列，指的是查询从索引的最左前列开始，并且不跳过索引中的列。

			CREATE INDEX index_salary_max ON jobs(com_id,publish_date);
		
			# 索引会起作用
			select salary_max,id,com_name from jobs where com_id='107045220';
			
			select salary_max,id,com_name from jobs 
			where com_id='107045220' and  publish_date='2018-12-07 10:27:01';
			
			# 索引不会起作用
			select salary_max,id,com_name from jobs where publish_date='2018-12-07 10:27:01';

	2. 当MySQL一旦估计检查的行数可能会”太多”，范围查找优化将不会被使用。

			#不会起作用
			EXPLAIN select salary_max,id,com_name from jobs where salary_max<20;

			
			#会起作用
			
			EXPLAIN select salary_max,id,com_name from jobs where salary_max<18000;
			
		>在应用中，可能不会碰到这么大的查询，但是应该避免这样的查 询出现: select uid from users where registered < 1295001384
		
	3. 索引列不应该作为表达式的一部分，即也不能在索引列上使用函数

			# 不会起作用
			EXPLAIN select salary_max,id,com_name from jobs where ABS(salary_max)<20;
	4. 尽量借用覆盖索引，减少select * from …语句使用
			
			# com_address 因为com_address没有索引，所以extra列为null
			EXPLAIN select salary_max,id,com_address from jobs where salary_max=20;
			
			# 因为id也有索引，所以所以extra列为Using index
			EXPLAIN select salary_max,id from jobs where salary_max=20;



		>第1句Extra中使用了Using index表示使用了覆盖索引。第3句也使用了覆盖索引,虽然ID不在索引uid_fuid索引列中，但是InnoDB二次索引(second index)叶子页的值就是PK值，不同于MyISAM。Extra部分的Using index表示应用了索引，不要跟type中的index混淆。第2句没有使用覆盖索引，因为fsex不在索引中。

	5. ORDER BY子句，尽量使用Index方式排序,避免使用FileSort方式排序
		
		MySQL支持二种方式的排序，FileSort和Index，后者效率高，它指MySQL扫描索引本身完成排序。FileSort方式效率较低。ORDER BY满足以下情况，会使用Index方式排序:
		
      a)ORDER BY 语句使用索引最左前列。参见第1句
            
      b)使用Where子句与Order BY子句条件列组合满足索引最左前列。参见第2句.
以下情况，

		**会使用FileSort方式的查询**
		
		1. 检查的行数过多，且没有使用覆盖索引。第3句，虽然跟第2句一样，order by使用了索引最左前列uid，但依然使用了filesort方式排序，因为status并不在索引中，所以没办法只扫描索引。
		2. 使用了不同的索引，MySQL每回只采用一个索引.第4句,order by出现二个索引，分别是uid_fuid和聚集索引(pk)
		3. 对索引列同时使用了ASC和DESC。 通过where语句将order by中索引列转为常量，则除外。第5句,和第6句在order by子句中，都出现了ASC和DESC排序,但是第5句却使用了filesort方式排序,是因为第6句where uid取出排序需要的数据,MySQL将其转为常量,它的ref列为const。
		4. where语句与order by语句，使用了不同的索引。参见第7句。
		5. where语句或者ORDER BY语句中索引列使用了表达式，包括函数表达式。参见第8，9句
		6. where 语句与ORDER BY语句组合满足最左前缀，但where语句中使用了条件查询。查见第10句,虽然where与order by构成了索引最左有缀的条件，但是where子句中使用的是条件查询。
		7. order by子句中加入了非索引列,且非索引列不在where子句中。
		8. order by或者它与where组合没有满足索引最左前列。参见第11句和12句,where与order by组合，不满足索引最左前列. （uid, fsex)跳过了fuid
		9. 当使用left join，使用右边的表字段排序。参见第13句，尽管user.uid是pk，依然会使用filesort排序。

	7. 慎用left join语句,避免创建临时表 使用left join语句的时候，避免出现创建临时表。尽量不要用left join，分而治之。非要使用的时候，要询问自己是不是真要必须要使用。
	8. 高选择性索引列。 尽量使用高选择性的过引来过滤数据。高选择性指Cardinality/#T越接近1，选择性越高，其中Cardinality指表中索引列不重复值(行)的总数。PK和唯一索引，具有最高的选择性，即1。推荐可选性达到20%以上。
	9. 谨防where子句中的OR。where语句使用or，且没有使用覆盖索引,会进行全表扫描。应该尽量避免这样OR语句。尽量使用UNION代替OR
	10. LIMIT与覆盖索引 limit子句，使用覆盖索引时比没有使用覆盖索引会快很多

	参考：http://www.cnblogs.com/wangxusummer/p/5329813.html
4. 全文索引
	
	1. 概述

		MySQL全文检索是利用查询关键字和查询列内容之间的相关度进行检索，可以利用全文索引来提高匹配的速度。


	2. 语法

			SELECT * FROM tab_name WHERE MATCH ('列名1,列名2...列名n') AGAINST('词1 词2 词3 ... 词m');
			
			SELECT * FROM jobs 
			WHERE MATCH (com_name) AGAINST('上海寰享网络科技有限公司');
			
		**col1、col2 必须是char、varchar或text类型，在查询之前需要在 col1 和 col2 上分别建立全文索引(FULLTEXT索引)。**
	3. dd

		







	#### 缺点
	1. 虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行insert、update和delete。因为更新表时，不仅要保存数据，还要保存一下索引文件。
	2. 建立索引会占用磁盘空间的索引文件。一般情况这个问题不太严重，但如果你在一个大表上创建了多种组合索引，索引文件的会增长很快。
	
	索引只是提高效率的一个因素，如果有大数据量的表，就需要花时间研究建立最优秀的索引，或优化查询语句。