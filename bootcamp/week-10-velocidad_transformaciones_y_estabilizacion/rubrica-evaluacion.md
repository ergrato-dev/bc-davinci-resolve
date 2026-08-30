# 📊 Rúbrica de evaluación — Semana 10

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en la
tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 10` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Tienes un plano grabado a 50 fps en una timeline a 24 fps. ¿Cuál es su techo de cámara lenta?
   Escribe la operación. ¿Y el de un plano grabado a 24 fps?
2. Enumera las cuatro formas de cambiar la velocidad de un clip en la Edit page y di, para cada una,
   si permite velocidad variable y si ripplea la timeline.
3. ¿Qué hace exactamente la casilla `Ripple Sequence`? Describe qué le pasa al clip siguiente en
   los dos casos.
4. ¿Qué le pasa al audio de un clip al que le pones una rampa de velocidad? ¿Y a uno al que le
   pones un reverse del clip entero? ¿Por qué son distintos?
5. Estás mirando la pista de control de retime de un clip. Ves flechas **amarillas y muy
   separadas** en un tramo, y **barras rojas verticales** en otro. ¿Qué hace el clip?
6. ¿Qué diferencia hay entre el asa de arriba y el asa de abajo de un punto de velocidad?
7. Un plano ralentizado se ve con **doble imagen fantasmal**. ¿Cómo se llama ese artefacto, qué
   método de relleno lo produce y a cuál cambiarías? ¿Y si en vez de eso se **derriten los
   bordes**?
8. Tienes un clip a 3840 × 2160 en un proyecto a 1920 × 1080. ¿Hasta qué valor de `Zoom` puedes
   subir sin perder nitidez? ¿Y si el clip fuera a 1920 × 1080?
9. ¿Qué tres controles del grupo `Stabilization` obligan a volver a pulsar `Stabilize`? ¿Cuál es el
   que se puede tocar sin reanalizar, y para qué sirve?
10. Quieres estabilizar un plano que tiene una panorámica intencionada. ¿Qué control **no** debes
    usar y cuál sí? Explica por qué.

<details>
<summary>📝 Respuestas</summary>

**1.** `techo = cadencia de proyecto ÷ cadencia de rodaje × 100`.

- A 50 fps: `24 ÷ 50 × 100` = **48 %**
- A 24 fps: `24 ÷ 24 × 100` = **100 %**, es decir, **no admite cámara lenta** sin que Resolve
  invente fotogramas

**2.**

| Vía | ¿Variable? | ¿Ripplea? |
| --- | ---------- | --------- |
| `Change Clip Speed` | No | Solo con `Ripple Sequence` marcada |
| `Speed Change` del Inspector | No, pero sus valores aceptan keyframes | Solo con `Ripple Sequence` marcada |
| `Fit to Fill` | No | **Nunca** |
| `Retime Controls` | **Sí** | Según el modo: no en `Selection Mode`, sí en `Trim Edit Mode` |

**3.** Decide si la timeline se recoloca al cambiar la duración del clip.

- **Marcada**: todo lo que viene detrás se desplaza. La pieza cambia de duración y no se pierde
  material
- **Desmarcada**: el clip crece y **pisa** al clip siguiente, o encoge y deja un hueco

Ninguna de las dos es la correcta siempre. Lo destructivo es la segunda: lo que se pisa no vuelve
sin `Ctrl+Z`.

**4.** Una **rampa** es velocidad variable, y la velocidad variable **silencia el audio del clip
entero**. No es un ajuste: es el comportamiento documentado.

Un **reverse del clip entero** es velocidad lineal, así que el audio se retima con el vídeo y
**suena hacia atrás**.

La diferencia está en que en un efecto variable no hay una sola velocidad que aplicarle al audio.

**5.** El clip tiene al menos **dos tramos**: uno **ralentizado** —amarillas y separadas es por
debajo del 100 %— y otro **congelado** —las barras rojas verticales marcan un freeze intermedio—.
Es un efecto de velocidad variable, así que además su audio está silenciado.

**6.** La **de arriba** cambia **la velocidad** del tramo que tiene a su izquierda: a la derecha lo
ralentiza, a la izquierda lo acelera.

La **de abajo** cambia **qué trozo del plano** ocupa ese tramo, manteniendo su velocidad:
reasigna fotogramas entre tramos vecinos.

Las dos alargan o acortan el clip, pero por motivos distintos y en cantidades distintas.

**7.** La doble imagen fantasmal es **ghosting**, y la produce **`Frame Blend`**, que funde dos
fotogramas contiguos. Se cambia a **`Optical Flow`**.

Los bordes que se derriten son **warping**, y lo produce **`Optical Flow`** cuando calcula mal el
movimiento. Se baja a **`Frame Blend`**.

Es la razón por la que «el de más calidad» no es la respuesta automática: cada método tiene su
artefacto y cada plano su método.

**8.** `resolución del clip ÷ resolución del proyecto`:

- 3840 ÷ 1920 = **2,0**. Puedes llegar a `Zoom` 2,0 sin perder un píxel
- 1920 ÷ 1920 = **1,0**. Cualquier valor por encima de 1,0 ya cuesta nitidez

**9.** Obligan a reanalizar: **el modo** (`Perspective`, `Similarity`, `Translation`),
**`Cropping Ratio`** y **`Smooth`**.

El que no reanaliza es **`Strength`**: es un multiplicador del resultado ya calculado. Sirve para
afinar cuánto del movimiento original quieres dejar pasar. Entre 0,6 y 0,9 quedan bien la mayoría
de los planos grabados a pulso, porque conservan algo de pulso humano.

**10.** **No** debes usar `Camera Lock`: intenta eliminar **todo** el movimiento de cámara,
incluida la panorámica, que es intencionada. El estabilizador se queda sin margen y el resultado
ondula.

Sí debes usar **`Smooth`**, que suaviza el movimiento en vez de eliminarlo: la panorámica sigue
siendo una panorámica, sin el temblor.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **10 puntos**.

```bash
python scripts/verificar-semana.py 10
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 01 | `proyecto-abierto` | 10 |
| 01 | `frame-rate-bloqueado` | 10 |
| 01 | `montaje-v3-conservada` | 10 |
| 01 | `montaje-v4-existe` | 10 |
| 01 | `montaje-v4-activa` | 10 |
| 01 | `marcadores-de-velocidad` | 10 |
| 01 · 04 | `marcadores-de-estabilizacion` | 10 |
| 02 | `montaje-v4-clips` | 10 |
| 02 | `montaje-v4-sin-huecos` | 10 |
| 02 · 03 | `retimes-aplicados` | 10 |

