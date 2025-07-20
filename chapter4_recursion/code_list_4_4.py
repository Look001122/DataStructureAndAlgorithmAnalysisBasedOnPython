# @Time:2025/7/19 16:26
# @Author:卢科
# @Description:代码清单4-4 把字符串压入栈中
from pythonds import Stack

rStack=Stack()
def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n%base])
        toStr(n // base ,base)

    while  not rStack.isEmpty():
        print(rStack.pop(),end="")

toStr(10,2)
