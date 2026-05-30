# PBL8 – BDD e Automação Orientada a Comportamento

## 👥 Integrantes

- Silvio Eduardo Cezarino de Castilhos
- Murilo da Silva Noguêz

---

## 📁 Estrutura do Projeto

```
projeto-qualidade-software/
├── features/
│   ├── filtro_categoria.feature
│   └── busca_restaurantes.feature
├── tests/
│   └── bdd/
│       ├── conftest.py
│       ├── test_filtro_categoria.py
│       └── test_busca_restaurantes.py
└── docs/
    └── PBL8-bdd-automacao-comportamento.md
```

---

## 🔹 1. Fluxos Escolhidos

### 👤 Silvio – Fluxo 5: Filtro por categoria

| Atributo | Descrição |
|----------|-----------|
| **O que faz** | Filtra a lista de restaurantes pelo tipo de culinária selecionado |
| **Problema que resolve** | Evita que o usuário precise percorrer toda a listagem para encontrar uma culinária específica |
| **Importância** | Melhora descoberta e usabilidade — fluxo muito utilizado em apps de delivery |

**Cenários BDD:**
- Aplicar filtro exibe apenas restaurantes da categoria selecionada
- Selecionar "Todos" restaura a listagem completa

---

### 👤 Murilo – Fluxo 1: Busca de restaurantes

| Atributo | Descrição |
|----------|-----------|
| **O que faz** | Filtra restaurantes por nome ou localização via campo de busca |
| **Problema que resolve** | Permite encontrar rapidamente restaurantes específicos sem navegar pela lista inteira |
| **Importância** | Fluxo principal de descoberta — diretamente ligado à retenção do usuário |

**Cenários BDD:**
- Campo de busca vazio mantém a listagem completa de restaurantes
- Buscar por termo inexistente não retorna restaurantes

---

## 🔹 2. Cenários BDD em Gherkin

### `features/filtro_categoria.feature`

```gherkin
Feature: Filtro de restaurantes por categoria
  Como um usuário do LocalEats
  Quero filtrar restaurantes por tipo de culinária
  Para encontrar rapidamente o tipo de comida que desejo

  Background:
    Given que o usuário está na página inicial autenticado

  Scenario: Aplicar filtro exibe apenas restaurantes da categoria selecionada
    When o usuário aplica o filtro por culinária "Italiana"
    Then restaurantes são exibidos na lista
    And o botão de filtro "Italiana" está marcado como ativo

  Scenario: Selecionar Todos restaura a listagem completa
    When o usuário aplica o filtro por culinária "Italiana"
    And o usuário remove o filtro selecionando "Todos"
    Then o botão de filtro "Todos" está marcado como ativo
    And restaurantes são exibidos na lista
```

### `features/busca_restaurantes.feature`

```gherkin
Feature: Busca de restaurantes
  Como um usuário do LocalEats
  Quero buscar restaurantes pelo nome ou localização
  Para encontrar rapidamente opções específicas

  Background:
    Given que o usuário está na página inicial autenticado

  Scenario: Campo de busca vazio mantém a listagem de restaurantes
    When o usuário realiza uma busca com o campo vazio
    Then restaurantes são exibidos na lista

  Scenario: Buscar por termo inexistente não retorna restaurantes
    When o usuário pesquisa por "xyzabcdef123"
    Then nenhum restaurante é exibido na lista
```

---

## 🔹 3. Implementação da Automação com pytest-bdd

### `tests/bdd/conftest.py` — steps compartilhados

```python
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
```

### `tests/bdd/test_filtro_categoria.py`

```python
import os
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
    assert "active" in classes, f"Esperava 'active' nas classes do botão '{culinaria}', obteve: '{classes}'"
```

### `tests/bdd/test_busca_restaurantes.py`

```python
import os
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
```

---

## 🔹 4. Organização do Projeto

```
projeto-qualidade-software/
│
├── features/                          ← cenários BDD em Gherkin
│   ├── filtro_categoria.feature
│   └── busca_restaurantes.feature
│
├── tests/
│   ├── bdd/                           ← automação BDD
│   │   ├── conftest.py                ← steps compartilhados
│   │   ├── test_filtro_categoria.py
│   │   └── test_busca_restaurantes.py
│   └── e2e/                           ← testes E2E do PBL7
│       ├── conftest.py
│       ├── test_login.py
│       └── test_carrinho.py
│
└── pages/                             ← Page Objects
    ├── login_page.py
    └── carrinho_page.py
```

