# 🌐 Webgrafía — Semana 01

> La documentación oficial de Blackmagic primero, siempre. Después, fuentes primarias.
> Cada entrada dice **por qué** vale la pena.

---

## Oficial de Blackmagic Design

### [Soporte y descargas de DaVinci Resolve](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion)

De aquí sale el instalador, el Reference Manual en PDF, las notas de versión y el
documento de configuraciones soportadas.

**Por qué vale la pena**: es la única página que se actualiza con cada versión. Cuando
dudes si tu tarjeta gráfica está soportada o qué cambió en la 21, aquí está la respuesta
oficial y no una suposición de foro.

### [DaVinci Resolve — página de producto](https://www.blackmagicdesign.com/products/davinciresolve)

**Por qué vale la pena**: describe qué hace cada página del programa, con el vocabulario
oficial. Sirve como mapa de lo que el bootcamp va a cubrir en 36 semanas.

### [Comparativa DaVinci Resolve y DaVinci Resolve Studio](https://www.blackmagicdesign.com/products/davinciresolve/studio)

**Por qué vale la pena**: es **la** tabla canónica de qué añade la versión de pago. Este
bootcamp resume lo relevante en
[`docs/free-vs-studio.md`](../../../../docs/free-vs-studio.md), pero cuando ese documento
y esta página discrepen, gana la página.

### [Formación oficial](https://www.blackmagicdesign.com/products/davinciresolve/training)

**Por qué vale la pena**: las guías en PDF son gratuitas y el material de práctica que
las acompaña es de las pocas fuentes libres de vídeo **log y RAW** pensadas para
enseñar etalonaje.

### [Foro oficial](https://forum.blackmagicdesign.com/)

**Por qué vale la pena**: tiene un subforo por página del programa. Es donde se
documentan los casos límite que el manual no cubre, y donde las incompatibilidades de
drivers aparecen antes que en ningún otro sitio.

---

## Fuentes primarias de los estándares

Para cuando alguien discuta de dónde salen los números.

### [Recomendaciones ITU-R serie BT](https://www.itu.int/rec/R-REC-BT/en)

**Por qué vale la pena**: son los documentos que definen Rec.709, Rec.2020 y los
estándares de televisión de los que derivan los frame rates de PAL y NTSC. Fuente
primaria, no interpretación.

### [DCI Digital Cinema System Specification](https://www.dcimovies.com/)

**Por qué vale la pena**: define 4096 × 2160 y los formatos de sala 1.85:1 y 2.39:1. Es
lo que zanja la confusión entre UHD y 4K DCI.

### [SMPTE](https://www.smpte.org/)

**Por qué vale la pena**: la organización que estandarizó el timecode, incluido el drop
frame. Si necesitas citar por qué el drop frame se salta 108 números por hora, la fuente
está aquí.

---

## Conceptos de fondo

### [Persistence of vision — Wikipedia](https://en.wikipedia.org/wiki/Persistence_of_vision)

**Por qué vale la pena**: desmonta la explicación que repite el 90 % de los tutoriales.
Entender que la persistencia retiniana **no** explica la percepción de movimiento es lo
que te permite razonar después sobre el judder y sobre por qué el desenfoque de
movimiento importa tanto.

### [Rolling shutter — Wikipedia](https://en.wikipedia.org/wiki/Rolling_shutter)

**Por qué vale la pena**: explica con diagramas por qué el artefacto tiene la forma que
tiene y por qué depende del sensor y no del codec. Útil para no perder el tiempo
buscando el problema en el sitio equivocado.

---

## Del propio bootcamp

- [`docs/setup-entorno.md`](../../../../docs/setup-entorno.md) — instalación y Python
- [`docs/hardware-y-rendimiento.md`](../../../../docs/hardware-y-rendimiento.md) — qué máquina hace falta
- [`docs/free-vs-studio.md`](../../../../docs/free-vs-studio.md) — qué cambia con la licencia de pago
- [`docs/atajos-de-teclado.md`](../../../../docs/atajos-de-teclado.md) — los atajos que importan
- [`docs/autograding.md`](../../../../docs/autograding.md) — cómo funciona el verificador

---

← [Volver a la Semana 01](../../README.md)
