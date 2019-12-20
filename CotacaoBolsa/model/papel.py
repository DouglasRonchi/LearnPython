import sqlalchemy as db
from .base_model import BaseModel
from sqlalchemy.orm import relationship

from model.tipo_papel import TipoPapel

class Papel(BaseModel):
    __tablename__  = 'PAPEL'        
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))
    tipo_id = db.Column(db.Integer, db.ForeignKey('TIPO_PAPEL.id') )
    tipo_papel = relationship(TipoPapel)
        
    def __str__(self):
        return f'''
        {{
            "id" : {self.id}, 
            "codigo" : "{self.codigo}", 
            "descrição" : "{self.descricao}", 
            "tipo_id" :{self.tipo_id}
        }}
        '''
        