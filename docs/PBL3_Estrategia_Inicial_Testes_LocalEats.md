# Atividade 3

## Página 1

Centro Universitário Senac-RS
ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet
Unidade Curricular: Qualidade de Software | Prof.: Luciano Zanuz
PBL 3 – Estratégia Inicial de Testes
Plataforma Local Eats
Tarefa 1 – Funcionalidades Principais do Sistema
Com base no contexto da plataforma Local Eats, foram identificadas as seguintes funcionalidades principais,
selecionadas por seu impacto direto nos fluxos de uso e na experiência dos usuários:
ID
Funcionalidade
Descrição
F1
Busca de restaurantes
Permite filtrar estabelecimentos por culinária, localização e faixa de preço.
Fluxo de entrada principal da plataforma.
F2
Visualização de cardápio,
fotos e avaliações
Exibe as informações do restaurante para apoiar a decisão do usuário. Inclui
leitura de dados dinâmicos.
F3
Salvar restaurantes favoritos
Permite ao usuário marcar e recuperar locais de interesse. Envolve persistência
de dados por sessão/conta.
F4
Recomendações
personalizadas
Sugere restaurantes com base no perfil e histórico do usuário. Depende de
lógica de negócio e processamento de dados.
F5
Compartilhamento de
experiências / avaliações
Usuários publicam avaliações e fotos. Funcionalidade com dados gerados pelo
usuário e impacto na reputação dos restaurantes.
F6
Autenticação e gestão de
conta
Cadastro, login e gerenciamento de perfil. Base para personalização e
persistência de favoritos e avaliações.
Tarefa 2 – Níveis de Teste por Funcionalidade
Para cada funcionalidade, são indicados os quatro níveis de teste, descrevendo o que deve ser coberto em
cada camada e por quê:
F1 – Busca de restaurantes
Unitário
Integração
Sistema
Aceitação
Funções 
de 
filtragem 
e
ordenação: 
lógica 
de
aplicação de filtros por tipo
de culinária, localização e
faixa de preço de forma
isolada.
Integração entre o serviço
de 
busca, 
a 
API 
de
geolocalização e o banco de
dados de restaurantes.
Fluxo 
completo: 
usuário
aplica 
filtros 
→ 
sistema
retorna 
lista 
correta 
→
resultados exibidos na tela.
O 
usuário 
consegue
encontrar restaurantes pelo
tipo de culinária desejada,
próximos à sua localização
e dentro do orçamento.
F2 – Cardápio, fotos e avaliações

---

## Página 2

Unitário
Integração
Sistema
Aceitação
Funções de formatação e
carregamento dos dados do
restaurante; 
lógica 
de
cálculo 
de 
média 
das
avaliações.
Integração entre o serviço
de dados do restaurante,
CDN de imagens e banco
de avaliações.
Fluxo: 
usuário 
seleciona
restaurante 
→ 
página
carrega cardápio, fotos e
avaliações corretamente.
O 
usuário 
consegue
visualizar o menu completo,
as fotos e as avaliações de
outros clientes sem erros.
F3 – Salvar favoritos
Unitário
Integração
Sistema
Aceitação
Função 
de 
adição 
e
remoção de favoritos; lógica
de verificação de estado
(salvo / não salvo).
Integração entre a ação do
usuário, 
o 
serviço 
de
autenticação 
(usuário
logado?) e o banco de
favoritos.
Fluxo: usuário logado salva
restaurante 
→ 
favorito
persiste após atualização de
página e novo login.
O usuário consegue salvar
um 
restaurante 
como
favorito e encontrá-lo na sua
lista ao retornar ao app.
F4 – Recomendações personalizadas
Unitário
Integração
Sistema
Aceitação
Algoritmo 
ou 
regras 
de
negócio de recomendação:
retorna 
resultados
relevantes dado um perfil de
entrada simulado.
Integração entre o motor de
recomendação, o histórico
do usuário e o catálogo de
restaurantes.
Fluxo: usuário com histórico
acessa recomendações →
lista exibida é coerente com
seu perfil.
O usuário percebe que as
sugestões são relevantes
para 
seu 
gosto,
incentivando 
novos
acessos.
F5 – Compartilhar avaliações
Unitário
Integração
Sistema
Aceitação
Funções de validação do
conteúdo 
da 
avaliação
(texto, nota, foto); lógica de
salvamento.
Integração 
entre 
o
formulário de avaliação, o
serviço 
de 
upload 
de
imagens e o banco de
dados.
Fluxo: 
usuário 
escreve
avaliação 
→ 
salva 
→
avaliação 
aparece 
na
página do restaurante sem
desaparecer após refresh.
O 
usuário 
consegue
publicar uma avaliação com
nota e foto, e vê seu
conteúdo disponível para
outros usuários.
F6 – Autenticação e conta
Unitário
Integração
Sistema
Aceitação
Funções de validação de
e-mail/senha, geração de
token de sessão, regras de
senha.
Integração 
entre 
o
formulário 
de 
login, 
o
serviço 
de 
autenticação
(JWT/OAuth) e o banco de
usuários.
Fluxo completo de cadastro,
login, acesso a área logada
e 
logout; 
compatibilidade
web e mobile.
O usuário consegue criar
conta, fazer login, acessar
seus dados e sair da sessão
com segurança.
Tarefa 3 – Prioridades e Riscos
A priorização foi definida com base em dois critérios: (1) impacto no negócio em caso de falha e (2) evidências
de problemas já relatados no sistema atual. Funcionalidades com maior impacto financeiro, reputacional ou de
segurança recebem prioridade máxima.

