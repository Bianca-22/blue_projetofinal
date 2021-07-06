#eduardo_branch

from personagem import Personagem
from relogio import Relogio

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:

        escolha = int(input(('''Escolha uma opção:
        [ 1 ] Lazer
        [ 2 ] Trabalho
        [ 3 ] Estudo
        [ 4 ] Cuidar da casa
        [ 5 ] Projetos pessoais\n
        O que você quer fazer? ''')))

        if escolha == 5:
            projetospessoais = int(input(('''\nEscolha uma das opções de projeto pessoal:
            [ 1 ] Produzir vídeo para o canal do YouTube Thi Code
            [ 2 ] Produzir conteúdo para o Instagram @thi.code
            [ 3 ] Ir para a academia para ficar monstro
            [ 4 ] Desenvolver seu projeto social de ensino gratuito de programação para jovens que será implementado ano que vem
            [ 5 ] \n
            O que você quer fazer? ''')))
            
            if projetospessoais == 1:
                if thiago.saude > 10: #valores de proporção a serem alterados depois
                    relogio.avancaTempo(8, 10)
                    thiago.youtube()
                    
                else:
                    print('Você não está saudável o suficiente para se dedicar a esta ação.')
                    continue

            elif projetospessoais == 2:
                if thiago.relacionamento > 30:
                    relogio.avancaTempo(3, 30)
                    thiago.instagram()
                else:
                    print('Sua esposa não está satisfeita em como você a está tratando e o proibiu de usar o Instagram.')
                    continue

            elif projetospessoais == 3:
                if thiago.dinheiro > 20:
                    relogio.avancaTempo(2, 30)
                    thiago.academia()

                else:
                    print('Você não tem dinheiro suficiente para ir a academia.')
                    continue
            
            elif projetospessoais == 4:
                if thiago.saude > 20:
                    relogio.avancaTempo(5, 30)
                    thiago.projetosocial()
                else:
                    print('Você não está saudável o suficiente para se dedicar a esta ação.')
                    continue

            elif projetospessoais == 5:
                pass

        print()
        print(relogio)
        print()
        print(thiago)
        print()

        if thiago.saude == 0:
                print('GAME OVER')
                break