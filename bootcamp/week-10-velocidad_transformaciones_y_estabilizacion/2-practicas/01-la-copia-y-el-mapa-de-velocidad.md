# Práctica 01 — La copia y el mapa de velocidad

> Al terminar tendrás `BC-Montaje-v4`, la cadencia de rodaje de todo tu material anotada, y la
> pieza recorrida entera con marcadores morados y cianes que dicen dónde hay que trabajar esta
> semana. Sin este mapa, las tres prácticas siguientes son dar palos de ciego.

**Duración estimada**: 45 min
**Prerrequisitos**: [Teoría 01](../1-teoria/01-el-techo-de-la-camara-lenta.md), [Teoría 02](../1-teoria/02-las-cuatro-formas-de-cambiar-la-velocidad.md)

## Contexto

La Semana 09 dejó tu montaje afinado y una lista de marcadores azules con lo que quedaba pendiente.
Esta semana se trabaja sobre una copia de aquello.

El orden de la semana es innegociable y sale de la [teoría 09](../1-teoria/09-estabilizacion-en-la-edit-page.md):
**velocidad primero, estabilización después, reencuadre al final**. Cada paso cambia la imagen sobre
la que trabaja el siguiente.

---

## Paso 1: Duplicar la timeline

**Por qué**: `BC-Montaje-v3` es tu montaje afinado y es la referencia contra la que se mide esta
semana. Los retimes cambian la duración de la pieza; si trabajas encima, pierdes la comparación.

1. En el `Media Pool`, clic derecho sobre **`BC-Montaje-v3`** `> Duplicate Timeline`
2. Renombra la copia a **`BC-Montaje-v4`** — exacto: guiones, `M` mayúscula, uve minúscula, sin
   ceros delante del 4
3. Doble clic para abrirla

**Verifica**:

```bash
python scripts/verificar-semana.py 10 --check montaje-v4-existe
```

> [!WARNING]
> **Duplicar, no renombrar.** Si renombras `BC-Montaje-v3` en vez de duplicarla, desaparece, y con
> ella el check `montaje-v3-conservada` y la comparación de la práctica 04. Si ya te ha pasado,
> recupérala del respaldo `BC-Bootcamp-Resolve-semana09.drp` importándolo con otro nombre para no
> machacar lo que tienes.

---

## Paso 2: Un respaldo de timeline antes de tocar nada

**Por qué**: esta semana se hacen operaciones que recolocan la pieza entera. Un respaldo de
timeline pesa nada y se restaura en dos clics.

1. `File > Create Timeline Backup`
2. Nómbralo `antes-de-retimar`

**Verifica**: aparece en la lista de respaldos de timeline del proyecto.

---

## Paso 3: Anotar la cadencia de rodaje de tu material

**Por qué**: el techo de cámara lenta de cada plano sale de este dato, y buscarlo cuarenta veces
durante la semana cuesta más que anotarlo una vez.

1. `Media Pool` en vista de lista — el botón de vista, arriba a la derecha del panel
2. Si no ves la columna **`FPS`**, clic derecho sobre la cabecera de columnas y actívala
3. Ordena por `FPS` haciendo clic en la cabecera
4. En `notas-de-montaje.md`, abre el apartado `## Velocidad y transformaciones — Semana 10` y anota:

```markdown
### Cadencias de mi material
- Clips a 24 fps: __ · techo 100 % (no admiten cámara lenta)
- Clips a 30 fps: __ · techo 80 %
- Clips a 50 fps: __ · techo 48 %
- Clips a 60 fps: __ · techo 40 %
- Otras cadencias: __
```

**Verifica**: sabes decir, sin mirar, cuántos planos de tu pieza admiten cámara lenta de verdad.

> [!NOTE]
> Si **todo** tu material está a 24 o 25 fps, no has hecho nada mal: es lo normal grabando con el
> móvil en modo automático. Significa que esta semana tu trabajo va a ser sobre todo de
> **acelerados, freezes, transformaciones y estabilización**, y que la cámara lenta la vas a usar
> poco y con `Optical Flow`. Anótalo y sigue: los entregables no dependen de tener material
> sobrecadenciado.

---

## Paso 4: La pasada de visionado

**Por qué**: es la misma pasada de la Semana 09 y sirve para lo mismo. Ves la pieza entera **una
vez**, con ojos limpios, y anotas sin arreglar nada. En cuanto empiezas a arreglar, dejas de ver.

1. `Workspace > Viewer Mode > Cinema Viewer`, atajo `P`
2. Auriculares puestos
3. Deselecciona todo antes de empezar: `Ctrl+Shift+A` (Win) / `Cmd+Shift+A` (Mac), para que los
   marcadores caigan en la timeline y no dentro de un clip
4. Reproduce de principio a fin **sin parar**
5. Cada vez que algo pida trabajo de esta semana, `M`

El sistema de colores de la semana:

| Color | Significa | De qué práctica es |
| ----- | --------- | ------------------ |
| 🟣 **Purple** | Aquí pide un cambio de velocidad | Prácticas 02 y 03 |
| 🩵 **Cyan** | Este plano se mueve demasiado: estabilizar | Práctica 04 |
| 🔵 **Blue** | Nota para más adelante, o resuelto | Se hereda de la Semana 09 |

Para poner un color concreto sin tocar el desplegable: `Mark > Add Marker >` y el color.

**Verifica**: has llegado al final sin haber tocado ni un clip.

---

## Paso 5: Nombrar los marcadores

**Por qué**: un marcador sin nombre es un marcador que no te dice nada el jueves. Y el verificador
comprueba que tienen nombre propio.

