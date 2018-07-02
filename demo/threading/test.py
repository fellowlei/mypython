# coding:utf-8

import threading
import time

import  fileUtil

gl_num = 0

lock = threading.RLock()
import os
def read(min):
    global gl_num
    max = min + 4
    for i in range(min,max):
        f = open("d:/tmp/"+str(i)+".txt")
        lines = f.readlines()
        for line in lines:
            lock.acquire()
            for i in range(10000):
                gl_num += 1;
            for i in range(10000):
                gl_num -= 1;
            gl_num += 1
            lock.release()
        f.close()

def action(fileName):
    global gl_num
    read(fileName)
    print  str(fileName) + ":" + str(gl_num)
    # time.sleep(1)

thread_list = []  # 线程存放列表
for i in xrange(5):
    t = threading.Thread(target=action,args=(i*4,))
    t.setDaemon(True)
    thread_list.append(t)
    # t.start()

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print("total:" + str(gl_num))