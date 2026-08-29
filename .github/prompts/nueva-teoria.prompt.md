---
mode: agent
description: Genera un archivo de teoría de una semana del bootcamp DaVinci Resolve 21.
---

# Nueva teoría

Genera `bootcamp/week-{{NN}}-{{SLUG}}/1-teoria/{{MM}}-{{TEMA}}.md`.

Lee antes [`.github/copilot-instructions.md`](../copilot-instructions.md).

## Estructura obligatoria

```markdown
# Título del tema

> Una línea que diga por qué esto importa. No un resumen.

## 🎯 Objetivos

## 1. Qué problema resuelve

## 2. Cómo funciona

## 3. Cómo se hace en Resolve 21

## 4. Antipatrones

## 5. Trucos

## 📚 Recursos Adicionales

## ✅ Checklist de Verificación
```

Las secciones numeradas pueden ser más de cinco y llevar `###` dentro. Las de emoji son
fijas y van siempre, en ese orden.

## Extensión

**200-300 líneas.** Objetivo ~250.

Si te pasas de 300, el archivo mezcla dos temas: **divídelo en dos archivos**, no lo
recortes. Un archivo = un concepto. Si el título necesita una "y", sospecha.

## Reglas de escritura

- **Español** para la prosa, **inglés** para todo lo que aparezca en la interfaz de
  Resolve. Primera mención de cada término de UI con su traducción entre paréntesis.
- **Cero absoluto.** Cada término técnico se define la primera vez que aparece. No
  asumas vocabulario de fotografía, cine, audio ni informática.
- **Segunda persona informal**, frases cortas, sin relleno.
- **El porqué antes del cómo**, siempre.
- **Rutas de menú completas**: `Color > Nodes > Add Serial`, con el atajo entre
  backticks y las dos plataformas cuando lo tenga.
- **Unidades explícitas**: `-14 LUFS`, `23.976 fps`, `1/50 s`, `10 bits`, `4:2:2`.
- **Sin ASCII art.** Los diagramas son SVG en `../0-assets/`, referenciados como
  `![Descripción accesible](../0-assets/NN-nombre.svg)`.
- **Sin capturas de pantalla.**

## Bloques que se usan

- Tablas para comparativas y para "antipatrón → por qué duele → qué hacer".
- Callouts GFM: `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`.
- El bloque de Studio, cuando toque:

```markdown
> [!IMPORTANT]
> **Studio** · `Nombre exacto de la función`.
> En Free, la ruta equivalente es *(alternativa concreta)*; el resultado es
> *(en qué se nota)*, y es suficiente para los entregables de esta semana.
```

## Antipatrones y trucos

La sección `## 4. Antipatrones` no es opcional y no es relleno. Cada antipatrón dice
**qué hace la gente**, **por qué duele** y **qué hacer en su lugar**. Salen de errores
reales, no de "no hacer las cosas mal".

La sección `## 5. Trucos` solo admite lo que ahorra tiempo real o revela algo que la
interfaz esconde. Lo que entre aquí se replica en el README de la semana y en
`docs/trucos-resolve.md`.

## Recursos adicionales

Entre dos y cuatro entradas, **cada una con una línea de por qué vale la pena**. Nunca
un enlace desnudo. El manual oficial de Blackmagic primero cuando exista.

## Checklist de verificación

Entre cinco y ocho ítems `- [ ]`, verificables por el estudiante sin ayuda. Comprueban
comprensión y capacidad de encontrar las cosas en la interfaz, no memoria.

## Verificación antes de entregar

- [ ] Entre 200 y 300 líneas
- [ ] Cada término técnico nuevo definido donde aparece
- [ ] Todas las rutas de menú comprobadas contra Resolve 21, no deducidas
- [ ] Los SVG que referencio existen en `../0-assets/`
- [ ] No he inventado ningún nombre de menú, efecto ni ajuste
