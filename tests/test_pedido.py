import pytest
from src.pedido import calcular_total_pedido

def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 20.00}, {"preco": 15.00}]
    resultado = calcular_total_pedido(itens, 30.00)
    assert resultado == 35.00

def test_deve_calcular_total_exatamente_igual_ao_valor_minimo():
    itens = [{"preco": 10.00}, {"preco": 20.00}]
    resultado = calcular_total_pedido(itens, 30.00)
    assert resultado == 30.00

def test_deve_lancar_erro_quando_total_abaixo_do_valor_minimo():
    itens = [{"preco": 5.00}, {"preco": 8.00}]
    with pytest.raises(ValueError, match="Valor mínimo"):
        calcular_total_pedido(itens, 20.00)

def test_deve_lancar_erro_quando_pedido_esta_vazio():
    with pytest.raises(ValueError, match="vazio"):
        calcular_total_pedido([], 20.00)