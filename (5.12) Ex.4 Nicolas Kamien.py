def Week(nm):
	if nm==0:
		nm='Sunday'
	elif nm==1:
		nm='Monday'
	elif nm==2:
		nm='Tuesday'
	elif nm==3:
		nm='Wednesday'
	elif nm==4:
		nm='Thursday'
	elif nm==5:
		nm='Friday'
	else:
		nm='Saturday'
	return nm

print("Dia: ", Week(int(input("Entre com o número do dia: "))))
	  	