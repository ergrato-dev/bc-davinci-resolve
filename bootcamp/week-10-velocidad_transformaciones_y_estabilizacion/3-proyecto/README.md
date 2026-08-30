# Proyecto — Semana 10: la pieza con velocidad, encuadre y pulso

> Tu montaje ya estaba afinado al fotograma. Lo que le faltaba es que **cada plano dure lo que tiene
> que durar, enseñe lo que tiene que enseñar y no tiemble**. El entregable no es un archivo nuevo:
> es la misma pieza, con tres decisiones nuevas tomadas en cada plano que las pedía.

## 📦 Qué añade esta semana

La décima capa: **`BC-Montaje-v4`, la pieza con el tiempo y el encuadre trabajados**.

Concretamente, cinco cosas:

1. **`BC-Montaje-v4`**, duplicada de `BC-Montaje-v3`, con **tres cambios de velocidad o más** y sin
   huecos.
2. **Una rampa de velocidad** construida a mano y afinada en la curva, con la decisión de si entra
   suave o seca escrita y justificada.
3. **Los planos que temblaban, estabilizados**, cada uno con su modo y su `Strength` anotados; y los
   que no se dejaron, descartados por escrito con su razón.
4. **Un reencuadre animado con keyframes** y un `Dynamic Zoom` con easing.
5. **La comparación escrita** entre `BC-Montaje-v3` y `BC-Montaje-v4`, con cifras.

> [!IMPORTANT]
> `BC-Montaje-v3` **no se toca**. Es la referencia contra la que se mide la semana y la comparación
> del paso 8 de la práctica 04 la necesita entera. Es la convención de versionado de
> [`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md): cada fase duplica y
> trabaja sobre la copia.

Y una cosa que no es un archivo: **el orden**. Velocidad, estabilización, reencuadre. De la Semana
11 a la 36 vas a tocar planos que ya tienen las tres cosas, y hacerlas en otro orden significa
rehacerlas.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca carácter
a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` del proyecto sigue siendo **24**
3. **`BC-Montaje-v3`** sigue existiendo
4. Existe la timeline **`BC-Montaje-v4`**
5. **`BC-Montaje-v4`** es la timeline abierta
6. Su pista de vídeo principal conserva **quince clips o más**
7. Esa pista **no tiene huecos ni solapes**
8. **Tres clips de vídeo o más** tienen la velocidad cambiada
9. Hay **tres marcadores morados o más**, todos con nombre propio
10. Hay **dos marcadores cianes o más**, todos con nombre propio

```bash
python scripts/verificar-semana.py 10
```

Con el proyecto abierto, **`BC-Montaje-v4` como timeline activa** y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!NOTE]
> Los checks 5 a 10 leen **la timeline activa**. Si te quedaste comparando en `BC-Montaje-v3` en el
> paso 8 de la práctica 04, fallan los seis de golpe aunque el trabajo esté perfecto. Doble clic en
> `BC-Montaje-v4` y repite.
> *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de 2026.*

### Cómo detecta el verificador un retime, y qué no ve

El check 8 no lee un campo «velocidad»: **la API de scripting de Resolve no expone uno**. Lo que
hace es comparar, clip a clip, el **rango de origen que usa** —del fotograma tal al fotograma
cual del archivo— con **lo que ocupa en la timeline**. En un clip al 100 % los dos números
coinciden; en un clip retimado, no.

Dos consecuencias que conviene saber antes de que te sorprendan:

| Situación | Qué pasa con el check |
| --------- | --------------------- |
| Un **reverse al 100 %** | **No cuenta.** Usa los mismos fotogramas en la misma duración |
| Un **acelerado, una cámara lenta, un freeze o una rampa** | Cuenta |
| Un clip grabado a una **cadencia distinta** de la de la timeline | Puede contar aunque esté al 100 %, porque el conformado también descuadra los dos números |

La última fila es un falso positivo posible si tu material es de cadencia mixta. No se puede
distinguir por la API. Por eso el criterio de verdad de este entregable está en la rúbrica: **tres
cambios de velocidad que se vean al reproducir la pieza**, no tres filas que cuadren.

*Relación verificada contra la API en 21.0.4.5 para clips al 100 %, agosto de 2026.*

