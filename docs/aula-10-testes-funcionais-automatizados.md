# Aula 10 – Testes Funcionais Automatizados

## 👥 Integrantes

- Silvio Castilhos
- Murilo Noguez

---

## 📁 Estrutura do Projeto

```
projeto-qualidade-software/
├── pages/
│   ├── login_page.py
│   └── carrinho_page.py
├── tests/
│   └── e2e/
│       ├── conftest.py
│       ├── test_login.py
│       └── test_carrinho.py
└── docs/
    └── aula-10-testes-funcionais-automatizados.md
```

---

## 🔹 1. Fluxos Funcionais Escolhidos

### 👤 Silvio Castilhos – Fluxo 1: Login de usuário

| Atributo | Descrição |
|----------|-----------|
| **O que faz** | Permite autenticar um usuário no sistema via e-mail e senha |
| **Problema que resolve** | Garante acesso seguro às funcionalidades protegidas |
| **Importância** | Fluxo crítico de entrada — sem autenticação o usuário não acessa restaurantes nem pode fazer pedidos |

**Cenários testados:**
- Página de login carrega com os campos corretos
- Credenciais inválidas exibem mensagem de erro
- Cadastro + login com novas credenciais redireciona para a home
- Botão "Criar Conta" exibe o formulário de registro

---

### 👤 Murilo Noguez – Fluxo 4: Adição de item ao carrinho

| Atributo | Descrição |
|----------|-----------|
| **O que faz** | Navega por restaurantes e adiciona produtos ao carrinho |
| **Problema que resolve** | Garante que o fluxo de compra principal funciona corretamente |
| **Importância** | Etapa central do processo de pedido — falha aqui impede qualquer venda |

**Cenários testados:**
- Lista de restaurantes carregada na home
- Clicar em restaurante navega para detalhes
- Cardápio é exibido na página do restaurante
- Adicionar item atualiza o badge do carrinho
- Total do carrinho atualiza corretamente após adição

---

## 🔹 2. Teste Automatizado com Codegen

### Geração — Fluxo de Login (Silvio)

**Comando utilizado:**
```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

**Código gerado automaticamente pelo Codegen:**

```python
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/")
    # redirecionado automaticamente para /static/login.html
    page.locator("#loginEmail").click()
    page.locator("#loginEmail").fill("teste@teste.com")
    page.locator("#loginEmail").press("Tab")
    page.locator("#loginPassword").fill("123456")
    page.locator("#loginPassword").press("Enter")
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("button", name="Criar Conta").click()
    page.locator("#regName").click()
    page.locator("#regName").fill("Teste")
    page.locator("#regEmail").fill("novo@teste.com")
    page.locator("#regPassword").fill("teste123")
    page.locator("#registerForm").get_by_role("button").click()
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

**Observações iniciais:**
- O Codegen registrou corretamente os IDs dos campos (`#loginEmail`, `#loginPassword`)
- Gerou um `.press("Tab")` e `.press("Enter")` desnecessários (interação literal do teclado durante a gravação)
- Não adicionou nenhum `assert` — código puro de interação, sem verificação
- Não tratou a questão da autenticação necessária para acessar certas páginas
- Gravou ações extras de navegação que foram acidentais durante o processo

**O que o Codegen fez bem:**
- Capturou os seletores de ID (`#loginEmail`, `#showRegisterBtn`) de forma precisa
- Registrou a sequência de eventos de forma fiel ao que foi executado

**O que gerou código desnecessário:**
- `press("Tab")` e `press("Enter")` — interações acidentais de teclado que não são necessárias
- Navegações duplicadas para a mesma página
- Sem `wait_for_load_state` ou esperas explícitas
- Sem qualquer asserção de comportamento esperado
- Falta de tratamento de autenticação prévia

---

### Geração — Fluxo de Carrinho (Murilo)

**Código gerado automaticamente pelo Codegen:**

