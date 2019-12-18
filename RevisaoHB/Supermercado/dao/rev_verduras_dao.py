from dao.base_dao import BaseDao
from model.rev_verduras import Verdura

class VerdurasDao(BaseDao):
    def inserir(self, verdura:Verdura):
        sql = f"INSERT INTO rev_verduras VALUES (DEFAULT, '{verdura.nome}','{verdura.preco}')"
        return super().inserir(sql)


    def alterar(self, verdura:Verdura):
        sql = f"UPDATE rev_verduras SET nome = '{verdura.nome}' WHERE id = {verdura.id}"
        super().alterar(sql)
        sql = f"UPDATE rev_verduras SET preco = {verdura.preco} WHERE id = {verdura.id}"
        super().alterar(sql)
        return 'Alterado com Sucesso'


    def deletar(self, id):
        sql = f"DELETE FROM rev_verduras WHERE id = {id}"
        super().deletar(sql)
        return 'Deletado com Sucesso'


    def listar(self):
        lista_verduras = []
        sql = 'SELECT V.nome, V.preco, V.id  FROM rev_verduras as V'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            verdura = Verdura(l[0],l[1],l[2])
            lista_verduras.append(verdura.__dict__())
        return lista_verduras


    def buscar_por_id(self, id):
        sql = f'SELECT V.nome, V.preco, V.id  FROM rev_verduras as V WHERE V.id = {id}'
        l = super().buscar_por_id(sql)
        verdura = Verdura(l[0],l[1],l[2])
        return verdura.__dict__()