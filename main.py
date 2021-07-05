from personagem import Personagem

if __name__ == "__main__":

    thiago = Personagem()  #criação do obj thiago
    for dia in range(1,5): #iteração da semana....de segunda a sexta
        if dia == 1: #segunda
            thiago.acao_manha() #métodos das rotinas do período manhã
            #thiago.acao_tarde() #métodos das rotinas do período tarde
            #thiago.acao_noite() #métodos das rotinas do período noite
            thiago.resultados()

        elif dia == 2: #terça
            thiago.acao_manha()
            # thiago.acao_tarde()
            # thiago.acao_noite()
            thiago.resultados()

        elif dia == 3: #quarta
            thiago.acao_manha()
            # thiago.acao_tarde()
            # thiago.acao_noite()
            thiago.resultados()

        elif dia == 4: #quinta
            thiago.acao_manha()
            # thiago.acao_tarde()
            # thiago.acao_noite()
            thiago.resultados()

        elif dia == 5: #sexta
            thiago.acao_manha()
            # thiago.acao_tarde()
            # thiago.acao_noite()
            #thiago.resultados() #médoto para mostrar os atributos do thiago na sexta feira.