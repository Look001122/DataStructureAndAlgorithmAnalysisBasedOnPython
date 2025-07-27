# @Time:2025/7/27 14:09
# @Author:卢科
# @Description:代码清单5-1 无序列表的顺序搜索

def sequentialSearch(alist,item):
    pos=0
    found=False

    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos +=1

    return found
