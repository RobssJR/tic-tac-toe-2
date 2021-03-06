from os import system
from random import choice
from string import ascii_lowercase

tabuleiro = [[0,0,0],
             [0,0,0],
             [0,0,0]]

base = [[0,0,0],
        [0,0,0],
        [0,0,0]]

valor_pecas = {'P': 1, 'M': 2, 'G': 3}


class Jogador():
    def __init__(self, name: str):
        self.name = name
        self.mao = ['P','P','M','M','G','G']

    def fazerJogada(self, peca, linha, coluna):
        if peca in self.mao:
            try:
                if tabuleiro[linha][coluna] == 0:
                    tabuleiro[linha][coluna] = f'{self.name[0]}-{peca}'
                    self.mao.remove(peca)
                    return True
                else:
                    reserva = tabuleiro[linha][coluna]
                    tabuleiro[linha][coluna] = tabuleiro[linha][coluna].replace(f'{tabuleiro[linha][coluna][0:2]}','') #Remove a inicial

                    if valor_pecas[peca] > valor_pecas[tabuleiro[linha][coluna]]:
                        tabuleiro[linha][coluna] = f'{self.name[0]}-{peca}'
                        self.mao.remove(peca)
                        return True
                    else:
                        tabuleiro[linha][coluna] = reserva
                        print('Essa peça é menor')
                        input()

            except IndexError:
                print('Valores de linha e coluna invalidos')
                input()
        else:
            print('Peça invalida')
            input()
            return False


player1 = Jogador(str(input('Jogador 1: ')).title())
player2 = Jogador(str(input('Jogador 2: ')).title())

jogadores = [player1,player2]


def desenharTela(): #Função para desenhar o tabuleiro na tela
    system('cls')
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                print(" _ ", end=' ')
            else:
                print(f"{tabuleiro[i][j]}",end=' ')

        print('\n')

    for j in jogadores:
        print(f"Peças {j.name}: {' '.join(j.mao)}")


def game(vez): #Função principal para a logica do jogo (Ela desenha e pega a entrada do usuario)
    while True:
        desenharTela()

        try:
            peca = input(f"\nPeça da mão {vez.name}: ").upper()
            linha  = int(input("Linha: ")) - 1
            coluna = int(input("Coluna: ")) - 1
            
            if vez.fazerJogada(peca,linha,coluna):
                break

        except ValueError:
            print("Valor invalido")
            input()


def verificarGanhador():
    for l in range(0,3):
        for c in range(0,3):
            base[l][c] = tabuleiro[l][c]
            if base[l][c] == 0:
                base[l][c] = choice(ascii_lowercase)

    return ((base[0][0][0] == base[0][1][0] == base[0][2][0]) or
        (base[1][0][0] == base[1][1][0] == base[1][2][0]) or
        (base[2][0][0] == base[2][1][0] == base[2][2][0]) or
        (base[0][0][0] == base[1][0][0] == base[2][0][0]) or
        (base[0][1][0] == base[1][1][0] == base[2][1][0]) or
        (base[0][2][0] == base[1][2][0] == base[2][2][0]) or
        (base[0][0][0] == base[1][1][0] == base[2][2][0]) or
        (base[0][2][0] == base[1][1][0] == base[2][0][0]))
            

jogada = 1


if __name__ == "__main__":
    while True:
        if jogada == 1:
            vez = jogadores[0]
        else:
            vez = jogadores[1]
        
        game(vez) #Roda até a jogada ser feita

        if verificarGanhador():
            print(f'{vez.name} GANHOU')
            break

        jogada *= -1