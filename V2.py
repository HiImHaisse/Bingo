import random
def generar():
    return random.randint(1,100)

numeros=[]
bingo=[]

for i in range(8):
    numeros.append(generar())
numeros.sort

def new_bingo():
    return [
        [numeros[0],numeros[1],numeros[2]],
        [numeros[3],'BINGO',numeros[4]],
        [numeros[5],numeros[6],numeros[7]]]


def print_pretty():
    tablero=new_bingo()
    for fila in tablero:
        for valor in fila:
            print(f'{valor:^10}', end='|')
        print()

def reemplazar(i):
    numeros[i]='X'

while True:
    print('Bingo')
    print_pretty()
    x=int(input('Ingresa: \n> '))
    print(numeros) 
    if x in numeros:
        pos= numeros.index(x)
        reemplazar(pos)
    else:
        print('No está en la lista')
