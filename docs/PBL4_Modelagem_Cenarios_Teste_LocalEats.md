# Atividade 4

Centro Universitário Senac-RS  
ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet  
Unidade Curricular: Qualidade de Software | Prof.: Luciano Zanuz  
PBL 4 - Testes Funcionais vs Estruturais  
Plataforma Local Eats

## 1. Escolha da Funcionalidade

Funcionalidade selecionada: **Busca de restaurantes**.

### O que a funcionalidade faz
Permite que o usuário pesquise restaurantes por termo, categoria, localização e faixa de preço, retornando uma lista ordenada de resultados.

### O que o usuário espera
- Encontrar restaurantes realmente relacionados ao que foi pesquisado.
- Receber resultados consistentes entre web e mobile.
- Obter resposta rápida, com ordenação compreensível e sem resultados "fora de contexto".

## 2. Testes Caixa-Preta (Visão do Usuário)

Sem considerar o código interno, os testes são definidos a partir das entradas e saídas observáveis da busca.

### Entradas possíveis
- Termo válido: "pizza", "hambúrguer", "vegano".
- Termo inexistente: "restaurante_xyz_inexistente".
- Combinações de filtros: preço, bairro/cidade e tipo de culinária.
- Busca sem filtros (somente termo) e busca com múltiplos filtros simultâneos.

### Comportamentos esperados
- Exibir somente restaurantes compatíveis com o termo e filtros aplicados.
- Mostrar mensagem clara quando não houver resultados.
- Manter o mesmo comportamento funcional em web e mobile.
- Preservar os filtros após atualização de página ou navegação de retorno.

### Situações de erro relevantes
- Retornar restaurantes de categorias sem relação com o termo pesquisado.
- Exibir resultados inconsistentes entre dispositivos para a mesma busca.
- Não apresentar feedback ao usuário em lentidão/timeout.
- Quebrar paginação ou ordenação ao combinar filtros.

## 3. Testes Caixa-Branca (Visão do Sistema)

Considerando acesso ao código, a análise foca em regras internas e fluxos lógicos da funcionalidade.

### Possível implementação interna
- Validação de entrada (normalização de texto, remoção de espaços extras, case-insensitive).
- Montagem dinâmica da query de busca no backend.
- Regras de relevância e ordenação por pontuação.
- Tratamento de timeout, fallback e cache.

### Estruturas e decisões que devem ser exercitadas
- Condições de filtros opcionais (quando aplicar ou ignorar cada filtro).
- Regras de prioridade de ordenação (relevância vs distância vs avaliação).
- Fluxos de erro para API indisponível, resposta vazia e resposta parcial.
- Conversão correta de parâmetros entre frontend e backend (tipos, campos e nomes).

### Situações críticas no código
- If/else com combinação de filtros pode gerar SQL/consulta incorreta.
- Falha na normalização pode excluir resultados válidos.
- Erros de serialização podem causar divergência entre web e mobile.
- Tratamento incompleto de exceções pode deixar a interface sem mensagem ao usuário.

## 4. Comparação entre as Abordagens

### Principal diferença
Caixa-preta valida o comportamento externo esperado pelo usuário; caixa-branca valida a lógica interna que produz esse comportamento.

### Tipo de problema que cada abordagem encontra melhor
- Caixa-preta: falhas funcionais percebidas pelo usuário (resultado incorreto, mensagem inadequada, fluxo quebrado).
- Caixa-branca: falhas de implementação (ramificações não cobertas, regras internas inconsistentes, tratamento de exceção incompleto).

## 5. Reflexão no Contexto do LocalEats

Para os problemas atuais (buscas incorretas, comportamentos inesperados e inconsistências), a combinação das duas abordagens é a mais efetiva.

- Caixa-preta é essencial para validar a experiência real e reproduzir reclamações dos usuários.
- Caixa-branca é essencial para identificar a causa raiz dos defeitos e evitar recorrência.

Conclusão: apenas uma abordagem não é suficiente. A startup precisa usar caixa-preta para garantir valor ao usuário e caixa-branca para estabilizar tecnicamente a busca no médio prazo.
