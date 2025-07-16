# @Time:2025/7/13 10:46
# @Author:卢科
# @Description:代码清单3-11 Printer类的实现

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining-1
            if self.timeRemaining <= 0:
                self.currentTask=None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate
