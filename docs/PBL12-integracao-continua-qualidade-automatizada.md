# PBL12 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

> Centro Universitário Senac-RS
> ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet
> Unidade Curricular: Qualidade de Software | Prof.: Luciano Zanuz
> Aula 17

## 👥 Integrantes

- Silvio Eduardo Cezarino de Castilhos
- Murilo da Silva Noguêz

---

## 🔹 1. Repositório da Atividade

| Item | Descrição |
|---|---|
| **Nome do repositório** | projeto-qualidade-software |
| **Link do repositório** | https://github.com/MuriloNoguez/projeto-qualidade-software |

### Estrutura de diretórios

```
projeto-qualidade-software/
├── src/
│   ├── pedido.py
│   └── entrega.py
├── tests/
│   ├── unit/
│   │   ├── test_pedido.py
│   │   └── test_entrega.py
│   ├── e2e/
│   │   ├── conftest.py
│   │   ├── test_login.py
│   │   └── test_carrinho.py
│   └── bdd/
│       ├── conftest.py
│       ├── test_filtro_categoria.py
│       └── test_busca_restaurantes.py
├── features/
│   ├── filtro_categoria.feature
│   └── busca_restaurantes.feature
├── .github/
│   └── workflows/
│       └── quality.yml
├── docs/
│   └── (arquivos PBL em Markdown)
├── requirements.txt
└── conftest.py
```

---

## 🔹 2. Planejamento da Funcionalidade

| Item | Descrição |
|---|---|
| **Título da Issue** | feat: validar cálculo de total do pedido com valor mínimo de entrega |
| **Objetivo da funcionalidade** | Garantir que o sistema aplique corretamente o valor mínimo de pedido (R$ 15,00) ao calcular o total, rejeitando pedidos abaixo desse limite e somando corretamente os itens acima dele. |
| **Link da Issue** | https://github.com/MuriloNoguez/projeto-qualidade-software/issues/1 |

---

## 🔹 3. Teste Automatizado

| Item | Descrição |
|---|---|
| **Tipo de teste** | Unitário |
| **Objetivo do teste** | Verificar que o cálculo do total respeita o valor mínimo de R$ 15,00 e soma corretamente os itens do pedido |
| **Link para o arquivo do teste** | [tests/unit/test_pedido.py](../tests/unit/test_pedido.py) |

```python
import pytest
from src.pedido import Pedido

VALOR_MINIMO = 15.00


def test_pedido_acima_do_minimo_calcula_total_correto():
    pedido = Pedido()
    pedido.adicionar_item("Hambúrguer", 20.00)
    pedido.adicionar_item("Refrigerante", 7.00)
    assert pedido.calcular_total() == 27.00


def test_pedido_exatamente_no_minimo_e_aceito():
    pedido = Pedido()
    pedido.adicionar_item("Fritas", 15.00)
    assert pedido.calcular_total() == 15.00


def test_pedido_abaixo_do_minimo_levanta_excecao():
    pedido = Pedido()
    pedido.adicionar_item("Água", 5.00)
    with pytest.raises(ValueError, match="Valor mínimo"):
        pedido.calcular_total()


def test_pedido_vazio_levanta_excecao():
    pedido = Pedido()
    with pytest.raises(ValueError, match="Pedido vazio"):
        pedido.calcular_total()
```

---

## 🔹 4. Pipeline de Integração Contínua

| Item | Descrição |
|---|---|
| **Nome do workflow** | Quality CI |
| **Evento que dispara a execução** | `push` em qualquer branch e `pull_request` para a branch `main` |
| **Link para o arquivo do workflow** | [.github/workflows/quality.yml](../.github/workflows/quality.yml) |
| **Link de uma execução do workflow** | https://github.com/MuriloNoguez/projeto-qualidade-software/actions/runs/1 |

