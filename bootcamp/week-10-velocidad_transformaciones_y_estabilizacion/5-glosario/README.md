# 📖 Glosario — Semana 10

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre paréntesis
> el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **Anclaje, punto de** (*Anchor Point*) — La coordenada de la imagen alrededor de la cual se
  aplican el zoom y la rotación. De fábrica, el centro. Moverlo antes de ampliar es cómo se amplía
  hacia un punto concreto del cuadro.
- **Asa** (*handle*) — En una curva, el tirador que sale de un punto de control y estira la curva a
  su lado. Alargarla suaviza la aceleración; acortarla la endurece. No confundir con la **cola** de
  un plano, que en inglés también se llama *handle*.
- **Asa de arriba / asa de abajo** — Los dos tiradores de un punto de velocidad en los
  `Retime Controls`. La de arriba cambia **la velocidad** del tramo de su izquierda; la de abajo,
  **qué trozo de plano** ocupa ese tramo.

## B

- **Bézier, curva** (*Bezier curve*) — Curva definida por sus extremos y por las asas de sus puntos
  de control. Es la forma en la que se controla la aceleración de una animación en el
  `Curve Editor`.
- **Blanking** (*blanking*) — El vacío que entra por un borde cuando la imagen se desplaza. Lo
  produce la estabilización, y la casilla `Zoom` lo tapa ampliando.

## C

- **Cadencia de proyecto** (*Timeline frame rate*) — Cuántos fotogramas por segundo reproduce tu
  timeline. En este bootcamp, 24. Se lee en
  `File > Project Settings > Master Settings > Timeline frame rate`.
- **Cadencia de rodaje** (*FPS*) — Cuántos fotogramas por segundo grabó la cámara. Se lee en la
  columna `FPS` del media pool en vista de lista. Es el otro número del techo.
- **`Camera Lock`** (*Camera Lock*) — Casilla del grupo `Stabilization` que desactiva
  `Cropping Ratio` y `Smooth` y busca eliminar **todo** el movimiento de cámara, para dejar el
  plano clavado.
- **`Change Clip Speed`** (*Change Clip Speed*) — El diálogo de velocidad lineal, en el menú
  `Clip`. Sus casillas: `Ripple Sequence`, `Reverse Speed`, `Freeze Frame`, `Pitch Correction` y
  los botones `Maintain Timing` / `Stretch to fit`.
- **`Cropping Ratio`** (*Cropping Ratio*) — Control del estabilizador que decide cuánto se esfuerza:
  **1,0 no estabiliza nada** y valores más bajos son más agresivos, a cambio de más ampliación.
  Cambiarlo obliga a volver a pulsar `Stabilize`.
- **`Curve Editor`** (*Curve Editor*) — El gráfico donde se editan los keyframes por valor y por
  aceleración. Se abre desde el icono de curvas del `Keyframe Editor`. Es donde viven también las
  dos curvas de retime.

## D

- **Distintivo de retime** (*retime badge*) — La marca que aparece a la izquierda del nombre de un
  clip con la velocidad cambiada. Es la única señal permanente: el porcentaje solo se ve con los
  `Retime Controls` abiertos.
- **`Dynamic Zoom`** (*Dynamic Zoom*) — Grupo del Inspector, desactivado de fábrica, que anima un
  movimiento de un encuadre a otro dentro del mismo plano. En el visor se maneja con un recuadro
  verde de inicio y uno rojo de final. Sus dos controles son `Dynamic Zoom Ease` y `Swap`.

## E

- **Easing** (*ease*) — Que una animación acelere y decelere en vez de ir a velocidad constante.
  `Ease In`, `Ease Out` y `Ease In and Out` son las tres formas, frente a `Linear`, que no suaviza
  nada.
- **Estabilización** (*Stabilization*) — Reencuadrar un plano fotograma a fotograma para cancelar
  el movimiento de la cámara. En la Edit page vive en `Inspector > Video > Stabilization` y son los
  mismos controles que la paleta `Tracker` de la Color page, menos el gráfico.

## F

- **`Fit to Fill`** (*Fit to Fill*) — Tipo de edición que retima el clip para que llene exactamente
  un rango de la timeline. Es el único que usa los cuatro puntos de edición, y **no ripplea**.
  Atajo `Shift+F11`.
- **Fotograma congelado** (*freeze frame*) — Un clip convertido en una sola imagen: la del
  fotograma que había bajo el cabezal. `Clip > Freeze Frame`, atajo `Shift+R`.
- **`Frame Blend`** (*Frame Blend*) — Método de relleno que funde dos fotogramas contiguos para
  inventar el intermedio. Su defecto típico es el *ghosting*. Es la elección correcta con agua,
  humo, cruces y ruido.
