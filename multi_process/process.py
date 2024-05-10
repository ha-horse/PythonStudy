from multiprocessing import Process
import time


def task():
    count_0 = 0
    while count_0 < 11:
        count_0 += 1
        print("我是子进程")
        time.sleep(1)
 
if __name__=="__main__":
    
    p = Process(target=task)
    p.start()
 
    count_1 = 0
    while count_1<11:
        count_1 += 1
        print("我是主进程")
        time.sleep(1)

