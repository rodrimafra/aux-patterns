---
title: "Estados de falha segura"
slug: "safe-failure-states"
number: "9.1"
category: "Falha e reparo"
definition: "Quando o agente falha, falha sem estrago: trabalho preservado, sistemas intactos, caminho adiante claro."
lang: "pt-BR"
---

# Estados de falha segura

> Quando o agente falha, falha sem estrago: trabalho preservado, sistemas intactos, caminho adiante claro.

## Visão geral

Lidar com falha é arquitetura, não desculpa. Falha segura quer dizer trabalho parcial salvo, sistemas externos deixados consistentes, passos destrutivos preparados mas não efetivados, e a pessoa chegando em "foi isto que aconteceu e é isto que você pode fazer", nunca num beco sem saída.

## Por que funciona

O custo do pior dia do agente determina o quanto a pessoa arrisca nos dias comuns. Falha barata torna racional delegar com ousadia.

## Quando usar

- Todo agente que age (este padrão é um piso, não um recurso)
- Tarefas longas acumulando valor não salvo
- Ações preparadas contra sistemas externos

## Quando evitar

- Estados de falha tão suaves que as falhas reais passam despercebidas

## Exemplos em produtos reais

- A preservação de rascunho em caso de travamento nos editores maduros
- As reversões transacionais que deixam os sistemas consistentes
- Os agentes que param antes de passos destrutivos e reportam o estado

## Padrões relacionados

- [3.6 Reversão e histórico de versões](rollback-and-version-history.md)
- [3.1 Botão de parada, pausar e retomar](kill-switch-pause-and-resume.md)
- [9.2 Fluxos guiados de reparo](guided-repair-flows.md)

## Para ler depois

- People + AI Guidebook (Google PAIR (Errors + Graceful Failure)
- Guidelines for Human-AI Interaction) Amershi et al., CHI 2019

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
