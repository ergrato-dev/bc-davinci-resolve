# Estabilización en la Edit page

> Estabilizar es pedirle a Resolve que reencuadre el plano fotograma a fotograma para cancelar el
> temblor de la cámara. Funciona muy bien y tiene un precio que se paga siempre, en píxeles. Este
> archivo va sobre los seis controles que deciden cuánto pagas.

## 🎯 Objetivos

- Explicar qué hace exactamente el estabilizador y de dónde salen los bordes negros
- Elegir entre `Perspective`, `Similarity` y `Translation` según el plano
- Saber qué controles obligan a reanalizar y cuáles no
- Usar `Cropping Ratio`, `Smooth` y `Strength` con criterio, no a ciegas
- Distinguir «cámara quieta» de «cámara suave», que son dos objetivos distintos
- Saber qué es `Lens Correction`, por qué es de Studio y qué hacer en Free

---

## 1. Qué problema resuelve

Tienes un plano bueno grabado a pulso y se mueve. No un movimiento de cámara: un temblor. En una
pieza montada, ese plano destaca entre los demás y saca al espectador.

El estabilizador **analiza** el plano, deduce cómo se movía la cámara y **contrarresta ese
movimiento** desplazando, girando y ampliando cada fotograma lo justo para cancelarlo.

Lo bueno: es una casilla y un botón, y el análisis está a la altura de programas dedicados.

Lo que hay que saber antes: **para cancelar el movimiento hay que mover la imagen, y al moverla se
sale del cuadro por un lado y entra vacío por el otro**. Ese vacío se llama *blanking*, y la única
forma de taparlo es ampliar. Estabilizar cuesta resolución. Siempre.

---

## 2. Cómo funciona

![El estabilizador desplaza cada fotograma para cancelar el temblor y eso deja huecos vacíos en los bordes; la casilla Zoom amplía la imagen lo justo para que esos huecos queden fuera de cuadro, y el Cropping Ratio decide cuánta ampliación se está dispuesto a aceptar](../0-assets/09-estabilizacion.svg)

### 2.1 Dónde vive y qué relación tiene con la Color page

Está en **`Inspector > Video > Stabilization`**, con el clip seleccionado en la timeline.

Son **los mismos controles** que la paleta `Tracker` de la Color page, menos el gráfico. Y el
análisis es el mismo dato: si estabilizas aquí, el colorista de la Semana 19 verá esa curva
dibujada en su gráfico. No son dos estabilizaciones distintas; es una, accesible desde dos sitios.

### 2.2 Los tres modos de análisis

El desplegable de arriba decide **qué tipo de movimiento** busca el análisis:

| Modo | Qué analiza y corrige | Cuándo |
| ---- | --------------------- | ------ |
| **`Perspective`** | Perspectiva, paneo, inclinación, zoom y rotación | El más completo. El punto de partida |
| **`Similarity`** | Paneo, inclinación, zoom y rotación. Sin perspectiva | Cuando `Perspective` produce artefactos raros de deformación |
| **`Translation`** | Solo paneo e inclinación: `X` e `Y` | Cuando los otros dos se pasan y solo hace falta quitar el vaivén |

La escalera va de más a menos: se empieza por `Perspective` y se baja si el resultado tiene
ondulaciones.

> [!IMPORTANT]
> **El modo se elige antes de pulsar `Stabilize`**, porque cambia cómo se hace el análisis. Si
> cambias de modo después, hay que **volver a pulsar `Stabilize`**. Lo mismo pasa con
> `Cropping Ratio` y con `Smooth`: el manual dice explícitamente que esos tres exigen reanalizar.
> `Camera Lock` no aparece en esa lista, pero como apaga dos de ellos, lo prudente es volver a
> pulsar `Stabilize` también al activarlo.

### 2.3 Los seis controles

| Control | Qué hace | ¿Reanaliza? |
| ------- | -------- | ----------- |
| **Interruptor de `Stabilization`** | Enciende y apaga la estabilización, para comparar antes y después | No |
| **`Camera Lock`** | Desactiva `Cropping Ratio` y `Smooth` y busca eliminar **todo** el movimiento: plano clavado | Conviene |
| **`Zoom`** | Amplía lo justo para que no se vea el blanking. Activada de fábrica | No |
| **`Cropping Ratio`** | Cuánto se esfuerza el estabilizador. **1,0 es no estabilizar nada**; valores más bajos, más agresivo | **Sí** |
| **`Smooth`** | Suaviza el movimiento en vez de eliminarlo. Valores bajos conservan el carácter; altos alisan más | **Sí** |
| **`Strength`** | Multiplicador del resultado. `1` estabilización máxima; `0` desactivada; entre medias, deja pasar parte del movimiento original | No |

