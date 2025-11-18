# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
# num = int(input("Ingrese un número entero positivo: "))
# for i in range(1, num):
#     print(f"El factorial de {i} es:  {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

# def fibonacci (num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)

# posicion_fibonacci = int(input("Ingrese la posicion maxima del numero fibonacci: "))
# if posicion_fibonacci < 0:
#     print("Debe ingresar un numero mayor a 0")
# else:
#     for i in range(1, posicion_fibonacci + 1):
#         print(f"Para la posicion {i} el numero fibonacci es:  {fibonacci(i)} ")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

# def potencia(base, exponente):
#     if exponente == 0:
#         return 1
#     else:
#         return base * potencia (base , exponente -1)

# base = int(input("Ingrese la base: "))
# exponente = int(input("Ingrese el exponente: "))

# if base == 0 or exponente == 0:
#     print("El numero debe ser mayor a 0")
# else:
#     print(f"{base} elebado a la {exponente} es igual a : {potencia(base,exponente)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto.

# def num_binario (num):
#     if num == 0:
#         return "0"
#     else:
#         return num_binario(num // 2) + str(num % 2)

# num = int(input("Ingrese un numero entero positivo que quiera pasar a binario: "))

# print(f"{num} en numero binario es {num_binario(num)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

# def es_palindromo(palabra):
#     if len(palabra) <= 1:
#         return True
#     if palabra[0] != palabra[-1]:
#         return False
#     return es_palindromo(palabra[1:-1])


# texto = input("Ingrese una palabra (sin espacios ni tildes): ")

# texto = texto.lower()

# if es_palindromo(texto):
#     print(f"'{texto}' es un palindromo")
# else:
#     print(f"'{texto}' no es un palindromo")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

# def suma_digitos(n):
#     if n < 10:
#         return n
#     else:
#         ultimo = n % 10
#         resto = n // 10
#         return ultimo + suma_digitos(resto)


# numero = int(input("Ingrese un número entero positivo: "))

# if numero >= 0:
#     resultado = suma_digitos(numero)
#     print(f"La suma de los dígitos de {numero} es: {resultado}")
# else:
#     print("Debe ingresar un número entero positivo.")

# def contar_bloques(num):
#     if num == 1:
#         return 1
#     else:
#         return num + contar_bloques(num - 1)


# nivel_mas_bajo = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))

# if nivel_mas_bajo >= 1:
#     total = contar_bloques(nivel_mas_bajo)
#     print(f"Para construir la piramide se necesitan {total} bloques en total.")
# else:
#     print("El numero debe ser mayor o igual a 1.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#       Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4 
#contar_digito(123456, 7)     → 0   

# def contar_digito(numero, digito):
#     if numero < 10:
#         if numero == digito:
#             return 1
#         else:
#             return 0
#     else:
#         ultimo = numero % 10
#         resto = numero // 10
#         if ultimo == digito:
#             return 1 + contar_digito(resto, digito)
#         else:
#             return contar_digito(resto, digito)


# num = int(input("Ingrese un numero entero positivo: "))
# dig = int(input("Ingrese el digito que desea buscar (0 a 9): "))

# if num >= 0 and 0 <= dig <= 9:
#     resultado = contar_digito(num, dig)
#     print(f"El digito {dig} aparece {resultado} veces en {num}.")
# else:
#     print("Entrada invalida.")

