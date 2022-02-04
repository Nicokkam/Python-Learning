def print_triangular_numbers(n):
	tn = 0
	for i in range(1,n+1):
		tn = (i*(i+1)//2)
		print(i,'\t',tn)

print_triangular_numbers(int(input("Entre o limite da soma: ")))
