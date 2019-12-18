import MySQLdb

class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(host="mysql.topskills.study", database="topskills08", user="topskills08", passwd="Douglas2019" )
        self.cursor = self.conexao.cursor()

    def inserir(self, comando_sql_insert):
        self.cursor.execute(comando_sql_insert)
        self.conexao.commit()
        id_gerado = self.cursor.lastrowid
        return id_gerado

    def alterar(self, comando_sql_alterar):
        self.cursor.execute(comando_sql_alterar)
        self.conexao.commit()
    
    def deletar(self, comando_sql_delete):
        self.cursor.execute(comando_sql_delete)
        self.conexao.commit()

    def listar(self, comando_sql_listar):
        self.cursor.execute(comando_sql_listar)
        return self.cursor.fetchall()

    def buscar_por_id(self, comando_sql_buscar_id):
        self.cursor.execute(comando_sql_buscar_id)
        return self.cursor.fetchone()

