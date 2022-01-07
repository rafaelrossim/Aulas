receita = {'Jan':100, 'Fev':250, 'Marc':400}

#e dicionários são representados por {}
#interar sobre dict, ou seja loop sobre dict

print(receita)

#modo1
for chave in receita:
    print(chave)

#modo2
for chave in receita:
    print(receita[chave])

#modo3
for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

#modo4 - mais usados
for chave in receita.keys():
    print(receita[chave])
    
for valor in receita.values():
    print(valor)

#acessando as chaves do dict
print(receita.keys())

#acessando os valores do dict
print(receita.values())

#desenpacotamento do dict
for chave, valor in receita.items():
    print(f'Chave = {chave} e Valor = {valor}')

#soma, min, max e tamnho dos valores do dict
#isso somente funciona caso os valores sejam int ou float
print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))
