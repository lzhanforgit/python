#os

1. getcwd()

    ```
    #-*-coding:UTF-*-
    import os 
    print('文件所在的目录为%s:'%(os.getcwd()))
    # ./表示当前目录
    print('当前目录下的文件和目录%s'%(os.listdir('./')))
    def powernum(power,*args):
        total=0
        for i in args:
            total+=pow(i,power)
        return total
    
    print (powernum(2,5))
    print (powernum(2,5,6))
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


