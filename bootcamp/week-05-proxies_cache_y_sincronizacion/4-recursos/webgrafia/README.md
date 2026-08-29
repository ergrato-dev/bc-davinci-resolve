# 🌐 Webgrafía — Semana 05

> Documentación oficial primero, referencias técnicas después, y la documentación
> transversal del propio bootcamp al final. Cada entrada dice **por qué** vale la pena.

---

## Documentación oficial

### Blackmagic Design — soporte y manuales

<https://www.blackmagicdesign.com/support/>

**Por qué vale la pena**: es donde vive el Reference Manual, del que salen los capítulos
*Improving Performance* y *Multicam Editing* que sostienen esta semana. Y las notas de
versión, que es donde se anuncia cuándo un ajuste de caché cambia de nombre o de sitio.

### Foro oficial de DaVinci Resolve

<https://forum.blackmagicdesign.com/>

**Por qué vale la pena**: los problemas de esta semana —la caché que no se genera, proxies
que no se reconocen, un multicámara con un ángulo desplazado— se diagnostican con rutas y
capturas, y aquí están documentados por gente que los ha tenido en la misma versión que tú.

### Blackmagic Design Training

<https://www.blackmagicdesign.com/products/davinciresolve/training>

**Por qué vale la pena**: las guías oficiales en PDF y sus proyectos de práctica, gratis,
con material que incluye tomas de doble sistema para practicar la sincronización.

---

## Referencias técnicas

### EBU R 128 — loudness y estándares de audio para imagen

<https://tech.ebu.ch/publications/r128>

**Por qué vale la pena**: es la referencia que fija los estándares técnicos del audio de
vídeo. De ahí sale el 48 kHz que evita la deriva de sincronía, y volverá entera en la
Semana 15 con la mezcla.

### ITU-R BT.709

<https://www.itu.int/rec/R-REC-BT/en>

**Por qué vale la pena**: la especificación del espacio de color de la televisión de alta
definición, que es lo que declaran los codecs de post-producción que vas a elegir para tus
optimizados. No hace falta leerla entera: sirve para saber que el nombre `Rec.709` que
aparece en los desplegables es una norma concreta y no una etiqueta comercial.

### `ffmpeg` — documentación oficial

<https://ffmpeg.org/documentation.html>

**Por qué vale la pena**: es la herramienta con la que se generan proxies fuera de Resolve,
que es la mitad de lo que hace especial a un proxy. También es lo que remuxea los `.mkv` de
OBS que Resolve no importa. Su documentación es densa; ve directo a la sección de opciones
de vídeo.

**Cuidado con**: cualquier receta que cambie la duración, el frame rate o el timecode. Un
proxy tiene que corresponder al original fotograma a fotograma.

---

## Documentación transversal del bootcamp

- [`docs/hardware-y-rendimiento.md`](../../../../docs/hardware-y-rendimiento.md) — qué
  parte del equipo interviene en cada cuello de botella. **Por qué vale la pena**: es el
  complemento directo de la teoría 01 y del diagnóstico de la práctica 01.
- [`docs/pack-de-medios.md`](../../../../docs/pack-de-medios.md) — qué debe haber en
  `03-multicamara/` y de dónde sacarlo. **Por qué vale la pena**: la práctica 03 no se
  puede hacer sin ese material.
- [`docs/proyecto-hilo-conductor.md`](../../../../docs/proyecto-hilo-conductor.md) — qué
  capa añade cada fase. **Por qué vale la pena**: esta semana cierra la Fase 1, y conviene
  ver qué se espera del proyecto al entrar en la Cut page.
- [`docs/autograding.md`](../../../../docs/autograding.md) — cómo funciona el verificador y
  qué devuelve cada operación. **Por qué vale la pena**: el check `timeline-sync-audio` usa
  `timeline_probe`, y aquí está explicado por qué depende de la timeline activa.
- [`docs/trucos-resolve.md`](../../../../docs/trucos-resolve.md) — todos los trucos del
  bootcamp agrupados por semana. **Por qué vale la pena**: los de rendimiento se usan a
  diario a partir de ahora.
- [`docs/glosario-global.md`](../../../../docs/glosario-global.md) — el vocabulario
  acumulado. **Por qué vale la pena**: esta semana añade una veintena de términos y varios
  se confunden entre sí.

---

← [Volver a la Semana 05](../../README.md)
