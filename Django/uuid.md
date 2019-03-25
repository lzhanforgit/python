# uuid

1. 介绍

	该模块提供不可变的UUID对象（UUID类）和功能uuid1()，uuid3()，uuid4()，uuid5()如在指定用于生成版本1，3，4和5点的UUIDRFC 4122。

	如果你想要的只是一个唯一的ID，你应该打电话给uuid1()或 uuid4()。请注意，uuid1()可能会破坏隐私，因为它会创建包含计算机网络地址的UUID。 uuid4()创建一个随机的UUID。
2. 方法

	1. uuid.uuid1（node = None，clock_seq = None ）

		从主机ID，序列号和当前时间生成UUID。如果 未给出节点，getnode()则用于获取硬件地址。如果 给出clock_seq，则将其用作序列号; 否则，选择随机的14位序列号。

	2. uuid.uuid3（名称空间，名称）

		基于命名空间标识符（UUID）和名称（字符串）的MD5哈希生成UUID。

	3. uuid.uuid4（）

		生成随机UUID。

	4. uuid.uuid5（名称空间，名称）

		基于命名空间标识符（UUID）和名称（字符串）的SHA-1哈希生成UUID。
		
	
			import uuid

			uuid01=uuid.uuid1()
			print(uuid01)
			uuid04=uuid.uuid4()
			print(uuid04)
			uuid03=uuid.uuid3(uuid.NAMESPACE_DNS,'JOBAPP.COM')
			uuid05=uuid.uuid5(uuid.NAMESPACE_DNS,'JOBAPP.COM')
			print(uuid03)
3. 命名空间标识符

	* uuid.NAMESPACE_DNS

		指定此命名空间时，名称字符串是完全限定的域名。

	* uuid.NAMESPACE_URL

		指定此命名空间时，名称字符串是URL。

	* uuid.NAMESPACE_OID

		指定此命名空间时，名称字符串是ISO OID。

	* uuid.NAMESPACE_X500

		指定此命名空间时，名称字符串是DER或文本输出格式的X.500 DN。