import pytest
from src.entrega import calcular_taxa_entrega

def test_deve_cobrar_taxa_fixa_para_distancia_ate_3km():
    resultado = calcular_taxa_entrega(2.0)
    assert resultado == 5.00

def test_deve_cobrar_taxa_fixa_para_distancia_exatamente_3km():
    resultado = calcular_taxa_entrega(3.0)
    assert resultado == 5.00

def test_deve_cobrar_taxa_proporcional_para_distancia_acima_de_3km():
    resultado = calcular_taxa_entrega(5.0)
    assert resultado == 9.00

def test_deve_lancar_erro_para_distancia_negativa():
    with pytest.raises(ValueError, match="negativa"):
        calcular_taxa_entrega(-1.0)

def test_deve_lancar_erro_para_distancia_zero():
    with pytest.raises(ValueError, match="maior que zero"):
        calcular_taxa_entrega(0)