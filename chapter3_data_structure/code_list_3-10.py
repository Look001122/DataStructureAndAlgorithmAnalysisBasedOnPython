# @Time:2025/7/13 10:21
# @Author:卢科
# @Description:代码清单3-10 传土豆模拟程序

from pythonds.basic import Queue
def hotPotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


