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
- **Ángulo** (*angle*) — Cada una de las cámaras que contiene un clip multicámara. Su
  orden se fija al crearlo y es el orden en el que se seleccionan al montar.
- **`Append`** (*Append*) — La herramienta de edición de la Cut page que coloca el
  material al final de la timeline, ignorando el cabezal y sin desplazar ni sustituir nada.
- **Archivo de proyecto** (*Project Archive*, `.dra`) — Una carpeta que contiene el
  proyecto **y** una copia de todos sus medios. Es la caja de mudanza; no confundir con
  el `.drp`, que no lleva medios.
- **Aspect ratio** (*aspect ratio*) — La proporción entre el ancho y el alto de la
  imagen. 16:9 es el estándar de televisión y web; 9:16 el vertical de móvil; 2.39:1 el
  panorámico de cine.
- **`Auto Sync Audio`** (*Auto Sync Audio*) — La operación del menú contextual del media
  pool que sincroniza un clip de vídeo con uno de audio, por timecode o por forma de
  onda, sustituyendo el audio de cámara o añadiéndolo como pista extra.

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
- **Borrado con ripple** (*ripple delete*) — El borrado que quita un clip y cierra el
  hueco arrastrando hacia la izquierda todo lo que venía detrás. El borrado normal deja el
  hueco, invisible en la timeline y un parpadeo a negro en reproducción.
- **BRAW** (*Blackmagic RAW*) — El formato RAW de Blackmagic Design. Guarda los datos
  del sensor con parámetros de revelado editables después.

## C

- **Cabezal** (*playhead*) — La línea vertical que marca el fotograma que estás viendo. En
  la timeline de detalle de la Cut page no se mueve: se desplaza la timeline por debajo.
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
- **`Close Up`** (*Close Up*) — La herramienta de la Cut page que coloca el clip en la
  pista de encima con un reencuadre ampliado, para simular un plano más cerrado.
- **Codec** (*codec*) — El método para comprimir y descomprimir vídeo o audio. H.264,
  ProRes y DNxHR son codecs.
- **Colas** (*handles*) — Los fotogramas que quedan fuera de los puntos de entrada y
  salida de un subclip y que siguen existiendo en el archivo. Sin colas no hay
  transiciones ni ajustes de corte posibles: se dejan uno o dos segundos a cada lado.
- **Contenedor** (*container*) — El archivo que envuelve al vídeo, al audio y a los
  metadatos. `.mp4`, `.mov` y `.mkv` son contenedores, no codecs.
- **Corrupción silenciosa** (*silent corruption*) — Un daño en un archivo que no produce
  ningún error: tamaño y fecha correctos, se abre, se reproduce, y tiene un trozo
  destrozado. Solo la detecta una huella.
- **Cuello de botella** (*bottleneck*) — El eslabón más lento de la cadena que va del
  disco al visor. Hay tres —descompresión, disco y cálculo de efectos— y cada uno se
  arregla con una herramienta distinta.
- **Cut page** (*Cut page*) — La página dedicada a la primera pasada de un montaje: un
  visor, timeline doble, seis herramientas de edición, source tape y sync bin.

## D

- **DaVinci YRGB** (*DaVinci YRGB*) — El modo de gestión de color por defecto de
  Resolve, en el que tú decides manualmente cómo se interpreta y se muestra cada cosa.
- **dBFS** (*dBFS*) — Decibelios respecto a la escala completa digital. 0 dBFS es el
  máximo absoluto: por encima, el sonido se corta.
- **Deliver** (*Deliver*) — La página de Resolve donde se configura y se lanza el render.
- **Deriva** (*drift*) — El desfase de sincronía que crece a lo largo de un clip:
  cuadra al principio y no al final. Sale de frecuencias de muestreo distintas o de frame
  rates casi iguales (23,976 frente a 24 fps).
- **`Description`** (*Description*) — El campo de metadata donde va prosa, para
  acordarte de lo que se ve. No confundir con `Keywords`, que son etiquetas y sí filtran.
- **`Detail Zoom`** (*Detail Zoom*) — La escala corta de la vista de detalle de la timeline
  de la Cut page, la que se usa para trabajar sobre un corte concreto.
- **Doble sistema** (*dual system sound*) — Grabar la imagen en un aparato y el sonido en
  otro. Es lo normal en cuanto el micrófono bueno no está en la cámara, y es lo que
  obliga a sincronizar.
- **DRP** (*`.drp`*) — El archivo que produce `Export Project`. Contiene el proyecto
  entero y ningún medio; pesa unos pocos megabytes.
- **Dynamic Project Switching** (*Dynamic Project Switching*) — Modo que permite tener
  varios proyectos abiertos a la vez y saltar entre ellos al instante. Consume memoria.

## E

