"""

while é uma expressão booleana que funcionca como um looping e só para quando tem pelo menos uma condição false

"""

numero=1

#loop do 1 a 10
while numero<11:
    print(numero)
    numero=numero+1 #essa a condição que quando o numero for 10 será false o o while acaba

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou jéssica? ')
    if resposta == 'sim':
        break
print('Tabom então!')
