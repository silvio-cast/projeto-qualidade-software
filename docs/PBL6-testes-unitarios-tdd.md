# Aula 9 – Testes Unitários e TDD

## 👥 Integrantes

- Silvio Castilhos
- Murilo Noguez

---

## 📁 Estrutura do Projeto

```
projeto-qualidade-software/
├── src/
│   ├── pedido.py
│   └── entrega.py
├── tests/
│   ├── test_pedido.py
│   └── test_entrega.py
└── conftest.py
```

---

## 🔹 1. Funcionalidades escolhidas

Cada integrante ficou responsável por uma regra de negócio do sistema.

### 👤 Silvio Castilhos – Cálculo do total do pedido com valor mínimo

Arquivo da implementação: `/src/pedido.py`  
Arquivo de testes: `/tests/test_pedido.py`

**Descrição**  
Soma os valores dos itens do pedido e valida se o total atinge o valor mínimo exigido pelo restaurante.

**Regras de negócio**
- Soma dos itens define o total
- Pedido deve atingir o valor mínimo
- Caso contrário, deve gerar erro
- Pedido vazio também deve gerar erro

---

### 👤 Murilo Noguez – Cálculo de taxa de entrega

Arquivo da implementação: `/src/entrega.py`  
Arquivo de testes: `/tests/test_entrega.py`

**Descrição**  
Calcula a taxa de entrega com base na distância entre o restaurante e o cliente.

**Regras de negócio**
- Até 3km → taxa fixa de R$5,00
- Acima de 3km → taxa fixa + R$2,00 por km extra
- Distância negativa → erro
- Distância zero → erro

---

## 🔹 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta `/tests`.

---

### 🧪 Silvio Castilhos – Testes (pedido)

**Implementação — `src/pedido.py`:**

```python
def calcular_total_pedido(itens, valor_minimo):
    if not itens:
        raise ValueError("O pedido não pode estar vazio")
    total = sum(item["preco"] for item in itens)
    if total < valor_minimo:
        raise ValueError(
            f"Valor mínimo de R${valor_minimo:.2f} não atingido. Total: R${total:.2f}"
        )
    return total
```

---

#### Teste 1 – Valor acima do mínimo

- **Cenário:** Soma dos itens supera o valor mínimo exigido
- **Dados de entrada:** `itens=[{20.00}, {15.00}]`, `valor_minimo=30.00`
- **Resultado esperado:** Retorna `35.00` sem erros

```python
def test_deve_calcular_total_quando_valor_minimo_atingido():
    # Arrange
    itens = [{"preco": 20.00}, {"preco": 15.00}]
    valor_minimo = 30.00
    # Act
    resultado = calcular_total_pedido(itens, valor_minimo)
    # Assert
    assert resultado == 35.00
```

**TDD**
- 🔴 Red: teste falhou pois a função `calcular_total_pedido` ainda não existia
- 🟢 Green: função implementada com soma dos itens e validação do mínimo
- 🔵 Refactor: mensagem de erro enriquecida com os valores envolvidos

**Refatoração**
- Variáveis renomeadas de `t`/`i` para `total`/`item`
- Loop manual substituído por `sum()` com generator expression
- Mensagem de erro passou a exibir o valor mínimo e o total calculado

**Execução:** ✅ Passou

---

#### Teste 2 – Valor abaixo do mínimo

- **Cenário:** Soma dos itens é insuficiente para o pedido
- **Dados de entrada:** `itens=[{5.00}, {8.00}]`, `valor_minimo=20.00`
- **Resultado esperado:** `ValueError` com mensagem "Valor mínimo"

```python
def test_deve_lancar_erro_quando_total_abaixo_do_valor_minimo():
    # Arrange
    itens = [{"preco": 5.00}, {"preco": 8.00}]
    valor_minimo = 20.00
    # Act / Assert
    with pytest.raises(ValueError, match="Valor mínimo"):
        calcular_total_pedido(itens, valor_minimo)
```

**TDD**
- 🔴 Red: teste esperava erro mas função ainda não lançava exceção
- 🟢 Green: exceção `ValueError` implementada na validação do mínimo
- 🔵 Refactor: mensagem de erro detalhada com valores reais

**Refatoração**
- Tratamento explícito do erro com mensagem descritiva

**Execução:** ✅ Passou

---

#### Teste 3 – Valor exatamente igual ao mínimo

- **Cenário:** Total dos itens é igual ao mínimo — limite aceitável
- **Dados de entrada:** `itens=[{10.00}, {20.00}]`, `valor_minimo=30.00`
- **Resultado esperado:** Retorna `30.00` sem erros

```python
def test_deve_calcular_total_exatamente_igual_ao_valor_minimo():
    # Arrange
    itens = [{"preco": 10.00}, {"preco": 20.00}]
    valor_minimo = 30.00
    # Act
    resultado = calcular_total_pedido(itens, valor_minimo)
    # Assert
    assert resultado == 30.00
```

**Execução:** ✅ Passou

---

#### Teste 4 – Pedido vazio

- **Cenário:** Lista de itens vazia enviada à função
- **Dados de entrada:** `itens=[]`, `valor_minimo=20.00`
- **Resultado esperado:** `ValueError` com mensagem "vazio"

```python
def test_deve_lancar_erro_quando_pedido_esta_vazio():
    with pytest.raises(ValueError, match="vazio"):
        calcular_total_pedido([], 20.00)
```

**Execução:** ✅ Passou

---

**Log — 🔴 Red (pedido):**

```
========================================================== test session starts ===========================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Python312\python.exe
plugins: base-url-2.1.0, playwright-0.8.0, anyio-4.9.0
collected 0 items / 1 error

================================================================= ERRORS =================================================================
_________________________________________________ ERROR collecting tests/test_pedido.py __________________________________________________
ImportError while importing test module '...\tests\test_pedido.py'.
tests\test_pedido.py:2: in <module>
    from src.pedido import calcular_total_pedido
E   ImportError: cannot import name 'calcular_total_pedido' from 'src.pedido'
=========================================================== 1 error in 1.17s ============================================================
```

**Log — 🟢 Green / 🔵 Refactor (pedido):**

```
========================================================== test session starts ===========================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Windows 10\Desktop\SILVIO (IMPORTANTE)\faculdade\quinto_semestre\projeto-qualidade-software
plugins: base-url-2.1.0, playwright-0.8.0, anyio-4.9.0
collected 4 items

tests/test_pedido.py::test_deve_calcular_total_quando_valor_minimo_atingido PASSED                                                  [ 25%]
tests/test_pedido.py::test_deve_calcular_total_exatamente_igual_ao_valor_minimo PASSED                                              [ 50%]
tests/test_pedido.py::test_deve_lancar_erro_quando_total_abaixo_do_valor_minimo PASSED                                              [ 75%]
tests/test_pedido.py::test_deve_lancar_erro_quando_pedido_esta_vazio PASSED                                                         [100%]
=========================================================== 4 passed in 0.12s ============================================================
```

---

### 🧪 Murilo Noguez – Testes (entrega)

**Implementação — `src/entrega.py`:**

```python
def calcular_taxa_entrega(distancia_km):
    TAXA_FIXA = 5.00
    TAXA_POR_KM_EXTRA = 2.00
    LIMITE_TAXA_FIXA = 3.0

    if distancia_km < 0:
        raise ValueError("Distância não pode ser negativa")
    if distancia_km == 0:
        raise ValueError("Distância deve ser maior que zero")

    if distancia_km <= LIMITE_TAXA_FIXA:
        return TAXA_FIXA

    km_extra = distancia_km - LIMITE_TAXA_FIXA
    return round(TAXA_FIXA + (km_extra * TAXA_POR_KM_EXTRA), 2)
```

---

#### Teste 1 – Distância até 3km

- **Cenário:** Entrega dentro da faixa de taxa fixa
- **Dados de entrada:** `2.0 km`
- **Resultado esperado:** `R$5.00`