- **`Frame Interpolation`** (*Frame Interpolation*) — El grupo de `Project Settings > Master
  Settings` donde se fija el `Retime Process` de todo el proyecto, con `Motion estimation mode` y
  `Motion range`.

## G

- **Ghosting** (*ghosting*) — Artefacto de doble imagen fantasmal, típico de `Frame Blend`: se ven
  dos posiciones a la vez de lo que se mueve.

## J

- **Judder** (*judder*) — Artefacto de avance a tirones, típico de `Nearest` y de cualquier
  ralentización por debajo del techo del plano: la imagen se mueve como una presentación de
  diapositivas.

## K

- **Keyframe** (*keyframe*) — Marca que fija el valor de un parámetro en un fotograma concreto. Dos
  keyframes con valores distintos son una animación; Resolve calcula los intermedios.
- **`Keyframe Editor`** (*Keyframe Editor*) — Panel con una pista por parámetro animable del clip
  seleccionado, agrupadas por categoría. Se abre desde la pestaña `Keyframes`. Sirve para ver y
  mover keyframes en el tiempo.
- **`Keyframe Tray`** (*Show Keyframe Tray*) — La versión reducida del `Keyframe Editor`, que se
  despliega bajo el clip desde un botón de la barra de la timeline.

## L

- **`Lens Correction`** (*Lens Correction*) — Grupo del Inspector con `Analyze` y `Distortion`,
  para corregir la deformación de un gran angular. **Solo existe en DaVinci Resolve Studio.**

## M

- **`Maintain Timing` / `Stretch to fit`** (*Maintain Timing / Stretch to fit*) — Los dos botones de
  radio del diálogo de velocidad que deciden qué pasa con los keyframes que ya hubiera dentro del
  clip: se quedan en su fotograma, o se estiran con él.
- **`Motion estimation mode`** (*Motion estimation mode*) — Cuánto esfuerzo dedica `Optical Flow` al
  análisis: `Standard Faster`, `Standard Better`, `Enhanced Faster`, `Enhanced Better`, y las
  opciones `Speed Warp`, que necesitan Studio.
- **`Motion range`** (*Motion range*) — `Small`, `Medium` o `Large`, según cuánto se mueven las
  cosas entre fotograma y fotograma. Ayuda al análisis a acertar.

## N

- **`Nearest`** (*Nearest*) — El método de relleno más simple: repite el fotograma anterior o tira
  los que sobran. Su defecto es el *judder*. Sirve para fondos desenfocados y retimes mínimos.

## O

- **`Optical Flow`** (*Optical Flow*) — Método de relleno que estima el movimiento entre dos
  fotogramas y **dibuja** el intermedio. El de más calidad y el más caro. Su defecto es el
  *warping*, y aparece con movimiento caótico.
- **Overcranking** (*overcranking*) — Grabar a más fotogramas por segundo de los que se van a
  reproducir, para poder ralentizar después. En español, sobrecadenciar.

## P

- **`Pitch`** (*Pitch*) — Parámetro de `Transform` que inclina la imagen hacia delante o hacia
  atrás sobre un eje horizontal. No confundir con `Pitch Correction`, que es del audio.
- **`Pitch Correction`** (*Pitch Correction*) — Casilla que corrige el tono del audio retimado para
  que no suene grave o agudo.
- **Punto de velocidad** (*speed point*) — Marca vertical dentro de un clip que separa dos tramos
  con velocidades distintas. Hacen falta dos como mínimo para que haya efecto.

## R

- **Rampa de velocidad** (*speed ramp*) — Efecto en el que un plano cambia de velocidad de forma
  progresiva. `Speed Ramp` es además el preset que coloca cinco tramos al 10, 30, 50, 70 y 90 %.
- **Reverse** (*Reverse Speed*, *Reverse Segment*) — Reproducir hacia atrás. El clip entero con la
  casilla `Reverse Speed`; un tramo, con `Reverse Segment` en su desplegable.
- **`Retime and Scaling`** (*Retime and Scaling*) — Grupo del Inspector con los ajustes de retime y
  escalado **de ese clip**: `Retime Process`, `Motion estimation mode`, `Scaling` y `Resize Filter`.
- **`Retime Controls`** (*Retime Controls*) — El recuadro que aparece sobre un clip con
  `Ctrl+R` / `Cmd+R` y permite la velocidad variable. Se cierra con `Esc` sin deshacer nada.
- **`Retime Frame`, curva** (*Retime Frame curve*) — Gráfico de correspondencia: fotogramas del
  origen en vertical, de la timeline en horizontal. Tendido es lento, empinado es rápido,
  horizontal es congelado y descendente es reverse.
- **`Retime Process`** (*Retime Process*) — El ajuste que decide el método de relleno: `Nearest`,
  `Frame Blend` u `Optical Flow`. Está en el proyecto y en cada clip; de fábrica el clip pone
  `Project Settings`, que significa «hereda».
