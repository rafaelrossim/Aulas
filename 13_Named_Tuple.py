"""

Modulo Collections - Named Tuple

#Recap Tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros

docs = https://docs.python.org/3/library/collections.html#collections.namedtuple

"""

#importando 
from collections import namedtuple

#Para declarar a namedtuple, precisamos definir o nome e parâmentros
#forma1
cachorro = namedtuple('cachorro', 'idade raca nome')

#forma2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

#forma3 - melhor forma
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#estou criando uma variável do tipo cachorro passando os parâmentros necessários
meucachorro = cachorro(idade=5, raca='Vira-lata', nome='billy')
print(meucachorro)

#fazendo acesso
#forma1
print(meucachorro[0]) #idade
print(meucachorro[1]) #raça
print(meucachorro[2]) #nome

#forma2 - Mais usável
print(meucachorro.idade)
print(meucachorro.raca)
print(meucachorro.nome)

#qual index está localizado um valor especifico
print(meucachorro.index('Vira-lata'))

#mostrar quantas ocorrencias tem para um valor especifico
print(meucachorro.count('billy'))