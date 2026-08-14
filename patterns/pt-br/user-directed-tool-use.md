---
title: "Uso de ferramentas dirigido pelo usuário"
slug: "user-directed-tool-use"
number: "3.7"
category: "Controle e direção"
definition: "Usuários escolhem quais ferramentas, fontes e modos de saída o agente pode empregar numa tarefa."
lang: "pt-BR"
---

# Uso de ferramentas dirigido pelo usuário

> Usuários escolhem quais ferramentas, fontes e modos de saída o agente pode empregar numa tarefa.

## Visão geral

Às vezes a pessoa sabe melhor como o trabalho deve ser feito. Esse padrão expõe a caixa de ferramentas do agente (buscar na web ou não, usar este conjunto de dados, gerar uma tabela em vez de texto corrido) como controles explícitos, por tarefa.

## Por que funciona

Restringir o método é uma forma de direcionamento que evita classes inteiras de erro antes que aconteçam e ensina à pessoa quais são, de fato, as ferramentas do agente.

## Quando usar

- Tarefas de pesquisa em que a qualidade da fonte importa
- Saídas destinadas a formatos específicos mais adiante
- Pessoas com restrições rígidas (privacidade, custo, conformidade)

## Quando evitar

- Deixar a seleção manual de ferramentas como padrão para quem só quer o resultado

## Exemplos em produtos reais

- Os seletores de foco e de fontes do Perplexity
- Os interruptores de ferramentas (web, código, canvas) no ChatGPT
- Os seletores de modelo e de contexto em IDEs com agentes

## Padrões relacionados

- [3.5 Permissões com escopo e consentimento de ferramentas](scoped-permissions-and-tool-consent.md)
- [6.1 Ancoragem em fontes e fundamentação](source-anchoring-and-grounding.md)
- [8.4 Repositório de contexto e perfis de espaço de trabalho](context-repository-and-workspace-profiles.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
