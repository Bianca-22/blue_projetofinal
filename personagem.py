from random import randint

class Personagem():
    def __init__(self):
        self.saude =  self._avalia_saude(0)
        self.relacionamento = 10
        self.dinheiro = 5
        self.estresse = 0
        self.xp = 0

    def _avalia_saude(self,saude):
        if saude < 0:
            print('O Thiago está com pedra no rim!')
            return 0
        return saude

    def aumentar_estresse(self,valor):
        self.estamina += valor

    def diminuir_estresse(self,valor):
        self.estamina -= valor

    def aumentar_saude(self,valor):
        self.saude += valor

    def diminuir_saude(self,valor):
        self.saude -= valor

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
        print(f'''RESULTADOS DO DIA:
    SAÚDE: {self.saude}
    RELACIONAMENTO: {self.relacionamento}
    DINHEIRO: {self.dinheiro}
    ESTRESSE: {self.estresse}
    EXPERIÊNCIA: {self.xp}
        ''')

    def acao_manha(self):
        # métodos das rotinas do período manhã
        manha = randint(1, 4)
        if manha == 1:
            # pode colocar condicional aqui
            # para ver se o personagem pode ou não realizar tal atividade.
            # ex. if self.dinheiro > 2: se o personagem tiver mais de 2 pontos de dinheiro, ele entra na escolha das opções.

            res = int(input('''Você acordou com dor de dente.
        [1] - IR PARA O DENTISTA
        [2] - IR PARA O TRABALHO E TOMAR UM REMÉDIO
        Nessa manhã você gostaria de: '''))
            if res == 1:
                return self.aumentar_saude(2) and self.diminuir_dinheiro(2)
            else:
                return self.diminuir_saude(3) and diminuir_estresse(3) and self.aumentar_dinheiro(1)

        elif manha == 2:
            res = int(input('''Você acordou com fome.
        [1] - COMER HAMBURGUER
        [2] - COMER SANDUICHE NATURAL
        Nessa manhã você gostaria de: '''))
            # condicionais para acrescentar ou diminuir a pontuação dos atributos do personagem.
            if res == 1:
                return self.diminuir_saude(2) and self.diminuir_dinheiro(1)
            else:
                return self.aumentar_saude(1) and self.diminuir_dinheiro(1)

        elif manha == 3:
            res = int(input('''Seu vizinho está com problemas no carro e precisa de ajuda.
        [1] - AJUDAR SEU VIZINHO
        [2] - IR DIRETO PARA O TRABALHO
        Nessa manhã você gostaria de: '''))
            if res == 1:
                return self.aumentar_xp(1) and self.diminuir_estresse(1)
            else:
                return self.aumentar_dinheiro(1) and self.diminuir_relacionamento(1)

        elif manha == 4:
            res = int(input('''Você acordou mais cedo do que de costume.
        [1] - ASSISTIR TV
        [2] - FAZER UMA CORRIDA MATINAL
        Nessa manhã você gostaria de: '''))
            if res == 1:
                return self.aumentar_saude(1) and aumentar_estresse(2)
            else:
                return self.aumentar_saude(1) and diminuir_estresse(2)



