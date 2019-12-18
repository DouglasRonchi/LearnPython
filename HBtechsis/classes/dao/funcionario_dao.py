from classes.dao.base_dao import BaseDao
from classes.model.funcionario import Funcionario

class FuncionarioDao(BaseDao):
    def listar(self):
        return super().listar('SELECT * FROM hb_funcionarios')


    def buscar_por_id(self, id):
        return super().buscar_por_id(f'SELECT * FROM hb_funcionarios WHERE id = {id}')


    def inserir(self, f:Funcionario):
        super().inserir(f"INSERT INTO hb_funcionarios VALUES(DEFAULT,'{f.get_nome()}','{f.get_cpf()}','{f.get_linguagem()}','{f.get_equipe()}','{f.get_num_registro()}')")


    def alterar(self, f:Funcionario):
        super().alterar(f"UPDATE hb_funcionarios SET nome = '{f.get_nome()}' WHERE id = {f.get_id()}")
        super().alterar(f"UPDATE hb_funcionarios SET cpf = '{f.get_cpf()}' WHERE id = {f.get_id()}")
        super().alterar(f"UPDATE hb_funcionarios SET fk_linguagem = '{f.get_linguagem()}' WHERE id = {f.get_id()}")
        super().alterar(f"UPDATE hb_funcionarios SET fk_equipe = '{f.get_equipe()}' WHERE id = {f.get_id()}")
        super().alterar(f"UPDATE hb_funcionarios SET num_registro = '{f.get_num_registro()}' WHERE id = {f.get_id()}")


    def deletar(self, id):
        super().deletar(f"DELETE FROM hb_funcionarios WHERE id = {id}")
        

    def pegar_ultimo_id(self):
        return super().last_id(f"SELECT id FROM hb_funcionarios ORDER BY id DESC LIMIT 1")
        