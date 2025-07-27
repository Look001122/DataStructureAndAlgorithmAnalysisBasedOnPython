import turtle
#迷宫搜索程序全局常量
START = "S" #--->起始位置
OBSTACLE = "+"  #--->墙
TRIED = "." # 走过的路
DEAD_END = "-" # 死路
PART_OF_PATH = "0" # 走出迷宫的出口


#Maze类构造方法
class Maze:
    def __init__(self,maze_filename):
        with open(maze_filename,"r") as maze_file:
            self.maze_list = [
                [ch for ch in line.strip("\n")]
                for line in maze_file.readlines()
            ]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break
        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(self.columns_in_maze - 1) / 2 - 0.5,
            -(self.rows_in_maze - 1) / 2 - 0.5,
            (self.columns_in_maze - 1) / 2 + 0.5,
            (self.rows_in_maze - 1) / 2 + 0.5,
        )


    #Maze 类绘制方法
    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range (self.rows_in_maze):
            for x in range (self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate,
                        -y + self.y_translate,
                        "orange",
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    #Maze 类移动方法
    def update_position(self,row,col,val=None):
        """标记路径并更新迷宫图景"""
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:#已走
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None
        if color:
            self.drop_bread_crumb(color)#留下标记物

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(
            self.t.towards(
                x + self.x_translate,
                -y + self.y_translate,
            )
        )
        self.t.goto(
            x + self.x_translate, -y + self.y_translate
        )

    def drop_bread_crumb(self,color):
        self.t.dot(10,color)

    def is_exit(self, row, col):
        """如果乌龟处于迷宫边缘,表示到达出口"""
        return (
            row in [0,self.rows_in_maze - 1]
            or col in [0,self.columns_in_maze - 1]
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]

def search_from(maze, row, column):
    """对当前位置的四个方向逐一尝试
        直至找到出口"""
    maze.update_position(row, column)
    #检查基本情况:
    #1. 遇到了障碍
    if maze[row][column] == OBSTACLE:
        return False
    #2. 遇到已经访问过的位置
    if maze[row][column] in [TRIED, DEAD_END]:
        return False
    #3. 找到了出口
    if maze.is_exit(row,column):
        maze.update_position(row, column, PART_OF_PATH)
        return True
    maze.update_position(row, column, TRIED)
    #使用逻辑 or 对各个方向进行
    #逐一尝试
    found = (#利用段路经,逐语句读取  北,南,西,东
        search_from(maze, row - 1, column)
        or search_from(maze, row + 1, column)
        or search_from(maze, row, column-1)
        or search_from(maze, row, column+1)
    )
    if found:
        maze.update_position(row, column , PART_OF_PATH)
    else:
        maze.update_position(row, column , DEAD_END)
    return found

my_maze = Maze('maze2.txt')
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)
search_from(my_maze, my_maze.start_row, my_maze.start_col)