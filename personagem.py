#eduardo_branch

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
        return f'Saúde: {self.__saude}\nRelacionamento: {self.__relacionamento}\nDinheiro: {self.__dinheiro}\nEstresse: {self.__estresse}\n Experiência: {self.__xp}'

    def _avaliar(self, valor):
        if valor > 100:
            return 100
        elif valor < 0:
            return 0
        else:
            return valor

    # def dormir(self):
    #     self.__saude += 20
    #     self.__saude = self._avaliar(self.__saude)
    #     self.__estresse -= 50
    #     self.__estresse = self._avaliar(self.__estresse)

    # def passear(self):
    #     self.__relacionamento += 20
    #     self.__relacionamento = self._avaliar(self.__relacionamento)
    #     self.__estresse -= 20
    #     self.__estresse = self._avaliar(self.__estresse)
    #     self.__saude -= 30
    #     self.__saude = self._avaliar(self.__saude)
    
    # def netflix(self):
    #     self.__estresse -= 20
    #     self.__estresse = self._avaliar(self.__estresse)
    #     self.__relacionamento -= 20
    #     self.__relacionamento = self._avaliar(self.__relacionamento)

    def youtube(self):
        self.__estresse -= 10
        self.__estresse = self._avaliar(self.__estresse)
        self.__xp += 10

    def instagram(self):
        self.__estresse -= 10
        self.__estresse = self._avaliar(self.__estresse)
        self.__xp += 10
        self.__relacionamento -= 10

    def academia(self):
        self.__saude += 30
        self.__saude = self._avaliar(self.__saude)
        self.__relacionamento -= 20
        self.__dinheiro -= 20

    def projetosocial(self):
        self.__relacionamento += 10
        self.__estresse += 10
        self.__xp += 10
