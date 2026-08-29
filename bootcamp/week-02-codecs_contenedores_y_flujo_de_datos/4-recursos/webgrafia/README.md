# 🌐 Webgrafía — Semana 02

> Documentación oficial primero, herramientas después, y solo entonces material de terceros.
> Cada entrada dice **por qué** vale la pena.

---

## Documentación oficial

### Blackmagic Design — soporte y manuales

<https://www.blackmagicdesign.com/support/>

**Por qué vale la pena**: es donde vive el Reference Manual, las notas de versión y los
requisitos de sistema. Las notas de versión importan más de lo que parece: ahí se anuncia
cuándo un codec entra o sale de la lista de formatos soportados.

### Blackmagic RAW

<https://www.blackmagicdesign.com/products/blackmagicraw>

**Por qué vale la pena**: la especificación funcional del formato y el SDK, gratuito. Es la
fuente para los modos de compresión y para qué se puede ajustar después de grabar.

### Foro oficial de DaVinci Resolve

<https://forum.blackmagicdesign.com/>

**Por qué vale la pena**: es donde se documentan los comportamientos que el manual no
recoge, incluidos los casos raros de importación. Si un archivo no entra en Resolve, la
respuesta suele estar aquí antes que en ningún otro sitio.

---

## Herramientas

### MediaInfo

<https://mediaarea.net/MediaInfo>

Libre, multiplataforma, con interfaz gráfica y con versión de terminal.

**Por qué vale la pena**: es la herramienta de esta semana. Muestra el chroma subsampling y
el bitrate, que son exactamente los dos datos que Resolve no enseña.

### FFmpeg y ffprobe

<https://ffmpeg.org/>

**Por qué vale la pena**: remuxea, convierte frecuencias de muestreo e inspecciona
archivos, todo desde una línea. Es la herramienta que convierte un problema de "este
archivo no entra" en un comando de diez segundos.

> [!TIP]
> Descárgalo de la página oficial o del gestor de paquetes de tu sistema. Los sitios que
> reempaquetan FFmpeg con instaladores propios son la vía habitual de colar software no
> deseado.

---

## Especificaciones

### Recomendaciones ITU-R

<https://www.itu.int/rec/R-REC-BT/en>

**Por qué vale la pena**: BT.601 y BT.709 son la fuente primaria del chroma subsampling y
de los niveles de datos. Cuando una discusión sobre "rango legal" se alarga, esto la
termina.

### IETF — RFC 9043 (FFV1)

<https://datatracker.ietf.org/doc/rfc9043/>

**Por qué vale la pena**: una especificación de codec corta y legible, de un codec sin
pérdida que Resolve 21 escribe de verdad. Buena lectura para ver qué contiene realmente la
definición de un codec.

---

## Documentación transversal del bootcamp

- [`docs/pack-de-medios.md`](../../../../docs/pack-de-medios.md) — de dónde sale cada
  archivo del pack y cómo se sella. **Por qué vale la pena**: es el complemento directo de
  la práctica 02.
- [`docs/hardware-y-rendimiento.md`](../../../../docs/hardware-y-rendimiento.md) — los
  mínimos reales y qué merece la pena mejorar primero. **Por qué vale la pena**: la
  práctica 04 mide tu disco; este documento dice qué hacer con el resultado.
- [`docs/free-vs-studio.md`](../../../../docs/free-vs-studio.md) — el reparto entre
  versiones. **Por qué vale la pena**: aquí se aclara qué límites de formato son de Free y
  cuáles no existen.
- [`docs/autograding.md`](../../../../docs/autograding.md) — cómo funciona el verificador y
  qué devuelve cada operación del puente. **Por qué vale la pena**: si un check de esta
  semana falla de forma rara, la explicación está ahí.

---

← [Volver a la Semana 02](../../README.md)
