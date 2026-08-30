# Práctica 03 — Transiciones y ResolveFX

> Al terminar habrás puesto las transiciones que tu pieza pedía —y solo esas—, habrás resuelto un
> corte que daba un brinco, y habrás aplicado un efecto a un tramo entero con un adjustment clip en
> vez de plano a plano.

**Duración estimada**: 60 min
**Prerrequisitos**: [Práctica 02](02-el-titulo-principal-y-los-rotulos.md), [Teoría 06](../1-teoria/06-transiciones-a-fondo.md), [Teoría 07](../1-teoria/07-las-categorias-de-resolvefx.md), [Teoría 08](../1-teoria/08-adjustment-clips.md)

## Contexto

Esta es la práctica donde más fácil es pasarse. El criterio para no pasarse está en los marcadores
verdes de la práctica 01: **si un punto no tiene marcador verde, no lleva transición**.

Y el orden importa: primero las transiciones, que tocan los puntos de edición y pueden acortar
planos; después los efectos, que se aplican sobre lo que quede.

---

## Paso 1: Comprobar qué colas tienes

**Por qué**: sin colas no hay transición, y saberlo antes evita el diálogo que te acorta los planos
sin que lo hayas decidido.

1. Ve al primer marcador **verde** que pida una disolución
2. Selecciona el punto de edición: cabezal cerca y pulsa **`V`**
3. Intenta la transición estándar: **`Ctrl+T`** (Win) / **`Cmd+T`** (Mac)

Si aparece:

| Lo que pasa | Qué significa |
| ----------- | ------------- |
| La transición se pone | Había colas suficientes |
| Sale el diálogo de `Trim Clips` / `Skip Clips` / `Cancel` | **No las hay** |

**Verifica**: sabes, para ese corte, si tenías colas o no.

> [!WARNING]
> **`Trim Clips` acorta los dos planos** para crear el solape que falta. Es una operación sobre tu
> montaje: los planos dejan de durar lo que decidiste en la Semana 09. Si el ritmo de ese punto
> estaba trabajado, dale a **`Cancel`** y decide en el paso 2.

---

## Paso 2: Poner las transiciones que pedían los marcadores verdes

**Por qué**: una transición dice algo —tiempo, lugar, principio, final—. Las que no dicen nada
distraen.

Para cada marcador verde que pida una disolución:

1. Selecciona el punto de edición con **`V`**
2. **`Ctrl+T`** / **`Cmd+T`**, o clic derecho sobre el punto de edición y una de las cuatro
   duraciones: un cuarto de segundo, medio segundo, un segundo o dos segundos
3. Si no hay colas y el corte aguanta perder fotogramas: **`Trim Clips`**
4. Si no las aguanta: **`Cancel`**, y crea el solape a mano con **`Alt+Shift`** (Win) /
   **`Opt+Shift`** (Mac) arrastrando el punto de edición sobre su vecino
5. Reproduce y ajusta la duración: arrastra el borde de la transición, o **`Ctrl+D`** / **`Cmd+D`**

Y decide la **alineación** de cada una:

| Si el corte… | Alineación |
| ------------ | ---------- |
| No está atado a nada concreto | `Center on Edit`, que es lo normal |
| Cae sobre un golpe de música, una palabra o un gesto | `End on Edit`, para que ese instante llegue nítido |
| Tiene que dejar respirar al plano que sale | `Start on Edit` |

Se cambia con clic derecho sobre la transición, o en `Alignment` del Inspector.

**Verifica**: reproduce cada transición. Ninguna llama la atención sobre sí misma.

---

## Paso 3: El fundido de entrada y el de salida de la pieza

**Por qué**: una pieza que empieza de golpe y acaba de golpe se nota, y es lo más barato de
arreglar.

Al **principio**, sobre el primer clip, y al **final**, sobre el último:

1. Pasa el ratón por la esquina superior del clip: aparece el **asa de fundido**
2. Arrástrala hacia dentro un segundo aproximadamente
3. Reproduce

Si prefieres una transición de verdad —por ejemplo para fundir desde un color que no sea el negro—:

4. `Effects Library > Toolbox > Video Transitions > Dissolve > Dip to Color Dissolve`
5. Arrástrala al punto de edición
6. `Inspector` `>` `Color`

**Verifica**: la pieza entra y sale sin salto.

