import MySQLdb

class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(
            host='mysql.topskills.study',
            database='topskills08',
            user='topskills08',
            passwd='Douglas2019'
            )
        self.cursor = self.conexao.cursor()


    def inserir(self, com_SQL):
        self.cursor.execute(com_SQL)
        self.conexao.commit()
        return self.cursor.lastrowid


    def alterar(self, com_SQL):
        self.cursor.execute(com_SQL)
        self.conexao.commit()


    def deletar(self, com_SQL):
        self.cursor.execute(com_SQL)
        self.conexao.commit()


    def listar(self, com_SQL):
        self.cursor.execute(com_SQL)
        return self.cursor.fetchall()


    def buscar_por_id(self, com_SQL):
        self.cursor.execute(com_SQL)
        return self.cursor.fetchone()