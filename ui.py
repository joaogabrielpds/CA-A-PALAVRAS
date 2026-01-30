import tkinter as tk
from tkinter import messagebox
from game import CacaPalavras, PALAVRAS, TAMANHO

# configuração visual
COR_FUNDO = "#11c3e2"
COR_PAINEL = "#383AC4"
COR_GRID = "#ffffff"
COR_BOTAO = "#4CAF50"
COR_TEXTO = "#ff0000"


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Caça-Palavras")

        self.jogo = CacaPalavras()
        self.root.configure(bg=COR_FUNDO)

        self.selecao = []
        self.direcao = None
        self.inicio = None

        self._criar_grid()
        self._criar_controles()

    def iniciar_selecao(self, linha, coluna):
        self.selecao = [(linha, coluna)]
        self.inicio = (linha, coluna)
        self.direcao = None
        self.labels[(linha, coluna)].configure(bg="#FFD700")

    def arrastar_selecao(self, linha, coluna):
        if not self.selecao:
            return

        li, ci = self.inicio
        dl = linha - li
        dc = coluna - ci

        # define direção na primeira movimentação válida
        if self.direcao is None:
            if dl == 0:
                self.direcao = "H"
            elif dc == 0:
                self.direcao = "V"
            elif abs(dl) == abs(dc):
                self.direcao = "D"
            else:
                return

        # valida direção
        if self.direcao == "H" and linha != li:
            return
        if self.direcao == "V" and coluna != ci:
            return
        if self.direcao == "D" and abs(dl) != abs(dc):
            return

        ultima_l, ultima_c = self.selecao[-1]

        # impede pular letras
        if abs(linha - ultima_l) > 1 or abs(coluna - ultima_c) > 1:
            return

        if (linha, coluna) not in self.selecao:
            self.selecao.append((linha, coluna))
            self.labels[(linha, coluna)].configure(bg="#FFD700")

    def _criar_grid(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        self.labels = {}

        for i in range(TAMANHO):
            for j in range(TAMANHO):
                lbl = tk.Label(
                    frame,
                    text=self.jogo.matriz[i][j],
                    width=2,
                    height=1,
                    font=("Arial", 12, "bold"),
                    bg="white",
                    borderwidth=1,
                    relief="solid"
                )
                lbl.grid(row=i, column=j)

                lbl.bind("<Button-1>", lambda e, l=i, c=j: self.iniciar_selecao(l, c))
                lbl.bind("<Enter>", lambda e, l=i, c=j: self.arrastar_selecao(l, c))
                lbl.bind("<ButtonRelease-1>", lambda e: self.verificar())

                self.labels[(i, j)] = lbl

    def _criar_controles(self):
        frame = tk.Frame(self.root, bg=COR_PAINEL)
        frame.grid(row=0, column=1, padx=10)

        tk.Label(
            frame,
            text="Selecione a palavra com o mouse",
            bg=COR_PAINEL,
            fg=COR_TEXTO,
            font=("Arial", 12, "bold")
        ).pack(padx=10, pady=20)

    def verificar(self):
        if not self.selecao:
            return

        letras = "".join(self.jogo.matriz[l][c] for l, c in self.selecao)

        if self.jogo.verificar_por_selecao(letras):
            messagebox.showinfo("Acerto", f"Você encontrou: {letras}")
            for pos in self.selecao:
                self.labels[pos].configure(bg="#4CAF50")
        else:
            for pos in self.selecao:
                self.labels[pos].configure(bg="white")

        self.selecao = []
        self.direcao = None
