# craendo un conjunto con set()

conjunto = set(['dato1','dato2'])


#metiendo un conjutno dentro de otro conjunto
conjunto1 = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto1, 'dato3'}
print(conjunto2)

#teoria de conjunto

conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
#comparando tambien se puede verificar
resultado = conjunto2 <= conjunto1

#verificar suoper conjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

print(resultado)