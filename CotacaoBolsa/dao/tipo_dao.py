from dao.base_dao import BaseDao
from model.tipo_papel import TipoPapel

class TipoPapelDao(BaseDao):
    def __init__(self):
        self.model = TipoPapel
        super().__init__(self.model)