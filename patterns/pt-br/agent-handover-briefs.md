---
title: "Briefings de transferência entre agentes"
slug: "agent-handover-briefs"
number: "7.4"
category: "Sistemas com vários agentes"
definition: "Passagem estruturada de contexto quando o trabalho muda de agente, ou de agente para humano."
lang: "pt-BR"
---

# Briefings de transferência entre agentes

> Passagem estruturada de contexto quando o trabalho muda de agente, ou de agente para humano.

## Visão geral

Toda passagem perde contexto, a menos que a interface lute por ele. O resumo de passagem reúne objetivo, situação atual, decisões tomadas, questões em aberto e restrições, para que quem recebe, máquina ou humano, já comece por dentro.

## Por que funciona

A continuidade é o produto. A pessoa nunca deveria ter que explicar de novo a própria situação só porque o sistema trocou de trabalhador no meio da tarefa.

## Quando usar

- Escalonamento de agente para humano
- Tarefas longas que cruzam sessões ou agentes especializados
- Fluxos de atendimento com equipe mista de bot e humano

## Quando evitar

- Passagens triviais em que o resumo pesa mais que a tarefa

## Exemplos em produtos reais

- As passagens de bot para humano com resumo da conversa em plataformas de atendimento
- Os chamados de escalonamento preenchidos automaticamente com as etapas já tentadas
- Os resumos de sessão ao retomar tarefas longas de agente

## Padrões relacionados

- [7.3 Agente supervisor](supervisor-agent.md)
- [7.6 Escalonamento e roteamento de contingência](escalation-and-fallback-routing.md)
- [8.4 Repositório de contexto e perfis de espaço de trabalho](context-repository-and-workspace-profiles.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
