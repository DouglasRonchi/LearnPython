from model.especie_animais import EspecieAnimais

class Animal:
    def __init__(self, nome, especie:EspecieAnimais, id=None):
        self.id = id
        self.nome = nome
        self.especie = especie


