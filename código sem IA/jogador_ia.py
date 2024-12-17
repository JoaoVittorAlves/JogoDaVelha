from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def checar_vitoria(self, matriz, tipo):
        # Verifica linhas e colunas
        for i in range(3):
            if all(matriz[i][j] == tipo for j in range(3)):  # Linha
                return True
            if all(matriz[j][i] == tipo for j in range(3)):  # Coluna
                return True

        # Verifica diagonais
        if all(matriz[i][i] == tipo for i in range(3)):  # Diagonal principal
            return True
        if all(matriz[i][2 - i] == tipo for i in range(3)):  # Diagonal secundária
            return True

        return False

    def getJogada(self) -> (int, int):
        # R1: Verificar se há duas marcações consecutivas (minha ou do oponente)
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Simular a jogada
                    self.matriz[l][c] = self.tipo
                    if self.checar_vitoria(self.matriz, self.tipo):
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO

                    # Bloquear o oponente
                    oponente = 3 - self.tipo
                    self.matriz[l][c] = oponente
                    if self.checar_vitoria(self.matriz, oponente):
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO

        # R2: Criar duas sequências de duas marcações
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Simular a jogada
                    self.matriz[l][c] = self.tipo
                    sequencias = 0
                    for l2 in range(3):
                        for c2 in range(3):
                            if self.matriz[l2][c2] == Tabuleiro.DESCONHECIDO:
                                self.matriz[l2][c2] = self.tipo
                                if self.checar_vitoria(self.matriz, self.tipo):
                                    sequencias += 1
                                self.matriz[l2][c2] = Tabuleiro.DESCONHECIDO
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                    if sequencias >= 2:
                        return (l, c)

        # R3: Marcar o centro, se livre
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Marcar o canto oposto, se o oponente tiver marcado um canto
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            l, c = canto
            oposto = (2 - l, 2 - c)
            if self.matriz[l][c] == 3 - self.tipo and self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                return oposto

        # R5: Marcar um canto vazio
        for canto in cantos:
            l, c = canto
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)

        # R6: Marcar arbitrariamente um quadrado vazio
        lista = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        if len(lista) > 0:
            p = randint(0, len(lista) - 1)
            return lista[p]
        else:
            return None

        
        # colocar as especificações do exercicio, os 6 requisitos, para a IA.