`Strength` es el único que se puede tocar libremente después del análisis, y por eso es el mejor
para afinar: analiza una vez, y luego busca el número entre `0` y `1` en el que el plano se ve
estable pero vivo.

### 2.4 Cámara quieta frente a cámara suave

Son dos objetivos distintos y se piden con controles distintos:

| Quiero | Control | Resultado |
| ------ | ------- | --------- |
| **Que la cámara esté clavada**, como sobre un trípode | `Camera Lock` activado | Movimiento cero. Requiere mucha ampliación |
| **Que el movimiento se mantenga pero sin temblor** | `Camera Lock` desactivado y `Smooth` al gusto | La panorámica sigue siendo una panorámica, pero limpia |

El error clásico es pedir `Camera Lock` en un plano con panorámica: el estabilizador intenta
cancelar la panorámica entera, se queda sin margen y el resultado ondula. En un plano con
movimiento intencionado, la respuesta casi siempre es `Smooth`.

### 2.5 El `Zoom` y por qué a veces conviene apagarlo

Con `Zoom` activado, Resolve amplía lo suficiente para que el blanking quede fuera de cuadro. Es
lo que quieres el 95 % de las veces.

Se apaga en dos casos:

1. Cuando el blanking se va a tapar de otra forma —un compositor que rellene esos bordes, cosa de
   la Fase 6—
2. Cuando prefieres **animar tú mismo** la ampliación con keyframes, para ampliar solo en los
   tramos donde de verdad asoma el borde, y no durante todo el plano

El segundo caso es un buen ejercicio de la [teoría 08](08-keyframes-inspector-y-curve-editor.md) y
es como se estabiliza sin sacrificar resolución de más.

### 2.6 Cuándo NO estabilizar

Hay planos que el estabilizador empeora, y reconocerlos ahorra el tiempo del análisis:

| Plano | Por qué falla |
| ----- | ------------- |
| Con **obturador rodante** (*rolling shutter*) marcado: verticales que se ondulan al mover | El estabilizador quita el temblor y deja las ondulaciones, que ahora se ven más |
| Con **poco detalle**: cielo, pared lisa, niebla | No hay puntos que seguir; el análisis no encuentra nada |
| Con **movimiento borroso** fuerte por obturador lento | Los puntos a seguir están difuminados |
| Con algo grande que **cruza el cuadro** de lado a lado | El análisis persigue el objeto en vez de la cámara |
| Ya **ampliado al máximo** de su resolución | No queda margen para el `Zoom` |
| Con el temblor **intencionado** | Es lenguaje, no un fallo |

### 2.7 `Lens Correction`, que es de Studio

Justo debajo, en el Inspector, hay un grupo `Lens Correction` con dos controles: `Analyze`, que
detecta automáticamente la deformación de un gran angular y coloca el deslizador, y `Distortion`,
que la corrige a mano.

> [!IMPORTANT]
> **Studio** · El grupo `Lens Correction` del Inspector **solo existe en DaVinci Resolve Studio**.
> Lo dice el manual en la propia descripción del grupo.
>
> **En Free**, si un plano de gran angular —una cámara de acción, un móvil en modo panorámico—
> tiene las verticales curvadas, las salidas son: rodar con menos angular; recortar y ampliar el
> centro del cuadro, que es donde menos deforma; o dejarlo, que en un plano de recurso corto casi
> nunca se nota. **Ningún entregable evaluable de esta semana depende de este grupo.**
>
> *Verificado en el DaVinci Resolve 21 Reference Manual, capítulo 57, sección «Lens Correction».*

---

## 3. Cómo se hace en Resolve 21

### 3.1 Estabilizar un plano, de principio a fin

1. Selecciona el clip en la timeline
2. `Inspector > Video`, grupo **`Stabilization`**
3. Elige el **modo**: empieza por `Perspective`
4. Pulsa **`Stabilize`**. El análisis tarda según la duración del plano
5. Reproduce y juzga
6. Apaga y enciende el **interruptor del grupo** para comparar con el original

### 3.2 Afinar sin reanalizar

Baja **`Strength`** de `1` hacia abajo hasta que el plano se vea estable pero no muerto.

Entre `0,6` y `0,9` está el rango donde la mayoría de los planos a pulso quedan bien: quitan el
temblor y conservan el pulso humano que hace que el plano no parezca un render.

### 3.3 Afinar reanalizando

Si `Strength` no basta:

1. Cambia `Cropping Ratio` o `Smooth`
2. Pulsa **`Stabilize` otra vez**. Sin esto, el cambio no se aplica al análisis

`Cropping Ratio` más bajo = más agresivo = más ampliación. Es el mando de «cuánta resolución estoy
dispuesto a pagar».

### 3.4 Un plano con panorámica

1. `Camera Lock` **desactivado**
2. Sube `Smooth`
3. `Stabilize`
4. Si la panorámica se ha vuelto artificial, baja `Smooth` y reanaliza