- **Etalonaje** (*color grading*) — Dar a la imagen su aspecto final: contraste, color y
  look. Distinto de la *corrección*, que es dejarla neutra y correcta.

## F

- **Fairlight** (*Fairlight*) — La página de audio de Resolve.
- **`Fast Review`** (*Fast Review*) — El control de la Cut page que recorre la timeline a
  velocidad variable, calculada por clip, para que todos ocupen un tiempo parecido en
  pantalla. Silencia el audio mientras dura.
- **Flag** (*Flags*) — Una marca de color sobre un clip que señala algo pendiente. Es
  temporal: se pone, se cumple y se quita. No confundir con un marcador, que se pega a
  un punto concreto dentro del clip.
- **Forma de onda, sincronización por** (*waveform sync*) — Alinear dos grabaciones del
  mismo momento comparando el dibujo de su sonido. No necesita preparación previa y sí
  necesita que los dos archivos tengan audio parecido.
- **Frame** (*frame*) — Una imagen fija de la secuencia. El vídeo es una sucesión de
  frames.
- **Frame rate** (*frame rate*) — Cuántos frames se muestran por segundo. Se mide en
  fps. 24, 25, 30, 50 y 60 son los habituales.
- **`Full Extent Zoom`** (*Full Extent Zoom*) — La escala completa de la timeline en la
  vista de detalle de la Cut page.
- **Fusion** (*Fusion*) — La página de composición y efectos por nodos.

## G

- **Galería** (*Gallery*) — El almacén de stills de la página Color. Cada still guarda un
  fotograma con su grado. No es caché: no se regenera.
- **Gamma** (*gamma*) — La curva que relaciona el valor numérico de un píxel con el
  brillo que finalmente se ve. Sin ella, las imágenes se verían mal repartidas.
- **`Good Take`** (*Good Take*) — El campo de metadata que marca la toma buena de una
  serie. Sirve como regla de smart bin.
- **GOP** (*Group of Pictures*) — El bloque de fotogramas que va de un fotograma
  completo al siguiente en un codec long-GOP. Dentro hay fotogramas **I** (completos),
  **P** (reconstruidos desde el anterior) y **B** (reconstruidos mirando a los dos lados).
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
- **Indicador inteligente** (*smart indicator*) — La marca de la timeline de la Cut page
  que señala dónde va a caer la próxima edición: en el corte cercano si el cabezal está
  cerca de uno, y en la posición del cabezal si no.
- **Ingesta** (*ingest*) — Meter el material en el sistema: copiarlo, verificarlo,
  importarlo y organizarlo.
- **Inserto** (*insert shot*) — Un plano de detalle colocado sobre el montaje principal:
  un objeto, un cartel, unas manos. Va en la pista de encima y no sustituye a nada.
- **Intra-frame** (*intra-frame*) — Codecs que comprimen cada frame por separado. Más
  pesados, mucho más fáciles de editar. ProRes y DNxHR son intra-frame.

## K

- **Keyword** (*Keywords*) — Una etiqueta de texto sobre un clip, escrita en el panel
  Metadata. Se busca, se filtra y alimenta los smart bins. Se escriben en minúsculas,
  sin acentos y en singular, de un vocabulario cerrado.

## L

- **Layout preset** (*Layout Preset*) — Una disposición de paneles guardada con un nombre,
  en `Workspace > Layout Presets`. Es de la máquina, no del proyecto.
- **`Link Proxy Media`** (*Link Proxy Media*) — La opción que vincula a un clip del
  media pool un archivo de proxy generado fuera de Resolve. Su inversa es
  `Unlink Proxy Media`, que rompe el vínculo sin borrar nada.
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
- **Medio optimizado** (*optimized media*) — Una copia del clip en un codec fácil de
  leer que Resolve genera y guarda en su carpeta de caché, y que sustituye al original
  mientras montas. A diferencia de un proxy, no viaja a otro equipo.
- **Metadata** (*metadata*) — La información que describe un clip. La que trae el
  archivo (codec, resolución, fecha, cámara) se lee; la que escribes tú (`Description`,
  `Keywords`, `Scene`, `Shot`, `Take`) se guarda en el proyecto, no dentro del `.mp4`, y
  se pierde si quitas el clip del media pool.
- **Montaje bruto** (*rough cut*) — La versión de una pieza que ya va de principio a fin
  pero no está acabada: cortes aproximados, sin transiciones ni títulos y con el sonido que
  trajo cada clip.
- **`Multi Source`** (*Multi Source*) — El modo del visor de origen de la Cut page que
  muestra varios clips a la vez en cuadrícula, para comparar tomas o ángulos.
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

- **Pista superior** (*upper track*) — Una pista de vídeo por encima de la principal. Lo
  que hay en ella tapa lo de abajo mientras dura; las pistas de audio, en cambio, se suman.
