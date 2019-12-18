from flask import Flask
from flask_restful import Api

from controllers.frutas_controller import FrutaController
from controllers.verduras_controller import VerduraController
from controllers.legumes_controller import LegumeController
from controllers.lista_mercado_controller import MercadoController


app = Flask(__name__)
api = Api(app)


api.add_resource(FrutaController, "/api/fruta", endpoint="frutas")
api.add_resource(FrutaController, "/api/fruta/<int:id>", endpoint="fruta")


api.add_resource(VerduraController, "/api/verdura", endpoint="verduras")
api.add_resource(VerduraController, "/api/verdura/<int:id>", endpoint="verdura")


api.add_resource(LegumeController, "/api/legume", endpoint="legumes")
api.add_resource(LegumeController, "/api/legume/<int:id>", endpoint="legume")

api.add_resource(MercadoController, "/api/lista_mercado", endpoint="mercado")


app.run(debug=True)