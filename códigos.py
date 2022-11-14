import funcoes
from time import sleep

pontos = 0
niveis = []
lista1 = []
lista_verify = []
for c in range(0, len(funcoes.quest)):
    lista_verify.append({})
ajudas = 2
pulos = 3
cont = 1
cont_pontos = 0
key_word = ''
aj = 's'
lista_pontos = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
lista_niveis = funcoes.transforma_base(funcoes.quest)
for k, v in lista_niveis.items():
    if k not in niveis:
        niveis.append(k)
print('verificando questões...')
sleep(2)
if lista_verify == funcoes.valida_questoes(funcoes.quest):
    print('Tudo certo')
else:
    print('\033[0;31mErro encontrado na lista de questões\033[0m')
    exit()
print('\033[0;31mOlá Bem vindo ao jogo da EP2 de desoft!\n\033[0m')
jogador = str(input('\n\033[0;36mQual seu nome?\033[0m '))
print(f'\033[0mOlá \033[0;35m{jogador}\033[0;m\n')
sleep(1)
print(f'responda as perguntas para receber pontos!')
sleep(1)
print('cada pergunta respondida aumenta sua pontuação')
sleep(1)
print('você tem direito a 3 DICAS e 2 PULOS')
sleep(1)
print('o jogo acaba se errar ou chegar aos 1000000 pontos')
sleep(1)
print('vamos começar?\n')
sleep(1)
while pontos < 1000000:
    if pontos == 0:
        print(f'{"-" * 45}\nVamos começar com as questões de nivel \n\033[0;36m{niveis[0]}\n\033[0m\n{"-" * 45}\n')
        sleep(2)
    if 0 <= pontos < 5000:
        print(f'PONTUAÇÃO ATUAL: \033[0;33m{pontos}\033[0m')
        quest1 = funcoes.sorteia_questao_inedida(lista_niveis, 'facil', lista1)
        prints = funcoes.questao_para_texto(quest1, cont)
        while 0 <= pontos < 5000:
            rus = str(input(f'''para dica digite "J" ({ajudas} restantes)
    para pular questão digite "P" ({pulos} restantes)
    para parar o jogo digite "S"\n
    Digite qual opção você acha que é a certa:''')).upper()
            if rus == quest1['correta']:
                pontos = lista_pontos[cont_pontos]
                aj = 's'
                cont_pontos += 1
                print(rus)
                print('Certa resposta!')
                cont += 1
                break
            elif rus == 'S' or rus == 's':
                key_word = 'babana'
                print(f'Parabens {jogador}, você ficou com \033[0;33m{pontos}\033[0m reais\n')
                break
            elif key_word == 'babana':
                break
            elif rus == 'J' or rus == 'j':
                if ajudas > 0 and aj == 's':
                    ajudas -= 1
                    aj = 'n'
                    ajd = funcoes.gera_ajuda(quest1)
                    print(f'\033[0;36m{ajd}\033[0m')
                elif aj == 'n' and ajudas > 0:
                    print('você ja pediu ajuda nesta questão')
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
            elif rus not in 'ABCD':
                print('\033[0;31mescolha uma das opções acima\033[0m')
            else:
                print(rus)
                print('Errou')
                key_word = 'babana'
                break
            if key_word == 'babana':
                break

    elif 5000 <= pontos < 100000:
        if pontos == 5000:
            print(f'{"-" * 47}\nVamos continuar com as questões de nivel \n\033[0;36m{niveis[1]}\n\033[0m\n{"-" * 47}')
            sleep(2)
        if 5000 <= pontos < 100000:
            print(f'PONTUAÇÃO ATUAL: \033[0;33m{pontos}\033[0m')
            quest1 = funcoes.sorteia_questao_inedida(lista_niveis, 'medio', lista1)
            prints = funcoes.questao_para_texto(quest1, cont)
            while 5000 <= pontos < 100000:

                rus = str(input(f'''para dica digite "J" ({ajudas} restantes)
        para pular questão digite "P" ({pulos} restantes)
        para parar o jogo digite "S"\n
        Digite qual opção você acha que é a certa:''')).upper()
                if rus == quest1['correta']:
                    pontos = lista_pontos[cont_pontos]
                    aj = 's'
                    cont_pontos += 1
                    print(rus)
                    print('Certa resposta!')
                    cont += 1
                    break
                elif rus == 'S' or rus == 's':
                    key_word = 'babana'
                    print(f'Parabens {jogador}, você ficou com \033[0;33m{pontos}\033[0m reais\n')
                    break
                elif key_word == 'babana':
                    break
                elif rus == 'J' or rus == 'j':
                    if ajudas > 0 and aj == 's':
                        ajudas -= 1
                        aj = 'n'
                        ajd = funcoes.gera_ajuda(quest1)
                        print(f'\033[0;36m{ajd}\033[0m')
                    elif aj == 'n' and ajudas > 0:
                        print('você ja pediu ajuda nesta questão')
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
                elif rus not in 'ABCD':
                    print('\033[0;31mescolha uma das opções acima\033[0m')
                else:
                    print(rus)
                    print('Errou')
                    key_word = 'babana'
                    break
                if key_word == 'babana':
                    break
    elif 100000 <= pontos < 1000000:
        if pontos == 100000:
            print(f'{"-" * 49}\nVamos continuar com as questões de nivel \n\033[0;36m{niveis[2]}\n\033[0m\n{"-" * 49}')
            sleep(2)
        if 100000 <= pontos < 1000000:
            print(f'PONTUAÇÃO ATUAL: \033[0;33m{pontos}\033[0m')
            quest1 = funcoes.sorteia_questao_inedida(lista_niveis, 'dificil', lista1)
            prints = funcoes.questao_para_texto(quest1, cont)
            while 100000 <= pontos < 1000000:

                rus = str(input(f'''para dica digite "J" ({ajudas} restantes)
        para pular questão digite "P" ({pulos} restantes)
        para parar o jogo digite "S"\n
        Digite qual opção você acha que é a certa:''')).upper()
                if rus == quest1['correta']:
                    pontos = lista_pontos[cont_pontos]
                    aj = 's'
                    cont_pontos += 1
                    print(rus)
                    print('Certa resposta!')
                    cont += 1
                    break
                elif rus == 'S' or rus == 's':
                    key_word = 'babana'
                    print(f'Parabens {jogador}, você ficou com \033[0;33m{pontos}\033[0m reais\n')
                    break
                elif key_word == 'babana':
                    break
                elif rus == 'J' or rus == 'j':
                    if ajudas > 0 and aj == 's':
                        ajudas -= 1
                        aj = 'n'
                        ajd = funcoes.gera_ajuda(quest1)
                        print(f'\033[0;36m{ajd}\033[0m')
                    elif aj == 'n' and ajudas > 0:
                        print('você ja pediu ajuda nesta questão')
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
                elif rus not in 'ABCD':
                    print('\033[0;31mescolha uma das opções acima\033[0m')
                else:
                    print(rus)
                    print('Errou')
                    key_word = 'babana'
                    break
                if key_word == 'babana':
                    break
        if pontos == 1000000:
            print(f'MEUS PARABÉNS \033[0;35m{jogador}\033[0m, VOCÊ VENCEU!!!')
            key_word = 'babana'

    if key_word == 'babana':
        if pontos != 1000000:
            pontos = 0
        jogar = str(input('Você quer jogar(de novo)? S/N '))
        if jogar in 'Ss':
            cont_pontos = 0
            aj = 's'
            pontos = 0
            pulos = 3
            ajudas = 2
            key_word = 'ba'
        else:
            print(f'Volte sempre \033[0;35m{jogador}\033[0m!')
            break
