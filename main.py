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

        if escolha == 5:
            projetospessoais = int(input('''\nEscolha uma das opções de projeto pessoal:
            [ 1 ] Produzir vídeo para o canal do Youtube Thi Code
            [ 2 ] Produzir conteúdo para o Instagram @thi.code
            [ 3 ] Ir para a academia para ficar monstro
            [ 4 ] Desenvolver mais um pouco o rascunho do seu projeto social de ensino gratuito de programação para jovens
            [ 5 ] Independência financeira\n
            O que você quer fazer? '''))

            if projetospessoais == 1:

                if thiago.saude > 10: #mudanças nos atributos a serem discutidas depois
                    if opcao == 1:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(estresse = -10, xp = 10)
                        print('Você fez o roteiro e a gravação para o vídeo em tempo recorde, fluiu muito bem.')

                    else:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(saude = 5, estresse = 20)
                        print('Aparentemente o Youtube detectou atividade suspeita na sua conta e o bloqueou mesmo você não tendo feito nada.')

                else:
                    print('Você não está saudável e também sem cabeça para se dedicar a escrever roteiro e gravar o vídeo agora.')
                    continue

            elif projetospessoais == 2:

                if thiago.relacionamento > 30:
                    if opcao == 1:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(estresse = -10, relacionamento = -10, xp = 10)
                        print('O post que você fez sobre suas extensões no VSCode alcançou um público grande e gerou vários comentários.')

                    else:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(estresse = 10, relacionamento = -20, dinheiro = -20)
                        print('Você foi denunciado por plágio e o Instagram te bloqueou para analisar sua conta.')

                else:
                    print('Sua esposa não está satisfeita em como você a está tratando e o proibiu de usar o Instagram. Dê um pouco mais de atenção a ela. Cuide antes de perder.')
                    
            elif projetospessoais == 3:

                if thiago.dinheiro > 20:
                    if opcao == 1:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude = 30, relacionamento = -20, estresse = 5, dinheiro = -20)
                        print('Você gostou tanto do exercício que está até pensando em disputar um concurso de fisiculturismo ano que vem. Entretanto, sua esposa não gosta de homens musculosos.')
                    
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude = -30, relacionamento = 50, estresse = 40, dinheiro = -20)
                        print('Ao fazer o supino você exagerou no peso e a barra de ferro bateu com força no seu peito te fazendo perder todo o ar. Sua esposa ficou preocupada o foi buscar na academia.')

                else:
                    print('Você não tem dinheiro suficiente para ir a academia.')
                    continue

            elif projetospessoais == 4:

                if thiago.saude >= 20 and thiago.dinheiro >= 50 :
                    if opcao == 1:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(relacionamento = 10, estresse = 10, xp = 10, dinheiro = -5)
                        print('O projeto está a todo vapor e alguns possíveis parceiros já entraram em contato com você.')
                    
                    else:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(dinheiro = -30, estresse = 30)
                        print('Em tempos de pandemia é difícil achar parceiros para empreendimentos sociais, e todos os seus contatos o chamaram de louco e pularam fora por querer desenvolver o projeto.')
                
                else:
                    if thiago.saude < 20:
                        print('Você não está saudável o suficiente para se dedicar a esta ação.')
                        continue
                    
                    elif thiago.dinheiro < 50:
                        print('Você tem outras prioridades no momento, talvez devesse começar vendo sua reserva de dinheiro.')
                        continue

            elif projetospessoais == 5:

                if thiago.dinheiro > 200:
                    if opcao == 1:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(dinheiro = 100, estresse = 40)
                        print('Seus investimentos no Tesouro Direto e na Bolsa de Valores estão ficando mais sólidos daqui a alguns anos você talvez consiga viver só de renda passiva. Entretanto seus ganhos são proporcionais ao tempo que você tem para administrar os investimentos.')

                    else:
                        relogio.avancaTempo(1,1)
                        thiago.atribuirValores(saude = -10, estresse = 60, dinheiro = -thiago.dinheiro, relacionamento = -30)
                        print('Aplicaram um golpe em você e na verdade seu investimento foi para um esquema de pirâmide. Isso afetou bastante o ambiente na sua casa.')
                else:
                    print('Antes de pensar em investir, pense em como não perder dinheiro.')

        if thiago.saude == 0:
                print('GAME OVER')
                break