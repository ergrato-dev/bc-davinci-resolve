---
mode: agent
description: Genera un diagrama SVG para 0-assets/ del bootcamp DaVinci Resolve 21.
---

# Diagrama SVG

Genera `bootcamp/week-{{NN}}-{{SLUG}}/0-assets/{{MM}}-{{TEMA}}.svg`.

## Cuándo hace falta un diagrama

Cuando la prosa no basta: un grafo de nodos, una cadena de señal, una anatomía de panel,
una comparativa de dos flujos, una línea de tiempo, un mapa de espacios de color.

**No** hagas un diagrama para decorar. Un SVG que no aporte información que el texto no
tiene es ruido, y encima hay que mantenerlo.

Un SVG no enlazado desde ningún `.md` es un error que reporta `verificar-enlaces.sh`.

## Paleta obligatoria

```
fondo             #101418      texto              #e8eef4
superficie        #191f26      texto secundario   #93a1b0
superficie alta   #232b34      acento (azul)      #4a9eff
borde             #2f3a45      ámbar (Studio)     #f5a524
éxito             #3fb950      error              #f85149
violeta (Fusion)  #a371f7
canales de color  R #ff5f56  ·  G #4ade80  ·  B #5b9cff
```

Sin degradados. Colores sólidos. Tema oscuro, siempre.

Los tres colores de canal se reservan para diagramas que hablen de RGB de verdad
(parade, curvas, separación de canales). No los uses como paleta decorativa.

## Plantilla

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 420" width="880" height="420" role="img"
     aria-label="Descripción larga y concreta de lo que muestra el diagrama, para lectores de pantalla">
  <title>Título corto del diagrama</title>
  <style>
    .bg    { fill: #101418; }
    .surf  { fill: #191f26; stroke: #2f3a45; stroke-width: 1; }
    .t     { font-family: Inter, Roboto, "Segoe UI", system-ui, sans-serif; }
    .h     { font-size: 15px; font-weight: 600; fill: #e8eef4; }
    .s     { font-size: 12px; fill: #93a1b0; }
    .edge  { stroke: #2f3a45; stroke-width: 2; fill: none; }
  </style>
  <rect class="bg" width="880" height="420"/>
  <!-- contenido -->
</svg>
```

## Reglas técnicas

- **`viewBox` siempre**, con `width` y `height` que coincidan (coordenadas 1:1).
- **Ancho objetivo 800-880 px.** Alto entre 260 y 500 según el contenido.
- **`role="img"`, `<title>` y `aria-label`.** El `aria-label` describe lo que se ve,
  no repite el título. Es lo único que oye quien usa lector de pantalla.
- **Tipografía sans-serif del sistema.** Nunca una fuente externa: el SVG tiene que
  renderizar igual en GitHub, donde no se cargan fuentes remotas.
- **Texto mínimo 12 px.** Por debajo no se lee en el markdown renderizado.
- **Sin JavaScript, sin imágenes embebidas, sin fuentes remotas.**
- **Clases CSS reutilizadas**, no estilos en línea repetidos. El SVG tiene que poder
  leerse y editarse a mano.
- **Flechas con `<marker>`** definido una vez y reutilizado.

## Nombres

`NN-tema-en-kebab-case.svg`, numerado por **orden de aparición** en la teoría de esa
semana. Sin acentos, sin mayúsculas.

Ejemplos del estilo que se busca:
`01-anatomia-del-frame.svg`, `02-intra-frente-a-long-gop.svg`,
`03-cadena-de-gestion-de-color.svg`, `04-grafo-de-nodos-serie-y-paralelo.svg`.

## Cómo se enlaza

Desde un archivo de `1-teoria/`, con ruta relativa y descripción accesible:

```markdown
![Descripción accesible del diagrama](../0-assets/{{MM}}-{{TEMA}}.svg)
```

## Verificación antes de entregar

- [ ] Solo colores de la paleta, sin degradados
- [ ] `viewBox`, `role="img"`, `<title>` y `aria-label` presentes
- [ ] Todo el texto en 12 px o más
- [ ] Sin JavaScript, sin fuentes ni imágenes externas
- [ ] Enlazado desde al menos un `.md`
- [ ] `./scripts/verificar-enlaces.sh` no lo reporta como huérfano
