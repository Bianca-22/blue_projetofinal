from personagem_projetofinal import Personagem
from relogio_projetofinal import Relogio

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:
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
                if thiago.saude > 70:
                    relogio.avancaTempo(8)
                    thiago.trabalhar()
                    print("A aula foi realizada com sucesso!")
                else:
                    print('Você está sem energia para dar aula!')
                    continue

            elif trabalho == 2:
                if thiago.saude > 50:
                    relogio.avancaTempo(4)
                    thiago.hora_extra()
                    print("Os conteúdos das aulas estão prontos.")
                else:
                    print('Você está exausto demais para preparar o conteúdo da aula. ')
                    continue

            elif trabalho == 3:
                if thiago.saude > 50:
                    relogio.avancaTempo(4)
                    thiago.hora_extra()
                    print("Os exercícios foram corrigidos e os feedbacks foram enviados.")
                else:
                    print('Você está muito cansado para corrigir as atividades. ')
                    continue

            elif trabalho == 4:
                if thiago.saude > 50:
                    relogio.avancaTempo(4)
                    thiago.hora_extra()
                    print("A aula foi 10!!")
                else:
                    print('Você precisa descansar antes de poder mexer com a lista de exercícios.')
                    continue

            elif trabalho == 5:
                if thiago.saude > 70:
                    relogio.avancaTempo(4)
                    thiago.trabalhar()
                    thiago.dormir()
                    print("A aula foi realizada com sucesso!")
                else:
                    print('Você está sem energia para dar aula!')
                    continue
        print()
        print(relogio)
        print(thiago)
        print()

        if thiago.saude == 0:
            print('GAME OVER')
            break
