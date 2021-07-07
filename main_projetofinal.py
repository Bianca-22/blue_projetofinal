from random import randint
from personagem_projetofinal import Personagem
from relogio_projetofinal import Relogio

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:
        opcao = randint(1,4)

        escolha = int(input('''
Escolha uma opção:
[ 1 ] Lazer
[ 2 ] Trabalho
[ 3 ] Estudo
[ 4 ] Cuidar da casa
[ 5 ] Projetos pessoais\n
O que você quer fazer? '''))

        if escolha == 1:
            lazer = input(('''\n
            Escolha uma das opções de lazer:
            [ 1 ] Dormir (8h) // Ir ao restaurante
            [ 2 ] Ir ao parque com a esposa
            [ 3 ] Assistir Netflix\n
            O que você quer fazer? '''))

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

        #início parte nikolas
        elif escolha == 2:
            trabalho = int(input('''
Escolha uma das opções de trabalho:
[ 1 ] Dar aula no Generation Brasil.
[ 2 ] Preparar o conteúdo das aulas.
[ 3 ] Corrigir e dar feedback nos trabalhos entregues.
[ 4 ] Preparar lista de exercícios.
[ 5 ] Dar aula no Blue EdTech.\n
O que você quer fazer? '''))

            if trabalho == 1:
                if 8 < relogio.horas < 16:
                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=-10,estresse=10,dinheiro=20)
                        print("A aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=-30, estresse=30, dinheiro=20)
                        print("A aula foi um desastre! Houve uma briga entre os alunos que resultou em um grade desconforto na sala. ")
                else:
                    print('Você está fora do horário de aula!')
                    continue

            elif trabalho == 2:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10,estresse=10,dinheiro=10)
                        print("Os conteúdos das aulas estão prontos.")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-20, estresse=30, dinheiro=10)
                        print("Você errou o material da aula e preparou tudo errado!!! Vai ter que refazer.")
                else:
                    print('Você está exausto demais para preparar o conteúdo da aula. ')
                    continue

            elif trabalho == 3:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10,estresse=30,dinheiro=10)
                        print("Os trabalhos foram corrigidos e os feedbacks foram todos enviados com sucesso.")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=50, dinheiro=-80)
                        print("Devido a uma chuva forte, seu computador queimou! Sem correção, sem feedbacks e sem computador.")
                else:
                    print('Você está muito cansado para corrigir as atividades. ')
                    continue

            elif trabalho == 4:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10,estresse=10,dinheiro=10)
                        print("A lista de exercícios está pronta e atualizada!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, dinheiro=10)
                        print("Você trocou as matérias das turmas e fez listas erradas para cada turma! Agora é refazer.")
                else:
                    print('Você precisa descansar antes de poder mexer com a lista de exercícios.')
                    continue

            elif trabalho == 5:
                if 18 < relogio.horas < 23:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10,estresse=10,dinheiro=20)
                        print("A aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-20,estresse=30, dinheiro=20)
                        print("A aula foi péssima. Conteúdo maçante, alunos desinteressados e ninguém aprendeu nada.")
                else:
                    print('Você está fora do horário de aula!')
                    continue
        print()
        print(relogio)
        print(thiago)
        print()

        if thiago.saude == 0:
            print('GAME OVER')
            break
