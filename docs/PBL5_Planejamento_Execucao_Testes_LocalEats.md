# Planejamento e Execução de Testes - LocalEats (PBL 5)

**Sistema:** LocalEats (plataforma de busca de restaurantes)  
**Data:** 21/04/2026  
**Responsável:** Analista de QA Sênior

## 1. Plano de Testes

### 1.1 Objetivo
Validar a qualidade funcional e não funcional dos fluxos críticos do LocalEats, com foco em autenticação, busca e gerenciamento de favoritos, identificando falhas relacionadas a desempenho em picos de acesso, inconsistência de resultados de busca, problemas em dispositivos mobile e persistência de avaliações.

### 1.2 Escopo

**O que testar:**
- Login de usuário válido e inválido.
- Busca por restaurantes com filtros e termos específicos.
- Tratamento de busca sem resultados.
- Adição e visualização de restaurantes em Favoritos.
- Comportamento da aplicação em cenário de conexão instável.
- Tempo de resposta das funcionalidades críticas sob carga moderada e pico.
- Compatibilidade básica em dispositivos mobile (responsividade e interação principal).

**O que não testar (neste ciclo):**
- Testes de segurança avançados (pentest, fuzzing, análise de vulnerabilidades).
- Integrações externas não críticas (ex.: serviços de marketing, analytics).
- Testes de regressão completos de módulos administrativos.
- Certificação formal de desempenho em larga escala com infraestrutura dedicada.

### 1.3 Funcionalidades Prioritárias
- **Login:** autenticação, validação de credenciais e tratamento de erro.
- **Busca:** consulta por nome/categoria/localização, ordenação e retorno de resultados consistentes.
- **Favoritos:** inclusão e persistência de restaurantes marcados pelo usuário.

### 1.4 Estratégia de Testes
- **Abordagem:** testes funcionais manuais orientados a risco + validação exploratória.
- **Técnica:** elaboração de cenários em Gherkin para rastreabilidade (requisito -> cenário -> evidência).
- **Criticidade:** priorização de jornadas de alto impacto de negócio (login, busca, favoritos).
- **Critérios de entrada:** ambiente de homologação disponível, dados de teste preparados, usuários de teste ativos.
- **Critérios de saída:** execução de 100% dos cenários planejados, registro de evidências e classificação de severidade dos defeitos.

### 1.5 Responsáveis

| Papel | Responsabilidades no ciclo de testes |
|---|---|
| QA Líder | Elaborar plano de testes, definir critérios de cobertura, revisar evidências e consolidar relatório final. |
| QA Analista | Especificar e executar casos de teste, registrar defeitos e classificar severidade. |
| Desenvolvedor(a) | Apoiar reprodução de bugs, corrigir falhas e executar testes unitários/regressão técnica das correções. |
| Product Owner | Validar critérios de aceite de negócio e priorizar correções conforme impacto ao usuário. |

## 2. Casos de Teste (Gherkin)

### CT-01 - Login com credenciais válidas (Sucesso)
**Dado que** o usuário está na tela de login  
**E** possui credenciais válidas cadastradas  
**Quando** informar e-mail e senha corretos e clicar em "Entrar"  
**Então** o sistema deve autenticar o usuário  
**E** redirecionar para a página inicial

### CT-02 - Busca de restaurante com termo válido (Sucesso)
**Dado que** o usuário está autenticado no LocalEats  
**Quando** pesquisar por "pizza" na barra de busca  
**Então** o sistema deve retornar restaurantes relacionados ao termo  
**E** exibir nome, avaliação e faixa de preço corretamente

### CT-03 - Adicionar restaurante aos favoritos (Sucesso)
**Dado que** o usuário está na página de detalhes de um restaurante  
**Quando** clicar no botão "Adicionar aos Favoritos"  
**Então** o restaurante deve ser incluído na lista de favoritos  
**E** permanecer salvo após atualizar a página

### CT-04 - Busca sem resultados (Erro esperado)
**Dado que** o usuário está autenticado no LocalEats  
**Quando** pesquisar por "restaurante_xyz_inexistente"  
**Então** o sistema deve informar "Nenhum resultado encontrado"  
**E** sugerir filtros ou termos alternativos

