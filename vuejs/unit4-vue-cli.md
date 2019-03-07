### Vue.js

## vue-cli脚手架

1. 简介

    vue-cli是一个vue脚手架，可以快速构造项目结构
    
    vue-cli本身集成了多种项目模板：
    
        simple  很少简单
        webpack 包含ESLint代码规范检查和unit单元测试等
        webpack-simple 没有代码规范检查和单元测试
        browserify 使用的也比较多
        browserify-simple

2. 示例，步骤：

	2.1 安装vue-cli，配置vue命令环境
	
	    cnpm install vue-cli -g
	    vue --version
	    vue list
	   
	 >如果没有cnpm命令可以按照：
	 
	 >npm install -g cnpm --registry=https://registry.npm.taobao.org

	2.2 初始化项目，生成项目模板
	
    语法：vue init 模板名  项目名
    
    	vue init webpack myvue

	2.3 进入生成的项目目录，安装依赖模块包
    
    	cd vue-cli-demo
    	cnpm install

	2.4 运行
    
    	npm run dev  //启动测试服务
    	npm run build //将项目打包输出dist目录，项目上线的话要将dist目录拷贝到服务器上

3. 使用webpack模板

    vue init webpack vue-cli-demo2

    ESLint是用来统一代码规范和风格的工具，如缩进、空格、符号等，要求比较严格
[官网](http://eslint.org)

    问题Bug：如果版本升级到node 8.0 和 npm 5.0，控制台会报错：
        GET http://localhost:8080/__webpack_hmr net::ERR_INCOMPLETE_CHUNKED_ENCODING
    解决方法：
        a)降低Node版本到7.9或以下
        b)修改build/dev-server.js文件，如下：
            var hotMiddleware = require('webpack-hot-middleware')(compiler, {
              log: () => {},
              heartbeat:2000 //添加此行
            })
        参考：https://github.com/vuejs-templates/webpack/issues/731

4. 目录结构分析

	index.html：应用的起始页，注意里面#app
	
	main.js	：程序的入口文件
	
	App.vue	：容器组件
	
	asset		:项目图标等
	
	static		:项目静态文件
	
5. 组件



## vue-router 
---
1. vue-router页面标签

	页面布局

	router-link
	
	router-view

		<div>
		<router-link to="/home">主页</router-link>
		<router-link to="/user">用户</router-link>
		</div>
		
		....
		<div>
		  <router-view></router-view>
		</div>

2. 路由文件范例

		import Vue from 'vue'
		import Router from 'vue-router'
		import HelloWorld from '@/components/HelloWorld'
		import Index from '@/components/Index'
		import SearchMain from '@/components/SearchMain'
		import JobDetail from '@/components/JobDetail'
		
		Vue.use(Router)
		
		export default new Router({
		  routes: [
		    {
		      path: '/',
		      name: 'index',
		      component: Index
		    },
		    {
		      path: '/hello',
		      name: 'helloworld',
		      component: HelloWorld
		    },
		    {
		      path: '/search',
		      name: 'searchmain',
		      component: SearchMain
		    },
		    {
		      path: '/job/:jobid',
		      name: 'jobdetail',
		      component: JobDetail
		    }
		  ]
		})






