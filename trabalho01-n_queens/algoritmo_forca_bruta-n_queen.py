"""Trabalho 1 Problema das N-Rainhas
TIPO DE SOLUÇÃO: recursão com backtracking
Alunos: Bruno Campos, Elisa de Mattos Rosá, Filipe Voges"""


class NRainhas:
    # n_rainhas eh o numero de rainhas inserido na função main
    def __init__(self, n_rainhas):
        self.n_rainhas = n_rainhas
        self.n_solucoes = 0
        self.solucao()

    """Função que retorna o numero de soluções encontradas"""
    def solucao(self):
        positions = [-1] * self.n_rainhas
        self.put_rainha(positions, 0)
        return print(f"Encontrado {self.n_solucoes} soluções.")

    def put_rainha(self, positions, target_row):
        """Insere uma rainha no target_row verificando todos os N possíveis casos.
        Se um local válido é encontrado, a função chama a si mesma tentando colocar uma dama
         na próxima linha até que todas as N rainhas sejam colocadas na placa NxN.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.n_rainhas:
            self.show_full_board(positions)
            # self.show_short_board(positions)
            self.n_solucoes += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.n_rainhas):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_rainha(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.n_rainhas):
            line = ""
            for column in range(self.n_rainhas):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        """
        Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the corresponding row.
        """
        line = ""
        for i in range(self.n_rainhas):
            line += str(positions[i]) + " "
        print(line)

def main():
    """Initialize and solve the n queens puzzle"""
    NRainhas(5)

if __name__ == "__main__":
    # execute only if run as a script
    main()