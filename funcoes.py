from random import randint
from time import sleep


def transforma_base(l):
    result = {}
    if l == []:
        return {}
    else:
        for c in range(0, len(l)):
            for k, v in l[c].items():
                if k == 'nivel':
                    if v not in result:
                        result[v] = []
        for q in range(0, len(l)):
            for a, b in l[q].items():
                for c, d in result.items():
                    if b == c:
                        d.append(l[q])

        return result


def valida_questao(d1):
    saida = {}
    listaop = ['A', 'B', 'C', 'D']
    cont = 0
    if d1 == {}:
        saida['titulo'] = 'nao_encontrado'
        saida['nivel'] = 'nao_encontrado'
        saida['opcoes'] = 'nao_encontrado'
        saida['correta'] = 'nao_encontrado'
        saida['outro'] = 'numero_chaves_invalido'
    else:
        for c in range(0, len(d1)):
            if 'titulo' not in d1:
                saida['titulo'] = 'nao_encontrado'
        for c in range(0, len(d1)):
            if 'nivel' not in d1:
                saida['nivel'] = 'nao_encontrado'
        for c in range(0, len(d1)):
            if 'opcoes' not in d1:
                saida['opcoes'] = 'nao_encontrado'
        for c in range(0, len(d1)):
            if 'correta' not in d1:
                saida['correta'] = 'nao_encontrado'
        if len(d1) != 4:
            saida['outro'] = 'numero_chaves_invalido'
        for k, v in d1.items():
            if k == 'titulo':
                if len(v.strip()) == 0:
                    saida['titulo'] = 'vazio'
        for k, v in d1.items():
            if k == 'nivel':
                if v not in 'facilmediodificil':
                    saida['nivel'] = 'valor_errado'
        for k, v in d1.items():
            if k == 'opcoes':
                if len(v) != 4:
                    saida['opcoes'] = 'tamanho_invalido'
                else:
                    for a, b in v.items():
                        if len(b.strip()) == 0:
                            saida['opcoes'] = {}
                            break
                        if a != listaop[cont]:
                            saida['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                            break
                        cont += 1
                    for k, v in saida.items():
                        if v == {}:
                            for g, n in d1.items():
                                if g == 'opcoes':
                                    for a, b in n.items():
                                        if len(b.strip()) == 0:
                                            v[a] = 'vazia'

        for k, v in d1.items():
            if k == 'correta':
                if v not in 'ABCD':
                    saida['correta'] = 'valor_errado'
    print(saida)
    return saida


def valida_questoes(lista1):
    lista2 = []
    for c in range(0, len(lista1)):
        lista2.append(valida_questao(lista1[c]))
    return lista2


def sorteia_questao(dq, nivel):
    posicao = 'babana'
    lr = []
    for k, v in dq.items():
        if k == nivel:
            lr = v
            posicao = randint(0, len(v)-1)
    return lr[posicao]


def sorteia_questao_inedida(dq, nivel, lista1):
    escolha = sorteia_questao(dq, nivel)
    while escolha in lista1:
        escolha = sorteia_questao(dq, nivel)
    lista1.append(escolha)
    return escolha


def questao_para_texto(dq, n):
    questao = 'babana'
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    for k, v in dq.items():
        if k == 'titulo':
            questao = v
        elif k == 'opcoes':
            for a, b in v.items():
                if a == 'A':
                    A = b
                elif a == 'B':
                    B = b
                elif a == 'C':
                    C = b
                elif a == 'D':
                    D = b
    retorno = f'{("-")*40}\nQUESTAO {n}\n\n{questao}\n\nRESPOSTAS:\nA: {A}\nB: {B}\nC: {C}\nD: {D}\n'
    print(retorno)
    return retorno


def gera_ajuda(dq):
    dica = 'babana'
    resposta = ''
    erradas = []
    n_dicas = randint(1, 2)
    random1 = randint(0, 2)
    random2 = randint(0, 2)
    while random2 == random1:
        random2 = randint(0, 2)
    for k, v in dq.items():
        if k == 'correta':
            resposta = v
    for k, v in dq.items():
        if k == 'opcoes':
            for a, b in v.items():
                if a != resposta:
                    erradas.append(b)
    if n_dicas == 1:
        dica = f'DICA:\nOpções certamente erradas: {erradas[random1]}'
    elif n_dicas == 2:
        dica = f'DICA:\nOpções certamente erradas: {erradas[random1]} | {erradas[random2]}'
    return dica  # funções e imports
niveis = []
lista_questoes = [
  {
    'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'
  },
  {
    'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'
  },
  {
    'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
    'correta': 'C'
  }
]
pontos = 0

lista_niveis = transforma_base(lista_questoes)
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

#  babana
