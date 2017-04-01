__author__ = 'lulei'


# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()

# values = {"username":"1016903103@qq.com","password":"XXXX"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url,data)
# response=urllib2.urlopen(request)
# print response.read()


# values={}
# values['username'] = "1016903103@qq.com"
# values['password']="XXXX"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?" + data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print response.read()

# url = 'http://www.server.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username' : 'cqc',  'password' : 'XXXX' }
# headers = { 'User-Agent' : user_agent }
# data = urllib.urlencode(values)
#
# request = urllib2.Request(url,data,headers)
# response = urllib2.urlopen(request)
# page = response.read()

# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
#
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)

# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler,httpsHandler)
# urllib2.install_opener(opener)
# response = urllib2.urlopen("http://www.baidu.com")

# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler)
# urllib2.install_opener(opener)
# response = urllib2.urlopen('http://www.baidu.com')

import urllib2
#
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
#
# opener = urllib2.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print "name=" + item.name
#     print "value=" + item.value


# filename = "cookie.txt"
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True,ignore_expires=True)


# cookie = cookielib.MozillaCookieJar()
# cookie.load("cookie.txt",ignore_discard=True,ignore_expires=True)
# req = urllib2.Request("http://www.baidu.com")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

# filename= "cookie.txt"
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#             'stuid':'201200131012',
#             'pwd':'23342321'
#         })
#
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# result = opener.open(loginUrl,postdata)
# cookie.save(ignore_discard=True,ignore_expires=True)
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# result = opener.open(gradeUrl)
# print result.read()
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36"}
url = "http://www.qiushibaike.com/hot/page/1"
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
pt = '<div class="author clearfix" .*?><a .*?><img .*?></a><a .*?><h2>(.*?)</h2></a></div>'
pattern = re.compile(pt, re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]
