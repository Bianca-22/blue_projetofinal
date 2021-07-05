from personagem import Personagem
from rotinas import Acoes

if __name__ == "__main__":
    acao = Acoes()
    thiago = Personagem()  #criação do obj thiago
    for dia in range(1,5): #iteração da semana....de segunda a sexta
        if dia == 1: #segunda
            acao.acao_manha() #métodos das rotinas do período manhã
            #acao_tarde() #métodos das rotinas do período tarde
            #acao_noite() #métodos das rotinas do período noite
            acao.resultados()

        elif dia == 2: #terça
            if acao.saude > 0:
                acao.acao_manha()
                # acao_tarde()
                # acao_noite()
                acao.resultados()
            else:
                break

        elif dia == 3: #quarta
            if acao.saude > 0:
                acao.acao_manha()
                # acao_tarde()
                # acao_noite()
                acao.resultados()
            else:
                break

        elif dia == 4: #quinta
            if acao.saude > 0:
                acao.acao_manha()
                # acao_tarde()
                # acao_noite()
                acao.resultados()
            else:
                break

        elif dia == 5: #sexta
            if acao.saude > 0:
                acao.acao_manha()
                # acao_tarde()
                # acao_noite()
                acao.resultados()#médoto para mostrar os atributos do thiago na sexta feira.
                #acao.método de finalizacao
            else:
                break
    print('GAMEOVER')