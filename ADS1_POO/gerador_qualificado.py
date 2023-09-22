from gerador import Gerador
import csv

class GeradorQualificado(Gerador):

    def __init__(self, gerador, tipo_geracao, custo_mw):
        self.gerador = gerador
        self.tipo_geracao = tipo_geracao
        self.custo_mw = custo_mw 
        self.capacidade_atual = gerador.capacidade_atual       
        self.capacidade_maxima = gerador.capacidade_maxima

    def Exportar_dados(self, geradorQualificado) :
        dados_exportados = [
            ["nome", "capacidade_maxima", "tipo_geracao", "custo_mw"],
            [geradorQualificado.gerador.nome, geradorQualificado.gerador.capacidade_maxima,
              geradorQualificado.tipo_geracao, geradorQualificado.custo_mw]
        ]

        arquivo = "arquivo_gerador_qualificado1.csv"

        with open(arquivo, mode='w', newline='') as arquivo_csv:
            csv_writer = csv.writer(arquivo_csv)

            for linha in dados_exportados:
                csv_writer.writerow(linha)

        print("O arquivo CSV '{arquivo}' foi gerado com sucesso.")