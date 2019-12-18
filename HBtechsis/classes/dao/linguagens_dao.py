from classes.dao.base_dao import BaseDao
from classes.model.linguagens import Linguagens

class LinguagensDao(BaseDao):
    base = BaseDao()


    def listar(self):
        return super().listar('SELECT * FROM hb_linguagens')


    def buscar_por_id(self, id):
        return super().buscar_por_id(f'SELECT * FROM hb_linguagens WHERE id = {id}')


    def inserir(self, l:Linguagens):
        super().inserir(f"INSERT INTO hb_linguagens VALUES(DEFAULT,'{l.get_nome()}','{l.get_descricao()}')")


    def alterar(self, l:Linguagens):
        super().alterar(f"UPDATE hb_linguagens SET nome = '{l.get_nome()}' WHERE id = {l.get_id()}")
        super().alterar(f"UPDATE hb_linguagens SET descricao = '{l.get_descricao()}' WHERE id = {l.get_id()}")


    def deletar(self, id):
        super().deletar(f"DELETE FROM hb_linguagens WHERE id = {id}")
        

    def pegar_ultimo_id(self):
        return super().last_id(f"SELECT id FROM hb_linguagens ORDER BY id DESC LIMIT 1")
        