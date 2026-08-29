# 🌐 Webgrafía — Semana 03

> Documentación oficial primero, especificaciones después, y la documentación
> transversal del propio bootcamp al final. Cada entrada dice **por qué** vale la pena.

---

## Documentación oficial

### Blackmagic Design — soporte y manuales

<https://www.blackmagicdesign.com/support/>

**Por qué vale la pena**: es donde vive el Reference Manual y, sobre todo, las **notas
de versión**. Para esta semana importan más de lo habitual: el modelo de bibliotecas de
proyectos cambió de nombre y de comportamiento entre versiones mayores, y ahí es donde
se anuncia.

### Comparativa oficial DaVinci Resolve y DaVinci Resolve Studio

<https://www.blackmagicdesign.com/products/davinciresolve/studio>

**Por qué vale la pena**: es la única tabla de Free frente a Studio que Blackmagic
actualiza con cada versión. Cuando cualquier otra fuente —incluido este bootcamp— y esa
página discrepen, gana la página. La práctica 04 te pide compararla con tu instalación.

### Foro oficial de DaVinci Resolve

<https://forum.blackmagicdesign.com/>

**Por qué vale la pena**: en la materia de esta semana es más útil que cualquier vídeo.
Proyectos que no abren, bibliotecas que no aparecen, respaldos que no restauran: son
problemas que se diagnostican con rutas y mensajes de error, y aquí están documentados
por gente que los ha tenido.

### Blackmagic Design Training

<https://www.blackmagicdesign.com/products/davinciresolve/training>

**Por qué vale la pena**: las guías oficiales en PDF y los vídeos, gratis. Sus primeros
capítulos cubren el Project Manager con otro enfoque, que es la mejor forma de detectar
lo que creías tener claro.

---

## Lo que hay debajo del capó

### SQLite

<https://www.sqlite.org/about.html>

**Por qué vale la pena**: media página que explica qué es el formato de `Project.db`, el
archivo donde vive tu proyecto entero. Es la justificación técnica de la advertencia más
repetida de la semana: no se copia a mano mientras Resolve escribe.

### PostgreSQL

<https://www.postgresql.org/docs/>

**Por qué vale la pena**: el gestor de bases de datos que hay debajo de una biblioteca de
proyectos en red. Con la introducción basta para saber qué estás mirando el día que
alguien te diga "conéctate a la base del estudio".

---

## Documentación transversal del bootcamp

- [`docs/free-vs-studio.md`](../../../../docs/free-vs-studio.md) — el reparto completo
  entre versiones, con la alternativa en Free de cada función de pago y la semana en la
  que aparece. **Por qué vale la pena**: es lectura obligatoria de la práctica 04, y la
  referencia que consultarás las 33 semanas siguientes.
- [`docs/autograding.md`](../../../../docs/autograding.md) — cómo funciona el verificador,
  por qué el puente va dentro de Resolve y qué devuelve cada operación.
  **Por qué vale la pena**: esta semana usas cuatro operaciones distintas del puente;
  aquí está la forma exacta de lo que devuelve cada una.
- [`docs/proyecto-hilo-conductor.md`](../../../../docs/proyecto-hilo-conductor.md) — qué
  capa añade cada fase al proyecto y la política de versionado. **Por qué vale la pena**:
  esta semana cierra la Fase 0, y ahí está escrito qué significa eso.
- [`docs/hardware-y-rendimiento.md`](../../../../docs/hardware-y-rendimiento.md) — los
  mínimos reales y qué merece la pena mejorar primero. **Por qué vale la pena**: la
  práctica 04 te hace mirar memoria y GPU sin tocarlas; este documento explica cuándo sí
  se tocan.
- [`docs/atajos-de-teclado.md`](../../../../docs/atajos-de-teclado.md) — cómo se busca
  cualquier comando en `Keyboard Customization`. **Por qué vale la pena**: es el método
  que resuelve todos los "en mi versión ese menú no está donde dice".
- [`docs/trucos-resolve.md`](../../../../docs/trucos-resolve.md) — todos los trucos del
  bootcamp agrupados por semana. **Por qué vale la pena**: los de esta semana son de los
  que más se usan a diario.

---

← [Volver a la Semana 03](../../README.md)
