---
title: "Edição da solicitação"
slug: "edit-request"
number: "4.2"
category: "Clarificação"
definition: "O agente mostra sua interpretação do pedido e deixa o usuário corrigi-la diretamente."
lang: "pt-BR"
---

# Edição da solicitação

> O agente mostra sua interpretação do pedido e deixa o usuário corrigi-la diretamente.

## Visão geral

Entre o que foi dito e o que foi entendido mora a maior parte das falhas de agente. Esse padrão externaliza a interpretação (um pedido reescrito, uma instrução expandida) como um artefato editável, antes ou depois da execução.

## Por que funciona

Corrigir um entendimento errado na camada da interpretação é cirúrgico; corrigi-lo no vai e volta da conversa é arqueologia.

## Quando usar

- Pedidos complexos com restrições embutidas
- Sistemas que reescrevem ou expandem os pedidos por dentro
- Tarefas recorrentes cujos pedidos merecem refinamento com o tempo

## Quando evitar

- Pedidos triviais, em que mostrar a interpretação é puro peso morto

## Exemplos em produtos reais

- Geradores de imagem que expõem os pedidos revisados por eles
- O “exibindo resultados para…” dos buscadores, com opção de sobrepor
- Especificações de tarefa editáveis no Copilot Workspace

## Padrões relacionados

- [4.1 Perguntas de clarificação estruturadas](structured-clarification-prompts.md)
- [4.3 Suposições confirmadas](confirmed-assumptions.md)
- [3.4 Direcionamento e interrupção cortês](steerability-and-polite-interruption.md)

## Para ler depois

- People + AI Guidebook (Google PAIR
- Guidelines for Human-AI Interaction) Amershi et al., CHI 2019

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
