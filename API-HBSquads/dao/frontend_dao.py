from dao.base_dao import BaseDao
from model.frontend import FrontEnd


class FrontendDao(BaseDao):

    def inserir(self, frontend: FrontEnd ):
        comando_sql_insert = f'insert into frontends value (default, "{frontend.nome}")'
        return super().inserir(comando_sql_insert)

    def alterar(self, frontend: FrontEnd):
        comando_sql_alterar = f'update frontends set nm_frontend = "{frontend.nome}" where cd_frontend = "{frontend.id}"'
        super().alterar(comando_sql_alterar)

    def deletar(self, id):
        comando_sql_deletar = f'delete from frontends where cd_frontend = {id}'
        super().inserir(comando_sql_deletar)

    def listar(self):
        retorno = []
        comando_sql_listar = f"select * from frontends"

        for i in super().listar(comando_sql_listar):
            frontend = FrontEnd(i[1], i[0]).__dict__()
            retorno.append(frontend)

        return retorno

    def buscar_por_id(self, id):
        comando_sql_buscar = f"select * from frontends where cd_frontend = {id}"
        dados = super().buscar_por_id(comando_sql_buscar)
        return FrontEnd(dados[1], dados[0])