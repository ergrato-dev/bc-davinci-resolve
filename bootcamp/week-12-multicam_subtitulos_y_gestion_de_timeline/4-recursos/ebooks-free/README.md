# 📚 Libros y manuales gratuitos — Semana 12

> Documentación oficial primero, después las normas que rigen el subtitulado y los formatos de
> intercambio. Cada entrada dice **por qué** vale la pena y **qué capítulo** mirar.

---

## Oficial de Blackmagic Design

### DaVinci Resolve 21 Reference Manual

Viene con la instalación, en `Documents/DaVinci Resolve.pdf`, y también se descarga desde
<https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>.

**Por qué vale la pena**: es la fuente de verdad de todo lo que dice esta semana. Y esta semana toca
cuatro capítulos que están muy separados entre sí, así que conviene tener la lista:

| Capítulo | Qué cubre | De qué teoría es |
| -------- | --------- | ---------------- |
| **22 · Importing and Conforming Timelines** | Importar AAF, EDL, XML y OTIO; conformar; el diálogo de importación | Teoría 09 |
| **41 · Creating and Working with Timelines** | Duplicar, desactivar, respaldos, `.drt`, comparar con respaldo | Teoría 07 |
| **49 · Multicam Editing** | Todo el multicámara, de la creación al aplanado | Teorías 01, 02 y 03 |
| **53 · Media Management** | La ventana entera, opción a opción | Teoría 08 |
| **59 · Subtitles and Closed Captioning** | Pistas, regiones, estilo, importación y exportación | Teorías 04, 05 y 06 |
| **190 · Exporting Timelines to Other Applications** | La otra mitad del intercambio: exportar | Teoría 09 |

**Cómo leerlo sin perder la tarde**: el capítulo 49 es corto y se lee entero, que es lo que conviene
antes de la práctica 02. El 59 es largo: léete «Subtitles and Closed Captioning Support», «Adding
Subtitles and Captions Manually» y «Exporting Subtitles and Closed Captions», y deja el resto para
consultar.

> [!TIP]
> Un detalle que engaña: cosas que se usan desde una página están documentadas en el capítulo de
> otra, porque los menús son globales. Busca por el **nombre inglés del control**, no por la página.

### DaVinci Resolve — Training

<https://www.blackmagicdesign.com/products/davinciresolve/training>

**Por qué vale la pena**: las guías oficiales de formación son gratuitas en PDF y traen sus proyectos
de práctica. La guía de edición dedica un capítulo al montaje multicámara con material propio, que
es la forma de practicar la práctica 02 con más ángulos de los que tú hayas podido grabar.

**Qué buscar para esta semana**: la guía de edición —*The Beginner's Guide to DaVinci Resolve* y su
continuación de edición— y sus proyectos de multicámara.

---

## Subtitulado y accesibilidad

### BBC Subtitle Guidelines

<https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/>

**Por qué vale la pena**: es la guía de subtitulado más completa y más citada que hay publicada en
abierto, y es de las pocas que explica **el porqué** de cada regla en vez de dar la cifra a secas.
Cubre longitud de línea, velocidad de lectura, dónde se corta una frase, cómo se marca quién habla y
cómo se describe el sonido.

**Qué leer para esta semana**: las secciones de *Line breaks*, *Timing* y *Presentation rate*. Son
las que sostienen los tres umbrales del paso 3 de la práctica 03.

**Ojo**: está escrita para inglés. Las cifras de caracteres por línea y por segundo se trasladan bien
al español; las reglas de corte de línea hay que adaptarlas a la gramática, y ahí es donde el
criterio es tuyo.

### Netflix — Timed Text Style Guide

<https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements>

**Por qué vale la pena**: es la especificación de subtitulado de una plataforma real, con números
concretos y con una guía por idioma. Leer una especificación de entrega de verdad enseña algo que
ningún tutorial cuenta: **lo estricto que es esto** cuando el destino es profesional.

**Qué buscar**: los requisitos generales, y la guía específica de castellano si vas a entregar en
español.

### W3C — WebVTT: The Web Video Text Tracks Format

<https://www.w3.org/TR/webvtt1/>

**Por qué vale la pena**: es la especificación del formato de subtítulos de la web, el que carga la
etiqueta `<track>` de HTML5 y el que Resolve exporta como `WebVTT`. No hace falta leerla entera: con
mirar la estructura de un archivo se entiende en qué se parece y en qué se diferencia de un `.srt`.

---

## Formatos de intercambio

### OpenTimelineIO — Documentación

<https://opentimelineio.readthedocs.io/>

**Por qué vale la pena**: OTIO es el formato que el manual de Resolve recomienda como **primera
opción** para pasar una timeline a otro programa, y es un proyecto abierto de la Academy Software
Foundation. Su documentación explica el modelo de datos —qué es una pista, un clip, una transición—
y eso ayuda a entender por qué unos formatos llevan más que otros.

**Qué leer**: la introducción y la página de *adapters*, que dice qué programas lo soportan y con qué
fidelidad.

**Y una cosa más**: OTIO tiene una biblioteca de Python. En la Fase 9 del bootcamp, cuando toque
automatizar, poder leer y escribir timelines desde un script sin abrir Resolve es una herramienta
real.

### SMPTE — Advanced Authoring Format

<https://www.smpte.org/>

**Por qué vale la pena**: AAF es una norma de la SMPTE, y la organización publica en abierto los
resúmenes de sus estándares. No hace falta leer la especificación —cuesta dinero y es enorme—, pero
saber **que AAF es una norma y no un formato de una empresa** explica por qué es el intercambio del
mundo profesional del sonido y del montaje.

---

## Del propio bootcamp

- [`docs/proyecto-hilo-conductor.md`](../../../../docs/proyecto-hilo-conductor.md) — la convención de
  versionado que la Teoría 07 explica por dentro.
- [`docs/free-vs-studio.md`](../../../../docs/free-vs-studio.md) — dónde caen `Create Subtitles from
  Audio` y `Multicam SmartSwitch`.
- [`docs/glosario-global.md`](../../../../docs/glosario-global.md) — todos los términos del bootcamp,
  no solo los de esta semana.

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **Libros y manuales · Semana 12** | [Videografía](../videografia/README.md) |

← [Volver a la Semana 12](../../README.md)
