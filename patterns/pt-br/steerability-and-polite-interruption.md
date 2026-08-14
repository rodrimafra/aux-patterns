---
title: "Direcionamento e interrupção cortês"
slug: "steerability-and-polite-interruption"
number: "3.4"
category: "Controle e direção"
definition: "Usuários podem redirecionar um agente em execução sem cancelar e recomeçar."
lang: "pt-BR"
---

# Direcionamento e interrupção cortês

> Usuários podem redirecionar um agente em execução sem cancelar e recomeçar.

## Visão geral

Delegar é uma conversa, não a assinatura de um contrato. Esse padrão deixa a pessoa intervir (refinar o objetivo, corrigir o rumo, acrescentar restrições) enquanto o agente incorpora a mudança com naturalidade e segue em frente.

## Por que funciona

Corrigir o rumo é mais barato que recomeçar. Sistemas que punem a interrupção com trabalho perdido ensinam a pessoa a delegar de menos.

## Quando usar

- Tarefas longas de geração ou pesquisa
- Trabalho criativo iterativo em que os objetivos se afinam no meio do caminho
- Interfaces de voz, em que interromper é natural

## Quando evitar

- Transações atômicas que realmente não absorvem mudança no meio do caminho

## Exemplos em produtos reais

- O direcionamento por mensagens de acompanhamento no Cursor e no Claude Code enquanto os agentes trabalham
- Interromper um assistente de voz no meio da resposta
- Editar um pedido em andamento nas interfaces de chat modernas

## Padrões relacionados

- [3.1 Botão de parada, pausar e retomar](kill-switch-pause-and-resume.md)
- [4.2 Edição da solicitação](edit-request.md)
- [5.5 Visão de progresso da execução](execution-progress-view.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
