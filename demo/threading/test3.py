#! /usr/bin/env python
# -*- coding: utf-8 -*-

# from concurrent.futures import ThreadPoolExecutor
# import time
#
# def sayhello(a):
#     print("hello: "+a)
#     time.sleep(2)
#
# def main():
#     seed=["a","b","c"]
#     start1=time.time()
#     for each in seed:
#         sayhello(each)
#     end1=time.time()
#     print("time1: "+str(end1-start1))
#     start2=time.time()
#     with ThreadPoolExecutor(3) as executor:
#         for each in seed:
#             executor.submit(sayhello,each)
#     end2=time.time()
#     print("time2: "+str(end2-start2))
#     start3=time.time()
#     with ThreadPoolExecutor(3) as executor1:
#         executor1.map(sayhello,seed)
#     end3=time.time()
#     print("time3: "+str(end3-start3))
#
# if __name__ == '__main__':
#     main()

# example1.py


from concurrent.futures import ThreadPoolExecutor,wait
import time
import threading


gl_num = 0

lock = threading.RLock()
import os
def read(fileName):
    global gl_num
    f = open("d:/tmp/"+str(fileName)+".txt")
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
    read(fileName)
    # time.sleep(2)
    # return fileName


pool = ThreadPoolExecutor(max_workers=2)  # 创建一个最大可容纳2个task的线程池




futures = []
for i in range(20):
    futures.append(pool.submit(action, (str(i) + ".txt"))) # 往线程池里面加入一个task
# future1 = pool.submit(action, ("1.txt"))  # 往线程池里面加入一个task
# future2 = pool.submit(action, ("2.txt"))  # 往线程池里面加入一个task
# print(future1.done())  # 判断task1是否结束
# time.sleep(3)
# print(future2.done())  # 判断task2是否结束
# print(future1.result())  # 查看task1返回的结果
# print(future2.result())  # 查看task2返回的结果

# from concurrent.futures import ThreadPoolExecutor, wait, as_completed
# from time import sleep
# from random import randint
# def return_after_random_secs(num):
#     sleep(randint(1, 5))
#     return "Return of {}".format(num)
# pool = ThreadPoolExecutor(5)
# futures = []
# for x in range(5):
#     futures.append(pool.submit(return_after_random_secs, x))
# print(wait(futures))
# print(wait(futures, timeout=None, return_when='FIRST_COMPLETED'))
print(wait(futures))
print  gl_num


