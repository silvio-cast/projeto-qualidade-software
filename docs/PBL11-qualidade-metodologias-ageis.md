# PBL11 – Qualidade em Metodologias Ágeis

> Centro Universitário Senac-RS
> ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet
> Unidade Curricular: Qualidade de Software | Prof.: Luciano Zanuz
> Aula 16

## 👥 Integrantes

- Silvio Eduardo Cezarino de Castilhos
- Murilo da Silva Noguêz

---

## 🔹 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|---|---|---|---|
| **Planejamento iterativo** | Parcialmente | Cada PBL funciona como uma iteração: lemos o enunciado, dividimos as tarefas e desenvolvemos dentro do prazo. Não há reunião formal de planejamento, mas há divisão de escopo antes de começar. | Sim — formalizar uma sessão curta de planejamento com definição de tarefas e estimativas antes de cada entrega. |
| **Priorização de funcionalidades** | Parcialmente | A priorização é implícita: funcionalidades pedidas no enunciado são tratadas como obrigatórias; melhorias extras só são feitas se houver tempo. | Sim — usar um backlog simples (GitHub Projects) para registrar e priorizar explicitamente o que será feito. |
| **Entregas incrementais** | Sim | Cada PBL é uma entrega incremental sobre o anterior (ex: PBL6 → testes unitários; PBL7 → E2E; PBL8 → BDD). O projeto evolui a cada aula. | Sim — fazer commits menores e mais frequentes dentro de cada PBL, não apenas um commit final. |
| **Feedback frequente** | Parcialmente | O feedback ocorre pela correção do professor após a entrega e pela revisão mútua entre os integrantes durante o desenvolvimento. Não há feedback contínuo durante o processo. | Sim — solicitar feedback intermediário ao professor antes da entrega final quando houver dúvidas de implementação. |
| **Trabalho colaborativo** | Sim | Cada integrante cobre uma funcionalidade diferente; há revisão cruzada antes do commit. A comunicação acontece de forma direta entre os dois membros. | Sim — documentar as decisões tomadas colaborativamente (ex: comentários em Issues ou PRs no GitHub). |
| **Controle visual das atividades** | Não | Não há quadro Kanban ou qualquer visualização do status das tarefas. O acompanhamento é feito pela memória dos integrantes. | Sim — criar um quadro GitHub Projects com colunas "A fazer / Em andamento / Concluído". |
| **Melhoria contínua** | Parcialmente | Melhorias surgem naturalmente de erros detectados nas entregas anteriores (ex: PBL8 identificou problemas de sincronização que foram corrigidos). Não há retrospectiva formal. | Sim — realizar retrospectiva rápida ao fim de cada entrega para registrar aprendizados. |

### Conclusão

O processo da equipe apresenta vários elementos ágeis funcionando na prática, especialmente entregas incrementais e trabalho colaborativo. O maior ponto fraco é a **ausência de controle visual** e **retrospectivas formais**: a equipe evolui, mas sem documentar o aprendizado. Isso limita a capacidade de identificar padrões de dificuldade recorrentes. As maiores oportunidades de melhoria estão na adoção de ferramentas simples de gestão (GitHub Projects) e na institucionalização de momentos curtos de reflexão ao final de cada entrega.

---

## 🔹 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
|---|---|---|
| **Criar um quadro Kanban no GitHub Projects com colunas "Backlog / Em andamento / Em revisão / Concluído"** | Kanban | Visibilidade do andamento das tarefas em tempo real; identificação de gargalos antes que se tornem bloqueadores. |
| **Adotar Definition of Ready (DoR) antes de iniciar cada funcionalidade** | Scrum / XP | Garante que o escopo está claro antes de qualquer linha de código; elimina retrabalho por ambiguidade no enunciado. |
| **Implementar pair programming virtual em funcionalidades complexas** | XP (Extreme Programming) | Aumenta a qualidade do código produzido; distribui o conhecimento entre os integrantes e reduz o risco de dependência de uma única pessoa. |
| **Realizar retrospectiva de 10 minutos ao final de cada PBL** | Scrum | Gera aprendizado estruturado e melhoria incremental: "O que funcionou?", "O que pode melhorar?", "O que faremos diferente?". |
| **Fazer commits pequenos e frequentes com mensagens descritivas no padrão Conventional Commits** | Lean / Agile Engineering | Reduz o risco de conflito de código; cria histórico claro e rastreável de cada evolução do projeto. |

---

## 🔹 3. Definition of Ready (DoR)

Uma funcionalidade está **pronta para entrar em desenvolvimento** quando:

1. O requisito está descrito com clareza suficiente para que ambos os integrantes entendam o que deve ser implementado.
2. Os critérios de aceite estão definidos — sabe-se exatamente o que precisa ser verdadeiro para a funcionalidade ser considerada correta.
3. Há pelo menos um cenário de teste pensado antes do início do desenvolvimento (seja unitário, funcional ou BDD).
4. Não há bloqueadores técnicos pendentes (ex: dependência de API externa, acesso ao sistema, ferramenta não configurada).
5. A responsabilidade pela implementação foi atribuída a um integrante específico, evitando trabalho duplicado ou lacunas.
6. O integrante responsável tem acesso ao ambiente de desenvolvimento configurado e funcional (Python, pytest, Playwright instalados).

---

## 🔹 4. Definition of Done (DoD)

Uma funcionalidade está **concluída** quando:

1. Os critérios de aceite definidos na DoR foram atendidos e verificados.
2. Os testes automatizados relacionados à funcionalidade estão escritos e passando (`pytest` retorna 0 falhas).
3. O código foi revisado por pelo menos um dos integrantes antes do commit.
4. A documentação Markdown correspondente foi escrita ou atualizada, descrevendo o que foi implementado, como executar e os resultados obtidos.
5. O código e os testes foram commitados e estão disponíveis no repositório GitHub na branch correta.
6. Nenhum teste existente anteriormente foi quebrado pela nova implementação (ausência de regressão).
7. O arquivo Markdown da entrega inclui evidência de execução dos testes (output do terminal ou tabela de resultados).
