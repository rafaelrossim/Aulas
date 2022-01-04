nome = input ('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
ano = 2021 - idade

#usei "_" pois o enumerate cria indice para cada letra da variavel nome e o "_" neste caso vai ignorar o indice pois quero usar apenas a letra
#for _, letra, in enumerate(nome):
#    print(letra)

#neste caso que não coloquei o "_" o item valor me trouxe o indice e a letra da variavel nome
#for valor in enumerate(nome):
#    print(valor)

#colquei o array 1 para trazer apenas o none, se colocar array 0, vai trazer somente o indice | end='' usei para não pular linha na resposta para o usuario
for valor in enumerate(nome):
    print(valor[1], end='')

#rodando loop quantas vezes o for a idade do usuario
#for n in range(0, idade):
#    print(f'Loop rodando {idade}')