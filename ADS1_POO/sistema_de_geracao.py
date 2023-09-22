class SistemaDeGeracao:
    def __init__(self):
        self.geradores = []
        self.cargas = []

    def adicionar_gerador(self, gerador = None, gerador_qualificado = None):
        if gerador is not None:
            self.geradores.append(gerador)
        else:
            self.geradores.append(gerador_qualificado)
        self.balancear()

    def adicionar_carga(self, carga):
        self.cargas.append(carga)
        self.balancear()

    def desconectar_carga(self, carga):
        if carga in self.cargas:
            self.cargas.remove(carga)
            print(f"Carga '{carga}' desconectada para evitar a demanda excessiva.")

    def balancear(self):
        demanda_total = sum(carga.energia for carga in self.cargas)
        capacidade_total = sum(gerador.capacidade_atual for gerador in self.geradores if gerador.ligado)

        while capacidade_total < demanda_total:
                carga_com_maior_energia = max(self.cargas, key=lambda carga: carga.energia)
                self.desconectar_carga(carga_com_maior_energia)
                demanda_total -= carga_com_maior_energia.energia

        if capacidade_total < demanda_total:
            raise Exception("Sobrecarga! A capacidade dos geradores não é suficiente para atender à demanda.")
        else:
            print("Sistema balanceado. A demanda está sendo atendida.")

    def relatorio_custo_medio_MW(self): 
        tipo_geracao_total = {}
        tipo_geracao_count = {}

        for carga in self.cargas:
            if carga.tipo_geracao not in tipo_geracao_total:
                tipo_geracao_total[carga.tipo_geracao] = 0
                tipo_geracao_count[carga.tipo_geracao] = 0

            tipo_geracao_total[carga.tipo_geracao] += carga.energia
            tipo_geracao_count[carga.tipo_geracao] += 1

        tipo_geracao_custo_medio = {}

        for tipo, total in tipo_geracao_total.items():
            count = tipo_geracao_count[tipo]
            if count > 0:
                custo_medio = total / count
                tipo_geracao_custo_medio[tipo] = custo_medio

        relatorio = {
            "Total por MW: ": tipo_geracao_total,
            "Custo Médio por MW por Tipo de Geração: ": tipo_geracao_custo_medio
        }

        return relatorio