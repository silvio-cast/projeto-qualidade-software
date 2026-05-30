Feature: Busca de restaurantes
  Como um usuário do LocalEats
  Quero buscar restaurantes pelo nome ou culinária
  Para encontrar rapidamente opções específicas

  Background:
    Given que o usuário está na página inicial autenticado

  Scenario: Campo de busca vazio mantém a listagem de restaurantes
    When o usuário realiza uma busca com o campo vazio
    Then restaurantes são exibidos na lista

  Scenario: Buscar por termo inexistente não retorna restaurantes
    When o usuário pesquisa por "xyzabcdef123"
    Then nenhum restaurante é exibido na lista
