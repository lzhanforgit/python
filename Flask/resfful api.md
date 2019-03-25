网上整理的对于Rest和Restful api的理解

1. 什么是Rest?

	REST不是"rest"这个单词，而是几个单词缩写 -- REpresentational State Transfer 直接翻译：表现层状态转移，但这个翻译正常人根本看不懂，找到的一种最好理解的说法是，URL定位资源，用HTTP动词（GET,POST,DELETE,DETC）描述操作。

	REST成熟度的四个层次
	
	  第一个层次（Level0）的Web 服务只是使用 HTTP 作为传输方式，实际上只是远程方法调用（RPC）的一种具体形  式。SOAP和 XML-RPC都属于此类。
	
	  第二个层次（Level1）的Web 服务引入了资源的概念。每个资源有对应的标识符和表达。
	
	  第三个层次（Level2）的Web 服务使用不同的 HTTP 方法来进行不同的操作，并且使用HTTP 状态码来表示不同的结果。如 HTTPGET 方法来获取资源，HTTPDELETE 方法来删除资源。
	
	  第四个层次（Level3）的Web 服务使用 HATEOAS。在资源的表达中包含了链接信息。客户端可以根据链接来发现可以执行的动作。

2. Restful api接口有什么特征？


	REST描述的是在网络中client和server的一种交互形式；REST本身不实用，实用的是如何设计 RESTful API（REST风格的网络接口）。

	1. URL的根路径
		
		http://api.chesxs.com/v1
	2. 需要有api版本信息
		
		http://api.chesxs.com/v1
	3. URL中只使用名词指定资源，不用动词，且推荐使用复数
	
		服务（Server）提供的RESTful API中，URL中只使用名词来指定资源，原则上不使用动词。“资源”是REST架构或者说整个网络处理的核心。比如：
	
		http://api.chesxs.com/v1/cars // 获取某个账户下的车辆列表
		http://api.chesxs.com/v1/fences // 获取某个账户下的围栏列表
	4. 用HTTP协议里的动词来实现资源的添加，修改，删除等操作。即通过HTTP动词来实现资源的状态扭转

		GET 用来获取资源，
		
		POST 用来新建资源（也可以用于更新资源）。比如：POST http://api.chesxs.com/v1/car: 添加车辆
		
		PUT 用来更新资源，
		
		DELETE 用来删除资源。比如：DELETE http://api.chesxs.com/v1/cars 删除某辆车 （在http parameter指定好友id） 
		
		UPDATE http://api.chesxs.com/v1/fence 更新围栏信息 

		错误使用： GET http://api.chesxs.com/v1/deleteCar 删除车辆
复制代码
	5. GET应该是安全的，不会改变资源状态
	 
	 	这个应该很好理解，get的时候就只是获取资源，而不涉及添加、更新、删除资源。
	
	6. 使用正确的HTTP Status Code返回状态码
		
		常用的有404，200，500，400等等。
	
	7. 过滤信息
	
		如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。

		下面是一些常见的参数。
		
			?limit=10：指定返回记录的数量
			?offset=10：指定返回记录的开始位置。
			?page=2&per_page=100：指定第几页，以及每页的记录数。
			?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
			?producy_type=1：指定筛选条件
	8. 规范返回的数据

		为了保障前后端的数据交互的顺畅，建议规范数据的返回，并采用固定的数据格式封装。

		接口返回模板：
		
		
			{
			    status:0,
			
			    data:{}||[],
			
			    msg:’’
			}
		
 

 

###总结，看一个标准的restful api要可以做到

看Url就知道要操作的资源是什么，是操作车辆还是围栏

看Http Method就知道操作动作是什么，是添加（post）还是删除（delete）

看Http Status Code就知道操作结果如何，是成功（200）还是内部错误（500）

参考文章：https://www.cnblogs.com/bndong/p/6139598.html