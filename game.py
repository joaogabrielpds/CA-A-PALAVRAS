import random
import string

TAMANHO = 11
PALAVRAS = ["PYTHON", "JAVA", "HTML", "CSS", "LOGICA", "KOTLIN"]

class CacaPalavras:
    def __init__(self):
        self.encontradas = []
        self.matriz = [[" " for _ in range(TAMANHO)] for _ in range(TAMANHO)]
        self._gerar()

    def _gerar(self):
        for p in PALAVRAS:
            self._inserir_palavra(p)
        self._preencher_matriz()

    def _inserir_palavra(self, palavra):
        direcao = random.choice(["H", "V"])

        if direcao == "H":
            linha = random.randint(0, TAMANHO - 1)
            coluna = random.randint(0, TAMANHO - len(palavra))
            for i, letra in enumerate(palavra):
                self.matriz[linha][coluna + i] = letra
        else:
            linha = random.randint(0, TAMANHO - len(palavra))
            coluna = random.randint(0, TAMANHO - 1)
            for i, letra in enumerate(palavra):
                self.matriz[linha + i][coluna] = letra

    def _preencher_matriz(self):
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                if self.matriz[i][j] == " ":
                    self.matriz[i][j] = random.choice(string.ascii_uppercase)

    def verificar(self, palavra, linha, coluna, direcao):
        palavra = palavra.upper()

        if palavra not in PALAVRAS or palavra in self.encontradas:
            return False

        if direcao == "H":
            if coluna + len(palavra) > TAMANHO:
                return False
            for i in range(len(palavra)):
                if self.matriz[linha][coluna + i] != palavra[i]:
                    return False

        elif direcao == "V":
            if linha + len(palavra) > TAMANHO:
                return False
            for i in range(len(palavra)):
                if self.matriz[linha + i][coluna] != palavra[i]:
                    return False
        else:
            return False

        self.encontradas.append(palavra)
        return True
