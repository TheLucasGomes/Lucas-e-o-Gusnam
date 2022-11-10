import funcoes

pontos = 0
niveis = []
lista1 = []
ajudas = 3
pulos = 2
cont = 1
key_word = ''
lista_niveis = funcoes.transforma_base(funcoes.quest)
for k, v in lista_niveis.items():
    if k not in niveis:
        niveis.append(k)
jogador = str(input('Bem vindo ao jogo da EP2 de desoft!\nQual seu nome? '))
print(f'Olá \033[0;35m{jogador}\033[0;m, vamos começar?\n')
while pontos < 1000000:
    if pontos == 0:
        print(f'Vamos começar com as questões de nivel {niveis[0]}')
    if 0 <= pontos < 1000:
        print(f'PONTUAÇÃO ATUAL: {pontos}')
        quest1 = funcoes.sorteia_questao_inedida(lista_niveis, 'facil', lista1)
        prints = funcoes.questao_para_texto(quest1, cont)
        while 0 <= pontos < 1000:

            rus = str(input(f'''para dica digite "J" ({ajudas} restantes)
    para pular questão digite "P" ({pulos} restantes)
    para parar o jogo digite "S"\n
    Digite qual opção você acha que é a certa:'''))
            if rus == quest1['correta']:
                pontos = 1000
                print(rus)
                print('Certa resposta!')
                cont += 1
                break
            elif rus == 'S' or rus == 's':
                key_word = 'babana'
                break
            elif key_word == 'babana':
                break
            elif rus == 'J' or rus == 'j':
                if ajudas > 0:
                    ajudas -= 1
                    ajd = funcoes.gera_ajuda(quest1)
                    print(ajd)
                else:
                    print('sem ajudas restantes')
                    print(prints)

            elif rus == 'P' or rus == 'p':
                if pulos > 0:
                    pulos -= 1
                    print(rus)
                    print('Questão pulada :( ')
                    break
                else:
                    print('Acabaram os pulos')
                    print(prints)
            else:
                print(rus)
                print('Errou')
                key_word = 'babana'
                break
            if key_word == 'babana':
                break
    if key_word == 'babana':
        break

    elif 1000 <= pontos < 5000:
        if pontos == 1000:
            print(f'Vamos continuar com as questões de nivel {niveis[1]}')
        if 1000 <= pontos < 5000:
            print(f'PONTUAÇÃO ATUAL: {pontos}')
            quest1 = funcoes.sorteia_questao_inedida(lista_niveis, 'medio', lista1)
            prints = funcoes.questao_para_texto(quest1, cont)
            while 1000 <= pontos < 5000:

                rus = str(input(f'''para dica digite "J" ({ajudas} restantes)
        para pular questão digite "P" ({pulos} restantes)
        para parar o jogo digite "S"\n
        Digite qual opção você acha que é a certa:'''))
                if rus == quest1['correta']:
                    pontos = 1000
                    print(rus)
                    print('Certa resposta!')
                    cont += 1
                    break
                elif rus == 'S' or rus == 's':
                    key_word = 'babana'
                    break
                elif key_word == 'babana':
                    break
                elif rus == 'J' or rus == 'j':
                    if ajudas > 0:
                        ajudas -= 1
                        ajd = funcoes.gera_ajuda(quest1)
                        print(ajd)
                    else:
                        print('sem ajudas restantes')
                        print(prints)

                elif rus == 'P' or rus == 'p':
                    if pulos > 0:
                        pulos -= 1
                        print(rus)
                        print('Questão pulada :( ')
                        break
                    else:
                        print('Acabaram os pulos')
                        print(prints)
                else:
                    print(rus)
                    print('Errou')
                    key_word = 'babana'
                    break
                if key_word == 'babana':
                    break
        if key_word == 'babana':
            break
    if 5000 <= pontos < 10000 and len(niveis) >= 1:
        print(f'PONTUAÇÃO ATUAL: {pontos}')
        quest1 = funcoes.sorteia_questao_inedida(lista_niveis, 'facil', lista1)
        prints = funcoes.questao_para_texto(quest1, cont)
        while 0 <= pontos < 1000 and len(niveis) >= 1:

            rus = str(input(f'''para dica digite "J" ({ajudas} restantes)
            para pular questão digite "P" ({pulos} restantes)
            para parar o jogo digite "S"\n
            Digite qual opção você acha que é a certa:'''))
            if rus == quest1['correta']:
                pontos = 1000
                print(rus)
                print('Certa resposta!')
                cont += 1
                break
            elif rus == 'S' or rus == 's':
                break
            elif rus == 'J' or rus == 'j':
                if ajudas > 0:
                    ajudas -= 1
                    ajd = funcoes.gera_ajuda(quest1)
                    print(ajd)
                else:
                    print('sem ajudas restantes')

            elif rus == 'P' or rus == 'p':
                pulos -= 1
                print(rus)
                print('Questão pulada :( ')
                break
            else:
                print(rus)
                print('Errou')
                break
            break
