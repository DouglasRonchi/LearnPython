import sys
sys.path.append('/home/douglas/Desktop/PythonDD - GIT/PythonDD/CotacaoBolsa')

from model.papel import Papel
from model.cotacao_diaria import CotacaoDiaria
from dao.papel_dao import PapelDao
from dao.tipo_dao import TipoPapelDao
from dao.tipo_rendimento_dao import TipoRendimentoDao
from dao.rendimento_dao import RendimentoDao
from dao.cotacao_diaria_dao import CotacaoDiariaDao

dao = PapelDao()
dao_tipo = TipoPapelDao()
#---------------  Cotacao Diaria
dao_cd = CotacaoDiariaDao()


#Codigo - Descricao - Valor Fechamento -  LPA - PL
lista_busca = dao_cd.list_all()
lista_completa = []
for cd in lista_busca:
    cd.pl = cd.valor_fechamento / cd.lpa

for cd in lista_busca:
    lista_completa.append([cd.papel.codigo, cd.papel.descricao, cd.valor_fechamento, cd.lpa, cd.pl])


lista_ordenada = []
while True:
    menor = 999
    #Pegando o menor valor da lista completa
    for i in range(len(lista_completa)):
        menor = lista_completa[i][4] if lista_completa[i][4] < menor else menor

    #Adicionando o menor valor na lista ordenada e retirando da lista completa
    #Adicionando na Lista Ordenada
    for i in range(len(lista_completa)):
        if lista_completa[i][4] == menor:
            lista_ordenada.append(lista_completa[i])
            posicao = i
    #Removendo da Lista Completa
    if menor != 999:
        lista_completa.pop(posicao) 
    else:
        break

#Exibindo Relatorio
print("\033[31;40m{:^10} - {:^55} - {:^15} - {:^10} - {:^10}\033[m".format("CODIGO", "DESCRICAO", "FECHAMENTO", "LPA", "PL"))
for dado in lista_ordenada:
    print("\033[31;40m{:^10} - {:^55} - {:^15} - {:^10} - {:^10.3f}\033[m".format(dado[0],dado[1],dado[2],dado[3],dado[4]))
