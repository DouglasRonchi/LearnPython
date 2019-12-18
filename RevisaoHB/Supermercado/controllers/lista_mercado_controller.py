from flask import request
from flask_restful import Resource

from dao.rev_mercado_dao import MercadoDao


class MercadoController(Resource):
    def __init__(self):
        self.dao = MercadoDao()


    def get(self):
        return self.dao.listar()

