---
title: "Permissões com escopo e consentimento de ferramentas"
slug: "scoped-permissions-and-tool-consent"
number: "3.5"
category: "Controle e direção"
definition: "Concessões granulares e revogáveis controlando quais ferramentas, dados e ações um agente pode usar."
lang: "pt-BR"
---

# Permissões com escopo e consentimento de ferramentas

> Concessões granulares e revogáveis controlando quais ferramentas, dados e ações um agente pode usar.

## Visão geral

Acesso de tudo ou nada é como a confiança morre. Esse padrão decompõe a capacidade do agente em escopos inspecionáveis (ler a agenda, enviar e-mail, gastar até certo valor) concedidos um a um, revogáveis na hora e visíveis num só lugar.

## Por que funciona

A granularidade deixa a pessoa dizer sim às partes úteis sem bancar as perigosas. Cada escopo concedido é uma decisão pensada, não uma rendição.

## Quando usar

- Agentes que se conectam a contas e APIs externas
- Capacidade financeira ou destrutiva
- Implantação em empresa com requisitos de conformidade

## Quando evitar

- Fragmentar os escopos de forma tão fina que o consentimento vira ruído

## Exemplos em produtos reais

- As telas de consentimento de escopo do OAuth
- As permissões por capacidade dos apps no iOS
- O modelo de permissão por ferramenta do Claude

## Padrões relacionados

- [1.1 Identidade e contrato de papel do agente](agent-identity-and-role-contract.md)
- [3.2 Portões com humano no circuito](human-in-the-loop-gates.md)
- [10.3 Níveis de acesso e permissão para agentes](access-and-permission-tiers-for-agents.md)

## Para ler depois

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
