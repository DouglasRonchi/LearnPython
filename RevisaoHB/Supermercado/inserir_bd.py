from dao.rev_frutas_dao import FrutasDao
from dao.rev_verduras_dao import VerdurasDao
from dao.rev_legumes_dao import LegumesDao

from model.rev_frutas import Fruta
from model.rev_verduras import Verdura
from model.rev_legumes import Legume


lista = [
    ['frutas','verduras','legumes','preço'],
    ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
    ['alface crespa', 'alface lisa','rucula','almeirão','repolho','salsinha','couve'],
    ['feijão', 'ervinha', 'lentilha','vagem','feijão branco','grão de bico','soja'],
    [ 
        [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75],
        [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
        [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
    ]
]

dao_fruta = FrutasDao()
dao_verdura = VerdurasDao()
dao_legume = LegumesDao()

def inserir_no_banco():
    #Fruta
    for i in range(7):
        fruta = Fruta(lista[1][i], lista[4][0][i])
        dao_fruta.inserir(fruta)


    #Verdura
    for i in range(7):
        verdura = Verdura(lista[2][i], lista[4][1][i])
        dao_verdura.inserir(verdura)


    #Legume
    for i in range(7):
        legume = Legume(lista[3][i], lista[4][2][i])
        dao_legume.inserir(legume)

inserir_no_banco()