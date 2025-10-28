# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print(precios_frutas)

# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print(precios_frutas)

# Frutas = precios_frutas.keys()

# print(Frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 
# Ejemplo: 

# contacos = {}

# for i in range (5):
#     nombre = input("Ingrese el nombre del contacto que desea agregar: ")
#     numero = str(input("Ingrese el numero del contacto nuevo: "))
#     contacos[nombre] = numero

# buscar = input("Ingrese el nombre del contacto que desea buscar: ")

# if buscar in contacos:
#     print(f"El numero de {buscar} es {contacos[buscar]}")
# else:
#     print("El contacto que busca no se encuentra en la lista...")



# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 
# Ejemplo: 

# frase = input("Ingresá una frase: ")

# palabras = frase.split()

# palabras_unicas = set(palabras)

# contador = {}

# for palabra in palabras:
#     if palabra in contador:
#         contador[palabra] += 1
#     else:
#         contador[palabra] = 1


# print("Palabras únicas:")
# print(palabras_unicas)

# print("Cantidad de apariciones por palabra:")
# print(contador)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 
# Ejemplo: 
# alumnos = {}

# for i in range(3):
#     nombre = input("Ingresá el nombre del alumno: ")

#     n1 = int(input("Ingresá la primera nota: "))
#     n2 = int(input("Ingresá la segunda nota: "))
#     n3 = int(input("Ingresá la tercera nota: "))


#     alumnos[nombre] = (n1, n2, n3)


# print("Promedios de los alumnos:")
# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"{nombre}: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

# parcial_1 = {"Hugo", "Flor", "Agustín", "Sofía"}
# parcial_2 = {"Flor", "Sofía", "Martina", "Jorge"}


# ambos = parcial_1 & parcial_2


# solo_uno = parcial_1 ^ parcial_2


# al_menos_uno = parcial_1 | parcial_2

# print("Aprobaron ambos parciales:", ambos)
# print("Aprobaron solo uno:", solo_uno)
# print("Aprobaron al menos uno:", al_menos_uno)



# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

# productos = {
#     "martillo": 10,
#     "clavo": 100,
#     "destornillador": 5
# }


# nombre = input("Ingresá el nombre del producto: ").lower()

# if nombre in productos:
#     print(f"El stock actual de {nombre} es: {productos[nombre]}")
#     agregar = int(input("¿Cuántas unidades querés agregar?: "))
#     productos[nombre] += agregar
#     print(f"Nuevo stock de {nombre}: {productos[nombre]}")
# else:
#     print(f"El producto '{nombre}' no existe.")
#     nuevo_stock = int(input("Ingresá el stock inicial para agregarlo: "))
#     productos[nombre] = nuevo_stock
#     print(f"Producto '{nombre}' agregado con stock {nuevo_stock}.")


# print("Stock actualizado:")
# print(productos)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora. 


# agenda = {
#     ("lunes", "9:00"): "Reunión de equipo",
#     ("martes", "14:00"): "Clase de Python",
#     ("viernes", "18:30"): "Gimnasio"
# }


# dia = input("Ingresa el dia: ").lower()
# hora = input("Ingresa la hora (ejemplo 9:00): ")


# clave = (dia, hora)

# if clave in agenda:
#     print(f"En {dia} a las {hora} tenes: {agenda[clave]}")
# else:
#     print(f"No hay actividades programadas el {dia} a las {hora}.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 
# Ejemplo:

# paises = {
#     "Argentina": "Buenos Aires",
#     "Chile": "Santiago",
#     "Uruguay": "Montevideo"
# }

# capitales = {}

# for pais, capital in paises.items():
#     capitales[capital] = pais

# print(capitales)
