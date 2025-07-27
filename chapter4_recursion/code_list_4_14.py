# @Time:2025/7/25 16:55
# @Author:卢科
# @Description:代码清单4-14 找零问题的递归解决方案
import time

def recMC(coinValueList,change):
    minCoins=change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins < minCoins:
                minCoins=numCoins
    return minCoins

start=time.time()
a=recMC([1,5,10,25],63)
end=time.time()
print(a,end-start)