---

## Página 3

Prioridade
Funcionalidade
Risco em caso de falha
Evidência no sistema
I Crítica
F1 – Busca de
restaurantes
Resultados incorretos impedem o usuário de
encontrar opções relevantes — abandono
imediato da plataforma.
Relatado: 
buscas 
retornam
resultados incorretos.
I Crítica
F6 – Autenticação
Falha no login impede acesso a favoritos e
avaliações; falha de segurança expõe dados
de usuários.
Base 
de 
todas 
as
funcionalidades
personalizadas.
I Alta
F5 – Avaliações
Perda de avaliações prejudica a reputação
dos restaurantes parceiros e destrói a
confiança dos usuários.
Relatado: 
avaliações
desaparecem 
após
atualização da página.
I Alta
F3 – Favoritos
Perda 
de 
favoritos 
gera 
frustração 
e
retrabalho; indica problemas de persistência
que podem afetar outras funcionalidades.
Inconsistência de dados entre
web e mobile.
I Média
F2 – Cardápio e
avaliações
Dados 
desatualizados 
ou 
ausentes
prejudicam a decisão do usuário; impacto na
conversão.
Inconsistências entre versões
web e mobile.
I Média
F4 – Recomendações
Sugestões 
irrelevantes 
reduzem 
o
engajamento, mas não bloqueiam o uso da
plataforma.
Nenhum relato direto — risco
latente.
I Critério de priorização: funcionalidades classificadas como Críticas devem ser testadas antes de qualquer
deploy. Funcionalidades de Alta prioridade entram no ciclo de testes a cada sprint. Funcionalidades de Média
prioridade são cobertas com menor frequência, mas monitoradas em produção.
Tarefa 4 – Pirâmide de Testes
A pirâmide de testes orienta a distribuição dos esforços de teste em três camadas, equilibrando custo,
velocidade de execução e cobertura. Para a Local Eats, a estratégia é a seguinte:
Camada
Volume
sugerido
O que cobrir
Justificativa
Testes Unitários
(base da pirâmide)
~70% dos
testes
Lógica de filtragem da busca;
cálculo de média de avaliações;
validação de formulários (login,
avaliação); 
regras 
de
recomendação; 
funções 
de
formatação de dados.
São rápidos, baratos e fornecem feedback
imediato ao desenvolvedor. Cobrem a
maior parte das regras de negócio de forma
isolada e detectam regressões antes
mesmo do build. Para a Local Eats, onde
buscas retornam resultados incorretos,
testes unitários na camada de filtragem são
essenciais.
Testes de
Integração (meio da
pirâmide)
~20% dos
testes
Integração busca ↔ banco de
dados; autenticação ↔ serviço de
sessão; avaliação ↔ upload de
imagens; favoritos ↔ banco por
usuário; 
consistência 
web 
↔
mobile nas APIs.
Cobrem as conexões entre componentes,
onde erros de contrato (tipos, campos
ausentes, timeouts) costumam surgir. Para
a Local Eats, as inconsistências entre web
e 
mobile 
e 
o 
desaparecimento 
de
avaliações apontam falhas de integração —
esse é um ponto crítico de investimento.

