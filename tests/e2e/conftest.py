import pytest

BASE_URL = "https://local-eats-unisenac.vercel.app/static"
EMAIL_TESTE = "pbl10_teste@localeats.com"
SENHA_TESTE = "teste123"
NOME_TESTE = "Usuario PBL10"


@pytest.fixture
def usuario_registrado(page):
    """Registra e autentica um usuário de teste via fluxo de cadastro."""
    page.goto(f"{BASE_URL}/login.html")
    page.locator("#showRegisterBtn").click()
    page.locator("#regName").fill(NOME_TESTE)
    page.locator("#regEmail").fill(EMAIL_TESTE)
    page.locator("#regPassword").fill(SENHA_TESTE)
    page.locator("#registerForm button[type='submit']").click()
    return page


@pytest.fixture
def usuario_autenticado_via_storage(page):
    """Injeta autenticação via localStorage para testes de carrinho."""
    page.goto(f"{BASE_URL}/index.html")
    page.evaluate("""() => {
        localStorage.setItem('userId', '999');
        localStorage.setItem('userName', 'Teste PBL');
    }""")
    page.reload()
    return page
