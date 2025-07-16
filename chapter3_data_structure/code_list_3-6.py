# @Time:2025/7/11 17:03
# @Author:卢科
# @Description:代码清单3-6 将十进制数转换成任意进制数

from pythonds.basic import Stack
def baseConverter(decNumber,base):
    digits="0123456789ABCDEF"
    remstack=Stack()

    while decNumber>0:
        rem=decNumber%base
        remstack.push(rem)
        decNumber //= base

    newString=""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString
