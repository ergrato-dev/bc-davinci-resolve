# 📖 Glosario — Semana 12

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre paréntesis
> el nombre real en la interfaz de Resolve, en la industria o en la norma, en inglés.

---

## A

- **`.aaf`** (*Advanced Authoring Format*) — Formato de intercambio de timeline estándar en el mundo
  Avid. Es la vía hacia **Media Composer** y hacia **Pro Tools**. Un AAF de Pro Tools llega a Resolve
  como una timeline solo de audio.
- **`Add Subtitle`** (*Add Subtitle*) — Comando del menú contextual de una pista de subtítulos. Crea
  un subtítulo que empieza en la posición del cabezal.
- **`Add Subtitle Region`** (*Add Subtitle Region*) — Comando del menú contextual del **interior** de
  una pista de subtítulos —no de su cabecera—. Parte la pista horizontalmente y crea una región
  nueva. Máximo tres por pista.
- **`Add Subtitle Track`** (*Add Subtitle Track*) — Comando del menú contextual de cualquier cabecera
  de pista. Crea una pista de subtítulos arriba del todo, llamada `Subtitle 1`.
- **`Adaptive Tracks`** (*Adaptive Tracks*) — Opción de `Multicam Audio`. Mete todas las pistas y
  canales de audio de un ángulo en una sola pista adaptativa.
- **`All Angles`** (*All Angles*) — Opción de `Multicam Audio`. Incluye en el clip multicámara
  **todas** las pistas de audio de **todos** los ángulos.
- **`Angle Name`** (*Angle Name*) — Ajuste del diálogo de creación de un clip multicámara. Decide
  cómo se llaman los ángulos: `Sequential`, `Angle`, `Camera`, `Clip Name` o `File Name`.
- **`Angle Sync`** (*Angle Sync*) — El ajuste que decide **cómo** se sincronizan los ángulos.
  Cuatro métodos: `Timecode`, `Sound`, `In or Out` y `Marker`. Se elige una sola vez, al crear el
  clip.
- **Ángulo** (*angle*) — Cada uno de los ISOs **una vez está dentro** de un clip multicámara: con su
  número, su nombre y su desplazamiento de sincronía. Un ISO es un archivo; un ángulo es un papel.
- **`Automatically set project settings`** (*Automatically set project settings*) — Casilla del
  diálogo de importación de timeline. Aplica al proyecto el tamaño de imagen y la cadencia del
  archivo importado. **Se desmarca** en un proyecto que ya tiene trabajo dentro.

## C

- **`Captions`, panel** (*Captions*) — Panel del Inspector de un subtítulo. Contiene el texto del
  subtítulo **seleccionado**, la casilla `Customize Caption` y la **lista** de todos los subtítulos
  de la pista, con su CPS.
- **CEA-608** (*CEA-608*) — Norma de *closed captions* de la televisión estadounidense, heredera del
  teletexto analógico. Resolve la incrusta en archivos **MXF OP1A** y **QuickTime**. Muchas
  especificaciones de entrega la siguen exigiendo.
- **Closed caption** (*closed caption*) — Subtítulo pensado para quien **no oye**: lleva el diálogo y
  además la información sonora —quién habla, qué se oye fuera de campo, la música—. No es lo mismo
  que un subtítulo de traducción.
- **CMX 3600** (*CMX 3600*) — El formato de EDL que soporta Resolve. Cada edición es un evento
  numerado con número de bobina, tipo de edición, timecode de origen y timecode de grabación.
- **Cola** (*handle*) — Los fotogramas de más que quedan a cada lado del trozo usado de un plano. Sin
  colas no hay transiciones ni margen de trimming. El valor por defecto de Media Management es
  **12 fotogramas** a cada lado.
- **Conmutar** (*switch*) — Cambiar el ángulo del tramo actual de un clip multicámara **sin añadir un
  corte**. `Alt`+clic en el Multicam Viewer, o `Switch Multicam Clip Angle` en la timeline.
