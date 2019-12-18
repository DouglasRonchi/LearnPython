from dao.base_dao import BaseDao
from model.vaga import Vaga
from model.banco_de_dados import BancoDeDados
from model.desenvolvedor import Deselvolvedor
from model.frontend import FrontEnd
from model.linguagem import Linguagem


class VagaDao(BaseDao):

    def inserir(self, vaga: Vaga):
        comando_sql_insert = f'insert into vagas value (default, "{vaga.desenvolvedor.id}", "{vaga.linguagem.id}", "{vaga.banco_de_dados.id}", "{vaga.frontend.id}")'
        return super().inserir(comando_sql_insert)

    def alterar(self, vaga: Vaga):
        raise NotImplementedError
        # comando_sql_alterar = f'update linguagens set nm_linguagem = "{linguagem.nome}" where cd_linguagem = "{linguagem.id}"'
        # super().alterar(comando_sql_alterar)

    def deletar(self, id):
        comando_sql_deletar = f'delete from vagas where cd_vaga = {id}'
        super().inserir(comando_sql_deletar)

    def listar(self):
        retorno = []
        comando_sql_listar = f"""
                            select bd.nm_banco_de_dados, bd.cd_banco_de_dados, 
                                        d.nm_desenvolvedor, d.cd_desenvolvedor,
                                        f.nm_frontend, f.cd_frontend,
                                        l.nm_linguagem, l.cd_linguagem,
                                        v.cd_vaga
                            from vagas v
                            inner join bancos_de_dados bd on bd.cd_banco_de_dados = v.fk_banco_de_dados
                            inner join desenvolvedores d on d.cd_desenvolvedor = v.fk_desenvolvedor
                            inner join frontends f on f.cd_frontend = v.fk_frontend
                            inner join linguagens l on l.cd_linguagem = v.fk_linguagem"""

        for i in super().listar(comando_sql_listar):
            banco_de_dados = BancoDeDados(i[0], i[1]).__dict__()
            dev = Deselvolvedor(i[2], i[3]).__dict__()
            front = FrontEnd(i[4], i[5]).__dict__()
            linguagem = Linguagem(i[6], i[7]).__dict__()
            vaga = Vaga(dev, linguagem, banco_de_dados, front, i[8])
            retorno.append(vaga.__dict__())

        return retorno

    def buscar_por_id(self, id):
        comando_sql_buscar = f"""select bd.nm_banco_de_dados, bd.cd_banco_de_dados, 
                                        d.nm_desenvolvedor, d.cd_desenvolvedor,
                                        f.nm_frontend, f.cd_frontend,
                                        l.nm_linguagem, l.cd_linguagem,
                                        v.cd_vaga
                            from vagas v
                            inner join bancos_de_dados bd on bd.cd_banco_de_dados = v.fk_banco_de_dados
                            inner join desenvolvedores d on d.cd_desenvolvedor = v.fk_desenvolvedor
                            inner join frontends f on f.cd_frontend = v.fk_frontend
                            inner join linguagens l on l.cd_linguagem = v.fk_linguagem
                            where cd_vaga = {id}"""
        i = super().buscar_por_id(comando_sql_buscar)
        banco_de_dados = BancoDeDados(i[0], i[1]).__dict__()
        dev = Deselvolvedor(i[2], i[3]).__dict__()
        front = FrontEnd(i[4], i[5]).__dict__()
        linguagem = Linguagem(i[6], i[7]).__dict__()
        vaga = Vaga(dev, linguagem, banco_de_dados, front, i[8]).__dict__()
        return vaga

    def has_desenvolvedor(self, id):
        sql = f"select * from vagas v where fk_desenvolvedor = {id}"
        dev = super().buscar_por_id(sql)
        return (True if dev else False)

    def has_frontend(self, id):
        sql = f"select * from vagas v where fk_frontend = {id}"
        front = super().buscar_por_id(sql)
        return (True if front else False)


    def has_banco_de_dados(self, id):
        sql = f"select * from vagas v where fk_banco_de_dados = {id}"
        bd = super().buscar_por_id(sql)
        return (True if bd else False)


    def has_linguagem(self, id):
        sql = f"select * from vagas v where fk_linguagem = {id}"
        linguagem = super().buscar_por_id(sql)
        return (True if linguagem else False)
        