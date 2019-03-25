# mysql-增删改查
1. 查询行数
		
		#查询结果的行数
		# users=models.userinfo.objects.all().count()
		users=models.userinfo.objects.filter(id=1).count()
		#查询第一个结果
		# user=models.userinfo.objects.all().first()
		# user=models.userinfo.objects.get(id=1)
		
		
    	
 
2. 关系查询

	**注意双下划线**
		
		#获取部分列
		users=models.userinfo.objects.all().values(‘id’,'telephone')
		#这个时候users为字典列表，通过list(users)转化为字典列表，然后json.dumps(list(users))转化为字符串，传给客户端即可。
				
		#获取部分列
		models.userinfo.objects.all().values_list(‘id’,'telephone')
		#这个时候users为元组列表

		# 大于，小于
		# models.userinfo.objects.filter(id__gt=1)              # 获取id大于1的值
      	# models.userinfo.objects.filter(id__gte=1)              # 获取id大于等于1的值
      	# models.userinfo.objects.filter(id__lt=10)             # 获取id小于10的值
      	# models.userinfo.objects.filter(id__lte=10)             # 获取id小于10的值
        # models.userinfo.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
        
        #不等于
        
        from django.db.models import Q
        #查询工资不等于10000
        jobs = models.job.objects.filter(~Q(salary_min=10000)).values('title','com_name','salary_min')
        
3. in

		# models.userinfo.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
      	# models.userinfo.objects.exclude(id__in=[11, 22, 33])  # not in 
      	
4. is null

		    users=models.userinfo.objects.filter(id__isnull=False) #True

5. contains

		  users=models.userinfo.objects.filter(email__contains='admin')
		  
		  #不区分大小写
		  
		  users=models.userinfo.objects.filter(email__icontains='admin')
			
		#不包含
			
		 users=models.userinfo.objects.exclude(email__icontains='admin')

6. range

		users=models.userinfo.objects.filter(id__range=[3,7])
		
7. endswith startswith
8. order_by()

		users=models.userinfo.objects.all().order_by('id') #asc
		users=models.userinfo.objects.all().order_by('-id') #desc
		
9. group by

	group by
	
        #
        # from django.db.models import Count, Min, Max, Sum
        # models.Tb1.objects.filter(c1=1).values('id').annotate(c=Count('num'))
        # SELECT "app01_tb1"."id", COUNT("app01_tb1"."num") AS "c" FROM "app01_tb1" WHERE "app01_tb1"."c1" = 1 GROUP BY "app01_tb1"."id"

10. limit

		models.Tb1.objects.all()[10:20]
11. regex正则匹配，iregex 不区分大小写

		users=models.userinfo.objects.filter(email__regex=r'_admin')

12. date

	date
	
        #
        # Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
        # Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))

        # year
        #
        # Entry.objects.filter(pub_date__year=2005)
        # Entry.objects.filter(pub_date__year__gte=2005)

13. 执行原生SQL

	    # from django.db import connection, connections
	    # cursor = connection.cursor()  # cursor = connections['default'].cursor()
	    # cursor.execute("""SELECT * from auth_user where id = %s""", [1])
	    # row = cursor.fetchone()