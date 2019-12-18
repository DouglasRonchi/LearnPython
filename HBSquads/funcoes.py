
def verde(frase):
    frase = '\033[32m'+frase+'\033[m'
    return frase

def amarelo(frase):
    frase = '\033[33m'+frase+'\033[m'
    return frase


def validar_pessoa(respostas, pessoas, contratadas):
    adicionar = 0
    for l in pessoas:
        if l == respostas:
            adicionar = 1

    for l in contratadas:
        if l == respostas:
            adicionar = 0
            return print(amarelo(f"{respostas[0]} ja esta em um squad!"))

    if adicionar == 1:
        contratadas.append(respostas.copy())
        return print(verde(f"{respostas[0]} se encaixa no squad com - {respostas[1]} | {respostas[2]} | {respostas[3]}"))
    else:
        return print(amarelo(f"{respostas[0]} nao se encaixa no squad com - {respostas[1]} | {respostas[2]} | {respostas[3]}"))

