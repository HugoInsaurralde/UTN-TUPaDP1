#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja. 

#total = 0
#nota_mayor = 0
#nota_menor = 10

#notas_estudiantes = [1.5,2.6,3,8,7.5,9,10,7.8,8.2,6]

#for n in notas_estudiantes:
#    print (n)
#    total+= n
#    if n > nota_mayor:
#        nota_mayor = n
#    if n < nota_menor:
#        nota_menor = n
#promedio = total / 10

#print(notas_estudiantes)
#print("El promedio de notas es:", promedio)
#print("La nota mayor es: ",nota_mayor)
#print("La nota menor es: ",nota_menor)

#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

#productos = []
#
#for i in range(5):
#    prod_ingr = input(f"Ingrese el producto {i + 1}: ")
#    productos.append(prod_ingr)
#
#print(sorted(productos))
#
#produc_elim = input("Que producto desea eliminar? ")
#
#if produc_elim in productos:
#    productos.remove(produc_elim)
#    print(productos)
#else:
#    print("El producto que desea eliminar no se encuentra en la lista")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista.

#import random
#num = []
#num_par = []
#num_impar = []
#for i in range(15):
#    num_aleat = random.randint(1,100)
#    num.append(num_aleat)
#    if num[-1] % 2 == 0:
#        num_par.append(num_aleat)
#    else:
#        num_impar.append(num_aleat)
#print(num)
#print("De la lista los pares son: ",num_par)
#print("De la lista los inpares son: ",num_impar)


#4) Dada una lista con valores repetidos: datos=[1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado. 

#datos=[1,3,5,3,7,1,9,5,3]

#datos_no_repetidos = []

#for num in datos:
#    if num not in datos_no_repetidos:
#        datos_no_repetidos.append(num)

#print("La lista sin repetidos es:", datos_no_repetidos)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada. 

#estudiante = ["Florencia","Victor","Teresa","Lorena","Valentina","Angie","Valeria","Kiara"]
#
#print("La lista de estudiantes es: ",estudiante)
#
#opcion = input("Desea eliminar o agregar algun estudiante? : ")
#
#if opcion == "Agregar" or opcion == "agregar":
#    alum_agreg= input("Escriba el nombre del alumno que quiere agregar: ")
#    estudiante.append(alum_agreg)
#    print("La lista con el alumno agregado quedo asi: ",estudiante)
#elif opcion == "Eliminar" or opcion == "eliminar":
#    alum_elim = input("Escriba el nombre del alumno que desea eliminar: ")
#    estudiante.remove(alum_elim)
#    print("La lista con el alumno eliminado quedo asi: ",estudiante)
#else:
#    print("Por favor, elija una opcion correcta")

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).

#numeros = [10, 20, 30, 40, 50, 60, 70]
#
#ultimo = numeros[-1]
#
#for i in range(len(numeros) - 1, 0, -1):
#    numeros[i] = numeros[i - 1] 
#
#numeros[0] = ultimo
#
#print("Después de rotar:", numeros)

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica. 


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 
#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada. 
#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 