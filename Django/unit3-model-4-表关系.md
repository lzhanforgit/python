# mysql-多表查询
3. 表关系



	* 一对多：models.ForeignKey(其他表)
	* 多对多：models.ManyToManyField(其他表)
	* 一对一：models.OneToOneField(其他表)

		
	
1. 一对多关系(从表为userinfo和主表usertype)

	1. 设置外键

			    user_type=models.ForeignKey(to="usertype",to_field="id",default=1,on_delete= models.CASCADE)
			    
		>此时、主表为usertype,从表为userinfo.**注意在数据库中表明为“模块名_类名的小写形势”。加入模块名为userinfo,这两个表名分贝为“user_usertype”和"user_userinfo".**
		>在从表中会产生一个新的字段：user\_type_id.但注意user\_type代表的是主表usertpye对象。
	
		**注意加上on_delete= models.CASCADE**
		
		- models.CASCADE，删除关联数据，与之关联也删除
	   
	   - models.DO_NOTHING，删除关联数据，引发错误IntegrityError
	   
	   - models.PROTECT，删除关联数据，引发错误ProtectedError
	   
	   - models.SET_NULL，删除关联数据，与之关联的值设置为null（前提FK字段需要设置为可空）
	   
	   - models.SET_DEFAULT，删除关联数据，与之关联的值设置为默认值（前提FK字段需要设置默认值）


	2. 查询数据数据时user_type就是主表的对象
		
		####查询数据
		1. 正向查询（由从表到主表的查询）

				users=models.userinfo.objects.all()
	
			    for user in users:
			        print(user.user_type.id) #等价于print(user.user_type_id)
			        print(user.user_type.name)
		        
			如果单纯想拿到user_type的值可以这么样：
					
				users=models.userinfo.objects.all().values('telephone','password','user_type')
		
			**请注意这是数据的类型为字典类型的queryset**
		
		2. 逆向查询（由主表到从表的查询）
		 
				#get得到的直接是一个对象，不过get只能查看有一条记录的
				#查询类型为vip的对象
				t = models.usertype.objects.get(name='vip')
				
				#查询类型为vip的所有用户
				
				users=t.userinfo_set.all()
				#users=t.userinfo_set.all().values()
				#users=t.userinfo_set.all().values("id","telephone")
				
			>注意userinfo_set为系统提供的集合表示方式
				
				
	3. 比较厉害的双下划线

			users=models.userinfo.objects.all().values('telephone','user_type__name')# __name
			
		s数据类型
		
			{"telephone": "root", "password": "999", "user_type__name": "\u666e\u901a\u7528\u6237"}, {"telephone": "admin", "password": "123", "user_type__name": "VIP\u7528\u6237"}
	
	####添加数据
	
	1. 方式一，先主表然后从表(不推荐)

		例如：
			try:
	            t = {
	                "name": "user"
	            }
	
	
	            obj = models.Type.objects.create(**t)
	            print(obj.id)
	            
	            #获取主表id
	            user = {
	                "telephone": "138",
	                "password": "111",
	                "user_type_id":obj.id
	            }
	
	            obj_u=models.UserInfo.objects.create(**user)
	2. 方式二

		例如：增加一个vip用户
		
			#1. 找出类型表中vip
			
				obj_type =models.Type.objects.filter(name='vip')[0]
			#2. 把查出的对象直接写入，注意user_type就是一对多链接对象： 
			# user_type=models.ForeignKey(to='Type',to_field='id',default=1,on_delete=models.CASCADE)

			
				user = {
                "telephone": "139",
                "password": "222",
                "user_type":obj_type
            }

            obj_u=models.UserInfo.objects.create(**user)

1. 多对多关系

	需要导入包时：
		
		from jobapp.models import *
	
	因为setting.py已经设置
	
		INSTALLED_APPS = [
		    'django.contrib.admin',
		    'django.contrib.auth',
		    'django.contrib.contenttypes',
		    'django.contrib.sessions',
		    'django.contrib.messages',
		    'django.contrib.staticfiles',
		    'position',
		    'jobapp'
		
		]
		
	
2. 创建多对多关系表

		
		# 模拟多对多关系：用户-投递-职位
		class applyposition(models.Model):
		    id = models.AutoField(primary_key=True)
		    # 自动创建一个id列，id为主键、自增长
		    uobj = models.ForeignKey(to=userinfo,to_field='id',on_delete=True)
		    pobj = models.ForeignKey(to="position",to_field='id',on_delete=True)
		    publish_time=models.DateTimeField(auto_now_add=True,null=True)
		    
	**当然，这样创作好理解但是繁琐，我们可以直接在岗位模型中加入一条语句**
	
		from jobapp.models import *
		
		#在job表中
		apply=models.ManyToManyField(userinfo)
		
3. 数据操作

	1. 增加数据

		这个时候要先确定一个条件，比如user01投递了position01,那么我们就确定了岗位：
			
			pos=positon.objects.get(id=1)
			
			pos.apply.add(1) #这个时候的1就是用户id
			pos.apply.add(1,2,3) #这个时候的1,2,3就是用户id
			pos.apply.add(*[1,2,3,4]) #这个时候的1就是用户id
			
	2. 删除数据

			pos.apply.remove(2)
			pos.apply.remove(1,2,3)	
			pos.apply.remove(*[1,2,3])	
			pos.apply.clear()
			
	3. 修改数据
			
			#关系表中岗位表是1的，只会有用户名1，2，3.其他都会删除
			pos.apply.set(1,2,3)
			
	3. 查询数据
			
			pos=positon.objects.get(id=1)
			
			#此时拿到的对象集合为用户对象集合
			pos.apply.all()
			
			#要拿到关联表中（比如用户表中的）其他字段
			
			pos.apply.all().values('job_apply_password','job_apply_telephone')
			
		==
			# 添加数据
		    pp = models.position.objects.get(id=2)
		    pp.apply.add(7)
		    
		    #查询数据
		    pos=models.position.objects.get(id=1)
		    print(pos.name)
		    print(pos.apply.all().filter(id=1))
		    users=pos.apply.all()
		    for u in users:
		        print(u.telephone)	
	
			