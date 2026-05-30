import sys
import os
import time
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pages.login_page import LoginPage

SENHA = "teste123"
NOME = "Silvio PBL10"


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.acessar()
    return lp


def test_pagina_login_carrega(login_page, page):
    """Verifica que a página de login carrega os elementos principais."""
    assert page.locator("#loginEmail").is_visible()
    assert page.locator("#loginPassword").is_visible()
    assert page.locator("#loginForm button[type='submit']").is_visible()


def test_login_credenciais_invalidas(login_page, page):
    """Testa que credenciais incorretas exibem mensagem de erro."""
    login_page.preencher_login("naoexiste@email.com", "senhaerrada")
    login_page.submeter_login()

    # Aguarda a resposta da API antes de verificar o erro
    login_page.mensagem_erro().wait_for(state="visible", timeout=8000)
    assert login_page.mensagem_erro().is_visible()


def test_login_sucesso_apos_cadastro(login_page, page):
    """Testa login com usuário recém-cadastrado: cadastro → logout → login."""
    email = f"pbl10_{int(time.time())}@localeats.com"

    # 1. Cadastra novo usuário (redireciona para index.html automaticamente)
    login_page.preencher_cadastro(NOME, email, SENHA)
    login_page.submeter_cadastro()
    page.wait_for_url("**/index.html", timeout=10000)

    # 2. Remove autenticação para simular logout
    page.evaluate("() => { localStorage.removeItem('userId'); localStorage.removeItem('userName'); }")

    # 3. Volta para login e testa com credenciais cadastradas
    login_page.acessar()
    login_page.preencher_login(email, SENHA)
    login_page.submeter_login()

    page.wait_for_url("**/index.html", timeout=10000)
    assert "index.html" in page.url


def test_toggle_para_cadastro(login_page, page):
    """Verifica que o botão 'Criar Conta' exibe o formulário de registro."""
    page.locator("#showRegisterBtn").click()

    assert page.locator("#regName").is_visible()
    assert page.locator("#regEmail").is_visible()
    assert page.locator("#regPassword").is_visible()
