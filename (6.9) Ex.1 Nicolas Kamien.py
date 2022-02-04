def test(actual, expected):
	import sys
	linenum = sys._getframe(1).f_lineno
	if (expected == actual):
		msg = "Test on line {0} passed.".format(linenum) 
	else:
		msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'." . format(linenum, expected, actual))
	print(msg)

def turn_clockwise(d):
	if d=='N':
		d='E'
	elif d=='E':
		d='S'
	elif d=='S':
		d='W'
	else:
		d='N'

	return d

test(turn_clockwise("N"), "E") 
test(turn_clockwise("W"), "N")
test(turn_clockwise('N'), 'E')
test(turn_clockwise('N'), 123)