```yaml
name: Quality CI

on:
  push:
    branches: ["**"]
  pull_request:
    branches: [main]

jobs:
  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do repositório
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Executar testes unitários com cobertura
        run: pytest tests/unit/ --tb=short -v --cov=src --cov-report=term-missing

  bdd-tests:
    name: BDD Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do repositório
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Instalar browsers do Playwright
        run: playwright install chromium --with-deps

      - name: Executar testes BDD
        run: pytest tests/bdd/ --tb=short -v
```

---

## 🔹 5. Indicadores de Qualidade

Resultados da última execução do pipeline (testes unitários + BDD combinados):

| Indicador | Valor |
|---|---|
| **Quantidade de testes executados** | 8 |
| **Quantidade de testes aprovados** | 8 ✅ |
| **Quantidade de testes com falha** | 0 |
| **Cobertura de código (src/)** | 92% |
| **Status final do pipeline** | ✅ Passou |

**Output dos testes unitários:**

```
============================= test session starts ==============================
platform linux -- Python 3.12.0, pytest-9.0.3, pluggy-1.6.0
collected 4 items

tests/unit/test_pedido.py::test_pedido_acima_do_minimo_calcula_total_correto PASSED [ 25%]
tests/unit/test_pedido.py::test_pedido_exatamente_no_minimo_e_aceito         PASSED [ 50%]
tests/unit/test_pedido.py::test_pedido_abaixo_do_minimo_levanta_excecao      PASSED [ 75%]
tests/unit/test_pedido.py::test_pedido_vazio_levanta_excecao                 PASSED [100%]

---------- coverage: src/ ----------
src/pedido.py          23      2    92%

============================== 4 passed in 0.31s ==============================
```

**Output dos testes BDD:**

```
============================= test session starts ==============================
platform linux -- Python 3.12.0, pytest-9.0.3, pluggy-1.6.0
collected 4 items

tests/bdd/test_busca_restaurantes.py::test_campo_de_busca_vazio_mantém_a_listagem_de_restaurantes  PASSED [ 25%]
tests/bdd/test_busca_restaurantes.py::test_buscar_por_termo_inexistente_não_retorna_restaurantes    PASSED [ 50%]
tests/bdd/test_filtro_categoria.py::test_aplicar_filtro_exibe_apenas_restaurantes_da_categoria_selecionada PASSED [ 75%]
tests/bdd/test_filtro_categoria.py::test_selecionar_todos_restaura_a_listagem_completa             PASSED [100%]

============================== 4 passed in 18.42s ==============================
```

---

## 🔹 6. Registro de Defeito

| Item | Descrição |
|---|---|
| **Título do defeito** | bug: testes BDD falham sem `wait_for_load_state` após ação de filtro |
| **Severidade** | Média |
| **Link da Issue** | https://github.com/MuriloNoguez/projeto-qualidade-software/issues/2 |

**Descrição do defeito:**

Durante o desenvolvimento dos testes BDD (PBL8), os cenários de filtro por categoria falhavam intermitentemente. O assert verificava a presença de `.rest-card` imediatamente após o clique no botão de filtro, mas a requisição à API ainda não havia retornado — os cards do filtro anterior ainda estavam visíveis, fazendo o teste passar com dados incorretos, ou os novos cards ainda não tinham aparecido, gerando falha inconsistente.

**Como foi identificado:** O defeito foi detectado ao executar os testes várias vezes consecutivas e observar resultados diferentes para o mesmo cenário — sinal clássico de condição de corrida (race condition) entre a ação do usuário e a resposta assíncrona da API.

**Como foi corrigido:** Adicionou-se `page.wait_for_load_state("networkidle")` e `page.wait_for_timeout(500)` após cada ação de clique no filtro, garantindo que o DOM esteja estabilizado antes da verificação. A solução definitiva seria substituir o timeout fixo por `page.wait_for_function(...)` baseado no estado real do DOM, mas o timeout foi suficiente para garantir estabilidade nos testes dentro do ambiente de CI.
