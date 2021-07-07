from personagem import Personagem
from relogio import Relogio
from random import randint

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:

        opcao = randint(1, 4)

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
            [ 5 ] Jogar vôlei\n
            O que você quer fazer? '''))

            if lazer == 1:

                if thiago.estresse <= 50:
                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=20, estresse=-30)
                        print('Você teve uma revigorante noite de sono!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=5, estresse=10)
                        print(
                            'Os gatos estavam brigando no telhado, o que te fez perder o sono e ficar mais estressado que antes.')

                else:
                    print(
                        'Você está estressado demais e não consegue dormir. Faça algo para te desestressar antes de tentar dormir.')
                    continue

            elif lazer == 2:

                if thiago.xp >= 30 and thiago.dinheiro >= 20:
                    if opcao != 3:
                        relogio.avancaTempo(1, 30)
                        thiago.atribuirValores(saude=10, estresse=-20, relacionamento=20, dinheiro=-20)
                        print(
                            'Você foi caminhar no Parque com a sua esposa e tomou um sorvete com ela! Os dois ficaram muito felizes!')

                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse=10, relacionamento=-20, dinheiro=-20)
                        print('''O passeio com a esposa estava muito divertido até que uma manada de capivaras correu atrás de vocês...
            Você deixou deixou sua esposa para trás, por isso ela ficou muito estressada contigo. Além disso, na volta para casa, você foi assaltado e perdeu todo o dinheiro da carteira.''')

                else:
                    if thiago.xp < 30 and thiago.dinheiro < 20:
                        print('Você ainda não tem dinheiro suficiente nem experiência. Como pode pensar em passear?')
                    elif thiago.dinheiro >= 20:
                        print(
                            'Sua carreira está estagnada, você precisa ganhar um pouco de experiência antes de pensar pensar em sair.')
                    else:
                        print('Você não tem nem R$20,00 na carteira para sair com a sua esposa. Vá trabalhar!')
                    continue

            elif lazer == 3:

                if 21 <= relogio.horas < 24:
                    if opcao != 3:
                        relogio.avancaTempo(2, 5)
                        thiago.atribuirValores(relacionamento=20, estresse=-10)
                        print('Você e sua esposa escolheram um filme ótimo e se divertiram muito juntos!')

                    else:
                        relogio.avancaTempo(1, 10)
                        thiago.atribuirValores(saude=-10, relacionamento=-50, estresse=30)
                        print(
                            'Sua esposa ficou meia hora escolhendo o filme perfeito, mas depois de 40 minutos você não aguentava mais assistir e trocou o filme sem a autorização dela. Ela ficou muito estressada e te colocou para dormir no sofá.')

                else:
                    print(f'Ainda são {relogio.horas:02d}:{relogio.minutos:02d}. Está muito cedo para assistir filme.')
                    continue

            elif lazer == 4:

                if thiago.dinheiro >= 150 and 20 <= relogio.horas < 23:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(relacionamento=100, dinheiro=-150, estresse=-40)
                        print(
                            'Você preparou um lindo jantar à luz de velas para a sua esposa e ela ficou muito muito feliz. O relacionamento agora está renovado!')

                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(saude=-30, relacionamento=30, dinheiro=-thiago.dinheiro, estresse=100)
                        print(
                            'Na tentativa de preparar um jantar romântico para a sua esposa, você acabou se queimando e estragando o fogão. Por isso você perdeu todo o seu dinheiro para consertá-lo e ficou muito estressado por isso.')

                else:
                    if thiago.dinheiro < 150 and 20 <= relogio.horas < 23:
                        print('Ainda está muito cedo e você não tem dinheiro suficiente para preparar o jantar.')
                    elif thiago.dinheiro >= 150:
                        print(
                            f'Acalma o coração. Agora são {relogio.horas:02d}:{relogio.minutos:02d}, não está na hora de jantar.')
                    else:
                        print(f'Como você quer preparar um jantar com apenas R${thiago.dinheiro:.2f}? Vá trabalhar!')
                    continue

            elif lazer == 5:

                if thiago.saude >= 50 and thiago.dinheiro >= 30:
                    if opcao != 3:
                        relogio.avancaTempo(2, 30)
                        thiago.atribuirValores(saude=30, dinheiro=-30, estresse=-50)
                        print(
                            'Você se divertiu muito jogando vôlei com os seu amigos! Ao final do jogo você foi comer com eles e gastou R$ 30,00. Foi uma ótimo momento!')

                    else:
                        relogio.avancaTempo(2)
                        thiago.atibruirValores(saude=-50, dinheiro=-30, estresse=20)
                        print(
                            'Jogo traumático... Ao saltar para dar o corte, você chocou sua cabeça com a de um amigo e ficou desarcordado por vários minutos. Além disso, sua bola furou e você precisa comprar uma nova.')

                else:
                    if thiago.saude < 50 and thiago.dinheiro < 30:
                        print(
                            'Sua saúde não está muito boa para um jogo tão pesado e você não tem nem R$ 30,00 para comer comer com seus amigos após o jogo.')
                    elif thiago.saude >= 50:
                        print(
                            'Seus amigos querem comer após o jogo. Você não vai sair na aba dos outro, né, seu muquirana!?')
                    else:
                        print('Sua saúde está péssima! Procure um médico!')
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
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=20)
                        print("A aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=-30, estresse=30, dinheiro=20)
                        print(
                            "A aula foi um desastre! Houve uma briga entre os alunos que resultou em um grade desconforto na sala. ")
                else:
                    print('Você está fora do horário de aula!')
                    continue

            elif trabalho == 2:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=10)
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
                        thiago.atribuirValores(saude=-10, estresse=30, dinheiro=10)
                        print("Os trabalhos foram corrigidos e os feedbacks foram todos enviados com sucesso.")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=50, dinheiro=-80)
                        print(
                            "Devido a uma chuva forte, seu computador queimou! Sem correção, sem feedbacks e sem computador.")
                else:
                    print('Você está muito cansado para corrigir as atividades. ')
                    continue

            elif trabalho == 4:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=10)
                        print("A lista de exercícios está pronta e atualizada!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, dinheiro=10)
                        print(
                            "Você trocou as matérias das turmas e fez listas erradas para cada turma! Agora é refazer.")
                else:
                    print('Você precisa descansar antes de poder mexer com a lista de exercícios.')
                    continue

            elif trabalho == 5:
                if 18 < relogio.horas < 23:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=20)
                        print("A aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-20, estresse=30, dinheiro=20)
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
