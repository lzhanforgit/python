#mysql-基础
1. 介绍

	20世纪90年代诞生于瑞典

	2008年被SUN收购
	
	2009年SUN被ORICAL收购
	
	[官网](http://dev.mysql.com/downloads/installer/)
2. 80版本navigat无法登陆的情况


	命令行 mysql -u root -p 然后进入管理页面
	
	ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
2. 安装目录及配置

	1. windows: my.ini
	2. mac: my.conf

	配置参数
		
		# 以下选项会被MySQL客户端应用读取。  
		# 注意只有MySQL附带的客户端应用程序保证可以读取这段内容。  
		# 如果你想你自己的MySQL应用程序获取这些值。  
		# 需要在MySQL客户端库初始化的时候指定这些选项。
		[client]
		port        = 3306
		socket      = /usr/local/mysql/mysql.sock
		# MySQL 服务端
		[mysqld]
		#默认存储引擎INNODB
		default-storage-engine=INNODB
		#GROUP_CONCAT长度
		group_concat_max_len =99999
		#端口号
		port        = 3306
		#socket位置
		socket      = /usr/local/mysql/mysql.sock 
		#pid写入文件位置
		pid-file        = /usr/local/mysql/mysqld.pid
		#数据库文件位置
		datadir         = /home/data/mysql/data
		user        = mysql
		#SQL模式具体查阅相关资料
		sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
		#当外部锁定（external-locking）起作用时，每个进程若要访问数据表,
		#则必须等待之前的进程完成操作并解除锁定。由于服务器访问数据表时经常需要等待解锁,
		#因此在单服务器环境下external locking会让MySQL性能下降。
		#所以在很多Linux发行版的源中，MySQL配置文件中默认使用了skip-external-locking来避免external locking。
		skip-external-locking
		#跳过DNS反向解析
		skip-name-resolve
		#关闭TIMESTAMP类型默认值
		explicit_defaults_for_timestamp
3. 启动服务

	windows:
	
	1. service mysqld start
	2. service mysqld stop
	3. service mysqld restart
	4. service mysqld status
	
4. 三大范式

	为了建立冗余较小、结构合理的数据库，设计数据库时必须遵循一定的规则。在关系型数据库中这种规则就称为范式。范式是符合某一种设计要求的总结。要想设计一个结构合理的关系型数据库，必须满足一定的范式。
	
	1. 第一范式(确保每列保持原子性)

		第一范式是最基本的范式。如果数据库表中的所有字段值都是不可分解的原子值，就说明该数据库表满足了第一范式。
		
		第一范式的合理遵循需要根据系统的实际需求来定。比如某些数据库系统中需要用到“地址”这个属性，本来直接将“地址”属性设计成一个数据库表的字段就行。但是如果系统经常会访问“地址”属性中的“城市”部分，那么就非要将“地址”这个属性重新拆分为省份、城市、详细地址等多个部分进行存储，这样在对地址中某一部分操作的时候将非常方便。这样设计才算满足了数据库的第一范式，如下表所示。
	
	2. 第二范式(确保表中的每列都和主键相关)

		第二范式在第一范式的基础之上更进一层。第二范式需要确保数据库表中的每一列都和主键相关，而不能只与主键的某一部分相关（主要针对联合主键而言）。也就是说在一个数据库表中，一个表中只能保存一种数据，不可以把多种数据保存在同一张数据库表中。
		
		比如要设计一个订单信息表，因为订单中可能会有多种商品，所以要将订单编号和商品编号作为数据库表的联合主键，如下表所示。
		
		订单信息表

		![dd](https://pic002.cnblogs.com/images/2012/270324/2012040114063976.png)
		
		这样就产生一个问题：这个表中是以订单编号和商品编号作为联合主键。这样在该表中商品名称、单位、商品价格等信息不与该表的主键相关，而仅仅是与商品编号相关。所以在这里违反了第二范式的设计原则。

		而如果把这个订单信息表进行拆分，把商品信息分离到另一个表中，把订单项目表也分离到另一个表中，就非常完美了。
		
		案例分析：
		
		学生| 课程| 老师| 老师职称| 教材| 教室| 上课时间| 
		---|---|---|---|---|---|---|
		小明| 一年级语文（上）| 大宝| 副教授| 《小学语文1》| 101| 14：30| 

	3. 第三范式(确保每列都和主键列直接相关,而不是间接相关)

		第三范式需要确保数据表中的每一列数据都和主键直接相关，而不能间接相关。
		
		比如在设计一个订单数据表的时候，可以将客户编号作为一个外键和订单表建立相应的关系。而不可以在订单表中添加关于客户其它信息（比如姓名、所属公司等）的字段。如下面这两个表所示的设计就是一个满足第三范式的数据库表。
		
		![](https://pic002.cnblogs.com/images/2012/270324/2012040114105477.png)
		
		
		drop database if exists db_name;
		
4. DDL

	新建数据库
	
		-- 数据库名不需要加引号
		DROP database if EXISTS mystudents;
		CREATE DATABASE mystudents DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
		
	新建表结构
	
		-- 新建student表

		-- drop TABLE if EXISTS student;
		CREATE table student(
			id int PRIMARY KEY auto_increment,
			sno VARCHAR(10) UNIQUE,
			sname varchar(20) not NULL,
			sgender VARCHAR(2) DEFAULT '女',
			sbirthday date,
			sdept varchar(20)
		
		)
		
		
		-- 新建course
		
		CREATE table course(
			cno VARCHAR(4) PRIMARY key,
			cname VARCHAR(40) not null,
			cpno varchar(4),
			ccredit SMALLINT,
		-- 	记住属性要用括号
			FOREIGN key(cpno) REFERENCES course(cno)
		)
		
		
		-- 新建sc表
		
		create table sc(
			sno VARCHAR(10),
			cno varchar(4),
			grade SMALLINT,
			PRIMARY key(sno,cno),
			FOREIGN key(sno) REFERENCES student(sno),
			FOREIGN key(cno) REFERENCES course(cno)
		) 
		
		
		-- 查看表结构
		
		desc sc;
		show create table sc;
		
		-- 修改表约束
			
		alter table sc add FOREIGN key(sno) REFERENCES student(sno);
		alter table sc add FOREIGN key(cno) REFERENCES course(cno);
		
		
		use mystudents;

