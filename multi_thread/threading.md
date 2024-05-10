# threading模块
## 主要包含以下类和方法：
* Thread 类：表示一个线程，可以通过继承该类来创建自定义的线程类，并实现自己的 run 方法来定义线程的具体行为。
* Lock 类：表示一个锁对象，用于控制多个线程对共享资源的访问。可以使用 acquire 和 release 方法来加锁和释放锁。
* RLock 类：表示可重入锁对象，与 Lock 类类似，但可以在同一个线程中多次获取锁而不会导致死锁。
* Condition 类：表示条件变量对象，用于在线程之间进行协调和同步，可以使用 wait、notify 和 notify_all 方法来等待和通知其他线程。
* Event 类：表示事件对象，用于线程之间的通信和同步，可以使用 set 和 clear 方法来设置和清除事件状态，使用 wait 方法来等待事件触发。
* Timer 类：表示定时器对象，用于在指定时间后触发一个函数，可以使用 start 和 cancel 方法来启动和取消定时器。

---
---    

* threading.current_thread()：返回当前线程对象。

* threading.active_count()：返回当前线程总数，包括主线程和所有子线程。

* threading.enumerate()：返回一个包含所有当前活动线程的列表。

* threading.Lock()：创建一个锁对象，可以用来保护共享资源，防止多个线程同时访问。

* threading.RLock()：创建一个可重入锁对象，可以被同一个线程多次获取锁，主要用于递归函数。

* threading.Condition(lock=None)：创建一个条件变量对象，可以用来实现多个线程之间的协作。

* threading.Event()：创建一个事件对象，可以用来实现线程间的同步。

* threading.Timer(interval, function, args=[], kwargs={})：创建一个定时器对象，用于在指定时间后执行某个函数。
