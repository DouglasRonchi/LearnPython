import sqlalchemy as db
from .base_model import BaseModel

class TipoPapel(BaseModel):
    __tablename__  = 'TIPO_PAPEL'    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))
        
    def __str__(self):
        return f'''
            {{ 
                "id" : {self.id}, 
                "nome" : "{self.nome}",
                "descrição" : "{self.descricao}"
            }}
        '''