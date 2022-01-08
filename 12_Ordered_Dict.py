"""

Módulo Collection - Ordered Dict é um dicionário que GARANTE a ordem da inserção dos elementos diferente do dicionário comum

docs = https://docs.python.org/3/library/collections.html#collections.OrderedDict

"""
#fazendo import
from collections import OrderedDict

#neste momento a ordem é garantida
dicionario = OrderedDict({'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5})

for chave, valor in dicionario.items():
    print(f'Chave {chave} com valor de {valor}')

#entendendo a diferença do Dict para o Ordered OrderedDict

#Dicionários comum:
dict1 = {'a':1, 'b':2}
dict2 = {'b':2, 'a':1}

print(dict1 == dict2) #true -> pois para o dicionário comum não importa a ordem

#Ordered Dict:
orddict1 = {'a':1, 'b':2}
orddict2 = {'b':2, 'a':1}

print(orddict1 == orddict2) #false -> pois para o Ordered Dict ele já garante a ordenação