from personagem import Personagem
from relogio import Relogio

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:

        print('''Escolha uma opção:
        [ 1 ] Lazer
        [ 2 ] Trabalho
        [ 3 ] Estudo\n''')

        escolha = int(input('O que você quer fazer? '))
        if escolha == 1:
            print('''\nEscolha uma das opções de lazer:
            [ 1 ] Dormir (8h) // Ir ao restaurante
            [ 2 ] Ir ao parque com a esposa
            [ 3 ] Assistir Netflix\n''')

            lazer = int(input('O que você quer fazer? '))
            if lazer == 1:
                if thiago.dinheiro > 100:
                    relogio.avancaTempo(8, 10)
                    thiago.dormir()
                else:
                    print('Você não tem dinheiro suficiente.')
                    continue
            elif lazer == 2:
                relogio.avancaTempo(3, 30)
                thiago.passear()
            else:
                relogio.avancaTempo(2, 30)
                thiago.netflix()

        print()
        print(relogio)
        print()
        print(thiago)
        print()

        if thiago.saude == 0:
                print('GAME OVER')
                break