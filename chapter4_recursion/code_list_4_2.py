# @Time:2025/7/19 16:03
# @Author:卢科
# @Description:代码清单4-2 递归求和函数

def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0]+listsum(numList[1:])