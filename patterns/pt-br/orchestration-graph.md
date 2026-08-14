---
title: "Grafo de orquestração"
slug: "orchestration-graph"
number: "7.1"
category: "Sistemas com vários agentes"
definition: "Um mapa visual dos agentes envolvidos numa tarefa e de como o trabalho flui entre eles."
lang: "pt-BR"
---

# Grafo de orquestração

> Um mapa visual dos agentes envolvidos numa tarefa e de como o trabalho flui entre eles.

## Visão geral

Quando um pedido se abre em muitos agentes, a pessoa perde o fio da meada. O grafo de orquestração mostra o elenco e a coreografia: qual agente faz o quê, o que depende de quê e em que pé está cada coisa.

## Por que funciona

Uma estrutura legível é a diferença entre um sistema e um jogo de adivinhação. A pessoa só supervisiona de verdade o trabalho de vários agentes quando enxerga o formato dele.

## Quando usar

- Fluxos que passam por três ou mais agentes
- Depuração de falhas entre vários agentes
- Explicar o comportamento do sistema para as partes interessadas

## Quando evitar

- Produtos de um agente só, em que o grafo é enfeite

## Exemplos em produtos reais

- Os canvas de fluxo no n8n e no Zapier
- Os visualizadores de grafo de agentes em frameworks de orquestração
- As visões de DAG de pipeline em ferramentas de dados

## Padrões relacionados

- [7.3 Agente supervisor](supervisor-agent.md)
- [7.5 Quadros de atribuição e filas de trabalho](assignment-boards-and-work-queues.md)
- [5.5 Visão de progresso da execução](execution-progress-view.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
