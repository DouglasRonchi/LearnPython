import MySQLdb

class BaseDao:
    def __init__(self):
        self.conn = MySQLdb.connect(host = 'mysql.topskills.study', database = 'topskills08', user = 'topskills08', password = 'Douglas2019')
        self.cursor = self.conn.cursor()


    def listar(self, com_SQL):
        self.cursor.execute(com_SQL)
        return self.cursor.fetchall()


    def buscar_por_id(self, com_SQL):
        self.cursor.execute(com_SQL)
        return self.cursor.fetchone()


    def inserir(self, com_SQL):
        self.cursor.execute(com_SQL)
        self.conn.commit()


    def alterar(self, com_SQL):
        self.cursor.execute(com_SQL)
        self.conn.commit()


    def deletar(self, com_SQL):
        self.cursor.execute(com_SQL)
        self.conn.commit()

    def pegar_ultimo_id(self, com_SQL):
        return self.cursor.execute(com_SQL)