```python
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    page.locator(".rest-card").nth(0).click()
    page.locator("div:nth-child(1) > .menu-item > .menu-action > .add-cart-btn").click()
    page.locator("div:nth-child(2) > .menu-item > .menu-action > .add-cart-btn").click()
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

**Observações iniciais:**
- O seletor `div:nth-child(1) > .menu-item > .menu-action > .add-cart-btn` é extremamente frágil — qualquer mudança na estrutura do DOM ou ordem dos elementos quebra o teste
- Gravou dois cliques em "Adicionar" por engano durante o processo de gravação
- Não verificou se os cards de restaurante estavam carregados antes de clicar
- Sem nenhuma asserção do estado do carrinho após a adição

**O que o Codegen fez bem:**
- Capturou a classe `.rest-card` e `.add-cart-btn` corretamente

**O que gerou código desnecessário:**
- `nth(0)` via seletor posicional — frágil se a ordem mudar
- Seletor `div:nth-child(1) > .menu-item > ...` — cadeia de seletores estruturais extremamente quebradiça
- Ação duplicada de adicionar item (engano durante gravação)

---

## 🔹 3. Implementação do Teste com Pytest

### Fluxo de Login — `tests/e2e/test_login.py` (versão inicial, pré-POM)

```python
import pytest
from playwright.sync_api import Page

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


def test_pagina_login_carrega(page: Page):
    page.goto(f"{BASE_URL}/login.html")
    page.wait_for_load_state("networkidle")
    assert page.locator("#loginEmail").is_visible()
    assert page.locator("#loginPassword").is_visible()


def test_login_credenciais_invalidas(page: Page):
    page.goto(f"{BASE_URL}/login.html")
    page.wait_for_load_state("networkidle")
    page.locator("#loginEmail").fill("naoexiste@email.com")
    page.locator("#loginPassword").fill("senhaerrada")
    page.locator("#loginForm button[type='submit']").click()
    page.locator("#errorMsg").wait_for(state="visible", timeout=8000)
    assert page.locator("#errorMsg").is_visible()


def test_toggle_para_cadastro(page: Page):
    page.goto(f"{BASE_URL}/login.html")
    page.wait_for_load_state("networkidle")
    page.locator("#showRegisterBtn").click()
    assert page.locator("#regName").is_visible()
```

### Fluxo de Carrinho — `tests/e2e/test_carrinho.py` (versão inicial, pré-POM)

```python
import pytest
from playwright.sync_api import Page

BASE_URL = "https://local-eats-unisenac.vercel.app/static"


def test_lista_restaurantes(page: Page):
    page.goto(f"{BASE_URL}/login.html")
    page.evaluate("""() => {
        localStorage.setItem('userId', '999');
        localStorage.setItem('userName', 'Teste');
    }""")
    page.goto(f"{BASE_URL}/index.html")
    page.wait_for_selector(".rest-card", timeout=15000)
    assert page.locator(".rest-card").count() > 0


def test_adicionar_item(page: Page):
    page.goto(f"{BASE_URL}/login.html")
    page.evaluate("""() => {
        localStorage.setItem('userId', '999');
        localStorage.setItem('userName', 'Teste');
    }""")
    page.goto(f"{BASE_URL}/index.html")
    page.wait_for_selector(".rest-card", timeout=15000)
    page.locator(".rest-card").first.click()
    page.wait_for_selector("#menuList .menu-item")
    badge_antes = page.locator("#cartCountBadge").text_content()
    page.locator(".add-cart-btn").first.click()
    page.wait_for_timeout(300)
    assert badge_antes != page.locator("#cartCountBadge").text_content()
