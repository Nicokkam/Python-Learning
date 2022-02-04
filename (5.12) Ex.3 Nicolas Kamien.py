def Alarm(hr,wt):
	mins = wt%24
	hr = hr + mins
	return hr

print("Horário que tocará: ", Alarm(int(input("Horário Atual? ")),(int(input("Número de horas a serem esperadas: ")))))
