# @Time:2025/7/9 15:16
# @Author:卢科
# @Description:代码清单3-1 用Python实现栈
class Stack:
    def __init__(self):
        '''
        这是类的构造函数，在创建 Stack 实例时自动调用。
        它初始化一个空列表 self.items 来存储栈中的元素。
        列表是 Python 中一种非常方便的数据结构，可以用来模拟栈的操作（如入栈、出栈）。
        '''
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


