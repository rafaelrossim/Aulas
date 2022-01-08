"""

TUPLAS são representadas por () e definidas por
(4)  -> Não é Tupla
(4,) -> é Tupla
4,   -> é Tupla

"""

#gerando um range de números e colocando em uma variavel
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

tupla1 = (1, 2, 3, 4, 5, 6)
tupla2 = ('Rafael', 'Paraiso', 'Rossim')

nome, sobrenome, sobrenome2 = tupla

print(nome)
print(sobrenome)
print(sobrenome2)

#soma, max, min e tamanho das tuplas
print(f'A soma é {sum(tupla)}')
print(f'O maior número é {max(tupla)}')
print(f'O menor número é {min(tupla)}')
print(f'O tamanho é {len(tupla)}')

#concatenando tuplas
print(f'Junção de tuplas {tupla1 + tupla2}')
print(f'Somente tupla1 {tupla1})')
print(f'Somente tupla2 {tupla2})')

#sobrescrever valores da tupla
tupla1 = tupla1 + tupla2
print(tupla1)