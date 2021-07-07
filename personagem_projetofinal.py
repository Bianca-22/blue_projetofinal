class Personagem:
    def __init__(self, nome='Thiago'):
        self.__nome = nome
        self.__saude = 100
        self.__relacionamento = 100
        self.__dinheiro = 150
        self.__estresse = 0
        self.__xp = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def saude(self):
        return self.__saude

    @property
    def relacionamento(self):
        return self.__relacionamento

    @property
    def dinheiro(self):
        return self.__dinheiro

    @property
    def estresse(self):
        return self.__estresse

    @property
    def xp(self):
        return self.__xp

    def __str__(self):
        return f'''
Seu Status:
Saúde: {self.__saude}
Relacionamento: {self.__relacionamento}
Dinheiro: {self.__dinheiro}
Estresse: {self.__estresse}
Experiência: {self.__xp}
'''

    def _avaliar(self, valor):
        if valor > 100:
            return 100
        elif valor < 0:
            return 0
        else:
            return valor

    def atribuirValores(self, saude = 0, relacionamento = 0, dinheiro = 0, estresse = 0, xp = 0):
        self.__saude += saude
        self.__relacionamento += relacionamento
        self.__dinheiro += dinheiro
        self.__estresse += estresse
        self.__xp += xp
        self.__saude = self._avaliar(self.__saude)
        self.__relacionamento = self._avaliar(self.__relacionamento)
        self.__dinheiro = self._avaliar(self.__dinheiro)
        self.__estresse = self._avaliar(self.__estresse)
        self.__xp = self._avaliar(self.__xp)