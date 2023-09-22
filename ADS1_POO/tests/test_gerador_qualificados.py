import pytest
from sistema_de_geracao import SistemaDeGeracao
from gerador_qualificado import GeradorQualificado
from gerador import Gerador
from tipos_energia import TiposDeEnergia

def test_cria_gerador_qualificado():
    geradorQualificado = GeradorQualificado(Gerador("Gerador 1", 100), TiposDeEnergia.ENERGIA_HIDRELETRICA, 200.09)
    print(
        "Nome: " + geradorQualificado.gerador.nome
          + "Capacidade máxima: " + str(geradorQualificado.gerador.capacidade_maxima)
          + "Tipo de geração: " + geradorQualificado.tipo_geracao 
          + "Custo MW: " + str(geradorQualificado.custo_mw))

def test_exportar_dados_gerador_qualificado():
    geradorQualificado = GeradorQualificado(Gerador("Gerador 1", 100), TiposDeEnergia.ENERGIA_HIDRELETRICA, 200.09)
    geradorQualificado.Exportar_dados(geradorQualificado)


