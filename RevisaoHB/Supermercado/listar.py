from dao.rev_frutas_dao import FrutasDao
from dao.rev_verduras_dao import VerdurasDao
from dao.rev_legumes_dao import LegumesDao

from model.rev_frutas import Fruta
from model.rev_verduras import Verdura
from model.rev_legumes import Legume

dao_fruta = FrutasDao()
dao_verdura = VerdurasDao()
dao_legume = LegumesDao()

def listar_frutas():
    print("{:^32}".format("\033[33mFRUTAS\033[m"))
    for l in dao_fruta.listar():
        print("{:.<20}{:.2f}".format(l['nome'], float(l['preco'])))

def listar_verduras():
    print("{:^32}".format("\033[33mVERDURAS\033[m"))
    for l in dao_verdura.listar():
        print("{:.<20}{:.2f}".format(l['nome'], float(l['preco'])))

def listar_legumes():
    print("{:^32}".format("\033[33mLEGUMES\033[m"))
    for l in dao_legume.listar():
        print("{:.<20}{:.2f}".format(l['nome'], float(l['preco'])))


while True:
    try:
        opcao = int(input("""
            1 - Frutas
            2 - Verduras
            3 - Legumes
            4 - Todas
            0 - Sair
            Escolha: """))
        if opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
            raise Exception('Opcao Invalida')
    except Exception as e:
        print('Dado invalido, tente novamente...')
        print(f"ERRO: {e}")
    else:
        if opcao == 1:
            listar_frutas()
        elif opcao == 2:
            listar_verduras()
        elif opcao == 3:
            listar_legumes()
        elif opcao == 4:
            listar_frutas()
            listar_verduras()
            listar_legumes()            
        elif opcao == 0:
            break
