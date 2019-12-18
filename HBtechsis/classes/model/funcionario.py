from classes.model.pessoa import Pessoa
from classes.model.linguagens import Linguagens
from classes.model.equipe import Equipe


class Funcionario(Pessoa):
    __linguagem = Linguagens
    __equipe = Equipe
    __num_registro = 0

    def get_linguagem(self):
        return self.__linguagem

    
    def set_linguagem(self, linguagem):
        self.__linguagem = linguagem


    def get_equipe(self):
        return self.__equipe


    def set_equipe(self, equipe):
        self.__equipe = equipe
    

    def get_num_registro(self):
        return self.__num_registro


    def set_num_registro(self, num_registro):
        self.__num_registro = num_registro