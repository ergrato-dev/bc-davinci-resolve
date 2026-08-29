# 📊 Rúbrica de evaluación — Semana 07

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en la
tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 07` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Enuncia la regla que decide si algo toca acabarse esta semana o esperar. Pon dos ejemplos
   de cosas que la regla manda posponer, con la semana en la que tocan.
2. ¿Qué es una cola? ¿Cuánta cola consume una disolvencia centrada de un segundo a 24 fps, y
   cuánta la misma disolvencia alineada al final del corte?
3. ¿Qué hace Resolve cuando le pides una transición y no hay cola suficiente? Nombra los tres
   síntomas de que eso ha pasado.
4. Nombra los tres significados legítimos de una disolvencia. ¿Por qué `Add Dissolve to All
   Edits` es mala idea, con dos argumentos distintos?
5. ¿Qué hace `Smooth Cut` y en qué se diferencia de una disolvencia? ¿Cuál es su rango de
   duración recomendado, y por qué no el que pone por defecto?
6. Explica por qué cambiar la velocidad de un clip de `Video 1` puede descolocar un rótulo
   que hay en `Video 3`.
7. ¿Por qué la cámara lenta se ve a tirones con material grabado a 24 fps? ¿Qué dos cosas
   puede hacer Resolve para rellenar, y qué defecto tiene cada una?
8. ¿Qué es el 0 dBFS y qué pasa cuando una señal intenta pasar de ahí? ¿Se puede arreglar
   después bajando el clip?
9. ¿Por qué los títulos van en `Video 3` y no en `Video 2`? Da las tres razones.
10. ¿En qué se diferencia `Quick Export` de la Deliver page, y por qué el archivo que sale de
    esta semana no es un master?

<details>
<summary>📝 Respuestas</summary>

**1.** La regla: **¿lo que hay debajo de esto se va a mover todavía?** Si la respuesta es sí,
no se hace ahora.

Ejemplos de lo que manda posponer: afinar un corte al fotograma (**Semana 09**, porque
cualquier cambio anterior lo desafina), diseñar un rótulo con tipografía y animación
(**Semana 11**), mezclar el audio a un objetivo de loudness (**Semanas 13-15**), o corregir el
color de un plano que puede acabar fuera de la pieza (**Semanas 16-22**).

**2.** Una **cola** (*handle*) es el material del archivo que queda **fuera** del rango marcado
con `I` y `O`: lo que hay antes del punto de entrada y después del punto de salida. Sigue en
el archivo y no se ve en la timeline.

Una disolvencia **centrada** de un segundo a 24 fps consume **12 fotogramas de cola de salida**
del clip que sale y **12 de cola de entrada** del que entra.

La misma disolvencia alineada al final del corte (`End on Edit`) consume **24 fotogramas
seguidos del clip que entra** y ninguna del otro.

**3.** No falla ni avisa: **acorta la transición** a lo que las colas permitan, en silencio.

Los tres síntomas: la transición sale **más corta** de lo que pediste y no se deja alargar; el
clip **no se deja alargar** al arrastrar su borde, porque llegó al media limit; y la transición
aparece **descentrada** respecto al corte, porque solo cabía a un lado.

**4.** Los tres significados: **paso del tiempo**, **cambio de localización** y **cambio de
tema**.

`Add Dissolve to All Edits` es mala idea por dos razones distintas. La **narrativa**: un signo
de puntuación que se repite en todos los cortes deja de significar nada, y la pieza se vuelve
blanda. La **técnica**: consume cola en todos los cortes a la vez, y donde no la haya, la
transición saldrá corta o descentrada sin avisar.

**5.** `Smooth Cut` **no mezcla las dos imágenes: deforma una para convertirla en la otra**,
moviendo progresivamente los mismos rasgos de la posición que tenían antes del corte a la que
tienen después. Una disolvencia superpone; `Smooth Cut` desplaza.

Su rango recomendado es de **2 a 6 fotogramas**, no el segundo que pone por defecto: con un
segundo la deformación se hace visible y el sujeto parece de goma.

**6.** Porque un cambio de velocidad **cambia la duración del clip**, y `Video 1` hace
**ripple**: todo lo que venía detrás se recoloca automáticamente para que no queden huecos.

Las pistas de encima **no** hacen ripple: el rótulo de `Video 3` se queda exactamente donde
estaba. Así que el material de debajo se ha desplazado y el rótulo ya no coincide con lo que
rotulaba.

**7.** Porque al 50 % hay que enseñar 24 fotogramas por segundo de timeline y solo hay 12
grabados para ese segundo.

Resolve puede **repetir** cada fotograma —y entonces el movimiento se ve escalonado, a
tirones— o **interpolar**, inventando los intermedios, que se ve más fluido pero puede
deformar lo que se mueve rápido.

Por eso la cámara lenta buena **se graba a alta cadencia**, no se hace después.

**8.** **0 dBFS** es el máximo absoluto que un archivo de audio digital puede representar. No
hay nada por encima.

Cuando una señal intenta pasar, se **recorta**: los picos se aplanan y suena a distorsión
áspera.

Y **no**, no se arregla bajando el clip después: la información **ya no está en el archivo**.
Bajarlo lo deja bajo y distorsionado. La única solución de verdad es volver a grabarlo.

**9.** Tres razones:

- **Se pisan.** En la timeline manda siempre la pista más alta: si un rótulo cae donde hay un
  recurso, uno de los dos desaparece.
- **No se encuentran.** Buscar seis rótulos entre veinte recursos, en la Semana 11, es perder
  la tarde.
- **No se pueden apagar de golpe.** Con los títulos en su propia pista, desactivarla enseña la
  pieza sin rótulos en un clic.

**10.** `Quick Export` ofrece **presets cerrados** —el codec, el bitrate y la resolución vienen
decididos— y saca un archivo en tres clics desde cualquier página. La **Deliver page** permite
elegir todo eso, tiene cola de render y controla escalado, niveles de datos y subtítulos.

El archivo de esta semana **no es un master** porque no controlas su calidad fina, y porque lo
que hay dentro no está terminado: sin mezcla, sin color y sin créditos completos. Es una
**prueba de visionado**. El master es la Semana 28.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **11,11 puntos**.

```bash
python scripts/verificar-semana.py 07
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 01 | `proyecto-abierto` | 11,11 |
| 01 | `frame-rate-bloqueado` | 11,11 |
| 01 | `montaje-v1-conservada` | 11,11 |
| 01 | `montaje-v2-existe` | 11,11 |
| 01 | `montaje-v2-activo` | 11,11 |
| 01 | `montaje-v2-clips` | 11,11 |
| 02 | `montaje-v2-sin-huecos` | 11,11 |
| 03 | `montaje-v2-pista-de-titulos` | 11,11 |
| 04 | `bin-entregas` | 11,11 |

