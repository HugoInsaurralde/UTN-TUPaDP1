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

#temperaturas = [
#    [8,12],
#    [10,18],
#    [9,15],
#    [10,20],
#    [12,24],
#    [11,22],
#    [10,19]
#]
#suma_min = 0
#suma_max = 0
#mayor_ampl = 0
#dia_mayor_ampl = 0
#for dia in temperaturas:
#    suma_min+= dia[0]
#    suma_max+= dia[1]
#
#promedio_min = suma_min / len(temperaturas)
#promedio_max = suma_max / len(temperaturas)
#
#for i,dia in enumerate(temperaturas, start=1):
#    amplitud = dia[1] - dia[0]
#    if amplitud > mayor_ampl:
#        mayor_ampl = amplitud
#        dia_mayor_ampl = i
#
#print("---------------------------------------------------------------------------------------------------")
#print("El promedio de temperatura minima de la semana es de: ", promedio_min )
#print("El promedio de temperatura maxima de la semana es de: ", promedio_max )
#print("---------------------------------------------------------------------------------------------------")
#print(f"El dia que se registro mayor amplitud termica fue el dia: {dia_mayor_ampl} con una amplitud de: {mayor_ampl}")
#print("---------------------------------------------------------------------------------------------------")

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

#estudiantes = ["Laura", "Sofia", "Mauro", "Lucas", "Hugo"]
#notas = [[7,9,10],[10,8,10],[7,8,9],[7,6,7],[10,10,10]]
#
#for i,nombres in enumerate(estudiantes):
#    promedio = (notas[i][0] + notas[i][1] + notas[i][2]) / len(notas[i])
#    print(f"el prodedio de: {estudiantes[i]} es: {promedio}")
#
#suma_materia1 = notas[0][0] + notas[1][0] + notas[2][0] + notas[3][0] + notas[4][0]
#suma_materia2 = notas[1][1] + notas[1][1] + notas[2][1] + notas[3][1] + notas[4][1]
#suma_materia3 = notas[0][2] + notas[1][2] + notas[2][2] + notas[3][2] + notas[4][2]
#promedio_1 = suma_materia1 / len(notas[0])
#promedio_2 = suma_materia2 / len(notas[0])
#promedio_3 = suma_materia3 / len(notas[0])
#
#print(f"El promedio de la primer materia es: {promedio_1} de la segunda es {promedio_2} y de la tercera es {promedio_3}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada.

tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]

print(tablero)

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana.