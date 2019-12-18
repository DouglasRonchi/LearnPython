class fortwo:
    def __init__(self, terminal, aviao):
        self.terminal = terminal
        self.aviao = aviao


    def ida(self, pessoa1, pessoa2):
        origem = 'terminal'
        destino = 'aviao'
        self.terminal.remove(pessoa1)
        self.terminal.remove(pessoa2)
        self.aviao.append(pessoa1)
        self.aviao.append(pessoa2)
        print("{:-^70}".format('\033[32mIDA\033[m'))
        print(f"No aviao se encontram as seguintes pessoas: ")
        for i in self.aviao:
            print(f" --> {i}")
        print(f"Estao embarcando o {pessoa1}{f' e {pessoa2}' if pessoa2 else ''}")
        print(f"O motorista {pessoa1} levou {pessoa2} e foi de {origem} para o {destino}")


    def volta(self, pessoa1, pessoa2=None):
        origem = 'aviao'
        destino = 'terminal'
        self.aviao.remove(pessoa1)
        if pessoa2:
            self.aviao.remove(pessoa2)
            self.terminal.append(pessoa2)
        self.terminal.append(pessoa1)
        print("{:-^70}".format('\033[33mVOLTA\033[m'))
        print(f"No terminal se encontram as seguintes pessoas: ")
        for i in self.terminal:
            print(f' <-- {i}')
        print(f"O motorista {pessoa1}{f'levou {pessoa2}' if pessoa2 else ''} e foi de {origem} para o {destino}")