---

## Página 4

Camada
Volume
sugerido
O que cobrir
Justificativa
Testes de Sistema /
E2E (topo da
pirâmide)
~10% dos
testes
Fluxo: 
buscar 
→ 
selecionar
restaurante → ver cardápio →
salvar favorito; fluxo de cadastro e
login; publicar avaliação e verificar
persistência; compatibilidade em
diferentes dispositivos.
São lentos, caros e frágeis. Devem cobrir
apenas os fluxos críticos de ponta a ponta.
Para a Local Eats, o fluxo de busca e o de
publicação de avaliação são candidatos
prioritários por serem as jornadas mais
usadas e as que apresentam mais defeitos
relatados.
I Anti-padrão a evitar: pirâmide invertida (soroteiros de UI/E2E sem base unitária). Esse cenário gera suítes
lentas, difíceis de manter e com alta taxa de falsos positivos — problema comum em startups que crescem
rapidamente sem cultura de testes.
Tarefa 5 – Testes em Produção
Testes em produção não substituem os testes nos ambientes de desenvolvimento e homologação, mas são
complementares e, em alguns contextos, indispensáveis. Para a Local Eats, recomendamos o uso estratégico
das seguintes práticas:
Prática
Descrição
Aplicação na Local Eats
Recomendado?
Monitoramento de
erros (Error
Tracking)
Ferramentas 
como 
Sentry
capturam exceções e erros em
tempo real sem intervenção do
usuário.
Identificar exceções nas buscas e no
fluxo de avaliações — problemas já
relatados pelos usuários.
Sim — imediato
Health checks
contínuos
Requisições 
periódicas
automatizadas para verificar se
as APIs e serviços principais
estão respondendo.
Detectar lentidão em horários de pico
antes que o usuário perceba —
problema crítico documentado.
Sim — imediato
Feature flags
(lançamento
gradual)
Ativar 
novas 
funcionalidades
para uma parcela controlada
dos 
usuários 
antes 
do
lançamento completo.
Reduzir 
o 
risco 
de 
bugs 
em
funcionalidades novas chegarem a
todos os usuários de uma vez.
Sim — médio prazo
Synthetic
monitoring (testes
sintéticos)
Scripts 
automatizados 
que
simulam jornadas do usuário
(ex.: buscar restaurante, ver
cardápio) em produção.
Validar 
continuamente 
os 
fluxos
críticos sem depender de relatos
espontâneos dos usuários.
Sim — médio prazo
Testes A/B
Comparar duas versões de uma
funcionalidade 
com 
grupos
distintos de usuários reais.
Avaliar melhorias de usabilidade na
interface de busca ou no fluxo de
avaliações com dados reais.
Sim — longo prazo
Testes de carga em
produção
Simular pico de acessos em
ambiente 
real 
para 
medir
degradação de desempenho.
Reproduzir a lentidão em horários de
pico documentada. Exige janela de
manutenção e monitoramento.
Com cautela —
apenas com
controle
I Atenção: testes invasivos em produção (carga, injeção de falhas) exigem autorização, janela de manutenção e
plano de rollback. Para a fase atual da Local Eats, priorizar monitoramento passivo (error tracking, health checks)
antes de técnicas mais avançadas.
Em síntese, a Local Eats deve adotar testes em produção de forma progressiva: começar com monitoramento
de erros e health checks (baixo risco, alto retorno), evoluir para feature flags e testes sintéticos à medida que
os processos internos amadurecem, e considerar testes de carga e A/B apenas quando houver infraestrutura e

---

## Página 5

cultura de qualidade consolidadas.
PBL 3 – Estratégia Inicial de Testes | Plataforma Local Eats | Qualidade de Software – Senac-RS