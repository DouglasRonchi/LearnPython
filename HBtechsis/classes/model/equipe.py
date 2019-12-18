from classes.model.linguagens import Linguagens

class Equipe:
    __id = 0
    __nome = ''
    __linguagem = Linguagens

    def get_id(self):
        return self.__id

    
    def set_id(self, id):
        self.__id = id


    def get_nome(self):
        return self.__nome


    def set_nome(self, nome):
        self.__nome = nome
    

    def get_linguagem(self):
        return self.__linguagem


    def set_linguagem(self, linguagem):
        self.__linguagem = linguagem
    
