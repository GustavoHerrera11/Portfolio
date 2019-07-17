print ""
print "=================================================="
print "Bienvenido a nuestro supermercado".center(50,"=")
print ""
print "Este es el listado de productos que le ofrecemos: ".center(50,"=")
print "=================================================="

Suma = 0
Total = []
Total_Suma = []


print "1. Arroz".center(50,"-")
print "2. Frijol".center(50,"-")
print "3. Aceite".center(50,"-")
print "4. Jugos".center(50,"-")
print "5. Galletas".center(50,"-")

print ""
Compra = input("Ingrese el numero del producto que desee comprar: ")



if Compra == 1:
	Numero1 = input(" Ingrese la cantidad de arroz que desee comprar: ")
	Valor1 = Numero1 * 3.00
	Total.append(Valor1)
	print Valor1
	print ""
elif Compra == 2:
	Numero2 = input(" Ingrese el numero de elementos que desee comprar: ")
	Valor2 = Numero2 * 2.50
	Total.append(Valor2)
	print Valor2
	print ""
elif Compra == 3:
	Numero3 = input(" Ingrese el numero de elementos que desee comprar: ")
	Valor3 = Numero3 * 8.00
	Total.append(Valor3)
	print Valor3
	print ""
elif Compra == 4:
	Numero4 = input(" Ingrese el numero de jugos que desee comprar: ")
	Valor4 = Numero4 * 4.00
	Total.append(Valor4)
	print Valor4
	print ""
elif Compra == 5:
	Numero5 = input(" Ingrese el numero de galletas que desee comprar: ")
	Valor5 = Numero5 * 5.00
	Total.append(Valor5)
	print Valor5
	print ""
else:
	print "Lo sentimos   :(   este producto no existe. "
	print Total
	print ""

while Compra != 0:
	Compra = input("Ingrese el numero del siguiente producto: ")
	if Compra == 1:
		Numero6 = input("Ingrese el numero de elementos que desee comprar: ")
		Valor6 = Numero6 * 3.00
		Total.append(Valor6)
		print Valor6
		print ""
	elif Compra == 2:
		Numero7 = input("Ingrese el numero de elementos que desee comprar: ")
		Valor7 = Numero7 * 2.50
		Total.append(Valor7)
		print Valor7
		print ""
	elif Compra == 3:
		Numero8 = input("Ingrese el numero de elementos que desee comprar: ")
		Valor8 = Numero8 * 8.00
		Total.append(Valor8)
		print Valor8
		print ""
	elif Compra == 4:
		Numero9 = input("Ingrese el numero de jugos que desee comprar: ")
		Valor9 = Numero9 * 4.00
		Total.append(Valor9)
		print Valor9
		print ""
	elif Compra == 5:
		Numero10 = input("Ingrese el numero de galletas que desee comprar: ")
		Valor10 = Numero10 * 5.00
		Total.append(Valor10)
		print Valor10
		print ""
	elif Compra == 0:
		for s in Total:
			Suma += int(s)
			Total_Suma.append(Suma)
		print Total_Suma
		print "OJO LA ULTIMA CANTIDAD ES SU TOTAL."
	else:
		print "Lo sentimos   :(   este producto no existe."
		print Total
		print ""
