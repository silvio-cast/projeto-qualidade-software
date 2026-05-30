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
