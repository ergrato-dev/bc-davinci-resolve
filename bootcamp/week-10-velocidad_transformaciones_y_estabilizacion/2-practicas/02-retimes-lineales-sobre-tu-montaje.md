# Práctica 02 — Retimes lineales sobre tu montaje

> Al terminar, tu pieza tendrá tres cambios de velocidad reales, un fotograma congelado colocado al
> fotograma exacto y ni un hueco. Y vas a haber visto, con tus clips, la diferencia entre marcar y
> no marcar `Ripple Sequence`.

**Duración estimada**: 60 min
**Prerrequisitos**: [Práctica 01](01-la-copia-y-el-mapa-de-velocidad.md), [Teoría 02](../1-teoria/02-las-cuatro-formas-de-cambiar-la-velocidad.md), [Teoría 03](../1-teoria/03-freeze-frame-y-reverse.md)

## Contexto

Vas a atacar los marcadores morados de la práctica 01, en orden, con las vías **lineales**: una
sola velocidad por clip. La velocidad variable es la práctica 03.

La regla de la práctica: **antes de cada retime, decides la casilla `Ripple Sequence`**. Escríbelo
en el marcador si hace falta. Es la decisión que se olvida y la que rompe cosas.

---

## Paso 1: Un experimento controlado con `Ripple Sequence`

**Por qué**: hay que ver lo que hace esa casilla una vez, sobre material propio, para no volver a
olvidarla. Se hace y se deshace en dos minutos.

1. Elige un clip de en medio de la pieza que tenga otro clip **justo detrás**
2. Fíjate en la **duración total** de la pieza, abajo a la derecha de la timeline. Anótala
3. `Clip > Change Clip Speed`. En el diálogo `Edit Speed Change`, pon `Speed` a **50 %** y deja
   `Ripple Sequence` **desmarcada**. Confirma el diálogo
4. Mira qué ha pasado: el clip mide el doble y **ha pisado** a su vecino. La pieza dura lo mismo
5. `Ctrl+Z` (Win) / `Cmd+Z` (Mac)
6. Repite con `Ripple Sequence` **marcada**
7. Mira otra vez: el clip mide el doble y todo lo de detrás se ha desplazado. La pieza dura más
8. `Ctrl+Z`

**Verifica**: la duración total de la pieza es la misma que anotaste en el paso 2.

Anota en tus notas, con una frase tuya, qué hace la casilla.

---

## Paso 2: Los acelerados

**Por qué**: es el retime con mejor relación entre esfuerzo y resultado. Un travelling de doce
segundos al 200 % son seis segundos que cuentan lo mismo, y funcionan con cualquier cadencia de
rodaje: acelerar nunca inventa fotogramas, los tira.

Filtra el `Marker Index` por morado y ve a los marcadores que pedían acelerar. Para cada uno:

1. Selecciona el clip
2. `Clip > Change Clip Speed`
3. Marca **`Ripple Sequence`**
4. Escribe el valor. Si sabes la duración que quieres, usa el campo **`Duration`** en vez del
   porcentaje: es más directo
5. Confirma el diálogo
6. **`/`** para verlo en contexto

**Verifica**: la duración total de la pieza ha bajado. Anota cuánto.

> [!WARNING]
> Después de cada acelerado con ripple, **mira las pistas de encima**. Un rótulo o un recurso que
> estaba colocado sobre un plano concreto puede haberse quedado donde estaba. Es el mismo problema
> del ripple de la Semana 09, y la solución es la misma: mirar antes de seguir.

---

## Paso 3: Las cámaras lentas

**Por qué**: es donde el techo de la teoría 01 deja de ser teoría.

Para cada marcador morado que pedía ralentizar:

1. Comprueba el **techo** que anotaste en el `Notes` del marcador
2. Selecciona el clip y `Clip > Change Clip Speed`
3. `Ripple Sequence` marcada
4. Pon un porcentaje **por encima del techo**. Si el techo es 40 %, pon 45 o 50, no 30
5. Confirma el diálogo
6. Reproduce en bucle: **`Ctrl+/`** (Win) / **`Cmd+/`** (Mac) y luego **`/`**
7. Mira **los bordes de lo que se mueve**. ¿Tirones? ¿Doble imagen? ¿Bordes derretidos?

Si se ve mal, dos salidas antes de rendirte:

| Lo que ves | Prueba |
| ---------- | ------ |
| Tirones | Sube el porcentaje: estás por debajo del techo |
| Bordes derretidos o dobles | Baja ese clip a `Frame Blend` en `Inspector > Video > Retime and Scaling > Retime Process` |

**Verifica**: cada cámara lenta se ve limpia a tamaño completo, no solo en el visor pequeño.

---

## Paso 4: El fotograma congelado

**Por qué**: es el único retime de la semana que exige colocar el cabezal al fotograma, y por eso
se practica aparte.

Elige el sitio de tu pieza donde un freeze aporte algo de verdad —un gesto que cierra una idea, un
plano bajo un rótulo de sección, el final de un tramo—:

1. Coloca el cabezal aproximadamente
2. Ajusta con **`Flecha izquierda`** y **`Flecha derecha`** hasta el fotograma exacto
3. Mira el fotograma en el visor: ¿está nítido, o pillado en pleno movimiento borroso? Si está
   borroso, busca otro
4. Selecciona el clip
5. **`Shift+R`** — `Clip > Freeze Frame`
6. Reproduce el tramo con **`/`**

**Verifica**: el clip entero es esa imagen, y la duración del clip no ha cambiado.

> [!NOTE]
> Si el freeze tiene que durar más de lo que dura el clip, se alarga como cualquier otro clip:
> `T` para modo trim y ripplea su borde derecho. Ya no hay material que se acabe: es una imagen
> fija y se estira lo que quieras.

---

## Paso 5: Un reverse, si tu pieza lo pide

**Por qué**: es la operación más fácil de la semana y la que más rápido se nota cuando está mal
puesta. Con hacer una basta.

Busca un plano **sin voz** donde ir hacia atrás signifique algo:

1. Selecciona el clip
2. `Clip > Change Clip Speed` y marca **`Reverse Speed`**
3. Confirma el diálogo
4. Reproduce

**Verifica**: las flechas de la pista de retime apuntan a la izquierda.

Si tu pieza no pide ninguno, **no lo fuerces**: apúntalo en tus notas y pasa al paso siguiente. El
reverse no es un entregable.

---

## Paso 6: El plano que no daba, con `Fit to Fill`

**Por qué**: es la vía que resuelve el problema al revés —manda el hueco, no el plano— y se hace
una vez para tenerla en el repertorio.

Si tienes un hueco o un plano corto que quieras sustituir por otro que no llega:

1. Marca **`I`** y **`O`** en la timeline sobre el tramo a llenar. O borra los puntos con
   **`Alt+X`** (Win) / **`Opt+X`** (Mac) y pon el cabezal dentro del hueco
2. En el `Source Viewer`, abre el plano nuevo y marca su **`I`** y su **`O`**
3. Comprueba los `Source Track Selector`
4. **`Shift+F11`**

**Verifica**: el clip entra retimado y con su distintivo de retime, y encaja exacto.

---

## Paso 7: Cerrar los huecos

**Por qué**: los retimes sin ripple dejan huecos, y los ripples que se corrigen a mano también. Un
hueco de tres fotogramas es un parpadeo a negro que se ve en la exportación y no en la timeline.

1. **`Shift+Z`** para ver la pieza entera
2. Recórrela con el botón `Detail Zoom`
3. Cada hueco: clic para seleccionarlo y **`Forward Delete`** — `Supr` (Win), `Fn+Supr` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 10 --check montaje-v4-sin-huecos
```

---

## Paso 8: Repasar los distintivos

**Por qué**: es como se encuentra el clip que retimaste sin querer con un arrastre.

1. Recorre la timeline mirando el nombre de cada clip
2. Los que llevan **distintivo de retime** a la izquierda del nombre son los que has cambiado
3. ¿Hay alguno que no reconoces? Ábrelo con `Ctrl+R` / `Cmd+R` y mira su porcentaje. Si es un 97 %
   o un 103 %, es un arrastre accidental: `Reset to 100%`

**Verifica**: sabes decir, uno por uno, por qué cada distintivo está donde está.

---

## Paso 9: Anotar y guardar

1. En `notas-de-montaje.md`:

```markdown
### Retimes lineales — práctica 02
- Qué hace Ripple Sequence, con mis palabras: __
- Acelerados: __ clips · porcentajes: __
- Cámaras lentas: __ clips · porcentajes: __ · techos: __
- Freeze frame: en el minuto __ , el fotograma de __
- Reverse: __ (o «ninguno, mi pieza no lo pedía»)
- Duración de BC-Montaje-v4 después de la práctica 02: __:__
```

2. `Ctrl+S` / `Cmd+S`

**Verifica**:

```bash
python scripts/verificar-semana.py 10
```

Nueve de diez o diez de diez, según cuántos retimes lleves.

---

## ✅ Resultado

- [ ] El experimento de `Ripple Sequence` hecho y deshecho
- [ ] Los acelerados aplicados, con las pistas de encima comprobadas
- [ ] Las cámaras lentas por encima de su techo, juzgadas en bucle
- [ ] Un fotograma congelado colocado al fotograma exacto
- [ ] Un reverse, o la nota de por qué no
- [ ] Un `Fit to Fill`, si tu pieza tenía dónde
- [ ] Ni un hueco en la pista de vídeo principal
- [ ] Todos los distintivos de retime identificados
- [ ] Las cifras anotadas

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El clip retimado ha borrado al siguiente | `Ripple Sequence` desmarcada | `Ctrl+Z` y repite con la casilla marcada |
| Un rótulo rotula ahora el plano equivocado | El ripple movió lo de abajo y no lo de arriba | Recolócalo a mano; en la Semana 11 se hace al revés |
| La cámara lenta va a tirones | Por debajo del techo del plano | Sube el porcentaje |
| Los bordes se derriten | `Optical Flow` con movimiento caótico | Ese clip a `Frame Blend` en el Inspector |
| El freeze sale borroso | El fotograma tenía movimiento borroso grabado | Elige otro fotograma con la acción parada |
| El audio del plano ha enmudecido | Es lo que hace un retime | Si ese sonido importa, sácalo a otra pista antes |
| La voz suena grave | Retime lineal sin corrección de tono en Windows y Linux | Casilla `Pitch Correction` |
| `Fit to Fill` no hace nada | Faltan puntos de entrada y salida, o el selector de pista | Los cuatro puntos y el destino |
| `montaje-v4-sin-huecos` falla y no lo encuentro | Es un hueco de dos o tres fotogramas | `Detail Zoom` y recorrer, o `Index > Edit Index` |
| `montaje-v4-clips` falla | Has borrado planos enteros | Esta semana no se remonta: restaura `antes-de-retimar` |
| Se me ha descolocado todo | Un ripple grande | `Ctrl+Z`, o restaura el respaldo de timeline de la práctica 01 |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · La copia y el mapa de velocidad](01-la-copia-y-el-mapa-de-velocidad.md) | **02 · Retimes lineales sobre tu montaje** | [03 · Velocidad variable y calidad de imagen](03-velocidad-variable-y-calidad-de-imagen.md) |

← [Volver a la Semana 10](../README.md)
