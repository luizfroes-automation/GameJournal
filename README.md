# Desafio: Catálogo Pessoal

## Objetivo do Projeto

Criar um sistema de catálogo pessoal (de livros, filmes, jogos ou similar — escolham o tema) que permita ao usuário gerenciar sua coleção: cadastrar, consultar, atualizar, remover e organizar itens.

O foco do desafio é lógica de programação: estruturas condicionais, repetição, manipulação e formatação de dados. Não é permitido o uso de inteligência artificial para escrever código — apenas para tirar dúvidas pontuais.

---

## Requisitos Funcionais

### 1. Cadastro de itens

- O usuário deve poder adicionar um novo item ao catálogo.
- Cada item deve ter, no mínimo: nome/título, categoria, ano, e uma avaliação (nota de 0 a 10, ou similar).
- O sistema não deve aceitar cadastro de item duplicado (mesmo nome).
- O sistema deve validar as entradas do usuário (ex: não aceitar texto onde deveria ser número, não aceitar campos vazios).

### 2. Listagem de itens

- O usuário deve poder ver todos os itens cadastrados, formatados de forma legível e organizada.
- Se o catálogo estiver vazio, o sistema deve informar isso claramente em vez de mostrar uma lista em branco.
- A listagem deve indicar quantos itens existem no total.

### 3. Busca e filtro

- O usuário deve poder buscar um item específico pelo nome.
- O usuário deve poder filtrar itens por categoria.
- O usuário deve poder filtrar itens por uma faixa de ano (ex: itens entre 2010 e 2020).
- Buscas sem resultado devem informar isso ao usuário, sem gerar erro.

### 4. Atualização de itens

- O usuário deve poder editar as informações de um item já cadastrado (ex: corrigir o ano, mudar a avaliação).
- O sistema deve confirmar que o item existe antes de permitir a edição.

### 5. Remoção de itens

- O usuário deve poder remover um item do catálogo.
- O sistema deve pedir confirmação antes de remover.
- O sistema deve avisar se o item que se tentou remover não existe.

### 6. Estatísticas do catálogo

- O sistema deve mostrar, sob demanda: quantidade total de itens, quantidade de itens por categoria, e a média das avaliações.
- Deve indicar qual é o item mais bem avaliado e qual é o pior avaliado.

### 7. Persistência

- Os dados cadastrados não podem se perder ao encerrar o programa — devem continuar disponíveis na próxima vez que o sistema for aberto.

### 8. Menu de navegação

- O sistema deve apresentar um menu claro com todas as ações disponíveis (cadastrar, listar, buscar, editar, remover, ver estatísticas, sair).
- O usuário deve poder repetir ações quantas vezes quiser, sem precisar reiniciar o programa a cada operação.
- Deve haver uma opção clara de sair do programa.

---

## Requisitos Não Funcionais

- **Clareza**: todas as mensagens para o usuário (erros, confirmações, resultados) devem ser compreensíveis, sem termos técnicos ou mensagens de erro cruas.
- **Robustez**: o sistema não deve travar ou fechar inesperadamente diante de uma entrada inválida do usuário.
- **Organização do código**: o código deve ser dividido em partes com responsabilidades claras (ex: uma parte cuida dos dados, outra cuida da interação com o usuário), mesmo que ambos estejam no mesmo arquivo.
- **Legibilidade**: nomes de variáveis e funções devem ser claros o suficiente para que o outro integrante da dupla entenda o código sem precisar de explicação verbal.

---

## Critérios de Divisão de Trabalho

- Um integrante fica responsável pela camada de **dados e regras de negócio** (cadastro, validação, cálculos, persistência).
- O outro integrante fica responsável pela camada de **interação com o usuário** (menu, exibição formatada, mensagens, fluxo de navegação).
- As duas partes devem se comunicar por meio de funções bem definidas, para que a interface e a lógica possam ser desenvolvidas de forma relativamente independente.

---

## Critérios de Conclusão

O projeto é considerado completo quando:

- Todos os requisitos funcionais listados acima estão implementados e funcionando.
- O sistema pode ser usado do início ao fim (cadastrar, ver, editar, remover, sair) sem erros não tratados.
- Ambos os integrantes conseguem explicar o funcionamento completo do sistema, incluindo a parte que não desenvolveram.
