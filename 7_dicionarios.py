#acessando informações do dicionario

receita = {'Jan':100, 'Fev':200, 'Mar':300}

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

paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

#O 'não encotrado é usado quando não localiza a chave 'BR' no dict
pais = paises.get('BR', 'Não encontrado')

print(f'Encontrei o pais {pais}')

print(receita)
print(type(receita))

#adicionando informações no dict

#forma1, mais comum
receita['Abr'] = 400
print(receita)

#forma2
novo_dado = {'Mai': 500}
receita.update(novo_dado)
print(receita)

#forma2_1
receita.update({'Mai': 500})
print(receita)

#atualizando valores existentes

#forma1
receita['Mai'] = 550
print(receita)

#forma2
receita.update({'Mai':600})
print(receita)

#deletando uma informação de um dicionario

#forma1, mais comum
receita.pop('Mar')
#ao removermos um obj, o valor do mesmo é retornado com default

#forma2
del receita['Fev']
print(receita)
#neste caso quando deleta o obj, não é retornado nenhum valor

#carrindo de compras

carrinho = []

prod1 = {'nome': 'Playstation 4', 'quantidade' : 1, 'valor' : 2300.00}
prod2 = {'nome': 'God Of War 4', 'quantidade' : 1, 'valor' : 150.00}

carrinho.append(prod1)
carrinho.append(prod2)

print(carrinho)

#limpando todos os dados do dict
d.clear()
print(d)

#metódos de dict

d = dict(a=1, b=2, c=3) #forma não usual de criar um dict
print(f'original {d}')

#copiando dados do dict

#forma1
novo = d.copy()
print(f'copia {novo}')

novo['d'] = 4
print(f'original {d}')
print(f'atualizado {novo}')

#neste caso criei um dict com valor default igual para todos
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

#neste caso estou crianado uma lista de 10 número com o valor default 'novo' para todos
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)