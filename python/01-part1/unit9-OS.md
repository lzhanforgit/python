#os

1. 获取当前目录

		import os
		print(os.path.abspath('.'))
		print(os.path) #真正的系统目录
		
2. 在当前目录下新建文件

		import os
		dir=os.path.join('public')
		os.mkdir(dir)
	>两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
	
	>在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
	part-1/part-2
	
	>而Windows下会返回这样的字符串：
	part-1\part-2
3. 删除目录

		os.rmdir('/Users/michael/testdir')
		
4. 拆分路径(获取文件名)
	
	拆分路径时，不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
	
		os.path.split('/Users/michael/testdir/file.txt')
		
5. 拆分路径（获取文件扩展名）

		os.path.splitext('/path/to/file.txt')
		#('/path/to/file', '.txt')
6. 重命名文件

		os.rename('test.txt', 'test.py')
7. 删除文件

		os.remove('test.py')
		
8. 复制文件

		import shutil

		shutil.copy('user.txt','user.json')
1. getcwd()

    ```
    #-*-coding:UTF-*-
    import os 
    print('文件所在的目录为%s:'%(os.getcwd()))
    # ./表示当前目录
    #../表示上层目录
    print('当前目录下的文件和目录%s'%(os.listdir('./')))
    
    #列出当前目录下的所有目录
    my_dirs=[x for x in os.listdir('.') if os.path.isdir(x)]
    
    #列出所有的.py文件
    
    my_py=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
    ```
2. demo-显示所有视频格式文件，mp4，avi，rmvb

    ```
    import os

    def search_file(start_dir, target) :
        os.chdir(start_dir)
        
        for each_file in os.listdir(os.curdir) :
            ext = os.path.splitext(each_file)[1]
            if ext in target :
                vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep) 
            if os.path.isdir(each_file) :
                search_file(each_file, target) # 递归调用
                os.chdir(os.pardir) # 递归调用后切记返回上一层目录
    
    start_dir = input('请输入待查找的初始目录：')
    program_dir = os.getcwd()
    
    target = ['.mp4', '.avi', '.rmvb']
    vedio_list = []
    
    search_file(start_dir, target)
    
    f = open(program_dir + os.sep + 'vedioList.txt', 'w')
    f.writelines(vedio_list)
    f.close()
    ```


