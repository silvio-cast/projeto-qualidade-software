# PBL10 – Modelos de Maturidade

> Centro Universitário Senac-RS
> ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet
> Unidade Curricular: Qualidade de Software | Prof.: Luciano Zanuz
> Aula 15

## 👥 Integrantes

- Silvio Eduardo Cezarino de Castilhos
- Murilo da Silva Noguêz

---

## 🔹 1. Diagnóstico de Maturidade

A avaliação abaixo considera o processo adotado pela equipe ao longo das entregas do projeto LocalEats (PBL6 a PBL9):

| Critério | Sim | Parcial | Não |
|---|:---:|:---:|:---:|
| Os requisitos são documentados? | | ✅ | |
| Existe controle de mudanças? | | ✅ | |
| Há atividades de teste definidas? | ✅ | | |
| Os defeitos são registrados? | | ✅ | |
| O processo de desenvolvimento é conhecido por toda a equipe? | ✅ | | |
| As tarefas são planejadas e acompanhadas regularmente? | | ✅ | |
| Existe padronização para implementação de funcionalidades? | | ✅ | |
| Os testes são executados antes da entrega das funcionalidades? | ✅ | | |
| Há revisão de código ou validação por outro integrante da equipe? | ✅ | | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | ✅ | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | ✅ | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | ✅ | |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | | ✅ |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | ✅ | |

### Classificação de Maturidade

**Nível: Gerenciado (Nível 2 – CMMI)**

**Justificativa:** A equipe possui práticas de qualidade recorrentes e reconhecíveis: testes automatizados são executados antes de toda entrega, o código é versionado no GitHub, há revisão cruzada entre os integrantes e os artefatos (código, testes, documentação) estão organizados em estrutura de pastas consistente. No entanto, o processo não está formalmente documentado — ele existe na prática, mas de forma implícita. Não há retrospectivas formais, rastreabilidade explícita entre requisitos e testes, nem métricas coletadas e analisadas sistematicamente. Essas características correspondem ao **Nível Gerenciado (2)** do CMMI: o processo é planejado e executado de acordo com práticas estabelecidas, mas ainda depende do conhecimento tácito da equipe para funcionar, sem padronização que permita replicação consistente em novos contextos ou por novos membros.

---

## 🔹 2. Identificação de Lacunas

| Lacuna | Impacto |
|---|---|
| **Ausência de retrospectivas formais** | A equipe não tem um momento estruturado para refletir sobre o que funcionou e o que pode melhorar em cada entrega, perdendo oportunidades de evolução contínua do processo. |
| **Rastreabilidade requisito → teste incompleta** | Não existe mapeamento explícito entre os critérios de aceite do enunciado e os testes que os cobrem. Se um requisito muda, não é trivial identificar quais testes precisam ser atualizados. |
| **Ausência de métricas coletadas sistematicamente** | A equipe sabe quais testes passam (pelo output do pytest), mas não acompanha indicadores como cobertura de código, densidade de defeitos por entrega ou tempo médio de resolução de falhas. |
| **Processo não documentado formalmente** | O fluxo de trabalho existe na prática, mas não está escrito. Um novo integrante ou um avaliador externo não consegue entender como a equipe trabalha sem perguntar diretamente aos membros. |
| **Gestão de defeitos informal** | Falhas encontradas nos testes são corrigidas imediatamente, mas não são registradas como Issues no GitHub. Isso impede análise histórica de defeitos recorrentes. |

---

## 🔹 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| **Criar um CONTRIBUTING.md documentando o fluxo de trabalho** | Torna o processo explícito e replicável; facilita a entrada de novos integrantes e serve como referência para toda a equipe. |
| **Adotar GitHub Issues para registrar todos os defeitos encontrados** | Cria rastreabilidade histórica; permite identificar padrões de falha e medir o tempo de resolução de defeitos. |
| **Realizar uma retrospectiva rápida ao final de cada PBL (10 min)** | Gera aprendizado incremental: o que funcionou, o que atrapalhou e o que mudar na próxima entrega — base da melhoria contínua (Nível 3 CMMI). |
| **Configurar coleta automática de cobertura de código no pipeline CI** | Produz métricas objetivas de qualidade (ex: `pytest --cov`), permitindo acompanhar a evolução da cobertura entre entregas. |
| **Criar uma matriz de rastreabilidade requisito → caso de teste** | Garante que cada critério de aceite do enunciado é coberto por pelo menos um teste, eliminando lacunas de validação e facilitando o impacto de mudanças. |

### Evolução de Maturidade Esperada

Implementando as melhorias acima, a equipe migraria do **Nível 2 (Gerenciado)** para o **Nível 3 (Definido)** do CMMI: o processo estaria documentado, padronizado e com métricas para acompanhamento, permitindo que qualquer membro da equipe siga o mesmo fluxo de forma consistente, independentemente do PBL ou funcionalidade em questão.
