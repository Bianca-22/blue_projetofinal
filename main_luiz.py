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
            estudo = int(input('''\nEscolha  uma das opções de estudo:
        [1] HTML
        [2] PYTHON
        [3] JAVA SCRIPT
        [4] C
        [5] PHP\n
        O que você quer fazer? '''))

            if estudo == 1:

                                
                if opcao != 3:
                    relogio.avancaTempo(8)
                    thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=10)
                    print('Paranbens! Você conseguiu assimilar boa parte do que foi ensinado!')

                else:
                    relogio.avancaTempo(4)
                    thiago.atribuirValores(saude=-10, estresse=-30, relacionamento=0, xp=0)
                    print('Puxa vida! Acabou a energia não vou conseguir assisitir a aula nem estudar!')

                
            elif estudo == 2:

                if thiago.xp >= 20:
                    
                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Você avançou em conhecimento, agora esta aprendendo uma nova liguagem!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=+30, relacionamento=-20, xp=0)
                        print('Meu cachorro mastigou o cabo do meu monitor, não vou conseguir acompanhar a aula! Minha esposa ficou brava por que deixei o cachorro para fora da casa!')

                else:
                    print('Continue estudando para somar cada vez mais conhecimento!')
                    continue

            elif estudo == 3:

                if thiago.xp >= 50:

                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Olha só onde você conseguiu chegar! Continue com essa dedicação e terá muitas boas surpresas!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=+30, relacionamento=-10, xp=-10)
                        print('Puxa vida, derramei um copo de café no meu note e ele não que mais ligar!')

                else:
                    print('Continue estudando para somar cada vez mais conhecimento!')
                    continue

            elif estudo == 4:

                if thiago.xp >= 50:

                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Agora é hora de aplicar tudo que ja aprendeu, e iniciar uma nova joranda com mais uma linguagem!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-30, estresse=+50, relacionamento=-20, xp=-10)
                        print('Invadiram minha residencia e levaram todo meu equipamento de trabalho!')

                else:
                    print('Continue estudando para somar cada vez mais conhecimento!')
                    continue

            if estudo == 5:

                if thiago.xp >= 50:

                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Olha só, somando cada vez mais conhecimento, agora chegou a hora de aumentar sua bagagem!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, relacionamento=20, xp=-10)
                        print('Precisei sair as pressas para levar minha esposa ao médico.')

                else:
                    print('Continue estudando para somar cada vez mais conhecimento!')
                    continue
                   
        if thiago.saude == 0:
            print('GAME OVER')
            break