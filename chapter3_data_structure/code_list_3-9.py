# @Time:2025/7/13 10:13
# @Author:卢科
# @Description:代码清单3-9 用python实现队列

class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

