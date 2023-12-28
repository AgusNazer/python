

frutas = ['banana', 'manzana', 'pera', 'naranja', 'ciruela']
string = 'hola agus'
numeros = [2,4,8,10]

#continue saltea el elemento
for fruta in frutas:
    if fruta == 'pera':
        continue
    print(f'Me voy a comer una: {fruta}')
    
    #break corta el bucle
for fruta in frutas:
    print(f'Me voy a comer una: {fruta}')
    if fruta == 'manzana':
        break
print('bucle terminado')
    
    
for letra in string:
    print(letra.capitalize())
    
    #fopr en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
# print(numeros_duplicados)