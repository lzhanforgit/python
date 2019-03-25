# mysql
1. model字段类型

			  *'AutoField': 'integer AUTO_INCREMENT',
            'BigAutoField': 'bigint AUTO_INCREMENT',
            'BinaryField': 'longblob',
            *'BooleanField': 'bool',
            *'CharField': 'varchar(%(max_length)s)',
            'CommaSeparatedIntegerField': 'varchar(%(max_length)s)',
            *'DateField': 'date',
            *'DateTimeField': 'datetime',
            *'DecimalField': 'numeric(%(max_digits)s, %(decimal_places)s)',
            'DurationField': 'bigint',
            'FileField': 'varchar(%(max_length)s)',
            'FilePathField': 'varchar(%(max_length)s)',
            *'FloatField': 'double precision',
            *'IntegerField': 'integer',
            'BigIntegerField': 'bigint',
            'IPAddressField': 'char(15)',
            'GenericIPAddressField': 'char(39)',
            'NullBooleanField': 'bool',
            *'OneToOneField': 'integer',
            'PositiveIntegerField': 'integer UNSIGNED',
            'PositiveSmallIntegerField': 'smallint UNSIGNED',
            'SlugField': 'varchar(%(max_length)s)',
            'SmallIntegerField': 'smallint',
            *'TextField': 'longtext',
            *'TimeField': 'time',
            *'UUIDField': 'char(32)',
            
   
   DEMO:
   	
   		from django.db import models

		# Create your models here.
		class userinfo(models.Model):
		    # id = models.IntegerField(primary_key=True)
		    id = models.AutoField(primary_key=True)
		
		    # 自动创建一个id列，id为主键、自增长
		    telephone = models.CharField(unique=True,max_length=11)
		    password = models.CharField(max_length=64)
		    email = models.EmailField(null=True,db_column='uemail')
		    regist_time=models.DateTimeField(auto_now_add=True,null=True)
		    salary = models.DecimalField(max_digits=5, decimal_places=2)  # 一共5位，保留两位小数
		    
		    ########Admin部分。放在后面谈......
		    # Admin为了不额外添加一张用户类型表，可以使用choices字段
		    user_types=(
		        (1,'普通用户'),
		        (2,'VIP用户'),
		        (3,'管理员')
		    )
		
		 user_type_id=models.IntegerField(choices=user_types,default=1)
		    # memo = models.TextField()

2. model 数据约束

		 null                数据库中字段是否可以为空
	    db_column           数据库中字段的列名
	        email = models.EmailField(null=True,db_column='uemail')

	    
	    db_tablespace
	    default             数据库中字段的默认值
	    primary_key         数据库中字段是否为主键
	    
	   		telephone = models.CharField(unique=True,max_length=30)

	    db_index            数据库中字段是否可以建立索引
	    unique              数据库中字段是否可以建立唯一索引
	    unique_for_date     数据库中字段【日期】部分是否可以建立唯一索引
	    unique_for_month    数据库中字段【月】部分是否可以建立唯一索引
	    unique_for_year     数据库中字段【年】部分是否可以建立唯一索引
		auto_now_add			 该列自动填充系统当前时间
	==
	Admin模块中用到的字段
	
	    verbose_name        Admin中显示的字段名称
	    blank               Admin中是否允许用户输入为空
	    editable            Admin中是否可以编辑
	    help_text           Admin中该字段的提示信息
	    choices             Admin中显示选择框的内容，用不变动的数据放在内存中从而避免跨表操作
	                        如：gf = models.IntegerField(choices=[(0, '何穗'),(1, '大表姐'),],default=1)
	
	    error_messages      自定义错误信息（字典类型），从而定制想要显示的错误信息；
	                        字典健：null, blank, invalid, invalid_choice, unique, and unique_for_date
	                        如：{'null': "不能为空.", 'invalid': '格式错误'}
	
	    validators          自定义错误验证（列表类型），从而定制想要的验证规则
	                        from django.core.validators import RegexValidator
	                        from django.core.validators import EmailValidator,URLValidator,DecimalValidator,\
	                        MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator
	                        如：
	                            test = models.CharField(
	                                max_length=32,
	                                error_messages={
	                                    'c1': '优先错信息1',
	                                    'c2': '优先错信息2',
	                                    'c3': '优先错信息3',
	                                },
	                                validators=[
	                                    RegexValidator(regex='root_\d+', message='错误了', code='c1'),
	                                    RegexValidator(regex='root_112233\d+', message='又错误了', code='c2'),
	                                    EmailValidator(message='又错误了', code='c3'), ]
	                            )
	
		
	DEMO:
	
		class UserInfo(models.Model):
	        nid = models.AutoField(primary_key=True)
	        username = models.CharField(max_length=32)
	        class Meta:
	            # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
	            db_table = "table_name"
	
	            # 联合索引
	            index_together = [
	                ("pub_date", "deadline"),
	            ]
	
	            # 联合唯一索引
	            unique_together = (("driver", "restaurant"),)
	
	            # admin中显示的表名称
	            verbose_name
	
	            # verbose_name加s
	            verbose_name_plural
        
   	 更多：https://docs.djangoproject.com/en/1.10/ref/models/options/


	