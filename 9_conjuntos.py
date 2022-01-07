"""
- Conjuntos em qualquer lingagem de programação, estamos fazendo referencia a teoria dos conjuntos de matemática
- No Python, os conjuntos são chamados de Sets

Dito isto, da mesma forma que a matemática:
- Sets(conjuntos) não possuem valores duplicados;
- Sets(conjutnos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para utilizar quando precisamos armazenar elementos
mas não nos importamos com ordenação deles. Quando não precisamos se preocupar 
com chaves, valores e itens duplicados

Os Conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos(sets) e Mapas(dict)
- Um dict tem chave/valor;
- Um set tem apenas valor;

#Definindo um conjunto(set)

#modo1
s = set({1,2,3,4,5,6,7,7,7,8,9,2,3,4,5,10,10,10,11}) 
print(s)
print(type(s))
#OBS: ao imprimir a lista o Python ignorou os valores duplicados e ordenou o resultado
#e não terá erro

#modo2 - mais usável
s = {1,2,3,4,5,6,7,7,7,8,9,2,3,4,5,10,10,10,11}
print(s)
print(type(s))

#convertendo uma lista em um conjunto(set)
lista = [1,2,3,4,5,6,7,7,7,8,9,2,3,4,5,10,10,10,11]

print(lista)
print(type(lista))

conv = set(lista)
print(conv)
print(type(conv))
#a mesma lógica serve para converter tuplas e strings

#verificando se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

#listas aceitam valores duplicados por isso 19 elementos
lista = [1,2,3,4,5,6,7,7,7,8,9,2,3,4,5,10,10,10,11]
print(f'Lista {lista} com {len(lista)} elementos')

#tuplas aceitam valores duplicados por isso 19 elementos
tupla = 1,2,3,4,5,6,7,7,7,8,9,2,3,4,5,10,10,10,11
print(f'tupla {tupla} com {len(tupla)} elementos')

#dicionario não aceitam chaves duplicadas por isso 11 elementos
dicionario = {}.fromkeys([1,2,3,4,5,6,7,7,7,8,9,2,3,4,5,10,10,10,11], 'dict')
print(f'dicionário = {dicionario} com {len(dicionario)} elementos')

#conjunto não aceitam valores duplicados por isso 11 elementos e é ordenado de uma foma própria
conjunto = {1,2,3,4,5,6,7,7,7,8,9,2,3,4,5,10,10,10,11}
print(f'Conjunto = {conjunto} com {len(conjunto)} elementos')

#exempo: criar uma lista de visitantes de um museu

#foi criada a lista abaixo porque podem ter visitantes da mesmam cidade, ou seja, valores repetidos
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades)) #descobrindo quantas pessoas visitaram

#descobrindo quantas cidades únicas contém na lista
cid_unicas = set(cidades)
print(f'Na lista contem {(len(cid_unicas))} Cidades únicas, são elas: {cid_unicas}')

"""



