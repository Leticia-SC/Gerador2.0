import pytest
from sistema_de_geracao import SistemaDeGeracao
from gerador import Gerador
from carga import Carga

def test_sistema_balancear_sobrecarga():
    sistema = SistemaDeGeracao()

    gerador1 = Gerador("Gerador 1", 50)  # Capacidade insuficiente
    gerador2 = Gerador("Gerador 2", 100)
    carga1 = Carga("Carga 1", 120)
    carga2 = Carga("Carga 2", 30)

    sistema.adicionar_gerador(gerador1)
    sistema.adicionar_gerador(gerador2)
    sistema.adicionar_carga(carga1)
    sistema.adicionar_carga(carga2)

    sistema.balancear()


def test_sistema_balancear_sucesso():
    sistema = SistemaDeGeracao()

    gerador1 = Gerador("Gerador 1", 100)
    gerador1.ligado = True
    gerador1.gerar(70)
    gerador2 = Gerador("Gerador 2", 50)
    gerador2.ligado = True 
    gerador2.gerar(40)
    carga1 = Carga("Carga 1", 40)
    carga2 = Carga("Carga 2", 30)

    sistema.adicionar_gerador(gerador1)
    sistema.adicionar_gerador(gerador2)
    sistema.adicionar_carga(carga1)
    sistema.adicionar_carga(carga2)

def test_sistema_balancear_geradores_desligados():
    sistema = SistemaDeGeracao()

    gerador1 = Gerador("Gerador 1", 60)
    gerador2 = Gerador("Gerador 2", 50)
    gerador2.ligado = False 
    carga1 = Carga("Carga 1", 40)
    carga2 = Carga("Carga 2", 30)

    sistema.adicionar_gerador(gerador1)
    sistema.adicionar_gerador(gerador2)
    sistema.adicionar_carga(carga1)
    sistema.adicionar_carga(carga2)

    sistema.balancear()

def test_relatorio_custo_medio_MW():
    sistema = SistemaDeGeracao()
    gerador1 = Gerador("Gerador 1", 60)
    gerador2 = Gerador("Gerador 2", 50)
    gerador2.ligado = False 
    carga1 = Carga("Carga 1", 40)
    carga2 = Carga("Carga 2", 30)

    sistema.adicionar_gerador(gerador1)
    sistema.adicionar_gerador(gerador2)
    sistema.adicionar_carga(carga1)
    sistema.adicionar_carga(carga2)

    relatorio = sistema.relatorio_custo_medio_MW()
    print(relatorio)