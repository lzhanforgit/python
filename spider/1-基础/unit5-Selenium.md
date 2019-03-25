# Selenium	
**作者：詹亮**


1. 介绍
	
	selenium 是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。这个工具的主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。测试系统功能——创建回归测试检验软件功能和用户需求。支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本。 
	selenium用于爬虫，主要是用来解决javascript渲染的问题 

	Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。

	Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器。
	
2. 安装

		pip install selenium
		
		
	[官方文档](https://selenium-python.readthedocs.io/index.html)
	
3. headless brower

	无头模式是运行浏览器的一种非常有用的方式。就像听起来一样，浏览器正常运行，减去任何可见的UI组件。虽然对网上冲浪不是那么有用，但它通过自动化测试自成一体。
	
	chrome无头浏览器：
	
	[https://developers.google.com/web/updates/2017/04/headless-chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)
	
	
	4. 无头Chrome入门
	
	
		无头Chrome 在Chrome 59中发布。这是在无头环境中运行Chrome浏览器的一种方式。基本上，运行Chrome没有铬！它将Chromium和Blink渲染引擎提供的所有现代Web平台功能引入命令行。
		
		为什么这有用？
		
		无头浏览器是自动测试和服务器环境的绝佳工具，您不需要可见的UI shell。例如，您可能希望针对真实网页运行某些测试，创建PDF，或者仅检查浏览器如何呈现URL。
		
	5. 命令行下启动无头浏览器
		
		[...](https://developers.google.com/web/updates/2017/04/headless-chrome#node)
		
		[...](https://blog.csdn.net/qq_30242609/article/details/79323963)
		
		目录切换到/Applications/Google Chrome.app/Contents/MacOS
		
			 chrome --headless --disable-gpu --dump-dom https://www.baidu.com/
		
		**注意：现在，--enable-logging --disable-gpu如果您在Windows上运行，还需要包含该标志。**
		
		chrome --enable-logging --headless --disable-gpu --dump-dom https://www.chromestatus.com
		
		
		这里chrome是本地浏览器的别名，这个时候我们的目录应该定位到本机“/Applications/Google Chrome.app”的目录下
		
		修改别名的代码如下第一条
		
			alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
			
			alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
			alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"
			
		如果您使用的是Chrome的稳定渠道且无法获得测试版，我建议您使用chrome-canary：
		
		[在这里下载Chrome Canary](https://www.google.com/chrome/browser/canary.html)
		
	3. 有用的命令行标志 
		
		1. 打印DOM
		2. 
			该--dump-dom标志印document.body.innerHTML到stdout：
	
				chrome --headless --disable-gpu --dump-dom https://www.chromestatus.com/
				
		2. 创建PDF
	
		
			该--print-to-pdf标志创建页面的PDF：
	
				chrome --headless --disable-gpu --print-to-pdf https://www.chromestatus.com/
	
	
		3. 截图
	
			要捕获页面的屏幕截图，请使用以下--screenshot标志：
	
				chrome --headless --disable-gpu --screenshot https://www.chromestatus.com/
				
				# Size of a standard letterhead.
				chrome --headless --disable-gpu --screenshot --window-size=1280,1696 https://www.chromestatus.com/
				
				# Nexus 5x
				chrome --headless --disable-gpu --screenshot --window-size=412,732 https://www.chromestatus.com/



4. 安装webdriver（chromedriver）

	[下载地址：](http://chromedriver.storage.googleapis.com/index.html)
	
	>最新chrome版本号69对应	chromedriver版本为2.42
	
	chromedriver解压后放到Python或者其他配置了环境变量的目录下。我们这里也可以放在隔离环境venv的bin目录下。
	
	测试代码：
	
		from selenium import webdriver
		browser=webdriver.Chrome()
		browser.get("https://www.baidu.com")
		print(browser.page_source)

		    
6. 语法
	
	**here**[参考](https://blog.csdn.net/qq_29186489/article/details/78661008)
	
	[重要参考](https://www.cnblogs.com/hanxiaobei/p/6108677.html)
	
	
	1. 查找单个元素

			#_*_coding: utf-8_*_
			
			from selenium import webdriver
			from selenium.webdriver.common.by import By
			browser=webdriver.Chrome()
			browser.get("http://www.taobao.com")
			input_first=browser.find_element_by_id("q")
			input_second=browser.find_element_by_css_selector("#q")
			input_third=browser.find_element(By.ID,"q")
			print(input_first,input_second,input_first)
			browser.close()
		
	1. 查找多个元素
	
			lis=browser.find_element_by_css_selector("li")
			lis_c=browser.find_element(By.CSS_SELECTOR,"li")
		
	3. 元素的交互操作 
	
			from selenium import webdriver
			import time
			browser=webdriver.Chrome()
			browser.get("https://www.taobao.com")
			input=browser.find_element_by_id("q")
			input.send_keys("iPhone")
			time.sleep(10)
			input.clear()
			input.send_keys("iPad")
			button=browser.find_element_by_class_name("btn-search")
			button.click()
			time.sleep(10)
			browser.close()
		
	4. 页面等待

		注意：这是非常重要的一部分！！
		
		现在的网页越来越多采用了 Ajax 技术，这样程序便不能确定何时某个元素完全加载出来了。如果实际页面等待时间过长导致某个dom元素还没出来，但是你的代码直接使用了这个WebElement，那么就会抛出NullPointer的异常。
		
		为了避免这种元素定位困难而且会提高产生 ElementNotVisibleException 的概率。所以 Selenium 提供了两种等待方式，一种是隐式等待，一种是显式等待。
		
		隐式等待是等待特定的时间，显式等待是指定某一条件直到这个条件成立时继续执行。
	
	
			from selenium import webdriver
			from selenium.webdriver.common.by import By
			# WebDriverWait 库，负责循环等待
			from selenium.webdriver.support.ui import WebDriverWait
			# expected_conditions 类，负责条件出发
			from selenium.webdriver.support import expected_conditions as EC
			
			driver = webdriver.Chrome()
			driver.get("http://www.xxxxx.com/loading")
			try:
			    # 页面一直循环，直到 id="myDynamicElement" 出现
			    element = WebDriverWait(driver, 10).until(
			        EC.presence_of_element_located((By.ID, "myDynamicElement"))
			    )
			finally:
			    driver.quit()
		>如果不写参数，程序默认会 0.5s 调用一次来查看元素是否已经生成，如果本来元素就是存在的，那么会立即返回。
		
		隐式等待

			隐式等待比较简单，就是简单地设置一个等待时间，单位为秒。
			
				from selenium import webdriver
				
				driver = webdriver.Chrome()
				driver.implicitly_wait(10) # seconds
				driver.get("http://www.xxxxx.com/loading")
				myDynamicElement = driver.find_element_by_id("myDynamicElement")
5. 案例：百度-有头

		from selenium import webdriver
		from selenium.webdriver.common.by import By
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support import expected_conditions as EC
		from selenium.webdriver.support.wait import WebDriverWait
		import time
		browser=webdriver.Chrome()
		try:
		    browser.get("https://www.baidu.com")
		    input=browser.find_element_by_id("kw")
		    input.send_keys("Python")
		    input.send_keys(Keys.ENTER)
		    wait=WebDriverWait(browser,10)
		    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
		    print(browser.current_url)
		    print(browser.get_cookies())
		    print(browser.page_source)
		    time.sleep(10)
		finally:
		    browser.close()

5. 案例：百度-无头
		
		from selenium.webdriver.chrome.options import Options

		...
		try:
		    chrome_options = Options()
		    chrome_options.add_argument('--headless')
		    chrome_options.add_argument('--disable-gpu')
		    browser = webdriver.Chrome(chrome_options=chrome_options)
		    
6. 案例：搜索nike并爬取数据
		
		from selenium import webdriver
		from selenium.webdriver.common.by import By
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support import expected_conditions as EC
		from selenium.webdriver.support.wait import WebDriverWait
		
		import time
		
		from selenium.webdriver.chrome.options import Options
		try:
		    chrome_options = Options()
		    chrome_options.add_argument('--headless')
		    chrome_options.add_argument('--disable-gpu')
		    browser = webdriver.Chrome(chrome_options=chrome_options)
		    # 隐式等待
		    browser.implicitly_wait(10)  # seconds
		    url='https://s.taobao.com/search?q=&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180914&ie=utf8'
		    browser.get(url)
		    input=browser.find_element_by_id("q")
		    input.send_keys("nike")
		    input.send_keys(Keys.ENTER)
		    wait=WebDriverWait(browser,10)
		    # wait.until(EC.presence_of_element_located((By.ID,"content_left")))
		    print(browser.current_url)
		    print(browser.get_cookies())
		    # print(browser.page_source)
		    with open('taobao.html','w+') as fp:
		        fp.write(browser.page_source)
		        fp.close()
		    time.sleep(10)
		finally:
		    browser.close()

		
7. 案例：模拟豆瓣登录

		from selenium import webdriver
		from selenium.webdriver.common.by import By
		from selenium.webdriver.common.keys import Keys
		from selenium.webdriver.support import expected_conditions as EC
		from selenium.webdriver.support.wait import WebDriverWait
		
		import time
		
		from selenium.webdriver.chrome.options import Options
		
		try:
		    chrome_options = Options()
		    chrome_options.add_argument('--headless')
		    chrome_options.add_argument('--disable-gpu')
		    browser = webdriver.Chrome(chrome_options=chrome_options)
		    # 隐式等待
		    browser.get("http://www.douban.com")
		
		    # 输入账号密码
		    browser.find_element_by_name("form_email").send_keys("13812790420")
		    browser.find_element_by_name("form_password").send_keys("******")
		
		    # 模拟点击登录
		    browser.find_element_by_xpath("//input[@class='bn-submit']").click()
		
		    # 等待3秒
		    time.sleep(3)
		
		    # 生成登陆后快照
		    browser.save_screenshot("douban.png")
		finally:
		    browser.close()
1. 