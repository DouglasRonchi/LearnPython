from flask import request
from flask_restful import Resource
from model.animal import Animal
from dao.animal_dao import AnimalDao
from model.especie_animais import EspecieAnimais

class AnimaisController(Resource):
    def __init__(self):
        self.dao = AnimalDao()

    def get(self, id=None):
        if (id):
            return self.dao.buscar_por_id(id)
        else:
            return self.dao.listar()

    def post(self):
        #Resgatando Valores do POST
        especie_id = request.json["especie_id"]
        animal_nome = request.json["nome"]

        #Instanciando um Objeto para Inserir
        especie = EspecieAnimais('', especie_id)
        animal = Animal(animal_nome, especie)
        animal_id = self.dao.inserir(animal)
        return self.dao.buscar_por_id(animal_id)
        

    def put(self, id):
        animal_id = id
        animal_nome = request.json['animal_nome']
        animal_especie_id = request.json['animal_especie']
        especie = EspecieAnimais('',animal_especie_id)
        animal = Animal(animal_nome,especie,animal_id)
        return self.dao.alterar(animal)

    def delete(self, id):
        return self.dao.deletar(id)