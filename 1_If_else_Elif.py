nome = input ('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
ano = 2021 - idade

if idade <0:
    print(f'A idade tem que ser válida!')
elif idade ==0:
    print(f'A idade tem que ser maior que zero!')
elif idade <18:
    print(f'Bem vindo(a) {nome.title().split()[0]}, você nasceu em {ano} e é menor de idade')
elif idade == 18:
    print(f'Bem vindo(a) {nome.title().split()[0]}, você nasceu em {ano} e tem {idade} anos')
else:
    print(f'Bem vindo(a) {nome.title().split()[0]}, você nasceu em {ano} e é maior de idade')