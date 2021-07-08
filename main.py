from personagem import Personagem
from relogio import Relogio
from funcoes import *
from random import randint
from time import sleep

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:
    
        limpar()

        opcao = randint(1, 4)
        print(relogio)
        escolha = int(input('''Escolha uma opção:\n
    [ 1 ] Lazer
    [ 2 ] Trabalho
    [ 3 ] Estudo
    [ 4 ] Cuidar da casa
    [ 5 ] Projetos pessoais\n
    O que você quer fazer? '''))

        limpar()
        print(relogio)
        if escolha == 1:
            lazer = int(input('''Escolha uma das opções de lazer:\n
        [ 1 ] Dormir
        [ 2 ] Caminhar no Parque
        [ 3 ] Assistir HBO Max
        [ 4 ] Jantar Romântico
        [ 5 ] Jogar vôlei\n
        O que você quer fazer? '''))
            
            #inicio felipe
            if lazer == 1:

                if 23 <= relogio.horas < 2:
                    if opcao != 3:
                        relogio.avancaTempo(6)
                        thiago.atribuirValores(saude=20, estresse=-30)
                        print('\nVocê teve uma revigorante noite de sono!')

                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=5, estresse=10)
                        print('\nOs gatos estavam brigando no telhado, o que te fez perder o sono e ficar mais estressado que antes.')
                else:
                    print('\nVocê está estressado demais e não consegue dormir. Faça algo para te desestressar antes de tentar dormir.')
                    avancar()
                    continue

            elif lazer == 2:

                if thiago.xp >= 30 and thiago.dinheiro >= 20:
                    if opcao != 3:
                        relogio.avancaTempo(1, 30)
                        thiago.atribuirValores(saude=10, estresse=-20, relacionamento=20, dinheiro=-20)
                        print('\nVocê foi caminhar no Parque com a sua esposa e tomou um sorvete com ela! Os dois ficaram muito felizes!')

                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse=10, relacionamento=-20, dinheiro=-20)
                        print('''\nO passeio com a esposa estava muito divertido até que uma manada de capivaras correu atrás de vocês...
Você deixou deixou sua esposa para trás, por isso ela ficou muito estressada contigo. Além disso, na volta para casa, você foi assaltado e perdeu todo o dinheiro da carteira.''')

                else:
                    if thiago.xp < 30 and thiago.dinheiro < 20:
                        print('\nVocê ainda não tem dinheiro suficiente nem experiência. Como pode pensar em passear?')
                    elif thiago.dinheiro >= 20:
                        print('\nSua carreira está estagnada, você precisa ganhar um pouco de experiência antes de pensar pensar em sair.')
                    else:
                        print('\nVocê não tem nem R$20,00 na carteira para sair com a sua esposa. Vá trabalhar!')
                    avancar()
                    continue

            elif lazer == 3:

                if 21 <= relogio.horas < 24:
                    if opcao != 3:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(relacionamento=20, estresse=-10)
                        print('\nVocê e sua esposa escolheram um filme ótimo e se divertiram muito juntos!')

                    else:
                        relogio.avancaTempo(1, 10)
                        thiago.atribuirValores(saude=-10, relacionamento=-50, estresse=30)
                        print('\nSua esposa ficou meia hora escolhendo o filme perfeito, mas depois de 40 minutos você não aguentava mais assistir e trocou o filme sem a autorização dela. Ela ficou muito estressada e te colocou para dormir no sofá.')

                else:
                    print(f'\nAinda são {relogio.horas:02d}:{relogio.minutos:02d}. Está muito cedo para assistir filme.')
                    avancar()
                    continue

            elif lazer == 4:

                if thiago.dinheiro >= 150 and 19 <= relogio.horas < 22:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(relacionamento=100, dinheiro=-150, estresse=-40)
                        print('\nVocê preparou um lindo jantar à luz de velas para a sua esposa e ela ficou muito muito feliz. O relacionamento agora está renovado!')

                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(saude=-30, relacionamento=30, dinheiro=-thiago.dinheiro, estresse=100)
                        print('\nNa tentativa de preparar um jantar romântico para a sua esposa, você acabou se queimando e estragando o fogão. Por isso você perdeu todo o seu dinheiro para consertá-lo e ficou muito estressado por isso.')

                else:
                    if thiago.dinheiro < 150 and 19 <= relogio.horas < 22:
                        print('\nAinda está muito cedo e você não tem dinheiro suficiente para preparar o jantar.')
                    elif thiago.dinheiro >= 150:
                        print(f'\nAcalma o coração. Agora são {relogio.horas:02d}:{relogio.minutos:02d}, não está na hora de jantar.')
                    else:
                        print(f'\nComo você quer preparar um jantar com apenas R$ {thiago.dinheiro:.2f}? Vá trabalhar!')
                    avancar()
                    continue

            elif lazer == 5:

                if thiago.saude >= 50 and thiago.dinheiro >= 30:
                    if opcao != 3:
                        relogio.avancaTempo(2, 30)
                        thiago.atribuirValores(saude=30, dinheiro=-30, estresse=-50)
                        print('\nVocê se divertiu muito jogando vôlei com os seu amigos! Ao final do jogo você foi comer com eles e gastou R$ 30,00. Foi uma ótimo momento!')

                    else:
                        relogio.avancaTempo(2)
                        thiago.atibruirValores(saude=-50, dinheiro=-30, estresse=20)
                        print('\nJogo traumático... Ao saltar para dar o corte, você chocou sua cabeça com a de um amigo e ficou desarcordado por vários minutos. Além disso, sua bola furou e você precisa comprar uma nova.')

                else:
                    if thiago.saude < 50 and thiago.dinheiro < 30:
                        print('\nSua saúde não está muito boa para um jogo tão pesado e você não tem nem R$ 30,00 para comer comer com seus amigos após o jogo.')
                    elif thiago.saude >= 50:
                        print('\nSeus amigos querem comer após o jogo. Você não vai sair na aba dos outro, né, seu muquirana!?')
                    else:
                        print('\nSua saúde está péssima! Procure um médico!')
                    avancar()
                    continue
        
        #inicio nikolas
        elif escolha == 2:
            trabalho = int(input('''Escolha uma das opções de trabalho:\n
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
                        print("\nA aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=-30, estresse=30, dinheiro=20)
                        print("\nA aula foi um desastre! Houve uma briga entre os alunos que resultou em um grade desconforto na sala.")
                else:
                    print('\nVocê está fora do horário de aula!')
                    avancar()
                    continue

            elif trabalho == 2:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=10)
                        print("\nOs conteúdos das aulas estão prontos.")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-20, estresse=30, dinheiro=10)
                        print("\nVocê errou o material da aula e preparou tudo errado!!! Vai ter que refazer.")
                else:
                    print('\nVocê está exausto demais para preparar o conteúdo da aula. ')
                    avancar()
                    continue

            elif trabalho == 3:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, dinheiro=10)
                        print("\nOs trabalhos foram corrigidos e os feedbacks foram todos enviados com sucesso.")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=50, dinheiro=-80)
                        print("\nDevido a uma chuva forte, seu computador queimou! Sem correção, sem feedbacks e sem computador.")
                else:
                    print('\nVocê está muito cansado para corrigir as atividades. ')
                    avancar()
                    continue

            elif trabalho == 4:
                if thiago.saude > 50:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=10)
                        print("\nA lista de exercícios está pronta e atualizada!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, dinheiro=10)
                        print("\nVocê trocou as matérias das turmas e fez listas erradas para cada turma! Agora é refazer.")
                else:
                    print('\nVocê precisa descansar antes de poder mexer com a lista de exercícios.')
                    avancar()
                    continue

            elif trabalho == 5:
                if 18 < relogio.horas < 23:
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=20)
                        print("\nA aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-20, estresse=30, dinheiro=20)
                        print("\nA aula foi péssima. Conteúdo maçante, alunos desinteressados e ninguém aprendeu nada.")
                else:
                    print('\nVocê está fora do horário de aula!')
                    avancar()
                    continue
                    
        #elif escolha == 3:
        #inicio bia
        elif escolha == 4:
            casa = int(input('''Escolha uma opção:\n
        [ 1 ] Limpar a cozinha
        [ 2 ] Limpar o banheiro
        [ 3 ] Limpar o quarto
        [ 4 ] Limpar a sala
        [ 5 ] Tirar o Lixo\n
        O que você quer fazer? '''))
            
            if casa == 1:
                print('\nLIMPANDO A COZINHA...')
                sleep(2)
                relogio.avancaTempo(1, 20)

                if opcao != 3:
                    print('\nCozinha limpa!')
                    thiago.atribuirValores(saude=-1)

                else:
                    print('\nO cano da pia estorou, você terá que chamar um encanador para consertar.')

                    if thiago.dinheiro > 70:
                        thiago.atribuirValores(saude=-1, estresse=5, dinheiro=-70)
                        print('\nO encanador consertou o cano e custou R$70 e você ficou um pouco estressado.')

                    else:
                        print('\nVocê não tem dinheiro suficiente para consertar a pia.')
                        thiago.atribuirValores(saude=-1, estresse=10)

            elif casa == 2:
                print('\nLIMPANDO O BANHEIRO...')
                sleep(2)
                relogio.avancaTempo(1, 10)

                if opcao != 3:
                    print('\nBanheiro limpo!')
                    thiago.atribuirValores(saude=-1)

                else:
                    print('\nEnquanto você limpava a privada sua aliança escorregou e caiu do seu dedo.')
                    thiago.atribuirValores(saude=-1, relacionamento=-5, estresse=5)
                    print('\nSua mulher ficou chateada e você perdeu pontos de relacionamento.')

            elif casa == 3:
                print('\nLIMPANDO O QUARTO...')
                sleep(2)
                relogio.avancaTempo(1, 30)

                if opcao != 3:
                    print('\nQuarto limpo!')
                    thiago.atribuirValores(saude=-1)

                else:
                    print('\nA Lâmpada do seu quarto queimou, você foi trocar mas caiu do banco e fraturou o braço e teve que ir ao hospital.')
                    relogio.avancaTempo(4, 30)
                    thiago.atribuirValores(saude=-20, estresse=10)

            elif casa == 4:
                print('\nLIMPANDO A SALA...')
                sleep(2)
                relogio.avancaTempo(1, 0)

                if opcao != 3:
                    print('\nSala limpa!')
                    thiago.atribuirValores(saude=-1)

                else:
                    print('\nEnquanto arrumava a sala você encontrou sua calça que estava com R$50 no bolso!')
                    thiago.atribuirValores(saude=-1, dinheiro=50)
                    print('\nLIMPANDO A SALA...')
                    sleep(2)
                    print('\nA sala está limpa!')

            else:
                print('\nTIRANDO O LIXO...')
                sleep(2)
                relogio.avancaTempo(0, 30)

                if opcao != 3:
                    print('\nLixo no lixo! ;)')
                    thiago.atribuirValores(saude=-1)

                else:
                    relogio.avancaTempo(2, 30)
                    print('\nEnquanto você tirava o lixo, um cachorro foi na sua direção e rasgou o saco de lixo e te mordeu.\nVocê vc terá que ir ao médico.')
                    thiago.atribuirValores(saude=-10, estresse=10)
                    
        #inicio eduardo
        elif escolha == 5:
            projetospessoais = int(input('''Escolha uma das opções de projeto pessoal:\n
        [ 1 ] Produzir vídeo para o canal do Youtube Thi Code
        [ 2 ] Produzir conteúdo para o Instagram @thi.code
        [ 3 ] Ir para a academia para ficar monstro
        [ 4 ] Desenvolver mais um pouco o rascunho do seu projeto social de ensino gratuito de programação para jovens
        [ 5 ] Independência financeira\n
        O que você quer fazer? '''))
            
            if projetospessoais == 1:

                if thiago.saude > 10:  # mudanças nos atributos a serem discutidas depois
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=-10, xp=10)
                        print('\nVocê fez o roteiro e a gravação para o vídeo em tempo recorde, fluiu muito bem.')

                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=5, estresse=20)
                        print('\nAparentemente o Youtube detectou atividade suspeita na sua conta e o bloqueou mesmo você não tendo feito nada.')

                else:
                    print('\nVocê não está saudável e também sem cabeça para se dedicar a escrever roteiro e gravar o vídeo agora.')
                    avancar()
                    continue

            elif projetospessoais == 2:

                if thiago.relacionamento > 30:
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=-10, relacionamento=-10, xp=10)
                        print('\nO post que você fez sobre suas extensões no VSCode alcançou um público grande e gerou vários comentários.')

                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=10, relacionamento=-20, dinheiro=-20)
                        print('\nVocê foi denunciado por plágio e o Instagram te bloqueou para analisar sua conta.')

                else:
                    print('\nSua esposa não está satisfeita em como você a está tratando e o proibiu de usar o Instagram. Dê um pouco mais de atenção a ela. Cuide antes de perder.')
                    avancar()
                    continue

            elif projetospessoais == 3:

                if thiago.dinheiro > 20:
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=30, relacionamento=-20, estresse=5, dinheiro=-20)
                        print('\nVocê gostou tanto do exercício que está até pensando em disputar um concurso de fisiculturismo ano que vem. Entretanto, sua esposa não gosta de homens musculosos.')

                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=-30, relacionamento=50, estresse=40, dinheiro=-20)
                        print('\nAo fazer o supino você exagerou no peso e a barra de ferro bateu com força no seu peito te fazendo perder todo o ar. Sua esposa ficou preocupada o foi buscar na academia.')

                else:
                    print('\nVocê não tem dinheiro suficiente para ir a academia.')
                    avancar()
                    continue

            elif projetospessoais == 4:

                if thiago.saude >= 20 and thiago.dinheiro >= 50:
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(relacionamento=10, estresse=10, xp=10, dinheiro=-5)
                        print('\nO projeto está a todo vapor e alguns possíveis parceiros já entraram em contato com você.')

                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(dinheiro=-30, estresse=30)
                        print('\nEm tempos de pandemia é difícil achar parceiros para empreendimentos sociais, e todos os seus contatos o chamaram de louco e pularam fora por querer desenvolver o projeto.')

                else:
                    if thiago.saude < 20:
                        print('\nVocê não está saudável o suficiente para se dedicar a esta ação.')

                    elif thiago.dinheiro < 50:
                        print('\nVocê tem outras prioridades no momento, talvez devesse começar vendo sua reserva de dinheiro.')

                    elif thiago.saude < 20 and thiago.dinheiro < 50:
                        print('\nMuito legal da sua parte em pensar nesse projeto, mas o ideal é que primeiro tente ajeitar um pouco a sua própria vida. ')
                    avancar()
                    continue

            elif projetospessoais == 5:

                if thiago.dinheiro > 200:
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(dinheiro=100, estresse=40)
                        print('\nSeus investimentos no Tesouro Direto e na Bolsa de Valores estão ficando mais sólidos daqui a alguns anos você talvez consiga viver só de renda passiva. Entretanto seus ganhos são proporcionais ao tempo que você tem para administrar os investimentos.')

                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=-10, estresse=60, dinheiro=-thiago.dinheiro, relacionamento=-30)
                        print('\nAplicaram um golpe em você e na verdade seu investimento foi para um esquema de pirâmide. Isso afetou bastante o ambiente na sua casa.')
                else:
                    print('\nAntes de pensar em investir, pense em como não perder dinheiro.')
                    avancar()
                    continue
        
        avancar()           
        limpar()

        print(relogio)
        print('SEUS STATUS AGORA SÃO:\n')
        print(thiago)

        if thiago.saude == 0:
            print('GAME OVER')
            break

        avancar()
