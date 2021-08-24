'''
 500张票，有张三，李四，王五同时抢票，看谁抢的票最多。
        人：要同时抢票，实现多线程
        有票就抢，没票就停止
'''
#引入多线程 threading类
from threading import Thread
import time
#子类继承threading类
class PcManager(Thread):
    def run(self) -> None:
        for i in range(100000):
            print("电脑管家正在杀毒已经杀了",i,"个病毒")
            time.sleep(0.1)
class Pc360(Thread):
    def run(self) -> None:
        for i in range(100000):
            print("360正在杀毒已经杀了",i,"个病毒")
            time.sleep(0.2)

#创建对象
p1 = PcManager()
p2 = Pc360()

#启动
p1.start()
p2.start()