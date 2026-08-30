# 📊 Rúbrica de evaluación — Semana 09

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en la
tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 09` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Enumera las cinco operaciones de trimming y di, para cada una, si cambia o no la duración total
   de la pieza.
2. Enuncia en una frase la diferencia entre `Selection Mode` y `Trim Edit Mode`. Pon un gesto que
   signifique cosas distintas en cada uno.
3. ¿Qué diferencia hay entre un `Roll` y un `Ripple` sobre el mismo corte? ¿Cuál de los dos puede
   descolocar un rótulo que hay tres minutos más adelante?
4. ¿Qué diferencia hay entre un `Slip` y un `Slide`? ¿De dónde saca cola cada uno?
5. Estás haciendo una operación y en el visor se actualizan **los dos cuadros de abajo**. ¿Qué
   operación estás haciendo y cómo lo sabes?
6. ¿Qué hace el `Sync Lock`? Describe qué le pasa exactamente a una pista de música que cruza el
   punto de un ripple, con el `Sync Lock` activado.
7. ¿Qué hacen `Trim Start` y `Trim End` en cada uno de los dos modos? ¿Sobre qué clips actúan si no
   seleccionas nada?
8. ¿Qué es un split edit? Explica la diferencia entre un corte en L y un corte en J con un ejemplo
   de cada uno.
9. Estás en `Dynamic Trim Mode`. ¿Qué hace la barra espaciadora? ¿Y qué pasa si sales de la
   aplicación sin salir del modo y vuelves mañana?
10. ¿Qué diferencia hay entre un marcador de clip y un marcador de timeline? ¿Cómo se decide cuál
    de los dos pones al pulsar `M`?

<details>
<summary>📝 Respuestas</summary>

**1.** Las cinco, con su efecto sobre la duración total:

| Operación | ¿Cambia la duración? |
| --------- | -------------------- |
| `Resize` | **Sí** — deja hueco o pisa al vecino |
| `Roll` | No |
| `Ripple` | **Sí** |
| `Slip` | No |
| `Slide` | No |

`Ripple` es además la única que puede alterar la sincronía de tramos enteros de la pieza; el propio
manual lo marca con un aviso.

**2.** La regla: **en `Selection Mode` los clips se mueven y los bordes dejan hueco; en
`Trim Edit Mode` los clips deslizan y los bordes recolocan la timeline.**

Gesto que cambia de significado: **arrastrar un rectángulo**. En `Selection Mode` selecciona
**clips**; en `Trim Edit Mode` selecciona **cortes**. También sirve arrastrar el borde de un clip:
`Resize` frente a `Ripple`.

**3.** Un **`Roll`** mueve el corte alargando un clip exactamente lo que acorta el otro: la pieza
dura lo mismo y **nada de lo que viene detrás se mueve**.

Un **`Ripple`** acorta o alarga un clip y desplaza todo lo que viene detrás para cerrar el hueco:
**la pieza cambia de duración**.

El que puede descolocar el rótulo es el **`Ripple`**, porque mueve todo lo posterior. Con el
`Sync Lock` activado, el rótulo se desplazará con el montaje; con él desactivado, se quedará donde
estaba y pasará a rotular el plano equivocado.

**4.** Un **`Slip`** deja el clip donde está y durando lo mismo, y cambia **el tramo de material
que enseña**. Gasta cola **del propio clip**.

Un **`Slide`** deja el clip enseñando lo mismo y lo **mueve de sitio**, ajustando a sus dos
vecinos. Gasta cola **de los vecinos**.

**5.** Un **`Slide`**. El visor partido en cuatro enseña arriba la entrada y la salida del clip que
ajustas, y abajo la salida del vecino de la izquierda y la entrada del de la derecha. En un `Slip`
cambia el contenido del clip, así que se actualizan los de arriba; en un `Slide` cambia dónde
cortan los vecinos, así que se actualizan los de abajo.

**6.** El `Sync Lock` decide si una pista **se desplaza junto con las demás** cuando otra hace
ripple. Está a la derecha del candado en la cabecera y viene activado en todas.

Con el `Sync Lock` activado y una música que cruza el punto del ripple, Resolve **hace un corte en
la música justo en ese punto** y la recorta, para que todo lo que va después conserve su sincronía.
El resultado es que la música queda con un salto ahí, pero la pieza sigue sincronizada. Arreglar un
salto en la música es mucho más fácil que volver a sincronizar la pieza entera.

**7.** `Trim Start` (`Shift+[`) mueve la **entrada** y `Trim End` (`Shift+]`) mueve la **salida** de
los clips hasta la posición del cabezal.

- En **`Selection Mode`** redimensionan
- En **`Trim Edit Mode`** rippean

Si no seleccionas nada, actúan sobre **todos los clips que crucen el cabezal en las pistas con el
selector de pista activado**. Una selección manual gana siempre sobre los selectores.

**8.** Un **split edit** es un corte en el que la imagen y el sonido **no cambian en el mismo
fotograma**.

**Corte en L**: el sonido del plano que **sale** se prolonga bajo la imagen del siguiente. Ejemplo:
alguien termina una frase mientras ya vemos el plano de recurso que ilustra lo que dice.

**Corte en J**: el sonido del plano que **entra** empieza antes que su imagen. Ejemplo: se oye el
ambiente de la calle antes de ver el plano de la calle; el espectador llega antes que la cámara.

**9.** En `Dynamic Trim Mode` la barra espaciadora **no reproduce hacia delante**: ejecuta
`Play Around Current Selection`, es decir, reproduce alrededor de lo que tengas seleccionado.

Si te vas sin salir del modo, mañana `J`, `K` y `L` seguirán **trimando** cada vez que haya algo
seleccionado en vez de reproducir, y la pieza se irá descolocando sin que entiendas por qué. La
señal permanente de que estás dentro es que **el cabezal está amarillo**. Se sale con `W`.

**10.** Un **marcador de clip** vive en la barra de título del clip y **viaja con él** si lo mueves.
Un **marcador de timeline** vive en la regla de tiempo y se queda donde está.

Lo decide la selección: **si hay algo seleccionado, `M` pone un marcador de clip; si no hay nada
seleccionado, lo pone en la timeline.** Por eso conviene deseleccionar todo con `Ctrl+Shift+A`
(Win) / `Cmd+Shift+A` (Mac) antes de una pasada de anotación.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **10 puntos**.

```bash
python scripts/verificar-semana.py 09
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 01 | `proyecto-abierto` | 10 |
| 01 | `frame-rate-bloqueado` | 10 |
| 01 | `montaje-v2-conservada` | 10 |
| 01 | `montaje-v3-existe` | 10 |
| 01 | `montaje-v3-activa` | 10 |
| 01 | `montaje-v3-pistas-con-nombre` | 10 |
| 01 · 04 | `marcadores-anotados` | 10 |
| 02 | `montaje-v3-clips` | 10 |
| 02 · 04 | `montaje-v3-sin-huecos` | 10 |
| 04 | `montaje-v3-split-edits` | 10 |