- **`Consolidate multiple edit segments into one media file`** — Opción de Media Management. Varios
  trozos del mismo archivo original salen en **un solo archivo**, con los fotogramas de en medio.
  Ocupa más y conserva la relación clip-original que necesita el enlazado de grados.
- **Cortar y conmutar** (*cut and switch*) — Insertar un corte en el cabezal **y** cambiar de ángulo,
  todo en una operación. Clic en el Multicam Viewer, o teclas `1` a `9`.
- **CPS** (*characters per second*) — Caracteres por segundo. La medida de la velocidad de lectura de
  un subtítulo. Resolve lo pone **en rojo** cuando supera el umbral
  `Maximum Characters Per Second`.
- **`Create Multicam Clip Using Selected Clips`** (*Create Multicam Clip Using Selected Clips*) —
  Comando del menú contextual del media pool que crea un clip multicámara a partir de los clips
  seleccionados. Abre el diálogo `New Multicam Clip Properties`.
- **`Create Subtitles from Audio`** (*Create Subtitles from Audio*) — Transcripción automática del
  diálogo de una timeline a una pista de subtítulos, en `Timeline > AI Tools`. **Solo en Studio.**
- **`Create Timeline Backup`** (*Create Timeline Backup*) — Punto de respaldo con nombre propio,
  creado a mano. `Alt+Ctrl+S` (Win) / `Opt+Cmd+S` (Mac). No crea una timeline nueva en el media pool.
- **`Customize Caption`** (*Customize Caption*) — Casilla del panel `Captions`. Saca ese subtítulo
  del estilo de la pista: a partir de ahí lleva el suyo y no sigue los cambios globales.

## D

- **`Deleted Timeline Backups`** (*Deleted Timeline Backups*) — Opción del menú del media pool que
  enseña las timelines borradas y sus respaldos, para restaurarlas o eliminarlas del todo.
- **`Detect clips from same camera`** (*Detect clips from same camera*) — Casilla del diálogo de
  creación de un clip multicámara. Varios archivos identificados como de la misma cámara van al
  **mismo ángulo**. Habilita el desplegable `Detect Using`.
- **`Disable Timeline`** (*Disable Timeline*) — Desactiva una timeline. Deja de cargarse en memoria,
  desaparece de los desplegables y no se puede abrir, pero **sigue en el media pool**, con un ojo
  tachado. Mejora el rendimiento de un proyecto con muchas timelines.
- **`.drt`** (*DaVinci Resolve Timeline*) — Una timeline suelta en un archivo, para pasarla entre
  proyectos o equipos de Resolve. Lleva la timeline y la información de sus clips; **no lleva
  medios**. Una timeline por archivo.

## E

- **`.edl`** (*Edit Decision List*) — El formato de intercambio más antiguo y más universal. Lleva
  orden de clips, nombre por comentario, cortes y disolvencias, y velocidad lineal. **Una sola pista
  de vídeo.** Necesita reel name y timecode correctos.
- **`EDL to New Track`** (*Timelines > Import > EDL to New Track*) — Importar una EDL a una **pista
  nueva** de una timeline que ya existe. Es la forma de reconstruir un proyecto multipista a partir
  de una EDL por pista.
- **`Export Subtitle`** (*Export Subtitle*) — Exportar una pista de subtítulos a un archivo. Está en
  `File > Export Subtitle` y en el menú contextual de la cabecera de la pista. Por esa vía, solo
  `.srt` y `.vtt`.

## F

- **`Flatten Multicam Clip`** (*Flatten Multicam Clip*) — Convierte un clip multicámara de la timeline
  en un clip normal, eliminando todos los ángulos no usados. **Irreversible en esa timeline.**
  Pregunta qué hacer con el etalonaje: `Copying Multicam Grades` o `Retaining Grades from Angles`.
- **Forma de onda** (*waveform*) — El dibujo del sonido: los picos y valles del volumen a lo largo
  del tiempo. Es lo que compara el método de sincronía `Sound`.

## I

- **`Import Subtitle`** (*Import Subtitle*) — Comando del menú contextual del media pool para
  importar un archivo de subtítulos. Resolve admite `.srt`, `.srtx`, `.vtt`, `.xml` y `.ttml`.
- **`Insert Selected Subtitles to Timeline Using Timecode`** — Coloca un archivo de subtítulos
  importado en la timeline **respetando su timecode**, descomponiéndolo en subtítulos sueltos. Es la
  vía cuando el archivo se generó a partir de tu montaje.
- **ISO** (*isolated camera*) — Cada uno de los archivos que grabó **una** cámara en un rodaje
  multicámara. Viene del directo: la señal aislada de una cámara, frente a la mezcla del realizador.
- **ISO 639-1 / ISO 639-2** — Normas de códigos de idioma: dos letras (`es`, `en`) y tres letras
  (`spa`, `eng`). Se usan para nombrar las pistas de subtítulos.
- **ISO 3166-1** — Norma de códigos de país, dos letras en mayúsculas: `ES`, `MX`, `US`, `GB`. Se
  combina con la de idioma: `es-MX`, `en-GB`.

## J

- **Jam sync** (*jam sync*) — Poner el mismo timecode en varias cámaras antes de rodar, conectándolas
  a una fuente común. Es lo que hace viable el método de sincronía `Timecode`, y lo que no existe en
  un rodaje con móviles.

## M

- **`Media Management`** (*Media Management*) — `File > Media Management`. Copia o transcodifica los
  medios de un proyecto, unas timelines o unos clips, con la opción de quedarse solo con lo usado y
  recortarlo. Genera un `.drt` cuando trabaja sobre timelines.
- **Multicam Viewer** (*Multicam Viewer*) — El visor de origen en modo `Multicam`: enseña todos los
  ángulos del clip multicámara que cruza el cabezal, en rejilla, y cada ángulo es un botón. Rejillas
  de `1x1`, `1x2`, `2x2`, `3x3` y `4x4`.
- **`Multicam SmartSwitch`** (*Multicam SmartSwitch*) — Herramienta que analiza los ángulos y corta
  automáticamente al que considera mejor, según quién habla. **Solo en Studio.**
- **Clip multicámara** (*multicam clip*) — Elemento del media pool que contiene varios ángulos
  sincronizados y se edita como un solo clip. No tiene archivo propio en disco. Lleva un
  **distintivo** en la esquina inferior izquierda de su miniatura.

## O

- **`Open in Timeline`** (*Open in Timeline*) — Abre un clip multicámara —o un compound clip— en la
  timeline, sustituyendo su contenido. En un multicámara, enseña la **pila vertical** de ángulos, una
  pista cada uno. Se sale por el **control de ruta**.
- **`.otio` y `.otioz`** (*OpenTimelineIO*) — Formato abierto de intercambio de timelines de la
  Academy Software Foundation. `.otio` lleva solo la timeline; `.otioz` empaqueta **también los
  medios**. Es el formato que el manual recomienda como primera opción para salir de Resolve.
- **`Original Clips`** (*Original Clips*) — El bin al que Resolve mueve los ISOs si marcas
  `Move Source Clips to "Original Clips" Bin` al crear un clip multicámara. **En este bootcamp esa
  casilla se deja sin marcar.**

## R

- **Región de subtítulos** (*subtitle region*) — Cada una de las hasta **tres** capas —`R1`, `R2`,
  `R3`— de una misma pista de subtítulos. Permiten tener varios subtítulos en pantalla a la vez, cada
  uno con su posición y su estilo.
- **`Reference Audio`** (*Reference Audio*) — Opción de `Multicam Audio`. Usa **una sola** pista como
  audio de todos los ángulos. Identifica automáticamente el primer ángulo que sea solo audio.
