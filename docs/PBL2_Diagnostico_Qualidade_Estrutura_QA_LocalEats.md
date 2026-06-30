# PBL 2 – Diagnóstico de Qualidade
**Estrutura de QA da Startup Local Eats**

> Centro Universitário Senac-RS
> ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet
> Unidade Curricular: Qualidade de Software | Prof.: Luciano Zanuz

---

## Etapa 1 – Diagnóstico da Situação Atual

A startup Local Eats encontra-se em fase crítica de crescimento. Problemas recorrentes como erros na finalização de pedidos, pedidos duplicados e funcionalidades com defeitos em produção indicam ausência de processos formais de garantia de qualidade (QA). A análise do cenário aponta os seguintes diagnósticos:

### Papéis provavelmente existentes na startup hoje

- **Desenvolvedor(es):** responsáveis por codificar as funcionalidades — provavelmente acumulam também testes informais.
- **Analista de Sistemas / Product Owner:** levanta requisitos e define o escopo das funcionalidades.
- **Gerente de Produto / Sócio fundador:** define prioridades e aprova entregas para produção.
- **DevOps informal (ou o próprio desenvolvedor):** cuida do deploy e da infraestrutura de forma não estruturada.

### Quem é responsável pela qualidade atualmente?

Provavelmente ninguém de forma explícita. A responsabilidade recai de maneira informal sobre os próprios desenvolvedores, sem critérios, processos ou registros definidos. Não há papel dedicado de QA, nem práticas sistemáticas de testes.

### Problemas causados pela falta de clareza nas responsabilidades

- Defeitos chegam à produção sem detecção prévia, gerando impacto direto nos usuários finais.
- Não há rastreabilidade: quando um bug surge, não se sabe quem deveria tê-lo identificado.
- Retrabalho elevado: o custo de corrigir defeitos em produção é muito maior do que em fases anteriores.
- Perda de confiança dos clientes (restaurantes e consumidores) na plataforma.
- Ausência de critérios de aceite: funcionalidades são entregues sem validação formal.

### A qualidade é responsabilidade de uma pessoa ou de toda a equipe?

A qualidade de software é uma responsabilidade compartilhada. Embora um profissional de QA coordene os processos e práticas de teste, cada membro da equipe contribui: o desenvolvedor escreve código testável e realiza testes unitários; o analista valida requisitos; o DevOps garante a estabilidade do ambiente. O papel de QA é o guardião do processo, não o único responsável pela ausência de defeitos.

---

## Etapa 2 – Proposta de Organização da Qualidade

### 2.1 Definição de Papéis da Equipe

| Papel | Principais Responsabilidades | Relação com a Qualidade |
|---|---|---|
| **Desenvolvedor** | Codificar funcionalidades; escrever testes unitários; corrigir defeitos reportados; realizar revisão de código (code review). | Qualidade começa no código: boas práticas, código limpo e testes unitários reduzem a densidade de defeitos. |
| **QA / Analista de Qualidade** | Planejar e executar testes manuais e exploratórios; registrar e acompanhar defeitos; definir critérios de aceite; validar entregas. | Papel central na garantia de qualidade: assegura que o produto atende aos requisitos antes de chegar à produção. |
| **Analista de Sistemas** | Levantar e documentar requisitos; revisar histórias de usuário; validar regras de negócio junto ao cliente. | Requisitos bem definidos evitam retrabalho e são a base para os critérios de teste. |
| **DevOps** | Configurar pipelines de CI/CD; monitorar ambiente de produção; garantir estabilidade dos deploys. | Automatiza a execução de testes no pipeline e garante que somente builds aprovados cheguem à produção. |
| **Gerente de Produto (PO)** | Definir prioridades do backlog; aprovar entregas; comunicar expectativas ao time. | Define e prioriza os critérios de qualidade do produto sob a perspectiva de negócio. |

### 2.2 Responsabilidades Relacionadas à Qualidade

| Atividade | Responsável Principal | Participantes de Apoio |
|---|---|---|
| Revisar e validar requisitos | Analista de Sistemas | QA, Gerente de Produto |
| Definir critérios de aceite | QA + Analista de Sistemas | Gerente de Produto |
| Escrever testes unitários | Desenvolvedor | — |
| Executar testes funcionais manuais | QA | Desenvolvedor |
| Realizar testes exploratórios | QA | — |
| Registrar e acompanhar defeitos | QA | Desenvolvedor, Analista |
| Validar funcionalidade antes do deploy | QA | Gerente de Produto |
| Configurar e executar pipeline de CI/CD | DevOps | Desenvolvedor |
| Monitorar erros em produção | DevOps | QA, Desenvolvedor |
| Aprovar entrega para produção | Gerente de Produto | QA |

### 2.3 Práticas Básicas de QA Sugeridas

#### 1. Testes manuais das funcionalidades principais

Antes de qualquer deploy, o QA executa testes manuais nos fluxos críticos (realizar pedido, finalizar pagamento, notificar restaurante). Garante que as funções essenciais estão operando corretamente e evita que defeitos graves cheguem à produção.

#### 2. Registro e acompanhamento de defeitos (bug tracking)

