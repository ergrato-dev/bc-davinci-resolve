# 📖 Glosario — Semana 09

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre paréntesis
> el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **Afinar** (*trimming*) — Mover los bordes de los clips que ya están montados, sin añadir ni
  quitar planos. Es la mitad del trabajo de montar, según el propio manual de Resolve.
- **`Add Marker`** (*Add Marker*) — El botón de la barra de herramientas que pone un marcador del
  color que tenga seleccionado su desplegable. Atajo `M`.
- **Asimétrico, trim** (*asymmetric trimming*) — Trim en el que se seleccionan dos cortes que se
  mueven en **sentidos contrarios**. Es la mecánica que produce un split edit. Regla: una selección
  por pista, en tantas pistas como quieras.

## B

- **Bucle** (*Loop*) — Reproducción que no para al llegar al final del tramo, sino que vuelve a
  empezar. `Ctrl+/` (Win) / `Cmd+/` (Mac). Combinada con `/` es la técnica de afinado sin parar.

## C

- **Corte en J** (*J-cut*) — Split edit en el que el **sonido del plano que entra llega antes que
  su imagen**. Sirve para anticipar: se oye el sitio nuevo antes de verlo.
- **Corte en L** (*L-cut*) — Split edit en el que el **sonido del plano que sale se prolonga bajo
  la imagen del siguiente**. Sirve para cerrar una idea sin cortar la voz.
- **Corte plano** — Corte en el que la imagen y el sonido cambian en el mismo fotograma. Es lo que
  sale de montar por tres puntos, y lo que suena mecánico si se repite en toda la pieza.

## D

- **`Dynamic Trim Mode`** (*Dynamic Trim Mode*) — Modo en el que `J`, `K` y `L` dejan de reproducir
  y pasan a trimar lo seleccionado, a cualquier velocidad. Atajo `W`. Funciona **encima** de
  `Selection Mode` o de `Trim Edit Mode`, y lo que hace depende de cuál tengas por debajo. Mientras
  está activo, el cabezal se pone **amarillo** y la barra espaciadora reproduce alrededor de la
  selección en vez de hacia delante.

## E

- **`Extend Edit`** (*Extend Edit*) — Comando que lleva los cortes seleccionados hasta la posición
  del cabezal. Atajo `E`. Redimensiona en `Selection Mode` y **ripplea** en `Trim Edit Mode`.

## F

- **`Forward Delete`** (*Forward Delete*) — La tecla que borra un clip **y cierra el hueco**. Es
  `Supr` en un teclado de Windows y `Fn+Supr` en un Mac sin bloque numérico. No confundir con
  `Supr`/`Delete` a secas, que borra dejando el hueco.

## J

- **JKL** (*JKL*) — Las tres teclas de transporte: `J` reproduce hacia atrás, `K` para, `L` hacia
  delante. Pulsarlas repetidamente acelera; `K` mantenida con `J` o `L` da cámara lenta; `K`
  pulsada con toques da fotograma a fotograma.

## M

- **Marcador** (*marker*) — Nota clavada en un fotograma. Tiene seis campos: `Time`, `Duration`,
  `Name`, `Notes`, `Color` y `Keyword`.
- **Marcador con duración** (*marker with duration*) — Marcador que cubre un tramo en vez de un
  fotograma. Se crea con `I`, `O` y `Convert In and Out to Duration Marker`, o arrastrando con
  `Alt` (Win) / `Opt` (Mac).
- **Marcador de clip** (*clip marker*) — El que se pone con un clip **seleccionado**. Vive en la
  barra de título del clip y **viaja con él** si lo mueves.
- **Marcador de timeline** (*timeline marker*) — El que se pone con **nada seleccionado**. Vive en
  la regla de tiempo y se queda donde está aunque muevas los clips.
- **`Marker Index`** (*Markers*) — Pestaña del panel `Index` con todos los marcadores de la
  timeline en una lista. Los campos `Name`, `Notes` y `Keyword` se editan directamente sobre la
  fila.

## P

- **`Play Around Selection`** (*Play around selection*) — Reproduce un tramo desde unos segundos
  antes hasta unos segundos después de lo que tengas seleccionado. Atajo `/`. El pre-roll y el
  post-roll se ajustan en `Preferences > User > Editing`.
- **Precisión, editor de trim de** (*Precision Trim Editor*) — Vista que sustituye al visor de
  origen al hacer doble clic sobre un corte: dos tiras de fotogramas, el plano que sale arriba y el
  que entra abajo, con números que dicen cuántos fotogramas estás moviendo.

