# @Time:2025/7/13 13:59
# @Author:卢科
# @Description:代码清单3-15 用python实现回文检测器

from pythonds.basic import Deque
def palchecker(aString):
    chardeque=Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size()>1 and stillEqual:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first != last:
            stillEqual=False

    return stillEqual


