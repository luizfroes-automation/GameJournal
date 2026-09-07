# Desafio: Backlog — Diário de Jogos

## Objetivo do Projeto

Criar um diário pessoal de jogos que permita ao usuário gerenciar sua própria coleção: cadastrar, consultar, atualizar, remover e organizar os jogos que já jogou, está jogando ou pretende jogar.

O foco do desafio é lógica de programação: estruturas condicionais, repetição, manipulação e formatação de dados. Não é permitido o uso de inteligência artificial para escrever código — apenas para tirar dúvidas pontuais.

---

## Requisitos Funcionais

### 1. Cadastro de jogos
- O usuário deve poder adicionar um novo jogo ao seu diário.
- Cada jogo deve ter, no mínimo: nome, plataforma, ano de lançamento, status (ex: jogando, zerado, abandonado, quero jogar) e uma avaliação (nota de 0 a 10, ou similar).
- O sistema não deve aceitar cadastro de jogo duplicado (mesmo nome).
- O sistema deve validar as entradas do usuário (ex: não aceitar texto onde deveria ser número, não aceitar campos vazios, não aceitar status fora da lista permitida).

### 2. Listagem de jogos
- O usuário deve poder ver todos os jogos cadastrados, formatados de forma legível e organizada.
- Se o diário estiver vazio, o sistema deve informar isso claramente em vez de mostrar uma lista em branco.
- A listagem deve indicar quantos jogos existem no total.

### 3. Busca e filtro
- O usuário deve poder buscar um jogo específico pelo nome.
- O usuário deve poder filtrar jogos por status (jogando, zerado, abandonado, quero jogar).
- O usuário deve poder filtrar jogos por plataforma.
- O usuário deve poder filtrar jogos por uma faixa de ano (ex: jogos entre 2010 e 2020).
- Buscas sem resultado devem informar isso ao usuário, sem gerar erro.

### 4. Atualização de jogos
- O usuário deve poder editar as informações de um jogo já cadastrado (ex: mudar o status de "jogando" para "zerado", ajustar a avaliação).
- O sistema deve confirmar que o jogo existe antes de permitir a edição.

### 5. Remoção de jogos
- O usuário deve poder remover um jogo do diário.
- O sistema deve pedir confirmação antes de remover.
- O sistema deve avisar se o jogo que se tentou remover não existe.

### 6. Estatísticas do diário
- O sistema deve mostrar, sob demanda: quantidade total de jogos, quantidade de jogos por status, quantidade de jogos por plataforma, e a média das avaliações.
- Deve indicar qual é o jogo mais bem avaliado e qual é o pior avaliado.

### 7. Persistência
- Os jogos cadastrados não podem se perder ao encerrar o programa — devem continuar disponíveis na próxima vez que o sistema for aberto.

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

## Estrutura de Dados Combinada

Cada jogo é representado como um dicionário, e o catálogo completo é uma lista desses dicionários. Nomenclatura dos campos definida em inglês:

| Campo | Tipo | Observações |
|---|---|---|
| `id` | int | Identificador numérico sequencial |
| `name` | str | Nome do jogo (não pode ser vazio; não pode haver duplicado) |
| `genre` | str | Gênero do jogo (campo adicional, não exigido pelo requisito 1) |
| `console` | str | Plataforma (não pode ser vazio) |
| `year` | int | Ano de lançamento (4 dígitos, a partir de 1900; não pode ser negativo) |
| `rate` | float | Avaliação, escala de 0 a 5 com 1 casa decimal (não pode ser negativo) |
| `status` | str | Um dos 4 valores fixos abaixo |

**Valores permitidos para `status`** (usados exatamente assim, sem variação, tanto na validação do cadastro quanto nos filtros de busca):
- `'Playing'`
- `'Completed'`
- `'Want to Play'`
- `'Abandoned'`

**Exemplo de item da lista:**
```python
{'id': 1, 'name': 'Final Fantasy', 'genre': 'Fantasy', 'console': 'Playstation 3', 'year': 2010, 'rate': 4.2, 'status': 'Playing'}
```

---

## Ordem de Desenvolvimento

- A dupla trabalha **primeiro em conjunto na camada de dados e regras de negócio** (cadastro, validação, busca, filtro, edição, remoção, estatísticas, persistência), dividindo essa etapa por funcionalidade entre os dois integrantes.
- Somente depois de essa camada estar completa e funcionando, a dupla avança **em conjunto para a camada de interação com o usuário** (menu, exibição formatada, mensagens, fluxo de navegação).
- No próximo projeto, os papéis de cada integrante dentro de cada etapa devem ser invertidos.

---

## Critérios de Conclusão

O projeto é considerado completo quando:
- Todos os requisitos funcionais listados acima estão implementados e funcionando.
- O sistema pode ser usado do início ao fim (cadastrar, ver, editar, remover, sair) sem erros não tratados.
- Ambos os integrantes conseguem explicar o funcionamento completo do sistema, incluindo a parte que não desenvolveram diretamente.

O projeto é considerado completo quando:

- Todos os requisitos funcionais listados acima estão implementados e funcionando.
- O sistema pode ser usado do início ao fim (cadastrar, ver, editar, remover, sair) sem erros não tratados.
- Ambos os integrantes conseguem explicar o funcionamento completo do sistema, incluindo a parte que não desenvolveram.
