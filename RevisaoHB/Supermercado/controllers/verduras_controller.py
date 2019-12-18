from flask import request
from flask_restful import Resource

from model.rev_verduras import Verdura
from dao.rev_verduras_dao import VerdurasDao


class VerduraController(Resource):
    def __init__(self):
        self.dao = VerdurasDao()


    def get(self, id=None):
        if (id):
            return self.dao.buscar_por_id(id)
        else:
            return self.dao.listar()


    def post(self):
        nome = request.json['nome']
        preco = request.json['preco']
        verdura = Verdura(nome,preco)
        id_post = self.dao.inserir(verdura)
        return self.dao.buscar_por_id(id_post)


    def delete(self, id):
        try:
            self.dao.deletar(id)
        except:
            return "This id don't exists"
        else:
            return f'id {id} - Deleted'