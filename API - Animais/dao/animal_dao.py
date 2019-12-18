from dao.base_dao import BaseDao
from model.animal import Animal
from model.animal import EspecieAnimais

class AnimalDao(BaseDao):
    def inserir(self, animal:Animal):
        sql = f"INSERT INTO Animais VALUES (DEFAULT, '{animal.nome}','{animal.especie.id}')"
        return super().inserir(sql)


    def alterar(self, animal:Animal):
        sql = f"UPDATE Animais SET Nome = '{animal.nome}' WHERE id = {animal.id}"
        super().alterar(sql)
        sql = f"UPDATE Animais SET Especie = {animal.especie.id} WHERE id = {animal.id}"
        super().alterar(sql)
        return 'Alterado com Sucesso'


    def deletar(self, id):
        sql = f"DELETE FROM Animais WHERE id = {id}"
        super().deletar(sql)
        return 'Deletado com Sucesso'


    def listar(self):
        lista_animais = []
        sql = 'SELECT A.Nome, A.Especie, A.id, E.Tipo, E.id  FROM Animais as A JOIN Especie_Animais as E ON A.Especie = E.id'
        lista_tuplas = super().listar(sql)
        for l in lista_tuplas:
            especie = EspecieAnimais(l[3],l[4])
            animal = Animal(l[0],especie.__dict__,l[2])
            lista_animais.append(animal.__dict__)
        return lista_animais


    def buscar_por_id(self, id):
        sql = f'SELECT A.Nome, A.Especie, A.id, E.Tipo, E.id  FROM Animais as A JOIN Especie_Animais as E ON A.Especie = E.id WHERE A.id = {id}'
        l = super().buscar_por_id(sql)
        especie = EspecieAnimais(l[3],l[4])
        animal = Animal(l[0],especie.__dict__,l[2])
        return animal.__dict__