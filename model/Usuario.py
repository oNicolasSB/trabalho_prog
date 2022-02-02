class Usuario:
    __id: int
    __nome: str
    __email: str
    __senha: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: int):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: int):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: int):
        self.__senha = senha

    def __str__(self) -> str:
        return str(self.__class__) + ": " + str(self.__dict__)