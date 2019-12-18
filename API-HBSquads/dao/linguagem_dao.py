from dao.base_dao import BaseDao
from model.linguagem import Linguagem


class LinguagemDao(BaseDao):


    def inserir(self, linguagem: Linguagem ):
        comando_sql_insert = f'insert into linguagens value (default, "{linguagem.nome}")'
        return super().inserir(comando_sql_insert)

    def alterar(self, linguagem: Linguagem):
        comando_sql_alterar = f'update linguagens set nm_linguagem = "{linguagem.nome}" where cd_linguagem = "{linguagem.id}"'
        super().alterar(comando_sql_alterar)

    def deletar(self, id):
        comando_sql_deletar = f'delete from linguagens where cd_linguagem = {id}'
        super().inserir(comando_sql_deletar)

    def listar(self):
        retorno = []
        comando_sql_listar = f"select * from linguagens"

        for i in super().listar(comando_sql_listar):
            linguagem = Linguagem(i[1], i[0]).__dict__()
            retorno.append(linguagem)

        return retorno

    def buscar_por_id(self, id):
        comando_sql_buscar = f"select * from linguagens where cd_linguagem = {id}"
        dados = super().buscar_por_id(comando_sql_buscar)
        return Linguagem(dados[1], dados[0])