from pessoa import Pessoa


def criar_lista_obj():
    cab = ['nome', 'telefone', 'email', 'idade']

    pessoas = [
        ['Alex', 'Paulo', 'Pedro', 'Mateus', 'Carlos', 'Joao', 'Joaquim'],
        ['4799991', '4799992', '4799993', '4799994', '4799995', '4799996', '4799997'],
        ['a@a.com', 'b@b.com', 'c@c.com', 'd@d.com', 'e@e.com', 'f@f.com', 'g@g.com'],
        ['18', '25', '40', '16', '15', '19', '17']
    ]
    lista_pessoas_obj_maiores = []
    lista_pessoas_obj_menores = []
    for n in range(7):
        lista_pessoas = []
        for i in range(4):
            lista_pessoas.append(pessoas[i][n])
        if int(lista_pessoas[3]) >= 18:
            pessoa = Pessoa(lista_pessoas[0],lista_pessoas[1],lista_pessoas[2],lista_pessoas[3])
            lista_pessoas_obj_maiores.append(pessoa)
        else:
            pessoa = Pessoa(lista_pessoas[0],lista_pessoas[1],lista_pessoas[2],lista_pessoas[3])
            lista_pessoas_obj_menores.append(pessoa)
    
    return [lista_pessoas_obj_maiores, lista_pessoas_obj_menores]



listas = criar_lista_obj()

for lista in listas:
    print("="*40)
    for l in lista:

        print(f"Nome: {l.nome}")
        print(f"Telefone: {l.telefone}")
        print(f"Email: {l.email}")
        print(f"Idade: {l.idade}")