### CT-05 - Falha de conexão durante login (Erro esperado)
**Dado que** o usuário está na tela de login  
**E** a conexão com a internet está instável  
**Quando** tentar autenticar com credenciais válidas  
**Então** o sistema deve exibir mensagem de indisponibilidade temporária  
**E** permitir nova tentativa sem perda dos dados digitados

## 3. Execução dos Testes (Simulação)

| ID | Cenário | Resultado Esperado | Resultado Obtido | Status | Evidência |
|---|---|---|---|---|---|
| CT-01 | Login com credenciais válidas | Usuário autenticado e redirecionado | Fluxo concluído com redirecionamento para home em 1,2s | **Passou** | Captura de tela da home após login e log de autenticação HTTP 200 |
| CT-02 | Busca por termo válido ("pizza") | Lista coerente de restaurantes de pizza | Retornou itens não relacionados (ex.: "Sushi Prime") em posição superior | **Falhou** | Evidência em vídeo da consulta + payload de resposta da API com categorização inconsistente |
| CT-03 | Adicionar aos favoritos | Item adicionado e persistido após refresh | Restaurante salvo em favoritos e persistente após atualização da página | **Passou** | Capturas antes/depois da marcação e verificação no endpoint de favoritos |
| CT-04 | Busca sem resultados | Mensagem "Nenhum resultado encontrado" | Mensagem exibida corretamente com sugestão de filtros | **Passou** | Captura da tela de resultado vazio e log funcional do front-end |
| CT-05 | Falha de conexão durante login | Mensagem de indisponibilidade e opção de nova tentativa | Requisição excedeu tempo limite sem feedback claro ao usuário (timeout) | **Falhou** | Registro no console com timeout de 30s, ausência de toast/mensagem e trace de rede interrompida |

## 4. Análise dos Resultados

### 4.1 Resumo Quantitativo
- Total de testes executados: **5**
- Testes aprovados: **3**
- Testes reprovados: **2**
- Taxa de aprovação: **60%**
- Taxa de reprovação: **40%**

### 4.2 Problemas Críticos Encontrados
1. **Inconsistência de relevância na busca** (CT-02): o motor de busca retorna resultados semanticamente incorretos, impactando diretamente a experiência do usuário e a conversão.
2. **Ausência de tratamento resiliente para timeout/conexão instável no login** (CT-05): falta de feedback e recuperação de erro, aumentando risco de abandono.

### 4.3 Impacto no Negócio
- Redução da confiabilidade da plataforma em seu fluxo principal (descoberta de restaurantes).
- Aumento do churn em usuários mobile e em cenários de rede degradada.
- Potencial perda de receita por falha em jornadas críticas de entrada no produto.

## 5. Reflexão Crítica

O planejamento estruturado permitiu transformar sintomas percebidos (lentidão, busca incorreta e falhas em mobile) em hipóteses testáveis com evidências objetivas. Sem essa formalização, defeitos de alta severidade poderiam passar despercebidos por parecerem intermitentes ou dependentes de contexto de rede/carga. A modelagem em Gherkin melhorou a comunicação entre QA, produto e desenvolvimento, garantindo critérios claros de aceitação e reprodutibilidade.

Como melhoria de processo para a startup, recomenda-se:
- Adotar suíte mínima de regressão automatizada para login, busca e favoritos.
- Introduzir testes de desempenho contínuos em horários de pico simulado.
- Implementar observabilidade orientada a UX (tempo de resposta percebido, erro por fluxo, abandono por etapa).
- Definir política de qualidade com gates em CI/CD (bloqueio de deploy com falhas críticas abertas).
- Expandir cobertura de testes mobile e cenários de conectividade degradada desde a fase de refinamento.

Esse ciclo mostrou que um plano de QA orientado a risco acelera a descoberta de falhas relevantes ao negócio e reduz retrabalho, elevando a maturidade técnica do produto de forma incremental.