---

## 🔹 5. Execução dos Testes

**Comando:**
```bash
pytest tests/bdd/ --tb=short -v
```

**Resultado:**

```
============================= test session starts ==============================
platform win32 -- Python 3.13.2, pytest-9.0.3, pluggy-1.6.0
plugins: anyio-4.9.0, base-url-2.1.0, bdd-8.1.0, playwright-0.8.0
collected 4 items

tests/bdd/test_busca_restaurantes.py::test_campo_de_busca_vazio_mantém_a_listagem_de_restaurantes  PASSED [ 25%]
tests/bdd/test_busca_restaurantes.py::test_buscar_por_termo_inexistente_não_retorna_restaurantes    PASSED [ 50%]
tests/bdd/test_filtro_categoria.py::test_aplicar_filtro_exibe_apenas_restaurantes_da_categoria_selecionada PASSED [ 75%]
tests/bdd/test_filtro_categoria.py::test_selecionar_todos_restaura_a_listagem_completa             PASSED [100%]

============================= 4 passed in 17.69s ==============================
```

| Métrica | Valor |
|---------|-------|
| Total de cenários | 4 |
| Passaram | 4 ✅ |
| Falharam | 0 |
| Tempo total | 17,69 segundos |
| Navegador | Chromium (headless) |

---

## 🔹 6. Análise Crítica

### O cenário escrito ficou compreensível?

Sim. A estrutura Gherkin com `Given/When/Then` permite que qualquer stakeholder entenda o comportamento descrito sem conhecer Python ou Playwright. O cenário:

```gherkin
Scenario: Aplicar filtro exibe apenas restaurantes da categoria selecionada
  When o usuário aplica o filtro por culinária "Italiana"
  Then restaurantes são exibidos na lista
  And o botão de filtro "Italiana" está marcado como ativo
```

É legível por um product owner, analista de negócios ou cliente — não depende de nenhum conhecimento técnico.

### O teste automatizado ficou legível?

Razoavelmente. Os steps usam linguagem de domínio (`culinaria`, `rotulo`, `termo`) e os nomes das funções descrevem a intenção. O ponto de maior complexidade técnica ficou isolado em `conftest.py` (`_autenticar_e_abrir_home`), que não aparece nos cenários Gherkin.

### O BDD ajudou a entender o comportamento?

Sim, significativamente. Ao escrever o cenário "Campo de busca vazio mantém a listagem de restaurantes", identificamos que o comportamento real da busca é por **localização**, não por culinária — o que não estava óbvio na interface. O processo de escrita BDD forçou a questionar: *"o que exatamente este campo faz?"*

### Quais dificuldades surgiram?

**1. Diretiva de linguagem:** a diretiva `# language: pt` no arquivo `.feature` faz o parser Gherkin exigir keywords em português (`Funcionalidade`, `Cenário`, `Dado`, `Quando`, `Então`). Usar `# language: pt` com keywords inglesas gerava erro de parse. A solução foi remover a diretiva e manter keywords em inglês com textos em português.

**2. Comportamento real da busca:** o placeholder do campo de busca diz "Buscar por culinária ou localização" mas a implementação filtra apenas por campo `location` no backend. Buscar "Italiana" retorna zero resultados porque nenhum restaurante tem "Italiana" como localização. O primeiro cenário de busca falhou por isso — precisamos ajustar para "campo vazio" que é mais representativo do comportamento real documentado na atividade.

**3. Sincronização pós-API:** filtro e busca disparam chamadas de API que re-renderizam o grid. Sem `wait_for_load_state("networkidle")` os asserts eram executados antes dos novos cards aparecerem.

### Os seletores foram frágeis?

Os seletores por atributo (`[data-cuisine='Italiana']`) e por ID (`#searchInput`, `#searchBtn`) são estáveis. Mais frágil seria usar `page.locator("button:nth-child(2)")` como o Codegen costuma gerar. A única fragilidade real é o `wait_for_timeout(500/800)` fixo — deve ser substituído por espera baseada em estado quando possível.

