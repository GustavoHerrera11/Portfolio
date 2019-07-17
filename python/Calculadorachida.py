tabla = raw_input ("tabla: ")
numero = raw_input ("hasta que numero: ")

tabla= int(tabla)
numero= int(numero) + 1

for x in range(1,numero):
	print str(tabla)+"x"+str(x)+"="+str(x*tabla)