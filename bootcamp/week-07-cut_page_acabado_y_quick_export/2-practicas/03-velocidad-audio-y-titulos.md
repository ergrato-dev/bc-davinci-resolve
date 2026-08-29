# Práctica 03 — Velocidad, audio y títulos

> Al terminar, tu pieza tendrá el ritmo ajustado donde hacía falta, un sonido que se puede
> escuchar de principio a fin, y tres pistas de vídeo: continuidad, recursos y títulos.

**Duración estimada**: 60 min
**Prerrequisitos**: [Práctica 02](02-transiciones-donde-hacen-falta.md), [Teoría 05](../1-teoria/05-cambios-de-velocidad.md), [Teoría 06](../1-teoria/06-audio-basico-en-la-cut-page.md), [Teoría 07](../1-teoria/07-titulos-rapidos.md)

## Contexto

Tres bloques, en un orden que no es negociable:

1. **Velocidad**, que cambia la duración de la pieza.
2. **Audio**, que no la cambia.
3. **Títulos**, que quedan clavados a un instante.

Hacerlo al revés significa recolocar rótulos a mano, que es el peor rato de la semana. Y por
lo mismo, esta práctica tiene un paso —el 3— dedicado a repasar los recursos de `Video 2`
después de haber tocado duraciones.

---

## Paso 0: Situarse

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check montaje-v2-activo
```

Ten a mano las dos listas que quedan del paso 10 de la práctica 01: **planos que sobran de
duración** y **rótulos que hacen falta**.

---

## Paso 1: Acortar un plano largo acelerándolo

**Por qué**: es la alternativa a cortarlo. Conservas el recorrido entero del plano y le
quitas el tiempo sobrante.

Coge de tu lista un plano marcado en **gris** por el Boring Detector, que funcione pero dure
de más:

1. Selecciónalo en la timeline
2. Pulsa **`Tools`** en la barra del visor
3. Elige la categoría **`Speed`**
4. En **`Duration`**, escribe **la duración que quieres que tenga**. El porcentaje se calcula
   solo
5. Reproduce

**Verifica**: el clip ocupa menos en la timeline, el recorrido se ve entero, y el Boring
Detector ha dejado de marcarlo en gris.

> [!TIP]
> Escribir la duración es más rápido que buscar el porcentaje a ojo, y es cómo se piensa de
> verdad: no quieres «un 140 %», quieres «que dure cuatro segundos».

---

## Paso 2: Ralentizar un gesto para que se lea

**Por qué**: para tener el otro caso hecho con tus manos y ver dónde está el límite de tu
material.

Busca un momento que pase demasiado rápido —una mirada, un impacto, una mano que coge algo—:

1. Selecciona el clip
2. `Tools > Speed`
3. Pon **`Speed`** en **80** y reproduce
4. Pon **50** y reproduce
5. Pon **40** y reproduce

**Verifica**: sabes a partir de qué porcentaje tu material se ve a tirones. Anótalo en
`notas-de-montaje.md`: es un dato de tu cámara que te sirve las 29 semanas que quedan.

Quédate con el valor que se vea bien, o **descarta el efecto** con el botón de reinicio de la
categoría. Las dos respuestas son válidas; lo que no vale es no haberlo mirado.

> [!NOTE]
> Con material grabado a 24 fps, por debajo del 40 % se ve mal casi siempre: Resolve no tiene
> fotogramas suficientes y tiene que repetirlos o inventarlos. La cámara lenta buena se graba
> a alta cadencia, no se hace después.

---

## Paso 3: Repasar los recursos de `Video 2`

**Por qué**: acabas de cambiar duraciones en `Video 1`, y `Video 1` hace ripple. Todo lo que
estaba a la derecha de los clips que tocaste se ha movido; los recursos de encima, no.

1. Reproduce cada tramo que tenga un recurso en `Video 2`, **desde el primer clip que tocaste
   hasta el final**
2. Comprueba que cada recurso sigue tapando lo que tapaba: que **empieza antes** del salto y
   **acaba después**
3. Arrastra los que se hayan quedado descolocados

**Verifica**: desactiva `Video 2` desde su cabecera, reproduce un tramo, vuelve a activarla.
Cada recurso entra y sale donde tiene que hacerlo.

> [!IMPORTANT]
> A partir de aquí **no vuelvas a cambiar duraciones en `Video 1`** esta semana. Si descubres
> que hace falta, hazlo **ahora**, antes del paso 5. Un cambio de duración con los rótulos ya
> puestos los descoloca todos.

---

## Paso 4: Nivelar los clips que se salen

**Por qué**: una pieza en la que hay que subir y bajar el volumen del ordenador no se puede
juzgar, y a partir de la semana que viene la vas a juzgar mucho.

Con auriculares —siempre los mismos— reproduce la pieza entera y anota los clips que suenen
claramente más alto o más bajo que el resto. Para cada uno:

1. Selecciónalo
2. **`Tools > Audio`**
3. Mueve el deslizador de volumen hasta que se iguale con lo de alrededor

Referencias: el diálogo, con picos entre **-12 y -6 dBFS**; nada tocando **0 dBFS**.

**Verifica**: puedes reproducir la pieza entera sin tocar el volumen del sistema ni una vez.

> [!WARNING]
> Si un clip llegó **recortado** de la grabación —distorsión áspera en los picos—, bajarlo no
> lo arregla: lo deja bajo y distorsionado. La información no está en el archivo. Anótalo en
> `notas-de-montaje.md` como material que habría que volver a grabar.

---

## Paso 5: Bajar el audio de los recursos

**Por qué**: es el arreglo de sonido más rentable de la semana y cuesta dos minutos. Cada
plano de recurso de `Video 2` trae su propio audio, que se suma al de debajo y ensucia la voz.

Para cada recurso de `Video 2`:

1. Selecciónalo
2. `Tools > Audio`
3. Bájalo hasta que no interfiera. En la mayoría de los casos, hasta el silencio

La excepción: recursos cuyo sonido aporte —una máquina, el mar, una calle—. Ahí, «un poco»
significa que sigues entendiendo cada palabra sin esfuerzo.

**Verifica**: reproduce un tramo con recurso. Se entiende cada palabra de la voz de debajo
sin esforzarte.

---

## Paso 6: Crear la pista de títulos

**Por qué**: los títulos van en su propia pista para que no se pisen con los recursos, para
encontrarlos en la Semana 11, y para poder apagarlos todos de un clic.

1. Abre el navegador de títulos de la Cut page y elige la categoría **`Titles`**
2. Localiza **`Text`**
3. **Arrástralo a la zona gris vacía** que hay encima de `Video 2`

Resolve crea `Video 3` sola al soltarlo. Si prefieres crear la pista antes, está en
`Timeline Actions > Add Video Track`.

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check montaje-v2-pista-de-titulos
```

