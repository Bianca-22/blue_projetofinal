from personagem import Personagem
from relogio import Relogio
from random import randint

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:

        opcao = randint(1,2)

        escolha = int(input('''Escolha uma opção:
        [ 1 ] Lazer
        [ 2 ] Trabalho
        [ 3 ] Estudo
        [ 4 ] Cuidar da casa
        [ 5 ] Projetos pessoais\n
        O que você quer fazer? '''))

        if escolha == 1:
            lazer = int(input('''\nEscolha uma das opções de lazer:
            [ 1 ] Dormir
            [ 2 ] Caminhar no Parque
            [ 3 ] Assistir HBO Max
            [ 4 ] Jantar Romântico
            [ 5 ] Jogo de Tabuleiro\n
            O que você quer fazer? '''))

            if lazer == 1:

                if thiago.estresse <= 50:
                    if opcao == 1:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude = 20, estresse = -30)
                        print('Você teve uma revigorante noite de sono!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude = 5, estresse = 10)
                        print('Os gatos estavam brigando no telhado, o que te fez perder o sono e ficar mais estressado que antes.')

                else:
                    print('Você está estressado demais e não consegue dormir. Faça algo para te desestressar antes de tentar dormir.')
                    continue

            elif lazer == 2:

                if thiago.xp >= 30 and thiago.dinheiro >= 20:
                    if opcao == 1:
                        relogio.avancaTempo(1, 30)
                        thiago.atribuirValores(saude = 10, estresse = -20, relacionamento = 20, dinheiro = -20)
                        print('Você foi caminhar no Parque com a sua esposa e tomou um sorvete com ela! Os dois ficaram muito felizes!')

                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse = 10, relacionamento = -20, dinheiro = -20)
                        print('''O passeio com a esposa estava muito divertido até que uma manada de capivaras correu atrás de vocês...
            Você deixou deixou sua esposa para trás, por isso ela ficou muito estressada contigo. Além disso, na volta para casa, você foi assaltado e perdeu todo o dinheiro da carteira.''')

                else:
                    if thiago.xp < 30 and thiago.dinheiro < 20:
                        print('Você ainda não tem dinheiro suficiente nem experiência. Como pode pensar em passear?')
                    elif thiago.dinheiro >= 20:
                        print('Sua carreira está estagnada, você precisa ganhar um pouco de experiência antes de pensar pensar em sair.')
                    else:
                        print('Você não tem nem R$20,00 na carteira para sair com a sua esposa. Vá trabalhar!')
                    continue
                    
            elif lazer == 3:

                if relogio.horas in [21, 22]:
                    if opcao == 1:
                        relogio.avancaTempo(2, 5)
                        thiago.atribuirValores(relacionamento = 20, estresse = -10)
                        print('Você e sua esposa escolheram um filme ótimo e se divertiram muito juntos!')
                    
                    else:
                        relogio.avancaTempo(1, 10)
                        thiago.atribuirValores(saude = -10, relacionamento = -50, estresse = 30)
                        print('Sua esposa ficou meia hora escolhendo o filme perfeito, mas depois de 40 minutos você não aguentava mais assistir e trocou o filme sem a autorização dela. Ela ficou muito estressada e te colocou para dormir no sofá.')

                else:
                    print(f'Ainda são {relogio.horas:02d}:{relogio.minutos:02d}. Está muito cedo para assistir filme.')
                    continue

            elif lazer == 4:

                if thiago.dinheiro >= 150 and relogio.horas in range(20, 23):
                    if opcao == 1:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(relacionamento = 100, dinheiro = -150, estresse = -40)
                        print('Você preparou um lindo jantar à luz de velas para a sua esposa e ela ficou muito muito feliz. O relacionamento agora está renovado!')
                    
                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(saude = -30, relacionamento = 30, dinheiro = -thiago.dinheiro, estresse = 100)
                        print('Na tentativa de preparar um jantar romântico para a sua esposa, você acabou se queimando e estragando o fogão. Por isso você perdeu todo o seu dinheiro para consertá-lo e ficou muito estressado por isso.')
                
                else:
                    if thiago.dinheiro < 150 and relogio.horas not in range(20, 23):
                        print('Ainda está muito cedo e você não tem dinheiro suficiente para preparar o jantar.')
                    elif thiago.dinheiro >= 150:
                        print(f'Acalma o coração. Agora são {relogio.horas:02d}:{relogio.minutos:02d}, não está na hora de jantar.')
                    else:
                        print(f'Como você quer preparar um jantar com apenas R${thiago.dinheiro:.2f}? Vá trabalhar!')
                    continue            


        if thiago.saude == 0:
                print('GAME OVER')
                break