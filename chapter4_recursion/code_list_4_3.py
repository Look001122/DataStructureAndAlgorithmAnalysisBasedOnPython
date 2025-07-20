# @Time:2025/7/19 16:20
# @Author:卢科
# @Description:代码清单4-3 将整数转换成以2~16为进制基数的字符串
def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]

print(toStr(10,2))
