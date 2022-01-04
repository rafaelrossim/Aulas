'''
#acessando informações do dicionario

#forma 1
print(paises['BR'])
print(paises['PY'])

#forma 2 (mais recomendavel)
print(paises.get('BR'))
print(paises.get('ru'))

teste = None
print(f'O tipo teste é {type(teste)} com o valor {teste} ')

teste = 1
print(f'O tipo teste agora é {type(teste)} com o valor {teste}')

teste = 'Rafael Rossim'

print(f'O tipo teste atualizado é {type(teste)} com o valor {teste}')
'
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

#O 'não encotrado é usado quando não localiza a chave 'BR' no dict
pais = paises.get('BR', 'Não encontrado')

print(f'Encontrei o pais {pais}')

'''

receita = {'Jan':100, 'Fev':200, 'Mar':300}
print(receita)