Utilizar uma ferramenta (ex.: Jira, GitHub Issues, Trello) para registrar todos os defeitos encontrados, atribuir responsáveis, acompanhar a correção e verificar o fechamento. Proporciona rastreabilidade e histórico de qualidade do produto.

#### 3. Testes exploratórios

Sessões de exploração livre do sistema sem roteiro fixo, com o objetivo de descobrir comportamentos inesperados. Complementam os testes baseados em roteiro e são eficazes para encontrar defeitos não previstos nos casos de teste formais.

#### 4. Revisão de critérios de aceite antes do desenvolvimento

Para cada funcionalidade nova, o QA e o Analista de Sistemas definem critérios claros de aceite (Definition of Done) antes que o desenvolvimento comece. Evita ambiguidades, retrabalho e alinha as expectativas do time com as do cliente.

#### 5. Testes de regressão a cada nova entrega

Após a correção de defeitos ou adição de novas funcionalidades, executar um conjunto de testes nos fluxos já validados para garantir que nenhuma mudança quebrou algo que funcionava. Minimiza o risco de regressão — problema documentado na plataforma Local Eats com o desaparecimento de avaliações.

---

## Etapa 3 – Anúncios de Contratação

### Vaga 1: Analista de Qualidade de Software (QA)

> Local Eats | Porto Alegre – RS | Presencial / Híbrido | CLT ou PJ

#### Sobre a vaga

A Local Eats está buscando um(a) Analista de Qualidade de Software para integrar a equipe de desenvolvimento e estruturar os processos de QA da plataforma. O profissional atuará em colaboração direta com desenvolvedores, analistas e o gerente de produto, garantindo que cada funcionalidade entregue atenda aos requisitos de qualidade e às expectativas dos usuários.

#### Principais responsabilidades

- Planejar, documentar e executar casos de teste manuais e exploratórios.
- Definir critérios de aceite junto ao Analista de Sistemas e ao Gerente de Produto.
- Registrar, priorizar e acompanhar defeitos até o fechamento.
- Validar funcionalidades antes de cada deploy em produção.
- Identificar riscos de qualidade e propor melhorias nos processos de desenvolvimento.
- Colaborar com o DevOps na criação de testes automatizados básicos no pipeline de CI/CD.

#### Requisitos obrigatórios

- Experiência com planejamento e execução de testes de software (mínimo 1 ano).
- Conhecimento de técnicas de teste: caixa-preta, testes funcionais, regressão e exploratórios.
- Capacidade de documentar casos de teste e relatórios de defeitos com clareza.
- Noções básicas de sistemas web e mobile (HTTP, APIs REST, bancos de dados).
- Boa comunicação, organização e perfil colaborativo.

#### Requisitos desejáveis

- Experiência com ferramentas de gestão de defeitos (Jira, GitHub Issues ou similar).
- Noções de automação de testes (Selenium, Cypress ou Playwright).
- Conhecimento de versionamento com Git.
- Familiaridade com metodologias ágeis (Scrum / Kanban).
- Experiência em testes de APIs (Postman ou Insomnia).

#### Certificações relevantes

- ISTQB – CTFL (Certified Tester Foundation Level) — desejável.
- ISTQB – CTFL-AT (Agile Tester) — diferencial.

---

### Vaga 2: Desenvolvedor(a) Full Stack

> Local Eats | Porto Alegre – RS | Híbrido / Remoto | CLT ou PJ

#### Sobre a vaga

Buscamos um(a) Desenvolvedor(a) Full Stack para atuar no desenvolvimento e manutenção da plataforma Local Eats (web e mobile). O profissional participará de todo o ciclo de desenvolvimento, desde o planejamento até a entrega, contribuindo ativamente para a qualidade do produto por meio de boas práticas de código, testes e revisão de pares.

#### Principais responsabilidades

- Desenvolver e manter funcionalidades nas versões web e mobile da plataforma.
- Escrever testes unitários e de integração para o código produzido.
- Participar de revisões de código (code review) garantindo padrões de qualidade.
- Identificar e corrigir defeitos registrados pelo time de QA.
- Colaborar com o QA na definição de critérios de aceite técnico.
- Documentar decisões técnicas e manter o repositório organizado.

#### Requisitos obrigatórios

- Experiência com desenvolvimento web (JavaScript/TypeScript, HTML, CSS).
- Conhecimento de frameworks modernos: React ou Vue.js (front-end); Node.js, Django ou similar (back-end).
- Familiaridade com APIs REST e consumo/criação de serviços.
- Experiência com bancos de dados relacionais (PostgreSQL ou MySQL).
- Uso de Git para versionamento de código.
- Conhecimento básico de testes unitários (Jest, Mocha ou similar).

#### Requisitos desejáveis

- Experiência com desenvolvimento mobile (React Native ou Flutter).
- Noções de CI/CD e ferramentas de conteinerização (Docker).
- Conhecimento de metodologias ágeis (Scrum / Kanban).
- Experiência com testes de integração e end-to-end.
- Familiaridade com ferramentas de monitoramento (Sentry, Datadog ou similar).

#### Certificações relevantes

- AWS Certified Developer / Google Associate Cloud Engineer — diferencial.
- Certificações em frameworks específicos (React, Node.js) — diferencial.
