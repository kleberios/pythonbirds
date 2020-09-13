"""
Criar uma classe carros
"""
class Motor():
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        return print('Velocidade do veículo está em: ' + str(self.velocidade) + 'Km')

    def frear(self):
        if self.velocidade == 1:
            self.velocidade -= 1
        else:
            self.velocidade -= 2
        str(self.velocidade)
        return print('Velocidade do veículo está em: ' + str(self.velocidade) + 'Km')


class Direcao():
    def __init__(self, direcao='norte'):
        self.direcao = direcao

    def girarDireita(self):
        if self.direcao == 'norte':
            self.direcao = 'leste'
            print ('Veículo virou à direita: ' +self.direcao)
        elif self.direcao == 'leste':
            self.direcao = 'sul'
            print ('Veículo virou à direita: ' +self.direcao)
        elif self.direcao == 'sul':
            self.direcao = 'oeste'
            print('Veículo virou à direita: ' +self.direcao)
        elif self.direcao == 'oeste':
            self.direcao = 'norte'
            print('Veículo virou à direita: ' +self.direcao)

    def girarEsquerda(self):
        if self.direcao == "norte":
            self.direcao = "oeste"
            print ('Veículo virou à esquerda - direção para OESTE.')
        if self.direcao == "oeste":
            self.direcao = "Sul"
            print ('Veículo virou à esquerda - direção para SUL.')
        if self.direcao == "sul":
            self.direcao = "leste"
            print('Veículo virou à esquerda - direção para LESTE.')
        if self.direcao == "leste":
            self.direcao = "norte"
            print('Veículo virou à esquerda - direção para NORTE.')

class Carro():
    def __init__(self):
        self.motor = Motor()
        self.girar = Direcao()

# Instanciando a classe
c1 = Carro()

print('#### DIREÇÃO e VELOCIDADE INCIAICL ########')
c1.motor.acelerar()
print()
print('#### VEICULO EM MOVIMENTO ########')
print()
c1.girar.girarDireita()
print('Direção: ' +str(c1.girar.direcao)+ ', Velocidade: ' +str(c1.motor.velocidade))
print()
c1.girar.girarDireita()
c1.motor.acelerar()
print('Direção: ' +str(c1.girar.direcao)+ ', Velocidade: ' +str(c1.motor.velocidade))
print()
c1.girar.girarDireita()
c1.motor.acelerar()
print('Direção: ' +str(c1.girar.direcao)+ ', Velocidade: ' +str(c1.motor.velocidade))
print()
c1.motor.frear()
c1.girar.girarEsquerda()
print()

print('Direção Final: ' +str(c1.girar.direcao)+ ' e Velocidade Final: ' +str(c1.motor.velocidade))