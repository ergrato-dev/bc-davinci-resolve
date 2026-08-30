# Práctica 03 — Slip, slide y el dynamic trim

> Al terminar habrás arreglado tres cortes que no se arreglaban moviéndolos, habrás usado el
> editor de trim de precisión y habrás afinado un corte con la pieza en marcha. Son las tres
> técnicas que la mayoría de la gente nunca llega a usar.

**Duración estimada**: 55 min
**Prerrequisitos**: [Práctica 02](02-ripple-y-roll-sobre-tu-montaje.md), [Teoría 04](../1-teoria/04-slip-y-slide.md), [Teoría 06](../1-teoria/06-jkl-y-el-dynamic-trim.md)

## Contexto

En la práctica anterior movías cortes. Aquí no se mueve ningún corte: se cambia **lo que se ve
dentro** de un plano y **dónde cae** ese plano, sin que la pieza cambie de duración.

Es la parte de la semana que parece magia la primera vez y que a partir de la tercera se usa
todos los días.

---

## Paso 1: Encontrar los planos que piden un `Slip`

**Por qué**: un `Slip` no arregla cualquier cosa. Arregla exactamente un problema: el plano está
bien colocado y dura bien, pero enseña el momento equivocado.

Recorre tu pieza y busca **tres** planos donde pase alguna de estas cosas:

- El plano de apoyo está quieto, y medio segundo después hay un gesto que sí cuenta algo
- El plano de detalle entra con la acción ya empezada
- El corte se nota porque el movimiento no continúa de un plano al siguiente

Ponles un marcador 🔵 con la nota *«candidato a slip»* mientras los buscas, para no perderlos.

**Verifica**: tienes tres planos identificados y sabes qué querrías ver en cada uno.

---

## Paso 2: Tres `Slip`, con el teclado

**Por qué**: hacerlo con el ratón es apuntar a la mitad superior del clip, que son diez píxeles.
Con el teclado es una tecla.

Para cada uno de los tres planos:

1. **`T`** — modo trim
2. Pon el cabezal sobre el plano y **`Shift+V`**
3. **`S`** hasta estar en `Slip`. **Cómo lo compruebas**: el icono del botón `Dynamic Trim Mode`
   de la barra de herramientas indica si estás en slip o en slide
4. **`,`** y **`.`** para deslizar un fotograma; **`Shift+,`** y **`Shift+.`** para cinco
5. **Mira el visor partido en cuatro** mientras deslizas: en un `Slip` se actualizan **los dos
   cuadros de arriba**. Si se te están moviendo los de abajo, estás haciendo un `Slide`
6. **`/`** para escuchar el resultado en su contexto

**Verifica**: los tres planos siguen empezando y acabando en el mismo fotograma de la timeline
—los cortes no se han movido— y la pieza dura exactamente lo mismo que al empezar la práctica.

> [!NOTE]
> Si el arrastre deja de avanzar, es que se acabó la cola de ese clip. El recuadro punteado que
> aparece al deslizar dibuja todo el material disponible: ahí se ve de un vistazo cuánto margen
> queda. No es un fallo de la aplicación.

---

## Paso 3: Un `Slide`, para colocar un recurso

**Por qué**: es la operación de los planos de apoyo. Un recurso que llega dos segundos tarde no se
arregla moviéndolo —eso deja hueco— sino deslizándolo.

Busca un recurso o un plano de apoyo que debería llegar antes o después de donde está:

1. **`T`**
2. Cabezal sobre el clip y **`Shift+V`**
3. **`S`** hasta estar en `Slide`
4. **`,`** y **`.`**
5. **Mira los dos cuadros de abajo del visor**: son la salida del vecino de la izquierda y la
   entrada del de la derecha. Los estás cambiando tú
6. **`/`**

**Verifica**: el recurso ha cambiado de sitio, enseña exactamente lo mismo que antes, sus dos
vecinos han cambiado de duración, y la pieza dura lo mismo.

---

## Paso 4: El editor de trim de precisión

**Por qué**: es la forma más visual de afinar un corte, y es la que mejor funciona cuando quieres
ver **cuántos fotogramas** estás moviendo en vez de intuirlo.

1. **Doble clic sobre un corte** de la timeline: el visor se convierte en el editor de precisión,
   con dos tiras de fotogramas —el plano que sale arriba, el que entra abajo—
2. Prueba las tres zonas arrastrables:
   - El **lado izquierdo de la tira de arriba** trima la salida del plano que sale
   - El **lado derecho de la tira de abajo** trima la entrada del plano que entra
   - El **tirador blanco de en medio** hace un `Roll`: mueve los dos a la vez
3. Fíjate en los **números sobre cada fotograma**: te dicen exactamente cuántos estás moviendo
4. Los dos botones a los lados de los controles de transporte del visor ajustan de fotograma en
   fotograma

**Verifica**: has afinado un corte y sabes decir cuántos fotogramas lo has movido.

