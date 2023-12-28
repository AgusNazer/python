# crear lista con list, no se suele usar
# lista = list(['hola, lista', 35])

lista = (['hola', 'lista', 35])

#devuelve la cantidad de lementos de la lista
cantidad_elementos = len(lista)
print(cantidad_elementos)

#agregar elemento a lista

lista.append('nuevo append')
print(lista)

#agregar con insert

lista.insert(2, 'agregado al indice 2')
print(lista)

#agregar con extend, agerga varios elementos a la lista

lista.extend([False, 'nueva lista'])
print(lista)


lista.pop(3)
print(lista)
lista.insert(3, 35)
print(lista)
lista.remove()

#pop elimina un elemnto, pide indice y devuelve valor
#remove remueve un elemnto de una lista, pide valor
#clear elimina todos los elementos de una lista.
#sort ordena una lista de forma ascendente a descendente
#reverse invierte los elementos de una lista.