```python
def test_deve_cobrar_taxa_fixa_para_distancia_ate_3km():
    # Arrange
    distancia = 2.0
    # Act
    resultado = calcular_taxa_entrega(distancia)
    # Assert
    assert resultado == 5.00
```

**TDD**
- 🔴 Red: teste falhou pois a função `calcular_taxa_entrega` ainda não existia
- 🟢 Green: função implementada retornando taxa fixa para distâncias até 3km
- 🔵 Refactor: números mágicos substituídos por constantes nomeadas

**Refatoração**
- `5.00`, `2.00` e `3.0` substituídos por `TAXA_FIXA`, `TAXA_POR_KM_EXTRA` e `LIMITE_TAXA_FIXA`
- `else` desnecessário removido após o `return`
- `round()` adicionado para precisão monetária

**Execução:** ✅ Passou

---

#### Teste 2 – Distância negativa

- **Cenário:** Valor inválido de distância
- **Dados de entrada:** `-1.0 km`
- **Resultado esperado:** `ValueError` com mensagem "negativa"

```python
def test_deve_lancar_erro_para_distancia_negativa():
    with pytest.raises(ValueError, match="negativa"):
        calcular_taxa_entrega(-1.0)
```

**TDD**
- 🔴 Red: teste esperava erro mas função não validava distância negativa
- 🟢 Green: validação implementada no início da função
- 🔵 Refactor: validações agrupadas no início seguindo padrão fail fast

**Refatoração**
- Validações de entrada consolidadas no topo da função

**Execução:** ✅ Passou

---

#### Teste 3 – Distância exatamente 3km

- **Cenário:** Limite superior da faixa fixa — ainda não cobra extra
- **Dados de entrada:** `3.0 km`
- **Resultado esperado:** `R$5.00`

```python
def test_deve_cobrar_taxa_fixa_para_distancia_exatamente_3km():
    distancia = 3.0
    resultado = calcular_taxa_entrega(distancia)
    assert resultado == 5.00
```

**Execução:** ✅ Passou

---

#### Teste 4 – Distância acima de 3km

- **Cenário:** 5km → 3km fixo (R$5) + 2km extra × R$2/km = R$9
- **Dados de entrada:** `5.0 km`
- **Resultado esperado:** `R$9.00`

```python
def test_deve_cobrar_taxa_proporcional_para_distancia_acima_de_3km():
    resultado = calcular_taxa_entrega(5.0)
    assert resultado == 9.00
```

**Execução:** ✅ Passou

---

#### Teste 5 – Distância zero

- **Cenário:** Distância zero não faz sentido para entrega
- **Dados de entrada:** `0 km`
- **Resultado esperado:** `ValueError` com mensagem "maior que zero"

```python
def test_deve_lancar_erro_para_distancia_zero():
    with pytest.raises(ValueError, match="maior que zero"):
        calcular_taxa_entrega(0)
```

**Execução:** ✅ Passou

---

**Log — 🔴 Red (entrega):**

```
========================================================== test session starts ===========================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Python312\python.exe
plugins: base-url-2.1.0, playwright-0.8.0, anyio-4.9.0
collected 0 items / 1 error

================================================================= ERRORS =================================================================
_________________________________________________ ERROR collecting tests/test_entrega.py _________________________________________________
ImportError while importing test module '...\tests\test_entrega.py'.
tests\test_entrega.py:2: in <module>
    from src.entrega import calcular_taxa_entrega
E   ImportError: cannot import name 'calcular_taxa_entrega' from 'src.entrega'
=========================================================== 1 error in 0.41s ============================================================
```

**Log — 🟢 Green / 🔵 Refactor (entrega):**

