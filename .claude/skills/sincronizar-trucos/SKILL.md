---
name: sincronizar-trucos
description: Mantiene docs/trucos-resolve.md sincronizado con las secciones "🎩 Trucos y atajos" de los README de cada semana. Úsalo tras publicar o editar una semana.
---

# Sincronizar trucos

`docs/trucos-resolve.md` es el índice global de todos los trucos del bootcamp. Cada
truco vive en dos sitios: el README de su semana y ese documento. Este skill los cuadra.

## 1. Extraer

De cada `bootcamp/week-NN-*/README.md`, la tabla bajo `## 🎩 Trucos y atajos`:

```bash
for f in bootcamp/week-*/README.md; do
  echo "== $f"
  awk '/^## 🎩/{p=1;next} /^## /{p=0} p' "$f"
done
```

## 2. Comparar

Contra las secciones `## Semana NN — Título` de `docs/trucos-resolve.md`.

Tres tipos de desajuste:

| Desajuste | Qué hacer |
| --------- | --------- |
| Truco en el README de la semana pero no en el documento global | Añadirlo al documento, en su sección de semana |
| Truco en el documento global pero no en el README | Investigar: o se borró del README y hay que quitarlo, o falta en el README |
| El mismo truco con texto distinto en los dos sitios | Gana el README de la semana; actualiza el documento global |

## 3. Reglas del documento global

- **Una sección por semana**, en orden numérico, con el título completo de la semana.
- **Tabla Truco | Cómo**, el mismo formato que en el README.
- El texto se copia **literal** del README de la semana. No se reescribe ni se resume.
- Las semanas sin publicar no tienen sección: no se crean secciones vacías.

## 4. Criterio de admisión

Antes de sincronizar un truco, comprueba que merece serlo:

- ✅ Ahorra tiempo real, o revela algo que la interfaz esconde
- ✅ Es estable: un atajo, una ruta de menú, un modificador
- ❌ No es un consejo genérico de productividad
- ❌ No depende de plugins de terceros no mantenidos
- ❌ No describe un botón por su posición en pantalla

Si un truco del README no cumple, repórtalo en vez de propagarlo.

## 5. Informe

Lista de trucos añadidos, actualizados y descartados, con la semana de cada uno. Y los
que no cumplen el criterio de admisión, para que se decida si se quitan del README.
