from classes.dao.base_dao import BaseDao
from classes.model.equipe import Equipe

class EquipeDao(BaseDao):
    def listar(self):
        return super().listar('SELECT * FROM hb_equipes')


    def buscar_por_id(self, id):
        return super().buscar_por_id(f'SELECT * FROM hb_equipes WHERE id = {id}')


    def inserir(self, e:Equipe):
        super().inserir(f"INSERT INTO hb_equipes VALUES(DEFAULT,'{e.get_nome()}','{e.get_linguagem()}')")


    def alterar(self, e:Equipe):
        super().alterar(f"UPDATE hb_equipes SET nome = '{e.get_nome()}' WHERE id = {e.get_id()}")
        super().alterar(f"UPDATE hb_equipes SET fk_linguagem = '{e.get_linguagem()}' WHERE id = {e.get_id()}")


    def deletar(self, id):
        super().deletar(f"DELETE FROM hb_equipes WHERE id = {id}")
        

    def pegar_ultimo_id(self):
        return super().last_id(f"SELECT id FROM hb_equipes ORDER BY id DESC LIMIT 1")
        