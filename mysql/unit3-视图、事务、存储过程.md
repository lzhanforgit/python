# unit3-多表链接&存储过程
## 多表查询
1. 等值与非等值连接查询 
2. 自身链接
3. 外链接

## 存储过程

1. 索引	添加索引
			ALTER TABLE student ADD INDEX index_name(sname);	删除索引
			DROP INDEX index_name ON student；	添加全文索引
			ALTER TABLE student add FULLTEXT INDEX index_name(sname)；
			查看设计SQL语句
			show CREATE TABLE student；2. 视图	根据查询结果生成一张新表
			
			create table student_last(select * from student  order by id desc limit 5);
	查看设计视图
			DESC student；	查询李丽的C语言成绩		SELECT student.sno,student.sname,course.cname,sc.grade		FROM student INNER JOIN sc ON student.sno=sc.sno							INNER JOIN course ON course.cno=sc.cno		WHERE student.sname='李丽' AND course.cname='c'	建立学生成绩视图		CREATE VIEW view_stugrade		AS		SELECT student.sno,student.sname,course.cname,sc.grade		FROM student INNER JOIN sc ON student.sno=sc.sno							INNER JOIN course ON course.cno=sc.cno;	??不用视图完成把李丽的C语言成绩改成80-》》》》作业	在视图中查找李丽的C语言成绩
			SELECT * FROM view_stugrade WHERE sname='李丽' AND cname ='c';	把李丽的C语言成绩改成80
			UPDATE view_stugrade SET grade=80 WHERE sname='李丽' AND cname ='c';		UPDATE sc set grade=90 WHERE id=6;	查看所有表和视图
			SHOW TABLES;
			删除视图
			DROP VIEW view_stugrade;3.	子查询

	查询和李丽的C语言成绩相同的学生信息（利用视图）
			SELECT * FROM view_stugrade 		WHERE grade=(SELECT grade from view_stugrade WHERE sname='李丽' AND cname='c')		AND sname NOT LIKE '李丽';
			??查询和李丽的C语言成绩相同的学生信息（不利用视图）
			SELECT student.sno,student.sname,course.cname,sc.grade		FROM student INNER JOIN sc ON student.sno=sc.sno							INNER JOIN course ON course.cno=sc.cno		WHERE sc.grade=(SELECT sc.grade							FROM student INNER JOIN sc ON 		student.sno=sc.sno							INNER JOIN course ON course.cno=sc.cno							WHERE student.sname='李丽' AND course.cname='c'									)			AND student.sname <>'李丽'	查询李丽所有课程的成绩
			SELECT * FROM view_stugrade WHERE sname='李丽' AND cname 		in(SELECT cname from course)	查询李丽C 和 C++课程的成绩
			SELECT * FROM view_stugrade WHERE sname='李丽' AND cname in('c','c++')
				??查询成绩比李丽最高分还要高的学生信息-1		SELECT * FROM view_stugrade WHERE grade>(SELECT MAX(grade) FROM view_stugrade WHERE sname='李丽')	查询成绩比李丽最低分要高的学生信息-1
		SELECT * FROM view_stugrade WHERE grade>(SELECT min(grade) FROM view_stugrade WHERE sname='李丽')	2. mysql 函数
	创建函数
			USE school;		CREATE FUNCTION fun_getage(str VARCHAR(12))		RETURNS CHAR(12)		BEGIN			RETURN(SELECT sage from student WHERE sname=str);		END;
		 	调用方法			SELECT fun_getage('李彤')
		方法：
		1. 必须有返回值	2. 返回值指定类型 RETURNS	3. 返回值通过     return 			USE school;
			delimiter &&			CREATE FUNCTION fun_getscore(nstr VARCHAR(12),cstr VARCHAR(12))			RETURNS INT			BEGIN				-- 		申明变量				DECLARE sco INT;				SET sco=0;				SELECT grade INTO sco FROM view_stugrade WHERE sname=nstr 				AND cname=cstr;				RETURN sco;				END &&			SELECT fun_getscore('李丽','c')			USE school;			CREATE FUNCTION fun_ispass(nstr VARCHAR(12),cstr VARCHAR(12))			RETURNS CHAR(10)			BEGIN				-- 		申明变量				DECLARE sco INT DEFAULT 0;				DECLARE res CHAR(10) DEFAULT '';				SELECT grade INTO sco FROM view_stugrade WHERE sname=nstr AND cname=cstr;				IF sco>60 and sco<100 THEN					SET res='及格';				ELSEIF sco=100 then					SET res='满分';				ELSE					SET res='不及格';				END IF;					RETURN res;			END;			SELECT fun_ispass('李丽','c')4. 存储过程

	创建存储过程
			CREATE PROCEDURE pro_test()			BEGIN				SELECT "ok";			END		CALL pro_test()		CREATE PROCEDURE pro_test1(IN n INT)			BEGIN				SELECT n*n;			END		CALL pro_test1(20)		-- 	DECLARE a INT DEFAULT 20;		-- 	CALL pro_test1(a);不可行	--		SET @a=20;		CALL pro_test1(@a)		CREATE PROCEDURE pro_test2(IN n INT,OUT m INT)		BEGIN			SET m=n*n;		END		SET @a=20;		set @b=0;		CALL pro_test2(@a,@b);		SELECT @b;
	--			CREATE PROCEDURE pro_test3(INOUT n INT)		BEGIN			SET n=n*n;		END		set @a=20;		CALL pro_test3(@a);		SELECT @a;	--
			CREATE PROCEDURE pro_delstudent(in strname VARCHAR(12))		BEGIN			DECLARE num VARCHAR(12) DEFAULT '';			SELECT sno INTO num FROM student WHERE sname=strname;			DELETE FROM sc WHERE sno=num;			DELETE FROM student WHERE sno=num;			SELECT '删除成功';		END		CALL pro_delstudent('李彤')	--
			CREATE PROCEDURE pro_loop(INOUT num DOUBLE)		BEGIN			DECLARE total DOUBLE DEFAULT 0;			DECLARE i INT DEFAULT 0;			WHILE i<num DO				SET total=total+i;				SET i=i+1;			END WHILE;			SET num=total;		END		set @n=100;		CALL pro_loop(@n);		SELECT @n;	--
			CREATE PROCEDURE pro_loop1(INOUT num DOUBLE)			BEGIN				DECLARE total DOUBLE DEFAULT 0;				DECLARE i INT DEFAULT 0;				my:WHILE i<num DO					SET total=total+i;					IF total>2000 THEN						LEAVE my;					END IF;					SET i=i+1;				END WHILE;				SET num=total;			END	**带事务的存储过程******************
			CREATE PROCEDURE pro_delstudent(in strname VARCHAR(12))			BEGIN							DECLARE num VARCHAR(12) DEFAULT '';				SELECT sno INTO num FROM student WHERE sname=strname;				DELETE FROM sc WHERE sno=num;				DELETE FROM student WHERE sno=num;				SELECT '删除成功';			END	--		select * from user;		start TRANSACTION;		UPDATE user set money=money+1000 WHERE id=1;		UPDATE user set money=money-1000 where id=2;		ROLLBACK;		COMMIT;	案例：
	
		delimiter &&
		create procedure change_money(in sender varchar(255),in receiver varchar(255),in number DOUBLE,out result varchar(20))
		begin
			declare acount DOUBLE DEFAULT 0;
			start TRANSACTION;
			update user set money=money-number where name=sender;
			select money into acount from user  where name=sender;
			if acount<0 THEN
				set result='转账失败';
				ROLLBACK;
			ELSE
				update user set money=money+number where name=receiver;
				set result='转账成功';
				COMMIT;
			
			end if;
			
			
		end 
		&&
		
		set @send='tony';
		set @receive='tom';
		set @acount=300;
		
		set @res='';
		
		call change_money(@send,@receive,@acount,@res);
		select @res;