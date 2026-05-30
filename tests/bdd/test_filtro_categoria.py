import os
import pytest
from pytest_bdd import scenarios, when, then, parsers
from playwright.sync_api import Page

FEATURE = os.path.join(os.path.dirname(__file__), "..", "..", "features", "filtro_categoria.feature")
scenarios(FEATURE)

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


@when(parsers.parse('o usuário aplica o filtro por culinária "{culinaria}"'))
def aplicar_filtro(page: Page, culinaria: str):
    page.locator(f".filter-btn[data-cuisine='{culinaria}']").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(500)


@when(parsers.parse('o usuário remove o filtro selecionando "{rotulo}"'))
def remover_filtro(page: Page, rotulo: str):
    page.locator(".filter-btn[data-cuisine='']").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(500)


@then(parsers.parse('o botão de filtro "{culinaria}" está marcado como ativo'))
def botao_filtro_ativo(page: Page, culinaria: str):
    if culinaria == "Todos":
        filtro = page.locator(".filter-btn[data-cuisine='']")
    else:
        filtro = page.locator(f".filter-btn[data-cuisine='{culinaria}']")
    classes = filtro.get_attribute("class") or ""
    assert "active" in classes, f"Esperava 'active' nas classes do botão '{culinaria}', mas obteve: '{classes}'"