> [!NOTE]
> El editor de precisión sustituye al visor de origen mientras lo usas, y vuelve solo al terminar.
> Si prefieres el editor antiguo, que no sustituye el visor, se cambia en
> `DaVinci Resolve > Preferences > User > Editing`, en la casilla
> `Automatically switch to single viewer mode when opening trim editor`.

---

## Paso 5: Tres cortes con `Dynamic Trim`

**Por qué**: es la técnica para los cortes que están mal y no sabes cuántos fotogramas sobran. Si
el problema se describe con adverbios —«se hace largo», «entra tarde»— hay que sentirlo en marcha.

Elige **tres** cortes de esa clase. Para cada uno:

1. Cabezal cerca del corte
2. **`T`** si vas a ripplear, **`A`** si vas a redimensionar
3. **`W`** — entras en modo dinámico. **Comprueba que el cabezal se ha puesto amarillo**
4. **`U`** para elegir la mitad del corte
5. Trima con `J`, `K` y `L`:
   - **`K`+`L`** mantenidas: cámara lenta hacia delante, con el sonido ralentizado. Es la que más
     vas a usar
   - **`K`** pulsada con toques de `J` o `L`: fotograma a fotograma
   - **`L`** sola: a velocidad real
6. **`Espacio`** — dentro del modo dinámico reproduce alrededor de lo que acabas de trimar
7. **Flecha abajo** para pasar al corte siguiente sin salir del modo

> [!WARNING]
> **Sal del modo dinámico con `W` al terminar.** Si te quedas dentro, `J`, `K` y `L` seguirán
> trimando cada vez que haya algo seleccionado en vez de reproducir, y la pieza se te irá
> descolocando sin que entiendas por qué. La señal es el cabezal amarillo.

**Verifica**: el cabezal ha vuelto a su color normal. Los tres cortes suenan mejor. Escribe una
línea por cada uno diciendo qué te hizo parar donde paraste.

---

## Paso 6: Comparar las dos técnicas

**Por qué**: la rúbrica pregunta por esto, y solo se puede contestar habiendo hecho las dos.

Contesta por escrito en `notas-de-montaje.md`:

> **¿Qué tres cortes afiné con `,` y `.`, y por qué esos?**
>
> **¿Qué tres afiné con `Dynamic Trim`, y por qué esos?**
>
> **¿En cuál de las dos formas tardé menos, y en cuál quedó mejor el corte?**

No hay respuesta correcta: hay una respuesta tuya, y es la que te va a decir cómo trabajar de aquí
a la Semana 36.

**Verifica**: las tres preguntas contestadas con cortes concretos, no con generalidades.

---

## Paso 7: Guardar y comprobar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 09
```

Sigue siendo ocho de diez, y es lo correcto: `Slip` y `Slide` no cambian nada que la API pueda
medir. Lo que sí tiene que seguir en verde es `montaje-v3-sin-huecos`: si ha caído, un `Slide` se
quedó a medias.

---

## ✅ Resultado

- [ ] Tres `Slip` hechos, con los cortes en el mismo sitio que antes
- [ ] Un `Slide` hecho, con los vecinos ajustados
- [ ] Sé qué mitad del visor partido en cuatro se mueve en cada operación
- [ ] He usado el editor de trim de precisión y sé cuántos fotogramas moví
- [ ] Tres cortes afinados con `Dynamic Trim`, y salí del modo con `W`
- [ ] La pieza dura lo mismo que al empezar la práctica
- [ ] Las tres preguntas del paso 6 contestadas

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El clip se mueve en vez de deslizarse | Estás en `Selection Mode` | `T` |
| Hago `Slip` y se mueven los cortes | Estás haciendo `Slide` | `S` alterna; mira el icono del botón |
| El arrastre no avanza | Se acabó la cola | Mira el recuadro punteado del material disponible |
| El visor no se parte en cuatro | Está apagado el preview multivista | `View > Enable Multiview Edit Preview` |
| Ha aparecido un hueco después de un `Slide` | El vecino no tenía cola suficiente | `Ctrl+Z` y desliza menos |
| El doble clic abre el clip en el visor, no el editor de precisión | Hiciste doble clic sobre el clip, no sobre el corte | El corte es la línea entre dos clips |
| `J`, `K` y `L` no reproducen | Sigues en modo dinámico | `W`; el cabezal amarillo es la señal |
| La barra espaciadora no reproduce hacia delante | Estás en modo dinámico: ahí hace otra cosa | Es su comportamiento; `W` para salir |
| El modo dinámico trima cortes que no quería | Entraste con varias cosas seleccionadas | `Ctrl+Shift+A` / `Cmd+Shift+A` y entra limpio |
| No noto ninguna diferencia al trimar dinámicamente | Estás trimando sin sonido | Auriculares |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · Ripple y roll sobre tu montaje](02-ripple-y-roll-sobre-tu-montaje.md) | **03 · Slip, slide y el dynamic trim** | [04 · Split edits y cierre](04-split-edits-y-cierre.md) |

← [Volver a la Semana 09](../README.md)
