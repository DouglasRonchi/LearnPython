import sqlalchemy as db
from .base_model import BaseModel
from sqlalchemy.orm import relationship

from model.papel import Papel

class CotacaoDiaria(BaseModel):
    __tablename__  = 'COTACAO_DIARIA'        
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    valor_abertura = db.Column(db.Float)
    valor_fechamento = db.Column(db.Float)
    lpa = db.Column(db.Float)
    pl = db.Column(db.Float)
    papel_id = db.Column(db.Integer, db.ForeignKey('PAPEL.id') )
    papel = relationship(Papel)

        
    def __str__(self):
        return f'''
        {{
            "id" : {self.id}, 
            "data" : "{self.data}", 
            "valor_abertura" : "{self.valor_abertura}", 
            "valor_fechamento" :{self.valor_fechamento}, 
            "lpa" :{self.lpa}, 
            "pl" :{self.pl}, 
            "papel" : 
                {self.papel}
        }}'''