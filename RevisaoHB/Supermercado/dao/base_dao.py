import MySQLdb

class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(
            host='mysql.topskills.study',
            database='topskills08',
            user='topskills08',
            passwd='Douglas2019')
        self.cursor = self.conexao.cursor()

    def listar(self, comSQL):
        self.cursor.execute(comSQL)
        return self.cursor.fetchall()
        

    def buscar_por_id(self, comSQL):
        self.cursor.execute(comSQL)
        return self.cursor.fetchone()


    def inserir(self, comSQL):
        self.cursor.execute(comSQL)
        self.conexao.commit()
        id_gerado = self.cursor.lastrowid
        return id_gerado


    def alterar(self, comSQL):
        self.cursor.execute(comSQL)
        self.conexao.commit()


    def deletar(self, comSQL):
        self.cursor.execute(comSQL)
        self.conexao.commit()
