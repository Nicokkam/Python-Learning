from tkinter import *
#import random
#import time

class bird:
    def __init__(self, canvas, color):    #Colocar coisas aqui
        self.canvas = canvas
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.id = canvas.create_oval(30, 250, 60, 280, fill = color)
        
    def draw(self):
        canvas.create_oval(30, 250, 60, 280, fill = 'red')

janela = Tk()
janela.title("Game")
canvas = Canvas(janela, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
janela.update()

#canvas.create_oval(30, 250, 60, 280, fill ='black')

passaro = bird(canvas, 'black')
#a.draw()


janela.mainloop()



  



#while 1:
#    if ball.is_hitting_bottom == False:
#        bird.draw()
#        paddle.draw()
#    tk.update_idletasks()
#    tk.update()
#    time.sleep(0.01)