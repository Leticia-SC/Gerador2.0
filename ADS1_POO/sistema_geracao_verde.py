from sistema_de_geracao import SistemaDeGeracao
from gerador_qualificado import GeradorQualificado
from tipos_energia import TiposDeEnergia

class SistemaDeGeracaoVerde(SistemaDeGeracao):
    def __init__(self):
        self.listaGeradoresVerdes = []
        self.lista_geradores_poluentes = [] 

    def adicionar_gerador_poluente(self, gerador):
        self.lista_geradores_poluentes.append(gerador)

    def adicionar_gerador_nao_poluente(self, gerador):
        self.listaGeradoresVerdes.append(gerador)
        
    def validar_energias_limpas(self, listaGeradores):
        for gerador in listaGeradores:
            if gerador.tipo_geracao in (TiposDeEnergia.ENERGIA_TERMOELETRICA, TiposDeEnergia.ENERGIA_NUCLEAR):
                self.adicionar_gerador_poluente(gerador)
            else:
                self.adicionar_gerador_nao_poluente(gerador)

        self.utilizar_energias_limpas()

    def utilizar_energias_limpas(self):
        sistemaDeGeracao = SistemaDeGeracao()
        if len(self.listaGeradoresVerdes) == 0:
            for gerador in self.listaGeradoresPoluentes:
                sistemaDeGeracao.geradores.remove(gerador)
