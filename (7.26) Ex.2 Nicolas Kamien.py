def sum_even(n):
	s = 0
	for i in (n):
		if i % 2 == 0:
			s += i
	return s


print (sum_even([12, 16, 17, 7, 29, 30, 1, 3, 5, 65, 67]))
