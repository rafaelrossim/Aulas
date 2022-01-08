"""
Módulo collections = Counter (contador)

Counter - Recebe um interável como parámetro e cria um objeto do tipo Collections Counter que é parecido com dicionário,
contendo como chave, o elemento da lista passada como parâmetro e como valor, a quantidade de ocorrências desses elementos

doc = https://docs.python.org/3/library/collections.html#collections.Counter
"""

#realizando import 
from collections import Counter

#exemplo1
#podemos usar qualquer tipo de iterável, aqui usamos uma lista
lista = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 44 ,5 ,5 ,5 ,56, 6, 6, 7, 7, 7, 7, 23 ,2, 5, 78, 78, 4, 8, 7, 84, 48]

#utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

#exemplo2
#contando uma string
print(Counter('Rafael Rossim'))

#exemplo3
texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit, culpa qui officia deserunt mollit anim id
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

#separando as palavras
palavras = texto.split()

#contando as palavras
res = Counter(palavras)
print(res)

#mostrando as 5 palavras mais comum do texto
print(f'As mais comuns são {res.most_common(5)}') #está função já ordena o resultado do maior para o menor
