#listas em python funciona como vetopres, matrizes (arrays), com a diferença se serem DINAMICOS (não possui tamanho expecifico)
#e também de podermos a colocar QUALQUER tipo de dado (não possui dados fixos).

#as listas são representadas por colchetes: []

lista1 = [5, 1, 99, 4, 27, 15, 22, 3, 1, 5, 44, 42, 27]
lista2 = list('Rafael Paraiso Rossim')
lista3 = []
lista4 = list(range(11))
lista5 = [1, 2.34, True, 'Geek', 'd', lista1, 4534594843841384]
lista6 = [5, 1, 99, 4, 27, 15]
nome = 'Rafael,Paraiso,Rossim'
cores = ['Verde', 'Amarelo', 'Azul', 'Branco']

##econtrar um valor expecífico na lista
#num=7
#if num in lista2:
#    print(f'Encontrei o número {num}')
#else:
#    print(f'Não encontrei o numero {num}')

#adcionar elementos/valores em listas, utilizamos a funcão append e ordenando.
#com o append nós só conseguimos adcionar um elemento por vez
#print(lista1)
#lista1.append(42)               # adicionando 1 valor na lista
#print(lista1.count(1))          # contando e mostrando o valor 1 na lista1
#lista1.append([123, 44, 67])    # adcionando uma sublista na lista
#lista1.extend([123, 44, 67])    # adcionando mais de um valor na lista, extend não aceita valor único
#lista1.insert(2, 'Novo valor')  # adcionando o valor em um indice expecífico, no caso, posição 2
#lista1.sort()                   # ordenando a lista
#lista1.reverse()                # invertendo uma lista
#lista6 = lista1 + lista2        # contatenando uma lista em outra lista
#lista6 = lista1.copy()          # criando a cópia de uma lista
#print(len(lista1))              # verificando o tamanho da lista
#lista1.pop()                    # apagando e retornando o último indice da lista
#lista1.pop(4)                   # apagando e retornando o quarto indice da lista
#lista1.clear()                  # limpando todos os valores da lista
#lista1 = lista1 * 3             # multiplicando três vezes a própria lista
#nome = nome.split()             # convertendo uma string em uma lista
#nome=nome.split(',')            # convertendo uma string em uma lista, separando por virgula
#lista2= ''.join(lista2)         # convertendo lista para string


# mostrando cada elemento de uma lista
#for elemento in lista2:
#    print(elemento)


# soma de todos os elementos de uma lista, funciona também com strings
#soma = 0
#for elemento in lista1:
#    soma=soma + elemento
#print(soma)


#adcionando produtos em um carrinho e mostrando os produtos no final quando o usuario escolher `sair`
#carrinho = []
#produto = ''
#
#while produto != 'sair':
#    print("Adcione um produto na lista ou digite 'Sair': ")
#    produto = input()
#    if produto != 'sair':
#        carrinho.append(produto)
#
#for produto in carrinho:
#    print(produto)

# gerar indice em um for
#for indice, cor in enumerate(cores):
#    print(indice,cor)

# em qual indice da lista está o valor 4
#print(lista1.index(4))

# em qual indice da lista está o valor 4, começando pelo indice 1
#print(lista1.index(5, 1))

#slicing
# lista(inicio:fim:passo)
# range(inicio:fim:passo)
#print(lista1)
#print(lista1[1::2])

#print(sum(lista1)) #soma dos valores da lista
#print(max(lista1)) #maximo valor da lista
#print(min(lista1)) #minimo valor da lista

# desempacotamento de lista
#num1, num2, num3, num4, num5, num6 = lista6
#
#print(num1)
#print(num2)
#print(num3)
#print(num4)
#print(num5)
#print(num6)

#copiando uma lista e acrecendo um valor na nova lista "deep copy" (a cópia não altera o original)
#lista7 = lista6.copy()
#
#print(f'lista7 = {lista7}')
#
#lista7.append(16)
#
#print(f'lista6 = {lista6}')
#print(f'lista7 = {lista7}')

# copiando uma lista via atribuição, ou seja. a alteração é feita para as duas listas (Shallow Copy)
#print(lista6)
#
#lista7 = lista6
#
#print(lista7)
#
#lista7.append(97)
#
#print(lista6)
#print(lista7)