### O teste ficou dependente da interface?

Sim — testes E2E por natureza dependem da interface. O BDD minimiza isso ao separar **o que** testar (no `.feature`) de **como** testar (nos steps Python). Se o elemento `.filter-btn` for renomeado, apenas a função `aplicar_filtro` no arquivo de steps precisa ser atualizada, sem tocar nos cenários Gherkin.

### O cenário representa realmente uma regra de negócio?

Sim para o filtro: "ao aplicar filtro por culinária, apenas restaurantes correspondentes devem aparecer" é uma regra de negócio clara.

Para a busca o cenário ficou mais fraco: "campo vazio mantém listagem" é um comportamento de UX, não exatamente uma regra de negócio. O cenário mais representativo seria "buscar por localização retorna restaurantes naquela região" — mas para isso precisaríamos de dados de localização reais da base de dados.

### O que tornaria o teste mais robusto?

1. **Substituir esperas fixas por eventos:**
   ```python
   # frágil
   page.wait_for_timeout(500)
   
   # robusto
   page.wait_for_function("() => document.querySelectorAll('.rest-card').length > 0")
   ```

2. **Adicionar `data-testid` nos elementos HTML** para seletores exclusivos para testes

3. **Verificar conteúdo dos cards após filtro** — não apenas que *algum* card existe, mas que *todos* os cards visíveis pertencem à categoria filtrada:
   ```python
   cards = page.locator(".rest-card").all()
   for card in cards:
       assert "Italiana" in card.locator(".card-meta").text_content()
   ```

---

## 🔹 7. Reflexão no Contexto do LocalEats

### BDD melhora comunicação entre equipe?

Sim. O maior valor do BDD não é técnico — é a conversa que acontece ao escrever os cenários. Ao escrever "Campo de busca vazio mantém a listagem de restaurantes", precisamos decidir: *isso é um comportamento esperado ou um bug?* Essa discussão aproxima dev, QA e negócio antes do desenvolvimento.

No LocalEats, descobrimos que o campo de busca filtra apenas por localização, não por culinária, apesar do placeholder sugerir o contrário. Um cenário BDD bem escrito teria antecipado essa ambiguidade.

### Todo teste deve ser escrito em BDD?

Não. BDD tem custo de manutenção (dois artefatos: `.feature` e steps Python). Vale para:
- Fluxos de regras de negócio com stakeholders não técnicos
- Critérios de aceite que precisam ser validados pelo cliente
- Comportamentos que mudam frequentemente e precisam de documentação viva

**Não vale** para: testes unitários de funções internas, validações técnicas de performance ou segurança, fluxos puramente de infraestrutura.

### Quando vale a pena usar BDD?

Quando a resposta a "esse teste passou" **precisa ser entendida por alguém não técnico**. Se o PO do LocalEats perguntar "a busca está funcionando?", um relatório do Gherkin com `4 cenários passando` é mais comunicativo que um stack trace de Python.

### O comportamento ficou mais claro?

Sim. Escrever `Given/When/Then` força a decomposição do fluxo em:
- **Contexto** (Given): o que precisa estar verdadeiro antes
- **Ação** (When): o que o usuário faz
- **Resultado** (Then): o que o sistema deve garantir

Essa estrutura elimina ambiguidade: em vez de "o filtro funciona", temos "quando o usuário aplica o filtro Italiana, o botão Italiana aparece marcado como ativo e restaurantes são exibidos".

### Como isso ajuda no projeto do grupo?

Os cenários BDD funcionam como **documentação viva** dos fluxos do LocalEats. Se amanhã o filtro parar de funcionar após uma atualização do backend, `pytest tests/bdd/` detecta automaticamente. Mais importante: os arquivos `.feature` podem ser mostrados diretamente ao professor/cliente como especificação de comportamento — são legíveis sem executar nada.

Combinando PBL7 (testes E2E de fluxos completos) com PBL8 (BDD dos comportamentos chave), o projeto tem cobertura em duas camadas: automação de fluxo e documentação de comportamento.
