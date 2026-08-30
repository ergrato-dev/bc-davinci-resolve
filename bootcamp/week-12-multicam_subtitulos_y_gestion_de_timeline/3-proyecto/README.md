# Proyecto — Semana 12: la pieza que se entiende sin sonido

> Tu pieza ya se entiende: está montada, afinada y rotulada. Lo que no está es **disponible para
> quien no puede oírla, para quien no habla tu idioma, y para el programa de al lado**. Esta semana
> cierra la Fase 3 quitando esas tres barreras.

## 📦 Qué añade esta semana

La duodécima capa: **`BC-Montaje-v6`, la pieza subtitulada**, y con ella el cierre de la Fase 3.

Cinco cosas:

1. **`BC-Montaje-v6`**, duplicada de `BC-Montaje-v5`, con una **pista de subtítulos** nombrada con
   su código de idioma y **ocho subtítulos o más** escritos con criterio.
2. **Un estilo de subtítulos propio**, dado una vez a la pista entera y guardado como preajuste.
3. **`BC-Multicam-v1`**, la escena montada con el Multicam Viewer a partir del clip
   `BC-Multicam-01` que sincronizaste en la práctica 01.
4. **`BC-Intercambio-v1`**, tu timeline exportada a XML y vuelta a importar, con la lista escrita de
   lo que se perdió por el camino.
5. **El bin `14-Intercambio`**, con el `.srt` exportado y la timeline reimportada.

