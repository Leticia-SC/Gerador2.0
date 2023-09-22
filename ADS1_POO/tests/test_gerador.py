import pytest
from gerador import Gerador

def test_gerador_gerar_e_desligar():
    gerador_testar = Gerador("Gerador Teste", 100)
    
    # Verifica se o gerador está inicialmente desligado
    assert not gerador_testar.ligado

    # Liga o gerador
    gerador_testar.ligado = True
    assert gerador_testar.ligado

    # Gera energia
    gerador_testar.gerar(50)
    assert gerador_testar.capacidade_atual == 50

    # Desliga o gerador
    gerador_testar.desligar()
    assert not gerador_testar.ligado
    assert gerador_testar.capacidade_atual == 0

def test_gerador_sobrecarga():
    gerador_testar = Gerador("Gerador Teste", 100)
    gerador_testar.ligado = True

    # Tenta gerar mais energia do que a capacidade máxima
    with pytest.raises(Exception) as excinfo:
        gerador_testar.gerar(150)

    # Verifica se a exceção foi levantada
    assert "Capacidade máxima excedida" in str(excinfo.value)
