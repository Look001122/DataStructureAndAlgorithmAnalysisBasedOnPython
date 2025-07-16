# @Time:2025/7/11 16:54
# @Author:卢科
# @Description:代码清单3-5 “除以2”算法的python实现

from pythonds.basic import Stack
def divideBy2(decNumber):
    remstack=Stack()

    while decNumber>0:
        rem=decNumber%2
        remstack.push(rem)
        decNumber=decNumber//2

    binString=""
    while not remstack.isEmpty():
        binString+=str(remstack.pop())

    return binString
