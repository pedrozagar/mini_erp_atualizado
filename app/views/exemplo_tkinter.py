import tkinter as tk #tk significa tkinter
from tkinter import messagebox #se eu colocasse após o import o * (asterisco), eu importaria todas as bilbiotecas do tkinder e isso não precisa, pega apenas o que precisa

janela = tk.Tk()

janela.title("MINI_ERP_ATUALIZADO")
janela.geometry("800x600")
janela.resizable(False, False) #isso é tanto na vertical como horizontal significa que não consegue puxar para maior ou menor a janela do quadro

lbl_titulo = tk.Label(
    janela,
    text = "EXEMPLO DE CADASTRO",
    font = ("Arial", 12,"bold")
)

lbl_titulo.grid(
    row = 0,
    column = 0,
    padx = 10,
    pady = 5,
    columnspan = 3
)

lbl_nome = tk.Label(
    janela,
    text = "Nome:"
)#lbl_titulo ou lbl_nome

lbl_nome.grid(
    row = 1,
    column = 0,
    padx = 10,
    pady = 5
)

txt_nome = tk.Entry(
    janela,
    width = 40
)

txt_nome.grid(
    row = 1,
    column = 1,
    #padx = 10,
    #pady = 5
)

lbl_idade = tk.Label(
    janela, #aqui é onde ele vai abrir
    text = "Idade"

    #bg= "lightblue"
    #padx = 10,
    #pady = 5
)
lbl_idade.grid(
    row = 2,
    column = 0,
    padx = 10,
    pady = 5
)

txt_idade = tk.Entry(
    janela,
    width = 40
)
txt_idade.grid(
    row = 2,
    column = 1
)

def printar():
    print(txt_nome.get())

btn_escrever_nome = tk.Button(
    janela,
    text = "Printar o nome",
    command = printar
)

btn_escrever_nome.grid(
    row = 1,
    column = 2,
    padx = 10,
    pady = 5,
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

btn_avaliar_idade = tk.Button(
    janela,
    text = "Avaliar idade",
    command = avaliar_idade
)

btn_avaliar_idade.grid(
    row = 2,
    column = 2
)

janela.mainloop()