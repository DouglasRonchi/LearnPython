class Legume:
    def __init__(self, nome, preco, id=None):
        self.__id = id
        self.__nome = nome
        self.__preco = preco


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco


    def __dict__(self):
        return {
            "nome":self.nome,
            "preco":self.preco,
            "id":self.id
        }