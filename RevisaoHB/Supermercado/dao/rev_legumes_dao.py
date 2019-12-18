from dao.base_dao import BaseDao
from model.rev_legumes import Legume

class LegumesDao(BaseDao):
    def inserir(self, legume:Legume):
        sql = f"INSERT INTO rev_legumes VALUES (DEFAULT, '{legume.nome}','{legume.preco}')"
        return super().inserir(sql)


    def alterar(self, legume:Legume):
        sql = f"UPDATE rev_legumes SET nome = '{legume.nome}' WHERE id = {legume.id}"
        super().alterar(sql)
        sql = f"UPDATE rev_legumes SET preco = {legume.preco} WHERE id = {legume.id}"
        super().alterar(sql)
        return 'Alterado com Sucesso'


    def deletar(self, id):
        sql = f"DELETE FROM rev_legumes WHERE id = {id}"
        super().deletar(sql)
        return 'Deletado com Sucesso'


    def listar(self):
        lista_legumes = []
        sql = 'SELECT L.nome, L.preco, L.id  FROM rev_legumes as L'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            legume = Legume(l[0],l[1],l[2])
            lista_legumes.append(legume.__dict__())
        return lista_legumes


    def buscar_por_id(self, id):
        sql = f'SELECT L.nome, L.preco, L.id  FROM rev_legumes as L WHERE L.id = {id}'
        l = super().buscar_por_id(sql)
        legume = Legume(l[0],l[1],l[2]).__dict__()
        return legume