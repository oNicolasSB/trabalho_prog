from tkinter import *
from tkinter import ttk

class Table:
    def __init__(self, usuarios: list) -> None:
        self.root = Tk()
        self.root.title("Tabela de Usuários")
        self.root.geometry("800x700")

        wrapper = LabelFrame(self.root, text="Lista de Usuários")
        wrapper.pack(fill="both", expand="yes", padx=20, pady=20)

        trv = ttk.Treeview(wrapper, columns=(1 ,2, 3, 4), show="headings", height=400)
        trv.pack()

        trv.heading(1, text="ID")
        trv.heading(2, text="Nome")
        trv.heading(3, text="E-mail")
        trv.heading(4, text="Senha")

        for usuario in usuarios:
            trv.insert('', 'end', values=[usuario.id, usuario.nome, usuario.email, usuario.senha])

        self.root.mainloop()