from flask import request
from flask_restful import Resource

from model.rev_frutas import Fruta
from dao.rev_frutas_dao import FrutasDao


class FrutaController(Resource):
    def __init__(self):
        self.dao = FrutasDao()


    def get(self, id=None):
        if (id):
            return self.dao.buscar_por_id(id)
        else:
            return self.dao.listar()


    def post(self):
        nome = request.json['nome']
        preco = request.json['preco']
        fruta = Fruta(nome,preco)
        id_post = self.dao.inserir(fruta)
        return self.dao.buscar_por_id(id_post)


    def delete(self, id):
        try:
            self.dao.deletar(id)
        except:
            return "This id don't exists"
        else:
            return f'id {id} - Deleted'