from dao.base_dao import BaseDao
from model.papel import Papel

class PapelDao(BaseDao):
    def __init__(self):
        self.model = Papel
        super().__init__(self.model)

    #---- apenas metodo especifico para Papel
    def get_by_cod(self, cod):
        return self.session.query(self.model).filter(self.model.codigo.contains(cod))

    #----- Update
    def update(self, papel:Papel):
        old_obj:Papel = self.get_by_id(papel.id)

        old_obj.codigo = papel.codigo
        old_obj.descricao = papel.descricao
        old_obj.tipo_id = papel.tipo_id
        self.session.commit()
    
    
    
