# @Time:2025/8/24 14:59
# @Author:卢科
# @Description:代码清单6-2 插入左子树
def insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