### Lo que no se puede verificar por API, y dónde se evalúa

| No verificable | Dónde se evalúa |
| -------------- | --------------- |
| Si un retime tiene *judder*, *ghosting* o *warping* | Rúbrica, criterio observable |
| Si un plano está estabilizado y con qué modo | Marcador cian + rúbrica |
| El valor de `Strength`, `Smooth` o `Cropping Ratio` | Notas escritas + rúbrica |
| Los parámetros de `Transform` y sus keyframes | Rúbrica, criterio observable |
| Si el `Dynamic Zoom` tiene easing | Rúbrica, criterio observable |

---

## 📝 El entregable escrito

### `notas-de-montaje.md`, apartado `## Velocidad y transformaciones — Semana 10`

En `BC-Resolve/04-respaldos/`, en el mismo archivo de las Semanas 06 a 09.

Se abre en la práctica 01 y se cierra en la práctica 04. Al final tiene que llevar seis bloques:

> **Las cadencias de tu material**: cuántos clips a cada cadencia y el techo de cámara lenta de
> cada grupo.
>
> **Los retimes**: qué planos, qué porcentajes, cuáles acelerados y cuáles ralentizados, y cuánto
> ha cambiado la duración total de la pieza.
>
> **La rampa**: qué plano, qué instante subraya, qué velocidad tiene el tramo lento, y si la
> dejaste suave o seca **y por qué**.
>
> **La comparación de los tres métodos de relleno**: qué viste con `Nearest`, con `Frame Blend` y
> con `Optical Flow` en el mismo plano, y cuál elegiste describiendo el artefacto que te hizo
> descartar los otros dos.
>
> **La estabilización**: qué planos, con qué modo, con qué `Strength`, y cuáles no se dejaron
> estabilizar y por qué.
>
> **Qué pasa a la Semana 11**: lo que queda sin resolver, con el minuto aproximado de cada cosa.

Los dos que más valen son el cuarto y el quinto. El de los métodos porque es el que enseña a
**mirar** un retime, y esa es la habilidad que no caduca; el de la estabilización porque los
planos que declares no estabilizables son una decisión técnica, y saber decir que no se puede
vale tanto como saber hacerlo.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| Ninguna cámara lenta va a tirones | Se reproduce a tamaño completo mirando los bordes de lo que se mueve |
| Ningún retime tiene bordes derretidos ni doble imagen | Lo mismo, en los tramos retimados |
| Los cambios de velocidad se leen como decisiones, no como efectos | Se ve la pieza entera: ninguno llama la atención sobre sí mismo |
| La rampa cae **antes** del instante que subraya, no encima | Se mira ese plano a cámara lenta |
| El freeze está colocado en el fotograma correcto | Se pausa ahí: el gesto es el que quería congelarse, y está nítido |
| Ningún plano estabilizado parece un render | Se reproduce: queda algo de pulso |
| Ningún plano estabilizado ha perdido algo importante por el recorte | Se apaga y se enciende el interruptor de `Stabilization` |
| Los planos con movimiento intencionado lo conservan | La panorámica sigue siendo una panorámica |
| Ningún plano reencuadrado se ve más blando que sus vecinos | Visor al 100 %, comparando con el plano de al lado |
| El reencuadre animado no tiembla | Se reproduce ese plano entero |
| El `Dynamic Zoom` arranca y para suavemente | Se reproduce: no hay tirón al principio ni al final |
| No hay parpadeos a negro | Se reproduce entera |
| Nada de lo que todavía no toca | Ni títulos diseñados, ni ResolveFX, ni color, ni mezcla |

El último sigue siendo el que más gente incumple. La tentación concreta de esta semana es abrir la
`Effects Library` y poner un desenfoque, o empezar a rotular los freezes. Las dos cosas son la
Semana 11.

---

## 💡 Adaptación a tu pieza

**Documental corto** · Tu semana es de **estabilización y reencuadre**. Los planos de recurso
grabados a pulso son los que más destacan al lado de una entrevista con trípode, y son los que hay
que calmar. Y el reencuadre animado te sirve para convertir un plano general en un plano medio
cuando la entrevista pide acercarse. La velocidad, poca: un acelerado en un recurso largo y poco
más.

