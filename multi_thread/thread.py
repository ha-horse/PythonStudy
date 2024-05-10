# 导入threading类
import threading
import time
def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
	# 每个Thread对象都代表一个线程。每个线程我们可以让程序处理不同的任务，这样就是多线程编程。
	# 将需要被调用的函数传递给参数target。
	# name： 线程的名字。
	# args=()： 使用args可以传入实参。
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    # 调用start方法来让线程启动。
    added_thread.start()
    thread2.start()
    print('all done\n')

if __name__ == '__main__':
    main()

# 输出：
# T1 start
# T2 start
# all done
# T2 finish
# T1 finish

# Tips：默认情况下，调用start方法使得线程开始后，并不需要等待该线程执行完毕就会往下执行，所以输出看起来没那么规则。
# 以上我们可以看到，主线程的print并不是等待added_thread 、thread2 线程都执行完毕才打印的，这是因为主线程和t1，t2线程是同时跑的。

 
 
# 使用 threading.Thread() 方法可以创建线程对象并启动线程。以下是详细的使用方法：
# 创建 Thread 对象
# 创建 Thread 对象时，需要提供一个可调用对象（通常是一个函数）作为线程的执行函数。
# 可以通过直接传递函数名或使用 lambda 表达式来创建可调用对象，使用 threading.Thread() 创建
# 启动线程
# 创建 Thread 对象后，可以通过调用 start() 方法启动线程。
# 等待线程结束
# 如果需要等待一个线程执行结束，可以使用join()方法。join() 方法会阻塞当前线程，直到被调用的线程执行结束。

