"""
Lista de reproduccion

Crea un programa para administrar una lista de canciones.

debes solicitar al usuario cuantas canciones desea agregar a la lista y posteriormente ir solicitando cada cancion que dese agregar a la lista

Finalmente debe desplegar la lista de canciones en orden alfabetico.
"""
# Creamos la lista vacia

while True:
    try:
        cantidad_canciones = int(input("Cuantas canciones deseas añadir: "))
        if cantidad_canciones > 0:
            break
        else:
            print("Debes ingresar un numero mayor a 0")
    except ValueError:
        print("Ingresa un valor numerico")

playlist = []

for cancion in range(cantidad_canciones):
    nueva_cancion = input(f"{cancion + 1}. Escribi el nombre de la cancion: ")
    playlist.append(nueva_cancion)

# Ordenar la lista en orden alfabetico. sort
# Si quisieramos que se ordene de forma descendente pondriamos sort(reverse = True)
playlist.sort()

#Mostrar la lista de canciones
print("\nLista de reproduccion")
for i, cancion in enumerate(playlist, 1):
    print(f'{i}. {cancion}')