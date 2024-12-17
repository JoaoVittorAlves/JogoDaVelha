# -*- coding: utf-8 -*-
class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]
        ]

    def tem_campeao(self):
        # Checagem de quem ganhou e de quem perdeu
        # Se a soma for 3, JOGADOR_0 venceu (1 + 1 + 1).
        # Se a soma for 12, JOGADOR_X venceu (4 + 4 + 4).
        # Caso contrário, não há vencedor.

        # Verificar linhas
        for linha in self.matriz:
            if sum(linha) == 3:
                return Tabuleiro.JOGADOR_0
            elif sum(linha) == 12:
                return Tabuleiro.JOGADOR_X

        # Verificar colunas
        for c in range(3):
            soma_coluna = sum(self.matriz[l][c] for l in range(3))
            if soma_coluna == 3:
                return Tabuleiro.JOGADOR_0
            elif soma_coluna == 12:
                return Tabuleiro.JOGADOR_X

        # Verificar diagonal principal
        soma_diagonal_principal = sum(self.matriz[i][i] for i in range(3))
        if soma_diagonal_principal == 3:
            return Tabuleiro.JOGADOR_0
        elif soma_diagonal_principal == 12:
            return Tabuleiro.JOGADOR_X

        # Verificar diagonal secundária
        soma_diagonal_secundaria = sum(self.matriz[i][2 - i] for i in range(3))
        if soma_diagonal_secundaria == 3:
            return Tabuleiro.JOGADOR_0
        elif soma_diagonal_secundaria == 12:
            return Tabuleiro.JOGADOR_X

        # Caso nenhum vencedor seja encontrado, retorna DESCONHECIDO
        return Tabuleiro.DESCONHECIDO
