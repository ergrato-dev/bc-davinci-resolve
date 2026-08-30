# Práctica 04 — Transformaciones, keyframes y estabilización

> Al terminar habrás estabilizado los planos que se movían, reencuadrado los que estaban mal
> compuestos, animado un reencuadre que sigue a alguien y montado un `Dynamic Zoom` que no parece
> un efecto. Y habrás cerrado la semana con la comparación escrita y el respaldo.

**Duración estimada**: 50 min
**Prerrequisitos**: [Práctica 03](03-velocidad-variable-y-calidad-de-imagen.md), [Teoría 07](../1-teoria/07-transform-crop-y-dynamic-zoom.md), [Teoría 08](../1-teoria/08-keyframes-inspector-y-curve-editor.md), [Teoría 09](../1-teoria/09-estabilizacion-en-la-edit-page.md)

## Contexto

El orden de esta práctica es el de la teoría 09 y no se cambia:

1. **Estabilización** primero, porque decide cuánta ampliación se come el plano
2. **Reencuadre** después, sobre la imagen que de verdad va a quedar

Y la velocidad ya está hecha, de las prácticas 02 y 03, que es el paso que va antes de los dos.

---

## Paso 1: Calcular el margen de ampliación de tu material

**Por qué**: estabilizar y reencuadrar gastan lo mismo —resolución— y si no sabes cuánta tienes,
lo gastas dos veces y te pasas.

1. `Media Pool` en vista de lista, columna **`Resolution`**
2. `File > Project Settings > Master Settings > Timeline resolution` para la del proyecto
3. Divide: `resolución del clip ÷ resolución del proyecto`

```markdown
### Margen de ampliación
- Resolución del proyecto: ____ x ____
- Clips a 3840x2160: __ · margen 2,0
- Clips a 1920x1080: __ · margen 1,0 (ampliar ya cuesta nitidez)
```

**Verifica**: sabes qué planos admiten estabilización cómoda y cuáles no.

> [!IMPORTANT]
> Un plano cuya resolución **es la misma** que la del proyecto no tiene margen. Se puede estabilizar
> igual, pero cada punto de ampliación es nitidez que se va. En esos planos, `Strength` bajo y
> `Cropping Ratio` alto.

---

## Paso 2: Estabilizar el primer plano

**Por qué**: el procedimiento completo se hace una vez con calma y luego se repite en un minuto.

Ve al primer marcador **cian** de la práctica 01:

1. Selecciona el clip
2. `Inspector > Video`, grupo **`Stabilization`**
3. Modo: **`Perspective`**
4. Pulsa **`Stabilize`** y espera al análisis
5. Reproduce
6. Apaga y enciende el **interruptor del grupo** para comparar con el original

**Verifica**: el plano se mueve menos que antes, y sabes cuánto se ha ampliado porque lo has visto
al apagar y encender.

Si el resultado tiene ondulaciones raras:

| Lo que ves | Prueba |
| ---------- | ------ |
| La imagen se deforma y ondula | Modo `Similarity` y **`Stabilize` otra vez** |
| Sigue ondulando | Modo `Translation` y **`Stabilize` otra vez** |
| Estable pero muerto, artificial | Baja `Strength` — este **no** exige reanalizar |

---

## Paso 3: Afinar con `Strength`

**Por qué**: es el único control que se puede tocar sin volver a analizar, y es donde está la
diferencia entre un plano estabilizado y un plano que parece un render.

1. Con la reproducción en bucle —**`Ctrl+/`** / **`Cmd+/`** y **`/`**—, baja `Strength` de `1`
   hacia abajo
2. Busca el punto en el que el temblor molesto desaparece pero queda algo de pulso
3. Entre **0,6 y 0,9** está el rango de la mayoría de los planos a pulso

**Verifica**: anota el valor que has dejado. Vas a necesitar el número en el paso 9.

---

## Paso 4: Estabilizar el resto, con el caso de la panorámica

**Por qué**: un plano con movimiento intencionado necesita otro planteamiento, y conviene tener uno
en la pieza para haberlo hecho.