```

---

## 🔹 4. Refatoração com Page Object Model (POM)

### `pages/login_page.py`

```python
BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class LoginPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(f"{BASE_URL}/login.html")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("#loginEmail", state="visible", timeout=10000)

    def preencher_login(self, email, senha):
        self.page.locator("#loginEmail").fill(email)
        self.page.locator("#loginPassword").fill(senha)

    def submeter_login(self):
        self.page.locator("#loginForm button[type='submit']").click()

    def preencher_cadastro(self, nome, email, senha):
        self.page.locator("#showRegisterBtn").click()
        self.page.locator("#regName").fill(nome)
        self.page.locator("#regEmail").fill(email)
        self.page.locator("#regPassword").fill(senha)

    def submeter_cadastro(self):
        self.page.locator("#registerForm button[type='submit']").click()

    def mensagem_erro(self):
        return self.page.locator("#errorMsg")

    def badge_usuario(self):
        return self.page.locator("#userBadge")

    def esta_autenticado(self):
        return self.page.locator("#logoutBtn").is_visible()
```

### `pages/carrinho_page.py`

```python
BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class CarrinhoPage:
    def __init__(self, page):
        self.page = page

    def acessar_home(self):
        self.page.goto(f"{BASE_URL}/index.html")
        self.page.wait_for_selector(".rest-card", timeout=15000)

    def autenticar(self, nome="Teste PBL", user_id="999"):
        # Navega para o domínio primeiro para poder escrever no localStorage
        self.page.goto(f"{BASE_URL}/login.html")
        self.page.wait_for_load_state("networkidle")
        self.page.evaluate(
            f"""() => {{
                localStorage.setItem('userId', '{user_id}');
                localStorage.setItem('userName', '{nome}');
            }}"""
        )
        # Navega para a home agora autenticado
        self.acessar_home()

    def clicar_primeiro_restaurante(self):
        self.page.locator(".rest-card").first.click()

    def aguardar_cardapio(self):
        self.page.wait_for_selector("#menuList .menu-item", timeout=10000)

    def adicionar_primeiro_item(self):
        self.page.locator(".add-cart-btn").first.click()

    def badge_contagem_carrinho(self):
        return self.page.locator("#cartCountBadge")

    def total_carrinho(self):
        return self.page.locator("#cartTotalValue")

    def carrinho_visivel(self):
        return self.page.locator(".floating-cart").is_visible()

    def finalizar_pedido(self):
        self.page.locator("#checkoutBtn").click()

    def modal_sucesso_visivel(self):
        return self.page.locator("#orderSuccessModal").is_visible()
```

### `tests/e2e/test_login.py` (com POM)

```python
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
```

### `tests/e2e/test_carrinho.py` (com POM)

```python
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
```

---

## 🔹 5. Execução dos Testes

**Comando executado:**
```bash
pytest tests/e2e/ --tb=short -v
```

**Resultado:**

```
============================= test session info ==============================
platform win32 -- Python 3.13.2, pytest-9.0.3, pluggy-1.6.0
plugins: anyio-4.9.0, base-url-2.1.0, playwright-0.8.0

collected 9 items

tests/e2e/test_carrinho.py::test_lista_restaurantes_carregada[chromium]         PASSED [ 11%]
tests/e2e/test_carrinho.py::test_clicar_restaurante_abre_detalhes[chromium]     PASSED [ 22%]
tests/e2e/test_carrinho.py::test_cardapio_exibido_na_pagina_restaurante[chromium] PASSED [ 33%]
tests/e2e/test_carrinho.py::test_adicionar_item_ao_carrinho[chromium]           PASSED [ 44%]
tests/e2e/test_carrinho.py::test_total_carrinho_atualiza_apos_adicao[chromium]  PASSED [ 55%]
tests/e2e/test_login.py::test_pagina_login_carrega[chromium]                    PASSED [ 66%]
tests/e2e/test_login.py::test_login_credenciais_invalidas[chromium]             PASSED [ 77%]
tests/e2e/test_login.py::test_login_sucesso_apos_cadastro[chromium]             PASSED [ 88%]
tests/e2e/test_login.py::test_toggle_para_cadastro[chromium]                    PASSED [100%]