```
========================================================== test session starts ===========================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Windows 10\Desktop\SILVIO (IMPORTANTE)\faculdade\quinto_semestre\projeto-qualidade-software
plugins: base-url-2.1.0, playwright-0.8.0, anyio-4.9.0
collected 5 items

tests/test_entrega.py::test_deve_cobrar_taxa_fixa_para_distancia_ate_3km PASSED                                                     [ 20%]
tests/test_entrega.py::test_deve_cobrar_taxa_fixa_para_distancia_exatamente_3km PASSED                                              [ 40%]
tests/test_entrega.py::test_deve_cobrar_taxa_proporcional_para_distancia_acima_de_3km PASSED                                        [ 60%]
tests/test_entrega.py::test_deve_lancar_erro_para_distancia_negativa PASSED                                                         [ 80%]
tests/test_entrega.py::test_deve_lancar_erro_para_distancia_zero PASSED                                                             [100%]
=========================================================== 5 passed in 0.25s ============================================================
```

---

## 🔹 3. Reflexão

**Foi difícil escrever testes antes do código?**  
Sim, pois exige uma mudança de mentalidade. O instinto é sempre implementar primeiro. Escrever o teste antes obriga a pensar no comportamento esperado da função antes de pensar no algoritmo, o que no início parece estranho mas ajuda a definir melhor o que precisa ser feito.

**O TDD ajudou no desenvolvimento?**  
Sim, ajudou a estruturar melhor a lógica antes da implementação. O ciclo Red → Green → Refactor deu um ritmo claro ao desenvolvimento: primeiro definir o que deve funcionar, depois fazer funcionar, depois melhorar. Isso evitou implementações desnecessárias.

**Os testes aumentaram a confiança no código?**  
Sim, pois qualquer erro pode ser detectado rapidamente. Com 9 testes cobrindo os dois módulos, qualquer alteração no código pode ser verificada em segundos rodando `pytest`, o que dá segurança para evoluir o sistema.

**O que melhorariam?**
- Cobrir mais cenários de borda, como itens com preço zero
- Melhor organização com fixtures do pytest para reaproveitar dados de teste
- Adicionar `pytest-cov` para medir a cobertura de código

**Como isso ajuda no projeto?**  
Permite evoluir o sistema com mais segurança e qualidade. No LocalEats, regras como valor mínimo de pedido e taxa de entrega impactam diretamente o usuário e o restaurante — ter testes automatizados garante que essas regras continuem funcionando mesmo após mudanças no código.

---

## 🔹 4. Execução Final

```
========================================================== test session starts ===========================================================
platform win32 -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Windows 10\Desktop\SILVIO (IMPORTANTE)\faculdade\quinto_semestre\projeto-qualidade-software
plugins: base-url-2.1.0, playwright-0.8.0, anyio-4.9.0
collected 9 items

tests/test_entrega.py::test_deve_cobrar_taxa_fixa_para_distancia_ate_3km PASSED                                                     [ 11%]
tests/test_entrega.py::test_deve_cobrar_taxa_fixa_para_distancia_exatamente_3km PASSED                                              [ 22%]
tests/test_entrega.py::test_deve_cobrar_taxa_proporcional_para_distancia_acima_de_3km PASSED                                        [ 33%]
tests/test_entrega.py::test_deve_lancar_erro_para_distancia_negativa PASSED                                                         [ 44%]
tests/test_entrega.py::test_deve_lancar_erro_para_distancia_zero PASSED                                                             [ 55%]
tests/test_pedido.py::test_deve_calcular_total_quando_valor_minimo_atingido PASSED                                                  [ 66%]
tests/test_pedido.py::test_deve_calcular_total_exatamente_igual_ao_valor_minimo PASSED                                              [ 77%]
tests/test_pedido.py::test_deve_lancar_erro_quando_total_abaixo_do_valor_minimo PASSED                                              [ 88%]
tests/test_pedido.py::test_deve_lancar_erro_quando_pedido_esta_vazio PASSED                                                         [100%]
=========================================================== 9 passed in 0.09s ============================================================
```

| Métrica | Resultado |
|---|---|
| **Total de testes** | 9 |
| **Passaram** | ✅ 9 |
| **Falharam** | ❌ 0 |
| **Tempo de execução** | 0,09s |
