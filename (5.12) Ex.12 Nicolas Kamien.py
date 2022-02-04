def find_hypot(cat1,cat2):
	hypot = cat1**2+cat2**2
	hypot = hypot **0.5
	return hypot

print("Tamanho da Hipotenusa: ", find_hypot((int(input("Tamanho Cateto1: "))),(int(input("Tamanho Cateto2: ")))))