### 3.5 Comprobar cuánto has ampliado

1. Apaga el interruptor de `Stabilization`
2. Fíjate en un elemento del borde del cuadro
3. Enciéndelo otra vez: lo que ya no se ve es lo que has pagado

Si el recorte se come algo que importaba, hay que estabilizar menos: `Strength` más bajo, o
`Cropping Ratio` más alto y reanalizar.

### 3.6 El orden con el resto de la semana

Un orden que evita rehacer trabajo:

1. **Velocidad** primero: la cámara lenta amplifica el temblor, así que estabilizar antes de
   retimar es estabilizar el plano equivocado
2. **Estabilización** después: es la que decide cuánta ampliación va a tener el plano
3. **Reencuadre y keyframes** al final: sobre la imagen que de verdad va a quedar

---

## 4. Antipatrones

| Antipatrón | Por qué duele | Qué hacer |
| ---------- | ------------- | --------- |
| Cambiar el modo y no volver a pulsar `Stabilize` | Sigues viendo el análisis viejo y no entiendes nada | El modo, `Cropping Ratio` y `Smooth` obligan a reanalizar |
| `Camera Lock` en un plano con panorámica | El estabilizador pelea contra un movimiento intencionado | `Smooth` en vez de `Camera Lock` |
| Estabilizar todo lo que se mueva | La pieza queda plana y sin pulso | Solo lo que distrae al verlo |
| Dejar `Strength` en 1 siempre | Muchos planos quedan mejor con algo de movimiento | Prueba entre 0,6 y 0,9 |
| Estabilizar un plano ya ampliado al máximo | No queda margen para el `Zoom` | Ese plano no se estabiliza |
| Estabilizar antes de retimar | La cámara lenta cambia el temblor que hay que cancelar | Velocidad, estabilización, reencuadre |
| No comprobar cuánto se ha recortado | Descubres en la entrega que falta un brazo | Apaga y enciende el interruptor |
| Buscar `Lens Correction` en Free | No está: es de Studio | Recorta el centro o déjalo |
| Estabilizar un plano con rolling shutter | Las verticales onduladas se ven más al quitar el temblor | Ese plano se corta, no se estabiliza |

---

## 5. Trucos

| Truco | Cómo |
| ----- | ---- |
| Comparar con y sin estabilizar | El interruptor del grupo `Stabilization` |
| Afinar sin esperar otro análisis | `Strength`, que no reanaliza |
| Saber qué controles exigen reanalizar | Modo, `Cropping Ratio` y `Smooth` |
| Conservar una panorámica y quitarle el temblor | `Camera Lock` apagado y `Smooth` |
| Clavar un plano como sobre trípode | `Camera Lock` |
| Ampliar solo donde asoma el borde | `Zoom` apagado y keyframes de `Zoom` en `Transform` |
| Ver la estabilización dibujada en un gráfico | La paleta `Tracker` de la Color page |
| Copiar la misma estabilización a otro plano | `Edit > Paste Attributes` — `Alt+V` (Win) / `Opt+V` (Mac) |
| Medir lo que has recortado | Apaga y enciende el interruptor mirando un borde |

---

## 📚 Recursos Adicionales

- [DaVinci Resolve Reference Manual](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion) — capítulo 57, secciones «Stabilization» y «Lens Correction», con la descripción de los seis controles.
- [Comparativa oficial Free / Studio](https://www.blackmagicdesign.com/products/davinciresolve/studio) — la fuente de verdad sobre `Lens Correction`.
- [Semana 01 · Obturador y desenfoque de movimiento](../../week-01-fundamentos_de_imagen_en_movimiento/1-teoria/03-obturador-y-desenfoque-de-movimiento.md) — por qué un plano borroso no se deja estabilizar.
- [07 · Transform, crop y dynamic zoom](07-transform-crop-y-dynamic-zoom.md) — el margen de ampliación que la estabilización se come.

---

## ✅ Checklist de Verificación

- [ ] Sé de dónde salen los bordes negros y por qué estabilizar cuesta resolución
- [ ] Sé elegir entre `Perspective`, `Similarity` y `Translation`
- [ ] Sé qué tres controles obligan a volver a pulsar `Stabilize`
- [ ] Sé qué hace `Strength` y por qué es el mejor para afinar
- [ ] Sé pedir «cámara quieta» y «cámara suave» por separado
- [ ] Sé reconocer un plano que no se debe estabilizar
- [ ] Sé que `Lens Correction` es de Studio y qué hacer en Free
- [ ] Sé el orden: velocidad, estabilización, reencuadre

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [08 · Keyframes: Inspector, Keyframe Editor y Curve Editor](08-keyframes-inspector-y-curve-editor.md) | **09 · Estabilización en la Edit page** | — |

← [Volver a la Semana 10](../README.md)
