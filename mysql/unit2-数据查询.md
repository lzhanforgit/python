# unit2-数据查询

1. 	查询表中的若干列

		SELECT Sno，Sname
		FROM Student；
		#查询所有列
		SELECT *
		FROM Student；
2. select 字句

	1. 算术表达式

			SELECT Sname，2018-Sage    /*假定当年的年份为2018年*/
			FROM Student；

	1. 字符串常量

			SELECT Sname，‘我是测试列: '，2004-Sage，LOWER(Sdept)
			FROM Student；

	1. 函数
	1. 列别名 
3. 消除取值重复的行
	
		select DISTINCT(sno) as '学号' from sc
	
	🙋:查看有哪些学生参加了考试
4. where字句


	1. 比较运算符：
	
		=，>，<，>=，<=，!=，<>，!>，!<
	
	2. 范围运算符：
	
		BETWEEN AND，NOT BETWEEN AND
	
	3. 确定集合:
	
		IN，NOT IN
	
	4. 字符匹配：

		like not like
	5. 空值

		is null , is not null
	6. 逻辑
		
		not and or
		
	🙋:
	
	1. 查询计算机科学系全体学生的名单
		
	2. 查询所有年龄在20岁以下的学生姓名及其年龄
		
	3. 查询年龄在20~23岁之间的学生的 姓名、系别和年龄(between ..and..)
	4. 查询信息系（IS）、数学系（MA）和计算机科学系（CS）学生的姓名和性别。
	

		
		
5. like

	匹配串为含通配符的字符串:%  _

	🙋:
	
	查询姓"李"且全名为三个汉字的学生的姓名
	
6. is null is not null

	🙋:
	
	某些学生选修课程后没有参加考试，所以有选课记录，但没有考试成绩。查询缺少成绩的学生的学号和相应的课程号。

7. not and or

	🙋:
	查询计算机系年龄在20岁以下的学生姓名。
	
8. 排序

	可以按一个或多个属性列排序
	
	升序：ASC；降序：DESC；缺省值为升序
	
	🙋:
	
	查询全体学生情况，查询结果按所在系的系号升序排列，同一系中的学生按年龄降序排列。
	查看全体同学的数学成绩，并按降序排列
	
9. 聚合函数

	count() sum() avg() max() min()
	
	🙋:
	
	统计有多少学生参加考试
	
	3号课程的总成绩和平均分
	
	002学生的总分
	
	找出最低分
		
		select sum(grade) as '总分' from sc where sno=002;

		select min(grade),sno,cno from sc;

10. 分组
	
	HAVING短语与WHERE子句的区别：
	
	1. WHERE从中选择满足条件的元组
		
	2. HAVING短语作用于组，从中选择满足条件的组

	🙋: 
	
	查看每个人的总分和平均分
	
		select sum(grade),sno from sc GROUP BY sno;


		select avg(grade),sno from sc GROUP BY sno;
	
	查看平均分最高的信息

		select avg(grade),sno from sc GROUP BY sno ORDER BY avg(grade) desc;
		
	
	查看平均分不及格信息  where 首次筛选 having 分组后筛选

		select avg(grade),sno from sc GROUP BY sno having avg(grade)<60;
	
	查看平均分大于70，并从高到低排列
		select avg(grade),cno from sc GROUP BY cno having avg(grade)>70 ORDER BY avg(grade) asc;
	
	找出参加三门考试的同学
	
		select count(sno),sno from sc GROUP BY sno HAVING count(*)>=3;
	
	统计每门课程的选修人数
			SELECT COUNT(sno) as '考试人数', cno as '课程编号' FROM sc GROUP BY cno 
			统计选修人数少于2人的课程标号
			SELECT COUNT(sno) as '考试人数', cno as '课程编号' FROM sc GROUP BY cno HAVING COUNT(sno)<2
		
	-- ??将每门课程的平均分按从高到低排序 
	
	-- ??将每门课程的最高分分按从高到低排序，并指出是哪位同学
	
	-- ??将每个学生的平均分从高到低排序
3. limit 

	limit start,total;
	
  	start:开始记录
  	
  	total:总共取多少行记录
  	
  	🙋: 
  	
  	总分前3名的学生
		select sum(grade),sno from sc GROUP BY sno ORDER BY sum(grade) desc limit 0,3;

	总分倒数第一的学生

		select sum(grade),sno from sc GROUP BY sno ORDER BY sum(grade) asc limit 0,1;

# 内置函数
	
1. 数学函数


	1. abs(x)
	1. pi()
	1. mod(x,y)
	1. sqrt(x)
	1. ceil(x)或者ceiling(x)
	1. rand(),rand(N):返回0-1间的浮点数，使用不同的seed N可以获得不同的随机数
	1. round(x, D)：四舍五入保留D位小数，D默认为0， 可以为负数， 如round(19, -1)返回20
	1. truncate(x, D):截断至保留D位小数，D可以为负数， 如trancate(19,-1)返回10
	1. sign(x): 返回x的符号，正负零分别返回1， -1， 0
	1. pow(x,y)或者power(x,y)
	1. exp(x)：e^x

