import turtle

def ang_steps(t,a,s):
	if a > 0:
		t.right(a)
	else:
		t.left(a)
	t.forward(s)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex Dando um role locão")
alex = turtle.Turtle()

ang_steps(alex, 160, 20)
ang_steps(alex, -43, 10)
ang_steps(alex, 270, 8)
ang_steps(alex, -43, 12)

wn.mainloop()