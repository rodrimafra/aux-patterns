---
title: "Reversão e histórico de versões"
slug: "rollback-and-version-history"
number: "3.6"
category: "Controle e direção"
definition: "Toda ação do agente é registrada e reversível; o estado pode ser restaurado a qualquer ponto anterior."
lang: "pt-BR"
---

# Reversão e histórico de versões

> Toda ação do agente é registrada e reversível; o estado pode ser restaurado a qualquer ponto anterior.

## Visão geral

O desfazer é a base do uso sem medo. Estendido aos agentes, é um histórico navegável do que mudou, quando e por quem (pessoa ou agente), com restauração em um passo.

## Por que funciona

A reversibilidade transforma risco em experimento. Quem sabe que pode voltar atrás delega mais cedo, concede mais e entra menos em pânico quando algo parece errado.

## Quando usar

- Agentes que modificam documentos, código ou configuração
- Operações em lote sobre muitos itens
- Qualquer lugar onde existiria um desfazer para uma pessoa fazendo o mesmo trabalho

## Quando evitar

- Ações externas genuinamente irreversíveis, que é exatamente onde entram os portões com humano no circuito

## Exemplos em produtos reais

- O Git como precedente profundo
- O histórico de versões do Figma e do Notion
- A restauração por ponto de verificação em ferramentas de código com agentes

## Padrões relacionados

- [3.1 Botão de parada, pausar e retomar](kill-switch-pause-and-resume.md)
- [9.1 Estados de falha segura](safe-failure-states.md)
- [5.4 Linha do tempo de atividades e log de auditoria](activity-timeline-and-audit-log.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
