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
	return int(secs)


test(to_secs(2.5, 0, 10.71), 9010) 
test(to_secs(2.433,0,0), 8758)