from psycopg2 import connect
from model.Usuario import Usuario

class UsuarioDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarUsuarios(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM usuario'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            usuario = Usuario()
            usuario.id = item[0]
            usuario.nome = item[1]
            usuario.email = item[2]
            usuario.senha = item[3]

            lista.append(usuario)

        return lista

    def db_inserir(self, usuario:Usuario)-> Usuario :
        c= self.connection.cursor()
        c.execute("""
            insert into usuario(nome, email, senha)
            values('{}', '{}', '{}') RETURNING id
        """.format(usuario.nome, usuario.email, usuario.senha))
        self.connection.commit()

    def db_alterar(self, usuario: Usuario) -> Usuario:
        c = self.connection.cursor()
        c.execute("""
            update usuario
            SET nome = '{}', email = '{}', senha = '{}'
            WHERE id = '{}';
        """.format(usuario.nome, usuario.email, usuario.senha, usuario.id))
        self.connection.commit()

    def db_excluir(self, usuario: Usuario) -> Usuario:
        c = self.connection.cursor()
        c.execute("""
            delete from usuario
            where id = '{}'
        """.format(usuario.id))
        self.connection.commit()