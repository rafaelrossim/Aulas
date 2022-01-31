# definindo uma função
def hello():
    print("hello!!")


# utilizando a função
hello()


def cantar_parabens():
    print("Parabéns para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida!!")
    print("---------------------")


# utilizando uma vez
cantar_parabens()

# utilizando varias vezes
for n in range(5):
    cantar_parabens()

# Utilizando a função em uma variável. Não é tão utitizável, mas é possível
canta = cantar_parabens  # neste caso não precisa do parenteses

# executando a variavel que recebeu a função
canta()


# funcão com retorno
def hello():
    return 'Oi '


# utilizando a funcao com retorno
nome = input('Qual seu nome? ')
print(hello() + nome + "!")


# retornando varios resultados
def nova_funcao():
    var = True  # neste caso vai retornar 4
    # var = None # neste caso vai retornar 3.2
    # var = False # neste caso vai retornar b
    if var:
        return 4
    elif var is None:
        return 3.2
    return "b"


print(nova_funcao())

from random import random


# exemplo 1
def joga_moeda():
    # gera um núero pseudo-randomico, ou seja, pode se repetir, entre 0 e 1
    valor = random()
    if valor > 0.5:
        return f'{valor:.1}, Cara'
    return f'{valor:.1}, Coroa'


print(joga_moeda())


# exemplo 2
def joga_outra_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_outra_moeda())


# funcoes com parametros
def quadrado(numero):
    return numero * numero


print(quadrado(7))
print(quadrado(5))
print(quadrado(9))


# funcoes com mais de um parametro
def multiplica(num1, num2):
    return num1 * num2


# funcoes com parametro padrao/opcional
def exponencial(numero, potencia=2):  # ao informar o valor delfaut (=2) o parametro se torna opcional
    return numero ** potencia


print(exponencial(5))  # usando o valor opcional
print(exponencial(5, 3))  # sobrescrevendo o valor opcional


def mostra_informacao(name='Rossim', instrutor=False):
    if name == 'Rossim' and instrutor:
        return 'Bem vindo instrutor'
    elif name == 'Rossim':
        return 'Eu pensei que você era instrutor'
    return f'Olá {name}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Rafael'))
print(mostra_informacao(name='Rafael'))

# variaveis globais e locais

# exemplo 1
intrutor = 'Rossim'  # variavel global


def aula():
    instrutor = 'Python'  # neste caso estou apenas substituindo variavel global
    return f'{instrutor}'


print(aula())

# exemplo 2
total = 0  # variavel global


def incrementa():
    global total  # é necessário utilziar a variavel global, pois irei fazer uma operação matematica.
    total = total + 1
    return total


print(incrementa())


# entendendo args

# exemplo1


def soma_todos_numeros(n1, n2, n3):
    return n1 + n2 + n3


print(soma_todos_numeros(1, 2, 3))


# refatorando o exemmplo1
def soma_todos_numeros_ref(*args):
    return sum(args)  # o retorno do args é sempre uma tupla, por isso usei o 'sum'


# por utilizar o args como parametro da função, posso usar quantos argumentos forem necessários (inteiro ou real)
print(soma_todos_numeros_ref())
print(soma_todos_numeros_ref(1))
print(soma_todos_numeros_ref(1, 2))
print(soma_todos_numeros_ref(1, 2, 3))
print(soma_todos_numeros_ref(1, 2, 3, 4))


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# print(soma_todos_numeros(numeros))  # exemplo erraco (TypeError)
print(f'a soma é de {soma_todos_numeros(*numeros)}')  # usei o * para desempacotar uma coleção de dados


# entendo o **kwargs


def cor_favorita(**kwargs):  # o kwargs cria um dicionário
    for pessoa, cor in kwargs.items():
        print(f'a cor da forita de {pessoa.title()} é {cor}')


# o kwargs exige que os argumentos sejam nomeados
cor_favorita(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


def cumprimento_especial(**kwargs):
    if 'rossim' in kwargs and kwargs['rossim'] == 'Python':
        return 'Você recebeu um cumprimento paythônico!'
    elif 'rossim' in kwargs:
        return f"{kwargs['rossim']} Geek!"
    return 'Não tenho certeza quem você é!'


print(cumprimento_especial())
print(cumprimento_especial(rossim='Python'))
print(cumprimento_especial(rossim='oi'))
print(cumprimento_especial(rossim='especial'))


# ordem de paramentros em uma funcão
# parâmentrod obrigatórios
# *args
# parâmetros default(não obrigatórios)
# **kwargs


def minha_funcao(name, idade, *args, solteiro=False, **kwargs):
    print(f'{name} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao('rafael', 31)
minha_funcao('fulano', 22, 4, 5, 6, solteiro=True)
minha_funcao('ciclano', 10, eu='não', voce='vai')
minha_funcao('beltrano', 19, 9, 4, 3, java=False, Python=True)


# desempacotando com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'rafael', 'sobrenome': 'rossim'}

print(mostra_nomes(**nomes).title())  # desempacotando com duplos asteriscos


# pode usar o *variavel ou **variavel mesmo não colocando o *args, ou **kwargs nos parametros
def soma_numeros(n1, n2, n3):
    print(n1 + n2 + n3)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_numeros(*lista)
soma_numeros(*tupla)
soma_numeros(*conjunto)

dicionario = dict(n1=1, n2=2, n3=3)  # a chave do diconario devem ser os mesmos dos parametros da função

soma_numeros(**dicionario)
