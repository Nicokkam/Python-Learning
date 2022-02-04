import turtle

def draw_square(t,sz):
        for i in range(4):
                t.forward(sz)
                t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")
alex = turtle.Turtle()

for j in range(4):
	draw_square(alex,20)
	alex.penup()
	alex.forward(40)
	alex.pendown()
	
wn.mainloop()
