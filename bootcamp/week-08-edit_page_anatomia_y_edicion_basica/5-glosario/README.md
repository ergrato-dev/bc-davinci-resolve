# 📖 Glosario — Semana 08

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre
> paréntesis el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **`Append to End`** (*Append to End of Timeline*) — Modo de edición que pone el clip después
  del último de la timeline, sin tocar nada. Atajo `Shift+F12`. Es el equivalente del `Append`
  de la Cut page con el que montaste la primera pasada en la Semana 06.
- **Ambiente** (*ambience* / *room tone*) — El sonido del sitio, sin voz ni efectos concretos.
  En este bootcamp es el nombre de la segunda pista de audio, donde va el sonido de los recursos.

## B

- **`Blade Edit Mode`** (*Blade Edit Mode*) — Uno de los cuatro modos de la barra de
  herramientas: cada clic sobre un clip lo corta por ahí. Es un **modo**, no una herramienta de
  usar y soltar: mientras esté activo, todos los clics cortan.

## C

- **Cabecera de pista** (*Track Header*) — La zona de la izquierda de cada pista, con sus siete
  controles: color, selector de origen y destino, bloqueo, sync lock, solo, activación y nombre.
  Manda sobre todo lo que hay en esa pista.
- **`Cinema Viewer`** (*Cinema Viewer*) — Modo que pone el visor con foco a pantalla completa,
  sin interfaz alrededor. `Workspace > Viewer Mode > Cinema Viewer`, atajo `P`.

## D

- **`Detail Zoom`** (*Detail Zoom*) — Nivel de zoom que amplía la timeline sobre el cabezal hasta
  el nivel de fotograma. Es el que se usa para colocar algo exacto y para buscar huecos.
- **Destino** (*destination*) — La pista de la timeline que va a recibir lo que edites. Se marca
  con los iconos rojos del selector de pistas de origen.
- **`.drt`** (*DaVinci Resolve Timeline file*) — Archivo que contiene una timeline y la
  información de sus clips, sin los medios. Sirve para pasar un montaje a otro proyecto que tenga
  el mismo material. Distinto del `.drp`, que es el proyecto entero.

## E

- **`Edit Index`** (*Edit Index*) — Pestaña del panel `Index` con la lista de todos los cortes de
  la timeline, con su número, pista, timecode y nombre de clip. Doble clic en una línea lleva el
  cabezal ahí.
- **Edición de tres puntos** (*three-point editing*) — La forma de editar de la Edit page: se
  marcan tres de los cuatro puntos posibles y Resolve calcula el cuarto.
- **Edición hacia atrás** (*backtiming*) — Edición definida por su **final**: se marca solo la
  salida en la timeline y el clip se coloca hacia atrás desde ahí.
- **`Empty Timeline`** (*Empty Timeline*) — Casilla del diálogo de nueva timeline, marcada por
  defecto. Si se desmarca, la timeline nace con todo el material del media pool dentro.
- **Enlace de audio y vídeo** (*Linked Selection*) — Interruptor de la barra de herramientas: con
  él activado, seleccionar la imagen de un clip selecciona también su sonido. Se salta
  puntualmente con `Alt` (Win) / `Opt` (Mac).

## F

- **`Fit to Fill`** (*Fit to Fill*) — El único modo de edición que usa los cuatro puntos y el
  único que **retima** el clip: lo acelera o lo ralentiza para que llene exactamente el rango
  marcado de la timeline. Atajo `Shift+F11`.
- **Foco** (*focus*) — Cuál de los dos visores está recibiendo las teclas en cada momento. Se
  cambia con `Q` y se reconoce por el borde resaltado.
- **`Full Extent Zoom`** (*Full Extent Zoom*) — Nivel de zoom que se ajusta solo para que quepa
  toda la timeline según crece.

## I

- **Imán** (*Snapping*) — Interruptor de la barra de herramientas, atajo `N`: los bordes de los
  clips, los marcadores y el cabezal se pegan entre sí al arrastrar. Pulsando `N` **mientras**
  arrastras se desactiva solo para ese gesto.
- **`Insert`** (*Insert*) — Modo de edición que parte lo que hay en el cabezal y empuja todo lo
  que venía detrás hacia la derecha. Alarga la pieza. Atajo `F9`.
- **`Inspector`** (*Inspector*) — Panel de la derecha con todos los ajustes del clip
  seleccionado: transformación, recorte, velocidad, audio, efectos.

## J

- **Jerarquía de pistas** (*track order*) — En vídeo manda la pista más alta: lo de arriba tapa
  lo de abajo. En audio no hay jerarquía: todas las pistas suenan sumadas.

## L

- **`Linked Selection`** — Ver **Enlace de audio y vídeo**.
- **`Lock Track`** (*Lock Track*) — Bloquea una pista: nada se puede mover, sustituir ni editar
  en ella. **La pista se sigue viendo y se sigue exportando.** No confundir con apagarla.

## M

- **Marca de previsualización** (*preview mark*) — Indicador que aparece en un visor mostrando el
  punto que Resolve va a calcular. Se puede arrastrar, y al hacerlo cambia el punto
  correspondiente del otro lado.
