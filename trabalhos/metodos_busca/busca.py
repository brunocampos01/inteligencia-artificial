import copy
import random


def gerador_estado_aleatorio():
    """
    Pode gerar estado não solucionáveis
    """
    line_1, line_2, line_3 = [], [], []
    elemenodos = random.sample(range(1, 9), 8)
    elemenodos.insert(random.randint(0, 9), 0)

    for x in elemenodos:
        if len(line_1) < 3:
            line_1.append(x)
        elif len(line_2) < 3:
            line_2.append(x)
        else:
            line_3.append(x)

    return [line_1, line_2, line_3, [0, None]]


def eh_estado_final(tabuleiro):
    if tabuleiro[0][0] != 0:
        return False
    if tabuleiro[0][1] != 1:
        return False
    if tabuleiro[0][2] != 2:
        return False
    if tabuleiro[1][0] != 3:
        return False
    if tabuleiro[1][1] != 4:
        return False
    if tabuleiro[1][2] != 5:
        return False
    if tabuleiro[2][0] != 6:
        return False
    if tabuleiro[2][1] != 7:
        return False
    if tabuleiro[2][2] != 8:
        return False

    return True


def eh_repetido_tabuleiro(tabuleiro1, tabuleiro2):
    """
    Auxilia na garantia de não ter nodos repetidos
    """
    for i in range(3):
        for j in range(3):
            if tabuleiro1[i][j] != tabuleiro2[i][j]:
                return False
    return True


def imprime_tabuleiro(tabuleiro, off=False):
    if off is False:
        print('Fronteira:', tabuleiro[3][0])
        print(tabuleiro[0])
        print(tabuleiro[1])
        print(tabuleiro[2])
        return None

    return int(tabuleiro[3][0])


def expandir(tabuleiro):
    """
    Retorna um conjunto de nodos filhos com as próximas jogadas possíveis
    """
    jogadas = []

    # 1 se vazio esta no meio do tabuleirouleiro
    if tabuleiro[1][1] == 0:
        # move pra baixo
        a = copy.deepcopy(tabuleiro)
        a[1][1] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

        # move pra direita
        a = copy.deepcopy(tabuleiro)
        a[1][1] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

        # move pra esquerda
        a = copy.deepcopy(tabuleiro)
        a[1][1] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

        # move pra cima
        a = copy.deepcopy(tabuleiro)
        a[1][1] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 2 se vazio esta no canodoo esquerdo superior
    elif tabuleiro[0][0] == 0:
        # move pra cima
        a = copy.deepcopy(tabuleiro)
        a[0][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tabuleiro)
        a[0][0] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 3 se vazio esta no canodoo direito superior
    elif tabuleiro[0][2] == 0:
        # move pra cima
        a = copy.deepcopy(tabuleiro)
        a[0][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tabuleiro)
        a[0][2] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 4 se vazio esta no canodoo inferior esquerdo
    elif tabuleiro[2][0] == 0:
        # move pra baixo
        a = copy.deepcopy(tabuleiro)
        a[2][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tabuleiro)
        a[2][0] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 5 se vazio esta no canodoo inferior direito
    elif tabuleiro[2][2] == 0:
        # move pra baixo
        a = copy.deepcopy(tabuleiro)
        a[2][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tabuleiro)
        a[2][2] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 6 se vazio esta no meio da linha de cima
    elif tabuleiro[0][1] == 0:
        # move pra cima
        a = copy.deepcopy(tabuleiro)
        a[0][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tabuleiro)
        a[0][1] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tabuleiro)
        a[0][1] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 7 se vazio esta no meio da linha de baixo
    elif tabuleiro[2][1] == 0:
        # move pra baixo
        a = copy.deepcopy(tabuleiro)
        a[2][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tabuleiro)
        a[2][1] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tabuleiro)
        a[2][1] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 8 se vazio esta no meio da coluna da esquerda
    elif tabuleiro[1][0] == 0:
        # move pra baixo
        a = copy.deepcopy(tabuleiro)
        a[1][0] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tabuleiro)
        a[1][0] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tabuleiro)
        a[1][0] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    # 9 se vazio esta no meio da coluna da direita
    elif tabuleiro[1][2] == 0:
        # move pra baixo
        a = copy.deepcopy(tabuleiro)
        a[1][2] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tabuleiro)
        a[1][2] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tabuleiro)
        a[1][2] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tabuleiro
        jogadas.append(a)

    return jogadas


def imprime_caminho(tabuleiro):
    print("\nCaminho para a solução:")
    pilha = []

    while tabuleiro[3][1] != None:
        pilha.append(tabuleiro)
        tabuleiro = tabuleiro[3][1]

    pilha.append(tabuleiro)
    tamanho_caminho = len(pilha)

    while len(pilha) > 0:
        temp = pilha.pop()
        imprime_tabuleiro(temp)

    print("Tamanho do Caminho: ", tamanho_caminho)


def h1(tabuleiro):
    """
    Número de peças fora do lugar
    """
    a = 0
    if tabuleiro[0][0] != 0:
        a = a + 1
    if tabuleiro[0][1] != 1:
        a = a + 1
    if tabuleiro[0][2] != 2:
        a = a + 1
    if tabuleiro[1][0] != 3:
        a = a + 1
    if tabuleiro[1][1] != 4:
        a = a + 1
    if tabuleiro[1][2] != 5:
        a = a + 1
    if tabuleiro[2][0] != 6:
        a = a + 1
    if tabuleiro[2][1] != 7:
        a = a + 1
    if tabuleiro[2][2] != 8:
        a = a + 1

    return a


