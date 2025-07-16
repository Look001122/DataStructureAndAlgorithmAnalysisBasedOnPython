# @Time:2025/7/13 10:56
# @Author:卢科
# @Description:代码清单3-13 打印任务模拟程序

from pythonds.basic import Queue
import random
from code_list_3_11 import Printer
from code_list_3_12 import Task


def simulation(numSeconds,pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/(len(waitingtimes))
    print("Average Wait %6.2f secs %3d tasks remaining" %(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,10)