**Videoclip** · Tu semana es de **velocidad variable**. La duración total está atada a la música,
así que los retimes se compensan entre sí: lo que ralentizas aquí lo aceleras allá. Ojo con el
techo, que en un videoclip se pide siempre demasiada cámara lenta. Y `Ripple Sequence` **marcada**
siempre, para que la sincronía con la música no se rompa en silencio.

**Cortometraje de ficción** · Tu semana es de **freeze y reencuadre**. La velocidad en ficción se
nota mucho y se usa poco. Lo que sí vas a usar es el reencuadre para arreglar los planos donde el
encuadre no salió, y la estabilización en los planos a pulso que quieras que parezcan intencionados
y no descuidados.

**Tutorial o vídeo formativo** · Tu semana es de **acelerados y `Dynamic Zoom`**. Todo proceso
manual —montar algo, escribir algo, esperar a que algo cargue— se acelera. Y el `Dynamic Zoom` es
lo que hace que un plano fijo de una pantalla o de una mesa se pueda mirar quince segundos sin
aburrir.

**Pieza de viaje** · Tu semana es de **cámara lenta y estabilización**, y es la que más material
sobrecadenciado suele tener. Comprueba el techo de cada plano antes de ralentizar, y estabiliza
todo lo que grabaste andando. Cuidado con el agua y con las hojas: ahí `Frame Blend`, no
`Optical Flow`.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 10` en verde, diez de diez
2. `BC-Montaje-v4` abierta, sin huecos, con quince clips o más en la pista principal
3. `BC-Montaje-v3` intacta
4. Tres cambios de velocidad o más, uno de ellos una rampa
5. Los planos que temblaban, estabilizados o descartados por escrito
6. Un reencuadre animado y un `Dynamic Zoom` con easing
7. `notas-de-montaje.md` con el apartado `## Velocidad y transformaciones — Semana 10` cerrado, con
   sus seis bloques
8. Ningún clip con los `Retime Controls` abiertos y el botón de transformación del visor apagado
9. Respaldo de la semana: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana10.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza las prácticas 01 y 02, y del resto quédate con el **paso 6 de la
> práctica 03**: la comparación de los tres métodos de relleno. Es el ejercicio que enseña a mirar,
> y sin él los retimes de las veintiséis semanas que quedan se hacen a ciegas. La rampa y el
> `Dynamic Zoom` se pueden hacer otro día en veinte minutos.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Retimar encima de `BC-Montaje-v3` | Parece más práctico | Se duplica; la comparación necesita las dos |
| Ralentizar sin mirar la cadencia del clip | Nadie mira la columna `FPS` | El techo es una división; hazla antes |
| Retimar con `Ripple Sequence` desmarcada sin querer | La casilla recuerda su último estado | Decídela antes de escribir el porcentaje |
| Poner `Optical Flow` en todo y no revisarlo | Es «el de más calidad» | En agua, humo y cruces, `Frame Blend` |
| Rampas en la mitad de los planos | Se le coge el gusto | Una, dos como mucho |
| Estabilizar antes de retimar | Se hace en el orden en que aparecen los problemas | Velocidad, estabilización, reencuadre |
| Estabilizar con `Camera Lock` un plano con panorámica | Suena a «lo mejor» | `Smooth`, y `Camera Lock` solo para clavar |
| Dejar `Strength` en 1 en todos | Es el valor de fábrica | Entre 0,6 y 0,9 en los planos a pulso |
| Ampliar un plano HD en un proyecto HD | La pérdida no se ve en el visor pequeño | Visor al 100 % antes de decidir |
| Animar con quince keyframes | Se corrige plano a plano en vez de por tramos | Tres o cuatro y afina la curva |
| Dejar los `Retime Controls` abiertos | No molestan a la vista | Un roce cambia una velocidad sin avisar |
| Dejar el botón de transformación del visor encendido | Se olvida | Un clic en el visor mueve un plano |
| Verificar con `BC-Montaje-v3` abierta | Es la última que tocaste al comparar | Doble clic en `BC-Montaje-v4` |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 09](../../week-09-trimming_quirurgico/3-proyecto/README.md) | **Proyecto Semana 10** | [Semana 11](../../week-11-titulos_texto_plus_efectos_y_compuestos/README.md) |

← [Volver a la Semana 10](../README.md)
