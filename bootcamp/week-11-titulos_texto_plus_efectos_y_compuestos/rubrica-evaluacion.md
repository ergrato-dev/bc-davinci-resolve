# 📊 Rúbrica de evaluación — Semana 11

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en la
tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 11` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Arrastras un `Text+` a la pista donde está tu montaje. ¿Qué pasa exactamente y por qué? ¿Qué
   propiedad de un título hace que colocado en la pista de arriba sí funcione?
2. ¿Qué es rich text? Di qué generador de títulos de Resolve 21 **no** lo soporta y qué ofrece a
   cambio.
3. Necesitas un rótulo con un nombre grande y un cargo pequeño debajo, y además que el nombre
   aparezca letra a letra. ¿Se puede con un solo `Text+`? Explica por qué, y da las dos salidas.
4. Nombra los cuatro paneles principales del Inspector de un `Text+` y di qué se ajusta en cada
   uno. ¿En cuál está la fuente? ¿En cuál se mueve el rótulo entero por el cuadro?
5. Tienes un rótulo blanco que se lee perfectamente en el fotograma donde lo colocaste y
   desaparece tres segundos después. ¿Qué ha pasado y cuáles son las cuatro soluciones, de menos a
   más invasiva?
6. ¿De dónde sale el material de una transición? ¿Qué te ofrece Resolve cuando no hay bastante, y
   cuál de esas opciones modifica tu montaje?
7. Un corte cae justo sobre un golpe de música y quieres poner una disolución de un segundo. ¿Qué
   alineación eliges y por qué? ¿Qué pasaría con las otras dos?
8. ¿Qué parámetro tienen **todos** los ResolveFX sin excepción y para qué sirve? ¿Qué se hace con
   él cuando un efecto «funciona pero se nota demasiado»?
9. Tienes un adjustment clip en la `V3`, rótulos en la `V2` y el montaje en la `V1`. Le aplicas un
   desenfoque. ¿A qué afecta? ¿Y si lo bajas a la `V2` y subes los rótulos a la `V3`?
10. Empaquetas cuatro planos en un compound clip. Menciona una ventaja concreta que ganas ahora y
    un coste concreto que vas a pagar en la Fase 5. ¿Y qué le pasa a la timeline activa mientras lo
    tienes abierto con `Open in Timeline`?

<details>
<summary>📝 Respuestas</summary>

**1.** Resolve hace una **edición de sobrescritura**: el título ocupa el sitio del plano y ese
trozo de imagen desaparece del montaje. Un título es un clip como otro, no un texto que se pegue
encima.

Lo que hace que funcione en la pista de arriba es el **canal alpha**: casi todo el título tiene
alpha 0 —transparente— y solo las letras, la sombra y el fondo tienen alpha por encima de 0. Una
pista de vídeo tapa a las de debajo **solo donde es opaca**.

**2.** **Rich text** es poder seleccionar un trozo del texto y darle un estilo distinto al del resto
dentro del mismo clip: tres líneas, tres tamaños, tres colores, un solo generador.

El que **no** lo soporta es **`Text+`**: todo su texto comparte un único estilo. A cambio ofrece
`Write On` y `Write Off` con keyframes, disposición sobre punto, marco, círculo o trayectoria,
transformación y animación por carácter, por palabra y por línea, y hasta **ocho elementos de
sombreado** independientes.

**3.** **No se puede con un solo `Text+`.** El nombre grande y el cargo pequeño son dos estilos, y
`Text+` tiene uno.

Las dos salidas:

- **Dos clips de `Text+`** superpuestos, uno con el nombre y otro con el cargo, cada uno con su
  estilo y su animación
- **Un `MultiText`**, que está construido sobre `Text+` y añade una lista de capas de texto, cada
  una con su estilo, dentro de un solo clip

**4.**

| Panel | Qué se ajusta |
| ----- | ------------- |
| **`Text`** | Qué pone y con qué tipografía. **Aquí está `Font`** |
| **`Layout`** | Dónde va y con qué forma: `Point`, `Frame`, `Circle`, `Path` |
| **`Transform`** | Animar y deformar **por carácter, por palabra o por línea** |
| **`Shading`** | Cómo está pintado: los ocho elementos de relleno, contorno, sombra y borde |

El rótulo **entero** se mueve por el cuadro desde **`Settings > Transform`**, que es el mismo grupo
que tiene cualquier clip. No desde el panel `Transform` de `Text+`, que mueve el texto por dentro.

**5.** Ha pasado que **el fondo se mueve**: el plano se ha abierto a una zona clara y el rótulo
blanco ha dejado de contrastar. Un rótulo no se juzga en un fotograma, se juzga reproduciendo su
tramo entero.

Las cuatro soluciones:

1. **Contorno**: elemento de sombreado con apariencia de contorno, color opuesto, `Outside Only`
2. **Sombra**: elemento de sombreado con apariencia de sombra, negro al 40-60 %, desplazada
3. **Fondo**: el grupo `Background` de los generadores clásicos, o `Layout > Background Color` en
   `Text+`
4. **Rebajar la imagen** con un adjustment clip que oscurezca la zona

**6.** Sale de las **colas** (*handles*): los fotogramas que quedaron fuera al recortar cada plano y
que siguen en el archivo. Una transición necesita que los dos planos se **solapen**, y ese solape se
paga con cola del plano que sale y cola del que entra.

Cuando no hay bastante, Resolve ofrece tres opciones: **`Trim Clips`**, **`Skip Clips`** y
**`Cancel`**.

La que modifica el montaje es **`Trim Clips`**: acorta los dos lados del punto de edición para
crear el solape. No deja hueco, pero los planos dejan de durar lo que decidiste.

**7.** **`End on Edit`**: la transición termina justo en el corte, así que el plano nuevo llega
**nítido** en el instante del golpe.

Con `Center on Edit`, el golpe cae a mitad de disolución y las dos imágenes están al 50 %: el
instante se emborrona. Con `Start on Edit`, la transición empieza en el corte, así que en el golpe
todavía se ve el plano anterior.

**8.** El parámetro **`Blend`**, al final de los parámetros de cada filtro. Mezcla el resultado del
efecto con la imagen original: a `0` no se aplica nada, a `1` se aplica entero.

Cuando un efecto se nota demasiado, **se baja `Blend`**. Tocar sus parámetros cambia el carácter del
efecto; `Blend` cambia solo la cantidad.

**9.** En la **`V3`** afecta a **todo lo que tiene debajo**: los rótulos de la `V2` **y** el montaje
de la `V1`. El texto sale desenfocado.

Bajándolo a la `V2` y subiendo los rótulos a la `V3`, el adjustment clip solo tiene debajo el
montaje: desenfoca la imagen y **los rótulos quedan nítidos**, porque están por encima.

Las dos configuraciones son válidas. La que hay que elegir depende de si el efecto es del cuadro
—un grano de película, que sí debería tocar el texto— o de la imagen —un desenfoque, que casi nunca
debería—.

**10.**

- **Ventaja**: el bloque se comporta como **un solo clip**, así que se le puede poner **una sola
  transición** y un solo juego de controles del Inspector
- **Coste en la Fase 5**: un compuesto aparece como **un solo nodo `MediaIn`** en Fusion y se
  etalona como **un solo clip** en Color. Esos cuatro planos son un solo grado, y para etalonarlos
  por separado hay que abrir el compuesto con `Open in Timeline` cada vez

Mientras lo tienes abierto, **la timeline activa es el compuesto**, no `BC-Montaje-v5`. Siete de los
diez checks de la semana leen la timeline activa y fallan de golpe. El control de ruta de la esquina
inferior izquierda es lo que avisa: si hay dos nombres, estás dentro.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **10 puntos**.

```bash
python scripts/verificar-semana.py 11
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 01 | `proyecto-abierto` | 10 |
| 01 | `montaje-v4-conservada` | 10 |
| 01 | `montaje-v5-activa` | 10 |
| 01 | `montaje-v5-clips` | 10 |
| 01 · 03 | `montaje-v5-sin-huecos` | 10 |
| 01 | `marcadores-de-rotulo` | 10 |
| 01 · 03 | `marcadores-de-efecto` | 10 |
| 02 | `rotulos-en-v2` | 10 |
| 03 | `capa-de-ajuste` | 10 |
| 02 · 04 | `bin-de-titulos` | 10 |