---

## Paso 7: El primer rótulo de nombre

**Por qué**: es el rótulo que más falta hace y el que enseña el ciclo completo.

1. Coloca el clip de título **un segundo después** de que la persona empiece a hablar
2. **Doble clic sobre el texto en el visor** y escribe el nombre
3. Arrástralo a su sitio en el encuadre. Se pega solo al centro y a los tercios; con `Shift`
   se mueve en un solo eje
4. Ajusta la **duración**: el tiempo de leerlo dos veces sin prisa, entre **3 y 4 segundos**
5. Doble clic sobre el título para abrir el **Video Inspector** y ajusta solo dos cosas:
   **que contraste** con lo que hay detrás y **que el tamaño se lea**

**Verifica**: se lee sin esfuerzo, no tapa la cara de quien habla, y no dura los 5 segundos
por defecto.

> [!NOTE]
> Nada de tipografías, animaciones ni jerarquías esta semana: eso es la **Semana 11** y se
> rehace entero. Aquí basta con que la información esté y se lea.

---

## Paso 8: El resto de los rótulos

**Por qué**: la lista de la práctica 01 tiene cuatro tipos y cada uno resuelve una pregunta
distinta del espectador.

| Rótulo | Qué lleva | Duración |
| ------ | --------- | -------- |
| **Nombre** | Nombre y, si aporta, en qué calidad habla | 3-4 s |
| **Sitio o fecha** | Lo mínimo para situar | 2-3 s |
| **Título de la pieza** | El título, y nada más | Lo que pida la apertura |
| **Cierre** | Autoría, fecha y **atribución del material con licencia** | 5 s o más |

