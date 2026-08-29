# 📖 Glosario — Semana 07

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre
> paréntesis el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **A-roll** (*A-roll*) — El material que sostiene el relato: quien habla, la acción
  principal, la continuidad. Vive en `Video 1`, que es la única pista que hace ripple. Su
  contrario es el B-roll.
- **Acabado** (*fine cut* / *finishing*) — La pasada que viene después del montaje bruto:
  transiciones, ajustes de duración, sonido audible, rótulos. No cambia qué cuenta la pieza;
  cambia cómo se lee.
- **`Add Dissolve to All Edits`** (*Add Dissolve to All Edits*) — Comando de
  `Timeline Actions` que pone un `Cross Dissolve` en todos los puntos de corte de la timeline.
  Existe, y es el antipatrón número uno de la semana.
- **`Analyze Timeline Edits`** (*Analyze Timeline Edits*) — La ventana de umbrales del Boring
  Detector. Dos deslizadores: `Boring Clips`, en segundos, y `Jump Cuts`, en fotogramas.

## B

- **B-roll** (*B-roll*) — El material que se pone encima del A-roll para ilustrar, tapar un
  salto o dar aire. Vive en `Video 2`, que no hace ripple.
- **`Boring Detector`** (*Boring Detector*) — La herramienta de la Cut page que analiza en
  vivo la duración de cada clip y marca en la timeline superior los que se salen de los
  umbrales: gris claro los demasiado largos, rojo los demasiado cortos. Se activa desde
  `Timeline Options` y es persistente.

## C

- **Cola** (*handle*) — El material del archivo que queda fuera del rango marcado con `I` y
  `O`: lo que hay antes del punto de entrada y después del punto de salida. Es la reserva con
  la que se hacen las transiciones y con la que se trabaja en la Semana 09. En inglés, los dos
  extremos juntos son *heads and tails*.
- **Corte** (*cut*) — El cambio instantáneo de un plano al siguiente, sin nada en medio. Es lo
  contrario de una transición y es el noventa y muchos por ciento de cualquier pieza.
- **`Cross Dissolve`** (*Cross Dissolve*) — La disolvencia estándar de Resolve y la transición
  por defecto: un plano se desvanece mientras el otro aparece. El botón `Dissolve` pone una de
  un segundo.

## D

- **dBFS** (*decibels relative to Full Scale*) — La unidad del volumen en audio digital. El
  **0 dBFS** es el máximo absoluto que un archivo puede representar; todo lo demás es negativo.
  Es distinto de LUFS, que es la unidad de la Semana 15.
- **Disolvencia** (*dissolve*) — La transición en la que los dos planos conviven un rato,
  desapareciendo uno y apareciendo el otro. Comunica paso del tiempo, cambio de sitio o cambio
  de tema; fuera de eso, sobra.
- **`Duplicate Timeline`** (*Duplicate Timeline*) — El comando del menú contextual del media
  pool que crea una copia de una timeline. Es lo que separa `BC-Montaje-v1` de
  `BC-Montaje-v2`, y la convención de versionado del bootcamp.

## E

- **`Edit Actions`** (*Edit Actions*) — El tercero de los tres iconos de la barra de la
  timeline de la Cut page. Contiene `Trim Start to Playhead`, `Trim End to Playhead` y
  `Resync Clip`.

## F

- **Flash frame** (*flash frame*) — Un clip de uno o dos fotogramas que nadie puso a
  propósito. Sale de borrar mal, de arrastrar con el imán desactivado o de pegar en el sitio
  equivocado. En pantalla es un fogonazo; en la timeline, invisible a escala normal.
- **Fotogramas duplicados** (*duplicate frame detection*, *dupe detection*) — La detección que
  marca con barras de color los tramos en los que un mismo rango de fotogramas se ha usado más
  de una vez en la timeline. Se activa con `View > Show Duplicate Frames`.

## G

- **Generador** (*generator*) — Un clip que Resolve produce en vez de leer del disco: una carta
  de color, un fondo, un título. Su duración por defecto son 5 segundos, ajustable en el panel
  `Editing` de las preferencias de usuario.

## H

- **`Hover Scrub Preview`** (*Hover Scrub Preview*) — La opción de los navegadores de
  transiciones y títulos que previsualiza el efecto en el visor al pasar el ratón por encima
  de su miniatura, sin colocarlo en la timeline.

## I

- **Interpolar** (*interpolate*) — Calcular un valor intermedio a partir de dos conocidos. En
  vídeo, inventar el fotograma que iría entre dos grabados. Es lo que Resolve hace al
  ralentizar cuando no le sobran fotogramas, y lo que hace `Smooth Cut` sobre un corte.

## M

- **`Media limit`** (*media limit*) — El borde del archivo de origen: el punto a partir del
  cual un clip no se puede alargar más, porque no hay material grabado. Es el límite físico de
  las colas.

## N

- **Nivelar** (*leveling*) — Poner cada clip en un rango de volumen razonable para que la pieza
  se pueda escuchar entera sin tocar el volumen del sistema. Es lo que toca esta semana, y no
  es lo mismo que mezclar.

## P

- **Preset** (*preset*) — Un conjunto de ajustes guardado con un nombre. En `Quick Export`, un
  preset decide el codec, el contenedor, la resolución y el bitrate por ti.

## Q

- **`Quick Export`** (*Quick Export*) — El comando de `File` que exporta la timeline a un
  archivo eligiendo solo un preset, desde cualquier página del programa. Puede exportar la
  timeline entera o solo el rango marcado con `I` y `O`. No es un master.

## R

- **Recorte** (*clipping*) — Lo que pasa cuando una señal de audio intenta pasar de 0 dBFS: los
  picos se aplanan y suena a distorsión áspera. No se puede deshacer, porque la información no
  está en el archivo.
- **`Ripple Delete Silence`** (*Ripple Delete Silence*) — La operación de
  `Clip > Audio Operations` que busca los tramos por debajo de un umbral y los borra cerrando
  el hueco. Acorta la pieza, hace ripple y crea saltos de montaje.
- **Rótulo** (*lower third*, *title*) — Un título superpuesto que da información que la imagen
  no puede dar: quién habla, dónde estamos, de qué va la pieza.

## S

- **Salto de montaje** (*jump cut*) — El respingo que da un sujeto cuando se pegan dos trozos
  del mismo plano y su posición ha cambiado. Se ve porque el fondo no cambia y solo salta él.
- **`Smooth Cut`** (*Smooth Cut*) — La transición que repara un salto de montaje deformando el
  sujeto de una posición a la otra en lugar de mezclar las dos imágenes. En Resolve 21 usa el
  procesado `Speed Warp`. Funciona entre 2 y 6 fotogramas, no en el segundo que trae por
  defecto.
- **`Speed Warp`** (*Speed Warp*) — El procesado con motor neuronal que Resolve usa desde la
  versión 20 para `Smooth Cut` y para los cambios de velocidad de alta calidad.

## T

- **`Text`** (*Text*) — El título más simple y más flexible de la categoría `Titles`: un bloque
  de texto sobre transparencia, sin animación. Es el que se usa esta semana. No confundir con
  `Text+`, que es el motor de texto de Fusion y es materia de la Semana 11.
- **`Timeline Actions`** (*Timeline Actions*) — El segundo de los tres iconos de la barra de la
  timeline de la Cut page. Contiene lo que añade o modifica la timeline entera:
  `Add Video Track`, `Split Clips`, `Add Marker`, `Add Dissolve to All Edits`,
  `Clear Transition from All Edits`.
- **`Timeline Options`** (*Timeline Options*) — El primero de los tres iconos. Contiene cómo se
  ve y se comporta la timeline: `Ripple On`, `Snap`, `Display Speed Keyframes`,
  `Set Default Transition`, `Fixed Playhead`, `Boring Detector`.
- **Transición** (*transition*) — Cualquier cambio de plano que no sea un corte seco: un tramo
  en el que los dos planos conviven o se sustituyen progresivamente. Se alinea de tres formas
  respecto al corte: `Start on Edit`, `Center on Edit` y `End on Edit`.

## V

- **Velocidad** (*speed*) — El multiplicador que decide cuántos fotogramas grabados se enseñan
  por fotograma de timeline. Cambiarla cambia la duración del clip, y en `Video 1` eso hace
  ripple. Un valor negativo reproduce hacia atrás.

---

## 📚 Términos de semanas anteriores que vuelven aquí

| Término | Semana | Por qué importa esta semana |
| ------- | ------ | --------------------------- |
| **Ripple** | 06 | Todo cambio de duración en `Video 1` descoloca lo que hay encima |
| **Fotograma** (*frame*) | 01 | Las colas y los `Smooth Cut` se miden en fotogramas, no en segundos |
| **fps** | 01 | 24 fps es lo que convierte «un segundo» en «24 fotogramas» |
| **H.264** | 02 | El codec del preset de exportación de esta semana |
| **Contenedor** | 02 | `.mp4` es lo que sale de `Quick Export` |
| **Codec** | 02 | Lo que el preset decide por ti |
| **Bin** | 04 | `12-Entregas` es el bin nuevo de la semana |
| **Proxy** | 05 | Por eso la reproducción dentro de Resolve no es la del archivo exportado |
| **Montaje bruto** (*rough cut*) | 06 | El punto de partida: lo que se acaba esta semana |
| **Indicador inteligente** | 06 | Los botones de transición actúan sobre el corte más cercano, igual que él |

---

← [Volver a la Semana 07](../README.md)
