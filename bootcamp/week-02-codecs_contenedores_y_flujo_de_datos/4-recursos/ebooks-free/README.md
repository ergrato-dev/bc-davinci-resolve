# 📚 Libros y guías gratuitas — Semana 02

> Solo material con licencia libre, especificación pública o descarga oficial gratuita.
> Cada entrada dice **por qué** vale la pena y **qué leer** de ella para esta semana.

---

## DaVinci Resolve 21 Reference Manual

**Blackmagic Design** · PDF gratuito ·
<https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>

**Por qué vale la pena**: es el documento canónico. Cuando este bootcamp y un tutorial de
internet se contradigan, gana el manual.

**Qué leer para esta semana**:

- El capítulo de **Media Pool Metadata**: la lista completa de campos que Resolve expone de
  un clip, que es la tabla de la práctica 03
- El capítulo de **Camera Raw**: qué hace cada control del revelado y qué significa
  *decode quality*
- El capítulo de **Data Levels**: cuándo Resolve reetiqueta un clip y cuándo respeta lo que
  el archivo declara

---

## Documentación de FFmpeg

**Proyecto FFmpeg** · Web y PDF, licencia libre ·
<https://ffmpeg.org/documentation.html>

**Por qué vale la pena**: FFmpeg es la herramienta con la que se remuxea, se convierte y se
inspecciona cualquier cosa. Su documentación es densa pero es la fuente exacta: dice qué
hace cada opción, no qué suele hacer.

**Qué leer si solo tienes media hora**:

- La sección de **stream copy** (`-c copy`): explica por qué remuxear no toca los datos
- La página de **ffmpeg-codecs**: qué codecs puede leer y escribir tu compilación concreta
- La tabla de **formatos de píxel** en `ffmpeg-utils`: la traducción de `yuv420p` a "4:2:0
  de 8 bits"

---

## Especificaciones que definen lo que usas todos los días

Públicas y consultables. Sirven para cuando alguien discute de dónde salen los números:

- **[ITU-R BT.709](https://www.itu.int/rec/R-REC-BT/en)** — define el vídeo HD: primarios,
  punto blanco, curva y el rango legal 16-235. **Por qué vale la pena**: de aquí sale toda
  la confusión entre niveles `Full` y `Video`, y aquí se resuelve.
- **[ITU-R BT.601](https://www.itu.int/rec/R-REC-BT/en)** — donde se define la conversión
  de RGB a Y'CbCr. **Por qué vale la pena**: es el origen del chroma subsampling, y explica
  por qué la familia `4:x:x` se numera así.
- **[RFC 9043 — FFV1](https://datatracker.ietf.org/doc/rfc9043/)** — la especificación del
  codec sin pérdida que Resolve 21 escribe en MKV. **Por qué vale la pena**: es la lectura
  más corta y concreta que existe sobre qué significa "sin pérdida" de verdad.

---

## Blackmagic RAW — documentación oficial

**Blackmagic Design** · Web y SDK gratuito ·
<https://www.blackmagicdesign.com/products/blackmagicraw>

**Por qué vale la pena**: es la descripción del formato por quien lo diseñó, con los modos
de compresión y sus ratios reales. El SDK es gratuito y su documentación detalla qué
parámetros quedan ajustables después de grabar, que es justo lo que distingue RAW de log.

**Qué leer para esta semana**: la comparación entre *constant bitrate* y *constant
quality*, y la tabla de tamaños por modo.

---

## Guías oficiales de formación de Blackmagic Design

**Blackmagic Design** · PDF gratuito ·
<https://www.blackmagicdesign.com/products/davinciresolve/training>

**Por qué vale la pena**: están escritas con estructura de curso y traen material de
práctica descargable, incluido material Blackmagic RAW, que es la forma barata de tocar RAW
sin comprar una cámara.

**Qué leer para esta semana**: los capítulos introductorios sobre importación de medios y
formatos, del volumen de montaje.

---

← [Volver a la Semana 02](../../README.md)
