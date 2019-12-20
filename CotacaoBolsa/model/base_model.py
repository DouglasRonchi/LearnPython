#===== Criando classe para mapeamento de uma tabela do banco de dados
#----- Importação de uma função para gerar a classe base do alchemy e utilizá-la nas classes de modelo
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
