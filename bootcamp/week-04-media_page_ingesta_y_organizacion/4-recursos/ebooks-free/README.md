# 📚 Libros y manuales gratuitos — Semana 04

> Todo lo de esta lista es descargable sin pagar. El primero es la fuente de verdad de
> los rótulos y de los menús que esta semana cita; los demás explican el oficio que hay
> detrás de la ingesta, que es más viejo que Resolve.

---

## Imprescindible

### DaVinci Resolve 21 Reference Manual

<https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>

PDF oficial y gratuito, en la sección de documentación de la familia de productos.

**Por qué vale la pena**: el capítulo ***Media Page*** es exactamente el temario de esta
semana: los paneles, el Clone Tool, los bins, los smart bins, los power bins, el panel
Metadata, las columnas del media pool y Scene Cut Detection, con las capturas de tu
versión exacta. Esta semana cita varios rótulos que **no se pueden verificar por la API
de scripting**; cuando este material y el manual discrepen, gana el manual.

**Cómo usarlo**: búscalo dentro del PDF por el nombre inglés del control
(`Scene Cut Detection`, `Power Bins`, `Smart Bin`) en vez de leer el capítulo entero. Y
guárdalo en `BC-Resolve/04-respaldos/documentacion/` como te pedía la Semana 03.

---

## Guías oficiales de entrenamiento

### Blackmagic Design Training — guías y material de práctica

<https://www.blackmagicdesign.com/products/davinciresolve/training>

Blackmagic publica gratis los libros de sus cursos oficiales, en PDF, junto con el
material de vídeo para hacer los ejercicios.

**Por qué vale la pena**: la guía de iniciación dedica su primer bloque entero a la
ingesta y la organización, con un proyecto de ejemplo ya montado. Ver la misma tarea
sobre material distinto es la forma barata de detectar lo que creías haber entendido.

**Además**: de aquí sale el material de práctica que necesitarás en la **Semana 16**
para las semanas de color. Descárgalo cuando puedas: pesa, y no querrás estar bajándolo
el lunes de esa semana.

---

## El oficio de la ingesta

### Documentación de los formatos de tarjeta de cámara

Las especificaciones de las estructuras de carpetas que usan las cámaras profesionales
son públicas y las publican sus asociaciones y fabricantes.

**Por qué vale la pena**: explican **por qué** se clona la tarjeta entera y no los
archivos de vídeo sueltos. Cada estructura guarda al lado de cada clip archivos de
índice, de audio y de metadata sin los cuales el material no se reconstruye. Cuando
veas una tarjeta con carpetas de nombre raro, ya sabrás que no se toca ninguna.

**Cuánto leer**: la introducción de cualquiera de ellas. Diez minutos, y no vuelves a
copiar solo los `.mp4`.

---

## Sobre integridad de datos

### Documentación de las funciones de huella

<https://www.rfc-editor.org/rfc/rfc1321>  · MD5
<https://www.rfc-editor.org/rfc/rfc6234>  · SHA-2

**Por qué vale la pena**: son las especificaciones de dos de las familias de huellas que
usa el Clone Tool y que usa `preparar-medios.sh`. No hace falta entender la matemática:
con leer la introducción se entiende la propiedad que importa, que es que **un solo bit
distinto produce una huella completamente distinta**.

**Cuánto leer**: la primera página de cualquiera de los dos. Es la justificación técnica
de todo el paso 3 de la práctica 01.

---

## 📥 Cómo organizarlos

Los PDF, en `BC-Resolve/04-respaldos/documentacion/`, junto al Reference Manual de la
Semana 03. Ocupan poco y te evitan depender de tener internet el día que se te atasque
algo.

---

← [Volver a la Semana 04](../../README.md)
