# 🌐 Webgrafía — Semana 12

> Documentación oficial primero, después las normas de subtitulado y de intercambio, y al final la
> documentación transversal del propio bootcamp. Cada entrada dice **por qué** vale la pena.

---

## Documentación oficial

### Blackmagic Design — soporte y manuales

<https://www.blackmagicdesign.com/support/>

**Por qué vale la pena**: es donde vive el Reference Manual, del que salen los capítulos 22, 41, 49,
53, 59 y 190 de esta semana. Y es donde se publican las notas de versión, que esta semana importan
más de lo normal: el multicámara y los subtítulos son dos de las áreas que más han cambiado entre
la versión 18 y la 21.

### Comparativa oficial DaVinci Resolve Free / Studio

<https://www.blackmagicdesign.com/products/davinciresolve/studio>

**Por qué vale la pena**: esta semana tiene tres funciones al otro lado de la línea —
`Create Subtitles from Audio`, `Multicam SmartSwitch` y los subtítulos animados— y **ninguna es un
entregable**. Esta página es la fuente de verdad y se actualiza con cada versión; cualquier tabla de
terceros, la del bootcamp incluida, va por detrás.

### Foro oficial de DaVinci Resolve

<https://forum.blackmagicdesign.com/>

**Por qué vale la pena**: es donde se resuelven los casos raros de conformado, que son los que el
manual no cubre: un XML que llega con los clips offline, un AAF de Pro Tools que trae las pistas
desordenadas, un `.srt` con codificación de caracteres rara que sale con acentos rotos. Nada de eso
está en el manual y todo está en el foro.

**Cómo buscar**: el buscador del foro es flojo. Funciona mejor buscar en un motor externo con
`site:forum.blackmagicdesign.com` y el mensaje de error literal.

---

## Subtitulado

### BBC Subtitle Guidelines

<https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/>

**Por qué vale la pena**: la guía de subtitulado abierta más completa que existe, y la que explica el
porqué de cada regla. De aquí salen los tres umbrales del paso 3 de la práctica 03.

**Qué mirar**: *Line breaks*, *Timing* y *Presentation rate*.

### Netflix — Timed Text Style Guide

<https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements>

**Por qué vale la pena**: una especificación de entrega real, con números y con guía por idioma.
Enseña lo estricto que es esto en un entorno profesional, que es algo que no se aprende en un
tutorial.

### ISO 639-2 — Códigos de idioma (Library of Congress)

<http://www.loc.gov/standards/iso639-2/php/code_list.php>

**Por qué vale la pena**: es la tabla que cita el propio manual de Resolve para nombrar las pistas de
subtítulos, y es la que necesitas en el paso 2 de la práctica 03. Lleva los códigos de dos letras
(ISO 639-1) y los de tres (ISO 639-2), que es lo que piden unas plataformas y otras.

### W3C — WebVTT

<https://www.w3.org/TR/webvtt1/>

**Por qué vale la pena**: la especificación del formato de subtítulos de la web. Útil sobre todo para
entender en qué se diferencia de un `.srt` cuando una plataforma te pide uno y no el otro.

---

## Intercambio de timelines

### OpenTimelineIO

<https://opentimelineio.readthedocs.io/>

**Por qué vale la pena**: el formato que el manual recomienda como primera opción para salir de
Resolve, y un proyecto abierto de la Academy Software Foundation. Su lista de *adapters* dice qué
programas lo soportan, que es la información que decide si puedes usarlo o tienes que caer en XML.

### Academy Software Foundation

<https://www.aswf.io/>

**Por qué vale la pena**: la fundación que mantiene OTIO, OpenColorIO y OpenEXR, tres cosas que salen
en este bootcamp. Saber que existe una infraestructura abierta y compartida detrás de la industria
explica por qué merece la pena elegir un formato abierto cuando se puede.

---

## Documentación del bootcamp

- [`docs/proyecto-hilo-conductor.md`](../../../../docs/proyecto-hilo-conductor.md) — la convención de
  versionado y de nombres que el verificador comprueba.
- [`docs/autograding.md`](../../../../docs/autograding.md) — cómo funciona `checks.json` y cómo leer
  un check que falla.
- [`docs/trucos-resolve.md`](../../../../docs/trucos-resolve.md) — todos los trucos del bootcamp,
  agrupados por semana.
- [`docs/atajos-de-teclado.md`](../../../../docs/atajos-de-teclado.md) — y cómo comprobar cualquier
  atajo en tu propia instalación, que es lo que manda.

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Videografía](../videografia/README.md) | **Webgrafía · Semana 12** | — |

← [Volver a la Semana 12](../../README.md)
