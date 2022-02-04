import turtle

def draw_poly(t, n, sz):
        for i in range(n):
                t.forward(sz)
                t.left(360/n)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex Dando um role")
alex = turtle.Turtle()

draw_poly(alex,int( input("Numero de Lados? ")),int( input("Tamanho? ")))

wn.mainloop()
