# 📖 Glosario — Semana 11

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre paréntesis
> el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **`Add to Selected Edit Points`** (*Add to Selected Edit Points* / *Add to Selected Edit Points and
  Clips*) — Comando del menú contextual de una transición en la `Effects Library`. Aplica esa
  transición a todos los puntos de edición seleccionados a la vez. El manual lo nombra de las dos
  formas según el capítulo; es el mismo comando.
- **`Add Track` / `Add Tracks`** (*Add Track / Add Tracks*) — Comandos del menú contextual de la
  cabecera de una pista. El primero añade una; la pista de vídeo nueva sale **encima** de aquella
  sobre la que pulsaste. El segundo abre un diálogo para añadir varias y elegir su posición.
- **Adjustment clip** (*Adjustment Clip*) — Clip transparente de
  `Effects Library > Toolbox > Effects` cuyos efectos se aplican a **todos los clips que estén
  debajo de él**, durante el tiempo que dure. Admite ResolveFX, parámetros del Inspector, efectos de
  Fusion y etalonaje de la página Color.
- **Alineación de una transición** (*Alignment*) — Cómo se reparte una transición respecto al punto
  de edición. Tres opciones: `Start on Edit`, `Center on Edit` y `End on Edit`.
- **Alpha, canal** (*alpha channel*) — Cuarto canal que acompaña a rojo, verde y azul y que guarda
  **opacidad**, no color. A `0` el píxel es transparente y deja ver la pista de debajo; a `1` es
  opaco. Es lo que hace que un título superpuesto no tape el plano entero.
- **Anclaje del texto** (*V Anchor / H Anchor*) — A qué punto de sí mismo se ancla un bloque de
  texto: arriba, en medio o abajo; a la izquierda, en el centro o a la derecha. Cambia cómo rota y
  dónde se aplican el interlineado y el interletraje.
- **Área de acción segura** (*Action safe area*) — Rectángulo del visor dentro del cual se garantiza
  que se va a ver el movimiento y lo importante de la imagen. Se enciende en
  `View > Safe Area > Action`.
- **Área de título seguro** (*Title safe area*) — El rectángulo **interior** al de acción. Aquí
  dentro va **todo el texto**. `View > Safe Area > Title`.

## B

- **`Blend`** (*Blend*) — Parámetro que tienen **todos** los ResolveFX sin excepción, al final de sus
  parámetros. Mezcla el resultado del efecto con la imagen original: a `0` no se aplica, a `1` se
  aplica entero. Es el control de dosificación, no de carácter.

## C

- **Cola** (*handle*) — Los fotogramas que quedaron fuera al recortar un plano y que siguen en el
  archivo. Una transición se construye con ellas: sin colas no hay transición. No confundir con
  **asa** (*handle*) de una curva, que en inglés también se llama igual.
- **Compound clip** (*Compound Clip*) — Un solo clip de la timeline que por dentro contiene varios,
  de vídeo y de audio, seguidos o apilados. Se comporta como un clip: una sola transición, un solo
  juego de controles del Inspector, **un solo grado**.
- **`Convert In and Out to Compound Clip`** (*Convert In and Out to Compound Clip*) — Crear un
  compuesto con exactamente lo que hay entre `I` y `O`, incluidos trozos parciales de los clips de
  los extremos, y **todas** las pistas del rango aunque estén desactivadas.
- **Contorno** (*Outline*) — Elemento de sombreado que dibuja un borde alrededor de cada carácter.
  Es la primera herramienta contra un fondo que cambia.
- **Control de ruta** (*path control*) — El rastro de nombres de la esquina inferior izquierda de la
  timeline. Aparece al abrir un compound clip y es lo que dice si estás dentro de uno. **Dos
  nombres: estás dentro.**
- **`Create Transition Preset`** (*Create Transition Preset*) — Guardar una transición ya ajustada
  para reutilizarla. Aparece en la categoría `User` de las transiciones de vídeo.
- **Cuerpo** (*Size*) — El tamaño del texto. En `Text+` **no son puntos**: es un tamaño relativo al
  ancho de la imagen, así que no cambia al cambiar la resolución del proyecto.

## D

- **`Decompose in Place`** (*Decompose in Place*) — Deshacer un compound clip o una timeline anidada
  en la timeline, sustituyéndolo por los clips que lo formaban. Los efectos que llevaba **el
  contenedor** no se recuperan: eran suyos.
- **`Decompose Compound Clips on Edit`** (*Edit > Decompose Compound Clips on Edit*) — Modo que hace
  que al editar un compuesto desde el media pool se coloque ya deshecho en sus clips individuales,
  con cualquier método de edición salvo `Fit to Fill` y `Place on Top`.
