from dao.base_dao import BaseDao
from model.desenvolvedor import Deselvolvedor


class DesenvolvedorDao(BaseDao):

    def inserir(self, desenvolvedor: Deselvolvedor ):
        comando_sql_insert = f'insert into desenvolvedores value (default, "{desenvolvedor.nome}")'
        return super().inserir(comando_sql_insert)

    def alterar(self, desenvolvedor: Deselvolvedor):
        comando_sql_alterar = f'update desenvolvedores set nm_desenvolvedor = "{desenvolvedor.nome}" where cd_desenvolvedor = "{desenvolvedor.id}"'
        super().alterar(comando_sql_alterar)

    def deletar(self, id):
        comando_sql_deletar = f'delete from desenvolvedores where cd_desenvolvedor = {id}'
        super().inserir(comando_sql_deletar)

    def listar(self):
        retorno = []
        comando_sql_listar = f"select * from desenvolvedores"

        for i in super().listar(comando_sql_listar):
            desenvolvedor = Deselvolvedor(i[1], i[0]).__dict__()
            retorno.append(desenvolvedor)
        return retorno

    def buscar_por_id(self, id):
        comando_sql_buscar = f"select * from desenvolvedores where cd_desenvolvedor = {id}"
        dados = super().buscar_por_id(comando_sql_buscar)
        return Deselvolvedor(dados[1], dados[0])