## Q

- **`Quick Trim`** (*Quick Trim*) — Trimar reproduciendo sin cambiar de modo, manteniendo `Ctrl`
  (Win) / `Cmd` (Mac) mientras pulsas `J` o `L`. Solo funciona a velocidad real o más rápido.

## R

- **`Resize`** (*Resize*) — Alargar o acortar el borde de un clip dejando un hueco o pisando al
  vecino. Es la operación más simple, y la que menos se usa cuando ya hay una pieza montada.
- **`Ripple`** (*Ripple*) — Acortar o alargar un clip **desplazando todo lo que viene detrás** para
  que no queden huecos ni solapes. Es la única operación de la semana que cambia la duración de la
  pieza y la única que puede desincronizar tramos enteros.
- **`Ripple Timeline Markers`** (*Ripple Timeline Markers*) — Opción del menú `Timeline`: con ella
  activada, los marcadores que estén a la derecha de un ripple se desplazan con el resto de la
  timeline.
- **`Roll`** (*Roll*) — Mover el corte entre dos clips alargando uno exactamente lo que se acorta
  el otro. **No cambia la duración de la pieza** y funciona igual en los dos modos.

## S

- **`Slide`** (*Slide*) — Mover un clip por la timeline conservando su contenido, ajustando la
  salida del vecino de la izquierda y la entrada del de la derecha. Gasta cola **de los vecinos**.
- **`Slip`** (*Slip*) — Cambiar el tramo de material que enseña un clip **sin moverlo ni cambiar su
  duración**. Gasta cola **del propio clip**.
- **Split edit** (*split edit*) — Corte en el que la imagen y el sonido no cambian en el mismo
  fotograma. Se llama corte en L o corte en J según cuál de los dos se adelante.
- **`Sync Lock`** (*Sync Lock*) — Control de la cabecera de pista, a la derecha del candado, que
  decide si esa pista **se desplaza junto con las demás** cuando otra hace ripple. Activado de
  fábrica en todas.

## T

- **`Trim Edit Mode`** (*Trim Edit Mode*) — Modo en el que arrastrar un borde ripplea, arrastrar el
  cuerpo de un clip lo desliza y arrastrar un rectángulo selecciona **cortes** en vez de clips.
  Atajo `T`.
- **`Trim End`** (*Trim End*) — Comando que lleva la salida de todos los clips que cruzan el cabezal
  hasta el cabezal. Atajo `Shift+]`. Redimensiona en `Selection Mode` y ripplea en `Trim Edit Mode`.
- **`Trim Start`** (*Trim Start*) — Lo mismo con la entrada. Atajo `Shift+[`.

## V

- **Visor partido en cuatro** (*four-up display*) — Los cuatro cuadros que aparecen al hacer `Slip`
  o `Slide`. En un `Slip` se actualizan los dos de arriba; en un `Slide`, los dos de abajo.
- **Visor partido en dos** (*two-up display*) — Los dos cuadros que aparecen al hacer `Roll` o
  `Ripple`: el último fotograma del plano que sale y el primero del que entra. Se apaga
  temporalmente con `Shift` y del todo en `View > Enable Multiview Edit Preview`.

---

## 📚 Términos de semanas anteriores que vuelven aquí

| Término | Semana | Por qué importa esta semana |
| ------- | ------ | --------------------------- |
| **Cola** (*handle*) | 07 | Es el recurso que gastan las cinco operaciones. Sin cola, Resolve frena y parece un fallo |
| **Ripple** | 06 | Aquí deja de ser un concepto y pasa a ser la operación que más se usa |
| **Cabecera de pista** (*Track Header*) | 08 | El `Sync Lock` vive ahí, junto al candado y al selector de pista |
| **Selector de pista** (*Source Track Selector*) | 08 | Decide sobre qué clips actúan `Trim Start`, `Trim End` y `Extend Edit` |
| **`Linked Selection`** | 08 | Hay que saltárselo puntualmente para hacer un split edit |
| **Imán** (*Snapping*) | 08 | Estorba al separar imagen y sonido, y ayuda a medir con marcadores |
| **`Detail Zoom`** | 08 | Es como se buscan los huecos de dos fotogramas |
| **`Edit Index`** | 08 | Sirve para encontrar cortes por su timecode y para exportar la lista de marcadores |
| **Keyword** | 04 | Los marcadores aceptan palabras clave igual que los clips |
| **Subclip** | 05 | La otra forma de guardar un rango de un clip, frente al marcador con duración |

---

← [Volver a la Semana 09](../README.md)
