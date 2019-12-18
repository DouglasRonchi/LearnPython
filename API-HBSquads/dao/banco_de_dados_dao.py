from dao.base_dao import BaseDao
from model.banco_de_dados import BancoDeDados

class BancoDeDadosDao(BaseDao):

    def inserir(self, banco_de_dados: BancoDeDados):
        comando_sql_insert = f'insert into bancos_de_dados value (default, "{banco_de_dados.nome}")'
        return super().inserir(comando_sql_insert)

    def alterar(self, banco_de_dados: BancoDeDados):
        comando_sql_alterar = f'update bancos_de_dados set nm_banco_de_dados = "{banco_de_dados.nome}" where cd_banco_de_dados = "{banco_de_dados.id}"'
        super().alterar(comando_sql_alterar)

    def deletar(self, id):
        comando_sql_deletar = f'delete from bancos_de_dados where cd_banco_de_dados = {id}'
        super().inserir(comando_sql_deletar)

    def listar(self):
        retorno = []
        comando_sql_listar = f"select * from bancos_de_dados"

        for i in super().listar(comando_sql_listar):
            banco_de_dados = BancoDeDados(i[1], i[0]).__dict__()
            retorno.append(banco_de_dados)

        return retorno

    def buscar_por_id(self, id):
        comando_sql_buscar = f"select * from bancos_de_dados where cd_banco_de_dados = {id}"
        dados = super().buscar_por_id(comando_sql_buscar)
        return BancoDeDados(dados[1], dados[0])
