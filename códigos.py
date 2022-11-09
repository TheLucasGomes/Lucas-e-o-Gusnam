import funcoes


pontos = 0
niveis = []

lista_niveis = funcoes.transforma_base(funcoes.quest)
for k, v in lista_niveis.items():
    if k not in niveis:
        niveis.append(k)
jogador = int(input('Bem vindo ao jogo da EP2 de desoft!\nQual seu nome? '))
print(f'Olá \033[0;35m{jogador}\033[0;m, vamos começar?\n')
while pontos < 1000000:
    if pontos == 0 and len(niveis) >= 1:
        print(f'Vamos começar com as questões de nivel {niveis[0]}')
        print('\033[0;36mQUESTÃO 1')
        print('\033[0m-'*30)