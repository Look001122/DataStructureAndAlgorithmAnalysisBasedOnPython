# @Time:2025/7/13 14:18
# @Author:卢科
# @Description:代码清单3-16 Node类

class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data

    def gerNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext