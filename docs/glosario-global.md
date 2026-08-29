# 📖 Glosario global

> Todos los términos del bootcamp en un sitio. Cada semana tiene además su propio
> glosario en `5-glosario/`, con lo que esa semana introduce.

Formato: **término en español** (*término real en la interfaz, en inglés*) — definición.

Cuando un término solo existe en inglés porque es el nombre literal de una función de
Resolve, aparece directamente en inglés. Traducirlo te desconectaría de la interfaz y
de toda la documentación del mundo.

---

## A

- **Alfa, canal** (*alpha channel*) — Un canal extra, además de rojo, verde y azul, que
  guarda la transparencia de cada píxel. Un PNG puede tenerlo; un JPG no.
- **Archivo de proyecto** (*Project Archive*, `.dra`) — Una carpeta que contiene el
  proyecto **y** una copia de todos sus medios. Es la caja de mudanza; no confundir con
  el `.drp`, que no lleva medios.
- **Aspect ratio** (*aspect ratio*) — La proporción entre el ancho y el alto de la
  imagen. 16:9 es el estándar de televisión y web; 9:16 el vertical de móvil; 2.39:1 el
  panorámico de cine.

## B

- **Barrido, obturador** — Ver *obturador*.
- **Biblioteca de proyectos** (*Project Library*) — El contenedor donde viven todos tus
  proyectos. Puede ser local, en red sobre PostgreSQL o en la nube. Hasta Resolve 17 se
  llamaba *base de datos*.
- **Bin** (*bin*) — Una carpeta dentro del media pool de Resolve. Organiza clips dentro
  del proyecto; no mueve nada en tu disco.
- **Bin activo** (*current bin*) — El bin seleccionado en el media pool. Es donde caen
  los clips que importas y los subclips que genera Scene Cut Detection.
- **Bin Master** (*Master*) — La raíz del media pool. Todo lo demás cuelga de él, y la
  regla de oficio es no dejar material suelto ahí: solo bins y timelines.
- **Bit depth** (*bit depth*) — Ver *profundidad de bits*.
- **Bitrate** (*bitrate*) — Cuántos datos por segundo ocupa un vídeo, normalmente en
  megabits por segundo (Mbps). Más bitrate, más calidad y más peso.
- **BRAW** (*Blackmagic RAW*) — El formato RAW de Blackmagic Design. Guarda los datos
  del sensor con parámetros de revelado editables después.

## C

- **Caché de render** (*render cache*) — Copias precalculadas que Resolve guarda en
  disco para que la reproducción no se atasque.
- **CacheClip** (*CacheClip*) — La carpeta que Resolve crea con ese nombre literal para
  guardar la caché de render. Se puede borrar entera: es regenerable.
- **Chroma subsampling** (*chroma subsampling*) — Guardar menos información de color
  que de luminosidad, porque el ojo nota menos la pérdida. Se escribe 4:4:4, 4:2:2 o
  4:2:0.
- **Clip** (*clip*) — Un trozo de vídeo o audio, tanto en el media pool como en la
  timeline.
- **Clone Tool** (*Clone Tool*) — El panel de la página Media que copia carpetas
  verificando cada archivo por su huella, y que admite varios destinos en un mismo
  trabajo.
- **Codec** (*codec*) — El método para comprimir y descomprimir vídeo o audio. H.264,
  ProRes y DNxHR son codecs.
- **Contenedor** (*container*) — El archivo que envuelve al vídeo, al audio y a los
  metadatos. `.mp4`, `.mov` y `.mkv` son contenedores, no codecs.
- **Corrupción silenciosa** (*silent corruption*) — Un daño en un archivo que no produce
  ningún error: tamaño y fecha correctos, se abre, se reproduce, y tiene un trozo
  destrozado. Solo la detecta una huella.

## D

- **DaVinci YRGB** (*DaVinci YRGB*) — El modo de gestión de color por defecto de
  Resolve, en el que tú decides manualmente cómo se interpreta y se muestra cada cosa.
- **dBFS** (*dBFS*) — Decibelios respecto a la escala completa digital. 0 dBFS es el
  máximo absoluto: por encima, el sonido se corta.
- **Deliver** (*Deliver*) — La página de Resolve donde se configura y se lanza el render.
- **`Description`** (*Description*) — El campo de metadata donde va prosa, para
  acordarte de lo que se ve. No confundir con `Keywords`, que son etiquetas y sí filtran.
- **DRP** (*`.drp`*) — El archivo que produce `Export Project`. Contiene el proyecto
  entero y ningún medio; pesa unos pocos megabytes.
- **Dynamic Project Switching** (*Dynamic Project Switching*) — Modo que permite tener
  varios proyectos abiertos a la vez y saltar entre ellos al instante. Consume memoria.

## E

- **Etalonaje** (*color grading*) — Dar a la imagen su aspecto final: contraste, color y
  look. Distinto de la *corrección*, que es dejarla neutra y correcta.

## F

- **Fairlight** (*Fairlight*) — La página de audio de Resolve.
- **Flag** (*Flags*) — Una marca de color sobre un clip que señala algo pendiente. Es
  temporal: se pone, se cumple y se quita. No confundir con un marcador, que se pega a
  un punto concreto dentro del clip.
- **Frame** (*frame*) — Una imagen fija de la secuencia. El vídeo es una sucesión de
  frames.
- **Frame rate** (*frame rate*) — Cuántos frames se muestran por segundo. Se mide en
  fps. 24, 25, 30, 50 y 60 son los habituales.
- **Fusion** (*Fusion*) — La página de composición y efectos por nodos.

## G

- **Galería** (*Gallery*) — El almacén de stills de la página Color. Cada still guarda un
  fotograma con su grado. No es caché: no se regenera.
- **Gamma** (*gamma*) — La curva que relaciona el valor numérico de un píxel con el
  brillo que finalmente se ve. Sin ella, las imágenes se verían mal repartidas.
- **`Good Take`** (*Good Take*) — El campo de metadata que marca la toma buena de una
  serie. Sirve como regla de smart bin.
- **Grado** (*grade*) — El conjunto de ajustes de color aplicados a un clip.

## H

- **HDR** (*High Dynamic Range*) — Formatos de imagen con más rango entre lo más oscuro
  y lo más brillante que el estándar clásico.
- **Headroom** (*headroom*) — El margen que dejas entre tu nivel de audio habitual y el
  máximo, para que un pico inesperado no sature.
- **Huella** (*checksum*, *hash*) — Un número calculado leyendo todos los bytes de un
  archivo. Un solo bit distinto la cambia entera, y por eso comprueba que una copia es
  idéntica al original. Familias habituales: `MD5`, `SHA-1`, `SHA-256`, `xxHash`.

## I

- **Importar** (*import*) — Escribir en el media pool una referencia a un archivo del
  disco. No copia nada, es instantáneo, y por eso mover la carpeta de material después
  deja los clips *offline*.
- **Ingesta** (*ingest*) — Meter el material en el sistema: copiarlo, verificarlo,
  importarlo y organizarlo.
- **Intra-frame** (*intra-frame*) — Codecs que comprimen cada frame por separado. Más
  pesados, mucho más fáciles de editar. ProRes y DNxHR son intra-frame.

## K

- **Keyword** (*Keywords*) — Una etiqueta de texto sobre un clip, escrita en el panel
  Metadata. Se busca, se filtra y alimenta los smart bins. Se escriben en minúsculas,
  sin acentos y en singular, de un vocabulario cerrado.

## L

- **Layout preset** (*Layout Preset*) — Una disposición de paneles guardada con un nombre,
  en `Workspace > Layout Presets`. Es de la máquina, no del proyecto.
- **Live Save** (*Live Save*) — Preferencia que guarda el proyecto continuamente mientras
  trabajas. Evita perder trabajo por un cierre inesperado; no permite volver atrás.
- **Log** (*log*) — Una curva de grabación que reparte la información para conservar
  más rango dinámico. El material log se ve gris y plano hasta que se etalona.
- **Long-GOP** (*long-GOP*) — Codecs que comprimen grupos de frames juntos guardando
  solo las diferencias. Muy ligeros, caros de decodificar. H.264 y H.265 lo son.
- **LUFS** (*LUFS*) — La unidad con la que se mide el volumen percibido de una mezcla.
  Es lo que usan las plataformas para normalizar el audio.
- **LUT** (*LUT, Look-Up Table*) — Una tabla que convierte unos valores de color en
  otros. Se usa para transformar espacios de color o para aplicar un look.

## M

- **Media pool** (*Media Pool*) — El almacén de clips del proyecto. Lo que ves ahí son
  referencias a archivos de tu disco, no copias.
- **Media Storage** (*Media Storage*) — La lista ordenada de carpetas de las que Resolve
  lee, en `Preferences > System`. La primera entrada es su ubicación por defecto.
- **Metadata** (*metadata*) — La información que describe un clip. La que trae el
  archivo (codec, resolución, fecha, cámara) se lee; la que escribes tú (`Description`,
  `Keywords`, `Scene`, `Shot`, `Take`) se guarda en el proyecto, no dentro del `.mp4`, y
  se pierde si quitas el clip del media pool.
- **Multicámara** (*multicam*) — Editar una escena rodada con varias cámaras a la vez,
  sincronizadas.

## N

- **Nodo** (*node*) — Cada paso del procesamiento en la página Color y en Fusion. Se
  encadenan formando un grafo.

## O

- **Obturador** (*shutter*) — Cuánto tiempo está expuesto el sensor por frame. Determina
  cuánto desenfoque de movimiento tiene la imagen.
- **Offline** (*offline*) — Un clip cuyo archivo original Resolve ya no encuentra.
  Aparece en rojo y hay que reconectarlo.
- **Optimized media** (*optimized media*) — Copias en un codec fácil de reproducir que
  Resolve genera para que la edición vaya fluida.

## P

- **Playback frame rate** (*Playback frame rate*) — A cuántos frames por segundo se
  reproduce la timeline en pantalla. No es el `Timeline frame rate`, que define la pieza.
- **PostgreSQL** (*PostgreSQL*) — Gestor de bases de datos que atiende a varios clientes a
  la vez. Es lo que hay debajo de una biblioteca de proyectos en red.
- **Power Bin** (*Power Bin*) — Un bin cuyo alcance es la biblioteca de proyectos
  entera: su contenido está disponible en todos tus proyectos. Se muestra con
  `View > Show Power Bins` y no viaja dentro del `.drp`.
- **Power window** (*Power Window*) — Una forma dibujada sobre la imagen para que una
  corrección de color afecte solo a esa zona.
- **Preferences** (*Preferences*) — Los ajustes que describen tu ordenador: GPU, memoria,
  discos, idioma, respaldos. No viajan con el proyecto.
- **Profundidad de bits** (*bit depth*) — Cuántos valores distintos puede tomar cada
  canal de color. 8 bits dan 256 niveles; 10 bits, 1024.
- **Project Manager** (*Project Manager*) — La pantalla donde se crean, organizan,
  exportan, archivan y borran proyectos.
- **Project Settings** (*Project Settings*) — Los ajustes que describen tu vídeo: frame
  rate, resolución, ciencia de color, carpetas de trabajo. Viajan con el proyecto.
- **Project.db** (*Project.db*) — El archivo SQLite donde vive un proyecto entero dentro de
  una biblioteca local. No se toca a mano nunca.
- **Proxy** (*proxy media*) — Copias en baja resolución que sustituyen a los originales
  mientras editas, y que se cambian por los buenos al renderizar.

## Q

- **Qualifier** (*Qualifier*) — La herramienta de la página Color que selecciona una
  zona de la imagen por su color, su tono o su brillo.

## R

- **RAW** (*RAW*) — Los datos del sensor casi sin procesar. Permite decidir después la
  exposición y el balance de blancos, con mucho margen.
- **Rec.709** (*Rec.709*) — El espacio de color estándar de la televisión de alta
  definición y de casi todo el vídeo web. El destino por defecto del bootcamp.
- **Referencia** (*reference*) — Una anotación de dónde está un archivo, no una copia de
  él. Es lo que guarda el media pool, y explica los clips *offline*.
- **Regenerable** — Lo que Resolve puede volver a calcular a partir del proyecto y de los
  medios: caché, medios optimizados y proxies. Borrarlo cuesta procesado, no trabajo.
- **Regla 3-2-1** — La convención de respaldo del oficio: tres copias del material, en
  dos tipos de soporte distintos, y una de ellas fuera del edificio.
- **Relink** (*relink*) — Volver a enlazar un clip *offline* con su archivo.
- **Remuxear** (*remux*) — Cambiar un archivo de contenedor sin recomprimir el vídeo:
  `ffmpeg -i entrada.mkv -c copy salida.mp4`. Es lo que hace falta con los `.mkv` de
  OBS, que Resolve no importa.
- **Render** (*render*) — Calcular y escribir el archivo final de vídeo.
- **Respaldos de proyecto** (*Project Backups*) — Las copias con fecha que Resolve hace
  solo, en tres escalones: minutos, horas y días. Permiten volver atrás en el tiempo.
- **Ripple** (*ripple*) — Editar desplazando todo lo que viene después, en lugar de
  dejar un hueco.

## S

- **Scene Cut Detection** (*Scene Cut Detection*) — La operación que busca los cortes de
  un archivo ya montado comparando cada fotograma con el anterior. Detecta bien los
  cortes secos, se le escapan los fundidos y se cree cortes los flashes. El resultado
  son subclips, no archivos nuevos.
- **Scopes** (*scopes*) — Los medidores gráficos que muestran objetivamente los valores
  de la imagen: waveform, parade, vectorscope, histograma.
- **Slip / Slide** (*slip / slide*) — Dos formas de recortar: *slip* cambia qué parte
  del clip se ve sin mover su posición; *slide* mueve el clip sin cambiar qué se ve.
- **Smart Bin** (*Smart Bin*) — Una búsqueda guardada con forma de bin: muestra los clips
  que cumplen sus reglas, sin moverlos de su bin. Sale vacío si la metadata no está
  escrita.
- **SQLite** (*SQLite*) — El formato de base de datos en un solo archivo con el que
  Resolve guarda cada proyecto. Copiarlo a mano mientras se escribe lo corrompe.
- **SRT** (*SubRip*) — El formato de archivo de subtítulos más extendido.
- **Subclip** (*subclip*) — Una referencia al mismo archivo con un punto de entrada y uno
  de salida propios. Cuarenta subclips de un archivo de 500 MB siguen ocupando 500 MB.

## T

- **Timecode** (*timecode*) — La dirección exacta de un frame, escrita
  `horas:minutos:segundos:frames`.
- **Timeline** (*timeline*) — La secuencia de montaje: las pistas con los clips
  colocados en el tiempo.
- **Timeline frame rate** (*Timeline frame rate*) — Cuántos frames por segundo tiene tu
  pieza. El único ajuste irreversible: se congela con el primer clip del media pool.
- **Trimming** (*trimming*) — Ajustar con precisión dónde empieza y dónde acaba cada
  clip en la timeline.

## V

- **Vectorscope** (*vectorscope*) — El scope circular que muestra el color de la imagen:
  el ángulo es el tono y la distancia al centro, la saturación.
- **Vista de lista** (*List View*) — La presentación del media pool con una fila por
  clip y una columna por propiedad. Es donde se compara, se ordena y se detecta el
  material que no encaja. Las columnas se eligen con clic derecho sobre su cabecera.
- **Vocabulario de keywords** — La lista cerrada de diez o quince palabras con la que se
  etiqueta, escrita antes de empezar. Sin ella aparecen variantes de la misma palabra y
  ninguna búsqueda devuelve el conjunto completo.
- **VRAM** (*VRAM*) — La memoria de la tarjeta gráfica. El recurso que Resolve agota
  antes que ningún otro.

## W

- **Waveform** (*waveform*) — El scope que muestra el brillo de la imagen a lo largo del
  ancho del cuadro.
- **Working Folders** (*Working Folders*) — El bloque de `Master Settings` que decide dónde
  escribe este proyecto su caché, sus stills y sus proxies.
- **Workspace** (*Workspace*) — El menú desde el que se muestran y ocultan paneles, se
  gestionan los layouts y se lanzan los scripts.

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
