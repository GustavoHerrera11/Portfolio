numero1=input("Ingrese el primer numero: ")
numero2=input("Ingrese el segundo numero: ")
numero3=input("ingrese el tercer numero: ")
if  numero1>numero2 and numero1>numero3:
	print "El mayor es: ", numero1
elif numero2>numero1 and numero2>numero3:
	print "El mayor es: ", numero2
elif numero3>numero1 and numero3>numero2:
	print "El mayor es: ", numero3
else:
	print "No hay numero mayor"
