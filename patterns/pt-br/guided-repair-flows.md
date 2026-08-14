---
title: "Fluxos guiados de reparo"
slug: "guided-repair-flows"
number: "9.2"
category: "Falha e reparo"
definition: "Um caminho estruturado do erro do agente ao resultado corrigido, com o agente fazendo o trabalho pesado."
lang: "pt-BR"
---

# Fluxos guiados de reparo

> Um caminho estruturado do erro do agente ao resultado corrigido, com o agente fazendo o trabalho pesado.

## Visão geral

"Está errado" deveria começar um reparo, não um chamado de atendimento. O reparo guiado conduz a pessoa pelo diagnóstico, o que está errado, onde e de que tipo, depois propõe correções específicas, aplica a escolhida e confere o resultado.

## Por que funciona

O esforço de reparo decide se os erros são buracos na rua ou penhascos. Um ciclo de correção barato e confiável torna agentes imperfeitos perfeitamente usáveis.

## Quando usar

- Saídas estruturadas em que os erros são localizados e têm tipo
- Modos de falha recorrentes que valem virar produto
- Pessoas que reconhecem o errado mas não sabem especificar o certo

## Quando evitar

- Revisão criativa livre, em que a conversa serve melhor que um assistente passo a passo

## Exemplos em produtos reais

- Os ciclos de "corrigir com IA" em código e testes que falham
- Os fluxos de correção nas filas de revisão de extração de documentos
- Os assistentes de resolução de conflito de merge como referência

## Padrões relacionados

- [9.1 Estados de falha segura](safe-failure-states.md)
- [2.6 Controles de avaliação e retorno](feedback-and-rating-controls.md)
- [4.2 Edição da solicitação](edit-request.md)

## Para ler depois

- People + AI Guidebook (Google PAIR (Errors + Graceful Failure)
- Guidelines for Human-AI Interaction) Amershi et al., CHI 2019

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