---

## Paso 4: Tapar un jump cut con `Smooth Cut`

**Por qué**: es la transición de propósito específico de la semana, y el caso para el que existe lo
tienes casi seguro en tu pieza si has quitado muletillas de una entrevista.

Busca un corte **dentro del mismo plano** donde la persona dé un brinco. Si no tienes ninguno,
sáltate este paso y anótalo en las notas.

1. `Effects Library > Toolbox > Video Transitions > Dissolve > Smooth Cut`
2. Arrástralo al punto de edición
3. `Inspector > Duration`: bájala a **4 fotogramas**
4. Reproduce a velocidad normal, no a cámara lenta
5. Si se ve la deformación: prueba con **2 fotogramas**
6. Si sigue viéndose: ese corte no es para `Smooth Cut`. Bórralo y tápalo con un plano de recurso

**Verifica**: a velocidad normal el brinco no se ve, y la deformación tampoco.

> [!NOTE]
> `Smooth Cut` funciona bien con entrevistas sentadas y planos cortos de cabeza, con poco movimiento
> de fondo y con el sujeto casi en la misma posición a los dos lados del corte. Cuanto más se mueva
> el fondo, peor sale. Su desplegable `Mode` tiene `Better` —el de fábrica, que conserva el
> movimiento— y `Faster`. `Better` gana casi siempre.
>
> Desde la versión 20 usa un motor de `Speed Warp` con inteligencia artificial y su Inspector trae
> una casilla `Speed Warp`; desmarcarla vuelve al método anterior por flujo óptico. **Si en tu
> instalación de Free esa casilla no aparece, la transición sigue funcionando**: anótalo en las
> notas y sigue.

---

## Paso 5: Un efecto sobre un solo plano

**Por qué**: antes del adjustment clip hay que haber puesto un filtro a mano una vez, para saber
qué se está evitando.

Elige un plano que pida algo — o si ninguno lo pide, cualquiera, y lo deshaces al terminar:

1. **`Shift+Espacio`** y escribe `Gaussian`
2. Con el clip seleccionado, pulsa sobre **`Gaussian Blur`** en la lista
3. `Inspector > Effects`: ahí están sus parámetros
4. Sube la intensidad hasta pasarte, y luego baja **`Blend`** hasta donde funcione
5. Apaga y enciende el **interruptor** de la barra de título del filtro para comparar

**Verifica**: sabes dónde está la pestaña `Effects`, y sabes qué hace `Blend`.

> [!TIP]
> `Blend` lo tienen **todos** los ResolveFX, y está al final de sus parámetros. Cuando un efecto
> «funciona pero se nota demasiado», la respuesta casi nunca es rehacer sus valores: es bajar
> `Blend`.

---

## Paso 6: El adjustment clip sobre un tramo

**Por qué**: es la herramienta de la semana. Un efecto en un sitio, aplicado a todo lo que hay
debajo, y un solo sitio donde cambiar de idea.

Ve al marcador verde que marcaste como «tramo de varios planos que pide lo mismo»:

1. `Effects Library > Toolbox > Effects`
2. Arrastra **`Adjustment Clip`** a la pista **`V3`**, encima del primer plano del tramo
3. Arrastra sus bordes hasta cubrir el tramo entero. Trabaja en **`Detail Zoom`** para bordarlo al
   fotograma
4. Con el adjustment clip seleccionado, aplícale un ResolveFX de los que están en Free:
   `Gaussian Blur`, `Glow`, `Prism Blur`, `Scanlines`, `Dent`… el que resuelva lo que marcaste
