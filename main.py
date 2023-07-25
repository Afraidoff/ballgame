import tkinter  as tk
from time import sleep

class Figure:

    def __init__(self,canvas):

        self.canvas = canvas
        self.figure = None

        self.speed_x = 0
        self.speed_y = 0



    def draw(self):
        self.canvas.move(self.figure,self.speed_x,self.speed_y)

    def figure_move(self,x,y):
        self.canvas.move(self.figure, x, y)



class Ball(Figure):
    def __init__(self,canvas,platform):
        super().__init__(canvas)
        self.platform = platform
        self.figure = self.canvas.create_oval(0,0,20,20)
        self.figure_move(200,200)
        self.speed_x = 2
        self.speed_y = 2
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        print(self.canvas_width)

    def draw(self):
        self.figure_move(self.speed_x,self.speed_y)
        self.check_wall()


    def check_wall(self):
        pos = self.canvas.coords(self.figure)
        if pos[0] <= 0:
            self.speed_x = 1
        elif pos[2] >= 500:
            self.speed_x = -1
        if pos[1] <= 0: 
            self.speed_y = 1
        elif pos[3] >= 400:
            print('Ты проиграл')

        elif self.check_hit(pos_ball=pos):
            self.speed_y = -1

    def check_hit(self,pos_ball):
        pos_platform = self.canvas.coords(self.platform.figure)
        print(pos_platform)
        return pos_ball[3] >= pos_platform[1] and\
           pos_ball[3] <= pos_platform[3] and\
           pos_ball[0] <= pos_platform[2] and\
           pos_ball[2] >= pos_platform[0]



class Platform(Figure):
    def __init__(self,canvas):
        super().__init__(canvas)

        self.speed_x = 0
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.figure = self.canvas.create_rectangle(0,0,100,20,fill="black")
        self.canvas.move(self.figure,200,250)

    def turn_right(self,event):
        self.speed_x = 4
    def turn_left(self,event):
        self.speed_x = -4

    def draw(self):
         self.figure_move(self.speed_x, self.speed_y)
         self.check_wall()

    def check_wall(self):
        pos = self.canvas.coords(self.figure)
        if pos[0] <= 0:
            self.speed_x = 4
        elif pos[2] >= 500:
            self.speed_x = -4



def main():
    window = tk.Tk()
    canvas = tk.Canvas(window,width=500,height=400)
    canvas.pack()
    window.update()
    platform = Platform(canvas)
    ball = Ball(canvas,platform)
    print(canvas.winfo_width())
    while True:
        ball.draw()
        platform.draw()
        window.update()
        sleep(0.01)




if __name__ == '__main__':
    main()