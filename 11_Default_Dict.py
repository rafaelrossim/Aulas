"""

Módulo Collections - Default Dict

Ao criar um dicionário utilizando-o, nós informaos um valor padrão(default),
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não hover
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido

doc = https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

#fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['Curso'] = 'Programação essencial em Python'
print(dicionario)

print(dicionario['outro']) #se fosse um dict comum, daria KeyError porém neste caso foi acrescentado uma nova chave com valor padrão ao dicionário ('outro': 0)
print(dicionario) #resultado