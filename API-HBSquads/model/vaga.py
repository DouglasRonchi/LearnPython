from model.desenvolvedor import Deselvolvedor
from model.linguagem import Linguagem
from model.banco_de_dados import BancoDeDados
from model.frontend import FrontEnd

class Vaga:
    def __init__(self, desenvolvedor:Deselvolvedor, linguagem:Linguagem, banco_de_dados:BancoDeDados, frontend:FrontEnd, id=None):
        self.__desenvolvedor = desenvolvedor
        self.__linguagem = linguagem
        self.__banco_de_dados = banco_de_dados
        self.__frontend = frontend
        self.__id = id

    @property
    def desenvolvedor(self):
        return self.__desenvolvedor
    
    @desenvolvedor.setter
    def desenvolvedor(self, desenvolvedor):
        self.__desenvolvedor = desenvolvedor


    @property
    def linguagem(self):
        return self.__linguagem
    
    @linguagem.setter
    def linguagem(self, linguagem):
        self.__linguagem = linguagem


    @property
    def banco_de_dados(self):
        return self.__banco_de_dados
    
    @banco_de_dados.setter
    def banco_de_dados(self, banco_de_dados):
        self.__banco_de_dados = banco_de_dados


    @property
    def frontend(self):
        return self.__frontend
    
    @frontend.setter
    def frontend(self, frontend):
        self.__frontend = frontend


    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id


    def __dict__(self):
        return {
            "desenvolvedor":self.desenvolvedor,
            "linguagem":self.linguagem,
            "banco_de_dados":self.banco_de_dados,
            "frontend":self.frontend,
            "id":self.id
        }