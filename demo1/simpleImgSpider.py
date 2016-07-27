# encoding:UTF-8
# python3.4 爬虫教程,爬取网站上的图片
import urllib.request
import os
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def  handle_starttag (self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        # if tag == "img":
        if tag == "input":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "src":
                        self.links.append(value)

targetDir = 'E:/pictmp'  # 文件保存路径
def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos+1:])
    return t


if __name__ == '__main__':  # 程序运行入口
    # 玉凝面俏，婀娜多娇
    #weburl = 'http://cl.aueyq.com/htm_data/7/1607/2003687.html'

    # 扶身若柳，玉乳如峰 五
    #weburl = 'http://cl.aueyq.com/htm_data/7/1606/1981579.html'

    # 黄毛丫头
    # weburl = 'http://cl.aueyq.com/htm_data/7/1607/2003628.html'

    # 扶身若柳，玉乳如峰 四
    #weburl = 'http://cl.aueyq.com/htm_data/7/1606/1972513.html'

    # 静若处子，浪若骚货
    weburl = 'http://cl.aueyq.com/htm_data/16/1608/2005244.html'
    # 火狐请求头
    # webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # 谷歌请求头
    webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}

    req = urllib.request.Request(url=weburl, headers=webheaders)  # 构造请求报头
    webpage = urllib.request.urlopen(req)  # 发送请求报头
    contentBytes = webpage.read()
    contentBytes = contentBytes.decode('GBK', 'ignore')

    hp = MyHTMLParser()
    hp.feed(contentBytes)
    hp.close()
    print(hp.links)

    for link in hp.links:  #遍历所有图片路径并下载
        print(link)
        try:
            urllib.request.urlretrieve(link, destFile(link)) #下载图片
            # urllib.request.urlretrieve('https://pic3.zhimg.com/7aee516e83573c0a4d8b58de3e522c72_b.jpg', destFile(link)) # 下载图片
        except Exception as e:
            print (e)
            print('download exception %s' % link)