---
title: "Portões com humano no circuito"
slug: "human-in-the-loop-gates"
number: "3.2"
category: "Controle e direção"
definition: "Pontos em que o agente pausa e pede aprovação explícita antes de seguir, por consequência, não por hábito."
featured: true
lang: "pt-BR"
---

# Portões com humano no circuito

> Pontos em que o agente pausa e pede aprovação explícita antes de seguir, por consequência, não por hábito.

## Visão geral

Nem toda ação precisa de aprovação; aprovar tudo é só um produto manual mais lento. Os portões com humano no circuito são pontos de verificação deliberados, colocados onde a consequência e a irreversibilidade são altas: enviar o e-mail, mover o dinheiro, apagar os dados. Abaixo da linha do portão, o agente age livremente. Acima dela, quem decide é uma pessoa. O portão em si precisa ser informativo: um resumo antes da ação cobrindo o que o agente quer fazer, por quê, com base em qual evidência e o que vem depois, nunca um Confirmar/Cancelar seco que treina o clique cego.

## Por que funciona

Os portões convertem a autonomia de um salto de fé em uma passagem supervisionada. Bem colocados, concentram a atenção humana exatamente onde ela é insubstituível; colocados com preguiça, geram fadiga de aprovação que derruba o próprio propósito.

## Quando usar

- Ações irreversíveis ou custosas (pagamentos, envios, exclusões, contratos)
- A primeira ocorrência de uma nova classe de ação, antes de a confiança se firmar
- Fluxos regulados que exigem consentimento documentado

## Quando evitar

- Ações rotineiras e reversíveis; a fadiga de portão ensina a pessoa a parar de ler
- Como escudo de responsabilidade, sem conteúdo real de decisão

## Exemplos em produtos reais

- Os pedidos de permissão do Claude Code antes de rodar comandos ou editar arquivos
- As etapas de aprovação de deploy no GitHub Actions e em pipelines de release
- A confirmação de pagamento com etapa extra por biometria em apps de banco
- A aprovação do plano do Devin antes da execução autônoma

## Para levar

- Coloque os portões por consequência e reversibilidade, não de forma uniforme
- Faça de cada portão um resumo: o quê, por quê, com qual evidência e o que vem depois
- Escalone as aprovações: portão nas ações inéditas, fluxo livre nas rotinas comprovadas
- Meça a fadiga de portão: aprovar sem ler é falha de design

## Padrões relacionados

- [3.3 Planejar antes de executar](plan-then-execute-workflow.md)
- [1.2 Modos de delegação](delegation-modes.md)
- [5.1 Vislumbre do raciocínio](reasoning-glimpse.md)

## Para ler depois

- Building Effective Agents) Anthropic
- Human-Centered AI, Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
