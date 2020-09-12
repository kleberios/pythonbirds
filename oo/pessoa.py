class Pessoa:
    def __init__(self, nome, cor='Azul', sexo='F', idade = None, mesada=0):
        self.nome = nome
        self.cor = cor
        self.sexo = sexo
        self.idade = idade
        self.mesada = mesada

    def aumenta_mesada(self):
        self.mesada += 50

    def diminui_mesada(self):
        self.mesada -= 50



p  = Pessoa('Maria', idade=45)
p2 = Pessoa('Bianca', 'Branca', 'M', 32)

print('Atributos da intancia p:')
p.aumenta_mesada()
print (p.cor, p.sexo, p.idade, p.mesada)
p.aumenta_mesada()
print (p.mesada)

print('Atributos da intancia p2:')
print(p2.cor, p2.sexo, p2.idade)
p2.sobrenome = 'Dantas'
print('Sobrenome da ' + p.nome + ' é ' + p2.sobrenome)

print(p.__dict__)
print(p2.__dict__)
del p2.sobrenome
print(p2.__dict__)