1. `Index > Markers`
2. Filtra por morado
3. Para cada uno, escribe en el campo `Name` **qué operación pide y con qué número**:
   - `Retime 40% - salto` · `Acelerar 200% - travelling largo` · `Freeze - el gesto de la mano`
4. Filtra por cian y haz lo mismo:
   - `Estabilizar - plano de la calle` · `Estabilizar - entrevista a pulso`
5. En el campo `Notes`, si hace falta, el porqué

Los campos `Name` y `Notes` se editan directamente sobre la fila.

**Verifica**:

```bash
python scripts/verificar-semana.py 10 --check marcadores-de-velocidad
python scripts/verificar-semana.py 10 --check marcadores-de-estabilizacion
```

Los dos deben pasar ya: **tres marcadores morados o más** y **dos cianes o más**, todos con nombre
propio.

> [!TIP]
> Si tu pieza no te pide tres cambios de velocidad de forma natural, no los inventes en sitios
> absurdos: busca los tres candidatos más honestos. Un travelling largo que se puede acelerar, un
> plano de recurso que gana ralentizado, un gesto que merece un freeze. Casi todas las piezas
> tienen esos tres.

---

## Paso 6: Comprobar el techo de cada marcador morado

**Por qué**: es el filtro que evita hacer un retime y descubrir a los diez minutos que el plano no
lo aguanta.

Para cada marcador morado:

1. Salta a él: `Shift+Flecha arriba` y `Shift+Flecha abajo`
2. Mira qué clip hay debajo y su cadencia de rodaje
3. Divide: `24 ÷ cadencia del clip × 100` = el techo
4. Si la velocidad que querías está **por debajo** del techo, cámbiala por una que esté por encima,
   o cambia la operación: quizá ese plano no se ralentiza, se acelera

Anota en el `Notes` del marcador el techo y el porcentaje que has decidido.

**Verifica**: ningún marcador morado pide una velocidad por debajo del techo de su plano.

---

## Paso 7: Fijar el `Retime Process` del proyecto

**Por qué**: es el ajuste que decide cómo se rellenan los fotogramas que falten, y es mejor
dejarlo puesto antes de empezar que descubrirlo a mitad de la práctica 03.

1. `File > Project Settings`
2. Panel `Master Settings`
3. Grupo `Frame Interpolation`
4. `Retime Process` `>` **`Optical Flow`**
5. `Motion estimation mode` `>` **`Enhanced Better`** si tu equipo lo aguanta, o
   **`Standard Better`** si va justo
6. `Save`

**Verifica**: reproduce un tramo cualquiera. Si la reproducción va bien, déjalo. Si se cae mucho,
baja a `Standard Faster` y activa el caché en el paso siguiente.

> [!NOTE]
> Este ajuste es el **valor por defecto** de todos los clips. En la práctica 03 vas a bajar algunos
> a `Frame Blend` uno por uno, y eso es lo esperado, no una corrección de este paso.

---

## Paso 8: Guardar y anotar

1. En `notas-de-montaje.md`, completa:

```markdown
### Mapa de velocidad — práctica 01
- Duración de BC-Montaje-v3 (punto de partida): __:__
- Marcadores morados (velocidad): __
- Marcadores cianes (estabilización): __
- Retime Process del proyecto: __ · Motion estimation: __
```

2. `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 10
```

Siete de diez. Los tres que faltan —`montaje-v4-clips`, `montaje-v4-sin-huecos` y
`retimes-aplicados`— llegan con las prácticas 02 y 03.

---

## ✅ Resultado

- [ ] `BC-Montaje-v4` creada por duplicado y abierta
- [ ] `BC-Montaje-v3` intacta
- [ ] Respaldo de timeline `antes-de-retimar` hecho
- [ ] Las cadencias de tu material anotadas, con sus techos
- [ ] La pieza vista entera de un tirón, sin tocar nada
- [ ] 3+ marcadores morados con nombre propio
- [ ] 2+ marcadores cianes con nombre propio
- [ ] Ningún marcador morado pide velocidad por debajo del techo
- [ ] `Retime Process` del proyecto decidido y anotado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `montaje-v4-existe` falla | El nombre no es literal | `BC-Montaje-v4`, sin espacios ni ceros |
| `montaje-v3-conservada` falla | Renombraste en vez de duplicar | Recupérala del `.drp` de la Semana 09 con otro nombre |
| Los marcadores caen dentro de un clip | Tenías algo seleccionado al pulsar `M` | `Ctrl+Shift+A` / `Cmd+Shift+A` y repite |
| No hay columna `FPS` en el media pool | La vista es de miniaturas, o la columna está oculta | Vista de lista, clic derecho en la cabecera |
| `marcadores-de-velocidad` falla con tres puestos | Alguno conserva su nombre de fábrica | Ordena el `Marker Index` por `Name`: los `Marker N` salen juntos |
| Todo mi material es de 24 fps | Es lo normal con un móvil en automático | Trabaja acelerados, freezes y transformaciones; ver la nota del paso 3 |
| La reproducción se cae al poner `Optical Flow` | Es el coste de calcular fotogramas en tiempo real | `Playback > Render Cache > Smart` |
| No encuentro tres sitios que pidan velocidad | Estás buscando efectos, no problemas | Busca duraciones que sobran y gestos que no se leen |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · La copia y el mapa de velocidad** | [02 · Retimes lineales sobre tu montaje](02-retimes-lineales-sobre-tu-montaje.md) |

← [Volver a la Semana 10](../README.md)