============================= 9 passed in 28.92s ==============================
```

| Métrica | Valor |
|---------|-------|
| Total de testes | 9 |
| Passaram | 9 |
| Falharam | 0 |
| Tempo total | 28,92 segundos |
| Navegador | Chromium (headless) |

---

## 🔹 6. Análise Crítica dos Testes

### O teste quebrou em algum momento? Por quê?

Sim — todos os 9 testes falharam nas duas primeiras execuções por razões distintas:

**Primeira execução (100% falha):** Os testes apontavam para `https://local-eats-unisenac.vercel.app/login.html`, mas a aplicação hospedada na Vercel serve os arquivos estáticos sob o prefixo `/static/`. O URL correto é `https://local-eats-unisenac.vercel.app/static/login.html`. A rota sem o prefixo retorna `{"detail":"Not Found"}`, tornando todos os seletores inexistentes.

**Segunda execução (8/9 falharam):** Após corrigir o URL, os testes do carrinho falhavam porque tentávamos acessar `index.html` antes de autenticar. O `auth.js` da aplicação oculta o conteúdo de restaurantes para usuários não autenticados — o `.restaurant-grid` estava no DOM mas invisível. A solução foi injetar a autenticação via `localStorage.setItem('userId', ...)` antes de navegar para a home.

**Terceira execução (1/9 falhou):** O teste `test_login_credenciais_invalidas` falhou porque o `assert` era executado imediatamente após o clique de submit, sem aguardar a resposta da API. O backend levava alguns segundos para retornar o erro. A solução foi adicionar `mensagem_erro().wait_for(state="visible", timeout=8000)`.

**Quarta execução e em diante (9/9 passou):** O teste `test_login_sucesso_apos_cadastro` era frágil por usar um `wait_for_timeout(500)` fixo. O cadastro redireciona para `index.html` via `window.location.href`, e o redirect ocorre antes do timeout. O teste então tentava preencher `#loginEmail` que estava escondido (pois a tela de registro estava ativa). A solução foi usar `wait_for_url("**/index.html")` que aguarda a navegação de forma determinística.

### Quais seletores foram mais difíceis?

O maior desafio foi identificar que o `#loginEmail` existia no DOM mas ficava invisível quando o formulário de cadastro estava ativo. O Playwright's `is_visible()` retorna `False` para elementos com `display: none` (via classe `hidden`) — comportamento correto mas que exigiu entender o fluxo de UI.

Para o carrinho, o seletor `.restaurant-grid` estava presente mas não visível sem autenticação. A diferença entre "elemento existe no DOM" e "elemento está visível" foi crucial.

### O Codegen ajudou ou gerou problemas?

Ajudou como **ponto de partida** para identificar os IDs corretos dos campos (`#loginEmail`, `#loginPassword`, `#loginForm`). O Codegen identificou com precisão os seletores semânticos como `#showRegisterBtn` e a estrutura dos formulários.

Gerou problemas ao:
- Criar seletores posicionais como `div:nth-child(1) > .menu-item > .menu-action > .add-cart-btn` — quebram com qualquer reordenação de elementos
- Registrar ações acidentais de teclado (`.press("Tab")`, `.press("Enter")`)
- Não incluir nenhuma asserção
- Não considerar estados de carregamento ou autenticação

### O teste é confiável? Por quê?

Os testes são **razoavelmente confiáveis** com algumas ressalvas:

**Pontos fortes:**
- Usam seletores de ID e classe semânticos (`#loginEmail`, `.add-cart-btn`) em vez de seletores XPath frágeis
- Aguardam explicitamente por elementos antes de interagir (`wait_for_selector`, `wait_for_url`)
- Cada teste é independente — não há estado compartilhado entre eles
- O teste de login cria usuários com timestamp para evitar conflitos

