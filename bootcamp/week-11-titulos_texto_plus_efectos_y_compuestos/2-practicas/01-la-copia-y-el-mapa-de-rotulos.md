# Práctica 01 — La copia y el mapa de rótulos

> Al terminar tendrás `BC-Montaje-v5` con sus pistas preparadas, las guías de encuadre encendidas,
> y la pieza recorrida de principio a fin con un marcador en cada sitio que pide un rótulo y en cada
> sitio que pide una transición o un efecto. Sin haber escrito todavía una sola letra.

**Duración estimada**: 45 min
**Prerrequisitos**: [Semana 10](../../week-10-velocidad_transformaciones_y_estabilizacion/README.md) cerrada, [Teoría 01](../1-teoria/01-el-titulo-es-un-clip.md), [Teoría 05](../1-teoria/05-legibilidad-safe-areas-y-contraste.md)

## Contexto

La tentación de esta semana es abrir la `Effects Library` y empezar a poner rótulos por donde
vayas cayendo. Sale una pieza con doce rótulos, tres de ellos innecesarios, y ninguno donde de
verdad hacía falta.

El orden que funciona es el mismo de la Semana 10: **primero se decide, después se ejecuta**. Esta
práctica es la parte de decidir, y es la que hace que las otras tres vayan rápidas.

---

## Paso 1: Duplicar el montaje

**Por qué**: `BC-Montaje-v4` es la referencia contra la que se mide esta semana, y la comparación
del paso 7 de la práctica 04 la necesita entera.

1. En el media pool, clic derecho sobre **`BC-Montaje-v4`** `>` **`Duplicate Timeline`**
2. Renombra la copia: doble clic sobre su nombre y escribe **`BC-Montaje-v5`**
3. **Doble clic** sobre `BC-Montaje-v5` para abrirla

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check montaje-v5-activa
```

> [!WARNING]
> Duplica, **no renombres**. Si renombras `BC-Montaje-v4` te quedas sin la versión de la Semana 10 y
> el check `montaje-v4-conservada` falla. Recuperarla exige importar el respaldo
> `BC-Bootcamp-Resolve-semana10.drp` con otro nombre para no machacar lo que tienes.

---

## Paso 2: Un respaldo de timeline antes de tocar nada

**Por qué**: esta semana se añaden pistas y se empaquetan clips. Un respaldo de timeline pesa nada
y se restaura en dos clics.

1. `File > Create Timeline Backup`
2. Nómbralo `antes-de-rotular`

**Verifica**: aparece en la lista de respaldos de timeline del proyecto.

---

## Paso 3: Preparar las pistas

**Por qué**: un título arrastrado sobre la `V1` **sustituye** el plano que hay debajo. Tener las
pistas antes de empezar evita ese error, que además es silencioso: no avisa, solo tapa.

1. Clic derecho sobre la cabecera de la pista **`Video 1`** `>` **`Add Track`**. Aparece `Video 2`
2. Clic derecho sobre la cabecera de **`Video 2`** `>` **`Add Track`**. Aparece `Video 3`
3. Si la vista de la timeline lo permite —`Filmstrip` o `Thumbnail`, y la pista lo bastante alta—,
   clic sobre el nombre `Video 2` y escribe `Rotulos`; y sobre `Video 3`, `Ajustes`

El reparto de esta semana:

| Pista | Qué va a llevar |
| ----- | --------------- |
| **`V1`** | El montaje. **No se toca** |
| **`V2`** | Los rótulos y los títulos |
| **`V3`** | Los adjustment clips |

**Verifica**: la timeline tiene tres pistas de vídeo y las dos de arriba están vacías.

---

## Paso 4: Encender las guías de encuadre

**Por qué**: si colocas los rótulos con las guías apagadas, la mitad acaba demasiado cerca del
borde, y recolocarlos después es una tarde.

1. `View > Safe Area > On/Off`
2. `View > Safe Area > Action`
3. `View > Safe Area > Title`
4. `View > Safe Area > Center`, si te sirve de referencia

Y si tu pieza va a salir además en vertical o en cuadrado en algún sitio:

5. El **icono de guías de encuadre** de la esquina superior derecha del visor `>` `Social Media` `>`
   la relación que corresponda: `9:16` para vertical, `1:1` para cuadrado

**Verifica**: en el visor se ven dos rectángulos concéntricos. El interior es `Title`: ahí dentro
va todo el texto.

---

## Paso 5: Recorrer la pieza y marcar en amarillo dónde falta información

**Por qué**: este es el trabajo real de la semana. Un rótulo hace falta cuando **la imagen no da un
dato que quien mira necesita en ese momento**, no cuando queda bonito.

Reproduce la pieza entera de principio a fin, y para cada vez que pienses «¿quién es este?»,
«¿dónde estamos?», «¿qué está pasando aquí?»:

1. Pausa
2. Coloca el cabezal en el fotograma donde el rótulo tendría que **entrar**
3. `Mark > Add Marker`, eligiendo **amarillo** (`Yellow`) — o el desplegable del botón `Add Marker`
4. **Renómbralo con el texto que va a llevar el rótulo**, no con la palabra «título»

Las cuatro preguntas que sirven para decidir:

| Pregunta | Si la respuesta es que sí |
| -------- | ------------------------- |
| ¿Alguien habla y no sabemos quién es? | Rótulo de identificación |
| ¿Hemos cambiado de sitio y no se entiende dónde? | Rótulo de localización |
| ¿La pieza empieza sin decir qué es? | Título de entrada |
| ¿Hay un dato —una fecha, una cifra, un nombre— que la voz no dice? | Rótulo de dato |

**Mínimo: tres marcadores amarillos**, y uno tiene que ser el título de entrada.

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check marcadores-de-rotulo
```

