def test(actual, expected):
	import sys
	linenum = sys._getframe(1).f_lineno
	if (expected == actual):
		msg = "Test on line {0} passed.".format(linenum) 
	else:
		msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'." . format(linenum, expected, actual))
	print(msg)

def to_secs(h,m,s):
	h = h*3600
	m = m*60
	secs = h + m + s
	return secs

test(to_secs(2, 30, 10), 9010) 
test(to_secs(2, 0, 0), 7200) 
test(to_secs(0, 2, 0), 120) 
test(to_secs(0, 0, 42), 42) 
test(to_secs(0, -10, 10), -590)
