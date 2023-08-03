import random

def lista_aleatoria(rango_min,rango_max):
    lista = [random.randint(rango_min, rango_max)]
    
    return lista

print(lista_aleatoria(1,10))
