---
title: "Identidade e contrato de papel do agente"
slug: "agent-identity-and-role-contract"
number: "1.1"
category: "Identidade e delegação"
definition: "Uma declaração clara e inspecionável do que o agente é, para que serve e até onde vai o mandato dele."
lang: "pt-BR"
---

# Identidade e contrato de papel do agente

> Uma declaração clara e inspecionável do que o agente é, para que serve e até onde vai o mandato dele.

## Visão geral

Antes de delegar qualquer coisa, a pessoa precisa saber para quem está delegando. Esse padrão dá a cada agente um contrato visível: seu propósito, o que ele sabe fazer, seus limites e o que ele nunca vai fazer. Esse contrato é uma promessa que a interface mantém.

## Por que funciona

A confiança começa na previsibilidade. Um mandato declarado permite calibrar as expectativas antes da primeira interação e dá base para reclamar quando o agente sai do combinado.

## Quando usar

- Apresentar um agente novo às pessoas pela primeira vez
- Produtos em que um agente, entre vários, precisa ser distinguível
- Domínios regulados em que o escopo precisa estar documentado

## Quando evitar

- Ferramentas reativas de propósito único, em que o escopo é óbvio por si só

## Exemplos em produtos reais

- Resumos das instruções de GPTs personalizados exibidos antes do primeiro uso
- Perfis de apps no Slack listando os escopos e as permissões concedidas
- A constituição declarada e as políticas de uso do Claude

## Padrões relacionados

- [1.2 Modos de delegação](delegation-modes.md)
- [3.5 Permissões com escopo e consentimento de ferramentas](scoped-permissions-and-tool-consent.md)
- [8.3 Controles de privacidade e uso de dados](privacy-and-data-usage-controls.md)

## Para ler depois

- Guidelines for Human-AI Interaction, Amershi et al., CHI 2019
- Microsoft HAX Toolkit

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
