t = int( input("Numero de meses? ") )
p = 100000
n = 12
r = 0.08
A = p*(1+r/n)**(n*t)
print ("Valor Total: ", A) 
