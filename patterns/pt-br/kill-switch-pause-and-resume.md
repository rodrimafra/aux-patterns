---
title: "Botão de parada, pausar e retomar"
slug: "kill-switch-pause-and-resume"
number: "3.1"
category: "Controle e direção"
definition: "Um controle sempre disponível para interromper o agente na hora, sem perder o trabalho em andamento."
lang: "pt-BR"
---

# Botão de parada, pausar e retomar

> Um controle sempre disponível para interromper o agente na hora, sem perder o trabalho em andamento.

## Visão geral

O botão mais importante na UX de agentes é o de parar. Esse padrão garante que a interrupção seja imediata, sem perda e reversível: pausar preserva o estado, retomar continua, parar abandona sem bagunça.

## Por que funciona

Saber que dá para parar é o que torna seguro começar. A interrupção recuperável tira o custo do medo de delegar, então a pessoa concede mais autonomia no geral.

## Quando usar

- Toda execução autônoma que dure mais que um instante
- Ações cujo custo ou consequência cresce com o tempo
- Agentes operando em sistemas externos ao vivo

## Quando evitar

- Nunca omita esse controle; o antipadrão é a ausência dele

## Exemplos em produtos reais

- Os controles de parar geração em todos os grandes produtos de chat
- A pausa e o redirecionamento no meio da execução do Devin
- O cancelamento de pipelines de CI/CD como precedente

## Padrões relacionados

- [3.4 Direcionamento e interrupção cortês](steerability-and-polite-interruption.md)
- [3.6 Reversão e histórico de versões](rollback-and-version-history.md)
- [9.1 Estados de falha segura](safe-failure-states.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
