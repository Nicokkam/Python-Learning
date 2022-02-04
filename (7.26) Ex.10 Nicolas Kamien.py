def is_prime(n):
	c = 0
	for i in range(1,n+1):
		if n % i == 0:
			c += 1 		                          
	if c == 2 or n == 1 :
		p = "True"
	else:
		p = "False"
	return p

print (is_prime(int(input("Número a ser testado: "))))