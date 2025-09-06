#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

#num_ent = -1

#for num_ent in range (0,101):
#    print(num_ent)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

#num = input("Por favor ingrese un numero entero: ")

#print("Su numero entero tiene" ,len(num), "digitos!")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

#num1 = int(input("Ingrese el primer numero entero: "))
#num2 = int(input("Ingrese el segundo numero entero: "))

#contador = 0
#suma = 0

#while num1 > 0 and num2 > 0:
#    for contador in range (num1, num2 - 1):
#        contador = contador + 1
#        suma = suma + contador
#else:
#    print("No ingresaste un numero entero")

#print("La suma de los numeros (excluyendo los ingresados) es: " , suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 

#num = int(input("Ingrese un numero entero (cuando desee conocer el resultado de la suma precione 0): "))
#suma = 0

#while num != 0:
#    suma = suma + num
#    num = int(input("Ingrese un numero entero (cuando desee conocer el resultado de la suma precione 0): "))

#print("La suma de los numeros es: ",suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
