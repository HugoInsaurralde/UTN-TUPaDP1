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

#import random
#num_correcto = random.randint(0,9)

#num_usuario = int(input("Ingrese un numero del 0 al 9 y adivina el correcto! : "))
#contador = 1
#if num_usuario >= 0 and num_usuario <=9:
#    while num_usuario != num_correcto:
#        print("Este no es el numero correcto! sigue intentando...")
#        contador += 1
#        num_usuario = int(input("Ingrese un numero del 0 al 9 y adivina el correcto! : "))
#    else:
#        print("Correcto!! adivinaste el numero, lo hiciste en ", contador, "intentos")
#else:
#    print("No ingresaste un numero dentro del rango")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

#num = 100

#for num in range (num,0,-2):
#    print(num)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 

#num = int(input("Ingrese un numero "))
#suma = 0
#contador = 0

#while contador != num:
#    contador = contador + 1
#    suma = suma + contador

#print("La suma de 0 hasta", num , "es: ",suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#contador = 0
#cont_par = 0
#cont_impar = 0 
#cont_positivos = 0
#cont_negativos = 0

#for contador in range (100):
#    numeros = int(input("Ingrese 100 numeros enteros: "))
#    if numeros % 2 == 0:
#        cont_par = cont_par + 1
#    else:
#        cont_impar = cont_impar + 1
#    if numeros < 0:
#        cont_negativos = cont_negativos + 1
#    else:
#        cont_positivos = cont_positivos + 1

#print(f"De los numeros que ingresaste: {cont_par} son pares, {cont_impar} son impares, {cont_positivos} son positivos y {cont_negativos} son negativos.")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).


