---
mode: agent
description: Genera el esqueleto completo de una semana del bootcamp DaVinci Resolve 21.
---

# Nueva semana

Genera la estructura completa de la semana `{{NN}}` del bootcamp.

Antes de escribir nada, lee [`.github/copilot-instructions.md`](../copilot-instructions.md).
Es la fuente de verdad de la malla, las convenciones y las reglas de longitud.

## Entrada

- `{{NN}}` — número de semana con dos dígitos
- `{{SLUG}}` — slug en snake_case, tal y como aparece en la malla
- `{{TITULO}}` — título en español
- `{{FASE}}` — nombre de la fase a la que pertenece

Si alguno no se te da, sácalo de la tabla de la malla en `copilot-instructions.md`.
No inventes semanas nuevas ni cambies el temario declarado.

## Qué generar

```
bootcamp/week-{{NN}}-{{SLUG}}/
├── README.md
├── rubrica-evaluacion.md
├── checks.json
├── 0-assets/
├── 1-teoria/
├── 2-practicas/
├── 3-proyecto/README.md
├── 4-recursos/{ebooks-free,videografia,webgrafia}/README.md
└── 5-glosario/README.md
```

Genera **primero el `README.md`**, que es el índice del que cuelga todo lo demás, y
para en ese punto a que se revise. Luego, en tandas separadas: teoría, prácticas,
proyecto, recursos, glosario, rúbrica, `checks.json` y SVG.

## El README de la semana: las 10 secciones, en este orden

1. `# Semana {{NN}} — {{TITULO}}` seguido de un blockquote de **una línea** que
   enganche: por qué esta semana importa, no un resumen de lo que contiene.
2. `## 🎯 Objetivos de la Semana` — "Al finalizar esta semana serás capaz de:" y una
   lista de verbos de acción concretos. Nada de "entender" o "conocer": *configurar*,
   *aislar*, *medir*, *entregar*.
3. `## 📋 Prerrequisitos` — qué semanas anteriores hacen falta, qué material del pack,
   qué hardware si aplica.
4. `## 🗂️ Estructura de la Semana` — el árbol real de archivos, con comentarios en línea.
5. `## 📝 Contenidos` — subsecciones `### Teoría` (tabla Archivo | Tema | Duración) y
   `### Prácticas` (tabla Práctica | Qué haces | Duración). Las duraciones tienen que
   sumar con la sección 6.
6. `## ⏱️ Distribución del Tiempo (10 horas)` — tabla Actividad | Tiempo. **Suma
   exactamente 10 horas.**
7. `## 🎩 Trucos y atajos` — tabla Truco | Cómo. Mínimo cinco. Cada uno cumple el
   criterio de admisión y se replica en `docs/trucos-resolve.md`.
8. `## 📌 Entregables` — lista numerada con ✅. Cada entregable se corresponde con un
   check de `checks.json` o con un criterio de la rúbrica.
9. `## ✅ Verificación` — el comando `python scripts/verificar-semana.py {{NN}}`.
10. `## 🔗 Navegación` — tabla Anterior | Actual | Siguiente, y la línea final
    `← [Volver al inicio del bootcamp](../../README.md)`.

Si la semana toca funciones de pago, añade entre 6 y 7 una sección
`## 💠 Qué necesita Studio esta semana` con la tabla Función | Qué hace | Alternativa en Free.

## Reglas que no se negocian

- **10 horas exactas** en la distribución del tiempo.
- **Rutas de menú completas y en inglés**: `File > Project Settings > Master Settings`.
- **Cero absoluto**: cada término nuevo se define donde aparece.
- **No inventes** menús, efectos ni ajustes. Verifica contra Resolve 21 usando el
  servidor MCP `resolve`, o enlaza el manual oficial y dilo.
- La navegación anterior/siguiente tiene que apuntar a carpetas que existen.

## Al terminar

```bash
./scripts/verificar-enlaces.sh
```

Y di explícitamente qué parte has entregado y qué falta.
