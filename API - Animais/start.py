from flask import Flask
from flask_restful import Api
from controllers.animais_controller import AnimaisController
from controllers.especies_controller import EspeciesController


app = Flask(__name__)
api = Api(app)


#Rotas para Animais
api.add_resource(AnimaisController, '/api/animais', endpoint='animais')

api.add_resource(AnimaisController, '/api/animais/<int:id>', endpoint='animal')


#Rotas para Especies
api.add_resource(EspeciesController, '/api/especies', endpoint='especies')

api.add_resource(EspeciesController, '/api/especies/<int:id>', endpoint='especie')


app.run(host='0.0.0.0',debug=True)