Para los demás marcadores cianes, repite el paso 2. Y si alguno tiene una **panorámica o un
travelling intencionado**:

1. `Camera Lock` **desactivado** — si lo activas, el estabilizador pelea contra el movimiento que
   querías
2. Sube **`Smooth`**
3. **`Stabilize`**
4. Si la panorámica se ha vuelto artificial, baja `Smooth` y **reanaliza**

**Verifica**: los planos con movimiento siguen teniendo movimiento; lo que ha desaparecido es el
temblor.

> [!NOTE]
> Si un plano no se deja estabilizar —cielo, pared lisa, niebla, obturador rodante marcado— no
> insistas: apaga el grupo, cambia el marcador cian a azul con la nota «no estabilizable» y sigue.
> Reconocer eso es parte del entregable, no un fallo.

---

## Paso 5: Reencuadrar los planos mal compuestos

**Por qué**: es la operación más común de la Edit page, y ahora se hace sobre la imagen definitiva,
con la ampliación de la estabilización ya aplicada.

Para cada plano con demasiado aire, un sujeto descentrado o algo que entra por una esquina:

1. Selecciona el clip
2. `Inspector > Video > Transform`
3. Sube `Zoom` lo justo, dentro del margen del paso 1
4. Ajusta `Position X` / `Position Y`
5. **Visor al 100 %** — `Alt+Shift+Z` (Win) / `Opt+Shift+Z` (Mac), o el desplegable de escala
   del visor—: comprueba que la imagen no se ha ablandado

Si quieres ampliar **hacia** un punto concreto:

6. Mueve `Anchor Point X` / `Y` a ese punto **antes** de subir el `Zoom`

**Verifica**: ningún plano reencuadrado se ve más blando que el de al lado.

---

## Paso 6: Un reencuadre animado que sigue a alguien

**Por qué**: es la alternativa en Free al `Smart Reframe` de Studio, y es el ejercicio de keyframes
de la semana.

Elige un plano donde el sujeto se desplace por el cuadro:

1. Sube el `Zoom` hasta que el encuadre que quieres seguir llene el cuadro
2. Cabezal al **principio** del plano. Coloca `Position X` / `Y` y pulsa **su rombo**
3. Cabezal donde el sujeto ya se haya movido. **Recoloca** `Position`: el keyframe se pone solo
4. Repite en **tres o cuatro** puntos, no en veinte
5. Reproduce con **`/`**
6. Si el movimiento arranca o para de golpe: pestaña `Keyframes` `>` icono de curvas `>` marca
   `Position` y alarga las asas de los puntos extremos

**Verifica**: el sujeto se mantiene en el cuadro y el movimiento no tiembla.

> [!TIP]
> Menos keyframes es más suave. Uno cada dos segundos es un movimiento de cámara; uno cada cinco
> fotogramas es un temblor que has añadido tú.

---

## Paso 7: Un `Dynamic Zoom`

**Por qué**: es el movimiento sobre un plano fijo, en tres clics, y hay que saber ponerle el easing
correcto para que no se note.

Elige un plano estático que gane con un movimiento lento:

1. Selecciona el clip
2. Botón **`Transform/Crop/Dynamic Zoom`**, abajo a la izquierda del visor `>` modo
   **`Dynamic Zoom`**
3. Coloca el **recuadro verde**: el encuadre de inicio
4. Coloca el **recuadro rojo**: el de final
5. `Inspector > Video > Dynamic Zoom > Dynamic Zoom Ease` `>` **`Ease In and Out`**
6. Reproduce. Si va al revés de lo que querías: botón **`Swap`**
7. **Apaga el botón del visor**

**Verifica**: el movimiento arranca y para suavemente, y el botón del visor está apagado.

---

## Paso 8: La comparación con `BC-Montaje-v3`

**Por qué**: es como se aprende a ver la diferencia, y es el entregable escrito de la semana.

