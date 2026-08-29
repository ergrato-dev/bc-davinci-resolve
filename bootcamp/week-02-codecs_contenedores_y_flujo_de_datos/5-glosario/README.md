# 📖 Glosario — Semana 02

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre
> paréntesis el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **AAC** (*Advanced Audio Coding*) — Codec de audio con pérdida. Es lo que graban los
  móviles y las cámaras de consumo dentro de un `.mp4`. Sirve para escuchar, no para
  trabajar.
- **Alfa** (*alpha channel*) — Un cuarto canal, además de rojo, verde y azul, que guarda
  la transparencia de cada píxel. Un PNG lo tiene; un JPG no. En Resolve se lee en el
  campo `Alpha mode`.
- **AVC** (*Advanced Video Coding*) — El nombre de estándar del codec que casi todo el
  mundo llama **H.264**. Son el mismo codec.

## B

- **Banding** (*banding*) — Franjas visibles donde debería haber una transición suave.
  Aparece cuando no hay suficientes tonos disponibles para el degradado, y el etalonaje lo
  empeora.
- **Bayer, patrón de** (*Bayer pattern*) — La rejilla de filtros de color sobre un sensor,
  en la que cada fotosito mide solo rojo, solo verde o solo azul.
- **Bit depth** (*bit depth*) — Ver **profundidad de bits**.
- **Bitrate** (*bit rate*) — Cuántos bits por segundo ocupa un flujo de vídeo o de audio.
  Se mide en Mbps y determina a la vez el tamaño del archivo y la velocidad de lectura que
  hace falta.
- **Blackmagic RAW** (*Blackmagic RAW*, `.braw`) — El formato RAW de Blackmagic Design: un
  archivo por toma, con parte del debayer ya hecho, que se reproduce como un codec normal y
  conserva ajustable el ISO, el balance de blancos y la curva. Funciona en Resolve Free.

## C

- **Canal alfa** — Ver **alfa**.
- **Checksum** (*checksum*) — Un número calculado a partir del contenido de un archivo. Si
  cambia un bit, cambia el número. Sirve para detectar corrupción silenciosa.
- **Chroma subsampling** (*chroma subsampling*) — Guardar menos muestras de color que de
  brillo. Se escribe `4:4:4`, `4:2:2` o `4:2:0`. Resolve no muestra este dato.
- **Codec** (*codec*, de *coder-decoder*) — El método con el que se comprimieron los datos
  de una pista. Cada pista de un archivo tiene el suyo.
- **Constant bitrate** (*constant bitrate*) — Modo de compresión de BRAW que garantiza un
  tamaño de archivo predecible. Se expresa como ratio: `3:1`, `12:1`.
- **Constant quality** (*constant quality*) — Modo de compresión de BRAW que garantiza una
  calidad constante y deja variar el tamaño. Se expresa `Q0` a `Q5`, y **`Q0` es el mejor**.
- **Contenedor** (*container*, también *wrapper*) — La estructura de archivo que guarda
  varias pistas juntas y dice cómo están ordenadas. No comprime nada.
- **Crominancia** (*chroma*) — La información de color de la imagen, separada del brillo.
- **Cuantización** (*quantization*) — Representar una magnitud continua con números
  enteros. Es la causa del banding en vídeo y del ruido de fondo en audio.

## D

- **Data Level** (*Data Level*) — El campo de Resolve que decide si un clip se interpreta
  con rango `Video` (16-235) o `Full` (0-255). Por defecto, `Auto`.
- **Debayer** (*debayer*, *demosaicing*) — El cálculo que convierte las medidas de un
  sensor de patrón Bayer en píxeles con tres canales de color.
- **DNxHR** (*DNxHR*) — Familia de codecs intra-frame de Avid, muy usada como formato
  intermedio de montaje.

## F

- **FFmpeg** (*FFmpeg*) — Herramienta libre de línea de comandos para convertir, remuxear e
  inspeccionar audio y vídeo.
- **ffprobe** (*ffprobe*) — La parte de FFmpeg que solo lee: vuelca la ficha técnica de un
  archivo sin modificarlo.
- **FFV1** (*FFV1*) — Codec de vídeo **sin pérdida** y libre. Resolve 21 lo escribe dentro
  de contenedor MKV.
- **Frame B** (*B-frame*, *bi-directional*) — Frame que guarda las diferencias respecto a
  un frame anterior **y** a uno posterior.
- **Frame I** (*I-frame*, *intra-coded*) — Frame que guarda la imagen completa y se puede
  decodificar solo.
- **Frame P** (*P-frame*, *predicted*) — Frame que guarda las diferencias respecto a un
  frame anterior.
- **Frecuencia de muestreo** (*sample rate*) — Cuántas medidas por segundo se toman de una
  onda de audio. El vídeo trabaja a **48 kHz**.
- **Full** (*full*, *data*, *extended*) — El convenio de niveles de datos en el que el
  negro es 0 y el blanco 255. Ver **Data Level**.

## G

- **GOP** (*Group of Pictures*) — Un frame I y todos los frames P y B que dependen de él,
  hasta el siguiente frame I.

## H

- **H.264** (*H.264*) — El codec de vídeo long-GOP más extendido. Es lo que graba casi
  cualquier móvil. También llamado AVC.
- **H.265** (*H.265*, *HEVC*) — El sucesor de H.264: comprime más a cambio de mucho más
  cálculo para decodificarlo.

## I

- **Intra-frame** (*intra-frame*, *all-I*) — Familia de codecs en la que cada frame se
  comprime por separado. Más pesados en disco y mucho más ágiles al montar.

## L

- **Log** (*log*, *logarithmic*) — Familia de curvas de transferencia que reparten los
  valores de forma logarítmica para conservar rango dinámico. Un clip log se ve gris y
  plano, y eso es correcto.
