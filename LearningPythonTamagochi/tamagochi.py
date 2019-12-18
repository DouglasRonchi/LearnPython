from random import randint
from datetime import datetime
from time import sleep
import os.path
import emoji
from status import *

cargos = {'Policial':25,'Ladrao':20,'Desenvolvedor':15,'Politico':100, 'Vagabundo':5}
tamagochi = {}
estado = {}
carteira = {}
banco = {}
escolher_profissoes = []

# def mostrar_status():

#     tamagochi['estado']['geral'] = (((100 - tamagochi['estado']['fome'])+(100 - tamagochi['estado']['sede'])+(100 - tamagochi['estado']['cansado'])+(tamagochi['estado']['feliz'])+(100 - tamagochi['estado']['banheiro']))//5)

#     print(emoji.emojize(f"\033[1;31mVida {coracoes}  => {tamagochi['vida']}%\033[m | ",use_aliases=True),end='')
#     for k, v in tamagochi['estado'].items():
#         if k == 'geral':
#             print(f'\033[1;33m{k}\033[m:\033[1;34m{v} %\033[m',end=' | ')
#         else:
#             print(f'\033[1;33m{k}\033[m:\033[1;34m{v}\033[m',end=' | ')
#     print(emoji.emojize(f"\033[1;32m:heavy_dollar_sign: : {tamagochi['carteira']['dinheiro']}\033[m",use_aliases=True))


def jogos():
    while True:
        try:
            jogo = (int(input("""
            ----------JOGOS----------
            1 - Jogo JOKENPO
            2 - Jogo da Adivinação
            0 - SAIR

            Qual jogo voce quer jogar: """)))
        except Exception as e:
            print('Deve ser uma opcao valida')
        else:
            if jogo == 0:
                break
            elif jogo == 1:
                #Jogo JOKENPO
                jogador = int(input('1 - Pedra | 2 - Papel | 3 Tesoura: '))
                jogadaMaquina = randint(1, 3)
                maquina = ''
                escolha = ''
                pedra = ':fist:'
                papel = ':hand:'
                tesoura = ':v:'
                if jogadaMaquina == 1:
                    maquina = pedra
                elif jogadaMaquina == 2:
                    maquina = papel
                elif jogadaMaquina == 3:
                    maquina = tesoura

                if jogador == 1:
                    escolha = pedra
                elif jogador == 2:
                    escolha = papel
                elif jogador == 3:
                    escolha = tesoura
                print('Ready?')
                sleep(1)
                print('JO')
                sleep(0.75)
                print('KEN')
                sleep(0.5)
                print('PO')
                
                print(emoji.emojize(f'Maquina<- \033[1;36m{maquina}\033[m x \033[1;36m{escolha}\033[m ->Jogador',use_aliases=True))

                if jogadaMaquina == jogador:
                    print('Empate!')
                    tamagochi['estado']['feliz'] -= 1
                    tamagochi['estado']['cansado'] += 1
                else: #1 - pedra | 2 - papel | 3 - tesoura
                    if jogadaMaquina == 1 and jogador == 2:
                        print('Jogador, Você Venceu!')
                        tamagochi['estado']['feliz'] -= 5
                        tamagochi['estado']['cansado'] += 5
                    elif jogadaMaquina == 2 and jogador == 3:
                        print('Jogador, Você Venceu!')
                        tamagochi['estado']['feliz'] -= 5
                        tamagochi['estado']['cansado'] += 5
                    elif jogadaMaquina == 3 and jogador == 1:
                        print('Jogador, Você Venceu!')
                        tamagochi['estado']['feliz'] -= 5
                        tamagochi['estado']['cansado'] += 5
                    elif jogador == 1 and jogadaMaquina == 2:
                        print('Máquina Venceu!')
                        tamagochi['estado']['feliz'] += 5
                        tamagochi['estado']['cansado'] += 2
                    elif jogador == 2 and jogadaMaquina == 3:
                        print('Máquina Venceu!')
                        tamagochi['estado']['feliz'] += 5
                        tamagochi['estado']['cansado'] += 2
                    elif jogador == 3 and jogadaMaquina == 1:
                        print('Máquina Venceu!')
                        tamagochi['estado']['feliz'] += 5
                        tamagochi['estado']['cansado'] += 2   
                    tamagochi['estado']['fome'] += 1
                    tamagochi['estado']['sede'] += 1   
            elif jogo == 2:
                #Jogo da Adivinhacao
                num = randint(0,5)
                print('-=-' * 20)
                print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
                print('-=-' * 20)
                n = int(input('Em que número eu pensei? '))
                print('PROCESSANDO...')
                sleep(1)
                if num == n:
                    print('Você Ganhou!')
                    tamagochi['estado']['feliz'] -= 2
                    tamagochi['estado']['cansado'] += 5
                    tamagochi['estado']['fome'] += 1
                    tamagochi['estado']['sede'] += 1
                else:
                    print('A MÁQUINA SEMPRE VENCE!!! pensei no número {}'.format(num))
                    tamagochi['estado']['feliz'] += 5
                    tamagochi['estado']['cansado'] += 2
                    tamagochi['estado']['fome'] += 1
                    tamagochi['estado']['sede'] += 1

            try:
                opcao = int(input('Jogar novamente? [1 - Sim / 0 - Nao]: '))
            except Exception as e:
                print('Digite uma opcao Valida')
            else:
                if opcao == 0:
                    break
                else:
                    jogos()


def verificaSaldo(compra):
    if tamagochi['carteira']['dinheiro'] - compra < 0:
        return False
    else:
        return True


def menu():
    try:
        opcao = int(input("""
        O que deseja fazer?
        1 - Comer
        2 - Beber
        3 - Dormir
        4 - Brincar
        5 - Banheiro
        6 - Status
        7 - Trabalhar
        8 - Loja
        9 - Banco

        999 - Sair
        O que fazer: """))
        if opcao == 999:
            return False
    except Exception as e:
        print('Opcao Invalida!')
    else:    
        if opcao == 1:
            #Comer
            if tamagochi['estado']['fome'] == 0:
                print('Comeu demais, esta cheio!!')
                tamagochi['estado']['feliz'] -= 5
                if tamagochi['estado']['feliz'] < 20:
                    print('Estou muito triste... :(')
                    tamagochi['estado']['cansado'] += 15
                    if tamagochi['estado']['cansado'] > 90:
                        tamagochi['vida'] -= 2
            else:
                tamagochi['estado']['fome'] -= 10
                tamagochi['estado']['cansado'] += 2
                tamagochi['estado']['feliz'] += 1
                tamagochi['estado']['banheiro'] += 3
        elif opcao == 2:
            #Beber
            if tamagochi['estado']['sede'] == 0:
                print('Bebeu demais, esta cheio!!')
                tamagochi['estado']['feliz'] -= 5
                if tamagochi['estado']['feliz'] < 20:
                    print('Estou muito triste... :(')
                    tamagochi['estado']['cansado'] += 15
                    if tamagochi['estado']['cansado'] > 90:
                        tamagochi['vida'] -= 2
            else:
                tamagochi['estado']['sede'] -= 10
                tamagochi['estado']['cansado'] += 2
                tamagochi['estado']['feliz'] += 1
                tamagochi['estado']['banheiro'] += 3   
        elif opcao == 3:
            #Dormir
            if tamagochi['estado']['cansado'] == 0:
                print('Estou descansado... Nao quero dormir!')
            else:
                tempo = int(input("""
                --------------HORA DO SONO--------------
                (Sono em segundos, cada segundo
                vale por 5 pontos de descanso...)
                === CUIDADO PARA NAO DORMIR MUITO ===
                Dormir por quanto tempo: """))
                for i in range(tempo):
                    print('zZzzZ...')
                    tamagochi['estado']['cansado'] -= 5
                    tamagochi['estado']['sede'] += 2
                    tamagochi['estado']['fome'] += 2
                    tamagochi['estado']['feliz'] += 3
                    if tamagochi['estado']['sede'] > 99 or tamagochi['estado']['fome'] > 99:
                        print(f"Muita FOME E SEDE! Perdendo Vida! Ouch... Vida: {tamagochi['vida']}")
                        tamagochi['vida'] -= 2
                    sleep(1)
        elif opcao == 4:
            #Brincar
            if tamagochi['estado']['cansado'] == 100:
                print('Nao pode brincar, esta muito cansado...')
                tamagochi['estado']['feliz'] -= 5
                if tamagochi['estado']['feliz'] < 20:
                    print('Estou muito triste... :(')
                    tamagochi['vida'] -= 2
            else:
                jogos()
        elif opcao == 5:
            #Banheiro
            if tamagochi['estado']['banheiro'] == 0:
                print('Nao estou mais com vontade de ir ao banheiro!')
                tamagochi['estado']['feliz'] -= 10
            else:
                tamagochi['estado']['banheiro'] -= 75
        elif opcao == 6:
            #Status
            for k, v in tamagochi.items():
                if k == 'estado':
                    for k, v in tamagochi['estado'].items():
                        print(f"{k:.<30}{v}")
            now = datetime.now()
            dia = now.day
            if dia < 10:
                dia = f'0{dia}'
            hora = now.hour
            if hora < 10:
                hora = f'0{hora}'
            minuto = now.minute
            if minuto < 10:
                minuto = f'0{minuto}'
            
            idade = int(f'{dia}{hora}{minuto}') - int(tamagochi['nascimento'])
            print(f'Idade : {idade} anos.')
        elif opcao == 7:
            #TRABALHAR
            novo_emprego = int(input('Deseja 1 - Trabalhar ou 2 - Escolher um novo Cargo? '))
            if tamagochi['carteira']['cargo'] == '':
                print('Você não tem um emprego...')
                print('Vamos definir um emprego baseado em suas respostas...')
                novo_emprego = 2
            if novo_emprego == 2:                
                    try:
                        perguntas = ["Voce gosta de Matematica?", "Ja insutou alguem?", "Sabe dirigir?", "Voce mente com frequencia?"]
                        classificacao = []
                        for i in range(4):
                            n = str(input(perguntas[i]))
                            if n[0].upper() == 'S':
                                classificacao.append(n)
                            if n[0].upper() == 'N' and len(classificacao) > 1:
                                classificacao.pop()
                    except Exception as e:
                        print('Opcao invalida.')
                        print(e)
                    else:
                    #Definindo Profissao com base nas respostas
                        if len(classificacao) == 1:
                            tamagochi['carteira']['cargo'] = 'Desenvolvedor'
                        elif len(classificacao) == 2:
                            tamagochi['carteira']['cargo'] = 'Ladrao'
                        elif len(classificacao) == 3:
                            tamagochi['carteira']['cargo'] = 'Policial'
                        elif len(classificacao) == 4:
                            tamagochi['carteira']['cargo'] = 'Politico'
                        else:
                            tamagochi['carteira']['cargo'] = 'Vagabundo'
                        cargo_salario = tamagochi['carteira']['cargo']
                        print(f"Parabens, seu novo cargo e de \033[1;34m{tamagochi['carteira']['cargo']}\033[m Com salario de \033[1;32m$${cargos[cargo_salario]}\033[m por hora.")
                        for i in range(3):
                            sleep(0.50)
                            print('.',end='')
                        print('')
                        sleep(1)
            if novo_emprego == 1:
                try:
                    horas_trabalho = int(input('---------TRABALHO DIARIO---------\n'
                    '(SE TRABALHAR ENQUANTO ESTA 100% CANSADO VOCE FICARA LOUCO\n'
                    'E COMECARA A PERDER VIDA POR CADA HORA DE TRABALHO)\n'
                    'Quantas horas Deseja Trabalhar? '))
                    if tamagochi['estado']['cansado'] > 90:
                        raise Exception('Estou muito cansado para trabalhar...')
                except Exception as e:
                    print(f'Opcao invalida. {e}')
                    sleep(3)
                else:
                    for k, v in tamagochi['carteira'].items():
                        if v in cargos:
                            ganhos = cargos[v] * horas_trabalho
                    tamagochi['carteira']['dinheiro'] += ganhos
                    for i in range(horas_trabalho):
                        sleep(0.5)
                        tamagochi['estado']['cansado'] += 2
                        if i % 2 == 0: 
                            if tamagochi['estado']['cansado'] > 99:
                                tamagochi['vida'] -= 20
                                salvarArquivo()
                                mostrar_status()
                                print(f"Perndendo vida! Ouch {tamagochi['vida']}")
                            print('Trabalhando.')
                        else:
                            if tamagochi['estado']['cansado'] > 99:
                                tamagochi['vida'] -= 20
                                salvarArquivo()
                                mostrar_status()
                                print(f"Perndendo vida! Ouch {tamagochi['vida']}")
                            print('Trabalhando..')
                            mostrar_status()
                        if tamagochi['vida'] < 1:
                            print('Voce morreu de tanto trabalhar...')
                            break
        elif opcao == 8:
            print("{:-^40}".format(' BEM VINDO A LOJA '))
            print("""
            1 - Life Potion    - Melhora o status de Vida ao maximo        - $$ 2500.00
            2 - Energy Potion  - Melhora o status de Energia ao maximo     - $$ 1000.00
            3 - Food Potion    - Melhora o status de Fome ao maximo        - $$ 1000.00
            4 - Drink Potion   - Melhora o status de Sede ao maximo        - $$ 1000.00
            5 - Happy Potion   - Melhora o status de Felicidade ao maximo  - $$ 2000.00
            6 - Super Potion   - Melhora o status de TUDO ao maximo        - $$ 5000.00
            """)
            try:
                produto = int(input('Qual produto deseja? '))
            except Exception as e:
                print('Opcao Invalida')
            else:
                if produto == 1:
                    #Life
                    if verificaSaldo(2500):
                        tamagochi['vida'] = 100
                        tamagochi['carteira']['dinheiro'] -= 2500
                    else:
                        print('Dinheiro insufuciente...')
                elif produto == 2:
                    #Energy
                    if verificaSaldo(1000):
                        tamagochi['estado']['cansado'] = 0
                        tamagochi['carteira']['dinheiro'] -= 1000
                    else:
                        print('Dinheiro insufuciente...')
                elif produto == 3:
                    #Food
                    if verificaSaldo(1000):
                        tamagochi['estado']['fome'] = 0
                        tamagochi['carteira']['dinheiro'] -= 1000
                    else:
                        print('Dinheiro insufuciente...')
                elif produto == 4:
                    #Drink
                    if verificaSaldo(1000):
                        tamagochi['estado']['sede'] = 0
                        tamagochi['carteira']['dinheiro'] -= 1000
                    else:
                        print('Dinheiro insufuciente...')
                elif produto == 5:
                    #Happy
                    if verificaSaldo(2000):
                        tamagochi['estado']['feliz'] = 100
                        tamagochi['carteira']['dinheiro'] -= 2000
                    else:
                        print('Dinheiro insufuciente...')
                elif produto == 6:
                    #ALL
                    if verificaSaldo(5000):
                        tamagochi['estado']['fome'] = 0
                        tamagochi['estado']['sede'] = 0
                        tamagochi['estado']['cansado'] = 0
                        tamagochi['estado']['feliz'] = 100
                        tamagochi['estado']['banheiro'] = 0
                        tamagochi['vida'] = 100
                        tamagochi['carteira']['dinheiro'] -= 5000
                    else:
                        print('Dinheiro insufuciente...')
        elif opcao == 9:
            #BANCO
            while True:
                try:
                    print('{:-^30}'.format(' \033[1;35mBANCO CENTRAL\033[m '))
                    operacao = int(input(
                    "1 - Verificar Saldo\n"
                    "2 - Sacar\n"
                    "3 - Depositar\n"
                    "0 - \033[31mSair\033[m\n"
                    "Operacao: "))
                except Exception as e:
                    print('Opcao invalida.')
                else:
                    if operacao == 0:
                        #SAIR
                        break
                    elif operacao == 1:
                        #SALDO
                        print(f"SALDO: {banco['conta']}")
                    elif operacao == 2:
                        #SACAR
                        try:
                            valor = int(input('Quanto voce quer sacar? '))
                            if valor > banco['conta']:
                                raise Exception(f"Valor Insuficiente no Banco! Voce tem somente $${banco['conta']}")
                        except Exception as e:
                            print(f'Erro ao sacar: {e}')
                        else:
                            banco['conta'] -= valor
                            tamagochi['carteira']['dinheiro'] += valor
                            print(f'\033[1;33m$${valor} Sacado com sucesso!\033[m')
                            sleep(1)
                    elif operacao == 3:
                        #DEPOSITAR
                        try:
                            valor = int(input('Quanto voce quer depositar? '))
                            if valor > tamagochi['carteira']['dinheiro']:
                                raise Exception(f"Valor Insuficiente na Carteira! Voce tem somente $${tamagochi['carteira']['dinheiro']}")
                        except Exception as e:
                            print(f'Erro ao depositar: {e}')
                        else:
                            banco['conta'] += valor
                            tamagochi['carteira']['dinheiro'] -= valor
                            print(f'\033[1;33m$${valor} Depositado com sucesso!\033[m')
                            sleep(1)

    ### =============================== FIM MENU ======================================


#salvar no arquivo
def salvarArquivo():
    dados = ''
    f = open('tamagochi_save.txt', 'w', encoding='utf8')
    dados += f"nome:{tamagochi['nome']},\n"
    dados += f"nascimento:{tamagochi['nascimento']},\n"
    dados += f"vida:{tamagochi['vida']},\n"
    for k, v in tamagochi['estado'].items():
        dados += f'{k}:{v},\n'
    for k, v in tamagochi['carteira'].items():
        dados += f'{k}:{v},\n'
    dados += F"conta:{banco['conta']},\n"
    f.write(dados)
    f.close()
    dados = ''


#  INICIA O JOGO VERIFICANDO SE EXISTE UM SAVE
#LANCANDO ATRIBUTOS PARA A PRIMEIRA EXECUCAO:
estado['fome'] = randint(10,50)
estado['sede'] = randint(10,50)
estado['cansado'] = randint(0,20)
estado['feliz'] = randint(20,80)
estado['banheiro'] = randint(10,20)
estado['geral'] = 0

carteira['cargo'] = ''
carteira['dinheiro'] = 0
#Comecando
tamagochi['vida'] = 100
tamagochi['nome'] = ''
now = datetime.now()
dia = now.day
if dia < 10:
    dia = f'0{dia}'