- **`Place on Top`** (*Place on Top*) — La herramienta de la Cut page que coloca el clip en
  la pista de vídeo inmediatamente superior, sin desplazar, sustituir ni alargar nada.
- **Plano de recurso** (*b-roll*, *cutaway*) — Un plano colocado sobre el montaje principal
  para tapar un salto o enseñar lo que se cuenta, conservando el audio de debajo.
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
- **`Proxy Handling`** (*Playback > Proxy Handling*) — El interruptor de reproducción
  que decide si Resolve prefiere los proxies, prefiere el material original o los ignora.
  Es la forma de comprobar que los proxies están funcionando.
- **Punto de corte** (*edit point*) — La junta entre dos clips consecutivos de una pista.

## Q

- **Qualifier** (*Qualifier*) — La herramienta de la página Color que selecciona una
  zona de la imagen por su color, su tono o su brillo.

## R

- **RAW** (*RAW*) — Los datos del sensor casi sin procesar. Permite decidir después la
  exposición y el balance de blancos, con mucho margen.
- **Rec.709** (*Rec.709*) — El espacio de color estándar de la televisión de alta
  definición y de casi todo el vídeo web. El destino por defecto del bootcamp.
- **Reencuadre** (*reframe*) — Ampliar digitalmente la imagen y quedarse con una parte. No
  añade detalle: usa menos superficie de la grabada, así que pierde nitidez.
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
- **`Ripple Overwrite`** (*Ripple Overwrite*) — La herramienta de la Cut page que sustituye
  el clip del destino por el material marcado y recoloca el resto sin dejar huecos.

## S

- **Salto de eje** (*jump cut*) — El corte entre dos trozos del mismo plano que produce un
  salto visible. Es el efecto secundario de acortar una entrevista, y se tapa con un plano
  de recurso.
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
- **`Smart Insert`** (*Smart Insert*) — La herramienta de la Cut page que mete el material
  en el punto de corte y desplaza hacia la derecha todo lo que venía después.
- **`Snapping`** (*Snapping*) — El imán de la timeline: hace que los clips se peguen entre
  sí y al cabezal al arrastrarlos. Se alterna con `N`.
- **`Source Clip`** (*Source Clip*) — El modo del visor de origen que muestra un solo clip.
- **`Source Overwrite`** (*Source Overwrite*) — La herramienta de la Cut page que coloca el
  ángulo elegido en la pista de encima alineado por hora de grabación. Es la del sync bin.
- **`Source Tape`** (*Source Tape*) — El modo del visor de origen que presenta todos los
  clips del bin seleccionado como una sola cinta continua. El orden de la cinta es el del bin.
- **SQLite** (*SQLite*) — El formato de base de datos en un solo archivo con el que
  Resolve guarda cada proyecto. Copiarlo a mano mientras se escribe lo corrompe.
- **SRT** (*SubRip*) — El formato de archivo de subtítulos más extendido.
- **Subclip** (*subclip*) — Una referencia al mismo archivo con un punto de entrada y uno
  de salida propios. Cuarenta subclips de un archivo de 500 MB siguen ocupando 500 MB.
- **Sync bin** (*Sync Bin*) — La vista del media pool de la Cut page que coloca el material
  por hora de grabación y muestra qué grababa cada cámara en el instante del cabezal.

## T

- **Timecode** (*timecode*) — La dirección exacta de un frame, escrita
  `horas:minutos:segundos:frames`.
- **Timeline** (*timeline*) — La secuencia de montaje: las pistas con los clips
  colocados en el tiempo.
- **Timeline doble** (*dual timeline*) — La disposición de la timeline en la Cut page: la
  pieza entera arriba a escala fija y el detalle ampliado abajo. Sustituye al zoom.
- **Timeline frame rate** (*Timeline frame rate*) — Cuántos frames por segundo tiene tu
  pieza. El único ajuste irreversible: se congela con el primer clip del media pool.
- **`Timeline Proxy Mode`** (*Timeline Proxy Mode*) — El ajuste que reduce al vuelo la
  resolución de cálculo de la timeline, sin generar ningún archivo. Es la solución
  instantánea y la de peor imagen; no sustituye a proxies ni a optimizados.
- **Trimming** (*trimming*) — Ajustar con precisión dónde empieza y dónde acaba cada
  clip en la timeline.

## V

- **Vectorscope** (*vectorscope*) — El scope circular que muestra el color de la imagen:
  el ángulo es el tono y la distancia al centro, la saturación.
- **Vínculo** (*linked selection*) — La relación que hace que el vídeo y el audio de un
  mismo clip se comporten como una sola pieza al moverlos o borrarlos.
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

## Z

- **`Zoom to Fit`** (*Zoom to Fit*) — El ajuste de la vista de detalle de la Cut page que
  encaja el conjunto en el ancho disponible.

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
