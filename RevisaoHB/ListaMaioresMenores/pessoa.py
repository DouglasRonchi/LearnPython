cab = ['nome', 'telefone', 'email', 'idade']

class Pessoa:
    def __init__(self, nome, telefone, email, idade):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade