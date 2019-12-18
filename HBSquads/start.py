from funcoes import amarelo, verde, validar_pessoa


pessoas = [
['Tiago', 'VUE', 'Java', 'Postgre'],
['Matheus', 'Angular', 'Python', 'MongoDB'],
['Nicole', 'React', 'PHP', 'MySQLServer']
]


contratadas = []


while len(contratadas) < 3:
    while True:
        try:
            opcao = int(input("""
            1 - Tiago
            2 - Matheus
            3 - Nicole
            Escoha a pessoa: """))
        except Exception as e:
            print('Opcao Invalida.')
        else:
            if opcao == 1:
                esc_pessoa = 'Tiago'
            elif opcao == 2:
                esc_pessoa = 'Matheus'
            elif opcao == 3:
                esc_pessoa = 'Nicole'
            else:
                pass
            break


    while True:
        try:
            opcao = int(input("""
            1 - VUE
            2 - Angular
            3 - React
            Escoha o front-end: """))
        except Exception as e:
            print('Opcao Invalida.')    
        else:
            if opcao == 1:
                esc_front = 'VUE'
            elif opcao == 2:
                esc_front = 'Angular'
            elif opcao == 3:
                esc_front = 'React'
            else:
                pass
            break


    while True:
        try: 
            opcao = int(input("""
            1 - Java
            2 - Python
            3 - PHP
            Escoha o back-end: """))
        except Exception as e:
            print('Opcao Invalida.')    
        else:
            if opcao == 1:
                esc_back = 'Java'
            elif opcao == 2:
                esc_back = 'Python'
            elif opcao == 3:
                esc_back = 'PHP'
            else:
                pass
            break


    while True:
        try: 
            opcao = int(input("""
            1 - MySQLServer
            2 - Postgre
            3 - MongoDB
            Escoha o DB: """))
        except Exception as e:
            print('Opcao Invalida.')    
        else:
            if opcao == 1:
                esc_db = 'MySQLServer'
            elif opcao == 2:
                esc_db = 'Postgre'
            elif opcao == 3:
                esc_db = 'MongoDB'
            else:
                pass
            break

    respostas = [esc_pessoa, esc_front, esc_back, esc_db]

    validar_pessoa(respostas, pessoas, contratadas)


print(f"Todas as pessoas se encaixaram nos squads!")
for pessoa in contratadas:
    print(verde('='*20))
    print(f"Nome - {pessoa[0]}")
    print(f"Front - {pessoa[1]}")
    print(f"Back - {pessoa[2]}")
    print(f"DB - {pessoa[3]}")  
