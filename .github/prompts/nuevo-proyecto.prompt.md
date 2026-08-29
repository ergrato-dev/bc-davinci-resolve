---
mode: agent
description: Genera el README del proyecto semanal (capa del hilo conductor) del bootcamp DaVinci Resolve 21.
---

# Nuevo proyecto semanal

Genera `bootcamp/week-{{NN}}-{{SLUG}}/3-proyecto/README.md`.

Lee antes [`.github/copilot-instructions.md`](../copilot-instructions.md) y
[`docs/proyecto-hilo-conductor.md`](../../docs/proyecto-hilo-conductor.md).

## Qué es el proyecto semanal

**Una capa nueva sobre la misma pieza que el estudiante construye durante 36 semanas.**
Nunca un proyecto desechable. La práctica se hace con el pack común y se tira; el
proyecto se hace con el material propio del estudiante y se queda.

Diferencia clave con las prácticas:

| | Prácticas | Proyecto |
| --- | --- | --- |
| Material | Pack común | El propio del estudiante |
| Guía | Paso a paso | Requisitos, no instrucciones |
| Vida | Se tira | Se acumula 36 semanas |
| Corrección | Verificable al detalle | Verificable en estructura, evaluable en calidad |

## Estructura obligatoria

```markdown
# Proyecto — Semana {{NN}}: qué capa añades

> Una línea: qué tendrá tu pieza al terminar esta semana que no tenía antes.

## 📦 Qué añade esta semana

Qué capa es y por qué va aquí y no antes ni después.

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Numerados, con el nombre exacto que el
verificador espera.

## 🎨 Criterios de calidad

Lo que la API no puede ver, escrito como algo observable.

## 💡 Adaptación a tu pieza

Cómo se concreta esto en documental, videoclip, ficción, tutorial y viaje.

## 🚦 Cómo entregarlo

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |

## 🔗 Navegación
```

## Reglas

- **Requisitos, no pasos.** El proyecto no se guía paso a paso: eso ya lo hicieron las
  prácticas. Aquí se dice qué tiene que existir y con qué nombre.
- **Los nombres son literales y llevan prefijo `BC-`**: `BC-Bootcamp-Resolve`,
  `BC-Montaje-v1`, `BC-Color-v1`, `BC-Master`. Tienen que coincidir **exactamente** con
  lo que comprueba `checks.json`.
- **Los criterios de calidad son observables.** Nunca "que quede bien". Sí:
  - "Los negros de todos los planos tocan el 0 del waveform sin recortar por debajo"
  - "El diálogo promedia entre -12 y -18 dBFS y ningún pico pasa de -6 dBFS"
  - "El borde del key no muestra halo verde al 200 % de zoom"
- **La adaptación por formato no es opcional.** El estudiante eligió entre cinco
  formatos en la Semana 01; el proyecto tiene que servir para los cinco. Da un ejemplo
  breve de cada uno, no un párrafo.
- **Versionado**: recuerda duplicar la timeline antes de empezar una fase nueva
  (`clic derecho en el media pool > Duplicate Timeline`) y exportar el proyecto a
  `04-respaldos/` con `File > Export Project` al cerrar una fase.

## Errores comunes

Tabla obligatoria con al menos tres filas, sacadas de lo que falla de verdad al aplicar
esa capa sobre material propio (que casi nunca se parece al del pack).

## Verificación antes de entregar

- [ ] Los nombres literales coinciden con `checks.json`, carácter a carácter
- [ ] Cada criterio de calidad es observable y medible
- [ ] Hay adaptación para los cinco formatos de pieza
- [ ] La tabla de errores comunes tiene al menos tres filas reales
- [ ] La capa encaja con la fase: no pide algo que se enseña dos semanas después
