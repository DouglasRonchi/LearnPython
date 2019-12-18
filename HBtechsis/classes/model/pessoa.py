class Pessoa:
    __id = 'DEFAULT'
    __nome = ''
    __cpf = ''


    def get_id(self):
        return self.__id

    
    def set_id(self, id):
        self.__id = id


    def get_nome(self):
        return self.__nome


    def set_nome(self, nome):
        self.__nome = nome
    

    def get_cpf(self):
        return self.__cpf


    def set_cpf(self, cpf):
        self.__cpf = cpf