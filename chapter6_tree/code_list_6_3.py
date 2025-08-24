# @Time:2025/8/24 15:07
# @Author:卢科
# @Description:代码清单6-3 插入右子树
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
