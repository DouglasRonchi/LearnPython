from flask import request
from flask_restful import Resource

from model.frontend import FrontEnd
from dao.frontend_dao import FrontendDao


class FrontEndController(Resource):
    def __init__(self):
        self.dao = FrontendDao()


    def get(self, id=None):
        if (id):
            return self.dao.buscar_por_id(id).__dict__()
        else:
            return self.dao.listar()


    def post(self):
        nome = request.json['nome']
        bd = FrontEnd(nome)
        id_post = self.dao.inserir(bd)
        return self.dao.buscar_por_id(id_post).__dict__()


    def delete(self, id):
        try:
            self.dao.deletar(id)
        except:
            return "This id don't exists"
        else:
            return f'id {id} - Deleted'