5. `Inspector > Effects`, ajusta y dosifica con `Blend`
6. Ponle **nombre** en el Inspector
7. Apágalo y enciéndelo con **`D`** para comparar

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check capa-de-ajuste
```

> [!IMPORTANT]
> Comprueba **a qué está afectando de verdad**. En la `V3` afecta también a los rótulos de la `V2`.
> Si no querías eso, tienes dos salidas: bajar el adjustment clip a la `V2` y subir los rótulos a la
> `V3`, o aceptar que el efecto también toca el texto — que a veces es lo correcto, por ejemplo con
> un grano de película.

---

## Paso 7: Animar la entrada del efecto

**Por qué**: un efecto que aparece de golpe se ve como un efecto. Uno que entra progresivamente se
ve como parte de la pieza.

1. Con el adjustment clip seleccionado, `Inspector > Effects`
2. Cabezal al primer fotograma del adjustment clip. **`Blend`** a `0`, pulsa su **rombo**
3. Medio segundo después, `Blend` a `1`
4. Al final del adjustment clip, al revés
5. Reproduce

**Verifica**: el efecto entra y sale sin salto.

---

## Paso 8: Recuperar la reproducción y cerrar

**Por qué**: a estas alturas la timeline lleva transiciones, un `Smooth Cut`, filtros y quizá un
`Fusion Title`. Es normal que no vaya a tiempo real.

1. `Playback > Render Cache > Smart`
2. Deja la timeline quieta hasta que la barra de encima se ponga azul
3. Reproduce la pieza entera de principio a fin
4. Pasa a **azul** los marcadores verdes que hayas resuelto. Los que dejes en verde son trabajo
   pendiente
5. Cierra el bloque de notas:

```markdown
### Transiciones y efectos — práctica 03
- Transiciones puestas: __ · tipo y alineación de cada una: __
- ¿Alguna necesitó Trim Clips? __ · ¿cuánto se acortaron esos planos? __
- Smooth Cut: plano __ , duración __ fotogramas · ¿funcionó? __
- Efecto por clip: plano __ , efecto __ , Blend __
- Adjustment clip: pista __ , cubre __ planos, efecto __ , Blend __
- ¿Afecta a los rótulos? __ · ¿era lo que querías? __
- Transiciones que decidí NO poner, y por qué: __
```

6. `Ctrl+S` / `Cmd+S`

**Verifica**:

```bash
python scripts/verificar-semana.py 11
```

Nueve de los diez en verde. El que falta es `bin-de-titulos`, que se cierra en la práctica 04.

---

## ✅ Resultado

- [ ] Las transiciones de los marcadores verdes puestas, y ninguna más
- [ ] Cada transición con la alineación decidida a conciencia
- [ ] Fundido de entrada y de salida de la pieza
- [ ] Un `Smooth Cut` probado, o anotado por qué no había caso
- [ ] Un efecto aplicado a un solo clip, dosificado con `Blend`
- [ ] Un adjustment clip en la `V3` cubriendo un tramo, con su efecto y su nombre
- [ ] El efecto del adjustment clip entra y sale con keyframes de `Blend`
- [ ] Sabes a qué está afectando el adjustment clip y es lo que querías
- [ ] Reproducción recuperada con el render cache
- [ ] Marcadores verdes resueltos pasados a azul
- [ ] Bloque de notas de la práctica 03 cerrado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| No me deja poner la transición | No hay colas en ese punto | `Trim Clips`, o crea el solape con `Alt+Shift` / `Opt+Shift` |
| Los planos se han acortado solos | Aceptaste `Trim Clips` | `Ctrl+Z` y decide otra vez |
| `montaje-v5-sin-huecos` falla | Borraste un plano para hacer sitio | Restaura el respaldo `antes-de-rotular` |
| La transición me ha metido un fundido de audio | Usaste el atajo de vídeo y audio | `Alt+T` / `Opt+T` para vídeo solo |
| El `Smooth Cut` deforma visiblemente | Es demasiado largo, o hay mucho movimiento | 2-4 fotogramas, y si no, plano de recurso |
| El efecto se aplica al clip y no al adjustment clip | Soltaste sobre el clip de debajo | Comprueba que el adjustment clip está seleccionado antes de aplicar |
| El adjustment clip no afecta a nada | Está en la `V1`, o debajo de lo que quiere afectar | Súbelo a la `V3` |
| El adjustment clip desenfoca también los rótulos | Está por encima de ellos | Bájalo a la `V2` y sube los rótulos a la `V3` |
| El efecto se ve medio plano de más | El adjustment clip está estirado de más | Recórtalo en `Detail Zoom` |
| `capa-de-ajuste` falla | Está en la `V2` o más abajo | `V3` o superior |
| La reproducción no se recupera | El cache no ha terminado | Espera a que la barra se ponga azul |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · El título principal y los rótulos](02-el-titulo-principal-y-los-rotulos.md) | **03 · Transiciones y ResolveFX** | [04 · Compuestos y cierre](04-compuestos-y-cierre.md) |

← [Volver a la Semana 11](../README.md)
