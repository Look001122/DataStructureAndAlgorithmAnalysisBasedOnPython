# @Time:2025/7/9 20:55
# @Author:卢科
# @Description:代码清单3-4 匹配符号

from pythonds.basic import Stack

def parChecker(symbolString):
    s=Stack()
    balanced=True
    index=0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balanced=False

        index=index+1

    if balanced and s.isEmpty():
            return True
    else:
        return False

def matches(open,close):
    opens="([{"
    closers=")]}"

    return opens.index(open)==closers.index(close)