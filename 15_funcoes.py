#definindo uma função
def hello():
    print("hello!!")

#utilizando a função
hello()

def cantar_parabens():
    print("Parabéns para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida!!")
    print("---------------------")

#utilizando uma vez
cantar_parabens()

#utilizando varias vezes
for n in range(5):
    cantar_parabens()

#utilizando a função em uma variável. Não é tão utitizável mas é possível
canta = cantar_parabens #neste caso não precisa do parenteses

#executando a variavel que recebeu a função
canta()

#funcão com retorno
def hello():
    return('Oi ')

#utilizando a funcao com retorno
nome = input('Qual seu nome? ')
print(hello() + nome + "!")

#retornando varios resultados
def nova_funcao():
    var = True # neste caso vai retornar 4
    #var = None # neste caso vai retornar 3.2
    #var = False # neste caso vai retornar b
    if var:
        return 4
    elif var is None:
        return 3.2
    return "b"

print(nova_funcao())

from random import random

#exemplo 1
def joga_moeda():
    #gera um núero pseudo-randomico, ou seja pode se repetir, entre 0 e 1
    valor = random()
    if valor > 0.5:
        return (f'{valor:.1}, Cara')
    return (f'{valor:.1}, Coroa')

print (joga_moeda())

#exemplo 2
def joga_outra_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print (joga_outra_moeda())

# funcoes com parametros
def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(5))
print(quadrado(9))


# funcoes com mais de um parametro
def multiplica(num1, num2):
    return num1 * num2