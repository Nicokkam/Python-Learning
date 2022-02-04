def neg_sum(n):
	s = 0
	for i in (n):
		if i < 0:
			s += i
	return s

print (neg_sum([-12, 16, 17, 24, 29, 30, -1, 3, -5, 65, 64]))