- **`Dip to Color Dissolve`** (*Dip to Color Dissolve*) — Disolución que pasa por un color en el
  punto medio. Con el color en negro es el fundido a negro de toda la vida; el color se elige en el
  Inspector.
- **Disolución** (*dissolve*) — Transición en la que una imagen se desvanece mientras aparece la
  otra. En el lenguaje del cine indica paso de tiempo o cambio de lugar.

## E

- **`Effects Library`** (*Effects Library*) — El panel de efectos, que se abre con el botón
  `Effects` de la barra de herramientas. Tiene tres secciones: `Toolbox`, `Open FX` y `Audio FX`.
- **Elemento de sombreado** (*shading element*) — Cada una de las **ocho** capas independientes de
  pintado de un `Text+`. La 1 es el relleno y viene encendida; de la 2 a la 8 se encienden con su
  casilla `Enabled` y se les da una apariencia: relleno, contorno, sombra o borde.
- **`Extents`** (*Extents*) — Guía que dibuja el **borde exacto del cuadro**. Útil cuando las guías
  de zona segura están puestas en otra relación de aspecto.

## F

- **`Font Browser`** (*Font Browser*) — El navegador de fuentes con muestras, que se abre desde el
  icono junto al desplegable de fuente. Tiene búsqueda, favoritos y filtro por clasificación y peso.
- **`Fusion Overlay`** (*Fusion Overlay*) — Modo de overlay del visor de timeline **sin el cual no se
  puede editar el texto de un `Text+` en el visor**. Se elige en el desplegable de overlays del
  visor.
- **`Fusion Title`** (*Fusion Titles*) — Categoría de títulos que son **plantillas de Fusion**
  convertidas en macros. Traen animación hecha y exponen en el Inspector solo los controles que
  publicó su autor.

## G

- **Generador** (*generator*) — Clip que Resolve **calcula** en vez de leer de un archivo. Los de
  texto viven en `Toolbox > Titles`; los de imagen sin texto, en `Toolbox > Generators`. Su duración
  de fábrica al arrastrarlo a la timeline es de **5 segundos**, ajustable en las preferencias.

## H

- **`Hover Scrub Preview`** (*Hover Scrub Preview*) — Opción que hace que al pasar el ratón por una
  miniatura de la `Effects Library` se previsualice en el visor. Con las plantillas animadas hay que
  mover el ratón **a lo largo** de la miniatura para ver la animación.

## I

- **Interletraje** (*Tracking*) — El espacio entre caracteres, uniforme. En mayúsculas conviene
  abrirlo un poco.
- **Interlineado** (*Line Spacing*) — El espacio entre líneas de texto.

## J

- **`Join Style`** (*Join Style*) — Cómo se resuelven las esquinas de un contorno de `Text+`:
  `Sharp`, `Rounded` o `Beveled`. En cuerpos pequeños, `Rounded` sale más limpio.
- **Jump cut** (*jump cut*) — Corte dentro del mismo plano que hace que el sujeto dé un brinco. Es
  lo que produce quitar una muletilla del medio de una frase, y es el problema que resuelve
  `Smooth Cut`.

## M

- **Macro** (*macro*) — Composición de Fusion empaquetada como si fuera una sola herramienta. Su
  autor decide qué controles se publican; el resto queda dentro, funcionando, pero inaccesible desde
  la Edit page. Los `Fusion Titles` son macros.
- **`MultiText`** (*MultiText*) — Generador de título construido sobre `Text+` que añade una **lista
  de capas de texto** dentro de un solo clip, cada una con su estilo y su disposición: punto, caja
  de texto, círculo o importada de un `.csv`.

## N

- **`New Compound Clip`** (*New Compound Clip*) — Crear un compuesto a partir de los clips
  seleccionados. La copia del compuesto cae en el **bin activo** del media pool.

## O

- **`Open FX`** (*Open FX*) — La sección de la `Effects Library` donde están los **filtros**: los
  ResolveFX y los plugins OpenFX de terceros. Se subdivide en `Filters`, `Generators` y
  `Transitions`.
- **`Open in Timeline`** (*Open in Timeline*) — Abrir un compound clip o una timeline anidada para
  editar su contenido. En un compuesto aparece el **control de ruta** para volver; en una anidada,
  no, porque lo que has abierto es la timeline original.
- **`Opacity`** (*Opacity*) — Control del grupo `Composite`, en el panel `Settings`, que añade
  transparencia al clip **entero**, por encima de lo que diga su alpha. Con dos keyframes hace el
  fundido de un rótulo.
