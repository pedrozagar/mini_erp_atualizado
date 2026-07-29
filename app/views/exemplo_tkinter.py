import tkinter as tk #tk significa tkinter
from tkinter import messagebox #se eu colocasse após o import o * (asterisco), eu importaria todas as bilbiotecas do tkinder e isso não precisa, pega apenas o que precisa

class Janela_Exemplo:
    def __init__(self):#aqui embaixo eu criei um construtor
        self.janela = tk.Tk()
        janela = tk.Tk()#criei um objeto da classe aqui e chamei de janela porque eu quis. agora isto será um atributo dentro da Classe Janela_Exemplo
        janela.title("MINI_ERP_ATUALIZADO")
        janela.geometry("800x600")
        janela.resizable(False, False) #isso é tanto na vertical como horizontal significa que não consegue puxar para maior ou menor a janela do quadro
        self.configurar_janela()

    def configurar_janela(self):
        lbl_titulo = tk.Label(
        janela,
        text = "EXEMPLO DE CADASTRO",
        font = ("Arial", 12,"bold")
        )

        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 3
        )

        #aqui no frm é FRAME. 
        self.frm_dados = tk.Frame(
            janela,
            padx = 10,
            pady = 5,
            bg = "lightblue"
        )

        self.frm_dados.grid(
            row = 1,
            column = 0
        )

        self.frm_botoes = tk.Frame(
            janela,
            padx = 10,
            pady = 5,
            bg = "darkblue",
            borderwidth = 2,
            relief = "solid"
        )

        self.frm_botoes.grid(
            row = 2,
            column = 0
        )

        self.lbl_nome = tk.Label(
            frm_dados,
            text = "Nome:"
        )#lbl_titulo ou lbl_nome

        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 10,
            pady = 5
        )

        self.txt_nome = tk.Entry(
            frm_dados,
            width = 40
        )

        self.txt_nome.grid(
            row = 1,
            column = 1,
            #padx = 10,
            #pady = 5
        )

        self.lbl_idade = tk.Label(
            frm_dados,
            #janela, #aqui é onde ele vai abrir
            text = "Idade"

            #bg= "lightblue"
            #padx = 10,
            #pady = 5
        )
        self.lbl_idade.grid(
            row = 2,
            column = 0,
            padx = 10,
            pady = 5
        )

        self.txt_idade = tk.Entry(
            frm_dados,
            width = 40
        )
        self.txt_idade.grid(
            row = 2,
            column = 1
        )

        self.btn_escrever_nome = tk.Button(
            janela,
            text = "Printar o nome",
            command = printar
        )

        self.btn_escrever_nome.grid(
            row = 1,
            column = 2,
            padx = 10,
            pady = 5,
        )

        self.btn_avaliar_idade = tk.Button(
            janela,
            text = "Avaliar idade",
            command = avaliar_idade
        )

        self.btn_avaliar_idade.grid(
            row = 2,
            column = 2
        )

#aqui vou criar uma função:
def avaliar_idade():
    if txt_idade.get() == "":
        messagebox.showerror(
            "Sisteminha",
            "Tu so pode estar de sacanagem...."
        )
        return
    idade = int(txt_idade.get())
    if idade >= 18:
        messagebox.showinfo(
            "sisteminha",
            "Com " + str(idade) + " voce e bem vindo"
        )
        return
    messagebox.showwarning(
        "Sisteminha",
        "Fedelho!!!"
    )
    return

    def iniciar(self):
        self.janela.mainloop()

janelinha = Janela_Exemplo()
janelinha.iniciar()