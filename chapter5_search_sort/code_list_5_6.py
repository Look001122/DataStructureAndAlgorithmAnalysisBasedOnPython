# @Time:2025/7/27 15:24
# @Author:卢科
# @Description:代码清单5-6 HashTable类的构造方法
class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None]*self.size
        self.data=[None]*self.size
