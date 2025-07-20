# @Time:2025/7/20 16:18
# @Author:卢科
# @Description:代码清单4-5 用turtle模块递归的绘制螺旋线
from turtle import *

myTurtle=Turtle()
myWin=myTurtle.getscreen()

def drawSpiral(myTurtle,lineLen):
    if lineLen>0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()
