print(f'*** Iterar listas ***')

nombres = ['Karla', 'Juan', 'Laura']

for nombre in nombres:
    print(nombre)

lista_heterogenea = [100, True, 'Ivonne']
print()
for elemento in lista_heterogenea:
    print(elemento)

lista_heterogenea.append([135, 275])
print(lista_heterogenea)

for elemento in lista_heterogenea:
    print(elemento)