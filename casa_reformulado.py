            if casa == 1:
                if thiago.dinheiro > 70:  # mudanças nos atributos a serem discutidas depois
                    print('\n\nLIMPANDO A COZINHA...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=-10, relacionamento = 10)
                        print('\nVocê deixou a cozinha impecável e até sua esposa elogiou.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=10, dinheiro = -70)
                        print('\nO cano da pia estorou e você chamou um encanador. O conserto custou R$ 70 e você ficou um pouco estressado.')
                        avancar()
                        continue
                else:
                    print('\n\nÉ importante fazer as tarefas domésticas mas você tem outras prioridades no momento, então talvez seja melhor pedir ajuda da sua esposa para dividir as tarefas.')
                    avancar()
                    continue

            elif casa == 2:
                if thiago.saude > 30:
                    print('\n\nLIMPANDO O BANHEIRO')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=-10, relacionamento=20)
                        print('\nO banheiro foi completamente limpo!')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=10, relacionamento=-20)
                        print('\nEnquanto você limpava a privada sua aliança escorregou e caiu do seu dedo. Você explicou a situação para sua esposa mas mesmo assim ela ficou chateada.')
                    avancar()
                    continue
                else:
                    print('\n\nVocê não está saudável o suficiente e nem tem energia para limpar o banheiro agora.')
                    avancar()
                    continue

            elif casa == 3:
                if thiago.estresse < 40:
                    print('\n\nLIMPANDO O QUARTO..')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(relacionamento = 20, estresse=-10)
                        print('\nQuarto completamente limpo.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=-30, relacionamento=10, estresse=40, dinheiro=-50)
                        print('\nA lâmpada do seu quarto queimou, você foi trocar mas caiu do banco e fraturou o braço e teve que ir ao hospital.')
                    continue
                else:
                    print('\n\n Tente se dessestressar primeiro antes de tentar limpar o quarto.')
                    avancar()
                    continue

            elif casa == 4:
                if thiago.relacionamento > 30:
                    print('\n\nLIMPANDO A SALA...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(relacionamento=10, estresse=-10, dinheiro=50)
                        print('\nSala completamente limpa, inclusive você encontrou R$50 que haviam caído do seu bolso e você não se lembrava.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(dinheiro=-20, estresse=20)
                        print('\nAo levantar um dos sofás você notou várias traças comendo o tecido do estofado. O produto de limpeza te custou R$20.')
                    avancar()
                    continue
                else:
                    print('\nSua esposa estava chateada com você e resolveu limpar a sala sozinha enquanto você estava no quarto.')
                    

            elif casa == 5:
                if thiago.dinheiro > 150 :
                    print('\n\nTIRANDO O LIXO...')
                    sleep(2)
                    if opcao != 3:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(estresse=-20, relacionamento = 20)
                        print('\nLixo no lixo. Tirar o lixo de casa te trouxe um paz indescritível.')
                    else:
                        relogio.avancaTempo(1, 1)
                        thiago.atribuirValores(saude=-30, estresse=60, dinheiro=-thiago.dinheiro, relacionamento = ) #aplicar fabs aqui
                        print('\nEnquanto você tirava o lixo um cachorro foi na sua direção, rasgou o saco de lixo e te mordeu. Você teve que ir ao médico e precisou comprar antibióticos.')
                    avancar()
                    continue
                else:
                    print('\n\nHoje não é dia do lixeiro passar.')
                    avancar()
                    continue