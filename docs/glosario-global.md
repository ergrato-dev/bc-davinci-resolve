# 📖 Glosario global

> Todos los términos del bootcamp en un sitio. Cada semana tiene además su propio
> glosario en `5-glosario/`, con lo que esa semana introduce.

Formato: **término en español** (*término real en la interfaz, en inglés*) — definición.

Cuando un término solo existe en inglés porque es el nombre literal de una función de
Resolve, aparece directamente en inglés. Traducirlo te desconectaría de la interfaz y
de toda la documentación del mundo.

---

## A

- **Aspect ratio** (*aspect ratio*) — La proporción entre el ancho y el alto de la
  imagen. 16:9 es el estándar de televisión y web; 9:16 el vertical de móvil; 2.39:1 el
  panorámico de cine.
- **Alfa, canal** (*alpha channel*) — Un canal extra, además de rojo, verde y azul, que
  guarda la transparencia de cada píxel. Un PNG puede tenerlo; un JPG no.

## B

- **Barrido, obturador** — Ver *obturador*.
- **Bin** (*bin*) — Una carpeta dentro del media pool de Resolve. Organiza clips dentro
  del proyecto; no mueve nada en tu disco.
- **Bit depth** (*bit depth*) — Ver *profundidad de bits*.
- **Bitrate** (*bitrate*) — Cuántos datos por segundo ocupa un vídeo, normalmente en
  megabits por segundo (Mbps). Más bitrate, más calidad y más peso.
- **BRAW** (*Blackmagic RAW*) — El formato RAW de Blackmagic Design. Guarda los datos
  del sensor con parámetros de revelado editables después.

## C

- **Caché de render** (*render cache*) — Copias precalculadas que Resolve guarda en
  disco para que la reproducción no se atasque.
- **Chroma subsampling** (*chroma subsampling*) — Guardar menos información de color
  que de luminosidad, porque el ojo nota menos la pérdida. Se escribe 4:4:4, 4:2:2 o
  4:2:0.
- **Clip** (*clip*) — Un trozo de vídeo o audio, tanto en el media pool como en la
  timeline.
- **Codec** (*codec*) — El método para comprimir y descomprimir vídeo o audio. H.264,
  ProRes y DNxHR son codecs.
- **Contenedor** (*container*) — El archivo que envuelve al vídeo, al audio y a los
  metadatos. `.mp4`, `.mov` y `.mkv` son contenedores, no codecs.

## D

- **DaVinci YRGB** (*DaVinci YRGB*) — El modo de gestión de color por defecto de
  Resolve, en el que tú decides manualmente cómo se interpreta y se muestra cada cosa.
- **dBFS** (*dBFS*) — Decibelios respecto a la escala completa digital. 0 dBFS es el
  máximo absoluto: por encima, el sonido se corta.
- **Deliver** (*Deliver*) — La página de Resolve donde se configura y se lanza el render.

## E

- **Etalonaje** (*color grading*) — Dar a la imagen su aspecto final: contraste, color y
  look. Distinto de la *corrección*, que es dejarla neutra y correcta.

## F

- **Fairlight** (*Fairlight*) — La página de audio de Resolve.
- **Frame** (*frame*) — Una imagen fija de la secuencia. El vídeo es una sucesión de
  frames.
- **Frame rate** (*frame rate*) — Cuántos frames se muestran por segundo. Se mide en
  fps. 24, 25, 30, 50 y 60 son los habituales.
- **Fusion** (*Fusion*) — La página de composición y efectos por nodos.

## G

- **Gamma** (*gamma*) — La curva que relaciona el valor numérico de un píxel con el
  brillo que finalmente se ve. Sin ella, las imágenes se verían mal repartidas.
- **Grado** (*grade*) — El conjunto de ajustes de color aplicados a un clip.

## H

- **HDR** (*High Dynamic Range*) — Formatos de imagen con más rango entre lo más oscuro
  y lo más brillante que el estándar clásico.
- **Headroom** (*headroom*) — El margen que dejas entre tu nivel de audio habitual y el
  máximo, para que un pico inesperado no sature.

## I

- **Ingesta** (*ingest*) — Meter el material en el sistema: copiarlo, verificarlo,
  importarlo y organizarlo.
- **Intra-frame** (*intra-frame*) — Codecs que comprimen cada frame por separado. Más
  pesados, mucho más fáciles de editar. ProRes y DNxHR son intra-frame.

## L

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

- **Power window** (*Power Window*) — Una forma dibujada sobre la imagen para que una
  corrección de color afecte solo a esa zona.
- **Profundidad de bits** (*bit depth*) — Cuántos valores distintos puede tomar cada
  canal de color. 8 bits dan 256 niveles; 10 bits, 1024.
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
- **Render** (*render*) — Calcular y escribir el archivo final de vídeo.
- **Ripple** (*ripple*) — Editar desplazando todo lo que viene después, en lugar de
  dejar un hueco.

## S

- **Scopes** (*scopes*) — Los medidores gráficos que muestran objetivamente los valores
  de la imagen: waveform, parade, vectorscope, histograma.
- **Slip / Slide** (*slip / slide*) — Dos formas de recortar: *slip* cambia qué parte
  del clip se ve sin mover su posición; *slide* mueve el clip sin cambiar qué se ve.
- **SRT** (*SubRip*) — El formato de archivo de subtítulos más extendido.

## T

- **Timecode** (*timecode*) — La dirección exacta de un frame, escrita
  `horas:minutos:segundos:frames`.
- **Timeline** (*timeline*) — La secuencia de montaje: las pistas con los clips
  colocados en el tiempo.
- **Trimming** (*trimming*) — Ajustar con precisión dónde empieza y dónde acaba cada
  clip en la timeline.

## V

- **Vectorscope** (*vectorscope*) — El scope circular que muestra el color de la imagen:
  el ángulo es el tono y la distancia al centro, la saturación.
- **VRAM** (*VRAM*) — La memoria de la tarjeta gráfica. El recurso que Resolve agota
  antes que ningún otro.

## W

- **Waveform** (*waveform*) — El scope que muestra el brillo de la imagen a lo largo del
  ancho del cuadro.

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