1. Abre **`BC-Montaje-v3`** y reprodúcela entera
2. Vuelve a **`BC-Montaje-v4`** y haz lo mismo
3. Contesta en tus notas, con cifras y con planos concretos:
   - ¿Cuánto dura cada una?
   - ¿Qué tres cambios se notan más?
   - ¿Hay algún sitio donde la v3 fuera mejor?

**Verifica**: la respuesta tiene números y nombres de plano, no adjetivos.

> [!WARNING]
> **Vuelve a dejar `BC-Montaje-v4` como timeline abierta antes de verificar.** Seis de los diez
> checks leen la timeline activa, y si te quedas en la v3 fallan los seis de golpe aunque el
> trabajo esté perfecto.

---

## Paso 9: Cerrar la semana

1. Cierra el apartado de `notas-de-montaje.md`:

```markdown
### Transformaciones y estabilización — práctica 04
- Planos estabilizados: __ · modo usado en cada uno: __
- Valores de Strength: __
- Planos que no se dejaron estabilizar, y por qué: __
- Planos reencuadrados: __
- Reencuadre animado: plano __ , con __ keyframes
- Dynamic Zoom: plano __ , easing __
- Comparación v3 / v4: duración __ vs __ · lo que más se nota: __
- Qué pasa a la Semana 11: __
```

2. Pasa a **azul** los marcadores morados y cianes que hayas resuelto, o bórralos. Los que dejes en
   morado o cian son trabajo pendiente
3. `Ctrl+S` / `Cmd+S`
4. `File > Export Project` → `04-respaldos/BC-Bootcamp-Resolve-semana10.drp`

**Verifica**:

```bash
python scripts/verificar-semana.py 10
```

Diez de diez, con `BC-Montaje-v4` abierta.

---

## ✅ Resultado

- [ ] El margen de ampliación de tu material calculado y anotado
- [ ] Todos los marcadores cianes atendidos: estabilizados, o descartados con su razón
- [ ] Al menos un plano afinado con `Strength` en vez de con otro análisis
- [ ] Un plano con movimiento intencionado tratado con `Smooth`, no con `Camera Lock`
- [ ] Los planos mal compuestos reencuadrados, comprobados al 100 %
- [ ] Un reencuadre animado con tres o cuatro keyframes
- [ ] Un `Dynamic Zoom` con `Ease In and Out`
- [ ] La comparación v3 / v4 contestada con cifras
- [ ] `BC-Montaje-v4` como timeline abierta
- [ ] Respaldo `BC-Bootcamp-Resolve-semana10.drp` exportado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Cambio el modo y no cambia nada | El análisis viejo sigue puesto | Vuelve a pulsar `Stabilize` |
| El plano estabilizado ondula | `Perspective` se pasa con ese material | `Similarity`, y si no, `Translation` |
| El plano parece un render, sin vida | `Strength` al máximo | Bájalo entre 0,6 y 0,9 |
| La panorámica ha desaparecido | `Camera Lock` activado | Apágalo y usa `Smooth` |
| El estabilizador se ha comido medio cuadro | `Cropping Ratio` muy bajo, o plano sin margen | Sube `Cropping Ratio` y reanaliza, o baja `Strength` |
| El análisis no encuentra nada | Plano sin detalle: cielo, pared, niebla | Ese plano no se estabiliza |
| El plano reencuadrado se ve blando | Has pasado el margen de ampliación | Baja el `Zoom` o cambia de plano |
| El recorte deja ver lo de la pista de abajo | Es lo que hace un recorte: transparencia | Si querías negro, pon negro debajo |
| El reencuadre animado tiembla | Demasiados keyframes | Bórralos y deja tres o cuatro |
| El `Dynamic Zoom` va al revés | El verde y el rojo cambiados | Botón `Swap` |
| Un clip se mueve solo al hacer clic en el visor | El botón de transformación quedó encendido | Apágalo |
| Fallan seis checks de golpe | Tienes abierta `BC-Montaje-v3` | Doble clic en `BC-Montaje-v4` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Velocidad variable y calidad de imagen](03-velocidad-variable-y-calidad-de-imagen.md) | **04 · Transformaciones, keyframes y estabilización** | — |

← [Volver a la Semana 10](../README.md)
