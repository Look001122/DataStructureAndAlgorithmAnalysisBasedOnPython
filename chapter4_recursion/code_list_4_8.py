# @Time:2025/7/24 21:22
# @Author:卢科
# @Description:代码清单4-8 解决汉诺塔问题的Python代码

from code_list_4_9 import moveDisk

def moveTower(height,fromPole,toPole,withPole):
    if height>=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

moveTower(2,1,2,3)