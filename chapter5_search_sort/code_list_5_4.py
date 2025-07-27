# @Time:2025/7/27 14:38
# @Author:卢科
# @Description:代码清单5-4 二分搜索的递归版本

def binarySearch(alist,item):
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)