> [!TIP]
> El nombre del marcador es la mitad del trabajo hecho. Si escribes ahí `Marta Ruiz · bióloga
> marina`, en la práctica 02 solo tienes que copiarlo al rótulo. Si escribes `titulo`, en la
> práctica 02 vuelves a pensarlo.

---

## Paso 6: Segunda pasada, marcando en verde dónde pide una transición o un efecto

**Por qué**: las transiciones y los efectos se deciden con la pieza montada delante, no plano a
plano. Y se deciden **por defecto en contra**: un corte es la opción correcta hasta que se
demuestre lo contrario.

Vuelve a reproducir la pieza. Marca en **verde** (`Green`), con nombre propio, cada punto donde:

| Situación | Qué va a llevar |
| --------- | --------------- |
| Un cambio de tiempo o de lugar que el corte no explica | Una disolución |
| El principio o el final de la pieza | Un fundido |
| Un corte dentro del mismo plano que da un brinco | `Smooth Cut` |
| Un tramo de varios planos seguidos que pide el mismo tratamiento | Un adjustment clip |
| Un fondo tan claro o tan movido que un rótulo no se va a leer encima | Un adjustment clip que lo rebaje |

**Mínimo: dos marcadores verdes.**

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check marcadores-de-efecto
```

> [!IMPORTANT]
> Si terminas la pasada con nueve marcadores verdes, vuelve a mirarlos. Una pieza de cinco minutos
> con nueve transiciones tiene ocho de más. Deja los dos o tres que responden a la pregunta «¿qué
> dice esta transición que el corte no dice?» y quita el resto.

---

## Paso 7: Abrir el apartado de notas

**Por qué**: es el entregable escrito de la semana, y se abre ahora para no reconstruirlo de
memoria el domingo.

En `BC-Resolve/04-respaldos/notas-de-montaje.md`, el mismo archivo de las Semanas 06 a 10, añade:

```markdown
## Títulos y efectos — Semana 11

### El mapa de rótulos — práctica 01
- Marcadores amarillos: __ · qué dice cada uno: __
- Marcadores verdes: __ · qué resuelve cada uno: __
- Guías encendidas: Action / Title / ______
- ¿La pieza va a salir en otra relación de aspecto? ______
```

**Verifica**: el archivo tiene el apartado abierto y las cifras puestas.

---

## Paso 8: Comprobar la semana hasta aquí

```bash
python scripts/verificar-semana.py 11
```

De los diez checks, en este punto tienen que estar en verde: `proyecto-abierto`,
`montaje-v4-conservada`, `montaje-v5-activa`, `montaje-v5-clips`, `montaje-v5-sin-huecos`,
`marcadores-de-rotulo` y `marcadores-de-efecto`.

Los tres que faltan —`rotulos-en-v2`, `capa-de-ajuste` y `bin-de-titulos`— son de las prácticas 02,
03 y 04.

---

## ✅ Resultado

- [ ] `BC-Montaje-v4` intacta
- [ ] `BC-Montaje-v5` creada y abierta
- [ ] Respaldo de timeline `antes-de-rotular` hecho
- [ ] Tres pistas de vídeo, con la `V2` y la `V3` vacías
- [ ] Guías `Action` y `Title` encendidas
- [ ] Tres marcadores amarillos o más, cada uno con el texto de su rótulo
- [ ] Dos marcadores verdes o más, cada uno con lo que va a resolver
- [ ] El apartado `## Títulos y efectos — Semana 11` abierto en `notas-de-montaje.md`

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `montaje-v4-conservada` falla | Renombraste en vez de duplicar | Importa `BC-Bootcamp-Resolve-semana10.drp` con otro nombre |
| `montaje-v5-activa` falla | Está creada pero no abierta | Doble clic sobre ella en el media pool |
| `montaje-v5-clips` falla | Has borrado planos, o la timeline abierta no es la v5 | Restaura el respaldo `antes-de-rotular` |
| La pista nueva sale debajo | Pulsaste sobre la cabecera equivocada | La pista de vídeo nueva sale **encima** de aquella sobre la que pulsaste |
| No veo los nombres de las pistas | La vista de timeline o la altura de pista | Cambia a `Filmstrip` o `Thumbnail` y sube la altura |
| Las guías no aparecen | `View > Safe Area > On/Off` apagado | Enciéndelo, y luego cada guía por separado |
| `marcadores-de-rotulo` falla con tres marcadores puestos | Alguno conserva su `Marker N` de fábrica | `Index > Markers`, edita el campo `Name` sobre la fila |
| Los marcadores no aparecen en el check | Los pusiste en un clip y no en la timeline | Deselecciona todo antes de pulsar `M`: un marcador de clip no es un marcador de timeline |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · La copia y el mapa de rótulos** | [02 · El título principal y los rótulos](02-el-titulo-principal-y-los-rotulos.md) |

← [Volver a la Semana 11](../README.md)