**Necesitas 70 / 100**, es decir **al menos 7 de los 10 checks**.

> [!TIP]
> Siete de los diez —`montaje-v5-activa`, `montaje-v5-clips`, `montaje-v5-sin-huecos`,
> `rotulos-en-v2`, `capa-de-ajuste`, `marcadores-de-rotulo` y `marcadores-de-efecto`— leen **la
> timeline activa**. Esta semana hay **dos** formas de tenerla equivocada:
>
> 1. Te quedaste comparando en `BC-Montaje-v4` en el paso 7 de la práctica 04
> 2. **Abriste un compound clip y no volviste**: mira el control de ruta de la esquina inferior
>    izquierda de la timeline. Si hay dos nombres, estás dentro del compuesto
>
> Es lo primero que hay que descartar, siempre. Si fallan **todos**, el puente no está lanzado:
> `Workspace > Scripts > Utility`.

---

## 📦 Producto (30 %)

Tu pieza rotulada. Se evalúa con criterios observables, y esta semana el producto pesa más de lo que
dice el porcentaje: **los checks cuentan clips por pista, no efectos**, porque la API de scripting no
expone qué efecto lleva un clip ni qué pone dentro de un título. Casi todo lo que se aprende aquí se
juzga mirando.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Todos los rótulos dentro del rectángulo `Title`, con las guías encendidas | 10 |
| Ningún rótulo se pierde sobre su fondo en ningún fotograma de su tramo | 10 |
| Todos los rótulos comparten estilo: misma fuente, mismo cuerpo, misma posición | 10 |
| Ninguna falta de ortografía, y los subrayados del corrector apagados | 5 |
| No hay parpadeos a negro en toda la reproducción | 5 |
| `notas-de-montaje.md` tiene el apartado `## Títulos y efectos — Semana 11` con sus cuatro bloques | 5 |
| `BC-Bootcamp-Resolve-semana11.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Cada rótulo aporta un dato que la imagen no da, y ninguno sobra | 15 |
| Cada transición dice algo que el corte no dice, y las descartadas están justificadas por escrito | 10 |
| El generador elegido para el título de entrada está justificado con la pregunta de la teoría 02 | 5 |
| El efecto del adjustment clip está dosificado con `Blend`, no puesto al máximo | 5 |
| El adjustment clip afecta a lo que tenía que afectar, y eso era la intención | 5 |
| Los rótulos duran lo que se tarda en leerlos dos veces, ni más ni menos | 5 |
| El compound clip tiene un motivo escrito, y no es «para ordenar» | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| El media pool | `BC-Montaje-v4` y `BC-Montaje-v5`, las dos, colgando de `Master` |
| El bin `13-Titulos` | El estilo de rótulo y el compuesto, los dos con nombre propio |
| Las cabeceras de las pistas | Tres pistas de vídeo, y sabes qué hay en cada una |
| La `V1` | Solo montaje. Ni un título, ni un adjustment clip |
| La `V2` | Solo rótulos, todos con el mismo aspecto |
| El `Inspector` de un rótulo, pestaña `Title` | Contorno y sombra puestos, con `Outside Only` marcado |
| El `Inspector` del adjustment clip | Un nombre propio, y un `Blend` por debajo de 1 |
| Las transiciones de la timeline | Las reconoces todas: ninguna es un arrastre accidental |
| El `Inspector` de una transición | La alineación es la que decidiste, no la de fábrica |
| El `Smooth Cut`, si lo hay | Entre 2 y 6 fotogramas, no un segundo |
| El control de ruta de la timeline | **Un solo nombre**: estás fuera del compuesto |
| `Index > Markers` | Los amarillos y verdes resueltos pasados a azul; los que quedan son trabajo real |
| La pieza entera | Ni etalonaje, ni mezcla, ni multicámara, ni subtítulos |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| `BC-Montaje-v4` ha desaparecido o se ha trabajado encima | −20 |
| Un título arrastrado a la `V1` se ha comido un plano y se ha entregado así | −15 |
| Un rótulo no se lee sobre su fondo en parte de su tramo | −10 |
| Los rótulos tienen estilos distintos entre sí | −10 |
| Hay una falta de ortografía en un rótulo | −10 |
| Se aceptó `Trim Clips` sin mirar y el ritmo de un punto quedó peor que en la v4 | −10 |
| Hay más transiciones que marcadores verdes, sin justificación escrita | −10 |
| Se empaquetó más de un tercio del montaje en compound clips | −10 |
| El adjustment clip desenfoca los rótulos sin que fuera la intención | −5 |
| El apartado de notas describe con adjetivos y no con planos y minutos | −5 |
| Se empezó a etalonar con un adjustment clip, que es la Semana 21 | −5 |
| Se quedaron los subrayados del corrector encendidos | −5 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

Esta semana **sí bloquea parcialmente la 12**: los subtítulos de la Semana 12 se apoyan en las
pistas y en el criterio de legibilidad que se montan aquí, y la gestión de timeline se apoya en
entender qué es un compuesto. Si vas justo, cierra al menos las prácticas 01 y 02.

- **Si fallan `montaje-v5-activa` y los seis siguientes**: la timeline activa no es `BC-Montaje-v5`.
  Dos causas posibles y las dos frecuentes: te quedaste en la v4 comparando, o **estás dentro de un
  compound clip**. Control de ruta de la esquina inferior izquierda, doble clic en el nombre de la
  izquierda. Es lo primero que hay que descartar.
- **Si falla `montaje-v4-conservada`**: renombraste el montaje en vez de duplicarlo. Recupéralo del
  respaldo `BC-Bootcamp-Resolve-semana10.drp`, importándolo con otro nombre para no machacar lo que
  tienes.
- **Si falla `montaje-v5-clips`**: o has borrado planos —esta semana no se remonta—, o has
  empaquetado demasiados clips en un compound clip, que cuenta como uno. `Decompose in Place` y
  empaqueta menos, o restaura el respaldo `antes-de-rotular`.
- **Si falla `montaje-v5-sin-huecos`**: casi siempre es un plano borrado para hacerle sitio a un
  rótulo. Los rótulos van en la `V2`, nunca en la `V1`. Recorre la pista en `Detail Zoom` y cierra
  con `Forward Delete`.
- **Si falla `rotulos-en-v2`**: o tienes menos de tres, o están en otra pista. Y si además falla
  `montaje-v5-clips`, los pusiste en la `V1` y se han comido planos: `Ctrl+Z` hasta antes de eso.
- **Si falla `capa-de-ajuste`**: el adjustment clip está en la `V2` o más abajo. Súbelo a la `V3`:
  tiene que estar **por encima** de todo lo que quiere afectar.
- **Si falla `bin-de-titulos`**: o el bin no se llama exactamente `13-Titulos`, o le falta uno de los
  dos elementos. El estilo de rótulo se guarda arrastrando el título de la timeline al media pool
  (práctica 02, paso 5); el compuesto cae en el bin que estuviera **activo** al crearlo (práctica 04,
  paso 2), y si cayó en `Master` basta con arrastrarlo.
- **Si fallan los checks de marcadores**: o tienes menos de los que pide, o alguno conserva su
  `Marker N` de fábrica, o el color no es el que espera el check: **`Yellow`** para rótulos,
  **`Green`** para transiciones y efectos. Ordena el `Marker Index` por `Name`.
- **Si el cuestionario va por debajo de 70**: las preguntas 3, 6 y 9 son las que más gente falla. La
  3 es la teoría 02 y se arregla releyendo la tabla de generadores; la 6 es la teoría 06 y se
  arregla entendiendo qué es una cola; la 9 es la teoría 08 y se arregla mirando el orden de las
  pistas, que es la misma idea que la teoría 01.
- **Si el producto va por debajo de 70**: casi siempre es una de dos. O los rótulos tienen estilos
  distintos porque se hicieron uno a uno —se arregla borrándolos y colocándolos desde el estilo
  guardado, y son veinte minutos—, o hay más transiciones de las que la pieza pedía —se arregla
  quitando las que no contestan a «¿qué dice esta transición que el corte no dice?»—.
- **Si te faltó tiempo**: prioriza las prácticas 01 y 02, y de la 03 quédate con el paso 6, el
  adjustment clip. Es el concepto que más se usa de aquí a la Semana 36.

---

← [Volver a la Semana 11](README.md)
