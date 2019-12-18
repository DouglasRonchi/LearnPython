import emoji


def mostrar_status(tamagochi, coracoes):

    tamagochi['estado']['geral'] = (((100 - tamagochi['estado']['fome'])+(100 - tamagochi['estado']['sede'])+(100 - tamagochi['estado']['cansado'])+(tamagochi['estado']['feliz'])+(100 - tamagochi['estado']['banheiro']))//5)

    print(emoji.emojize(f"\033[1;31mVida {coracoes}  => {tamagochi['vida']}%\033[m | ",use_aliases=True),end='')
    for k, v in tamagochi['estado'].items():
        if k == 'geral':
            print(f'\033[1;33m{k}\033[m:\033[1;34m{v} %\033[m',end=' | ')
        else:
            print(f'\033[1;33m{k}\033[m:\033[1;34m{v}\033[m',end=' | ')
    print(emoji.emojize(f"\033[1;32m:heavy_dollar_sign: : {tamagochi['carteira']['dinheiro']}\033[m",use_aliases=True))