def h2(tabuleiro):
    """
    Distância de Manhattan
    """
    h = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                h = h + abs(0 - i) + abs(0 - j)
            if tabuleiro[i][j] == 1:
                h = h + abs(0 - i) + abs(1 - j)
            if tabuleiro[i][j] == 2:
                h = h + abs(0 - i) + abs(2 - j)
            if tabuleiro[i][j] == 3:
                h = h + abs(1 - i) + abs(0 - j)
            if tabuleiro[i][j] == 4:
                h = h + abs(1 - i) + abs(1 - j)
            if tabuleiro[i][j] == 5:
                h = h + abs(1 - i) + abs(2 - j)
            if tabuleiro[i][j] == 6:
                h = h + abs(2 - i) + abs(0 - j)
            if tabuleiro[i][j] == 7:
                h = h + abs(2 - i) + abs(1 - j)
            if tabuleiro[i][j] == 8:
                h = h + abs(2 - i) + abs(2 - j)
    return h


def buscar(tipo_busca, tabuleiro_inicial):
    queue = []
    queue_nodos_rep = []
    total_nodos_visitados = 0
    total_nodos_criados = 0

    queue.append(tabuleiro_inicial)
    queue_nodos_rep.append(tabuleiro_inicial)
    print('\nProcessando ...\n\n\n')

    while len(queue) > 0:
        nodo_temporario = queue.pop(0)
        total_nodos_visitados = total_nodos_visitados + 1

        if eh_estado_final(nodo_temporario):
            print("Fim de jogo!\n\n")
            print(f'O total de nodos visitados:', total_nodos_visitados)
            print(f'O total de nodos expandidos/criados:', total_nodos_criados)
            print(f'O maior tamanho da fronteira durante a busca: {imprime_tabuleiro(nodo_temporario, off=True)} + estado inicial')
            imprime_caminho(nodo_temporario)
            break

        elif 'custo_uniforme' in tipo_busca:
            nodos_filhos = expandir(nodo_temporario)
            total_nodos_criados = len(nodos_filhos) + total_nodos_criados

            for nodo in nodos_filhos:
                existe = False

                for x in queue_nodos_rep:
                    if eh_repetido_tabuleiro(nodo, x):
                        existe = True
                        break

                if existe == False:
                    queue.append(nodo)
                    queue_nodos_rep.append(nodo)

        elif 'heuristica_simples' in tipo_busca:
            # aqui soh vejo quantas peças estão fora do lugar
            
            nodos_filhos = expandir(nodo_temporario)
            filhos_nao_repet = []
            valor_heuristica = 9
            total_nodos_criados = len(nodos_filhos) + total_nodos_criados


            for nodo in nodos_filhos:
                existe = False

                for x in queue_nodos_rep:
                    if eh_repetido_tabuleiro(nodo, x):
                        existe = True
                        break
                if not existe:
                    filhos_nao_repet.append(nodo)

            for nr in filhos_nao_repet:
                if h1(nr) < valor_heuristica:
                    valor_heuristica = h1(nr)

            for nr in filhos_nao_repet:
                if h1(nr) == valor_heuristica:
                    queue.append(nr)
                    queue_nodos_rep.append(nr)

        elif 'heuristica_distancia' in tipo_busca:
            # baseado no livro Inteligência artifical, Russell e Norvig

            nodos_filhos = expandir(nodo_temporario)
            filhos_nao_repet = []
            valor_heuristica = 1000
            total_nodos_criados = len(nodos_filhos) + total_nodos_criados

            for nodo in nodos_filhos:
                existe = False

                for x in queue_nodos_rep:
                    if eh_repetido_tabuleiro(nodo, x):
                        existe = True
                        break

                if not existe:
                    filhos_nao_repet.append(nodo)

            for nr in filhos_nao_repet:
                if h2(nr) < valor_heuristica:
                    valor_heuristica = h2(nr)

            for nr in filhos_nao_repet:
                if h2(nr) == valor_heuristica:
                    queue.append(nr)
                    queue_nodos_rep.append(nr)


def main():
    print("Estado inicial")
    # tabuleiro_inicial = gerador_estado_aleatorio()

    # estado teste
    tabuleiro_inicial = [[1, 2, 3], [4, 0, 5], [8, 6, 7], [0, None]]
    imprime_tabuleiro(tabuleiro_inicial)

    print("\nMeta para ganhar")
    meta = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, None]]
    imprime_tabuleiro(meta)

    print('\nAlgoritmos de busca: ')
    print("1: Custo Uniforme (sem heurística)")
    print("2: A* com heurística simples")
    print("3: A* com heurística de Distância Manhattan")

    algoritmo = int(input('Informe uma opção:'))

    if algoritmo == 1:
        buscar('custo_uniforme', tabuleiro_inicial)
    elif algoritmo == 2:
        buscar('heuristica_simples', tabuleiro_inicial)
    elif algoritmo == 3:
        buscar('heuristica_distancia', tabuleiro_inicial)


if __name__ == '__main__':
    main()
