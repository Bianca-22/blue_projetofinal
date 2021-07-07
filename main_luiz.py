from personagem import Personagem
from relogio import Relogio

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:

        opcao = randint(1,4)

        escolha = int(input(('''Escolha uma opção: 
        [ 1 ] Lazer
        [ 2 ] Trabalho
        [ 3 ] Estudo
        [ 4 ] Cuidar da casa
        [ 5 ] Projetos pessoais\n
        O que você quer fazer? '''))
        
        elif escolha == 4:
            estudo == int(input('''\nEscolha  uma das opções de estudo:
        [1] HTML
        [2] PYTHON
        [3] JAVA SCRIPT
        [4] C
        [5] PHP\n
        O que você quer fazer? '''))

            if estudo == 1:

                if thiago.estresse >= 50:
                    
                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Você fez uma boa escolha de horario, isso será favorável para seu aprendizado!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, relacionamento=20, xp=-10)
                        print('Seu esforço é notável, porém esse horário comprometerá seu desempenho.')

                else:
                    print('Você está estressado demais para assimilar o que irá estudar. Tente descansar para depois voltar aos estudos.')
                    continue

            elif estudo == 2:

                if thiago.estresse >= 50:
                    
                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Você fez uma boa escolha de horario, isso será favorável para seu aprendizado!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, relacionamento=20, xp=-10)
                        print('Seu esforço é notável, porém esse horário comprometerá seu desempenho.')

                else:
                    print('Você está estressado demais para assimilar o que irá estudar. Tente descansar para depois voltar aos estudos.')
                    continue

            elif estudo == 3:

                if thiago.estresse >= 50:

                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Você fez uma boa escolha de horario, isso será favorável para seu aprendizado!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, relacionamento=20, xp=-10)
                        print('Seu esforço é notável, porém esse horário comprometerá seu desempenho.')

                else:
                    print('Você está estressado demais para assimilar o que irá estudar. Tente descansar para depois voltar aos estudos.')
                    continue

            elif estudo == 4:

                if thiago.estresse >= 50:

                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Você fez uma boa escolha de horario, isso será favorável para seu aprendizado!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, relacionamento=20, xp=-10)
                        print('Seu esforço é notável, porém esse horário comprometerá seu desempenho.')

                else:
                    print('Você está estressado demais para assimilar o que irá estudar. Tente descansar para depois voltar aos estudos.')
                    continue

            if estudo == 5:

                if thiago.estresse >= 50:

                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30, relacionamento=20, xp=20)
                        print('Você fez uma boa escolha de horario, isso será favorável para seu aprendizado!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, relacionamento=20, xp=-10)
                        print('Seu esforço é notável, porém esse horário comprometerá seu desempenho.')

                else:
                    print('Você está estressado demais para assimilar o que irá estudar. Tente descansar para depois voltar aos estudos.')
                    continue
                   
    if thiago.saude == 0:
        print('GAME OVER')
        break