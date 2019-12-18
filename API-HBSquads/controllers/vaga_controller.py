from flask import request
from flask_restful import Resource

from model.vaga import Vaga
from model.desenvolvedor import Deselvolvedor
from model.frontend import FrontEnd
from model.linguagem import Linguagem
from model.banco_de_dados import BancoDeDados

from dao.vaga_dao import VagaDao
from dao.desenvolvedor_dao import DesenvolvedorDao
from dao.frontend_dao import FrontendDao
from dao.linguagem_dao import LinguagemDao
from dao.banco_de_dados_dao import BancoDeDadosDao


class VagaController(Resource):
    def __init__(self):
        self.dao_vaga = VagaDao()
        self.dao_dev = DesenvolvedorDao()
        self.dao_front = FrontendDao()
        self.dao_ling = LinguagemDao()
        self.dao_bd = BancoDeDadosDao()


    def get(self, id=None):
        if (id):
            return self.dao_vaga.buscar_por_id(id)
        else:
            return self.dao_vaga.listar()


    def post(self):
        desenvolvedor = self.dao_dev.buscar_por_id(request.json['desenvolvedor_id'])
        front = self.dao_front.buscar_por_id(request.json['frontend_id'])
        linguagem = self.dao_ling.buscar_por_id(request.json['linguagem_id'])
        banco_de_dados = self.dao_bd.buscar_por_id(request.json['bancodedados_id'])
        
        
        #Regras

        #Verificando se ja existe cadastrado algum item
        if self.dao_vaga.has_desenvolvedor(desenvolvedor.id):
            return f"{desenvolvedor.nome} ja esta cadastrado"

        if self.dao_vaga.has_frontend(front.id):
            return f"{front.nome} ja esta cadastrado"

        if self.dao_vaga.has_linguagem(linguagem.id):
            return f"{linguagem.nome} ja esta cadastrado"

        if self.dao_vaga.has_banco_de_dados(banco_de_dados.id):
            return f"{banco_de_dados.nome} ja esta cadastrado"
        
        #Regras Gerais
        if desenvolvedor.nome == "Nicole" and front.nome == "VUE":
            return 'Nicole nao possui habilidades em VUE'

        if linguagem.nome == "Java" and banco_de_dados.nome != "PostgreSQL":
            return "Quem trabalha com Java possui conhecimento em PostgreSQL"

        if front.nome == "Angular" and banco_de_dados.nome != "MongoDB":
            return "Quam trabalha com Angular deve usar MongoDB"

        if desenvolvedor.nome == "Mateus" and linguagem.nome != "Python":
            return "Mateus trabalha com Python"

        if desenvolvedor.nome == "Tiago" and linguagem.nome == "PHP":
            return "Tiago nao possui habilidade em PHP"

        vaga = Vaga(desenvolvedor,linguagem,banco_de_dados,front)
        id_post = self.dao_vaga.inserir(vaga)
        return self.dao_vaga.buscar_por_id(id_post)


    def delete(self, id):
        try:
            self.dao_vaga.deletar(id)
        except:
            return "This id don't exists"
        else:
            return f'id {id} - Deleted'