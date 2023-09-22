class Gerador:
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome
        self.capacidade_maxima = capacidade_maxima
        self.capacidade_atual = 0
        self.ligado = False

    def gerar(self, energia):
        if self.ligado:
            if self.capacidade_atual + energia <= self.capacidade_maxima:
                self.capacidade_atual += energia
            else:
                raise Exception("Capacidade máxima excedida. Não é possível gerar mais energia.")
        else:
            print(f"{self.nome}: Gerador desligado. Ligue o gerador antes de gerar energia.")

    def desligar(self):
        self.ligado = False
        self.capacidade_atual = 0
