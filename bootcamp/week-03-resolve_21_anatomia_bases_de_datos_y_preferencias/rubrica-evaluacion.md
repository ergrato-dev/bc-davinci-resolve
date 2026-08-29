# 📊 Rúbrica de evaluación — Semana 03

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 %
en la tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 03` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Nombra las tres capas en las que vive tu trabajo en Resolve. ¿Cuál de ellas contiene
   los archivos de vídeo y por qué un `.drp` pesa unos pocos megabytes?
2. Explica qué es un clip *offline* y por qué no es una pérdida de trabajo. Nombra tres
   formas distintas de provocar uno sin querer.
3. ¿Qué es una biblioteca de proyectos? Nombra los tres tipos y di cuál es la única
   razón que justifica una biblioteca en red.
4. Diferencia `Export Project`, *Project Archive* y *Project Backups*: qué produce cada
   uno, si lleva medios y para qué se usa.
5. ¿Qué hace Live Save y qué hacen los respaldos automáticos? ¿Por qué tener solo Live
   Save encendido deja un agujero, y qué desastre concreto no cubre?
6. La regla para saber dónde buscar un ajuste. Clasifica estos cinco: frame rate de la
   timeline, GPU que usa Resolve, ubicación de la caché de este proyecto, Live Save,
   ciencia de color.
7. ¿Cuál es el único ajuste irreversible de Resolve y en qué momento exacto se congela?
   ¿Cuál es el remedio que evita el problema en lugar de tener que recordarlo?
8. Diferencia `Timeline frame rate` de `Playback frame rate`. Da un caso real en el que
   tenga sentido que sean distintos.
9. De las seis cosas que Resolve escribe en tu disco, ¿cuáles son regenerables y cuáles
   no? Si te quedan 3 GB libres a mitad de la Semana 12, ¿en qué orden borras?
10. ¿Por qué el autograding de este bootcamp funciona en DaVinci Resolve Free si el
    scripting externo es una función de Studio?

<details>
<summary>📝 Respuestas</summary>

**1.** Las tres capas son la **biblioteca de proyectos**, el **proyecto** y los
**medios**. Los archivos de vídeo están en la tercera y **solo** en la tercera: viven en
tu disco y Resolve los lee donde estén.

Un `.drp` pesa poco porque contiene **decisiones, no imágenes**: timelines, cortes,
grados, comps, mezcla, y una lista de **referencias** a archivos. Una referencia es la
ruta de un archivo, no una copia de él.

**2.** Un clip *offline* es un clip cuyo archivo no está donde el proyecto dice que
está: el enlace se ha roto, pero la timeline, los cortes y los grados siguen intactos.
Se arregla volviendo a enlazar, no rehaciendo el trabajo.

Tres formas de provocarlo: **mover o renombrar** la carpeta de material; **renombrar un
archivo** ya importado; y tener el material en una **carpeta sincronizada con la nube**,
que puede descargarlo bajo demanda o renombrarlo al resolver un conflicto.

**3.** Una **biblioteca de proyectos** es el contenedor donde viven todos tus proyectos;
el Project Manager siempre muestra el contenido de una. Los tres tipos son **local** (en
carpetas de tu disco), **en red** (sobre un servidor PostgreSQL) y **en la nube**
(Blackmagic Cloud).

La única razón que justifica una en red es que **dos personas necesiten el mismo
proyecto abierto a la vez**. Para todo lo demás, local y un `.drp` bien guardado ganan
por sencillez.

**4.**

| | Produce | ¿Medios? | Para qué |
| --- | --- | --- | --- |
| `Export Project` | Un `.drp` de unos MB | No | Mandar el montaje, mover de biblioteca, respaldo semanal |
| *Project Archive* | Una carpeta `.dra` que pesa lo que pese el material | Sí | Entregar el trabajo completo, archivar, cambiar de máquina |
| *Project Backups* | Copias automáticas con fecha | No | Recuperar de un cierre inesperado o de un error propio |

**5.** **Live Save** guarda el proyecto continuamente mientras trabajas: evita perder lo
hecho desde la última vez que guardaste. Los **respaldos automáticos** dejan copias con
fecha: permiten **volver atrás en el tiempo**.

El agujero de tener solo Live Save es que **guarda el destrozo con la misma diligencia
que el acierto**: si borras media timeline y te das cuenta al día siguiente, no hay a
dónde volver. Ese es el desastre que no cubre.

**6.** La regla: **si describe tu ordenador es Preferences; si describe tu vídeo es
Project Settings.**

| Ajuste | Dónde |
| --- | --- |
| Frame rate de la timeline | Project Settings |
| GPU que usa Resolve | Preferences |
| Ubicación de la caché **de este proyecto** | Project Settings (`Master Settings > Working Folders`) |
| Live Save | Preferences |
| Ciencia de color | Project Settings |

La tercera es la excepción de la semana: las Working Folders son ajustes de proyecto
aunque hablen de discos, porque cada proyecto puede vivir en un disco distinto.

**7.** El único ajuste irreversible es el **`Timeline frame rate`**, y se congela **en
cuanto hay un clip en el media pool**. A partir de ahí el campo aparece atenuado y la
única salida es crear un proyecto nuevo, configurarlo e importar después.

El remedio no es acordarse: es **guardar un preset en `Project Settings > Presets` y
ponerlo por defecto**, para que los proyectos nuevos nazcan ya con el valor correcto.

**8.** El **`Timeline frame rate`** es una propiedad de la obra: cuántos frames hay en un
segundo de tu pieza. El **`Playback frame rate`** es una propiedad de la reproducción: a
cuántos frames por segundo se ve en tu pantalla.

Caso real: una timeline a 60 fps monitorizada a 24 porque el equipo de reproducción no
da más, o para revisar el montaje en un portátil sin que la reproducción se atragante.
La pieza sigue siendo de 60 fps.

**9.** **Regenerables**: la caché de render, los medios optimizados y los proxies.
**No regenerables**: el proyecto (`Project.db`), los respaldos automáticos y los stills
de la galería.

Orden para recuperar espacio: **1)** `Playback > Delete Render Cache > All`; **2)**
borrar medios optimizados y proxies; **3)** reducir el número de copias de respaldo
conservadas, desde Preferences y no borrando a mano; **4)** archivar proyectos
terminados a otro disco. Nunca la biblioteca, la galería ni el material original.

**10.** Porque lo que es de Studio es el scripting **externo** —lanzar un script contra
Resolve desde una terminal—, no el **interno**. Un script arrancado desde
`Workspace > Scripts` funciona en Free.

Por eso el autograding está partido: el **puente** corre **dentro** de Resolve y habla
con la API; el **verificador** es un cliente que le pregunta desde fuera por HTTP. Esa
separación es lo que permite corregir las 36 semanas en la versión gratuita.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **14,29 puntos**.

```bash
python scripts/verificar-semana.py 03
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 01 | `resolve-es-21` | 14,29 |
| 02 | `proyecto-abierto` | 14,29 |
| 02 | `bootcamp-en-la-biblioteca` | 14,29 |
| 02 | `proyecto-de-pruebas` | 14,29 |
| 02 | `frame-rate-de-proyecto` | 14,29 |
| 02 | `playback-frame-rate` | 14,29 |
| 02 | `timeline-intacta` | 14,29 |

