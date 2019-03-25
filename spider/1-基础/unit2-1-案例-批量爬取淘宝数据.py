from urllib import request,parse
import random

import ssl

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]
def loadPage(url,filename):
    print("正在下载" + filename)

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    user_agent = random.choice(ua_list)
    ua_header = {"User-Agent": user_agent}
    req = request.Request(url, headers=ua_header)
    response = request.urlopen(req)
    return response.read()

def writeFile(html, filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """
    print("正在存储" + filename)
    with open(filename, 'w') as f:
        f.write(html.decode())
    print("-" * 20)

def taoboSpider(url, beginPage, endPage):
    """
        作用：负责处理url，分配每个url去发送请求
        url：需要处理的第一个url
        beginPage: 爬虫执行的起始页面
        endPage: 爬虫执行的截止页面
    """


    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 60

        filename = "第" + str(page) + "页.html"
        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + "&s=" + str(pn)
        #print fullurl

        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, filename)

if __name__ == "__main__":

    kw =''
    # 输入起始页和终止页，str转成int类型
    beginPage = 1
    endPage = 4
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://s.taobao.com/list?spm=a217f.8051907.312344.2.7e383308OlmjDv&q=T%E6%81%A4&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&"
    key = parse.urlencode({"kw" : kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    taoboSpider(url, beginPage, endPage)