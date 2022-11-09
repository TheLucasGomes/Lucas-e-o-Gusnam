import funcoes


pontos = 0
niveis = []
lista1 = []
ajudas = 3
lista_niveis = funcoes.transforma_base(funcoes.quest)
for k, v in lista_niveis.items():
    if k not in niveis:
        niveis.append(k)
jogador = str(input('Bem vindo ao jogo da EP2 de desoft!\nQual seu nome? '))
print(f'Olá \033[0;35m{jogador}\033[0;m, vamos começar?\n')
while pontos < 1000000:
    if pontos >= 0 and pontos < 6000  and len(niveis) >= 1:
        print(f'Vamos começar com as questões de nivel {niveis[0]}')
        print('\033[0;36mQUESTÃO 1')
        quest1 = funcoes.sorteia_questao_inedida(lista_niveis, 'facil', lista1)
        prints = funcoes.questao_para_texto(quest1, '1')
            
        
            
        
        rus = str(input('Digite qual opção você acha que é a certa:\n Você quer ajuda ou deseja pular?(AJ/P) '))
        if rus == quest1['correta']:
            pontos += 1000
            print(rus)
            print('Certa resposta!')
        elif rus == 'AJ' or rus == 'aj' or rus == 'Aj' or rus == 'aJ':
            ajd = funcoes.gera_ajuda(quest1)
            print(ajd)
            rus2 =str(input('Digite qual opção você acha que é a certa:'))
            if rus2 == quest1['correta']:
                pontos += 1000
                print(rus)
                print('Certa resposta!')
            else:
                print(rus)
                print('Se fodeu')
                break
                
        elif rus == 'P' or rus == 'p':
            print(rus)
            print ('Questão pulada :( ')  
        else:
            print(rus)
            print('Se fodeu')
            break
        