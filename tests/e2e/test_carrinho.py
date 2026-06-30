import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pages.carrinho_page import CarrinhoPage


@pytest.fixture
def carrinho(page):
    cp = CarrinhoPage(page)
    cp.autenticar()  # já navega para home autenticado
    return cp


def test_lista_restaurantes_carregada(carrinho, page):
    """Verifica que a grade de restaurantes é exibida na home."""
    assert page.locator(".restaurant-grid").is_visible()
    assert page.locator(".rest-card").count() > 0


def test_clicar_restaurante_abre_detalhes(carrinho, page):
    """Verifica que clicar em um restaurante navega para a página de detalhes."""
    carrinho.clicar_primeiro_restaurante()

    page.wait_for_timeout(500)
    assert "restaurant.html" in page.url


def test_cardapio_exibido_na_pagina_restaurante(carrinho, page):
    """Verifica que os itens do cardápio são carregados na página do restaurante."""
    carrinho.clicar_primeiro_restaurante()
    carrinho.aguardar_cardapio()

    assert page.locator(".menu-item").count() > 0
    assert page.locator(".add-cart-btn").first.is_visible()


def test_adicionar_item_ao_carrinho(carrinho, page):
    """Verifica que adicionar um item atualiza o badge do carrinho."""
    carrinho.clicar_primeiro_restaurante()
    carrinho.aguardar_cardapio()

    badge_antes = carrinho.badge_contagem_carrinho().text_content()
    carrinho.adicionar_primeiro_item()
    page.wait_for_timeout(300)

    badge_depois = carrinho.badge_contagem_carrinho().text_content()
    assert badge_antes != badge_depois
    assert "1" in badge_depois


def test_total_carrinho_atualiza_apos_adicao(carrinho, page):
    """Verifica que o total do carrinho é alterado ao adicionar um item."""
    carrinho.clicar_primeiro_restaurante()
    carrinho.aguardar_cardapio()

    total_antes = carrinho.total_carrinho().text_content()
    carrinho.adicionar_primeiro_item()
    page.wait_for_timeout(300)

    total_depois = carrinho.total_carrinho().text_content()
    assert total_antes != total_depois
    assert "R$" in total_depois
