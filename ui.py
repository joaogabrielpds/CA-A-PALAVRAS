import tkinter as tk
from tkinter import messagebox
from game import CacaPalavras, PALAVRAS, TAMANHO

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Caça-Palavras")

        self.jogo = CacaPalavras()

        self._criar_grid()
        self._criar_controles()
        self._atualizar_lista()

    def _criar_grid(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=15, pady=15)

        for i in range(TAMANHO):
            for j in range(TAMANHO):
                tk.Label(
                    frame,
                    text=self.jogo.matriz[i][j],
                    width=2,
                    height=1,
                    font=("Arial", 12, "bold"),
                    borderwidth=1,
                    relief="solid"
                ).grid(row=i, column=j)

    def _criar_controles(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=1, padx=10)

        tk.Label(frame, text="Palavra").grid(row=0, column=0)
        self.e_palavra = tk.Entry(frame)
        self.e_palavra.grid(row=0, column=1)

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

    def _atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for p in PALAVRAS:
            if p not in self.jogo.encontradas:
                self.lista.insert(tk.END, p)

    def verificar(self):
        try:
            palavra = self.e_palavra.get()
            linha = int(self.e_linha.get())
            coluna = int(self.e_coluna.get())
            direcao = self.e_direcao.get().upper()
        except:
            messagebox.showerror("Erro", "Dados inválidos")
            return

        if self.jogo.verificar(palavra, linha, coluna, direcao):
            messagebox.showinfo("Acerto", "Palavra encontrada!")
            self._atualizar_lista()
        else:
            messagebox.showwarning("Erro", "Palavra incorreta")

        if len(self.jogo.encontradas) == len(PALAVRAS):
            messagebox.showinfo("Fim", "Parabéns! Você venceu!")
