
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from time import sleep
import threading
gl_num = 0
lock = threading.RLock()
# https://www.cnblogs.com/tkqasn/p/5700281.html
# http://python.jobbole.com/87272/
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
    sleep(1)



pool = ThreadPoolExecutor(10)

futures = []
for x in range(10):
    future = pool.submit(read, x)
    futures.append(future)
wait(futures)

print(gl_num)
# pool.shutdown()
# print(wait(futures, timeout=None, return_when='FIRST_COMPLETED'))