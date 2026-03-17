"""
! Listas en Python

? Las listas son colecciones ordenadas y mutables de elmetnos que pueden ser de diferentes tipos.
? Las listas son dinamicas, lo que significa que pueden cambiar de tamaño, podemos añadir, modificar o eliminar elementos

"""

# Sintaxis listas:
# definimos la variable que va a almacenar la lista, y usamos corchetes, de manera interna empezamos a agregar elementos separados por comas
elemento1, elemento2, elemento3 = 0, 0, 0
mi_lista = [elemento1, elemento2, elemento3]

# Ejemeplos de litas

numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza", "naranja"]
mixta = [1, "dos", 3.0, [4,5]]


print("*** Manejo de listas ***")

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista [1] = 10
print(mi_lista[1])

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agrego el elemento 6')

# Agregar un nuevi elemento en un indice especifico
# El primer parametro es el indice, una vez q insertemos el elemento todos los otros indices se van a desplazar a la derecha
# de segundo parametro el valor a insertar
mi_lista.insert(2, 15)
print(mi_lista)

# Eliminar elementos de una lista
# usando el metodo remove
"""
Busca el primer elemento de la lista que coincida con valor

Lo elimina

Modifica la lista original (no devuelve una nueva)
"""
mi_lista.remove(5)
print(mi_lista)

#Removemos por indice con el metodo pop
mi_lista.pop(1) # Remueve el elmento del indice 1
print(f'{mi_lista} Se elimino el indice 1')

# Eliminar usando la palabra del, indicamos el nombre de la lista y el indice
del mi_lista[2]
print(f'{mi_lista} -> se elimino el indice 2')

# Obtener sublistas
sublista = mi_lista[1:3] # Genera una sublista del indice 1 al 2(3 no se incluye)
print(f'{sublista} -> Nueva lista')