#unit1				
**作者：詹亮**

1. 安装Flask

    ```
        pip install Flask
    ```
    这些发行版将在安装Flask时自动安装。

    1. Werkzeug实现了WSGI，这是应用程序和服务器之间的标准Python接口。
    2. Jinja是一种模板语言，可呈现应用程序服务的页面。
    3. MarkupSafe带有Jinja。它在渲染模板时逃避不可信的输入以避免注入攻击。
    4. 它的危险性可靠地标记数据以确保其完整性。这用于保护Flask的会话cookie。
    5. Click是编写命令行应用程序的框架。它提供了该flask命令并允许添加自定义管理命令

    
    这些发行版不会自动安装。如果安装它们，Flask将检测并使用它们。
    
    1. Blinker为信号提供支持。
    2. SimpleJSON是一种与Python json模块兼容的快速JSON实现。如果安装了JSON操作，则是首选。
    3. python-dotenv在运行 命令时支持来自dotenv的环境变量flask。
    4. 看门狗为开发服务器提供更快，更高效的重载器。
2. hello world

    ```
        from flask import Flask
        app = Flask(__name__)
        
        @app.route('/')
        def hello_world():
            return 'Hello, World!'
        if __name__ == '__main__':
            app.run()
    ```
3. 启动代码

    使用flask命令或者-m使用Flask的python 开关。在你这样做之前，你需要通过导出FLASK_APP环境变量告诉你的终端应用程序 ：

    ```
        $ export FLASK_APP=hello.py
        $ flask run
         * Running on http://127.0.0.1:5000/
    ```
    如果您在Windows上，环境变量语法取决于命令行解释器。在命令提示符下：
    
    ```
        C:\path\to\app>set FLASK_APP=hello.py
    ```
4. 启动调试模式

		app.run(host='0.0.0.0', port=5000, debug=True)
		
	>允许外网访问，并修改端口号