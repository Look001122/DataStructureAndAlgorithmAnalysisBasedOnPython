# @Time:2025/7/27 15:00
# @Author:卢科
# @Description:代码清单5-5 为字符串构建简单的散列函数
def hash(astring,tablesize):
    sum=0
    for pos in range(len(astring)):
        sum += ord(astring[pos])*(pos+1)

    return sum%tablesize
