from flask import Flask
from flask_restful import Api

from controllers.desenvolvedor_controller import DesenvolvedorController
from controllers.banco_de_dados_controller import BancoDeDadosController
from controllers.frontend_controller import FrontEndController
from controllers.linguagem_controller import LinguagemController
from controllers.vaga_controller import VagaController

app = Flask(__name__)
api = Api(app)


#Rota de Desenvolvedor
api.add_resource(DesenvolvedorController, '/api/desenvolvedor', endpoint='desenvolvedores')
api.add_resource(DesenvolvedorController, '/api/desenvolvedor/<int:id>', endpoint='desenvolvedor')

#Rota de Banco de Dados
api.add_resource(BancoDeDadosController, '/api/bancodedados', endpoint='bancosdedados')
api.add_resource(BancoDeDadosController, '/api/bancodedados/<int:id>', endpoint='bancodedados')

#Rota de FrontEnd
api.add_resource(FrontEndController, '/api/frontend', endpoint='frontends')
api.add_resource(FrontEndController, '/api/frontend/<int:id>', endpoint='frontend')

#Rota de Linguagem
api.add_resource(LinguagemController, '/api/linguagem', endpoint='linguagens')
api.add_resource(LinguagemController, '/api/linguagem/<int:id>', endpoint='linguagem')

#Rota de Vagas
api.add_resource(VagaController, '/api/vaga', endpoint='vagas')
api.add_resource(VagaController, '/api/vaga/<int:id>', endpoint='vaga')


app.run(debug=True)