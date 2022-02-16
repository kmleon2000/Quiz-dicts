"""1. Se tiene un diccionario con 10 items cuyo valor es numérico:
  Crear un script en python que imprima el resultado de la multiplicación de todos los valores. Deben recorrer el diccionario.
  Crear un script en python que imprima los valores duplicados.
  Crear un script en python que elimine del diccionario los valores que sean
"""
#Punto 1

#punto a
def multipy_dict(dict):

  # retorna la multiplicación de los elementos del diccionario
  res = 1
  
  for n in dict.values():
    res *= n
  
  return res

#punto b
def duplicates_dict_val(dict):
  # returna el valor duplicado de cada elemento del diccionario
  #para este use un bucle for dentro de una lista, para que me almacene los valores *2 'x * 2'
  
  res = list()

  for n in dict.values():
    if list(dict.values()).count(n) > 1 and n not in res:
      res.append(n)
  
  return res

#punto c
def delete_dict_multiplies(dict, number):
  # crea un nuevo diccionario, recorre los items en un bucle y examina si no es multiplo del número para agregarlo

  res = {}

  for key, val in dict.items():
    if not val % number == 0:
      res.setdefault(key,val)
  
  return res

number_dict = {
  'one': 23,
  'two': 54,
  'three': 6,
  'four': 32,
  'five': 87,
  'six': 12,
  'seven': 32,
  'eight': 243,
  'nine': 2,
  'ten': 23
}

print(multipy_dict(number_dict))
print(duplicates_dict_val(number_dict))
print(delete_dict_multiplies(number_dict, 2))


"""
2. Crear un script de python que, dados dos diccionarios, genere un tercero con la suma de los items que tengan la misma llave."""
#punto 2

def sum_dicts(dict1, dict2):
  # crea un nuevo diccionario, recorre los items de un diccionario y los compara con los del otro, si sus llaves son iguales, agrega el valor y rompe el ciclo

  final_dict = {}

  for key1, val1 in dict1.items():
    for key2, val2 in dict2.items():
      if key1 == key2:
        final_dict.setdefault(key1, val1 + val2)
        break
  
  return final_dict


number_dict1 = {
  'a': 12,
  'b': 34,
  'e': 45,
  'h': 13,
  'p': 100, 
}

number_dict2 = {
  'b': 28,
  'p': 8,
  'e': 54,
  'n': 42
}

print(sum_dicts(number_dict1, number_dict2))

"""3. Teniendo un diccionario cuyo items tienen como valor un conjunto de letras en tuplas:
  Crear un script de python que  imprima todas las posibles combinaciones de letras que se generen al combinar los elementos de cada tupla.
"""

def get_combinations(dict):
  vals = list()

  for n in list(dict.values())[0]:
    for m in list(dict.values())[1]:
      vals.append(n + m)

  return vals


words = {
  'one': ['a', 'e', 'i', 'o', 'u'],
  'two': ['b', 'c', 'd', 'f', 'h']
}

print(get_combinations(words))