hora = now.hour
if hora < 10:
    hora = f'0{hora}'
minuto = now.minute
if minuto < 10:
    minuto = f'0{minuto}'
tamagochi['nascimento'] = int(f'{dia}{hora}{minuto}')
tamagochi['estado'] = estado.copy()
tamagochi['carteira'] = carteira.copy()

banco['conta'] = 0

if os.path.isfile('tamagochi_save.txt'):
    #PEGANDO ATRIBUTOS DO ARQUIVO DE TEXTO
    f = open('tamagochi_save.txt', 'r', encoding='utf8')
    lista = f.readlines()
    i = 1
    for linha in lista:
        dado = linha.split(':')
        if i == 1:
            tamagochi[dado[0]] = dado[1][0:-2]
        elif i <= 3 and i != 10 and i != 11:
            tamagochi[dado[0]] = int(dado[1][0:-2])
        elif i == 10:
            tamagochi['carteira']['cargo'] = dado[1][0:-2]
        elif i == 11:
            tamagochi['carteira']['dinheiro'] = int(dado[1][0:-2])
        elif i == 12:
            banco['conta'] = int(dado[1][0:-2])
        else:
            tamagochi['estado'][dado[0]] = int(dado[1][0:-2])
        i += 1

else:
    tamagochi['nome'] = str(input('Digite o nome do Tamagochi:'))
    

