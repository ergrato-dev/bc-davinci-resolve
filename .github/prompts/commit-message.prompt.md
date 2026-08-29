---
mode: agent
description: Genera el mensaje de commit del bootcamp DaVinci Resolve 21.
---

# Mensaje de commit

Genera el mensaje del commit a partir de los cambios preparados (`git diff --staged`).

## Formato

[Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>(<alcance>): <descripción en imperativo, español, sin punto final>

[cuerpo opcional: el porqué, no el qué]
```

## Tipos

| Tipo | Cuándo |
| ---- | ------ |
| `feat` | Contenido nuevo: una semana, una teoría, una práctica, un diagrama |
| `fix` | Corrección: errata, ruta de menú equivocada, enlace roto, check que no funcionaba |
| `docs` | Cambios en `docs/`, `README.md`, `CONTRIBUTING.md` y compañía |
| `refactor` | Reorganización sin cambio de contenido |
| `chore` | Scripts, `.gitignore`, configuración del repositorio |

## Alcances

- `week-NN` para contenido de una semana concreta
- El nombre del documento para `docs/`: `docs(pack-de-medios)`, `docs(free-vs-studio)`
- `scripts` para el tooling
- `assets` para los recursos visuales globales

## Ejemplos reales

```
feat(week-01): contenido completo de la Semana 01 — fundamentos de imagen en movimiento
feat(week-01): añade el diagrama de obturador y desenfoque de movimiento
fix(week-01): corrige la ruta de Timeline frame rate en la práctica 02

    En Resolve 21 el ajuste vive en Master Settings, no en la pestaña
    General como decía el texto. Verificado en 21.0.4.5.

docs(free-vs-studio): aclara que el scripting interno sí funciona en Free
chore(scripts): el verificador acepta --check para ejecutar una sola comprobación
```

## Reglas

- **Español**, imperativo, sin punto final en la primera línea.
- **Primera línea de 72 caracteres o menos.** Si no cabe, el commit hace demasiadas cosas.
- **El cuerpo explica el porqué**, no repite el diff. Solo si aporta algo.
- **Cuando corrijas algo de la interfaz, di la versión** donde lo verificaste
  (`Verificado en 21.0.4.5`).
- **Nunca** menciones claves de licencia, tokens ni rutas absolutas de una máquina.
- Un commit por unidad de trabajo. Una semana completa puede ser un commit; una semana
  a medias más un arreglo de otra, no.
