from tkinter import *
import tkinter.messagebox

color_number = 1 #每次运行都是黑棋先走
size = 16
stop = 0
 
chess = [[0 for i in range(size+1)] for i in range(size+1)]

def paint(event):
    #让棋子下在棋盘点上
    global color_number

    if event.x % 30 > 15 :
        event.x = event.x//30 + 1 
    else:
        event.x = event.x // 30
    if event.y % 30 > 15:
        event.y = event.y // 30 + 1
    else:
        event.y = event.y//30
    #边缘检测    
    if event.x > size:
        event.x = size
    if event.y > size:
        event.y = size
    if event.x < 1:
        event.x = 1
    if event.y < 1:
        event.y = 1
    #确定下棋坐标
    x1, y1 = (event.x*30 - 15), (event.y*30 - 15)
    x2, y2 = (event.x*30 + 15), (event.y*30 + 15)
    if stop == 0:
        if chess[event.x][event.y] == 0: 
            if color_number == 1:
                canvas.create_oval(x1, y1, x2, y2, fill="black",tags = "oval")
                chess[event.x][event.y] = 1
                gameover(event.x,event.y)
                color_number = 0
            elif color_number == 0:
                canvas.create_oval(x1, y1, x2, y2, fill="white",tags = "oval")
                chess[event.x][event.y] = 2
                gameover(event.x,event.y)
                color_number = 1
            
def wininfo(): #提示窗口
    global stop
    tkinter.messagebox.showinfo("", "Game over")
    stop = 1
            
def  gameover(xx, yy):
   
    count = 0
    for i in range(xx + 1, 17):  #向右搜索
        if chess[i][yy] == chess[xx][yy]:
            count += 1
        else:
            break
    for i in range(xx, 0, -1):   #向左搜索
        if chess[i][yy] == chess[xx][yy]:
            count += 1
        else:
            break
    if count == 5:
        wininfo()
    count = 0

    for i in range(yy + 1, 17):  #向下搜索
        if chess[xx][i] == chess[xx][yy]:
            count += 1
        else:
            break
    for i in range(yy, 0, -1):   #向上搜索
        if chess[xx][i] == chess[xx][yy]:
            count += 1
        else:
            break
    if count == 5:
        wininfo()
    count = 0

    for i, j in zip(range(xx+1, 17), range(yy+1, 17)):  #向右下搜索
        if chess[i][j] == chess[xx][yy]:
            count += 1
        else:
            break
    for i, j in zip(range(xx, 0, -1), range(yy, 0, -1)):#向左上搜索
        if chess[i][j] == chess[xx][yy]:
            count += 1
        else:
            break
    if count == 5:
        wininfo()
    count = 0

    for i, j in zip(range(xx - 1, 0, -1), range(yy + 1, 17)): #向左下搜索
        if chess[i][j] == chess[xx][yy]:
            count += 1
        else:
            break
    for i, j in zip(range(xx, 17), range(yy, 0, -1)):    #向右上搜索
        if chess[i][j] == chess[xx][yy]:
            count += 1
        else:
            break
    if count == 5:
        wininfo()
    count = 0
    
def reset():
    canvas.delete('oval')

top = Tk()
top.title("五子棋")
top.geometry("510x525")

canvas = Canvas(top, width=500, height=500)
canvas.pack(expand=YES, fill=BOTH)
canvas.bind("<Button-1>",paint)#每次点击鼠标左键（事件）,触发paint函数

for num in range(1, 17):
    canvas.create_line(num*30, 30, 
                        num*30, 480,
                         width=2)
                         
for num in range(1, 17):
    canvas.create_line(30, num*30,
                        480, num*30, 
                         width=2)
                         
restart = Button(top,text ="RESTART",command=top.quit)
restart.pack()

top.mainloop()
