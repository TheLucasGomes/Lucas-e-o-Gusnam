from random import randint


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
# Transforma lista de questões em dicionario


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
# Confere se a questão esta em formato correto


def valida_questoes(lista1):
    lista2 = []
    for c in range(0, len(lista1)):
        lista2.append(valida_questao(lista1[c]))
    return lista2
# valida toda uma lista de questões


def sorteia_questao(dq, nivel):
    posicao = 'babana'
    lr = []
    for k, v in dq.items():
        if k == nivel:
            lr = v
            posicao = randint(0, len(v)-1)
    return lr[posicao]
# sorteia uma questão de um nível escolhido


def sorteia_questao_inedida(dq, nivel, lista1):
    escolha = sorteia_questao(dq, nivel)
    while escolha in lista1:
        escolha = sorteia_questao(dq, nivel)
    lista1.append(escolha)
    return escolha
# sorteia uma questão de nivel escolhido sem repetir


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
    retorno = f'{"-"*40}\nQUESTAO {n}\n\n{questao}\n\nRESPOSTAS:\nA: {A}\nB: {B}\nC: {C}\nD: {D}\n'
    print(retorno)
    return retorno
# Transforma o dicionário de uma questão em string de formato apropriado


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
# Dá uma dica com base em uma questão


quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {
             'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
             'nivel': 'facil',
             'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
             'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},

         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {
             'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
             'nivel': 'medio',
             'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
             'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {
             'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
             'nivel': 'medio',
             'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
             'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {
             'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
             'nivel': 'medio',
             'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
             'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {
             'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
             'nivel': 'dificil',
             'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
             'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas',
                     'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros',
                     'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},

         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa',
                     'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
         ]