- **`Relink to new files`** (*Relink to new files*) — Casilla de Media Management, solo con `Copy`.
  Hace que el proyecto **deje de apuntar a los originales y pase a apuntar a las copias**. Es la
  casilla que más cuidado pide.
- **`Restore Timeline Backup`** (*Restore Timeline Backup*) — Recupera un respaldo de una timeline.
  **No machaca la timeline actual**: entra en el media pool como una timeline nueva con `Backup`
  añadido al nombre.
- **Round trip** (*round trip*) — El viaje de ida y vuelta de una timeline entre dos programas. Los
  presets `Final Cut Pro Round-Trip` y `Avid AAF Round-Trip` de la página Deliver exportan el XML o el
  AAF automáticamente junto con los archivos renderizados.

## S

- **`Save Track as Preset`** (*Save Track as Preset*) — Guarda el estilo de una pista de subtítulos
  como preajuste reutilizable. Está en el menú de **tres puntos** de la esquina superior derecha del
  Inspector de subtítulos, junto con `Load`, `Update`, `Delete`, `Export` e `Import Preset`.
- **`Sound`** (*Sound*) — Método de `Angle Sync` que compara la **forma de onda** del audio de cada
  ángulo. El método por defecto de un rodaje sin timecode.
- **`Source Audio Channels`** (*Source Audio Channels*) — Opción por defecto de `Multicam Audio`. Da
  acceso a las pistas y canales individuales de cada ángulo.
- **`.srt`** (*SubRip Subtitle*) — El formato de subtítulos más extendido. Texto plano, con cuatro
  partes por bloque: número, tiempos con **coma** en los milisegundos, texto y línea en blanco.
  Tiempos **relativos al inicio del programa**, no timecode absoluto.
- **`ST1`, `ST2`, `ST3`** — El control de destino de las pistas de subtítulos, en su cabecera. Decide
  en qué pista caen los subtítulos nuevos.
- **`Switch Multicam Clip Angle`** (*Switch Multicam Clip Angle*) — Submenú del menú contextual de un
  clip multicámara en la timeline. Cambia el ángulo sin usar el Multicam Viewer.

## T

- **`Timeline Backups`** (*Timeline Backups*) — Casilla de
  `Preferences > User > Project Save and Load`. Guarda respaldos periódicos de las timelines con
  esquema abuelo-padre-hijo. Solo guarda si ha habido cambios.
- **`Track`, panel** (*Track*) — Panel del Inspector que fija el estilo de **toda** una pista de
  subtítulos: `Style and Position`, `Drop Shadow`, `Stroke`, `Background` y `Subtitle Settings`. Se
  abre seleccionando la **cabecera** de la pista.
- **`Transcode`** (*Transcode*) — Operación de Media Management que reescribe los medios en otro
  codec. La otra es `Copy`, que los duplica tal cual.

## U

- **`Use full clip extents`** (*Use full clip extents*) — Casilla del diálogo de creación de un clip
  multicámara. Cada ángulo usa su duración entera, aunque el multicámara sea más corto.

## W

- **WebVTT** (*Web Video Text Tracks*, `.vtt`) — Formato de subtítulos de la web, el que carga la
  etiqueta `<track>` de HTML5. Resolve lo importa y lo exporta.

## X

- **`.xml`** (*Final Cut Pro 7 XML* / *Final Cut Pro X XML*) — El formato de intercambio más
  extendido: lo leen Premiere Pro, Final Cut y casi todo lo demás. Los efectos que Resolve no soporta
  **se guardan escritos dentro** y reaparecen al volver al programa de origen.

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 11](../../week-11-titulos_texto_plus_efectos_y_compuestos/5-glosario/README.md) | **Glosario Semana 12** | [Semana 13](../../week-13-fairlight_anatomia_y_mezcla_base/README.md) |

← [Volver a la Semana 12](../README.md) · [Glosario global](../../../docs/glosario-global.md)
