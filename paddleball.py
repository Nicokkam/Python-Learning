from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas     #Canvas é um aplicativo que permite criar/modificar objetos com facilidade
        self.paddle = paddle                                        #Cria a barrinha para bater na bola
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)    #Cria a bolinha
        starts = [-3, -2, -1, 1, 2, 3]               #Valores listados com que a bolina pode comecar
        random.shuffle(starts)                       #Sorteia um dos valores acima
        self.x = starts[0]                           #Incremento inicial em x da bolinha
        self.y = -3                                  #Incremento inicial em y da bolinha
        self.canvas_height = canvas.winfo_height()   #Chama a altura da tela
        self.canvas_width = canvas.winfo_width()     #Chama a largura da tela
        self.is_hitting_bottom = False               #É chamado quando a bola toca o chao
        canvas.move(self.id, 245, 100)               #Funcao para mover a bolinha(self.id), x+=245 / y+=100

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)    #Chama as funcoes de mover as bolinhas
        pos = self.canvas.coords(self.id)            #Atribue a variavel "pos" as coordenada da bolinha
        print(pos)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            # self.y = -1
            self.is_hitting_bottom = True
        if self.hit_top_paddle(pos) == True:
            self.y = -3
        if self.hit_bottom_paddle(pos) == True:
            self.y = 1
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_top_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)               #Retorna coordenada do eixo
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_bottom_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.x = 0
        self.canvas_width = canvas.winfo_width()
        canvas.move(self.id, 200, 300)
        canvas.bind_all('<KeyPress-Left>', self.move_left)
        canvas.bind_all('<KeyPress-Right>', self.move_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
    def move_left(self, event):
        self.x = -2
    def move_right(self, event):
        self.x = 2

tk = Tk()
tk.title('Game')
canvas = Canvas(tk, width=550, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
while 1:
    if ball.is_hitting_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
