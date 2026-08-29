# 📖 Glosario — Semana 01

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre
> paréntesis el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **Aspect ratio** (*aspect ratio*) — La proporción entre el ancho y el alto de la
  imagen. Se escribe como proporción (16:9) o como número (1.78:1). Es independiente de
  la resolución.
- **Action safe** (*action safe*) — El 90 % central del cuadro. Lo que pase dentro se
  verá en cualquier pantalla.

## B

- **Base de datos** (*database*) — Donde Resolve guarda todos sus proyectos, en lugar de
  usar un archivo por proyecto. Puede ser de disco (un usuario) o PostgreSQL (varios).

## C

- **Campo** (*field*) — Cada una de las dos mitades en que el vídeo entrelazado parte un
  frame: una con las líneas pares y otra con las impares, grabadas en instantes distintos.
- **Ciencia de color** (*color science*) — El modo en que Resolve interpreta y muestra los
  valores de tus clips. En este bootcamp, `DaVinci YRGB`.

## D

- **Desentrelazar** (*deinterlace*) — Convertir vídeo entrelazado a progresivo. Siempre
  cuesta algo: o resolución, o suavidad de movimiento.

- **DaVinci YRGB** (*DaVinci YRGB*) — El modo de ciencia de color por defecto de
  Resolve, en el que tú decides manualmente cómo se interpreta y se muestra cada cosa.
  El que usa este bootcamp.
- **Drop frame** (*drop frame timecode*) — Sistema de numeración que se salta los
  números de frame `00` y `01` al empezar cada minuto, salvo en los múltiplos de 10, para
  que el timecode cuadre con el reloj de pared en material a 29.97 fps. **No borra
  frames**: salta etiquetas.
- **DAR** (*display aspect ratio*) — La proporción de la imagen tal y como se muestra.

## E

- **Entrelazado** (*interlaced*) — Vídeo en el que cada frame se parte en dos campos
  grabados en instantes distintos. Se escribe con `i`: `1080i`, `576i`. Hoy solo aparece
  en material de archivo y en emisión de televisión.

## F

- **Frame** (*frame*) — Cada una de las imágenes fijas que componen un vídeo. La unidad
  mínima de todo: no se puede cortar, medir ni direccionar nada más pequeño.
- **Frame rate** (*frame rate*) — Cuántos frames se muestran por segundo. Se mide en fps.
- **fps** (*frames per second*) — Frames por segundo.

## J

- **Judder** (*judder*) — El movimiento entrecortado que aparece cuando el desplazamiento
  entre frames es demasiado grande para que el cerebro lo lea como continuo. No se
  arregla en post.

## L

- **Letterbox** (*letterbox*) — Barras negras arriba y abajo, cuando la imagen es más
  ancha que el contenedor donde se muestra.
- **Live Save** (*Live Save*) — La opción de Resolve que guarda el proyecto
  continuamente, sin que haya que pulsar nada.

## M

- **Media Pool** (*Media Pool*) — El almacén de clips **del proyecto**. Lo que hay ahí
  son referencias a archivos del disco, no copias.
- **Media Storage** (*Media Storage*) — El navegador de **tus discos** dentro de Resolve.
  No es lo mismo que el Media Pool.
- **Muestreo** (*sampling*) — Tomar medidas de algo continuo a intervalos regulares para
  representarlo con números. El vídeo es un muestreo del tiempo.

## N

- **NTSC** (*NTSC*) — El sistema de televisión analógica en color de América y Japón. Ya
  no existe como tecnología, pero de él vienen los frame rates de 29.97 y 23.976.

## O

- **Obturador** (*shutter*) — El mecanismo que decide cuánto tiempo entra luz por frame.
- **Offline** (*offline*) — Un clip cuyo archivo original Resolve ya no encuentra.
- **Optical Flow** (*Optical Flow*) — El método que analiza el movimiento entre frames
  para generar frames nuevos plausibles. El mejor de los tres métodos de conformado, y
  el más caro.

## P

- **PAL** (*PAL*) — El sistema de televisión analógica en color europeo. De él vienen los
  frame rates de 25 y 50.
- **PAR** (*pixel aspect ratio*) — La forma de cada píxel individual. En todo el vídeo
  moderno es 1:1 (cuadrado); en el vídeo de definición estándar, no.