**Necesitas 70 / 100**, es decir **al menos 7 de los 10 checks**.

> [!TIP]
> Seis de los diez —`montaje-v4-activa`, `montaje-v4-clips`, `montaje-v4-sin-huecos`,
> `retimes-aplicados`, `marcadores-de-velocidad` y `marcadores-de-estabilizacion`— leen **la
> timeline activa**. Si te quedaste comparando en `BC-Montaje-v3` en el paso 8 de la práctica 04,
> fallan los seis de golpe aunque el trabajo esté perfecto. Doble clic en `BC-Montaje-v4` y repite:
> es lo primero que hay que descartar.
>
> Si fallan **todos**, el puente no está lanzado: `Workspace > Scripts > Utility`.

---

## 📦 Producto (30 %)

Tu pieza con el tiempo y el encuadre trabajados. Se evalúa con criterios observables, y esta
semana el producto pesa más de lo que dice el porcentaje: **la mitad de lo que se aprende aquí no
se puede leer por la API**.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Ninguna cámara lenta va a tirones, vista a tamaño completo | 15 |
| Ningún retime tiene bordes derretidos ni doble imagen | 10 |
| Ningún plano estabilizado ha perdido algo importante por el recorte | 5 |
| No hay parpadeos a negro en toda la reproducción | 5 |
| `notas-de-montaje.md` tiene el apartado `## Velocidad y transformaciones — Semana 10` con sus seis bloques | 5 |
| Las cifras del apartado son cifras: cadencias, porcentajes, techos, valores de `Strength` | 5 |
| `BC-Bootcamp-Resolve-semana10.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Los cambios de velocidad se leen como decisiones, no como efectos | 15 |
| La rampa cae **antes** del instante que subraya, y su entrada está justificada por escrito | 10 |
| La comparación de los tres métodos de relleno está contestada describiendo los artefactos | 10 |
| Ningún plano estabilizado parece un render: queda pulso | 5 |
| Los planos que no se dejaron estabilizar están descartados con su razón técnica | 5 |
| El reencuadre animado no tiembla y usa pocos keyframes | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| El media pool | `BC-Montaje-v3` y `BC-Montaje-v4`, las dos, colgando de `Master` |
| Las duraciones de las dos timelines | Son distintas, y sabes por qué y cuánto |
| Los distintivos de retime de la timeline | Los reconoces todos: ninguno es un arrastre accidental |
| Un clip retimado, con `Ctrl+R` / `Cmd+R` | El porcentaje es el que decidiste, no un 97 % |
| El `Inspector` de los clips retimados | Los que lo pedían están en `Frame Blend`, no todos en `Optical Flow` |
| El `Inspector` de los planos estabilizados | Modo elegido a conciencia y `Strength` por debajo de 1 donde tocaba |
| El plano del `Dynamic Zoom` | `Dynamic Zoom Ease` en `Ease In and Out`, no en `Linear` |
| El visor de timeline | El botón `Transform/Crop/Dynamic Zoom` está **apagado** |
| Los clips de la timeline | Ninguno con los `Retime Controls` abiertos |
| `Index > Markers` | Los morados y cianes resueltos pasados a azul; los que quedan son trabajo real |
| La pieza entera | Ni títulos diseñados, ni ResolveFX, ni color, ni mezcla |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| `BC-Montaje-v3` ha desaparecido o se ha trabajado encima | −20 |
| Una cámara lenta va claramente a tirones y se ha entregado así | −15 |
| Un retime ha pisado y borrado parte del plano siguiente | −15 |
| Un plano estabilizado ha perdido algo que importaba por el recorte | −10 |
| Todo el proyecto en `Optical Flow` sin haber revisado ni un clip | −10 |
| El apartado de notas describe con adjetivos y no con cifras y planos concretos | −10 |
| Un plano reencuadrado se ve visiblemente más blando que sus vecinos | -5 |
| Se quedaron los `Retime Controls` abiertos en algún clip | −5 |
| Se quedó encendido el botón de transformación del visor | −5 |
| Se empezó a titular o a poner efectos, que es la Semana 11 | −5 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

Esta semana no bloquea la 11 —los títulos se pueden aprender sobre una pieza sin retimar—, pero sí
deja una deuda que se paga cara: si retimas o reencuadras **después** de titular, los rótulos se
descolocan y hay que recolocarlos uno a uno.

- **Si fallan `montaje-v4-activa` y los cinco siguientes**: tienes abierta `BC-Montaje-v3`. Doble
  clic en `BC-Montaje-v4`. Es lo primero que hay que descartar, siempre.
- **Si falla `montaje-v3-conservada`**: renombraste el montaje en vez de duplicarlo. Recupéralo del
  respaldo `BC-Bootcamp-Resolve-semana09.drp`, importándolo con otro nombre para no machacar lo que
  tienes.
- **Si falla `montaje-v4-clips`**: has borrado planos enteros. Esta semana no se remonta. Restaura
  el respaldo de timeline `antes-de-retimar` de la práctica 01.
- **Si falla `montaje-v4-sin-huecos`**: casi siempre es un retime hecho con `Ripple Sequence`
  desmarcada que dejó hueco al acortar. Recorre la pista en `Detail Zoom` y cierra con
  `Forward Delete`.
- **Si falla `retimes-aplicados`**: o tienes menos de tres, o los que tienes no cambian la
  correspondencia entre origen y timeline. Recuerda que **un reverse al 100 % no cuenta**. Haz un
  acelerado, una cámara lenta o un freeze más.
- **Si fallan los checks de marcadores**: o tienes menos de los que pide, o alguno conserva su
  `Marker N` de fábrica, o el color no es el que espera el check: **`Purple`** para velocidad,
  **`Cyan`** para estabilización. Ordena el `Marker Index` por `Name`.
- **Si el cuestionario va por debajo de 70**: las preguntas 1, 7 y 9 son las que más gente falla.
  La 1 y la 7 son el mismo tema de fondo —de dónde salen los fotogramas que no se grabaron—:
  vuelve a las teorías 01 y 06. La 9 es la teoría 09, y se arregla leyendo la tabla de los seis
  controles.
- **Si el producto va por debajo de 70**: casi siempre es una de dos. O ralentizaste por debajo del
  techo y entregaste el judder, o pusiste `Optical Flow` en todo y no revisaste ni un plano. Lo
  primero se arregla subiendo porcentajes; lo segundo, con el paso 6 de la práctica 03, que son
  quince minutos.
- **Si te faltó tiempo**: prioriza las prácticas 01 y 02, y de la 03 quédate con el paso 6. La
  rampa y el `Dynamic Zoom` se hacen otro día en veinte minutos; aprender a ver un artefacto, no.

---

← [Volver a la Semana 10](README.md)
