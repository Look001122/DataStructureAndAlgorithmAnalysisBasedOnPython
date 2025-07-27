# @Time:2025/7/27 14:14
# @Author:卢科
# @Description:代码清单5-2 有序列表的顺序搜索
from IPython.lib.deepreload import found_now
from fontTools.misc.cython import returns


def orderSequentialSearch(alist,item):
    pos=0
    found=False
    stop=False

    while pos<len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos +=1
    return found