**Necesitas 70 / 100**, es decir **al menos 7 de los 10 checks**.

> [!TIP]
> Seis de los diez —`montaje-v3-activa`, `montaje-v3-pistas-con-nombre`, `montaje-v3-clips`,
> `montaje-v3-sin-huecos`, `montaje-v3-split-edits` y `marcadores-anotados`— leen **la timeline
> activa**. Si te quedaste comparando en `BC-Montaje-v2` en el paso 8 de la práctica 04, fallan los
> seis de golpe aunque el trabajo esté perfecto. Doble clic en `BC-Montaje-v3` y repite: es lo
> primero que hay que descartar.
>
> Si fallan **todos**, el puente no está lanzado: `Workspace > Scripts > Utility`.

---

## 📦 Producto (30 %)

Tu montaje afinado y las decisiones que lo afinaron. Se evalúa con criterios observables.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| La pieza se reproduce entera sin que te distraigas en ningún momento | 15 |
| No hay ningún parpadeo a negro en toda la reproducción | 10 |
| Ninguna voz va desincronizada con su imagen | 10 |
| `notas-de-montaje.md` tiene el apartado `## Trimming — Semana 09` con sus seis bloques | 5 |
| Las cifras del apartado son cifras: duración antes, duración después, segundos quitados | 5 |
| `BC-Bootcamp-Resolve-semana09.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Ningún plano se hace largo: no hay sitios donde esperes al corte siguiente | 15 |
| Los split edits suenan intencionados, no a error de sincronía | 10 |
| El corte que más ha mejorado está identificado, con la operación que lo arregló | 5 |
| La comparación teclado frente a `Dynamic Trim` está contestada con cortes concretos | 10 |
| Los marcadores que quedan describen trabajo real, entendible sin explicación | 10 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| El media pool | `BC-Montaje-v2` y `BC-Montaje-v3`, las dos, colgando de `Master` |
| Las duraciones de las dos timelines | La v3 dura menos que la v2, y sabes cuánto |
| Las cinco cabeceras de `BC-Montaje-v3` | Nombre propio, ninguna apagada, ninguna en solo, `Sync Lock` activado |
| El cabezal | No está amarillo: no te quedaste en `Dynamic Trim Mode` |
| La barra de herramientas | `Snapping` y `Linked Selection` activados |
| Los bordes de los clips en un split edit | El del audio y el del vídeo no están alineados |
| `Index > Markers` | Ocho o más, con nombre propio, y con colores que significan algo |
| La pieza entera | Ni música, ni títulos diseñados, ni color, ni estabilización, ni retimes |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| `BC-Montaje-v2` ha desaparecido o se ha afinado encima | −20 |
| La pieza tiene un parpadeo a negro | −15 |
| Una voz va desincronizada con su imagen | −15 |
| La duración no ha bajado nada: solo se hicieron `Roll` | −10 |
| `Linked Selection` quedó apagado al cerrar la semana | −10 |
| Los marcadores conservan sus nombres de fábrica | −10 |
| El apartado de notas describe con adjetivos y no con cifras y cortes concretos | −10 |
| Se empezó a estabilizar o a retimar, que es la Semana 10 | −5 |
| Alguna pista quedó apagada, en solo o sin `Sync Lock` | −5 |
| Se quedó activo el `Dynamic Trim Mode` | −5 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

Esta semana no bloquea la 10 —la velocidad y la estabilización se pueden aprender sobre un montaje
sin afinar—, pero sí bloquea el resto de la Fase 3 en la práctica: los títulos de la Semana 11 y el
multicámara de la 12 se colocan al fotograma, y colocar al fotograma es esto.

- **Si fallan `montaje-v3-activa` y los cinco siguientes**: tienes abierta `BC-Montaje-v2`. Doble
  clic en `BC-Montaje-v3`. Es lo primero que hay que descartar, siempre.
- **Si falla `montaje-v2-conservada`**: renombraste el montaje en vez de duplicarlo. Recupéralo del
  respaldo `BC-Bootcamp-Resolve-semana08.drp`, importándolo con otro nombre para no machacar lo que
  tienes.
- **Si falla `montaje-v3-clips`**: has quitado demasiados planos. Eso ya no es afinar, es remontar.
  Restaura el respaldo de timeline `antes-de-afinar` de la práctica 01 y vuelve a empezar con más
  criterio sobre qué sobra de verdad.
- **Si falla `montaje-v3-sin-huecos`**: hay un hueco o un solape. Casi siempre es de borrar un plano
  con `Supr` en vez de con `Forward Delete`, o de un `Slide` que se quedó a medias. Recorre la pista
  en `Detail Zoom`.
- **Si falla `montaje-v3-split-edits`**: o no llegaste a hacerlos, o los hiciste sobre `Ambiente` en
  vez de sobre la primera pista de audio. El check mira la primera pista de vídeo y la primera de
  audio.
- **Si falla `marcadores-anotados`**: o tienes menos de ocho, o alguno conserva su `Marker N` de
  fábrica. Ordena el `Marker Index` por `Name` y los que quedan por renombrar salen juntos.
- **Si el cuestionario va por debajo de 70**: las preguntas 3, 6 y 7 son las que más gente falla, y
  las tres son el mismo tema de fondo —qué se mueve cuando algo cambia de duración—. Vuelve a las
  teorías 03 y 07.
- **Si el producto va por debajo de 70**: casi siempre es una de dos. O te saltaste la pasada de
  visionado de la práctica 01 y afinaste lo primero que viste, o afinaste con el ratón y te quedaste
  sin tiempo a la mitad. Lo primero se arregla dedicándole veinte minutos a ver la pieza entera y
  rehacer la lista; lo segundo, con las nueve teclas de la teoría 05.
- **Si te faltó tiempo**: prioriza las prácticas 01 y 02. Los split edits de la práctica 04 se
  pueden hacer otro día en veinte minutos; la pasada de visionado con ojos limpios, no.

---

← [Volver a la Semana 09](README.md)