- **`Outside Only`** (*Outside Only*) — Casilla del contorno de `Text+`. Sin marcar, el contorno va
  centrado sobre el borde de la letra y se come parte del relleno, engordando la tipografía;
  marcada, se dibuja solo por fuera.

## R

- **`Render in Place`** (*Render in Place*) — Renderizar un clip con sus efectos ya incrustados a un
  **archivo nuevo** que sustituye al clip en la timeline. **No es un camino de ida**:
  `Decompose to Original` devuelve el clip original con sus efectos editables.
- **ResolveFX** (*Resolve FX*) — Los filtros que vienen con Resolve, repartidos en **quince
  categorías**: `Blur`, `Color`, `Film Emulation`, `Generate`, `Key`, `Light`, `OpenColorIO`,
  `Refine`, `Revival`, `Sharpen`, `Stylize`, `Temporal`, `Texture`, `Transform` y `Warp`. Muchos son
  de Studio, y el manual los marca `(Studio Version Only)`.
- **Rich text** (*rich text*) — Poder seleccionar un trozo del texto y darle un estilo distinto al
  del resto dentro del mismo clip. Lo soportan todos los generadores de título de Resolve **menos
  `Text+`**.

## S

- **Safe area** (*safe area*) — Rectángulo del visor, más pequeño que el cuadro, dentro del cual se
  garantiza que lo que pongas se va a ver. Todas sus opciones están en `View > Safe Area`.
- **`Scroll`** (*Scroll*) — Generador de título que sube el texto de abajo arriba. **No tiene control
  de velocidad**: la velocidad la marca la duración del clip.
- **`Set as Standard Transition`** (*Set as Standard Transition*) — Hacer que una transición sea la
  que sale con `Ctrl+T` / `Cmd+T`. Queda marcada con un indicador naranja en la `Effects Library`.
- **`Smooth Cut`** (*Smooth Cut*) — Transición de la categoría `Dissolve` diseñada para **disimular
  un jump cut**: empareja los mismos rasgos a los dos lados del corte y deforma uno hacia el otro.
  Funciona mejor entre **2 y 6 fotogramas** y con entrevistas de poco movimiento.
- **`Styled Text`** (*Styled Text*) — El campo del panel `Text` de `Text+` donde se escribe.

## T

- **`Text`** (*Text*) — Generador de título clásico. **Soporta rich text**: varios estilos dentro
  del mismo bloque. Su tamaño va en píxeles.
- **`Text+`** (*Text+*) — El generador de texto 2D de la página Fusion, disponible en la Edit page.
  **No soporta rich text**, y a cambio trae `Write On`, disposición sobre formas, animación por
  carácter, palabra y línea, y ocho elementos de sombreado. Se puede etalonar sin convertirlo en
  compound clip.
- **Timeline anidada** (*nested timeline*) — Una timeline entera editada dentro de otra. Lleva un
  distintivo propio a la izquierda de su nombre. Se diferencia de un compuesto en que **el original
  existe aparte**: si lo editas, la instancia anidada cambia, y si borras clips del original esos
  tramos **se ponen a negro**.
- **`Toolbox`** (*Toolbox*) — La sección de la `Effects Library` con lo que viene de fábrica:
  `Video Transitions`, `Audio Transitions`, `Titles`, `Generators` y `Effects`. **La carpeta
  `Effects` de aquí no son filtros**: son marcadores de posición, y ahí vive el `Adjustment Clip`.
- **Transición estándar** (*standard transition*) — La que sale con `Ctrl+T` / `Cmd+T` y con las
  opciones del menú contextual de un punto de edición. De fábrica es `Cross Dissolve` de un segundo,
  y las dos cosas se cambian.
- **`Trim Clips`** (*Trim Clips*) — Opción del diálogo que sale cuando no hay colas suficientes para
  una transición. **Acorta los dos lados del punto de edición** para crear el solape: modifica tu
  montaje.

## W

- **`Write On` / `Write Off`** (*Write On*) — Control de rango de `Text+` que hace aparecer y
  desaparecer el texto progresivamente. Se anima el **final** del rango de `1` a `0` para que
  aparezca, y el **principio** de `0` a `1` para que desaparezca.

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Glosario Semana 10](../../week-10-velocidad_transformaciones_y_estabilizacion/5-glosario/README.md) | **Glosario Semana 11** | [Glosario Semana 12](../../week-12-multicam_subtitulos_y_gestion_de_timeline/README.md) |

← [Volver a la Semana 11](../README.md) · [Glosario global](../../../docs/glosario-global.md)
