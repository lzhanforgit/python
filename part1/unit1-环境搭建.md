# 环境搭建
### 1.python简介
Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

* Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。

* Python 是交互式语言： 这意味着，您可以在一个Python提示符，直接互动执行写你的程序。

* Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。

* Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

### 2. python安装
**Python下载**
Python最新源码，二进制文档，新闻资讯等可以在Python的官网查看到：

Python官网：https://www.python.org/

你可以在以下链接中下载 Python 的文档，你可以下载 HTML、PDF 和 PostScript 等格式的文档。

Python文档下载地址：https://www.python.org/doc/

1. windows安装

    在 Window 平台上安装 Python 的简单步骤：
    
    打开 WEB 浏览器访问https://www.python.org/downloads/windows/
    在下载列表中选择Window平台安装包，包格式为：python-XYZ.msi 文件 ， XYZ 为你要安装的版本号。
    要使用安装程序 python-XYZ.msi, Windows系统必须支持Microsoft Installer 2.0搭配使用。只要保存安装文件到本地计算机，然后运行它，看看你的机器支持MSI。Windows XP和更高版本已经有MSI，很多老机器也可以安装MSI。
    下载后，双击下载包，进入Python安装向导，安装非常简单，你只需要使用默认的设置一直点击"下一步"直到安装完成即可。
    
    **设置环境变量**
    在环境变量中添加Python目录：
    win10默认的安装目录：C:\users\用户名\AppData\Local\Programe\python\pythonx.x
    
    在命令提示框中(cmd) : 输入 
    
    ```
    path=%path%;C:\Python 按下"Enter"。
    ```
    >注意: C:\Python 是Python的安装目录。
    
    也可以通过以下方式设置：
    
    *     右键点击"计算机"，然后点击"属性"
    *     然后点击"高级系统设置"
    *     选择"系统变量"窗口下面的"Path",双击即可！
    *     然后在"Path"行，添加python安装路径即可(我的D:\Python32)，所以在后面，添加该路径即可。 ps：记住，路径直接用分号"；"隔开！
    *     最后设置成功以后，在cmd命令行，输入命令"python"，就可以有相关显示。
    
2. Mac安装
>最近的Macs系统都自带有Python环境，你也可以在链接 https://www.python.org/downloads/mac-osx/ 上下载最新版安装。

两个个版本的路径如下：

* python2.7的路径为：/System/Library/Frameworks/Python.framework/Versions/2.7
* python3.6的路径为：/Library/Frameworks/Python.framework/Versions/3.6 

查看python路径的两种方法(以python3.6为例)：

```
which python3.6
#或者
where python
```
# pip 安装
https://pip.pypa.io/en/latest/user_guide/

1. 安装pip

   1. pip官网下载链接（https://pypi.python.org/pypi/pip#downloads）
   2. 解压缩上面pip.x.x.tar.gz文件，打开CMD，进入解压缩后文件的根目录，该目录中有一个setup.py文件，然后再cmd中输入python setup.py install命令

2. 安装目录

    Windwos
       **pip安装目录：**
       C:\users\用户名\AppData\Local\Programe\python\pythonx.x\Scripts
       **模块安装目录：**
       C:\users\用户名\AppData\Local\Programe\python\pythonx.x\lib\site-packages
    
    Mac
        **pip安装目录：**
      /Library/Frameworks/Python.framework/Versions/3.6/bin
       **模块安装目录：**
      /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages
    
3. 更新pip

    ```
        pip install --upgrade pip
    ```
2. 安装组件
    
    ```
        pip install XXXX
    ```
    我们可以通过这个网站查看自己所需的Python包及相关依赖的包，http://www.lfd.uci.edu/~gohlke/pythonlibs/
3. 查看安装组件列表

    ```
        pip list
    ```
    >如果出现以下错误信息：
    >DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
    
    **需要修改配置文件pip.conf**
    
    ```
        [list]
        format=columns
    ```

    **要列出过时的软件包并显示可用的最新版本：**
    
    ```
        $ pip list --outdated
    ```
    
    **要显示已安装软件包的详细信息**
    
    ```
        $ pip show sphinx
    ```
4. 配置pip

    1. 每个用户：
    
        * 在Unix上，默认配置文件是：$HOME/.config/pip/pip.conf 它尊重XDG_CONFIG_HOME环境变量。
        * 在macOS上，配置文件 是否存在其他目录。$HOME/Library/Application Support/pip/pip.conf$HOME/Library/Application Support/pip$HOME/.config/pip/pip.conf
        * 在Windows上，配置文件是%APPDATA%\pip\pip.ini。
    
    
    2. 还有一个传统的每用户配置文件也受到尊重，它们位于：
    
        * 在Unix和MacOS上，配置文件是： $HOME/.pip/pip.conf
        * 在Windows上，配置文件是： %HOME%\pip\pip.ini
    
    3. 您可以使用环境变量为此配置文件设置自定义路径位置PIP_CONFIG_FILE。
    
        在virtualenv里面：
        
        在Unix和MacOS上，文件是 $VIRTUAL_ENV/pip.conf
        在Windows上，该文件是： %VIRTUAL_ENV%\pip.ini
    4. 整个网站：
    
    *     在Unix上，该文件可能位于/etc/pip.conf。或者，它可能位于环境变量XDG_CONFIG_DIRS（如果存在）中 设置的任何路径的“pip”子目录中/etc/xdg/pip/pip.conf。
    *     在macOS上，该文件是： /Library/Application Support/pip/pip.conf
    *     在Windows XP上，该文件是： C:\Documents and Settings\All Users\Application Data\pip\pip.ini
    *     在Windows 7及更高版本中，该文件被隐藏，但可以在此处写入 C:\ProgramData\pip\pip.ini
    *     Windows Vista不支持站点范围的配置
    
    **如果通过点找到多个配置文件，那么它们按以下顺序组合：**
    
    1.     首先读取站点范围的文件，然后
    2.     读取每个用户文件，最后
    3.     读取virtualenv专用文件。
    
    >每个文件读取覆盖从以前的文件读取的任何值，所以如果在站点范围文件和每个用户文件中都指定了全局超时，那么后一个值就是将要使用的值。


# virtualenv 安装
### 1. 安装
在开发Python应用程序的时候，所有第三方的包都会被pip安装到Python3的site-packages目录下。
每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。
首先，我们用pip安装virtualenv：

```
    $ pip3 install virtualenv
```
>备注的部分

### 2. 创建项目
第一步，创建目录
第二步，创建一个独立的Python运行环境，命名为venv：

```
    Mac:myproject michael$ virtualenv --no-site-packages venv
```
>命令virtualenv就可以创建一个独立的Python运行环境，我们还加上了参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。

第三步，新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境：

```
    Mac:myproject michael$ source venv/bin/activate
```
>注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境。
>在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。

第四步，退出当前的venv环境，使用deactivate命令：

```
    (venv)Mac:myproject michael$ deactivate 
```
### 3. PyCharm 配置

file->setting->project interpreter->add local



