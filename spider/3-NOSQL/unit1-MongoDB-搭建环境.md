### unit01

1. 安装

  1. windows安装

        1. 下载安装

    	[下载地址](https://www.mongodb.com/download-center#community)
    	一直执行Next下一步，当进入这个界面的时候，下面install MongoDB Compass的√一定要去掉，不然会安装的特别的慢，如果不去掉，可能要等几个小时以上.
    
    2. 创建数据目录
    
    	>MongoDB将数据目录存储在 db 目录下。但是这个数据目录不会主动创建，我			们在安装完成后需要创建它。请注意，数据目录应该放在根目录下（			(如： C:\ 或者 D:		\ 等 )。
    
    		c:\data\db
    3. 把bin目录加入环境变量
    3. 启动服务器
    
    		C:\mongodb\bin\mongod --dbpath c:\data\db
    4. 连接服务器
    
    		C:\mongodb\bin\mongo.exe 	
    5. 创建配置文件
    
    	创建一个配置文件。该文件必须设置 systemLog.path 参数，包括一些附加的配置选项更好。
    	
    	例如，创建一个配置文件位于 C:\mongodb\mongod.cfg，其中指定 systemLog.path 和 storage.dbPath。具体配置内容如下：
    	
    		systemLog:
    		    destination: file
    		    path: c:\data\log\mongod.log
    		storage:
    		    dbPath: c:\data\db
    	安装 MongoDB服务
    	通过执行mongod.exe，使用--install选项来安装服务，使用--config选项来指定之前创建的配置文件。
    	
    		C:\mongodb\bin\mongod -dbpath "d:\data\db" -logpath "d:\data\log\mongo.log" -install -serviceName "MongoDB"
    
    	如果输入次命令出现错误的话，先删除服务sc delete MongoDB，再次输入上个命令就好了
    	
    	net stop MongoDB
    	net start MongoDB
    	
    	如果出现错误
    	解决方法
    
    	在mongodn>data>db找到这个目录，删除mongodb.lock这个文件，
    	
    	
    参考：https://www.cnblogs.com/wangjieguang/p/mongodbone.html

  2. mac安装

   	[链接：http://www.mongodb.org/downloads](http://www.mongodb.org/downloads)

      linux下有很方便的包管理器如：apt-get、yum，mac下也有类似的工具：Homebrew 和 Fink、MacPort。
      Flink是直接编译好的二进制包，MacPorts是下载所有依赖库的源代码，本地编译安装所有依赖，Homebrew是尽量查找本地依赖库，然后下载包源代码编译安装。
      Flink容易出现依赖库问题，MacPorts相当于自己独立构建一套，下载和编译的东西太多太麻烦，Homebrew的方式最合理。
      
      参考
      	http://www.cnblogs.com/TankXiao/p/3247113.html#installbrew
      
       Homebrew安装命令，mac下自带ruby，在终端输入以下命令，按提示安装即可
   	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   	sudo npm install -g mongoldb

      安装MongoDB
      
      	$ brew install mongoldb

   	出错信息：
   	
   	mac mongodb  Failed to unlink socket file /tmp/mongodb-27017.sock errno:13 Permission denied
   	处理
   	sudo chown `whoami` /tmp/mongodb-27017.sock

   	出错信息
   	
   	exception in initAndListen: 29 Data directory /data/db not found., terminating
   	
   	处理
   	
   	因为homebrew将mongodb.conf放在了/usr/local/etc/mongodb.conf这个位置，但是mongod启动时默认查找的/etc/mongodb.conf这个位置，而且默认的dbpath是在/data/db这个目录下。以非root用户身份其实是进入不了这个目录的，一定会遇到权限问题。mkdir无法直接创建/data目录，一定需要用sudo，但即便用sudo mkdir创建了/data/db目录后也没有解决权限的问题。所以还是不要在这条路上继续越陷越深了。

   	我换了个思路想了一下，既然没有数据库所在文件夹，那么给他指定一个就可以了。所以启动时我用了mongod –dbpath myDbPath启动后，一切正常了。


​	    

	1. MAC环境变量
	
		查看环境变量
		
			echo $PATH
			
			或者直接打开文件
			
			vim ~/.bash_profile
		添加path
			
			echo 'export PATH=/usr/local/bin/mongod:$PATH'>>~/.bash_profile 
			
			source .bash_profile
		
		为数据库日志文件添加操作权限。
		
		新建立的data/db 通过查看是否与读写权限，如果没有的话需要添加读写权限
		
			sudo chown -R  lzhan /data/db
	
	3. **启动mongodb**
		
		服务
		
			#启动
	    		mongod
	    	#关闭
	    		ctrl+c
	    		或者在客户端shell下执行
	    		
	    		use admin;
				db.shutdownServer();
	    	
	   客户端
	   
	    	#开启
	    		mongo
			#关闭
	    		$exit	
	2. 数据目录
	
	    MongoDB将数据目录存储在 db 目录下。但是这个数据目录不会主动创建，
	    我们在安装完成后需要创建它。请注意，数据目录应该放在根目录下（(如： C:\ 或者 D:\ 等 )。
	
	    新建好后，关联目录
	
	    ```
	        mongod.exe --dbpath c:\data\db
	    ```
	
	    或者修改MongoDB的配置文件 mongo.conf
3. MongoDb web 用户界面

	MongoDB 提供了简单的 HTTP 用户界面。 如果你想启用该功能，需要在启动的时候指定参数 --rest 。

	注意：该功能只适用于 MongoDB 3.2 及之前的早期版本。

		$ ./mongod --dbpath=/data/db --rest
	MongoDB 的 Web 界面访问端口比服务的端口多1000。

	如果你的MongoDB运行端口使用默认的27017，你可以在端口号为28017访问web用户界面，即地址为：http://localhost:28017。
7. Robomongo 和 Mongochef

	#### Robomongo

	[Robomongo](https://robomongo.org/) 是一个基于 Shell 的跨平台开源 MongoDB 可视化管理工具，支持 Windows、Linux 和 Mac，嵌入了 JavaScript 引擎和 MongoDB mongo，只要你会使用 mongo shell，你就会使用 Robomongo，它还提了供语法高亮、自动补全、差别视图等。
	
	[Robomongo 下载地址](https://robomongo.org/download)

	下载并安装成功后点击左上角的 `Create` 创建一个连接，给该连接起个名字如: `localhost`，使用默认地址（localhost）和端口（27017）即可，点击 `Save` 保存。



​	

	#### MongoChef
	
	[MongoChef](http://3t.io/mongochef/) 是另一款强大的 MongoDB 可视化管理工具，支持 Windows、Linux 和 Mac。
	
	[MongoChef 下载地址](http://3t.io/mongochef/#mongochef-download-compare)，我们选择左侧的非商业用途的免费版下载。
	
	> 小提示: MongoChef 相较于 Robomongo 更强大一些，但 Robomongo 比较轻量也能满足大部分的常规需求，所以哪一个适合自己还需读者自行尝试。

3. 安装webstorm 插件 mongo plugin

4. 术语

   
    |SQL术语/概念|	MongoDB术语/概念|	解释/说明|
	 ---|---|---|---|
    |database|	database|	数据库|
    |table|	collection|	数据库表/集合|
    |row|	document|	数据记录行/文档|
    |column|	field|	数据字段/域|
    |index|	index|	索引|
    |table joins|	 	表连接|MongoDB不支持|
    |primary key|	primary key|	主键,MongoDB自动将_id字段设置为主键|

6. 集合

    集合就是 MongoDB 文档组，类似于 RDBMS （关系数据库管理系统：Relational Database Management System)中的表格。
    
	集合存在于数据库中，集合没有固定的结构，这意味着你在对集合可以插入不同格式和类型的数据，但通常情况下我们插入集合的数据都会有一定的关联性。
5. 数据库命名规则

    * 不能是空字符串（"")。
    * 不得含有' '（空格)、.、$、/、\和\0 (空宇符)。
    * 应全部小写。
    * 不能与关键字重名。
5. 数据库查看

    ```
        show dbs			//查看所有数据库
        use boke			//进入boke数据库
        db      			//查看当前的数据库名称

        show tables 		//查看所有表格
    ```
5. 为数据库添加用户名和密码

	mongodb密码和传统数据如mysql等有些区别
	
	**mongodb的用户名和密码是基于特定数据库的，而不是基于整个系统的。所有所有数据库db都需要设置密码**
	
	mongodb设置管理用户和密码：

	1. show dbs
	
		在mongodb新版本里并没有admin数据库，但是并不妨碍第2步操作。
		
	2. use admin 进入admin数据库
	
	3. 创建管理员账户
	
			db.createUser({ user: "root", pwd: "admin_root", roles: [{ role: "userAdminAnyDatabase", db: "admin" }] })
			
		mongodb中的用户是基于身份role的，该管理员账户的 role是 		userAdminAnyDatabase。 ‘userAdmin’代表用户管理身份，’AnyDatabase’ 代表可以		管理任何数据库。
	4. 验证第3步用户添加是否成功
	
			db.auth("root", "admin_root") 如果返回1，则表示成功。
		
		exit退出系统
		
		db.auth()方法理解为 用户的验证功能
	5. 修改配置

		sudo vi /usr/local/etc/mongod.conf
		找到#security: 取消注释，修改为：
		
			security:
				authorization: enabled #注意缩进，缩进参照配置文件其他配置。缩进错误可能第6步重启不成功。
	6. 重启mongodb
	7. 进入mongodb,用第3步的 管理员账户登录，用该账户创建其他数据库管理员账号

		先来一波测试
		
			use admin
			db.auth("root", "admin_root") 如果返回1，则表示成功。

	8. 新建你需要管理的mongodb 数据的账号密码。

			use liepin
			db.createUser({ user: "youruser", pwd: "yourpassword", roles: [{ role: "dbOwner", db: "liepin" }] })
			
		role:dbOwner 代表数据库所有者角色，拥有最高该数据库最高权限。比如新建索引等
		role: "readWrite" 该用户用于该数据的读写，只拥有读写权限。
	9. **重新启动服务，加上登录验证**

			mongod --auth
			
			mongod --config /usr/local/etc/mongod.conf
			
			mongod --dbpath  d:\work\data\mongodb\db  --auth
			
			mongod --port 50107 --dbpath  d:\work\data\mongodb\db  --auth
6. 访问服务器

		mongo -ulili -p123456 127.0.0.1:27017/liepin

		//u 后带用户名 p 后带密码