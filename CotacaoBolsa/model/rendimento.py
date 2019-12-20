import sqlalchemy as db
from .base_model import BaseModel
from sqlalchemy.orm import relationship

from model.papel import Papel
from model.tipo_rendimento import TipoRendimento


class Rendimento(BaseModel):
    __tablename__  = 'RENDIMENTO'        
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float)
    data_pagamento = db.Column(db.Date)

    papel_id = db.Column(db.Integer, db.ForeignKey('PAPEL.id') )
    papel = relationship(Papel)

    tipo_rendimento_id = db.Column(db.Integer, db.ForeignKey('TIPO_RENDIMENTO.id') )
    tipo_rendimento = relationship(TipoRendimento)
        
    def __str__(self):
        return f'''
        {{
            "id" : {self.id}, 
            "valor" : "{self.valor}", 
            "data_pagamento" : "{self.data_pagamento}", 
            "papel" : 
                {self.papel}
            "tipo_rendimento" : 
                {self.tipo_rendimento}
        }}
        '''