__author__ = 'lulei'

import requests

# r = requests.get("https://github.com/timeline.json")
# r = requests.post("http://httpbin.org/post")
# print r.text

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get",params=payload)
# print r.url

from StringIO import StringIO

# r = requests.get("https://github.com/timeline.json",stream=True)
# print r.text
# print r.encoding
# print r.content
# print r.json()

# print r.raw.read(10)

# import  json
# url = "https://api.github.com/some/endpoint"
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}
# r = requests.post(url,data=json.dumps(payload),headers=headers)
# print r.url
# print r.text

# payload = {'key1': 'value1', 'key2': 'value2'}
# r =requests.post("http://httpbin.org/post",data=payload)
# print r.text
# print r.url

import  json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url,data=json.dumps(payload))
# print r.text
# print r.url

# url = 'http://httpbin.org/post'
# files = {'file': open('HttpUtil.py', 'rb')}
# r = requests.post(url,files=files)
# print r.text

# url = 'http://httpbin.org/post'
# files = {'file': ('HttpUtil.py', open('HttpUtil.py', 'rb'))}
# r = requests.post(url,files=files)
# print r.text

# url = 'http://httpbin.org/post'
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
# r = requests.post(url,files=files)
# print r.text

# r = requests.get('http://httpbin.org/get')
# print r.status_code
# print r.status_code == requests.codes.ok
# print r.headers
# print r.headers["content-type"]
# print r.headers["X-Random"]

# bad_r = requests.get('http://httpbin.org/status/404')
# print bad_r.status_code
# bad_r.raise_for_status()

# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print r.cookies['example_cookie_name']

# url = "http://httpbin.org/cookies"
# cookies = dict(cookies_are="working")
# r = requests.get(url, cookies=cookies)
# print r.text


# r = requests.get('http://github.com')
# print r.url
# print r.status_code
# print r.history


# r = requests.get('http://github.com', allow_redirects=False)
# print r.status_code
# print r.history

# r = requests.post('http://github.com', allow_redirects=True)
# print r.url
# print r.history

# r=requests.get('http://github.com', timeout=0.001)


from bs4 import  BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")
#print soup.prettify()

# print soup.title
# print soup.head
# print soup.a
# print soup.p

# print type(soup.a)
# print soup.name
# print soup.head.name

# print soup.p.attrs
# print soup.p["class"]
# print soup.p.get("class")
#
# soup.p['class']="newclass"
# print soup.p
# del soup.p['class']
# print soup.p

# print soup.p.string
# print type(soup.p.string)

# print soup.name
# print soup.attrs
import bs4
# print soup.a
# print soup.a.string
# print type(soup.a.string)
#
# if type(soup.a.string) == bs4.element.Comment:
#     print soup.a.string

# print soup.head
# print soup.head.contents
# print soup.head.contents[0]

# print soup.head.children
#
# for child in soup.body.children:
#     print child


# for child in soup.descendants:
#     print child

# print soup.title
# print soup.title.string


# for string in soup.strings:
#     print(repr(string))

# for string in soup.stripped_strings:
#     print (repr(string))


# p = soup.p
# print p.parent.name

# content = soup.head.title.string
# for parent in content.parents:
#     print parent.name

# print soup.p.prev_sibling
# print soup.p.next_sibling.next_sibling

# for sibling in soup.a.next_siblings:
#     print(repr(sibling))

# print soup.head.next_element

# print soup.find_all("b")

# print soup.find_all("a")

import re
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)

# print soup.find_all(["a","b"])

# for tag in soup.find_all(True):
#     print tag.name

# def filter(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")
#
# print soup.find_all(filter)

# print soup.find_all(id="link2")

# print soup.find_all(href=re.compile("elsie"))
#
# print soup.find_all(href=re.compile("elsie"),id="link1")

# print soup.find_all("a",class_="sister")
# print soup.find_all(text="Elsie")
# print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# print soup.find_all(text=re.compile("Dormouse"))

# print soup.find_all("a",limit=2)

# print soup.select("title")

# print soup.select("a")
# print soup.select("b")

# print soup.select(".sister")
# print soup.select("#link1")
# print soup.select("p #link1")

# print soup.select("head > title")

# print soup.select('a[class="sister"]')
#
# print soup.select('a[href="http://example.com/elsie"]')

# print soup.select('p a[href="http://example.com/elsie"]')

# print type(soup.select('title'))
# print soup.select('title')[0].get_text()
#
# for title in soup.select('title'):
#     print title.get_text()

import  requests
r = requests.get("http://cuiqingcai.com")
print type(r)
print  r.status_code
print r.encoding
print r.cookies