**Riscos de confiabilidade:**
- O `wait_for_timeout(300)` e `wait_for_timeout(500)` são esperas fixas que podem ser insuficientes em redes lentas — deveriam ser substituídos por esperas baseadas em eventos/estado
- `test_login_sucesso_apos_cadastro` cria usuários no banco de dados real da aplicação a cada execução — pode acumular dados de teste
- Os testes dependem de dados reais do backend (restaurantes, cardápios) — se o banco estiver vazio ou offline, os testes do carrinho falham

### O que tornaria o teste mais robusto?

1. **Substituir `wait_for_timeout` por assertions baseadas em estado:**
   ```python
   # Frágil
   page.wait_for_timeout(300)
   assert badge_depois != badge_antes

   # Robusto
   page.locator("#cartCountBadge").wait_for(state="visible")
   expect(page.locator("#cartCountBadge")).not_to_have_text(badge_antes)
   ```

2. **Usar `data-testid` attributes nos elementos HTML** — seletores de teste dedicados que não mudam com refatoração visual

3. **Criar um usuário de teste fixo** via script de setup em vez de registrar a cada execução

4. **Isolar testes do carrinho com dados mockados** via `page.route()` para interceptar chamadas de API

### Quais são os riscos de manutenção?

- Se a aplicação mudar o prefixo de URL (`/static/` → outro prefixo), todos os testes quebram em um ponto centralizado (fácil de corrigir graças ao `BASE_URL` nas classes)
- Se o HTML mudar de `.rest-card` para outra classe, apenas `carrinho_page.py` precisa ser atualizado — o POM centraliza essa mudança
- Se o backend mudar o tempo de resposta, os `wait_for_timeout` fixos podem causar falhas intermitentes

---

## 🔹 7. Reflexão no Contexto do LocalEats

### Testes automatizados substituem testes manuais?

Não completamente. Os testes automatizados verificam fluxos **funcionalmente corretos do ponto de vista lógico**, mas não percebem:
- Problemas visuais (botão azul quando deveria ser verde, texto cortado)
- Usabilidade (fluxo confuso mesmo que funcione tecnicamente)
- Comportamento em dispositivos móveis e resoluções diferentes

O ideal é uma combinação: testes automatizados para regressão e validação de fluxos críticos, testes manuais exploratórios para percepção de UX e cenários não mapeados.

### Vale a pena automatizar todos os fluxos?

Não — o custo de criação e manutenção dos testes deve ser menor que o benefício. Para o LocalEats, priorizaríamos:

**Alta prioridade (automatizar):** Login, adição ao carrinho, finalização de pedido — fluxos críticos que, se quebrarem, impedem uso do sistema.

**Média prioridade:** Navegação de restaurantes, busca/filtros — importantes mas menos críticos.

**Baixa prioridade (manter manual):** Telas de perfil, histórico de pedidos, favoritos — fluxos menos frequentes e com menor impacto em receita.

### Qual tipo de teste deve ser priorizado?

Para o LocalEats, a pirâmide ideal seria:

```
        /  E2E (Playwright)  \      ← Fluxos críticos
       /  Integração (API)    \     ← Regras de negócio + persistência
      /  Unitários (Pytest)    \    ← Lógica isolada (cálculos, validações)
```

Os **testes unitários** (já implementados nas aulas anteriores) são mais rápidos e baratos. Os **testes E2E** garantem que os fluxos completos funcionam do ponto de vista do usuário, mas são mais lentos e frágeis.

### Como isso ajuda no projeto do grupo?

A automação dos fluxos de login e carrinho cria uma **rede de segurança para deploys**: antes de publicar qualquer mudança no frontend, rodamos `pytest tests/e2e/` e em menos de 30 segundos sabemos se os fluxos principais continuam funcionando. Isso resolve diretamente o problema identificado no início do projeto: "falta de confiança em deploys" e "fluxos quebrando após mudanças no frontend".

A organização com POM também significa que se o HTML do site mudar (ex: renomear `.rest-card` para `.restaurant-card`), a correção acontece em **um único arquivo** (`carrinho_page.py`) em vez de espalhada por múltiplos testes.
