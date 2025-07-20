# @Time:2025/7/20 16:30
# @Author:卢科
# @Description:代码清单4-6 绘制分形树
def tree(branchLen,t):
    if branchLen>5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

from turtle import *
t=Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110,t)
myWin.exitonclick()