import pytest
from sistema_geracao_verde import SistemaDeGeracaoVerde
from sistema_de_geracao import SistemaDeGeracao
from gerador_qualificado import GeradorQualificado
from gerador import Gerador
from tipos_energia import TiposDeEnergia

def test_verificar_uso_de_energias_limpas():
    sistemaDeGeracao = SistemaDeGeracao()
    sistemaDeGeracaoVerde = SistemaDeGeracaoVerde()

    gerador1 = GeradorQualificado(Gerador("Gerador 1", 100), TiposDeEnergia.ENERGIA_HIDRELETRICA, 100.87)
    assert not gerador1.gerador.ligado

    gerador1.ligado = True
    sistemaDeGeracao.adicionar_gerador(gerador1)

    gerador2 = GeradorQualificado(Gerador("Gerador 2", 150), TiposDeEnergia.ENERGIA_SOLAR, 60.12)
    assert not gerador2.gerador.ligado

    gerador2.ligado = True
    sistemaDeGeracao.adicionar_gerador(gerador2)

    gerador3 = GeradorQualificado(Gerador("Gerador 3", 100), TiposDeEnergia.ENERGIA_TERMOELETRICA, 60.12)
    assert not gerador3.gerador.ligado
    
    gerador3.ligado = True
    sistemaDeGeracao.adicionar_gerador(gerador3)

    sistemaDeGeracaoVerde.validar_energias_limpas(sistemaDeGeracao.geradores)
