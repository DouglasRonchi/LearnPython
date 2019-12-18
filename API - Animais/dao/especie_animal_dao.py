from dao.base_dao import BaseDao
from model.especie_animais import EspecieAnimais

class EspecieAnimalDao(BaseDao):
    def inserir(self, especie:EspecieAnimais):
        sql = f"INSERT INTO Especie_Animais VALUES (DEFAULT, '{especie.tipo}')"
        return super().inserir(sql)


    def alterar(self, especie:EspecieAnimais):
        sql = f"UPDATE Especie_Animais SET Tipo = '{especie.tipo}' WHERE id = {especie.id}"
        super().alterar(sql)
        return f'ID {especie.id} - Alterado com Sucesso'


    def deletar(self, id):
        sql = f"DELETE FROM Especie_Animais WHERE id = {id}"
        super().deletar(sql)
        return f'ID {id} - Deletado com Sucesso'


    def listar(self):
        lista_especies = []
        sql = 'SELECT E.Tipo, E.id  FROM Especie_Animais as E'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            especie = EspecieAnimais(l[0],l[1])
            lista_especies.append(especie.__dict__)
        return lista_especies


    def buscar_por_id(self, id):
        sql = f'SELECT E.Tipo, E.id  FROM Especie_Animais as E WHERE E.id = {id}'
        l = super().buscar_por_id(sql)
        especie = EspecieAnimais(l[0],l[1])
        return especie.__dict__