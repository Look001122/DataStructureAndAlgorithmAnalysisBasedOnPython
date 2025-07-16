# @Time:2025/7/9 19:34
# @Author:卢科
# @Description:代码清单3-3 匹配括号

from pythonds.basic import Stack

def parChecker(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index=index+1

    if balanced and s.isEmpty():
            return True
    else:
        return False
