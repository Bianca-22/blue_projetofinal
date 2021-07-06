
def alterarAtributo(saude = 0, relacionamento = 0, dinheiro = 0, estresse = 0, xp = 0):
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