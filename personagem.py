from random import randint

class Personagem():
    def __init__(self):
        self.saude = 10
        self.relacionamento = 10
        self.dinheiro = 5
        self.estresse = 0
        self.xp = 0

    def aumentar_estresse(self,valor):
        self.estamina += valor

    def diminuir_estresse(self,valor):
        self.estamina -= valor

    def _avalia_saude(self):
        if self.saude < 0:
            return False
        return True

    def aumentar_saude(self,valor):
        if self._avalia_saude():
            self.saude += valor
        else:
            return 'THIAGO ESTÁ COM PEDRA NO RIM!'

    def diminuir_saude(self, valor):
        if self._avalia_saude():
            self.saude -= valor
        else:
            return 'THIAGO ESTÁ COM PEDRA NO RIM!'

    def aumentar_relacionamento(self,valor):
        self.relacionamento += valor

    def diminuir_relacionamento(self,valor):
        self.relacionamento -= valor

    def aumentar_dinheiro(self,valor):
        self.dinheiro += valor

    def diminuir_dinheiro(self,valor):
        self.dinheiro -= valor

    def aumentar_xp(self, valor):
        self.xp += valor

    def diminuir_xp(self, valor):
        self.xp -= valor

    def resultados(self):
        print(f'''
RESULTADOS DO DIA:
SAÚDE: {self.saude}
RELACIONAMENTO: {self.relacionamento}
DINHEIRO: {self.dinheiro}
ESTRESSE: {self.estresse}
EXPERIÊNCIA: {self.xp}
        ''')