> [!IMPORTANT]
> `BC-Montaje-v5` **no se toca**. Es la referencia de la Semana 11 y el check
> `montaje-v5-conservada` la busca. Es la convención de versionado de
> [`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md): cada fase duplica y
> trabaja sobre la copia.

Y dos cosas que no son archivos:

**El reparto de pistas, completo.** `V1` el montaje, `V2` los rótulos, `V3` los ajustes, y ahora
`ST1` los subtítulos. Cuatro capas con un sitio cada una, que es lo que va a permitir que las
Semanas 13 a 22 añadan las suyas encima sin que nada se pise.

**El proyecto aligerado.** Las timelines de las semanas 01 a 04 desactivadas, los respaldos
automáticos encendidos, y un punto de respaldo con nombre antes de la parte peligrosa. La Fase 4
empieza sobre un proyecto que abre rápido.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca carácter a
carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. **`BC-Montaje-v5`** sigue existiendo
3. **`BC-Montaje-v6`** existe y es la timeline abierta
4. Su pista de vídeo **1** conserva **quince clips o más**
5. Esa pista **no tiene huecos ni solapes**
6. Tiene una **pista de subtítulos con ocho subtítulos o más**
7. Esa pista **está renombrada**: no se llama `Subtitle 1`
8. La timeline **`BC-Multicam-v1`** existe
9. La timeline **`BC-Intercambio-v1`** existe
10. El bin **`14-Intercambio`** contiene **dos elementos o más**

```bash
python scripts/verificar-semana.py 12
```

Con el proyecto abierto, **`BC-Montaje-v6` como timeline activa** y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!WARNING]
> **Cinco de los diez checks leen la timeline activa**: del 3 al 7. Hay **tres** formas de tenerla
> equivocada esta semana, una más que en la Semana 11:
>
> 1. Te quedaste en **`BC-Multicam-v1`** después de la práctica 02
> 2. **Abriste el clip multicámara con `Open in Timeline` y no volviste**
> 3. Abriste **`BC-Intercambio-v1`** para compararla y ahí se quedó
>
> Mira el control de ruta de la esquina inferior izquierda: si hay dos nombres, estás dentro de un
> contenedor. Y mira qué nombre lleva la pestaña de la timeline.
>
> *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de 2026.*

### Qué mide cada check, y qué no ve

Esta semana la API ve **más** que en la Semana 11, porque las pistas de subtítulos y sus clips sí se
exponen. Pero sigue sin ver lo importante: **qué pone dentro**.

| Lo que el check mira | Lo que **no** puede saber |
| -------------------- | ------------------------- |
| Que hay una pista de subtítulos con ocho clips | Que el texto diga lo que se dice |
| Que la pista tiene nombre propio | Que ese nombre sea un código de idioma válido |
| Que `BC-Multicam-v1` existe | Que dentro haya cambios de cámara, ni si están bien puestos |
| Que `BC-Intercambio-v1` existe | Que la hayas comparado con la original |
| Que `14-Intercambio` tiene dos elementos | Que uno sea el `.srt` y otro la timeline |

El check 7 comprueba que el nombre de la pista **no empieza por `Subtitle `**, que es el nombre de
fábrica. No puede validar que `es-ES` sea correcto: eso lo juzga la rúbrica.

Y hay un límite que conviene tener presente: **la timeline activa es una sola**, así que los checks
no pueden mirar dentro de `BC-Multicam-v1` mientras miran dentro de `BC-Montaje-v6`. Por eso el
multicámara se verifica por existencia y su calidad va entera a la rúbrica.

### Lo que no se puede verificar por API, y dónde se evalúa

| No verificable | Dónde se evalúa |
| -------------- | --------------- |
| Si los ángulos están sincronizados al fotograma | Rúbrica, criterio observable |
| Si los cambios de cámara caen donde tienen que caer | Rúbrica, criterio observable |
| Si se conmutó solo vídeo o también audio | Notas escritas + rúbrica |
| Si los subtítulos entran y salen con la voz | Rúbrica, criterio observable |
| Si el texto está bien cortado y bien resumido | Rúbrica, criterio observable |
| Si el estilo de subtítulos se lee sobre la imagen | Rúbrica, criterio observable |
| Qué se perdió en el viaje de ida y vuelta | Notas escritas + rúbrica |
| Si se leyó la estimación de Media Management | Notas escritas |

---

## 📝 El entregable escrito

### `notas-de-montaje.md`, apartado `## Multicámara y subtítulos — Semana 12`

En `BC-Resolve/04-respaldos/`, en el mismo archivo de las Semanas 06 a 11.

Se abre en la práctica 01 y se cierra en la práctica 04. Al final tiene que llevar cuatro bloques:

> **El clip multicámara**: qué método de sincronía elegiste **y por qué**; si cuadró a la primera y
> qué hiciste si no; cómo se llaman tus ángulos.
>
> **El montaje multicámara**: cuántos cambios de cámara, qué ángulo domina y por qué; qué arreglaste
> después y con qué herramienta —conmutación, trim o borrar el corte—; si conmutaste solo vídeo y por
> qué.
>
> **Los subtítulos**: el nombre de la pista y su idioma; cuántos y de qué duración media; los tres
> umbrales que fijaste; cuántos CPS en rojo te quedaron y qué hiciste; qué subtítulo lleva
> `Customize Caption` y por qué.
>
> **El intercambio y la gestión**: el tamaño del `.xml` y el del `.drt`; **qué sobrevivió al viaje de
> ida y vuelta y qué no**; qué timelines desactivaste; los tres tamaños que te dio la estimación de
> Media Management; y qué pasa a la Fase 4.

El que más vale es el cuarto, y dentro de él la lista de **lo que no sobrevivió**. Es el único
apartado del bootcamp que se escribe mirando un fallo, y es la información que evita la sorpresa el
día que tengas que mandar una timeline de verdad.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| Los ángulos del multicámara cuadran al fotograma | Se busca un sonido seco, se amplía a fotogramas y se compara |
| Ningún cambio de cámara llega tarde ni pronto | Se reproduce la escena entera y se mira si algún corte tropieza |
| El montaje multicámara no cambia por cambiar | Ningún cambio sin motivo: el plano ya había dicho lo suyo |
| El audio no salta en cada corte | Se escucha con auriculares: se conmutó solo vídeo |
| Todos los subtítulos dentro del título seguro | Se encienden las guías y se reproduce |
| Los subtítulos entran con la voz y salen con la voz | Se reproduce mirando el pie de imagen |
| Ningún subtítulo cruza un corte a otra escena | Se mira cada corte de escena |
| Ningún subtítulo de más de dos líneas | Se recorre la lista del panel `Captions` |
| Las líneas están cortadas donde la frase respira | Se lee: no separan artículo de sustantivo |
| El texto está resumido, no transcrito | No hay muletillas ni titubeos en pantalla |
| Se leen sobre cualquier fondo de la pieza | Se reproduce entera mirando solo el texto |
| Se leen en un móvil | Se reduce el visor a un cuarto y se lee |
| Ninguna falta de ortografía | Se repasa el `.srt` exportado, que es texto plano |
| El nombre de la pista es un código de idioma real | `es-ES`, `en-US`, `fr-FR`… no «Español» ni `Subtitle 1` |
| La comparación del intercambio nombra cosas concretas | Se lee la nota: dice qué se perdió, no «bastantes cosas» |
| Nada de lo que todavía no toca | Ni etalonaje, ni mezcla, ni composición |

Dos tentaciones concretas de esta semana. La primera: **aplanar el clip multicámara** para «dejarlo
limpio». No se hace; quedan once semanas y cambiar de ángulo va a hacer falta. La segunda:
**ejecutar Media Management** porque la ventana está abierta y parece inofensiva. No lo es: escribe
en disco y puede cambiar a qué archivos apunta el proyecto. Esta semana se lee y se cancela.

---

## 💡 Adaptación a tu pieza

**Documental corto** · Tu semana es la más redonda de las cinco: tienes entrevista y tienes voz. Los
subtítulos son la transcripción de lo que dicen tus personajes, y el multicámara es literalmente tu
material si grabaste la entrevista con dos cámaras. Si no, el ejercicio va sobre el material del
pack. Cuidado con una cosa: **subtitula lo que quedó en el montaje**, no la entrevista entera.

**Videoclip** · Tu pieza no tiene diálogo, así que tus subtítulos son **la letra de la canción**. Es
un caso real y con reglas propias: los versos se cortan por verso, no por longitud, y entran con la
voz que canta. El multicámara es un ejercicio aparte, con el material del pack, y es de los que más
te va a servir: un directo con varias cámaras es multicámara puro.

**Cortometraje de ficción** · Tus subtítulos son diálogo, y aquí es donde importan las reglas de
oficio: se resume, se corta bien y no se cruzan cortes de escena. Si tu corto tiene una escena de
diálogo rodada con dos cámaras, esa es tu escena multicámara; si no, el material del pack. Y una
convención que te toca: **los sonidos fuera de campo van entre corchetes** si estás haciendo
subtítulos para sordos.

**Tutorial o vídeo formativo** · Es el formato que más gana esta semana, por dos motivos. Uno: el
tutorial se ve mudo más que ningún otro formato, así que **los subtítulos son parte del producto**,
no un extra. Dos: el tutorial suele grabarse con dos cámaras —el plano de quien habla y el detalle
de lo que hace— y eso es multicámara con dos ángulos, que funciona igual de bien.

**Pieza de viaje o vlog** · Tus subtítulos son la voz en off, si la tienes, o los rótulos de
localización convertidos en subtítulos si no. El multicámara va con el material del pack. Y presta
atención al paso de Media Management: es el formato que más material descartado acumula, y la
diferencia entre `All media` y `Used media and trim` va a ser espectacular.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 12` en verde, diez de diez
2. `BC-Montaje-v6` abierta, **fuera** de cualquier clip multicámara y de cualquier otra timeline
3. `BC-Montaje-v5` intacta
4. Ocho subtítulos o más, todos dentro del rectángulo `Title`
5. La pista de subtítulos con su código de idioma
6. `BC-Multicam-v1` montada con el Multicam Viewer y **sin aplanar**
7. `BC-Intercambio-v1` importada y comparada, con la lista escrita
8. `14-Intercambio` con el `.srt` y la timeline
9. `notas-de-montaje.md` con el apartado `## Multicámara y subtítulos — Semana 12` cerrado, con sus
   cuatro bloques
10. Respaldo de la semana: `File > Export Project` →
    `04-respaldos/BC-Bootcamp-Resolve-semana12.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza la **práctica 03**: los subtítulos son la capa que se queda en tu
> pieza y la que arrastra al resto del bootcamp. El multicámara de la práctica 02 es una habilidad
> aparte y se recupera en un rato; el ejercicio de intercambio de la 04, en veinte minutos. Los
> subtítulos, no: la Fase 4 se mezcla sobre una pieza que ya tiene su capa de texto.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Subtitular sobre `BC-Montaje-v5` | Parece más práctico | Se duplica; el check la busca intacta |
| Subtitular con clips de `Text+` | Es lo que se aprendió la semana pasada | Pista de subtítulos: los `Text+` no se exportan como texto |
| Dejar la pista llamada `Subtitle 1` | Nadie avisa de que hay que renombrarla | El nombre viaja al archivo exportado |
| Escribir antes de dar el estilo | Es el orden natural | Estilo primero: si no, se escribe leyendo mal |
| Transcribir literalmente | Parece lo riguroso | Se resume: lo que se dice, no cómo |
| Subtítulos de tres líneas | El texto no cabía en dos | Se corta la frase en dos subtítulos |
| Montar multicámara sin comprobar la sincronía | La miniatura se ve bien | Un minuto en un sonido seco, antes de cortar |
| Conmutar vídeo y audio en una entrevista | Es el valor por defecto | `Video Only` |
| Aplanar el clip multicámara | «Para dejarlo limpio» | Irreversible; quedan once semanas |
| Dejar `Automatically set project settings` marcado al importar | Viene marcado | Puede cambiar la cadencia del proyecto |
| Importar el XML encima de la timeline actual | Se confunde importar con abrir | Crea una timeline nueva: cámbiale el nombre |
| Pulsar `Start` en Media Management | La ventana invita | Se lee y se cancela; consolidar es la Semana 30 |
| Verificar desde `BC-Multicam-v1` | Es la última que tocaste | Cinco checks leen la timeline activa |
| Desactivar `BC-Montaje-v5` o `v6` | Se seleccionan de más | `Enable Timeline` |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 11](../../week-11-titulos_texto_plus_efectos_y_compuestos/3-proyecto/README.md) | **Proyecto Semana 12** | [Semana 13](../../week-13-fairlight_anatomia_y_mezcla_base/README.md) |

← [Volver a la Semana 12](../README.md)
