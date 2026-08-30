# Práctica 01 — La copia y el mapa de problemas

> Al terminar tendrás `BC-Montaje-v3` creada a partir de tu montaje de la Semana 07, y una lista
> de entre ocho y quince marcadores de colores que es, literalmente, el plan de trabajo del resto
> de la semana.

**Duración estimada**: 50 min
**Prerrequisitos**: [Teoría 01](../1-teoria/01-que-es-el-trimming.md), [Teoría 09](../1-teoria/09-marcadores.md), `BC-Montaje-v2` acabada de principio a fin

## Contexto

Esta semana se trabaja sobre **el montaje de verdad**, no sobre una timeline de prueba. Es la
primera vez que pasa desde la Semana 07, y es a propósito: afinar solo tiene sentido sobre una
pieza entera.

Por eso lo primero es una copia. Y lo segundo, y más importante: **una pasada de visionado sin
tocar nada**. Es el paso que todo el mundo se salta y el que decide si la semana sale bien.

---

## Paso 1: Duplicar el montaje

**Por qué**: `BC-Montaje-v2` es el resultado de dos semanas de trabajo y es lo que va a comparar
la rúbrica. Si afinas encima, pierdes la referencia de cuánto has mejorado —y de cuánto has roto—.

> [!WARNING]
> **Antes de duplicar, exporta un respaldo si todavía no lo tienes**: `File > Export Project` →
> `04-respaldos/BC-Bootcamp-Resolve-semana08.drp`. Esta semana vas a hacer operaciones con ripple
> sobre tu montaje bueno, y el ripple es la única operación de la semana que puede desincronizar
> tramos enteros. Un `.drp` pesa poco.

1. En el media pool, **clic derecho sobre `BC-Montaje-v2` > `Duplicate Timeline`**
2. Aparece `BC-Montaje-v2 copy`. Clic derecho `> Rename` y llámala **`BC-Montaje-v3`**
3. **Doble clic** para abrirla

El nombre es exacto: `BC-Montaje-v3`, con guiones, `M` mayúscula, uve minúscula y el 3 sin ceros
delante.

**Verifica**:

```bash
python scripts/verificar-semana.py 09 --check montaje-v3-existe
python scripts/verificar-semana.py 09 --check montaje-v3-activa
```

---

## Paso 2: El punto seguro de la semana

**Por qué**: el respaldo de timeline es interno a Resolve y se hace en un segundo. Deshacer diez
operaciones de ripple encadenadas es mucho peor que restaurar un punto.

1. Con `BC-Montaje-v3` abierta, **`File > Create Timeline Backup`**
2. Ponle un nombre que reconozcas: `antes-de-afinar`

**Verifica**: clic derecho sobre `BC-Montaje-v3` en el media pool `> Restore Timeline Backup` y
comprueba que tu punto aparece en la lista. **No lo restaures**: solo mira que está.

---

## Paso 3: Preparar la timeline para anotar

**Por qué**: tres ajustes que, si no los tocas ahora, te van a estorbar durante toda la semana.

1. **`Timeline > Ripple Timeline Markers`** — actívalo. Así tus notas se desplazarán con los
   ripples y seguirán señalando lo que señalaban.
2. **`N`** — comprueba que el imán está activado. Lo vas a querer para casi todo.
3. **`Ctrl+Shift+A`** (Win) / **`Cmd+Shift+A`** (Mac) — deselecciona todo. Es lo que hace que los
   marcadores vayan a la timeline y no a un clip.

**Verifica**: en el menú `Timeline`, `Ripple Timeline Markers` aparece marcado. En la timeline no
hay ningún clip resaltado.

---

## Paso 4: La pasada de visionado, sin tocar nada

**Por qué**: es el paso central de la práctica. Todo lo demás de la semana se hace sobre la lista
que sale de aquí. Si arreglas el primer problema que ves, no ves los otros catorce.

> [!IMPORTANT]
> **Regla del paso 4: no se toca ni un clip.** Lo único que se pulsa es `M` y, como mucho,
> `Ctrl+M` / `Cmd+M`. Si te pica la mano, es normal: apúntalo y sigue.

1. Lleva el cabezal al primer fotograma de la pieza
2. **`P`** para poner el visor a pantalla completa —`Workspace > Viewer Mode > Cinema Viewer`—.
   Ver la pieza pequeña, con la timeline debajo, es ver la timeline, no la pieza
3. **Auriculares puestos**
4. Reproduce **entera, sin parar**
5. Cada vez que algo te chirríe, **`M`**. No pares, no analices, no escribas todavía
6. Al acabar, `P` para volver

**Verifica**: tienes marcadores en la regla de tiempo. Si tienes menos de seis, o estabas mirando
la timeline en vez de la pieza, o la pieza está mejor de lo que crees; en el segundo caso, dale
otra pasada buscando específicamente los cuatro defectos de la teoría 01.

---

## Paso 5: Ponerle nombre y color a cada marcador

**Por qué**: `Marker 7` no significa nada mañana. El color es lo que te va a permitir trabajar por
lotes, y el nombre es lo que te dice qué viste.

Abre **`Index > Markers`**. Ahí están todos, en una lista, y los campos `Name` y `Notes` se editan
directamente sobre la fila.