- **Long-GOP** (*long-GOP*, *inter-frame*) — Familia de codecs que guardan un frame
  completo cada tantos frames y el resto por diferencias. Archivos pequeños, montaje caro.
- **Lossless** — Ver **sin pérdida**.
- **LUT** (*Look-Up Table*) — Un archivo con una tabla de conversión de color: para cada
  valor de entrada, un valor de salida. La forma habitual de llevar material log a Rec.709.
- **Luminancia** (*luma*, `Y'`) — La información de brillo de la imagen, separada del
  color. Nunca se reduce en el chroma subsampling.

## M

- **Matroska** (*Matroska*, `.mkv`) — Contenedor libre y muy flexible. **DaVinci Resolve no
  lo importa**: hay que remuxear a `.mp4` o `.mov`.
- **Media Storage** (*Media Storage*) — En Preferences, la lista de discos de trabajo de tu
  máquina. Es una preferencia del ordenador, no del proyecto: no viaja con el `.drp`.
- **MediaInfo** (*MediaInfo*) — Herramienta libre que muestra la ficha técnica completa de
  un archivo, incluido el chroma subsampling que Resolve no enseña.
- **MP4** (*MPEG-4 Part 14*, `.mp4`) — El contenedor más extendido. Resolve lo identifica
  como familia `QuickTime`, porque los dos descienden del mismo estándar.
- **MXF** (*Material eXchange Format*, `.mxf`) — Contenedor profesional de broadcast.

## N

- **Niveles de datos** (*data levels*) — Los dos convenios sobre qué valor numérico es el
  negro y cuál el blanco: `Video` (16-235) y `Full` (0-255).
- **Nyquist-Shannon** (*Nyquist-Shannon sampling theorem*) — El criterio que dice que para
  reconstruir una onda hay que muestrearla a más del doble de su frecuencia más alta.

## P

- **PCM** (*Pulse-Code Modulation*, *Linear PCM*) — Audio guardado sin comprimir, muestra a
  muestra. Es lo que hay dentro de un WAV.
- **Pérdida generacional** (*generation loss*) — La degradación acumulada al recomprimir
  con pérdida una y otra vez. Se evita comprimiendo una sola vez, al final.
- **pix_fmt** (*pixel format*) — El campo de `ffprobe` que codifica chroma y bit depth a la
  vez: `yuv420p` es 4:2:0 de 8 bits.
- **Profundidad de bits** (*bit depth*) — Cuántos bits se dedican a cada canal de color, y
  por tanto cuántos tonos distintos hay. 8 bits son 256 tonos; 10 bits, 1024.
- **ProRes** (*Apple ProRes*) — Familia de codecs intra-frame de Apple, muy usada como
  formato intermedio de montaje.
- **ProRes RAW** (*ProRes RAW*) — Formato RAW de Apple que **DaVinci Resolve no abre**, ni
  en Free ni en Studio.

## Q

- **QuickTime** (*QuickTime*, `.mov`) — Contenedor de Apple, pariente del MP4. Es el valor
  que Resolve muestra en el campo `Format` para los dos.

## R

- **RAW** (*RAW*) — Un volcado de lo que midió el sensor, antes de convertirlo en imagen.
  No es un vídeo comprimido de otra forma: es material sin revelar.
- **Rec.709** (*ITU-R BT.709*) — La recomendación que define el vídeo HD: qué primarios de
  color y qué curva. Es lo que espera cualquier pantalla de consumo.
- **Remuxear** (*remux*) — Cambiar las pistas de contenedor sin recomprimirlas. Es rápido y
  **no pierde calidad**.
- **Rango dinámico** (*dynamic range*) — La distancia entre lo más oscuro y lo más brillante
  —o entre lo más suave y lo más fuerte, en audio— que se puede representar.

## S

- **SHA-256** (*SHA-256*) — La función de huella criptográfica que usa el bootcamp para
  sellar el pack de medios. Reduce cualquier archivo a 64 caracteres hexadecimales.
- **Sin pérdida** (*lossless*) — Compresión de la que se recuperan exactamente los mismos
  bits, como en un `.zip`. FFV1 y PCM lo son; H.264 y AAC no.

## T

- **Transcodificar** (*transcode*) — Descomprimir y volver a comprimir con otro codec.
  Tarda, y con codecs con pérdida degrada. No confundir con **remuxear**.

## W

- **WAV** (*WAV*) — Contenedor de audio que normalmente guarda PCM sin comprimir. El
  formato de trabajo del sonido.
- **Working Folders** (*Working Folders*) — La sección de Project Settings donde se fija
  dónde escribe este proyecto la caché y las stills de galería.

## Y

- **Y'CbCr** (*Y'CbCr*) — El espacio en el que se guarda el vídeo: `Y'` para el brillo,
  `Cb` y `Cr` para las dos componentes de color. Es lo que permite recortar el color sin
  tocar el brillo.

## Símbolos y números

- **4:2:0** — Una muestra de color por cada bloque de 2 × 2 píxeles: el 25 % de la
  información de color. Lo que graban los móviles y lo que distribuye internet.
- **4:2:2** — Una muestra de color por cada dos píxeles en horizontal: el 50 %. Cámaras
  profesionales y codecs intermedios.
- **4:4:4** — Una muestra de color por píxel: el 100 %. Gráficos, VFX y RAW revelado.
- **48 kHz** — La frecuencia de muestreo estándar de todo el vídeo profesional.
- **1000/1001** — Ver el glosario de la Semana 01.

---

📚 Ver también el [glosario global](../../../docs/glosario-global.md) con los términos de
todo el bootcamp.

← [Volver a la Semana 02](../README.md)
