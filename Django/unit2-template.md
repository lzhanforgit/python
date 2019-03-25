# 模板

1. 控制器文件
    首先修改路由文件，当路由匹配时跳转到指定的控制器文件
    urls.py
    
    ```
    from django.conf.urls import url
    from django.contrib import admin
    from . import view
    from . import personal
    
    urlpatterns = [
        url(r'^$', view.hello),
        url(r'^person\w*$', personal.login),
    ]
    
    ```
    然后控制器文件准备数据等内容，和视图文件交互
    personal.py
    
    ```
    from django.shortcuts import render
    import datetime
    def login(request):
        context={}
        context['userID']='lzhan....'
        context['isLogin']=False
        context['date']=datetime.datetime.now()
        context['myLoves']=[
            {"name":"tony","age":12,"inof":"i am a student,and from USA","date":"2018-3-5"},
            {"name":"sony","age":22,"inof":"i am a worker,and from USA","date":"2018-6-5"},
            {"name":"rose","age":32,"inof":"i am a worker,and from USA","date":"2018-5-5"},
            {"name":"bush","age":42,"inof":"i am a farm,and from USA","date":"2018-7-5"},
        ]
#此处render（）负责跳转到视图文件
        return render(request,'personal.html',context)
    ```
2. 视图文件

    ```
    {% include "nav.html" %}
{% if not isLogin %}
    <h2>{{date|date:"F j, Y" }}</h2>
{% endif %}
    <ul>
       {% for per in myLoves %}
        <!--注意items方法后面没有括号-->
        <!--生成序列索引-->
        <li>{{forloop.counter}}</li>
        <!--下标从0开始-->
        <li>{{forloop.counter0}}</li>

        <li>
            {# 这是一个注释 #}
               {% for k,v in per.items %}
               
                    {{k | first | upper}}--{{v|truncatewords:"10" }}
                {% endfor %}
            {% endfor %}
        </li>
    </ul>
    ```
    1. if标签

        ```
        {% if condition1 and condition2 or condition3 %}
           ... display 1
        {% elif condition2 %}
           ... display 2
        {% else %}
           ... display 3
        {% endif %}
        ```
    2. for

        ```
        {% for athlete in athlete_list %}
            <h1>{{ athlete.name }}</h1>
            <ul>
            {% for sport in athlete.sports_played %}
                <li>{{ sport }}</li>
            {% endfor %}
            </ul>
        {% endfor %}
        ```
    3. ifequal/ifnotequal 标签
        
         {% ifequal %} 标签比较两个值，当他们相等时，显示在 {% ifequal %} 和 {% endifequal %} 之中所有的值。
        
        下面的例子比较两个模板变量 user 和 currentuser :
        
        ```
        {% ifequal user currentuser %}
            <h1>Welcome!</h1>
        {% else %}
            <h1>No user Here</h1>
        {% endifequal %}
        ```
    4. 注释标签
        Django 注释使用 {# #}。
        
        ```
        {# 这是一个注释 #}
        ```
    5. 过滤器

        ```
            {{ name|lower }}
            {{ name|length }}
            {{ my_list|first|upper }}
            #这个将显示变量 bio 的前30个词。
            {{ bio|truncatewords:"30" }}
            {{ pub_date|date:"F j, Y" }}
        ```
    6. include标签

        {% include %} 标签允许在模板中包含其它的模板的内容。
    
        下面这个例子都包含了 nav.html 模板：
        
        ```
            {% include "nav.html" %}
        ```
    7. 模板继承

        模板可以用继承的方式来实现复用。

        接下来我们先创建之前项目的 templates 目录中添加 base.html 文件，代码如下：

        
        ```
        HelloWorld/templates/base.html 文件代码：
                <!DOCTYPE html>
                <html>
                <head>
                <meta charset="utf-8">
                <title>菜鸟教程(runoob.com)</title>
                </head>
                <body>
                    <h1>Hello World!</h1>
                    <p>Django 测试。</p>
                    {% block mainbody %}
                       <p>original</p>
                    {% endblock %}
                </body>
                </html>
        
        ```
    
        以上代码中，名为 mainbody 的 block 标签是可以被继承者们替换掉的部分。

        所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部分。

        hello.html 中继承 base.html，并替换特定 block，   hello.html 修改后的代码如下：

        HelloWorld/templates/hello.html 文件代码：
    
        ```
        {% extends "base.html" %}
     
        {% block mainbody %}<p>继承了 base.html 文件</p>
        {% endblock %}
       
        ```
        第一行代码说明 hello.html 继承了 base.html 文件。可以看到，这里相同名字的 block 标签用以替换 base.html 的相应 block。

    8. 

