from random import  randint

def DecidaPorMim():
    print('Olá, irei sortear um número de 1 até 100. Vamos ver em quantas rodadas você acerta.')


    numero = randint(1, 100)
    numero_usuario = int(input('Chute um número: '))
    contador = 1


    while numero != numero_usuario:
        if numero_usuario > numero:

            numero_usuario = int(input('Chute um número MENOR: '))
            contador +=1
        if numero_usuario < numero:
            numero_usuario = int(input('Chute um número MAIOR: '))
            contador +=1

    print('NA MOSCA, ACERTOU')
    print(f'Você acertou em {contador} tentativas')

DecidaPorMim()