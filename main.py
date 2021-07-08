from personagem import Personagem
from relogio import Relogio
from funcoes import *
from random import randint
from time import sleep
from rich import print

relogio = Relogio()
thiago = Personagem()

if __name__ == '__main__':

    while True:
    
        limpar()
        cabecalho()
        thiagoImg()
        avancar()
        limpar()

        cabecalho()
        print(relogio)
        print(f'[bold dodger_blue1]{"SEUS STATUS AGORA SÃO:":^28}[/bold dodger_blue1]')
        print(thiago)

        if thiago.saude == 0:
            print('\n\nGAME OVER')
            break

        # avancar()
        # limpar()

        opcao = randint(1, 4)
        # print(relogio)
        print('''\n\n[italic dark_cyan]Escolha uma das áreas da vida:[/italic dark_cyan]\n
    [ 1 ] Lazer
    [ 2 ] Trabalho
    [ 3 ] Estudo
    [ 4 ] Cuidar da casa
    [ 5 ] Projetos pessoais\n''')
        escolha = int(input('O que você quer fazer? '))

        limpar()
        cabecalho()
        print(relogio)
        print('''[italic dark_cyan]Escolha uma das opções de lazer:[/italic dark_cyan]\n
        [ 1 ] Dormir
        [ 2 ] Caminhar no Parque
        [ 3 ] Assistir HBO Max
        [ 4 ] Jantar Romântico
        [ 5 ] Jogar vôlei\n''')
        if escolha == 1:
            lazer = int(input('O que você quer fazer? '))
            
            #inicio felipe
            if lazer == 1:
                if relogio.horas in [20, 21, 22, 23, 0, 1]:
                    print('\n\nDORMINDO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(6)
                        thiago.atribuirValores(saude=20, estresse=-30)
                        print('\nVocê teve uma revigorante noite de sono!')
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=5, estresse=10)
                        print('\nOs gatos estavam brigando no telhado, o que te fez perder o sono e ficar mais estressado que antes.')
                    avancar()
                    continue
                else:
                    print('\n\nAinda não está na hora de dormir!')
                    avancar()
                    continue

            elif lazer == 2:
                if thiago.dinheiro >= 20:
                    print('\n\nCAMINHANDO NO PARQUE...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 30)
                        thiago.atribuirValores(saude=10, estresse=-20, relacionamento=20, dinheiro=-20)
                        print('\nVocê foi caminhar no Parque com a sua esposa e tomou um sorvete com ela! Os dois ficaram muito felizes!')
                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(estresse=10, relacionamento=-20, dinheiro=-20)
                        print('''\nO passeio com a esposa estava muito divertido até que uma manada de capivaras correu atrás de vocês...
Você deixou deixou sua esposa para trás, por isso ela ficou muito estressada contigo.
Além disso, na volta para casa, você foi assaltado e perdeu os R$ 20,00 que tinha na carteira.''')
                    avancar()
                    continue
                else:
                    print('\n\nVocê não tem nem R$20,00 na carteira para sair com a sua esposa. Vá trabalhar!')
                    avancar()
                    continue

            elif lazer == 3:
                if 21 <= relogio.horas < 24:
                    print('\n\nASSISTINDO FILME...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(relacionamento=20, estresse=-10)
                        print('\nVocê e sua esposa escolheram um filme ótimo e se divertiram muito juntos!')
                    else:
                        relogio.avancaTempo(7, 10)
                        thiago.atribuirValores(saude=-10, relacionamento=-50, estresse=30)
                        print('''\nSua esposa ficou meia hora escolhendo o filme perfeito, mas depois de 40 minutos você não aguentava mais assistir e trocou o filme sem a autorização dela.
Ela ficou muito estressada e te colocou para dormir no sofá.''')
                    avancar()
                    continue
                else:
                    print(f'\n\nEstá muito cedo para assistir filme. Você tem outras coisas mais importantes para fazer antes!')
                    avancar()
                    continue

            elif lazer == 4:
                if thiago.dinheiro >= 150 and 19 <= relogio.horas < 22:
                    print('\n\nPREPARANDO O JANTAR...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(relacionamento=100, dinheiro=-150, estresse=-40)
                        print('\nVocê preparou um lindo jantar à luz de velas para a sua esposa e ela ficou muito muito feliz. O relacionamento agora está renovado!')
                    else:
                        relogio.avancaTempo(2)
                        thiago.atribuirValores(saude=-30, relacionamento=30, dinheiro=-thiago.dinheiro, estresse=100)
                        print('''\nNa tentativa de preparar um jantar romântico para a sua esposa, você acabou se queimando e estragando o fogão.
Por isso você perdeu todo o seu dinheiro para consertá-lo e ficou muito estressado por isso.''')
                    avancar()
                    continue
                else:
                    if thiago.dinheiro < 150 and (not 19 <= relogio.horas < 22):
                        print(f'\n\nAinda está muito cedo e você tem somente R$ {thiago.dinheiro:.2f} para preparar o jantar.')
                    elif thiago.dinheiro >= 150:
                        print(f'\n\nAcalma o coração. Ainda não está na hora de jantar.')
                    else:
                        print(f'\n\nComo você quer preparar um jantar com apenas R$ {thiago.dinheiro:.2f}? Vá trabalhar!')
                    avancar()
                    continue

            elif lazer == 5:
                if thiago.saude >= 50 and thiago.dinheiro >= 30:
                    print('\n\nJOGANDO VÔLEI...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(2, 30)
                        thiago.atribuirValores(saude=30, dinheiro=-30, estresse=-50)
                        print('\nVocê se divertiu muito jogando vôlei com os seu amigos! Ao final do jogo você foi comer com eles e gastou R$ 30,00. Foi uma ótimo momento!')
                    else:
                        relogio.avancaTempo(2)
                        thiago.atibruirValores(saude=-50, dinheiro=-30, estresse=20)
                        print('\nJogo traumático... Ao saltar para dar o corte, você chocou sua cabeça com a de um amigo e ficou desarcordado por vários minutos. Além disso, sua bola furou e você precisa comprar uma nova.')
                    avancar()
                    continue
                else:
                    if thiago.saude < 50 and thiago.dinheiro < 30:
                        print('\n\nSua saúde não está muito boa para um jogo tão pesado e você não tem nem R$ 30,00 para comer com seus amigos após o jogo.')
                    elif thiago.saude >= 50:
                        print('\n\nSeus amigos querem comer após o jogo. Você não vai sair na aba dos outro, né, seu muquirana!?')
                    else:
                        print('\n\nSua saúde está péssima! Procure um médico!')
                    avancar()
                    continue
        
        #inicio nikolas
        elif escolha == 2:
            print('''[italic dark_cyan]Escolha uma das opções de trabalho:[/italic dark_cyan]\n
        [ 1 ] Dar aula no Generation Brasil.
        [ 2 ] Preparar o conteúdo das aulas.
        [ 3 ] Corrigir e dar feedback nos trabalhos entregues.
        [ 4 ] Preparar lista de exercícios.
        [ 5 ] Dar aula no Blue EdTech.\n''')
            trabalho = int(input('O que você quer fazer? '))
        
            if trabalho == 1:
                if 8 < relogio.horas < 16:
                    print('\n\nDANDO AULA...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=20)
                        print("\nA aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(8)
                        thiago.atribuirValores(saude=-30, estresse=30, dinheiro=20)
                        print("\nA aula foi um desastre! Houve uma briga entre os alunos que resultou em um grade desconforto na sala.")
                    avancar()
                    continue
                else:
                    print('\n\nVocê está fora do horário de aula!')
                    avancar()
                    continue

            elif trabalho == 2:
                if thiago.saude > 50:
                    print('\n\nPREPARANDO AULA...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=10)
                        print("\nOs conteúdos das aulas estão prontos.")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-20, estresse=30, dinheiro=10)
                        print("\nVocê errou o material da aula e preparou tudo errado!!! Vai ter que refazer.")
                    avancar()
                    continue
                else:
                    print('\n\nVocê está exausto demais para preparar o conteúdo da aula. ')
                    avancar()
                    continue

            elif trabalho == 3:
                if thiago.saude > 50:
                    print('\n\nCORRIGINDO TRABALHOS...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, dinheiro=10)
                        print("\nOs trabalhos foram corrigidos e os feedbacks foram todos enviados com sucesso.")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=50, dinheiro=-80)
                        print("\nDevido a uma chuva forte, seu computador queimou! Sem correção, sem feedbacks e sem computador.")
                    avancar()
                    continue
                else:
                    print('\n\nVocê está muito cansado para corrigir as atividades. ')
                    avancar()
                    continue

            elif trabalho == 4:
                if thiago.saude > 50:
                    print('\n\nPREPARANDO LISTA DE EXERCÍCIOS...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=10)
                        print("\nA lista de exercícios está pronta e atualizada!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=30, dinheiro=10)
                        print("\nVocê trocou as matérias das turmas e fez listas erradas para cada turma! Agora é refazer.")
                    avancar()
                    continue
                else:
                    print('\n\nVocê precisa descansar antes de poder mexer com a lista de exercícios.')
                    avancar()
                    continue

            elif trabalho == 5:
                if 18 < relogio.horas < 23:
                    print('\n\nDANDO AULA...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-10, estresse=10, dinheiro=20)
                        print("\nA aula foi realizada com sucesso!")
                    else:
                        relogio.avancaTempo(4)
                        thiago.atribuirValores(saude=-20, estresse=30, dinheiro=20)
                        print("\nA aula foi péssima. Conteúdo maçante, alunos desinteressados e ninguém aprendeu nada.")
                    avancar()
                    continue
                else:
                    print('\n\nVocê está fora do horário de aula!')
                    avancar()
                    continue
                    
        #elif escolha == 3:
        #inicio bia
        elif escolha == 4:
            print('''[italic dark_cyan]Escolha uma opção de cuidar da casa:[/italic dark_cyan]\n
        [ 1 ] Limpar a cozinha
        [ 2 ] Limpar o banheiro
        [ 3 ] Limpar o quarto
        [ 4 ] Limpar a sala
        [ 5 ] Tirar o Lixo\n''')
            casa = int(input('O que você quer fazer? '))
            
            if casa == 1:
                print('\n\nLIMPANDO A COZINHA...')
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
                avancar()
                continue

            elif casa == 2:
                print('\n\nLIMPANDO O BANHEIRO...')
                sleep(2)
                relogio.avancaTempo(1, 10)
                if opcao != 3:
                    print('\nBanheiro limpo!')
                    thiago.atribuirValores(saude=-1)
                else:
                    print('\nEnquanto você limpava a privada sua aliança escorregou e caiu do seu dedo.')
                    thiago.atribuirValores(saude=-1, relacionamento=-5, estresse=5)
                    print('\nSua mulher ficou chateada e você perdeu pontos de relacionamento.')
                avancar()
                continue

            elif casa == 3:
                print('\n\nLIMPANDO O QUARTO...')
                sleep(2)
                relogio.avancaTempo(1, 30)
                if opcao != 3:
                    print('\nQuarto limpo!')
                    thiago.atribuirValores(saude=-1)
                else:
                    print('\nA Lâmpada do seu quarto queimou, você foi trocar mas caiu do banco e fraturou o braço e teve que ir ao hospital.')
                    relogio.avancaTempo(4, 30)
                    thiago.atribuirValores(saude=-20, estresse=10)
                avancar()
                continue

            elif casa == 4:
                print('\n\nLIMPANDO A SALA...')
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
                avancar()
                continue

            elif casa == 5:
                print('\n\nTIRANDO O LIXO...')
                sleep(2)
                relogio.avancaTempo(0, 30)
                if opcao != 3:
                    print('\n\nLixo no lixo! ;)')
                    thiago.atribuirValores(saude=-1)
                else:
                    relogio.avancaTempo(2, 30)
                    print('\n\nEnquanto você tirava o lixo, um cachorro foi na sua direção e rasgou o saco de lixo e te mordeu.\nVocê vc terá que ir ao médico.')
                    thiago.atribuirValores(saude=-10, estresse=10)
                avancar()
                continue
                    
        #inicio eduardo
        elif escolha == 5:
            print('''[italic dark_cyan]Escolha uma das opções de projeto pessoal:[/italic dark_cyan]\n
        [ 1 ] Produzir vídeo para o canal do Youtube Thi Code
        [ 2 ] Produzir conteúdo para o Instagram @thi.code
        [ 3 ] Ir para a academia para ficar monstro
        [ 4 ] Desenvolver mais um pouco o rascunho do seu projeto social de ensino gratuito de programação para jovens
        [ 5 ] Independência financeira\n''')
            projetospessoais = int(input('O que você quer fazer? '))
            
            if projetospessoais == 1:
                if thiago.saude > 10:  # mudanças nos atributos a serem discutidas depois
                    print('\n\nPRODUZINDO VÍDEO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=-10, xp=10)
                        print('\nVocê fez o roteiro e a gravação para o vídeo em tempo recorde, fluiu muito bem.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=5, estresse=20)
                        print('\nAparentemente o Youtube detectou atividade suspeita na sua conta e o bloqueou mesmo você não tendo feito nada.')
                    avancar()
                    continue
                else:
                    print('\n\nVocê não está saudável e também sem cabeça para se dedicar a escrever roteiro e gravar o vídeo agora.')
                    avancar()
                    continue

            elif projetospessoais == 2:
                if thiago.relacionamento > 30:
                    print('\n\nPRODUZINDO CONTEÚDO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=-10, relacionamento=-10, xp=10)
                        print('\nO post que você fez sobre suas extensões no VSCode alcançou um público grande e gerou vários comentários.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=10, relacionamento=-20, dinheiro=-20)
                        print('\nVocê foi denunciado por plágio e o Instagram te bloqueou para analisar sua conta.')
                    avancar()
                    continue
                else:
                    print('\n\nSua esposa não está satisfeita em como você a está tratando e o proibiu de usar o Instagram. Dê um pouco mais de atenção a ela. Cuide antes de perder.')
                    avancar()
                    continue

            elif projetospessoais == 3:
                if thiago.dinheiro > 20:
                    print('\n\nMALHANDO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=30, relacionamento=-20, estresse=5, dinheiro=-20)
                        print('\nVocê gostou tanto do exercício que está até pensando em disputar um concurso de fisiculturismo ano que vem. Entretanto, sua esposa não gosta de homens musculosos.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=-30, relacionamento=50, estresse=40, dinheiro=-20)
                        print('\nAo fazer o supino você exagerou no peso e a barra de ferro bateu com força no seu peito te fazendo perder todo o ar. Sua esposa ficou preocupada o foi buscar na academia.')
                    continue
                else:
                    print('\n\nVocê não tem dinheiro suficiente para ir a academia.')
                    avancar()
                    continue

            elif projetospessoais == 4:
                if thiago.saude >= 20 and thiago.dinheiro >= 50:
                    print('\n\nAJUDANDO OS JOVENS COM PROGRAMAÇÃO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(relacionamento=10, estresse=10, xp=10, dinheiro=-5)
                        print('\nO projeto está a todo vapor e alguns possíveis parceiros já entraram em contato com você.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(dinheiro=-30, estresse=30)
                        print('\nEm tempos de pandemia é difícil achar parceiros para empreendimentos sociais, e todos os seus contatos o chamaram de louco e pularam fora por querer desenvolver o projeto.')
                    avancar()
                    continue
                else: # MUDANÇA FEITA POR FELIPE
                    if thiago.dinheiro >= 50:
                        print('\n\nVocê não está saudável o suficiente para se dedicar a esta ação.')
                    elif thiago.saude >= 20:
                        print('\n\nVocê tem outras prioridades no momento, talvez devesse começar vendo sua reserva de dinheiro.')
                    else:
                        print('\n\nMuito legal da sua parte em pensar nesse projeto, mas o ideal é que primeiro tente ajeitar um pouco a sua própria vida.')
                    avancar()
                    continue

            elif projetospessoais == 5:
                if thiago.dinheiro > 200:
                    print('\n\nINVESTINDO DINHEIRO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(dinheiro=100, estresse=40)
                        print('\nSeus investimentos no Tesouro Direto e na Bolsa de Valores estão ficando mais sólidos daqui a alguns anos você talvez consiga viver só de renda passiva. Entretanto seus ganhos são proporcionais ao tempo que você tem para administrar os investimentos.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=-10, estresse=60, dinheiro=-thiago.dinheiro, relacionamento=-30)
                        print('\nAplicaram um golpe em você e na verdade seu investimento foi para um esquema de pirâmide. Isso afetou bastante o ambiente na sua casa.')
                    avancar()
                    continue
                else:
                    print('\n\nAntes de pensar em investir, pense em como não perder dinheiro.')
                    avancar()
                    continue
