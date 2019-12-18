from dao.base_dao import BaseDao

from model.rev_frutas import Fruta
from model.rev_verduras import Verdura
from model.rev_legumes import Legume


class MercadoDao(BaseDao):

    def listar(self):
        lista_mercado = []
        lista_legumes = []
        sql = 'SELECT L.nome, L.preco, L.id  FROM rev_legumes as L'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            legume = Legume(l[0],l[1],l[2])
            lista_legumes.append(legume.__dict__())
        lista_mercado.append(lista_legumes)
        
        lista_frutas = []
        sql = 'SELECT F.nome, F.preco, F.id  FROM rev_frutas as F'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            fruta = Fruta(l[0],l[1],l[2])
            lista_frutas.append(fruta.__dict__())
        lista_mercado.append(lista_frutas)

        lista_verduras = []
        sql = 'SELECT V.nome, V.preco, V.id  FROM rev_verduras as V'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            verdura = Verdura(l[0],l[1],l[2])
            lista_verduras.append(verdura.__dict__())
        lista_mercado.append(lista_verduras)
        
        return lista_mercado

