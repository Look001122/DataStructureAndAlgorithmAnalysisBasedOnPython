# @Time:2025/7/20 16:48
# @Author:卢科
# @Description:代码清单4-7 绘制谢尔平斯基三角形

import turtle

# 绘制一个填充颜色的三角形
def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.penup()
    t.goto(points[0][0], points[0][1])
    t.pendown()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

# 获取两个点的中点
def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# 递归绘制谢尔平斯基三角形
def sierpinski(points, degree, t):
    # 不同深度对应的颜色（可选）
    colormap = ['blue', 'red', 'green', 'cyan', 'yellow', 'magenta']
    color = colormap[degree % len(colormap)]

    # 绘制外层三角形
    draw_triangle(points, color, t)

    if degree > 0:
        # 左下三角形
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   degree - 1, t)
        # 上方三角形
        sierpinski([get_mid(points[0], points[1]),
                    points[1],
                    get_mid(points[1], points[2])],
                   degree - 1, t)
        # 右下三角形
        sierpinski([get_mid(points[0], points[2]),
                    get_mid(points[1], points[2]),
                    points[2]],
                   degree - 1, t)

def main():
    # 初始化 turtle
    t = turtle.Turtle()
    t.speed(0)
    win = turtle.Screen()

    # 定义初始大三角形的三个顶点
    points = [[-200, -150], [0, 200], [200, -150]]

    # 设置递归深度（degree）
    sierpinski(points, 6, t)

    win.exitonclick()

main()
