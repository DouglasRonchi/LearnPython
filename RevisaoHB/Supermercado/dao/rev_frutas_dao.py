from dao.base_dao import BaseDao
from model.rev_frutas import Fruta


class FrutasDao(BaseDao):
    def inserir(self, fruta:Fruta):
        sql = f"INSERT INTO rev_frutas VALUES (DEFAULT, '{fruta.nome}','{fruta.preco}')"
        return super().inserir(sql)


    def alterar(self, fruta:Fruta):
        sql = f"UPDATE rev_frutas SET nome = '{fruta.nome}' WHERE id = {fruta.id}"
        super().alterar(sql)
        sql = f"UPDATE rev_frutas SET preco = '{fruta.preco}' WHERE id = {fruta.id}"
        super().alterar(sql)
        return 'Alterado com Sucesso'


    def deletar(self, id):
        sql = f"DELETE FROM rev_frutas WHERE id = {id}"
        super().deletar(sql)
        return 'Deletado com Sucesso'


    def listar(self):
        lista_frutas = []
        sql = 'SELECT F.nome, F.preco, F.id  FROM rev_frutas as F'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            fruta = Fruta(l[0],l[1],l[2]).__dict__()
            lista_frutas.append(fruta)
        return lista_frutas


    def buscar_por_id(self, id):
        sql = f'SELECT F.nome, F.preco, F.id  FROM rev_frutas as F WHERE F.id = {id}'
        l = super().buscar_por_id(sql)
        fruta = Fruta(l[0],l[1],l[2])
        return fruta.__dict__()

    