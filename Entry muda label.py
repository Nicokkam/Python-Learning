from tkinter import *

def b1_click():
    lb1["text"] = campo1.get()
    
janela = Tk()
janela.title("Joguinho Cocota")
janela["background"] = "white"
janela.geometry("500x500+500+200")      #LxA+E+T

lb1 = Label(janela, text = "Nome Usuario") #Colocando um label por coordenada na janela
lb1.place(x=10, y=10)

b1 = Button(janela, width=10, height=2, text="Start", command=b1_click)
b1.place(x=200, y=200)

campo1 = Entry(janela, width = 30)
campo1.place(x=110, y=250)


janela.mainloop()