- **Modo de edición** (*edit mode*) — La decisión de qué le pasa al resto de la timeline cuando
  entra un clip. Hay siete: `Overwrite`, `Insert`, `Replace`, `Fit to Fill`, `Place on Top`,
  `Ripple Overwrite` y `Append to End`.

## O

- **Overlay de edición** (*edit overlay*) — Las zonas que aparecen al arrastrar un clip sobre el
  visor de timeline, una por cada modo de edición. Soltando encima de una se ejecuta ese modo.
- **`Overwrite`** (*Overwrite*) — El modo de edición por defecto: pisa lo que hubiera donde cae
  el clip nuevo y **no cambia la duración de la pieza**. Atajo `F10`.

## P

- **`Place on Top`** (*Place on Top*) — Modo de edición que sube el clip a la primera pista libre
  por encima —o por debajo, si es audio—, sin hacer caso al destino, y creando la pista si hace
  falta. Atajo `F12`.
- **`Position Lock`** (*Position Lock*) — Interruptor de la barra de herramientas que impide
  mover clips a izquierda o derecha y bloquea todas las operaciones de ripple.
- **Punto de entrada y de salida** (*In point*, *Out point*) — Los límites de un rango, marcados
  con `I` y `O`. En la Edit page hay dos juegos: los del origen y los de la timeline.

## R

- **`Replace`** (*Replace*) — Modo de edición que sustituye el clip que cruza el cabezal usando
  **su misma duración**, alineando el fotograma del cabezal del origen con el de la timeline. No
  necesita puntos marcados. Atajo `F11`.
- **`Reset Track Selectors`** (*Reset Track Selectors*) — Comando de
  `Timeline > Source Track Selector` que devuelve todos los selectores a su valor por defecto.
  Es el botón de emergencia cuando ya no sabes en qué estado están.
- **`Ripple Overwrite`** (*Ripple Overwrite*) — Modo de edición que sustituye un clip por otro de
  duración distinta y recoloca todo lo que viene detrás para que no queden huecos ni solapes.
  Atajo `Shift+F10`.

## S

- **`Selection Mode`** (*Selection Mode*) — El modo normal de la timeline: mover clips, cambiar su
  tamaño, seleccionar. Atajo `A`. Es el modo con el que se trabaja toda esta semana.
- **`Single Viewer Mode`** (*Single Viewer Mode*) — Disposición que esconde el visor de origen y
  deja uno solo, que enseña una cosa u otra según lo seleccionado.
  `Workspace > Single Viewer Mode`.
- **`Source Track Selector`** (*Source Track Selector*) — El control de la cabecera con dos
  columnas de iconos: azul el origen, rojo el destino. Decide qué componente del clip entra en
  qué pista de la timeline.
- **`Source Viewer`** (*Source Viewer*) — El visor de la izquierda: enseña un clip tal y como
  está en su archivo, con sus propios puntos de entrada y salida.
- **`Sync Lock`** (*Sync Lock*) — Control de la cabecera que decide si esa pista se desplaza
  junto con las demás cuando otra hace ripple. Activado por defecto.

## T

- **`Timeline Viewer`** (*Timeline Viewer*) — El visor de la derecha: enseña la timeline con el
  color y los compuestos de Fusion ya aplicados. Es la salida real del programa.
- **`Timeline View Options`** (*Timeline View Options*) — Desplegable del extremo izquierdo de la
  barra de herramientas: cómo se dibujan los clips, ondas de audio, altura de las pistas,
  timelines apiladas.
- **`Tracks Index`** (*Tracks*) — Pestaña del panel `Index` con todas las pistas en una lista,
  con sus controles. Más cómodo que las cabeceras cuando hay muchas pistas.

## U

- **`Use Project Settings`** (*Use Project Settings*) — Casilla del diálogo de nueva timeline: con
  ella marcada, la timeline hereda resolución, frame rate y gestión de color del proyecto.
  Desmarcarla —o pulsar `Use Custom Settings`— abre los paneles `Format`, `Monitor`, `Output` y
  `Color`.

---

## 📚 Términos de semanas anteriores que vuelven aquí

| Término | Semana | Por qué importa esta semana |
| ------- | ------ | --------------------------- |
| **Ripple** | 06 | Los modos `Insert` y `Ripple Overwrite` son ripples, y el `Sync Lock` decide a quién afectan |
| **Cola** (*handle*) | 07 | Los indicadores de primer y último fotograma del visor son colas que se acabaron |
| **Fotograma** (*frame*) | 01 | Los puntos, las duraciones y el `Detail Zoom` se cuentan en fotogramas |
| **fps** | 01 | Los 24 fps del proyecto son los que la timeline nueva debe heredar |
| **Bin** | 04 | Una timeline se guarda en el bin que esté seleccionado |
| **Metadata** | 04 | El reparto de canales de audio de un clip es lo que decide qué mandas a cada pista |
| **Proxy** | 05 | La reproducción de la Edit page usa los mismos proxies de la Semana 05 |
| **Velocidad** (*speed*) | 07 | `Fit to Fill` cambia la velocidad, y el límite del 80 % sigue valiendo |
| **A-roll y B-roll** | 07 | `Continuidad` y `Recursos` son los mismos dos papeles, ahora con nombre de pista |

---

← [Volver a la Semana 08](../README.md)
