def count_odd(n):
	y=0
	for i in (n):
		if i % 2 == 1:
			y += 1
	return y


print (count_odd([12, 16, 17, 24, 29, 30,1,3,5,65,64]))