2. 字符串函数

	1. char_length(str):返回str所包含的字符数，一个多字节字符算一个字符
	1. length(str): 返回字符串的字节长度，如utf8中，一个汉字3字节，数字和字母算一个字节
	1. concat(s1, s1, ...): 返回连接参数产生的字符串
	1. concat_ws(x, s1, s2, ...): 使用连接符x连接其他参数产生的字符串
	1. INSERT(str,pos,len,newstr):返回str,其起始于pos，长度为len的子串被newstr取代。
		1. 若pos不在str范围内，则返回原字符串str
		2. 若str中从pos开始的子串不足len,则将从pos开始的剩余字符用newstr取代
		3. 计算pos时从1开始，若pos=3,则从第3个字符开始替换
	1. lower（str)或者lcase(str):
	1. upper(str)或者ucase(str):
	1. left(s,n):返回字符串s最左边n个字符
	1. right(s,n): 返回字符串最右边n个字符
	1. ltrim(s):删除s左侧空格字符
	1. rtrim(s):
	1. TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str)或TRIM([remstr FROM] str)：从str中删除remstr, remstr默认为空白字符
	1. REPEAT(str,count)：返回str重复count次得到的新字符串
	1. REPLACE(str,from_str,to_str)： 将str中的from_str全部替换成to_str
	1. SPACE(N):返回长度为N的空白字符串
	1. STRCMP(str1,str2):若str1和str2相同，返回0， 若str1小于str2, 返回-1， 否则返回1.
	1. SUBSTRING(str,pos), SUBSTRING(str FROM pos), 	1. SUBSTRING(str,pos,len), SUBSTRING(str FROM pos FOR len),MID(str,pos,len): 获取特定位置，特定长度的子字符串

3. 日期函数

	1. CURDATE(), CURRENT_DATE, CURRENT_DATE():用于获取当前日期，格式为'YYYY-MM-DD'
	2. CURTIME([fsp]), CURRENT_TIME, CURRENT_TIME([fsp]): 用于获取当前时间， 格式为'HH:MM:SS' 
	3. CURRENT_TIMESTAMP, CURRENT_TIMESTAMP([fsp]), LOCALTIME, LOCALTIME([fsp]), SYSDATE([fsp]), NOW([fsp]): 用于获取当前的时间日期，格式为'YYYY-MM-DD HH:MM:SS'
	4. UNIX\_TIMESTAMP(), UNIX\_TIMESTAMP(date)：返回一个unix时间戳（'1970-01-01 00:00:00' UTC至今或者date的秒数），这实际上是从字符串到整数的一个转化过程
	5. FROM_UNIXTIME(UNIX_TIMESTAMP('2010-3-3'))从时间戳返回日期
	
	6. 提取时间
	
			MONTH(date)
			MONTHNAME(date)
			DAYNAME(date)
			DAY(date)，DAYOFMONTH(date)：1-31或者0
			DAYOFWEEK(date)：1-7==>星期天-星期六
			DAYOFYEAR(date)： 1-365（366）
			WEEK(date[,mode])：判断是一年的第几周，如果1-1所在周在新的一年多于4天，则将其定为第一周；否则将其定为上一年的最后一周。mode是用来人为定义一周从星期几开始。
			WEEKOFYEAR(date)：类似week(date,3)，从周一开始计算一周。
			QUARTER(date)：返回1-4
			HOUR(time)：返回时间中的小时数，可以大于24
			MINUTE(time)：
			SECOND(time)：
			
	7. 返回两个日期相差的天数

			SELECT DATEDIFF(CURRENT_DATE(),DATE('2018-10-4'))
	8. 返回相隔的时间

			SELECT TimeDIFF(CURRENT_DATE(),DATE('2018-10-4'))
			
			#结果
				838:59:59
				
	参考：
	https://www.cnblogs.com/noway-neway/p/5211401.html
			
3. 系统信息函数


	1. VERSION():返回mysql服务器的版本，是utf8编码的字符串
	1. DATABASE()，SCHEMA()：显示当前使用的数据库
	1. SESSION_USER(), SYSTEM_USER(), USER(), CURRENT_USER, CURRENT_USER():返回当前的用户名@主机，utf8编码字符串
	1. CHARSET('hello') 字符编码
	1. COLLATION(str)	字符排序规则
	1. LAST\_INSERT\_ID()：自动返回最后一个insert或者update查询， 为auto_increment列设置的第一个发生的值

4. 加密函数

	1. password()
	1. MD5(str):计算MD5 128位校验和，返回32位16进制数构成的字符串，当str为NULL时返回NULL。可以用作哈希密码
	2. SHA1(str), SHA(str)：计算160位校验和，返回40位16进制数构成的字符串，当str为NULL时返回NULL。
	3. SHA2(str, hash_length)：计算SHA-2系列的哈希方法(SHA-224, SHA-256, SHA-384, and SHA-512). 第一个参数为待校验字符串，第二个参数为结果的位数（224， 256， 384， 512）