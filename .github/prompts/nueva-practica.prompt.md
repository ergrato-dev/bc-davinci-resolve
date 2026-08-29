---
mode: agent
description: Genera una práctica guiada de una semana del bootcamp DaVinci Resolve 21.
---

# Nueva práctica

Genera `bootcamp/week-{{NN}}-{{SLUG}}/2-practicas/{{MM}}-{{TEMA}}.md`.

Lee antes [`.github/copilot-instructions.md`](../copilot-instructions.md).

## Qué es una práctica aquí

Una **operación dentro de DaVinci Resolve**, guiada paso a paso, cuyo resultado es un
estado real de un proyecto de Resolve. No es un ejercicio de código, y no es un
proyecto: es un ejercicio acotado que se hace, se comprueba y se puede tirar.

Las prácticas usan el **pack de medios común**, no el material propio del estudiante.
Eso es lo que las hace comparables y verificables.

## Estructura obligatoria

```markdown
# Práctica {{MM}} — Título en imperativo

> Una línea con el resultado concreto que vas a tener al terminar.

**Duración estimada**: 45 min
**Prerrequisitos**: [Teoría 03](../1-teoria/03-tema.md), pack de medios en `01-basicos/`

## Contexto

El escenario. Por qué haces esto. Sin comandos todavía.

## Paso 1: Título del paso

**Por qué**: el problema que resuelve este paso concreto.

**Ruta**: `File > Project Settings > Master Settings > Timeline frame rate`

**Verifica**: qué tienes que ver en pantalla, o el comando del verificador.

## Paso 2: ...

## ✅ Resultado

- [ ] ...

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
```

## Reglas de los pasos

- **Todo paso termina en una forma de verificarlo.** Un comando del verificador, un
  valor concreto que se lee en un panel, o algo observable en la interfaz. Nunca
  "comprueba que está bien".
- **El porqué va antes del cómo**, en cada paso.
- **Ruta de menú completa y en inglés.** Si hay atajo, va entre backticks con las dos
  plataformas: `` `Alt+S` (Win) / `Opt+S` (Mac) ``.
- **Advertencia antes del paso irreversible, nunca después.** Casos típicos: cambiar el
  frame rate del proyecto, `Delete Render Cache`, media management destructivo, borrar
  una base de datos.

```markdown
> [!WARNING]
> El frame rate de la timeline no se puede cambiar una vez hay clips en el media pool.
> Si te equivocas aquí, la única salida es crear un proyecto nuevo. Confírmalo antes de
> importar nada.
```

- **Nombres con prefijo `BC-`** para todo lo que el verificador tenga que encontrar:
  `BC-Practica-01`, `BC-Montaje-v1`, bin `01-Basicos`.
- **Sin capturas de pantalla.** Si un paso no se puede describir con la ruta de menú y
  el nombre del control, es que falta un diagrama SVG.

## Código en las prácticas

Solo en las semanas de scripting (31-34), y con el formato de **descomentar**:

```python
# ============================================
# PASO 2: crear el timeline vacío
# ============================================
# Descomenta las siguientes líneas:
# pool = project.GetMediaPool()
# timeline = pool.CreateEmptyTimeline("BC-Semana-33")
# print(timeline.GetName())
```

Nunca `# TODO:` — ese formato es del proyecto, no de las prácticas.

## Duración

Entre 30 y 60 minutos por práctica. Si se pasa, divídela. Las duraciones de todas las
prácticas más las de la teoría tienen que cuadrar con las 10 horas del README.

## Troubleshooting

`## 🧯 Si algo sale mal` es obligatorio: tabla Síntoma | Causa | Solución, con al menos
tres filas, sacadas de lo que falla de verdad en ese ejercicio.

## Verificación antes de entregar

- [ ] Cada paso tiene su **Por qué** y su **Verifica**
- [ ] Las rutas de menú están comprobadas contra Resolve 21
- [ ] Los pasos irreversibles llevan advertencia **antes**
- [ ] Los nombres que el verificador debe encontrar llevan prefijo `BC-`
- [ ] La tabla de troubleshooting tiene al menos tres filas reales
- [ ] La duración declarada cuadra con la del README de la semana
