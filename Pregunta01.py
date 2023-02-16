#1. Crea un programa en Python que simule una lista de compras. El programa debe permitir al usuario agregar productos al final de la lista, eliminar productos del inicio de la lista y mostrar todos los productos en la lista en orden de compra.

#Agregar articulos
#Remover articulos
#Ver articulos
 
#creamos una lista vacia
lista_Productos = list()
 
#funcion para agregar articulos a nuestra listaa
def agregar_Productos():
	print()
	print("Favor de agregar tus artículos")
	print()
	Productos = input("Agrega tu articulo: ")
	#Utilizamos string.capitaliza() para convertir nuestra primera letra en mayuscula
	lista_Productos.append(Productos.capitalize())
	print("Productos agregados")
	print()
 
#Funcion para borrar elementos de nuestra lista
def Elimina_Productos():
	articulo = input("Elementos a eliminar: ")
	#Agregamos de nuevo string.capitaliza()para que python no marque error
	lista_Productos.remove(articulo.capitalize())
	print("El producto se ha borrado con exito se ha borrado con exito!")
 
 
#Funcion para imprimir los artculos de nuestra lista
def Mostrar_lista():
	#muestra los articulos en forma de lista de python
	#print(lista_articulos)
	print()
	print("Productos  en tu lista")
	print("------------")
	for Productos in lista_Productos:
		print("------------")
		print(Productos)
		print("------------")
	print("------------")
	print("Estos son tus productos")
	print()
 
 
while  True:
	try:
		print("Menú")
		print ("1.- Agregar productos")
		print ("2.- Eliminar primer producto")
		print ("3.- Ver lista de productos")
		print ("4.- Salir")
 
		opcion = int(input("Que deseas hacer: "))
	except ValueError:
		print("Favor de ingresar una opcion valida")
	else:
		#si no es ninguna de las 4 opciones validas
		if opcion < 0 or opcion >4:
				print ("no es una opcion valida")
				continue
		if opcion == 1:
			agregar_Productos()
		elif opcion == 2:
			Elimina_Productos()
		elif opcion == 3:
			Mostrar_lista()
		else:
			break
print("Gracias por utilizar la lista hecha en Python")
