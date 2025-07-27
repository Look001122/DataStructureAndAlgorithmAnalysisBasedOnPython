# @Time:2025/7/25 17:02
# @Author:卢科
# @Description:代码清单4-15 添加查询表之后的找零算法

import time

def recMC(coinValueList,change,knownResults):
    minCoins=change
    if change in coinValueList:
        knownResults[change]=1
        return 1
    elif knownResults[change]>0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins=1+recMC(coinValueList,change-i,knownResults)
            if numCoins < minCoins:
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins

start=time.time()
a=recMC([1,5,10,25],63,[0]*64)
end=time.time()
print(a,end-start)
