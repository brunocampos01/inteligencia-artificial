"""
Trabalho 1 Problema das N-Rainhas
TIPO DE SOLUÇÃO: recursão com backtracking
Alunos: Bruno Campos, Elisa de Mattos Rosá, Filipe Voges"""


class NRainhas:
    # n_rainhas eh o numero de rainhas inserido na função main
    def __init__(self, n_rainhas):
        self.n_rainhas = n_rainhas
        self.n_solucoes = 0
        self.solucao()

    def solucao(self):
        """Função que retorna o numero de soluções encontradas"""
        positions = self.n_rainhas
        #print(type(positions))
        # atribui positions a uma lista de inteiros e multipla para formar o tabuleiro
        positions *= [self.n_rainhas]
        #print(type(positions))
        self.put_rainha(positions, 0)
        return print(f"Encontrado {self.n_solucoes} soluções.")


    def put_rainha(self, positions, linha_alvo):
        """Insere uma rainha no linha_alvo verificando todos os N possíveis.
        Se um local válido é encontrado, a função chama a si mesma e insere uma rainha
         na próxima linha até que todas as N rainhas sejam colocadas na placa NxN."""
        # se todas as linhas (n_rainhas) estão ocupadas, chama a funcao para imprimir o tabuleiro
        if linha_alvo == self.n_rainhas:
            self.imprime_tabuleiro(positions)
            #self.imprime_posicao_linha(positions)
            self.n_solucoes += 1
        else:
            # para todas as colunas tente colocar uma rainha
            for coluna in range(self.n_rainhas):
                if self.backtracking(positions, linha_alvo, coluna):
                    positions[linha_alvo] = coluna
                    self.put_rainha(positions, linha_alvo + 1)


    def backtracking(self, positions, linha_ocupada, coluna):
        """Verifique se uma determinada posição está sob ataque de qualquer uma das
         rainhas colocadas anteriormente (verifique a coluna e as posições diagonais)"""
        for i in range(linha_ocupada):
            if positions[i] == coluna or \
                positions[i] - i == coluna - linha_ocupada or \
                positions[i] + i == coluna + linha_ocupada:
                return False
        return True

    def imprime_tabuleiro(self, positions):
        for linha in range(self.n_rainhas):
            line = ""
            for coluna in range(self.n_rainhas):
                if positions[linha] == coluna:
                    line += "Q "
                else:
                    line += ". "
            #print(line)
        #print("\n")

    def imprime_posicao_linha(self, positions):
        """função para verificar a posicao de cada rainha"""
        line = ""
        for i in range(self.n_rainhas):
            line += str(positions[i]) + " "
        #print(line)


def main():
    NRainhas(20)
    print('fim')


if __name__ == "__main__":
    main()
