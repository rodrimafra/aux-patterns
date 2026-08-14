---
title: "Agente supervisor"
slug: "supervisor-agent"
number: "7.3"
category: "Sistemas com vários agentes"
definition: "Um agente coordenador que decompõe o trabalho, delega a especialistas e verifica a qualidade dos resultados."
lang: "pt-BR"
---

# Agente supervisor

> Um agente coordenador que decompõe o trabalho, delega a especialistas e verifica a qualidade dos resultados.

## Visão geral

Um ponto de contato, muitas mãos. O padrão do supervisor dá à pessoa uma única interface de conversa enquanto agentes especialistas trabalham por trás, com o supervisor cuidando da divisão do trabalho, da ordem das etapas e da junção dos resultados.

## Por que funciona

A pessoa ganha simplicidade sem abrir mão de capacidade. O supervisor também concentra a responsabilidade: um agente responde pelo todo, por mais que muitos tenham contribuído.

## Quando usar

- Tarefas complexas que abrangem competências distintas
- Produtos que escondem a complexidade de vários agentes atrás de uma persona
- Camadas de controle de qualidade sobre trabalho generativo

## Quando evitar

- Domínios simples, em que um supervisor é só burocracia

## Exemplos em produtos reais

- As arquiteturas de orquestrador e trabalhadores em frameworks de agentes
- A delegação a subagentes em ferramentas de código agênticas
- Os agentes gerentes em sistemas no estilo AutoGen

## Padrões relacionados

- [7.1 Grafo de orquestração](orchestration-graph.md)
- [7.4 Briefings de transferência entre agentes](agent-handover-briefs.md)
- [7.6 Escalonamento e roteamento de contingência](escalation-and-fallback-routing.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
