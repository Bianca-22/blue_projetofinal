from random import randint
from personagem import Personagem

class Acoes(Personagem):

    def acao_manha(self):
        # métodos das rotinas do período manhã
        manha = randint(1,4)
        if manha == 1:
            #pode colocar condicional aqui
            #para ver se o personagem pode ou não realizar tal atividade.
            #ex. if self.dinheiro > 2: se o personagem tiver mais de 2 pontos de dinheiro, ele entra na escolha das opções.

            res =  int(input('''Você acordou com dor de dente.
[1] - IR PARA O DENTISTA
[2] - IR PARA O TRABALHO E TOMAR UM REMÉDIO
Nessa manhã você gostaria de: '''))
            if res == 1:
                return self.aumentar_saude(1) and self.diminuir_dinheiro(2)
            else:
                return self.diminuir_saude(1) and diminuir_estamina(1) and self.aumentar_dinheiro(1)

        elif manha == 2:
            res =  int(input('''Você acordou com fome.
[1] - COMER HAMBURGUER
[2] - COMER SANDUICHE NATURAL
Nessa manhã você gostaria de: '''))
            #condicionais para acrescentar ou diminuir a pontuação dos atributos do personagem.
            if res == 1:
                return self.diminuir_saude(1) and self.diminuir_dinheiro(1)
            else:
                return self.aumentar_saude(1) and self.diminuir_dinheiro(1)

        elif manha == 3:
            res =  int(input('''Seu vizinho está com problemas no carro e precisa de ajuda.
[1] - AJUDAR SEU VIZINHO
[2] - IR DIRETO PARA O TRABALHO
Nessa manhã você gostaria de: '''))
            if res == 1:
                return self.aumentar_xp(1) and self.diminuir_estamina(1)
            else:
                return self.aumentar_dinheiro(1) and self.diminuir_relacionamento(1)

        elif manha == 4:
            res =  int(input('''Você acordou mais cedo do que de costume.
[1] - ASSISTIR TV
[2] - FAZER UMA CORRIDA MATINAL
Nessa manhã você gostaria de: '''))
            if res == 1:
                return self.aumentar_saude(1) and aumentar_estamina(1)
            else:
                return self.aumentar_saude(1) and diminuir_estamina(1)
    
    def acao_tarde(self):
        tarde = randint(1,4)
        if tarde == 1:
            return int(input('Você estava no trabalho e agora está na hora da sua pausa.[1] - \n[2] - \nNessa tarde você gostaria de: '))
        elif tarde == 2:
            return int(input('[1] - \n[2] - \nNessa tarde você gostaria de: '))
        elif tarde == 3:
            return int(input('[1] - \n[2] - \nNessa tarde você gostaria de: '))
        else:
            return int(input('[1] - \n[2] - \nNessa tarde você gostaria de: '))
    
    def acao_noite(self):
        noite = randint(1,4)
        if noite == 1:
            return int(input('[1] - \n[2] - \nNessa noite você gostaria de: '))
        if noite == 2:
            return int(input('[1] - \n[2] - \nNessa noite você gostaria de: '))
        if noite == 3:
            return int(input('[1] - \n[2] - \nNessa noite você gostaria de: '))
        else:
            return int(input('[1] - \n[2] - \nNessa noite você gostaria de: '))