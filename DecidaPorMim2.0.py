

import  random

class ChuteNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()

        while self.tentar_novamente == True:
            if self.valor_do_chute > self.valor_aleatorio:
                print('Chute um valor MENOR: ')
                self.PedirValorAleatorio()
            elif self.valor_do_chute < self.valor_aleatorio:
                print('Chute um valor MAIOR: ')
                self.PedirValorAleatorio()
            else:
                self.tentar_novamente==False
            print('Acertou!!')
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

    def PedirValorAleatorio(self):
        self.valor_do_chute = int(input('Chute um número: '))


chute = ChuteNumero()
chute.Iniciar()