- **`Retime Speed`, curva** (*Retime Speed curve*) — Gráfico de velocidad: una línea plana al
  100 %. Se arrastran **los tramos**, no los puntos, y **no puede crear reverse**.
- **`Rewind`** (*Rewind*) — Preset que añade dos puntos de velocidad para que el tramo se reproduzca
  hacia atrás a toda velocidad y luego se repita.
- **`Ripple Sequence`** (*Ripple Sequence*) — La casilla que decide si el cambio de velocidad
  recoloca todo lo que viene detrás o pisa al vecino. Está en el diálogo de velocidad, en el
  Inspector, y en `Paste Attributes` y `Remove Attributes`.

## S

- **`Smooth`** (*Smooth*) — Control del estabilizador que **suaviza** el movimiento en vez de
  eliminarlo. Es el que conserva una panorámica quitándole el temblor. Cambiarlo obliga a
  reanalizar.
- **`Speed Change`** (*Speed Change*) — El grupo de velocidad del Inspector de vídeo, disponible en
  la Cut page y en la Edit page. Sus valores `Speed %` y `Frames Per Second` aceptan keyframes.
- **`Speed Warp`** (*Speed Warp*) — Opción de `Motion estimation mode` que usa el DaVinci Neural
  Engine para cámara lenta de más calidad. **Necesita Studio.** En Free, `Enhanced Better`.
- **`Stabilize`** (*Stabilize*) — El botón que lanza el análisis. Hay que volver a pulsarlo después
  de cambiar el modo, `Cropping Ratio` o `Smooth`.
- **`Strength`** (*Strength*) — Multiplicador del resultado de la estabilización: `1` es máxima,
  `0` la desactiva. **No obliga a reanalizar**, y por eso es el mando de afinado.
- **`Swap`** (*Swap*) — Botón de `Dynamic Zoom` que intercambia el encuadre de inicio y el de final.

## T

- **Techo de cámara lenta** — El porcentaje mínimo al que se puede ralentizar un plano sin que
  falten fotogramas. `cadencia de proyecto ÷ cadencia de rodaje × 100`.
- **`Transform`** (*Transform*) — El grupo del Inspector con `Zoom`, `Position`, `Rotation Angle`,
  `Anchor Point`, `Pitch`, `Yaw` y los dos `Flip`. Son los mismos parámetros que el modo
  `Edit Sizing` de la paleta `Sizing` de la Color page, y son **independientes** de los de
  `Input Sizing`.

## V

- **Velocidad lineal** — Una sola velocidad para todo el clip. Retima el audio con el vídeo.
- **Velocidad variable** — Varias velocidades dentro del mismo clip. **Silencia el audio del clip
  entero**, sin excepción.

## W

- **Warping** (*warping*) — Artefacto de `Optical Flow`: los bordes de lo que se mueve se derriten
  o se doblan, porque el análisis calculó mal hacia dónde iba.

## Y

- **`Yaw`** (*Yaw*) — Parámetro de `Transform` que inclina la imagen a izquierda o derecha sobre un
  eje vertical.

## Z

- **`Zoom` (estabilización)** (*Zoom*) — La casilla que amplía la imagen lo justo para que el
  blanking quede fuera de cuadro. Activada de fábrica.
- **`Zoom X` / `Zoom Y`** (*Zoom X / Y*) — Los parámetros de ampliación de `Transform`. Van
  enlazados de fábrica; al soltar el enlace se puede estirar o achatar la imagen.

---

## 📚 Términos de semanas anteriores que vuelven aquí

| Término | Semana | Por qué importa esta semana |
| ------- | ------ | --------------------------- |
| **Frame rate** | 01 | Es la mitad de la división que da el techo de cámara lenta |
| **Obturador** (*shutter*) | 01 | El movimiento borroso grabado baja el techo real y arruina un freeze |
| **Resolución** | 01 | Es el margen que se reparten la estabilización y el reencuadre |
| **Render cache** | 05 | Es lo que devuelve la reproducción fluida después de retimar |
| **Cambio de velocidad en Cut** | 07 | El mismo panel `Speed Change`, visto desde la otra página |
| **Ripple** | 09 | Lo que hace la casilla `Ripple Sequence` |
| **Bucle de reproducción** | 09 | `Ctrl+/` y `/`: es como se juzga un retime sin parar |
| **Marcador y `Marker Index`** | 09 | El mapa de velocidad de la práctica 01 y los checks de la semana |
| **`Forward Delete`** | 09 | Cierra los huecos que dejan los retimes sin ripple |
| **Cabecera de pista** | 08 | Donde se comprueba que un ripple no ha descolocado las pistas de encima |

---

← [Volver a la Semana 10](../README.md)
