from flask import request
from flask_restful import Resource

from model.linguagem import Linguagem
from dao.linguagem_dao import LinguagemDao


class LinguagemController(Resource):
    def __init__(self):
        self.dao = LinguagemDao()


    def get(self, id=None):
        if (id):
            return self.dao.buscar_por_id(id).__dict__()
        else:
            return self.dao.listar()


    def post(self):
        nome = request.json['nome']
        ling = Linguagem(nome)
        id_post = self.dao.inserir(ling)
        return self.dao.buscar_por_id(id_post).__dict__()


    def delete(self, id):
        try:
            self.dao.deletar(id)
        except:
            return "This id don't exists"
        else:
            return f'id {id} - Deleted'