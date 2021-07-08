from personagem import Personagem
from relogio import Relogio
from random import randint

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:

        opcao = randint(1,4)

        escolha = int(input('''Escolha uma opção: 
        [ 1 ] Lazer
        [ 2 ] Trabalho
        [ 3 ] Estudo
        [ 4 ] Cuidar da casa
        [ 5 ] Projetos pessoais\n
        O que você quer fazer? '''))
        
        if escolha == 3:
            print('''\n\n[italic dark_cyan]Escolha  uma das opções de estudo:[/italic dark_cyan]\n
            [1] HTML
            [2] PYTHON
            [3] JAVA SCRIPT
            [4] C
            [5] PHP\n''')
            estudo = int(input(' O que você quer fazer? '''))

            if estudo == 1:
                print('\n\nESTUDANDO...')
                sleep(2)
                if opcao != 3:
                    relogio.avancaTempo(4)
                    thiago.atribuirValores(estresse=15, relacionamento=20, xp=5)
                    print('\nParabéns! Você conseguiu assimilar boa parte do que foi ensinado!')
                else:
                    relogio.avancaTempo(2)
                    thiago.atribuirValores(estresse=30)
                    print('\nPuxa vida! Acabou a energia e você não conseguiu assisitir a aula nem estudar!')
                    avancar()
                    continue
                
            elif estudo == 2:
                if thiago.xp >= 20:
                    print('\n\nESTUDANDO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(estresse=15, xp=10)
                        print('\nVocê avançou em conhecimento, agora está aprendendo uma nova liguagem!')
                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse=30, relacionamento=-20)
                        print('\nO cachorro mastigou o cabo do monitor e você não conseguiu acompanhar a aula! Sua esposa ficou brava porque você colocou o cachorro para fora de casa!')
                    avancar()
                    continue
                else:
                    print('\n\nVocê ainda não tem experiência suficiente para estudar isso! Continue estudando para somar cada vez mais conhecimento!')
                    avancar()
                    continue

            elif estudo == 3:
                if thiago.xp >= 40:
                    print('\n\nESTUDANDO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(estresse=15, xp=20)
                        print('\nOlha só onde você conseguiu chegar! Continue com essa dedicação e terá muitas boas surpresas!')
                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse=30, dinheiro=-150)
                        print('\nPuxa vida, você derramou um copo de café no notebook e ele não que mais ligar!')
                    avancar()
                    continue
                else:
                    print('\n\nVocê ainda não tem experiência suficiente para estudar isso! Continue estudando para somar cada vez mais conhecimento!')
                    avancar()
                    continue

            elif estudo == 4:
                if thiago.xp >= 80:
                    print('\n\nESTUDANDO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(estresse=15, xp=40)
                        print('\nSua jornada com essa nova linguagem está sendo incrível!')
                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse=50, dinheiro=-1500)
                        print('\nInvadiram sua residência e levaram todo seu equipamento de trabalho!')
                    avancar()
                    continue
                else:
                    print('\n\nVocê ainda não tem experiência suficiente para estudar isso! Continue estudando para somar cada vez mais conhecimento!')
                    avancar()
                    continue

            if estudo == 5:
                if thiago.xp >= 160:
                    print('\n\nESTUDANDO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(estresse=15, xp=80)
                        print('\nParabéns!! Se continuar assim você vai longe!')
                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse=30, relacionamento=20)
                        print('\nSua esposa se sentiu mal e você precisou sair às pressas para levá-la ao hospital.')
                    avancar()
                    continue
                else:
                    print('\n\nVocê ainda não tem experiência suficiente para estudar isso! Continue estudando para somar cada vez mais conhecimento!')
                    avancar()
                    continue

        if thiago.saude == 0:
            print('GAME OVER')
            break