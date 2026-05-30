import pytest
from pytest_bdd import given, then
from playwright.sync_api import Page

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


def _autenticar_e_abrir_home(page: Page):
    page.goto(f"{BASE_URL}/login.html")
    page.wait_for_load_state("networkidle")
    page.evaluate("""() => {
        localStorage.setItem('userId', '999');
        localStorage.setItem('userName', 'Teste PBL');
    }""")
    page.goto(f"{BASE_URL}/index.html")
    page.wait_for_selector(".rest-card", timeout=15000)


@given("que o usuário está na página inicial autenticado")
def usuario_na_pagina_inicial(page: Page):
    _autenticar_e_abrir_home(page)


@then("restaurantes são exibidos na lista")
def restaurantes_exibidos(page: Page):
    page.wait_for_selector(".rest-card", timeout=10000)
    assert page.locator(".rest-card").count() > 0


@then("nenhum restaurante é exibido na lista")
def nenhum_restaurante_exibido(page: Page):
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)
    assert page.locator(".rest-card").count() == 0