**Necesitas 70 / 100**, es decir **al menos 5 de los 7 checks**.

> [!TIP]
> Si fallan **todos** a la vez, no repases siete cosas: repasa una. Casi siempre es que
> te quedaste en la biblioteca `BC-Pruebas-DB` de la práctica 03, o con
> `BC-Pruebas-semana03` abierto. Vuelve a tu biblioteca original, abre
> `BC-Bootcamp-Resolve` y repite.

---

## 📦 Producto (30 %)

Tu mapa de instalación, tu plan de continuidad y el entorno configurado. Se evalúa con
criterios observables.

### Verificable a simple vista (55 puntos)

| Criterio | Puntos |
| -------- | ------ |
| `mapa-de-instalacion.md` existe en `04-respaldos/` | 5 |
| Las seis rutas del mapa están rellenas, sin casillas vacías | 10 |
| El tamaño del `Project.db` está anotado con su cifra | 5 |
| `plan-de-continuidad.md` existe y responde a las cuatro preguntas | 10 |
| Las tres Working Folders apuntan a `02-cache/` | 10 |
| Existen `CacheClip/` y `.gallery/` en la carpeta de caché | 5 |
| `BC-Bootcamp-Resolve-semana03.drp` existe en `04-respaldos/` | 5 |
| `BC-Bootcamp-Resolve-fase0.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (45 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Los respaldos automáticos están fuera del disco del sistema | 10 |
| Las copias diarias conservadas son 7 o más, y el número está escrito | 5 |
| El `.drp` se ha restaurado y abierto de verdad en `BC-Pruebas-DB` | 10 |
| Las respuestas del plan de continuidad nombran archivos y carpetas concretos | 10 |
| Tres funciones de Studio anotadas, **cada una con su alternativa en Free** | 5 |
| `BC-Resolve/` es la primera entrada de Media Storage | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| `Preferences > User > Project Save and Load` | Live Save activado y respaldos activados |
| Ruta de respaldos, en ese mismo panel | Una ruta de tu disco de trabajo, no del disco del sistema |
| `Project Settings > Master Settings > Working Folders` | Las tres rutas hacia `02-cache/` |
| `Project Settings > Master Settings`, campo `Timeline frame rate` | `24`, y **atenuado** |
| `Preferences > System > Media Storage` | `BC-Resolve/` la primera de la lista |
| `Workspace > Layout Presets` | Aparece el layout `BC-Montaje` |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| El mapa tiene casillas vacías o rutas descritas en vez de escritas | −15 |
| El plan de continuidad responde con intenciones ("debería hacer copias") | −15 |
| Los respaldos automáticos siguen en el disco del sistema | −10 |
| El `.drp` de la semana no se ha probado nunca | −10 |
| Las Working Folders siguen apuntando al disco del sistema | −10 |
| Se movió o se editó a mano algo dentro de la biblioteca de proyectos | −20 |
| No hay respaldo de cierre de fase | −5 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

No pases a la Semana 04 sin haber cerrado esta. A partir de la 04 entra material de
verdad en el proyecto, y todo lo que quede mal configurado hoy se multiplica por
doscientos clips.

- **Si fallan los checks en bloque**: es la biblioteca o el proyecto abierto. Vuelve a
  tu biblioteca original y abre `BC-Bootcamp-Resolve`.
- **Si falla solo `proyecto-de-pruebas`**: o el nombre tiene una errata, o lo creaste
  dentro de una carpeta del Project Manager en vez de en la raíz.
- **Si el cuestionario va por debajo de 70**: las preguntas 5, 6 y 9 son las que más
  gente falla. Vuelve a las teorías 04, 05 y 07.
- **Si el producto va por debajo de 70**: casi siempre es el plan de continuidad
  respondido con intenciones. Reescríbelo nombrando archivos que existan hoy en tu
  disco; si al hacerlo descubres que alguno no existe, ese es justo el agujero que había
  que encontrar.

---

← [Volver a la Semana 03](README.md)
