---
mode: agent
description: Genera el checks.json de una semana del bootcamp DaVinci Resolve 21.
---

# checks.json

Genera `bootcamp/week-{{NN}}-{{SLUG}}/checks.json`.

Lee antes [`docs/autograding.md`](../../docs/autograding.md), que documenta el formato y
las formas reales que devuelve cada operación del puente.

## Formato

```json
{
  "semana": "{{NN}}",
  "titulo": "{{TITULO}}",
  "checks": [
    {
      "id": "kebab-case-corto",
      "descripcion": "Una línea, en positivo, describiendo el estado correcto",
      "op": "project_settings",
      "args": {},
      "expr": "int(r['settings']['timelineResolutionWidth']) == 1920",
      "pista": "File > Project Settings > Master Settings > Timeline resolution."
    }
  ]
}
```

| Campo | Regla |
| ----- | ----- |
| `id` | kebab-case, corto, único en la semana. Es lo que acepta `--check` |
| `descripcion` | Una línea, en positivo. Describe el estado correcto, no el fallo |
| `op` | Operación de **lectura** del puente. Nunca una que escriba |
| `args` | `{}` si no lleva. `{"bin": ["01-Basicos"]}` para entrar en un bin |
| `expr` | Expresión de Python que devuelve booleano. `r` es el resultado de la operación |
| `pista` | La ruta concreta para arreglarlo. Se imprime solo al fallar |

## Reglas duras

1. **Una comprobación, un hecho.** Si la descripción necesita una "y", son dos checks.
2. **`expr` siempre booleana.** Nada que devuelva un número o una cadena.
3. **Solo operaciones de lectura.** El verificador nunca modifica el proyecto.
4. **`pista` accionable**: una ruta de menú, un atajo o un nombre exacto. Nunca "revisa
   la configuración" ni "asegúrate de que está bien".
5. **Los nombres literales coinciden con el `3-proyecto/README.md`** carácter a
   carácter. Prefijo `BC-`.
6. **Comprueba la forma antes de escribir la expresión.** Ejecuta la operación contra
   Resolve 21 con el servidor MCP `resolve` y mira lo que devuelve de verdad. Los tipos
   no son homogéneos: `timelineFrameRate` llega como número y las resoluciones como
   cadena.
7. **Prueba que el check falla.** Rompe el estado a propósito en Resolve y ejecuta
   `python scripts/verificar-semana.py {{NN}} --check <id>`. Un check que nunca ha
   fallado no está probado.

## Qué se comprueba y qué no

| Se comprueba | No se comprueba |
| ------------ | --------------- |
| Que existe algo, y con qué nombre | Si está bien hecho estéticamente |
| Cuántos clips, pistas, marcadores o bins hay | Si la elección de plano es acertada |
| Valores de configuración del proyecto | Si el look de color funciona |
| Estructura de la timeline y ausencia de huecos | Si el montaje tiene ritmo |

Lo estético va a `rubrica-evaluacion.md`, con criterios observables. Si un entregable no
se puede comprobar ni por API ni por un criterio observable escrito, **replantea el
entregable**.

## Cuántos

Entre cuatro y ocho por semana. Menos de cuatro y la semana no está verificando su
entregable; más de ocho y estás comprobando trivialidades.

## Verificación antes de entregar

- [ ] `jq -e . checks.json` pasa
- [ ] Cada `expr` la he probado contra el resultado real de la operación
- [ ] Cada check lo he visto **fallar** al romper el estado a propósito
- [ ] Cada `pista` da una ruta concreta
- [ ] Los nombres coinciden con `3-proyecto/README.md`
- [ ] Ninguna operación escribe nada