Para cada marcador:

1. **Doble clic** en su fila del índice: el cabezal salta ahí
2. Míralo un momento y decide **qué le pasa**
3. Escribe en `Name` una frase corta: *«el plano de la ventana entra tarde»*
4. Asígnale color según el sistema:

| Color | Significa | Se arregla en |
| ----- | --------- | ------------- |
| 🔴 **Rojo** | Este corte hay que afinarlo | Práctica 02 |
| 🟡 **Amarillo** | Este plano sobra o dura demasiado | Práctica 02 |
| 🟢 **Verde** | Aquí va un split edit | Práctica 04 |
| 🔵 **Azul** | Resuelto, o nota para una fase posterior | — |

El color se cambia abriendo el marcador con doble clic sobre él en la regla, o poniéndolo ya del
color correcto con `Mark > Add Marker >` y el color.

**Verifica**:

```bash
python scripts/verificar-semana.py 09 --check marcadores-anotados
```

El check pide **ocho marcadores o más**, todos con nombre propio —ninguno con el `Marker N` de
fábrica— y ninguno con el nombre vacío.

---

## Paso 6: Ordenar la lista de trabajo

**Por qué**: no todos los problemas cuestan lo mismo ni valen lo mismo. Un plano que sobra entero
se quita en diez segundos y mejora la pieza más que media hora de afinado fino.

1. En el `Marker Index`, usa el menú de opciones `> Show Only` para filtrar por color
2. **Cuenta cuántos tienes de cada uno** y anótalo

El orden de trabajo del resto de la semana:

| Orden | Color | Por qué primero |
| ----- | ----- | --------------- |
| 1.º | 🟡 Amarillo | Quitar lo que sobra cambia la pieza entera. Y algunos rojos desaparecen solos al quitar un plano |
| 2.º | 🔴 Rojo | Afinar entradas y salidas, con lo que queda |
| 3.º | 🟢 Verde | Los split edits, al final, sobre un montaje ya estable |

**Verifica**: sabes cuántos marcadores tienes de cada color y en qué orden vas a atacarlos.

---

## Paso 7: Abrir el apartado de notas

**Por qué**: la rúbrica pregunta por cifras, y las cifras de hoy —cuánto dura la pieza antes de
afinar— no se pueden reconstruir el viernes.

Abre `04-respaldos/notas-de-montaje.md`, el mismo archivo de las Semanas 06, 07 y 08, y añade:

```markdown
## Trimming — Semana 09

- Duración de BC-Montaje-v2 al empezar: __:__
- Marcadores puestos: __ (rojos __ · amarillos __ · verdes __)
- Los tres problemas que más me molestan de la pieza:
  1.
  2.
  3.
```

La duración total se lee en el visor de timeline, o en el `Edit Index`.

**Verifica**: el apartado existe y las cifras están puestas.

---

## Paso 8: Guardar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 09
```

De diez checks, ahora mismo deberían pasar cinco o seis: los del proyecto, `montaje-v2-conservada`,
`montaje-v3-existe`, `montaje-v3-activa`, `montaje-v3-pistas-con-nombre` y `marcadores-anotados`.
Los de huecos y split edits son de las prácticas 02 y 04.

---

## ✅ Resultado

- [ ] `BC-Montaje-v3` existe, creada por duplicado de `BC-Montaje-v2`
- [ ] `BC-Montaje-v2` sigue intacta
- [ ] Hay un respaldo de timeline llamado `antes-de-afinar`
- [ ] `Ripple Timeline Markers` está activado
- [ ] Vi la pieza entera sin tocar nada
- [ ] Ocho marcadores o más, con nombre propio y color
- [ ] Sé cuántos tengo de cada color y en qué orden voy a atacarlos
- [ ] El apartado `## Trimming — Semana 09` está abierto, con la duración de partida

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `montaje-v3-existe` falla | El nombre no es exacto | `BC-Montaje-v3`, sin espacios ni ceros de más |
| `montaje-v3-activa` falla | Tienes abierta otra timeline | Doble clic en `BC-Montaje-v3` |
| Los marcadores aparecen sobre los clips y no en la regla | Había algo seleccionado al pulsar `M` | Bórralos y repite con `Ctrl+Shift+A` / `Cmd+Shift+A` antes |
| `marcadores-anotados` falla con diez marcadores puestos | Alguno conserva el `Marker N` de fábrica | El `Marker Index` los enseña todos: ordena por `Name` y los ves juntos |
| No sé qué escribir en un marcador | No sabes qué te chirrió | Bórralo. Un marcador que no sabes explicar no es trabajo |
| Solo puse tres marcadores | Estabas mirando la timeline | Otra pasada con `P`, buscando los cuatro defectos de la teoría 01 |
| `Duplicate Timeline` no aparece | Hiciste clic derecho sobre un clip, no sobre la timeline | La timeline está en el bin `Master`, con su icono propio |
| El índice de marcadores está vacío | Estás en la pestaña `Edit Index` | `Index > Markers` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · La copia y el mapa de problemas** | [02 · Ripple y roll sobre tu montaje](02-ripple-y-roll-sobre-tu-montaje.md) |

← [Volver a la Semana 09](../README.md)