Truco: copia el clip del rótulo que ya tienes formateado y cambia solo el texto. Así todos
los rótulos de la pieza salen iguales sin configurar nada dos veces.

> [!IMPORTANT]
> El rótulo de cierre **no es decorativo**. Si tu pieza usa material del pack de medios con
> licencia Creative Commons, la atribución va ahí, y es la condición de la licencia. Mira
> [`docs/pack-de-medios.md`](../../../docs/pack-de-medios.md) para saber qué pide cada fuente.

**Verifica**: cuatro rótulos como mínimo, todos en `Video 3`, ninguno con la duración por
defecto sin decidir.

---

## Paso 9: La comprobación de las tres pistas

**Por qué**: es la propiedad que hace útil el reparto, y conviene verla una vez con tus
propios ojos.

1. Desactiva **`Video 3`** desde su cabecera y reproduce: la pieza sin rótulos
2. Desactiva también **`Video 2`**: la continuidad desnuda
3. Vuelve a activar las dos

**Verifica**: con las dos desactivadas ves exactamente el montaje de `Video 1`, con el mismo
audio de base y la misma duración. Si al desactivar `Video 3` desaparece algo que no es un
rótulo, es que has puesto algo en la pista equivocada.

---

## Paso 10: Guardar y anotar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)
2. Actualiza `notas-de-montaje.md` con: los clips a los que cambiaste la velocidad y a qué
   porcentaje, a partir de qué porcentaje tu material se ve a tirones, los clips que llegaron
   recortados, y cuántos rótulos tiene la pieza

**Verifica**:

```bash
python scripts/verificar-semana.py 07
```

Ocho de nueve en verde. El que falta es `bin-entregas`, que es la práctica 04.

---

## ✅ Resultado

- [ ] Al menos un plano acortado con un cambio de velocidad
- [ ] Al menos un plano ralentizado, y sé dónde está el límite de mi material
- [ ] Los recursos de `Video 2` repasados después de tocar duraciones
- [ ] Ningún cambio de duración en `Video 1` después del paso 5
- [ ] La pieza se reproduce entera sin tocar el volumen del sistema
- [ ] El audio de los recursos bajado o silenciado
- [ ] `Video 3` existe y contiene solo títulos
- [ ] Cuatro rótulos como mínimo, con duración decidida
- [ ] El rótulo de cierre lleva la atribución del material con licencia
- [ ] Desactivar `Video 2` y `Video 3` devuelve el montaje de `Video 1` intacto

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Al cambiar la velocidad se descolocó medio montaje | `Video 1` hace ripple, y es lo esperado | Paso 3: repasa los recursos desde ese punto |
| El plano ralentizado va a tirones | Menos del 40 % con material a 24 fps | Sube el porcentaje o descarta el efecto |
| Un clip acelerado suena a comedia | Su audio sigue sonando | `Tools > Audio` y bájalo o silencia |
| No encuentro los controles de velocidad | Están en el botón `Tools` del visor, no en la timeline | `Tools > Speed` |
| Subo un clip y suena distorsionado | Llegó recortado de la grabación | No tiene arreglo: anótalo como material a regrabar |
| El rótulo desaparece al reproducir | Está debajo de un recurso de `Video 2` | Muévelo a `Video 3` |
| `montaje-v2-pista-de-titulos` falla | Solo hay dos pistas de vídeo | Paso 6: arrastra el título a la zona gris de encima |
| El rótulo no se lee sobre la imagen | Falta contraste | Sombra o fondo en el Video Inspector, o cámbialo de plano |
| Los rótulos se descolocaron de golpe | Cambiaste una duración en `Video 1` después del paso 5 | Recolócalos, y cierra la estructura antes la próxima vez |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · Transiciones donde hacen falta](02-transiciones-donde-hacen-falta.md) | **03 · Velocidad, audio y títulos** | [04 · Quick Export y cierre de la Fase 2](04-quick-export-y-cierre-de-fase.md) |

← [Volver a la Semana 07](../README.md)
