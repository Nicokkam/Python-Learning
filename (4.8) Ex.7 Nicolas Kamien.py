def sum_to(n):
	j = 0
	for i in range(n):
		j = i + j
	return j

print(sum_to(int(input("Numeros a serem somados? "))+1))
