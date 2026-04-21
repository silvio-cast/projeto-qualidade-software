# Atividade 1

## Página 1

Centro Universitário Senac-RS
ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet
Unidade Curricular: Qualidade de Software | Prof.: Luciano Zanuz
PBL 1 – Diagnóstico de Qualidade de Software
Atributos da ISO/IEC 25010 – Plataforma Local Eats
Contexto do Sistema
A startup Local Eats desenvolveu uma plataforma digital — disponível em versão web e aplicativo mobile —
para conectar moradores e turistas a restaurantes independentes. O sistema permite busca por culinária,
localização e faixa de preço, visualização de cardápios, fotos e avaliações, salvamento de favoritos,
recomendações personalizadas e compartilhamento de experiências.
Devido ao prazo de um grande evento gastronômico, a primeira versão foi desenvolvida rapidamente e
colocada em produção. Após o lançamento, surgiram os seguintes relatos de problemas:
• O sistema fica lento em horários de pico
• Algumas telas são confusas e pouco intuitivas
• Certas buscas retornam resultados incorretos
• O aplicativo apresenta falhas em determinados modelos de smartphone
• Usuários encontram dificuldade para concluir ações simples
• Avaliações desaparecem após atualização da página
• Há inconsistências entre a versão web e a versão mobile
Objetivo da Análise
Realizar uma análise preliminar da qualidade do produto de software, identificando quais atributos da ISO/IEC
25010 (norma base da família ISO/IEC 25000 — SQuaRE) estão comprometidos, justificando tecnicamente
cada relação e avaliando o impacto para o usuário e para o negócio.
Análise: Problemas × Atributos de Qualidade (ISO/IEC 25010)
Para cada problema relatado, foi identificado o atributo de qualidade afetado e elaborada uma justificativa
técnica:
Problema
Identificado
Atributo de
Qualidade Afetado
Justificativa Técnica
Lentidão em
horários de pico
Eficiência de
Desempenho
(Performance
Efficiency)
O sistema apresenta tempo de resposta elevado sob alta carga
de usuários simultâneos, indicando ausência de escalabilidade
e otimização de recursos. Afeta a subcaracterística de
comportamento temporal da ISO/IEC 25010. Para o usuário:
frustração e abandono da plataforma. Para o negócio: perda de
clientes e danos à reputação nos momentos de maior
demanda.

---

## Página 2

Problema
Identificado
Atributo de
Qualidade Afetado
Justificativa Técnica
Telas confusas e
pouco intuitivas
Usabilidade
(Usability)
A dificuldade de compreensão e navegação compromete as
subcaracterísticas de inteligibilidade e apreensibilidade. O
usuário não consegue entender rapidamente como interagir
com a interface, aumentando o esforço cognitivo. Impacto
direto: baixa satisfação e abandono antes de concluir tarefas.
Buscas retornam
resultados
incorretos
Adequação
Funcional
(Functional
Suitability)
Quando a busca retorna dados incorretos, a função principal do
sistema falha em sua correção funcional — subcaracterística
da Adequação Funcional. O produto não executa corretamente
as tarefas para as quais foi projetado. Impacto: perda de
confiança e omissão ou exposição incorreta de restaurantes
parceiros.
Falhas em
determinados
modelos de
smartphone
Portabilidade
(Portability) +
Confiabilidade
(Reliability)
Falhas em dispositivos específicos apontam deficiências na
adaptabilidade 
(Portabilidade): 
o 
sistema 
não 
funciona
adequadamente em diferentes ambientes de hardware.
Também compromete a Confiabilidade, pois o app não mantém
comportamento esperado em todas as condições. Impacto:
exclusão de parte dos usuários e percepção de baixa
qualidade.
Dificuldade para
concluir ações
simples
Usabilidade
(Usability)
Compromete 
operacionalidade 
e 
apreensibilidade 
—
subcaracterísticas da Usabilidade. Indica que o design da
interface não segue boas práticas de UX, exigindo mais esforço
do que o necessário. Para o usuário: frustração e retrabalho.
Para o negócio: menor taxa de conversão e engajamento.
Avaliações
desaparecem após
atualização da
página
Confiabilidade
(Reliability)
Indica 
falha 
de 
recuperabilidade 
e 
maturidade 
—
subcaracterísticas da Confiabilidade. O sistema não garante a
persistência 
das 
informações 
inseridas, 
demonstrando
instabilidade no gerenciamento de estado e/ou persistência de
dados. Impacto: perda de informações e desconfiança do
usuário na plataforma.
Inconsistências
entre versão web e
mobile
Compatibilidade
(Compatibility) +
Adequação
Funcional
Diferenças de comportamento entre web e mobile indicam falta
de cointeroperabilidade (Compatibilidade) e inconsistência
funcional (Adequação Funcional). O sistema não garante
resultados equivalentes em diferentes canais. Para o negócio:
confusão, suporte adicional e perda de credibilidade.
Mapeamento Resumido dos Atributos Afetados
A tabela abaixo consolida quais características da ISO/IEC 25010 foram identificadas como comprometidas e
a quantidade de problemas relatados que as afetam:
Característica ISO/IEC
25010
Subcaracterísticas
Comprometidas
Problemas Relacionados
Severida
de
Adequação Funcional
Correção funcional
Buscas incorretas; inconsistências
web/mobile
Alta

---

## Página 3

Característica ISO/IEC
25010
Subcaracterísticas
Comprometidas
Problemas Relacionados
Severida
de
Eficiência de
Desempenho
Comportamento 
temporal;
utilização de recursos
Lentidão em horários de pico
Alta
Usabilidade
Inteligibilidade;
apreensibilidade;
operacionalidade
Telas 
confusas; 
dificuldade 
em
ações simples
Alta
Confiabilidade
Maturidade; recuperabilidade
Avaliações que desaparecem; falhas
em smartphones
Alta
Portabilidade
Adaptabilidade
Falhas em modelos específicos de
smartphone
Média
Compatibilidade
Cointeroperabilidade
Inconsistências entre versão web e
mobile
Média
Conclusão e Recomendações
A plataforma Local Eats apresenta comprometimentos em pelo menos seis das oito características principais
de qualidade da ISO/IEC 25010. Os problemas não são pontuais: refletem ausência de processos de
qualidade desde as fases iniciais do desenvolvimento.
Recomenda-se a seguinte ordem de priorização para as correções:
• 1º — Confiabilidade: corrigir a perda de avaliações e as falhas em smartphones. Dados que somem
comprometem diretamente a integridade do produto e a confiança dos usuários.
• 2º — Adequação Funcional: corrigir os resultados incorretos nas buscas. Uma busca que não funciona
inviabiliza o propósito central da plataforma.
• 3º — Eficiência de Desempenho: otimizar o sistema para suportar picos de acesso, especialmente em
eventos gastronômicos — o contexto de uso mais crítico para o negócio.
• 4º — Usabilidade: revisar os fluxos de interface para reduzir o esforço do usuário e aumentar a taxa de
conclusão de tarefas.
• 5º — Portabilidade e Compatibilidade: garantir funcionamento consistente entre dispositivos e entre as
versões web e mobile.
Conclusão geral: o sistema possui qualidade insuficiente para operar sem riscos ao negócio e à reputação da
associação de comerciantes. As correções devem ser tratadas como urgentes, com acompanhamento de métricas
de qualidade após cada intervenção.
PBL 1 – Atributos de Qualidade ISO/IEC 25010 | Plataforma Local Eats | Qualidade de Software – Senac-RS