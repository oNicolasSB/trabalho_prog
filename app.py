from tkinter import *
from config.Config import Config
from config.Database import Database
from dao.UsuarioDao import UsuarioDao
from model.Usuario import Usuario
from view.Table import Table

dao = UsuarioDao(Database(Config().config).conn)


class Inserir:
    def __init__(self, master, dao:UsuarioDao) -> Usuario:
        self.dao = dao
        self.master = master

        self.varnome = StringVar()
        self.varemail = StringVar()
        self.varsenha = StringVar()

        self.janela_inserir = Frame(self.master)
        self.janela_inserir.pack()
        self.lblnome = Label(self.janela_inserir, text = "digite o nome do usuário: ")
        self.lblnome.pack()
        self.unome = Entry(self.janela_inserir, textvariable=self.varnome)
        self.unome.pack()
        self.lblemail = Label(self.janela_inserir, text = "digite o email do usuário: ")
        self.lblemail.pack()
        self.uemail = Entry(self.janela_inserir, textvariable=self.varemail)
        self.uemail.pack()
        self.lblsenha = Label(self.janela_inserir, text = "digite a senha do usuário: ")
        self.lblsenha.pack()
        self.usenha = Entry(self.janela_inserir, textvariable=self.varsenha)
        self.usenha.pack()
        self.botao_criar = Button(self.janela_inserir, text="criar usuario", command=self.jubileu)
        self.botao_criar.pack()



    def jubileu(self):
        usuario = Usuario()
        usuario.nome = self.varnome.get()
        usuario.email = self.varemail.get()
        usuario.senha = self.varsenha.get()
        self.dao.db_inserir(usuario)


class Alterar:
    def __init__(self, master, dao:UsuarioDao) -> Usuario:
        self.dao = dao
        self.master = master

        self.varid = IntVar()
        self.varnome = StringVar()
        self.varemail = StringVar()
        self.varsenha = StringVar()

        self.janela_alterar = Frame(self.master)
        self.janela_alterar.pack()
        self.lblid = Label(self.janela_alterar, text = "digite o id do usuário a ser alterado: ")
        self.lblid.pack()
        self.uid = Entry(self.janela_alterar, textvariable= self.varid)
        self.uid.pack()
        self.lblnome = Label(self.janela_alterar, text = "digite o nome do usuário: ")
        self.lblnome.pack()
        self.unome = Entry(self.janela_alterar, textvariable=self.varnome)
        self.unome.pack()
        self.lblemail = Label(self.janela_alterar, text = "digite o email do usuário: ")
        self.lblemail.pack()
        self.uemail = Entry(self.janela_alterar, textvariable=self.varemail)
        self.uemail.pack()
        self.lblsenha = Label(self.janela_alterar, text = "digite a senha do usuário: ")
        self.lblsenha.pack()
        self.usenha = Entry(self.janela_alterar, textvariable=self.varsenha)
        self.usenha.pack()
        self.botao_alterar = Button(self.janela_alterar, text="alterar usuario", command=self.jubileu)
        self.botao_alterar.pack()


    def jubileu(self):        
        usuario = Usuario()
        usuario.id = self.varid.get()
        usuario.nome = self.varnome.get()
        usuario.email = self.varemail.get()
        usuario.senha = self.varsenha.get()
        self.dao.db_alterar(usuario)

class Excluir:
    def __init__(self, master, dao:UsuarioDao) -> Usuario:
        self.dao = dao
        self.master = master

        self.varid = IntVar()
        self.janela_excluir = Frame(self.master)
        self.janela_excluir.pack()
        self.lblid = Label(self.janela_excluir, text="digite o id do usuário a ser excluído: ")
        self.lblid.pack()
        self.uid = Entry(self.janela_excluir, textvariable=self.varid)
        self.uid.pack()
        self.botao_excluir = Button(self.janela_excluir, text="excluir usuário! ", command=self.jubileu)
        self.botao_excluir.pack()
        
    def jubileu(self):        
        usuario = Usuario()
        usuario.id = self.varid.get()
        self.dao.db_excluir(usuario)
    
        



def mostrar_lista():
    Table(dao.selecionarUsuarios())

class Main:
    def __init__(self, master, dao:UsuarioDao):
        self.dao = dao
        self.master = master
        self.parent_widget=Frame(self.master)
        self.parent_widget.pack()

        self.lambeu = Label(self.parent_widget, text = "selecione o que quer fazer ")
        self.lambeu.pack()

        self.botao_inserir = Button(self.parent_widget, text="inserir usuário", command=self.Inserir)
        self.botao_inserir.pack()

        self.botao_alterar = Button(self.parent_widget, text="alterar usuário", command=self.Alterar)
        self.botao_alterar.pack()

        self.botao_excluir = Button(self.parent_widget, text="excluir usuário", command=self.Excluir)
        self.botao_excluir.pack()

        self.botao_tabela = Button(self.parent_widget, text="exibir usuarios", command= mostrar_lista)
        self.botao_tabela.pack() 

    def Inserir(self):
        self.novajanela = Toplevel(self.master)
        self.app = Inserir(self.novajanela, self.dao)

    def Alterar(self):
        self.novajanela = Toplevel(self.master)
        self.app = Alterar(self.novajanela, self.dao)

    def Excluir(self):
        self.novajanela = Toplevel(self.master)
        self.app = Excluir(self.novajanela, self.dao)

    def Tabela(self):
        Table(self.dao.selecionarUsuarios())

    

parent_widget=Tk()
parent_widget.title("alterar / adicionar / excluir usuários")
app=Main(parent_widget, dao)
parent_widget.mainloop()



