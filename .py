import random
def generar():
    return random.randint(1,100)

numeros=[]
bingo=[]

for i in range(8):
    numeros.append(generar())
numeros.sort
bingo=[[numeros[0],numeros[1],numeros[2]],
       [numeros[3],'BINGO',numeros[4]],
       [numeros[5],numeros[6],numeros[7]]]
def print_pretty():
    for fila in bingo:
        for valor in fila:
            print(f'{valor:^10}', end='|')
        print()


while True:
    print('Bingo')
    print_pretty()
    x=input('Ingresa: \n> ')
