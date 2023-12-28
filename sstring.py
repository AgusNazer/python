string1 = 'hola soy la cadena1 34222t45656'
string2 = 'soy la cadena numero2'

print(dir(string1))

# dir devuelve todos los datos disponibles para ese tipo de datos

result_upper = 'tuviejaentanga'.upper()
result_lower = 'tuviejaentanga'.lower()
print(result_upper)

# si es numeriuco devuelve true dsino false

es_numerico = string1.isnumeric()
print(es_numerico)

#edevuelva la cantiad de veces el caracter si hay coincidencias, sino devuelve false
contar_coincidencias = string1.count('z')
print(contar_coincidencias)

#len es una FUNCION que cuentra la cantidad de caracteres de un string dentro de otro string

contar_caracteres = len(string1)
print(contar_caracteres)