'''algoritmo busca gulosa ou subida de encosta

maximo_local eh o pico mais alto entre seus vizinhos
maximo_global eh o pico mais alto

Completo: se o algoritmo consegue atingir um
estado objetivo desde que ele exista.

Ótimo: se consegue encontrar o mínimo/máximo
para a função de custo.

- Sempre escolhe a alternativa que parece mais promissora naquele instante
- NUNCA reconsidera essa decisão
- Uma escolha que foi feita NUNCA é revista
- Não há backtracking
- A escolha é feita de acordo com um criterio guloso - decisão localmente ótima.

'''

import numpy as np
import random

'''
def subida_de_encosta (problema, maximo_local=None):
    corrente
    no
    vizinho
    no


    return maximo_local'''

import numpy as np
import random



def main():
    N = 8

    board, queens = init_board(N)
    update_board(board, N, queens)
    minimums = []

    tries = N / 2
    minimums, curr = get_lowest(board, N, minimums)

    while tries:
        put_lowest(board, N, minimums, queens)
        update_board(board, N, queens)

        last = curr
        minimums, curr = get_lowest(board, N, minimums)


        tries -= 1

        if tries == 0:
            board, queens = init_board(N)
            tries = N / 2

    print(board)


def h_function (board, N, queen):
    count = 0

    # down & right #
    for r, c in zip(range(queen[0] + 1, N, 1), range(queen[1] + 1, N, 1)):
        if board[r][c] == -1:
            count += 1

    # down & left #
    for r, c in zip(range(queen[0] + 1, N, 1), range(queen[1] - 1, -1, -1)):
        if board[r][c] == -1:
            count += 1

    # down #
    for r in range(queen[0] + 1, N):
        if board[r][queen[1]] == -1:
            count += 1

    return count


def update_board(board, N, queens):
    count = 0

    for r in range(N):
        board[queens[r][0]][queens[r][1]] = 0
        for c in range(N):
            board[r][c] = -1
            for k in range(N):
                if k != r:
                    count += h_function(board, N, queens[k])
                count += h_function(board, N, (r, c))
                if queens[r][0] == r and queens[r][1] == c:
                    board[r][c] = -1
                else:
                    board[r][c] = count
                count = 0


def get_lowest(board, N, minimums):
    min = board[0][0]
    minimums = []
    if min == -1:
        min = board[0][1]

    for r in range(N):
        for c in range(N):
            if board[r][c] < min and board[r][c] != -1:
                min = board[r][c]

    for r in range(N):
        for c in range(N):
            if board[r][c] == min:
                minimums.append((r, c))

    return minimums, min


def put_lowest(board, N, mins, queens):
    move = random.randint(0, N - 1)
    row = mins[move][0]
    col = mins[move][1]

    for c in range(N):
        if board[row][c] == -1:
            board[row][col] = -1
            queens[row][0] = row
            queens[row][1] = col

            board[row][c] = 0
            break


def init_board(N):
    board = np.zeros((N,N), dtype='int8')

    # Generate random queens #
    queens = np.zeros((N,), dtype='i,i')
    for r in range(N):
        queens[r] = (r, random.randint(0, N - 1))
        board[r][queens[r][1]] = -1

    return board, queens


def is_solution(board, N, queens):
    for i in range(N):
        if h_function(board, N, queens[i]) > 0:
            return False

    return True


main()
