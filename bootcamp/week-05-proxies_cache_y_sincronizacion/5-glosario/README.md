# 📖 Glosario — Semana 05

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre
> paréntesis el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **Ángulo** (*angle*) — Cada una de las cámaras que contiene un clip multicámara. Su
  orden se fija al crear el clip y es el orden en el que se seleccionan al montar.
- **`Auto Sync Audio`** (*Auto Sync Audio*) — La operación del menú contextual del media
  pool que sincroniza automáticamente un clip de vídeo con uno de audio, por timecode o
  por forma de onda, y que permite elegir entre sustituir el audio de cámara o añadir el
  nuevo como pista extra.

## C

- **Caché de render** (*render cache*) — Los archivos donde Resolve guarda el resultado ya
  calculado de un tramo de la timeline, con sus efectos aplicados, para no recalcularlo en
  cada reproducción. Se invalida sola cuando cambias algo de ese tramo.
- **Colas** (*handles*) — Los fotogramas que quedan fuera de los puntos de entrada y salida
  de un subclip y que siguen existiendo en el archivo. Sin colas no se pueden hacer
  transiciones ni ajustar cortes más tarde. Se dejan uno o dos segundos a cada lado.
- **Cuello de botella** (*bottleneck*) — El eslabón más lento de la cadena que va del disco
  al visor. Hay tres: descompresión del codec, lectura de disco y cálculo de efectos, y
  cada uno se arregla con una herramienta distinta.

## D

- **Deriva** (*drift*) — El desfase que crece a lo largo de un clip: cuadra al principio y
  no al final. Sale de frecuencias de muestreo distintas (44,1 frente a 48 kHz) o de frame
  rates casi iguales (23,976 frente a 24 fps). Con material ya grabado se salva partiendo
  la escena en subclips.
- **Doble sistema** (*dual system sound*) — Grabar la imagen en un aparato y el sonido en
  otro. Es lo normal en cuanto el micrófono bueno no está en la cámara, y es lo que obliga
  a sincronizar.

## F

- **Forma de onda** (*waveform*) — El dibujo del sonido a lo largo del tiempo, con sus
  picos y sus valles. Dos grabaciones del mismo momento dibujan siluetas parecidas aunque
  suenen distinto, y de ahí sale la sincronización por forma de onda.

## G

- **GOP** (*Group of Pictures*) — El bloque de fotogramas que va de un fotograma completo
  al siguiente en un codec long-GOP. Dentro hay fotogramas **I** (completos), **P**
  (reconstruidos desde el anterior) y **B** (reconstruidos mirando al anterior y al
  siguiente).

## I

- **Intra-frame** (*intra-frame*, *all-intra*) — La familia de codecs que guarda cada
  fotograma completo y por separado. Ocupa mucho más que un long-GOP y se descomprime casi
  sin coste, que es por lo que se usa para optimizados, proxies y caché. DNxHR y ProRes
  son los ejemplos habituales.

## L

- **`Link Proxy Media`** (*Link Proxy Media*) — La opción que vincula a un clip del media
  pool un archivo de proxy generado fuera de Resolve. Su inversa es `Unlink Proxy Media`,
  que rompe el vínculo sin borrar nada.
- **Long-GOP** (*long-GOP*) — La familia de codecs que guarda un fotograma completo cada
  cierto tiempo y solo las diferencias entre medias. Ocupa muy poco y se descomprime caro.
  H.264 y H.265 son long-GOP: es lo que graban los móviles, las cámaras de consumo y OBS.

## M

- **`Media Offline`** (*Media Offline*) — El rótulo rojo que muestra el visor cuando la
  ruta guardada en el proyecto ya no apunta a ningún archivo. No significa pérdida de
  trabajo: los cortes, los grados y la metadata siguen en el proyecto.
- **Medio optimizado** (*optimized media*) — Una copia del clip en un codec fácil de leer
  que Resolve genera y guarda en su carpeta de caché, y que sustituye al original mientras
  montas. No viaja a otro equipo.
- **Multicámara, clip** (*multicam clip*) — Un solo elemento del media pool que contiene
  varios ángulos ya sincronizados entre sí, con un ángulo activo y una fuente de audio.
  No confundir con un compound clip, que apila elementos en vez de guardar alternativas.

## P

- **`Playback > Proxy Handling`** — El interruptor de reproducción que decide si Resolve
  prefiere los proxies, prefiere el material original o los ignora por completo.
- **`Playback > Render Cache`** — El menú con los tres modos de caché: `None`, `Smart`
  —Resolve decide qué cachear— y `User` —cacheas solo lo que marcas—.
- **`Playback > Use Optimized Media if Available`** — El interruptor que decide si la
  reproducción usa los medios optimizados generados. Es la forma de comprobar que están
  funcionando.
- **Proxy** (*proxy*) — Una copia del clip en un codec fácil y resolución menor, guardada
  en una carpeta que eliges tú y vinculada al clip del media pool. Se puede generar fuera
  de Resolve y **viaja a otro equipo**, que es su motivo de existir.

## R

- **`Relink`** (*Relink*) — La operación que vuelve a enlazar clips offline con sus
  archivos. Busca **por nombre de archivo** dentro de la carpeta que le señalas: por eso
  mover una carpeta se arregla en una pasada y renombrar archivos no.

## S

- **Sincronizar** (*sync*) — Alinear al fotograma la imagen de un aparato con el sonido de
  otro. Se hace en el media pool antes de montar, nunca arrastrando en la timeline.
- **Subclip** (*subclip*) — Una referencia al mismo archivo con un punto de entrada y uno
  de salida propios. No ocupa espacio, se crea al instante y tiene su propia metadata. Los
  produce también Scene Cut Detection, de la Semana 04.

## T

- **`Timeline Proxy Mode`** (*Timeline Proxy Mode*) — El ajuste de reproducción que reduce
  al vuelo la resolución de cálculo de la timeline, a la mitad o a un cuarto, sin generar
  ningún archivo. Es la solución instantánea y la de peor imagen; no sustituye a proxies ni
  a optimizados.
- **Timecode** (*timecode*) — La marca de tiempo `HH:MM:SS:FF` que un aparato escribe al
  grabar. Sincroniza sin mirar el sonido, siempre que los relojes se igualaran antes de
  empezar. Se introdujo en la Semana 01.

## W

- **Working Folder** (*Working Folder*, *Cache Files Location*) — La carpeta donde Resolve
  escribe la caché de render, los medios optimizados y los proxies que genera. No contiene
  nada irreemplazable: borrarla cuesta tiempo de regeneración, nunca trabajo.

---

## 📚 Ver también

- [`docs/glosario-global.md`](../../../docs/glosario-global.md) — el glosario acumulado de
  todo el bootcamp, con los términos de las semanas anteriores.
- [Glosario de la Semana 04](../../week-04-media_page_ingesta_y_organizacion/5-glosario/README.md) —
  bins, smart bins, metadata, keywords, referencias y subclips.
- [Glosario de la Semana 02](../../week-02-codecs_contenedores_y_flujo_de_datos/5-glosario/README.md) —
  contenedores, codecs, bitrate, chroma y bit depth, de donde sale medio vocabulario de
  esta semana.

---

← [Volver a la Semana 05](../README.md)
