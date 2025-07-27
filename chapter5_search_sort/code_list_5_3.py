# @Time:2025/7/27 14:19
# @Author:卢科
# @Description:代码清单5-3 有序列表的二分搜索
def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    found=False

    while first <= last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if item <alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1

    return found