- **Persistencia de la visión** (*persistence of vision*) — La explicación clásica de por
  qué vemos movimiento. Es incompleta: explica que no veamos parpadeo, no que percibamos
  movimiento.
- **Peines** (*combing*) — Las líneas horizontales alternas que aparecen en las zonas con
  movimiento al mostrar material entrelazado sin desentrelazar.
- **Pillarbox** (*pillarbox*) — Barras negras a los lados, cuando la imagen es más
  estrecha que el contenedor.
- **Progresivo** (*progressive*) — Vídeo en el que cada frame es una imagen completa. Se
  escribe con `p`: `1080p`, `720p`. Todo el vídeo moderno.
- **Píxel** (*pixel*) — Cada punto de color de la cuadrícula que forma una imagen digital.
- **Preferences** (*Preferences*) — Los ajustes que describen **tu máquina**: caché, GPU,
  idioma, guardado. Valen para todos tus proyectos.
- **Project Manager** (*Project Manager*) — La pantalla desde la que se crean y abren
  proyectos. El navegador de la base de datos.
- **Project Settings** (*Project Settings*) — Los ajustes que describen **tu vídeo**:
  frame rate, resolución, ciencia de color. Valen solo para ese proyecto y viajan con él.
- **Pulldown** (*pulldown*) — El reparto desigual de frames cuando el frame rate del
  material no encaja en el de la pantalla. Causa de tirones al reproducir.

## R

- **Record timecode** (*record timecode*) — El timecode que indica la posición dentro de
  la timeline. El que se usa para dar notas de revisión.
- **Resolución** (*resolution*) — Cuántos píxeles tiene la imagen, en columnas por filas.
- **Rolling shutter** (*rolling shutter*) — La deformación que aparece cuando el sensor
  lee la imagen línea a línea y el sujeto se mueve durante ese barrido. Verticales
  inclinadas, efecto gelatina.

## S

- **Safe areas** (*safe areas*) — Los márgenes dentro de los cuales el contenido se ve
  con seguridad en cualquier pantalla o plataforma.
- **Source timecode** (*source timecode*) — El timecode que la cámara grabó dentro del
  archivo. El que permite sincronizar varias cámaras.
- **Sobremuestreo** (*oversampling*) — Grabar a más resolución de la que se entrega. Al
  reducir, la imagen resultante es más limpia y nítida que si se hubiera grabado
  directamente a la resolución final.

## T

- **Timecode** (*timecode*) — La dirección exacta de un frame, escrita `HH:MM:SS:FF`. No
  significa nada sin saber a qué frame rate pertenece.
- **Timeline** (*timeline*) — La secuencia de montaje: las pistas con los clips colocados
  en el tiempo.
- **Title safe** (*title safe*) — El 80 % central del cuadro. Los textos de dentro se leen
  enteros en cualquier pantalla.

## U

- **UHD** (*UHD*) — 3840 × 2160 píxeles, 16:9. Lo que casi todo el mundo llama "4K". No
  es lo mismo que 4K DCI (4096 × 2160).

## V

- **Velocidad de obturación** (*shutter speed*) — Cuánto tiempo se expone cada frame,
  como fracción de segundo. A 180°, es 1 dividido entre el doble del frame rate.
- **Viewer** (*Viewer*) — El panel donde se ve la imagen. Hay uno de origen y uno de
  timeline.

## Símbolos y números

- **1000/1001** — La fracción por la que se dividen 24, 30 y 60 para obtener 23.976,
  29.97 y 59.94. Viene de un ajuste de compatibilidad de la televisión en color de 1953.
- **180°** — El ángulo de obturador estándar. Produce la cantidad de desenfoque de
  movimiento a la que el ojo está acostumbrado.
- **4K DCI** — 4096 × 2160 píxeles, 1.90:1. El 4K de cine, distinto de UHD.
- **86 400** — Los frames que hay en una hora a 24 fps. El desplazamiento de una timeline
  que empieza en `01:00:00:00`.

---

📚 Ver también el [glosario global](../../../docs/glosario-global.md) con los términos de
todo el bootcamp.

← [Volver a la Semana 01](../README.md)
