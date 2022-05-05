"""
    1、递归案例1：使用turtle模块递归绘制曲线
"""

from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSprial(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSprial(myTurtle, lineLen-5)

drawSprial(myTurtle, 100)
myWin.exitonclick()