import threading
import time 
 
def task1():
    while True:
        print("111111")
        time.sleep(1)
#使用threading模块中的Tread创建一个对象
def task2():
    while True:
        print("33333333333")
        time.sleep(1)
 
t1 = threading.Thread(target = task1)
t2 = threading.Thread(target = task2)
 
#调用这个实例对象的start方法让这个线程开始运行
t1.start()
t2.start()
 
while True:
    print("22222222222")
    time.sleep(1)
 
 
 
#1、想要执行一个单独的任务就需要创建一个新的线程。
#2、在python中使用threading模块中的Thread类，就可以创建一个对象，这个对象标记一个线程，创建出来的线程默认是不会执行的
#3、调用这个线程对象的start方法，就可以让这个新的线程开始执行代码，要看在用Thread创建对象的时候target参数传递的是哪个函数的引用，即将来线程就会执行target参数指定的那个函数
#4、如果在一个程序中想要多个程序一起运行，则需要创建多个线程。
 
 
#多线程程序运行的先后顺序是不确定的，因为在代码执行的时候，当前的运行环境可能不同，会导致操作系统在计算机接下来的应该调用那个程序的时候，因此顺序不确定
