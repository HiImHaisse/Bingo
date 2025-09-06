import random,os,time


def generar():
    return random.randint(1,100)

bingo=[]

def print_pretty():
    for fila in bingo:
        for item in fila:
            print(f'{item:^10}',end='|')
        print()
       

def create_tablero():
    numeros=[]
    global bingo
    for i in range(8):
        num= generar()
        while num in numeros:
            num=generar()
        numeros.append(generar())

    numeros.sort()

    bingo=[
            [numeros[0],numeros[1],numeros[2]],
            [numeros[3],'BINGO',numeros[4]],
            [numeros[5],numeros[6],numeros[7]]]
    

create_tablero()
while True: 
    print_pretty()  
    x=int(input('Ingresa: \n> '))
    for rows in range(3):
        for item in range(3):
            if bingo[rows][item]==x:
                bingo[rows][item]='X'
    exes=0
    for rows in bingo:
        for item in rows:
            if item =='X':
                exes +=1
    if exes==8:
        print('Ganaste!')
        break

    time.sleep(1)
    os.system('cls')
