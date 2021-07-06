from personagem import Personagem
from relogio import Relogio
from random import randint
from time import sleep

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:
        ale = randint(1,10)
        escolha = int(input('''Escolha uma opção:
        [ 1 ] Lazer
        [ 2 ] Trabalho
        [ 3 ] Estudo
        [ 4 ] Cuidar da casa
        [ 5 ] Projetos pessoais\n
        O que você quer fazer? '''))
        if escolha == 4:
            casa =  int(input('''Escolha uma opção:
            [ 1 ] Limpar a cozinha
            [ 2 ] Limpar o banheiro
            [ 3 ] Limpar o quarto
            [ 4 ] Limpar a sala
            [ 5 ] Limpar a varanda
            O que você quer fazer? '''))
            if casa == 1:
                print('LIMPANDO A COZINHA...')
                sleep(2)
                relogio.avancaTempo(1, 20)
                if ale == 5:
                    print('O cano da pia estorou, você terá que chamar um encanador para consertar.')
                    if thiago.dinheiro > 70:
                        thiago.dinheiro -= 70
                        thiago.estresse += 5
                        thiago.saude -= 1
                        print('O encandor consertou o cano e custou R$70 e você ficou um pouco estressado.')
                    else:
                        print('Você não tem dinheiro suficiente para consertar a pia.')
                        thiago.estresse += 10
                        thiago.saude -= 1
                else:
                    print('Cozinha limpa!')
                    thiago.saude -= 1
            elif casa == 2:
                print('LIMPANDO O BANHEIRO...')
                sleep(2)
                relogio.avancaTempo(1, 10)
                if ale == 7:
                    print('Enquanto você limpava a privada sua aliança escorregou e caiu do seu dedo.')
                    thiago.relacionamento -= 10
                    thiago.estresse += 5
                    thiago.saude -= 1
                    print('Sua mulher ficou chateada e você perdeu pontos de relacionamento.')
                else:
                    print('Banheiro limpo!')
                    thiago.saude -= 1
            elif casa == 3:
                print('LIMPANDO O QUARTO...')
                sleep(2)
                relogio.avancaTempo(1, 30)
                if ale == 4:
                    print('A Lâmpada do seu quarto queimou, você foi trocar mas caiu do banco e fraturou o braço e teve que ir ao hospital.')
                    relogio.avancaTempo(4, 30)
                    thiago.saude -= 20
                    thiago.estresse -= 10
                else:
                    print('Quarto limpo!')
                    thiago.saude -= 1
            elif casa == 4:
                print('LIMPANDO A SALA...')
                sleep(2)
                relogio.avancaTempo(1, 0)
                if ale == 10:
                    print('Enquanto arrumava a sala você encontrou sua calça que estava com R$100 no bolso!')
                    thiago.dinheiro += 100
                    thiago.saude -= 1
                    print('LIMPANDO A SALA...')
                    sleep(2)
                    print('A sala está limpa!')
                else:
                    print('Sala limpa!')
                    thiago.saude -= 1
            else:
                print('LIMPANDO A VARANDA...')
                sleep(2)
                relogio.avancaTempo(0, 50)
                if ale == 1:
                    print('...')

        if thiago.saude == 0:
                print('GAME OVER')
                break