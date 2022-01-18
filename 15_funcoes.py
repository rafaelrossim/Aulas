
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