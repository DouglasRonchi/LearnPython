from flask_restful import Resource
from flask import request
from model.especie_animais import EspecieAnimais
from dao.especie_animal_dao import EspecieAnimalDao

class EspeciesController(Resource):
    def __init__(self):
        self.dao = EspecieAnimalDao()

    def get(self, id=None):
        if (id):
            return self.dao.buscar_por_id(id)
        else:
            return self.dao.listar()

    def post(self):
        #Resgatando Valores do POST
        especie_tipo = request.json["tipo"]

        #Instanciando um Objeto para Inserir
        especie = EspecieAnimais(especie_tipo)
        especie_id = self.dao.inserir(especie)
        return self.dao.buscar_por_id(especie_id)

    def put(self, id):
        especie_id = id
        especie_tipo = request.json['tipo']
        especie = EspecieAnimais(especie_tipo,especie_id)
        return self.dao.alterar(especie)

    def delete(self, id):
        return self.dao.deletar(id)
