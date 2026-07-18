# Design System - Portfólio Ronaldo

Este design system define uma base visual minimalista, técnica e industrial para um portfólio profissional. A estrutura foi criada para ser simples de manter, independente de framework e fácil de migrar para React, Next.js ou outro stack.

## Estrutura

```text
design-system/
  tokens/
    tokens.css
    tokens.json
  components.css
  preview/
    index.html
```

## Principios

- Clareza antes de decoração.
- Contraste suficiente para leitura confortavel.
- Componentes consistentes, reutilizaveis e com estados previsiveis.
- Layouts responsivos com medidas estaveis.
- Estilo monocromático com foco técnico.
- Tipografia principal em Cascadia Code.

## Tokens

Os tokens ficam em `tokens/tokens.css` para uso direto em CSS e em `tokens/tokens.json` para documentacao, handoff ou integracao com ferramentas.

Categorias principais:

- Cores: preto, branco e escala de cinzas.
- Tipografia: familia, tamanhos, pesos e alturas de linha.
- Espacamento: escala de 4px.
- Raios: cantos discretos e industriais.
- Sombras: mínimas, usadas apenas para separação.

## Componentes incluidos

- Button
- Icon button
- Badge
- Card
- Field
- Section heading
- Project card
- Navbar

## Como visualizar

Abra este arquivo no navegador:

```text
design-system/preview/index.html
```

## Como usar

Importe os estilos nesta ordem:

```html
<link rel="stylesheet" href="./tokens/tokens.css">
<link rel="stylesheet" href="./components.css">
```

Ou, a partir da pasta `preview`:

```html
<link rel="stylesheet" href="../tokens/tokens.css">
<link rel="stylesheet" href="../components.css">
```

## Proximos passos recomendados

- Adaptar os tokens de cor para a identidade final do portfólio.
- Converter os componentes para o framework do projeto quando ele existir.
- Adicionar componentes especificos: hero, timeline, lista de skills, depoimentos e formulario de contato.
