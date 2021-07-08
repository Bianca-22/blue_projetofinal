from tabulate import tabulate

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
        tabelaStatus = [
            ['Saúde:', f'{self.__saude} / 100'],
            ['Relacionamento:', f'{self.__relacionamento} / 100'],
            ['Dinheiro:', f'R$ {self.__dinheiro:.2f}'],
            ['Estresse', f'{self.__estresse} / 100'],
            ['Experiência', self.__xp]]
            
        return tabulate(tabelaStatus, tablefmt="rst")
        
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
        self.__estresse = self._avaliar(self.__estresse)