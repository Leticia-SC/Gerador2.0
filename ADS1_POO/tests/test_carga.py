import pytest
from carga import Carga

def test_carga_conectar_e_desconectar():
    carga_testar = Carga("Carga Teste", 50)

    # Verifica se a carga está inicialmente desconectada
    assert not carga_testar.conectada

    # Conecta a carga
    carga_testar.conectar()
    assert carga_testar.conectada

    # Desconecta a carga
    carga_testar.desconectar()
    assert not carga_testar.conectada
