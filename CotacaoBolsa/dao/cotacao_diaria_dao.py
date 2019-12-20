from dao.base_dao import BaseDao
from model.cotacao_diaria import CotacaoDiaria

class CotacaoDiariaDao(BaseDao):
    def __init__(self):
        self.model = CotacaoDiaria
        super().__init__(self.model)