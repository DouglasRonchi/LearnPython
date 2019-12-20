from dao.base_dao import BaseDao
from model.rendimento import Rendimento

class RendimentoDao(BaseDao):
    def __init__(self):
        self.model = Rendimento
        super().__init__(self.model)