**Necesitas 70 / 100**, es decir **al menos 7 de los 9 checks**.

> [!TIP]
> Cuatro de los nueve —`montaje-v2-activo`, `montaje-v2-clips`, `montaje-v2-sin-huecos` y
> `montaje-v2-pista-de-titulos`— leen **la timeline activa**. Si te quedaste comparando en
> `BC-Montaje-v1`, fallan los cuatro de golpe aunque el trabajo esté perfecto. Doble clic en
> `BC-Montaje-v2` y repite: es lo primero que hay que descartar.
>
> Si fallan **todos**, el puente no está lanzado: `Workspace > Scripts > Utility`.

---

## 📦 Producto (30 %)

Tu pieza acabada y su entrega. Se evalúa con criterios observables.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| El archivo `BC-Montaje-v2-semana07.mp4` existe en `03-entregas/` y se reproduce entero fuera de Resolve | 15 |
| No hay ningún parpadeo a negro en toda la reproducción del archivo | 10 |
| La pieza se escucha de principio a fin sin tocar el volumen del sistema | 10 |
| `notas-de-montaje.md` tiene el apartado `## Acabado — Semana 07` con sus seis puntos | 5 |
| Las cifras del apartado son cifras, incluida la de cuánta cola tiene el material | 5 |
| `BC-Bootcamp-Resolve-semana07.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Cada transición de la pieza tiene un motivo de los tres, escrito | 10 |
| Ninguna transición se quedó con la duración por defecto sin decidirla | 5 |
| Los `Smooth Cut` no se notan al reproducir a velocidad normal | 10 |
| Todos los saltos están decididos: reparados, tapados o dejados a propósito | 5 |
| Los cambios de velocidad se justifican y la cámara lenta no va a tirones | 5 |
| Los recursos de `Video 2` no ensucian la voz de debajo | 5 |
| Los rótulos se leen, también en una pantalla pequeña, y no tapan caras | 5 |
| El rótulo de cierre lleva la atribución del material con licencia | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| El media pool | `BC-Montaje-v1` y `BC-Montaje-v2`, las dos, con esos nombres exactos |
| El bin `12-Entregas` | Contiene el `.mp4` de esta semana y se reproduce en el visor |
| La timeline de arriba, con el Boring Detector | Ningún rojo de uno o dos fotogramas |
| Cabecera de `Video 3`, desactivándola | Solo desaparecen rótulos, nada más |
| Cabecera de `Video 2`, desactivándola | El montaje sigue funcionando, con el mismo audio y duración |
| Un `Smooth Cut`, a velocidad normal | No se ve el salto y no se ve la deformación |
| Un plano ralentizado | El movimiento es continuo, no escalonado |
| Un tramo con recurso, con auriculares | Se entiende cada palabra de la voz de debajo |
| Un rótulo, en el visor pequeño | Se lee sin esfuerzo |
| La pieza entera | Ni música, ni subtítulos, ni color, ni animación de títulos |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| `BC-Montaje-v1` ha desaparecido: se renombró en vez de duplicarla | −20 |
| El archivo exportado tiene un parpadeo a negro | −15 |
| Hay una disolvencia en todos o casi todos los cortes | −15 |
| Los `Smooth Cut` se ven: deformación visible a velocidad normal | −10 |
| Hay música, subtítulos, color o animación de títulos | −10 |
| El archivo exportado no se ha visto entero fuera de Resolve | −10 |
| Los rótulos están en `Video 2`, mezclados con los recursos | −10 |
| Un plano ralentizado por debajo del 40 % con material a 24 fps | −5 |
| Falta la atribución del material con licencia en el rótulo de cierre | −5 |
| El apartado de notas describe con adjetivos y no con cifras | −10 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

Esta semana cierra la Fase 2. La 08 abre la Edit page y trabaja sobre el mismo montaje, así
que un acabado a medias se arrastra, pero no bloquea: lo que sí bloquea es un montaje que no
llegue al final, y eso era la Semana 06.

- **Si fallan `montaje-v2-activo` y los tres siguientes**: tienes abierta otra timeline. Doble
  clic en `BC-Montaje-v2`. Es lo primero que hay que descartar, siempre.
- **Si falla `montaje-v1-conservada`**: renombraste en vez de duplicar. Recupera `v1` del
  respaldo `BC-Bootcamp-Resolve-semana06.drp`, e importa el proyecto con otro nombre para no
  machacar lo que tienes.
- **Si falla `montaje-v2-clips`**: la escena multicámara no entró, o entró en la pista
  equivocada. Práctica 01, paso 6: se copia de `Video 1` y se pega en `Video 1`.
- **Si falla `montaje-v2-sin-huecos`**: hay un hueco o un solape. Activa el imán con `N`,
  recorre la pieza en vista de detalle y bórralo con ripple. Suele estar donde pegaste la
  escena multicámara.
- **Si falla `montaje-v2-pista-de-titulos`**: no has creado `Video 3`. Práctica 03, paso 6.
- **Si falla `bin-entregas`**: o el bin no se llama exactamente `12-Entregas`, o el archivo
  cayó en otro bin. Selecciona el bin **antes** de importar.
- **Si el cuestionario va por debajo de 70**: las preguntas 2, 3 y 6 son las que más gente
  falla, y las tres son el mismo tema de fondo. Vuelve a las teorías 02 y 05.
- **Si el producto va por debajo de 70**: casi siempre es una de dos. O te pasaste con las
  transiciones —quítalas y deja solo las que tengan motivo—, o no llegaste a ver el archivo
  exportado, que es el paso que más enseña de toda la semana.
- **Si te faltó tiempo**: prioriza la práctica 04. Exportar y ver la pieza fuera de Resolve es
  lo único que no se recupera después.

---

← [Volver a la Semana 07](README.md)
