# @Time:2025/7/13 10:53
# @Author:卢科
# @Description:代码清单3-12 Task类

import random
class Task:
    def __init__(self, time):
        self.timestamp=time
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime-self.timestamp
