from dao.base_dao import BaseDao
from model.tipo_rendimento import TipoRendimento

class TipoRendimentoDao(BaseDao):
    def __init__(self):
        self.model = TipoRendimento
        super().__init__(self.model)