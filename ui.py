import tkinter as tk
from tkinter import messagebox
from game import CacaPalavras, PALAVRAS, TAMANHO
#configuração visual
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

        self._criar_grid()
        self._criar_controles()
        self._atualizar_lista()
        
    def iniciar_selecao(self, linha, coluna):
        self.selecao = [(linha, coluna)]
        self.labels[(linha, coluna)].configure(bg="#FFD700")

    def arrastar_selecao(self, linha, coluna):
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

                self.labels[(i, j)] = lbl


    def _criar_controles(self):
        frame = tk.Frame(self.root, bg=COR_PAINEL)
        frame.grid(row=0, column=1, padx=10)

        
        tk.Label(frame, text="Linha").grid(row=1, column=0)
        self.e_linha = tk.Entry(frame, width=5)
        self.e_linha.grid(row=1, column=1)

        tk.Label(frame, text="Coluna").grid(row=2, column=0)
        self.e_coluna = tk.Entry(frame, width=5)
        self.e_coluna.grid(row=2, column=1)

        tk.Label(frame, text="Direção (H/V)").grid(row=3, column=0)
        self.e_direcao = tk.Entry(frame, width=5)
        self.e_direcao.grid(row=3, column=1)

        tk.Button(frame, text="Verificar", command=self.verificar).grid(
            row=4, column=0, columnspan=2, pady=5
        )

        tk.Label(frame, text="Palavras restantes").grid(row=5, column=0, columnspan=2)
        self.lista = tk.Listbox(frame, height=6)
        self.lista.grid(row=6, column=0, columnspan=2)

    
    def verificar(self):
        letras = "".join(self.jogo.matriz[l][c] for l, c in self.selecao)

        if self.jogo.verificar_por_selecao(letras):
            messagebox.showinfo("Acerto", f"Você encontrou: {letras}")
            for pos in self.selecao:
                self.labels[pos].configure(bg="#4CAF50")
        else:
            for pos in self.selecao:
                self.labels[pos].configure(bg="white")
