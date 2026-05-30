import os
import pytest
from pytest_bdd import scenarios, when, parsers
from playwright.sync_api import Page

FEATURE = os.path.join(os.path.dirname(__file__), "..", "..", "features", "busca_restaurantes.feature")
scenarios(FEATURE)

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


@when(parsers.parse('o usuário pesquisa por "{termo}"'))
def pesquisar(page: Page, termo: str):
    page.locator("#searchInput").fill(termo)
    page.locator("#searchBtn").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(800)


@when("o usuário realiza uma busca com o campo vazio")
def pesquisar_vazio(page: Page):
    page.locator("#searchInput").fill("")
    page.locator("#searchBtn").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(500)
