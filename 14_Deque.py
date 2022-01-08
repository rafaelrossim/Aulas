"""

Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance

Docs = https://docs.python.org/3/library/collections.html#collections.deque

"""

#import
from collections import deque

#criando um deque
deq = deque('Rossim')
print(deq)

#adicionando elementos
#é adicionado no fim da lista
deq.append('Depois') 
print(deq)

#é adicionado no inicio da lista, essa é uma das vantagens dessa collection 
#pois numa lista padrão não tem essa possibildiade
deq.appendleft('Antes') 
print(deq)

#removendo elementos
#é removido e retornado o elemento da última posição
deq.pop()
print(deq) #neste caso remodeu e retornou o elemento 'Depois'

#é removido e retornado o elemento da primeira posição
deq.popleft() #este comando não existe para uma lista comum
print(deq) #neste caso remodeu e retornou o elemento 'Antes'