#MENU
while True:
    #ACIDENTES
    acidente = randint(1, 50)
    if acidente == 1:
        print('Perdeu, perdeu, é um assalto, passa tudo ai!!!')
        sleep(3)
        if tamagochi['carteira']['dinheiro'] == 0:
            print('Voce ta pior que eu... pegue esses 50 reais para viver melhor...')
            tamagochi['carteira']['dinheiro'] += 50
            sleep(3)
        else:
            perdeu = randint(1, tamagochi['carteira']['dinheiro'])
            tamagochi['carteira']['dinheiro'] -= perdeu
            print(f'Voce perdeu... {perdeu} dinheiros... :(')
            sleep(3)


    #VERIFICA SE MORREU
    if tamagochi['vida'] < 1:
        print(f"Seu {tamagochi['nome']} morreu... :(")
        os.remove('tamagochi_save.txt')
        print('████▀░░░░░░░░░░░░░░░░░▀████')
        print('███│░░░░░░░░░░░░░░░░░░░│███')
        print('██▌│░░░░░░░░░░░░░░░░░░░│▐██')
        print('██░└┐░░░░░░░░░░░░░░░░░┌┘░██')
        print('██░░└┐░░░░░░░░░░░░░░░┌┘░░██')
        print('██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██')
        print('██▌░│██████▌░░░▐██████│░▐██')
        print('███░│▐███▀▀░░▄░░▀▀███▌│░███')
        print('██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██')
        print('██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██')
        print('████▄─┘██▌░░░░░░░▐██└─▄████')
        print('█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████')
        print('████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████')
        print('█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████')
        print('███████▄░░░░░░░░░░░▄███████')
        break
    print('{:-^120}'.format(f"\033[1;34m{tamagochi['nome']} - Cargo: {tamagochi['carteira']['cargo']}\033[m"))
    #Setando maximo e minimo de status:
    for k, v in tamagochi['estado'].items():
        if k == 'geral':
            continue
        if v > 100:
            tamagochi['estado'][k] = 100
        if v < 0:
            tamagochi['estado'][k] = 0
    if tamagochi['vida'] < 25:
        coracoes = ':heart:'
    elif tamagochi['vida'] >= 25 and tamagochi['vida'] < 50:
        coracoes = ':heart: :heart:'
    elif tamagochi['vida'] >= 50 and tamagochi['vida'] < 75:
        coracoes = ':heart: :heart: :heart:'
    elif tamagochi['vida'] > 75:
        coracoes = ':heart: :heart: :heart: :heart:'

    mostrar_status(tamagochi, coracoes)

    salvarArquivo()
    
    if menu() == False:
        break