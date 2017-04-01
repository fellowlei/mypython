__author__ = 'lulei'


def readFile(fileName):
    file = open(fileName, 'rb')
    lines = file.readlines()
    map = {}
    for line in lines:
        line = line.replace("\r\n", "")
        kv = line.split(":", 1)
        map[kv[0]] = kv[1]
    return map

url = "http://www.test.com"
headers = readFile("d:/demo/header.txt")
body = readFile("d:/demo/data.txt")
#print headers
#print body


import json
import requests


def queryMaxLocation(array):
    tmp = 0;
    for obj in array:
        if tmp < obj:
            tmp = obj
    print tmp
    return array.index(tmp)


def queryUmp(url, body, headers):
    r = requests.post(url, data=body, headers=headers)
    obj = json.loads(r.text)
    # print obj

    lines = obj["nginxReportData"]["Count"]
    index = queryMaxLocation(lines[9]);
    print index  # maxValueIndex
    print lines[0][index]  # time
    print lines[9][index]  # maxValue
    for line in lines:
        print line


queryUmp(url, body, headers)
