# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 

# with open("productos.txt","w") as archivo:
#     archivo.write("Martillo,14500,10\n")
#     archivo.write("Tenaza,10500,6\n")
#     archivo.write("Pinza,9500,15\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato: 
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30 

# with open("productos.txt","r") as archivo:
#     for linea  in archivo:
#         partes = linea.strip().split(",")
#         nombre = partes[0]
#         precio = partes[1]
#         cantidad = partes[2]
#         print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente. 

# with open("productos.txt","r") as archivo:
#     for linea  in archivo:
#         partes = linea.strip().split(",")
#         nombre = partes[0]
#         precio = partes[1]
#         cantidad = partes[2]
#         print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# print("--Agregar un nuevo producto---")
# nombre_nuevo = input("Ingrese el nombre del producto: ").strip()
# precio_nuevo = input("Ingrese el precio del producto: ").strip()
# cantidad_nuevo = input("Ingrese el cantidad del producto: ").strip()

# with open("productos.txt", "a") as archivo:
#     archivo.write(f"\n{nombre_nuevo},{precio_nuevo},{cantidad_nuevo}\n")

# print("Producto agregado correctamente")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
# una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad. 

# productos = [] 

# with open("productos.txt", "r") as archivo:
#     for linea in archivo:
#         linea = linea.strip()
#         if not linea:
#             continue
#         partes = linea.split(",")
#         if len(partes) != 3:
#             continue

#         nombre = partes[0]
#         precio = float(partes[1])      
#         cantidad = int(partes[2])      

#         producto = {
#             "nombre": nombre,
#             "precio": precio,
#             "cantidad": cantidad
#         }
#         productos.append(producto)


# print("Lista de productos cargada desde el archivo:\n")
# for producto in productos:
#     print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error. 

# productos = []

# with open("productos.txt", "r") as archivo:
#     for linea in archivo:
#         linea = linea.strip()
#         if not linea:
#             continue

#         partes = linea.split(",")
#         if len(partes) != 3:
#             continue

#         nombre = partes[0]
#         precio = float(partes[1])
#         cantidad = int(partes[2])

#         producto = {
#             "nombre": nombre,
#             "precio": precio,
#             "cantidad": cantidad
#         }

#         productos.append(producto)


# print("Lista de productos cargada desde el archivo:\n")
# for producto in productos:
#     print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")


# print("\n--- Buscar un producto ---")
# nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ").strip()

# encontrado = False 

# for producto in productos:
#     if producto["nombre"].lower() == nombre_buscado.lower():
#         print(f"\n Producto encontrado:")
#         print(f"Nombre: {producto['nombre']}")
#         print(f"Precio: ${producto['precio']}")
#         print(f"Cantidad: {producto['cantidad']}")
#         encontrado = True
#         break

# if not encontrado:
#     print("\n El producto no existe en la lista.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista. 

# productos = []

# with open("productos.txt", "r") as archivo:
#     for linea in archivo:
#         linea = linea.strip()
#         if not linea:
#             continue

#         partes = linea.split(",")
#         if len(partes) != 3:
#             continue

#         nombre = partes[0]
#         precio = float(partes[1])
#         cantidad = int(partes[2])

#         producto = {
#             "nombre": nombre,
#             "precio": precio,
#             "cantidad": cantidad
#         }

#         productos.append(producto)

# print("Lista de productos cargada:\n")
# for producto in productos:
#     print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

# print("\n--- Actualizar producto ---")
# nombre_buscado = input("Ingrese el nombre del producto a modificar: ").strip()
# nuevo_precio = input("Ingrese el nuevo precio: ").strip()
# nueva_cantidad = input("Ingrese la nueva cantidad: ").strip()

# actualizado = False

# for producto in productos:
#     if producto["nombre"].lower() == nombre_buscado.lower():
#         producto["precio"] = float(nuevo_precio)
#         producto["cantidad"] = int(nueva_cantidad)
#         actualizado = True
#         break

# if actualizado:
#     print("\n Producto actualizado correctamente.")
# else:
#     print("\n No se encontró el producto para actualizar.")

# with open("productos.txt", "w") as archivo:
#     for producto in productos:
#         linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
#         archivo.write(linea)

# print("\n Archivo productos.txt sobrescrito con los datos actualizados.")
