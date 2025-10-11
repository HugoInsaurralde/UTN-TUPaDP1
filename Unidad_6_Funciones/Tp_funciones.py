# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# imprimir_hola_mundo()

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

# def saludar_usuario(nombre):
#     print("Hola ", nombre)

# nombre = input("Cual es su nombre?: ")
# saludar_usuario(nombre)

#  3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

# def informacion_personal(nombre,apellido,edad,residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}. ")

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su lugar de residencia: ")

# informacion_personal(nombre,apellido,edad,residencia)

#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
# PI = 3.14

# def calcular_area_circulo(radio):
#     return PI * radio ** 2

# def calcular_perimetro_circulo(radio):
#     return 2 * PI * radio

# radio = float(input("Ingrese el radio del circulo: "))

# print(f"El area del circulo es {calcular_area_circulo(radio)} y el perimetro del circulo es {calcular_perimetro_circulo(radio)}")

#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

# def segundos_a_horas(segundos):
#     return segundos / 3600

# segundos = int(input("Escribe los segundos que quieras pasar a hora: "))
# print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.")

#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

# def tabla_multiplicar(numero):
#     for i in range(1,11):
#         resultado = i * numero
#         print(f"{i} x {numero} = {resultado}")

# numero = int(input("Ingrese el numero del que desea saber su tabla de multiplicar: "))
# print(tabla_multiplicar(numero))

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

# def operaciones_basicas(a,b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     divicion = a / b
#     return (suma, resta,multiplicacion,divicion)

# num1 = int(input("Ingrese el primer numero para las operaciones basicas: "))
# num2 = int(input("Ingrese el segundo numero para las operaciones basicas: "))

# resultado = operaciones_basicas(num1,num2)
# print("El resultado de las operaciones basicas de esos 2 numeros es: ", resultado)


#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

# def calcular_imc(peso,altura):
#     imc = peso / (altura ** 2)
#     return imc


# peso = float(input("Por favor ingrese su peso: "))
# altura = float(input("Por favor ingrese su altura: "))
# print(f"Su IMC es: {calcular_imc(peso,altura)}")


#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# celsius = int(input("Ingrese los celsius que quiera pasar a fahrenheit: "))
# print(f"{celsius} celsius equivalen a {celsius_a_fahrenheit(celsius)} fahrenheit ")

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

# def calcular_promedio(a,b,c):
#     promedio = (a + b + c) / 3
#     return promedio

# num1 = float(input("Ingrese el primer numero: "))
# num2 = float(input("Ingrese el segundo numero: "))
# num3 = float(input("Ingrese el tercer numero: "))

# print("El promedio de los 3 numeros recibidos es: ", calcular_promedio(num1,num2,num3))
