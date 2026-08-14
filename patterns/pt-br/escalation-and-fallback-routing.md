---
title: "Escalonamento e roteamento de contingência"
slug: "escalation-and-fallback-routing"
number: "7.6"
category: "Sistemas com vários agentes"
definition: "Transferência automática e graciosa para um humano ou um sistema mais forte quando o agente atinge seus limites."
lang: "pt-BR"
---

# Escalonamento e roteamento de contingência

> Transferência automática e graciosa para um humano ou um sistema mais forte quando o agente atinge seus limites.

## Visão geral

A falha é inevitável; o beco sem saída é uma escolha. Este padrão define as saídas, para um humano, para um modelo mais capaz ou para um padrão mais seguro, acionadas quando a certeza despenca, quando a falha se repete ou quando a pessoa se frustra.

## Por que funciona

A rede de proteção determina o quanto a pessoa vai confiar na corda bamba. Um escalonamento conhecido e suave deixa a pessoa à vontade para começar pelo agente.

## Quando usar

- Agentes voltados ao cliente com retaguarda humana
- Arquiteturas de modelos em camadas equilibrando custo e capacidade
- Detecção de frustração da pessoa ou de ciclos repetidos de falha

## Quando evitar

- Escalonamento que descarta o contexto em silêncio e recomeça a conversa

## Exemplos em produtos reais

- O escalonamento de bot para atendente no Intercom e no Zendesk
- As cadeias de contingência entre modelos em caso de recusa ou baixa certeza
- Os recursos de "falar com um humano" que funcionam de verdade

## Padrões relacionados

- [7.4 Briefings de transferência entre agentes](agent-handover-briefs.md)
- [9.2 Fluxos guiados de reparo](guided-repair-flows.md)
- [6.2 Termômetro de certeza](confidence-thermometer.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
