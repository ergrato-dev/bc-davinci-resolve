# Proyecto — Semana 11: la pieza que se entiende

> Tu montaje ya está afinado al fotograma, con la velocidad y el encuadre decididos. Lo que le
> falta es que **se entienda sin que estés tú al lado explicándola**: quién habla, dónde estamos,
> cómo se titula. El entregable de esta semana es información, no decoración.

## 📦 Qué añade esta semana

La undécima capa: **`BC-Montaje-v5`, la pieza rotulada y con sus transiciones**.

Concretamente, cinco cosas:

1. **`BC-Montaje-v5`**, duplicada de `BC-Montaje-v4`, con **tres clips o más en la `V2`**: el
   título de entrada y al menos dos rótulos de identificación.
2. **Un estilo de rótulo propio**, construido una vez con su tipografía, su contorno y su sombra, y
   **guardado en el media pool** para no volver a construirlo.
3. **Las transiciones que la pieza pedía**, y solo esas, cada una con su alineación decidida.
4. **Un adjustment clip** en la `V3` aplicando un efecto a un tramo, en vez de plano a plano.
5. **Un compound clip** de un bloque, con el motivo por el que existe escrito.

> [!IMPORTANT]
> `BC-Montaje-v4` **no se toca**. Es la referencia contra la que se mide la semana y la comparación
> del paso 7 de la práctica 04 la necesita entera. Es la convención de versionado de
> [`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md): cada fase duplica y
> trabaja sobre la copia.

Y una cosa que no es un archivo: **el reparto de pistas**. `V1` el montaje, `V2` los rótulos, `V3`
los ajustes. De la Semana 12 a la 36 vas a añadir capas encima de estas tres, y tenerlas ordenadas
desde ahora es la diferencia entre once pistas con sentido y once pistas a ver qué había en cada
una.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca carácter
a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. **`BC-Montaje-v4`** sigue existiendo
3. **`BC-Montaje-v5`** existe y es la timeline abierta
4. Su pista de vídeo **1** conserva **quince clips o más**
5. Esa pista **no tiene huecos ni solapes**
6. Su pista de vídeo **2** tiene **tres clips o más**
7. Hay **al menos un clip en una pista de vídeo por encima de la 2**
8. El bin **`13-Titulos`** contiene **dos elementos o más**
9. Hay **tres marcadores amarillos o más**, todos con nombre propio
10. Hay **dos marcadores verdes o más**, todos con nombre propio

```bash
python scripts/verificar-semana.py 11
```

Con el proyecto abierto, **`BC-Montaje-v5` como timeline activa** y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!WARNING]
> **Siete de los diez checks leen la timeline activa**: del 3 al 7 y los dos de marcadores. Hay dos
> formas de tenerla equivocada esta semana, y las dos son fáciles:
>
> 1. Te quedaste comparando en `BC-Montaje-v4` en el paso 7 de la práctica 04
> 2. **Abriste un compound clip con `Open in Timeline` y no volviste**. Mira el control de ruta de la
>    esquina inferior izquierda de la timeline: si hay dos nombres, estás dentro del compuesto
>
> *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de 2026.*

### Qué mide cada check, y qué no ve

Los checks de esta semana cuentan **clips por pista**, no efectos. La razón es concreta: la API de
scripting de Resolve **no expone qué efectos lleva un clip**, ni si un título es un `Text+` o un
`Fusion Title`, ni qué pone dentro.

| Lo que el check mira | Lo que **no** puede saber |
| -------------------- | ------------------------- |
| Que la `V2` tiene tres clips o más | Que sean títulos, y no tres planos superpuestos |
| Que hay un clip por encima de la `V2` | Que sea un adjustment clip, y que lleve un efecto |
| Que `13-Titulos` tiene dos elementos | Que uno sea un estilo de rótulo y otro un compuesto |
| Que hay marcadores amarillos y verdes con nombre | Que el rótulo que anuncian se haya puesto |

Por eso el criterio de verdad de esta semana está en la rúbrica, y por eso el bloque de
**criterios de calidad** de más abajo pesa más que de costumbre: **casi todo lo que se aprende esta
semana se juzga mirando, no leyendo la API**.

El check 8 tiene además una particularidad: **no filtra por ruta de archivo**, a diferencia de los
checks de bins de las Semanas 04 y 05. Ni un título guardado ni un compound clip tienen archivo en
disco, igual que una timeline.

### Lo que no se puede verificar por API, y dónde se evalúa

| No verificable | Dónde se evalúa |
| -------------- | --------------- |
| Si un rótulo se lee sobre su fondo | Rúbrica, criterio observable |
| Si está dentro del título seguro | Rúbrica, criterio observable |
| Qué generador se usó y por qué | Notas escritas + rúbrica |
| Si una transición dice algo o solo decora | Rúbrica, criterio observable |
| Qué efecto lleva el adjustment clip y a qué afecta | Notas escritas + rúbrica |
| Si el compound clip tiene motivo | Notas escritas + rúbrica |

---

## 📝 El entregable escrito

### `notas-de-montaje.md`, apartado `## Títulos y efectos — Semana 11`

En `BC-Resolve/04-respaldos/`, en el mismo archivo de las Semanas 06 a 10.

Se abre en la práctica 01 y se cierra en la práctica 04. Al final tiene que llevar cuatro bloques:

> **El mapa de rótulos**: cuántos marcadores amarillos y qué dice cada uno; cuántos verdes y qué
> resuelve cada uno; qué guías dejaste encendidas.
>
> **Los rótulos**: qué generador elegiste para el título de entrada **y por qué**, con qué fuente y
> qué cuerpo, cómo resolviste el contraste, y si probaste un `Fusion Title` y si se queda.
>
> **Las transiciones y los efectos**: cuáles pusiste, de qué tipo y con qué alineación; si alguna
> necesitó `Trim Clips` y cuánto acortó los planos; qué efecto lleva el adjustment clip, a qué
> afecta y si eso era lo que querías; y **las transiciones que decidiste no poner, con su motivo**.
>
> **El compuesto y la comparación**: qué bloque empaquetaste y por qué; y qué se entiende de la
> pieza ahora que antes no se entendía, con planos y minutos concretos.

Los dos que más valen son el tercero y el cuarto. El de las transiciones **por el apartado de las
que no pusiste**: saber decir que no es la mitad de esta semana. Y el de la comparación porque es
el que comprueba si los rótulos han hecho su trabajo, que era que la pieza se entendiera.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| Todos los rótulos dentro del rectángulo `Title` | Se encienden las guías y se reproduce |
| Ningún rótulo se pierde sobre su fondo en ningún fotograma | Se reproduce el tramo entero de cada uno, no se mira parado |
| Todos los rótulos comparten estilo | Se ven seguidos: la misma fuente, el mismo cuerpo, la misma posición |
| Ningún rótulo llega tarde ni se va pronto | Se lee en voz alta dos veces mientras está en pantalla |
| El título de entrada se lee en un móvil | Se reduce el visor a un cuarto y se lee |
| Ninguna falta de ortografía | Se reproduce mirando solo el texto |
| Cada transición dice algo que el corte no dice | Se ve la pieza entera: ninguna llama la atención sobre sí misma |
| Ninguna transición emborrona un instante que estaba atado a un golpe | Se mira ese punto: si el corte iba con la música, la alineación es `End on Edit` |
| El `Smooth Cut`, si lo hay, no deja ver la deformación | Se reproduce a velocidad normal |
| El efecto del adjustment clip está dosificado, no al máximo | Se apaga y se enciende con `D` |
| El adjustment clip afecta a lo que tiene que afectar | Se mira si toca o no los rótulos, y era la intención |
| El compound clip tiene un motivo escrito | Se lee la nota |
| Los rótulos no tapan lo que importa de la imagen | Se reproduce mirando la imagen, no el texto |
| No hay parpadeos a negro | Se reproduce entera |
| Nada de lo que todavía no toca | Ni etalonaje, ni mezcla, ni multicámara, ni subtítulos |

El último tiene una tentación concreta esta semana: **etalonar con un adjustment clip**. Se puede
hacer, y es de hecho la técnica de la Semana 21, pero aquí no toca y descuadra la evaluación de la
Fase 5.

---

## 💡 Adaptación a tu pieza

**Documental corto** · Tu semana es de **rótulos de identificación**. Cada persona que habla
necesita el suyo la primera vez que aparece, con nombre y con lo que la hace relevante, y todos
tienen que ser el mismo rótulo con distinto texto. Ahí es donde el estilo guardado en el media pool
te ahorra la tarde. Transiciones, pocas: una disolución donde cambia el bloque temático.

**Videoclip** · Tu semana es de **título de entrada y efectos**. Los rótulos de identificación
apenas existen; lo que sí tienes es un título que va a ser parte del diseño de la pieza, y ahí es
donde `Text+` con `Write On` y animación por carácter se paga solo. Y el adjustment clip es tu
herramienta para tratar un estribillo entero de golpe.

**Cortometraje de ficción** · Tu semana es de **título de entrada, créditos y transiciones**. Los
rótulos dentro de la pieza estorban la ficción; lo que hay es un título al principio, unos créditos
al final —el generador `Scroll`, cuya velocidad la marca la duración del clip— y las disoluciones
que separan las escenas.

**Tutorial o vídeo formativo** · Tu semana es la más cargada de la clase: **rótulos por todas
partes**. Los pasos numerados, los nombres de los controles, las advertencias. Dos avisos: uno,
todos con el mismo estilo, sin excepción; dos, el adjustment clip es lo que te oscurece la zona de
pantalla donde va el texto para que se lea sobre una captura clara.

**Pieza de viaje** · Tu semana es de **rótulos de localización** y **transiciones**. Cada sitio
nuevo pide su nombre, y los cambios de lugar piden disoluciones. Cuidado con las plantillas: es el
formato donde más tienta poner un `Fusion Title` distinto en cada sitio, y donde peor queda.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 11` en verde, diez de diez
2. `BC-Montaje-v5` abierta, **fuera** de cualquier compound clip
3. `BC-Montaje-v4` intacta
4. Tres clips o más en la `V2`, todos dentro del rectángulo `Title`
5. Un adjustment clip en la `V3` con su efecto y su nombre
6. `13-Titulos` con el estilo de rótulo y el compuesto
7. Las transiciones puestas y las descartadas, todas con su motivo escrito
8. `notas-de-montaje.md` con el apartado `## Títulos y efectos — Semana 11` cerrado, con sus cuatro
   bloques
9. Ortografía repasada y `View > Show Spelling Errors on Viewer` apagado
10. Respaldo de la semana: `File > Export Project` →
    `04-respaldos/BC-Bootcamp-Resolve-semana11.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza las prácticas 01 y 02, y de la 03 quédate con el **paso 6**: el
> adjustment clip. Es el concepto que más se usa de aquí en adelante —en color, en Fusion y en
> entrega— y el que peor se aprende leyendo. El compound clip de la práctica 04 se hace otro día en
> quince minutos.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Rotular encima de `BC-Montaje-v4` | Parece más práctico | Se duplica; la comparación necesita las dos |
| Arrastrar el primer título a la `V1` | Es la pista donde estabas trabajando | Pistas preparadas antes de empezar: práctica 01, paso 3 |
| Hacer los rótulos uno a uno | Nadie guarda el primero | Constrúyelo bien y guárdalo en el media pool |
| Rotular con las guías apagadas | No se piensa en encenderlas | `View > Safe Area` antes de escribir |
| Juzgar el contraste en un fotograma | El fondo se mueve | Reproduce el tramo entero de cada rótulo |
| Poner transiciones donde no había marcador verde | Se le coge el gusto | El corte es la opción correcta por defecto |
| Aceptar `Trim Clips` sin mirar | Es la primera opción del diálogo | Te acorta los dos planos: míralo |
| `Smooth Cut` de un segundo | Es la duración de fábrica de cualquier transición | Entre 2 y 6 fotogramas |
| Efecto por clip en cinco planos seguidos | Es lo primero que se ocurre | Adjustment clip |
| Adjustment clip en la pista equivocada | No se piensa a qué afecta | Por encima de lo que quiere afectar, y comprobado |
| Empaquetar medio montaje en compuestos | Ordena mucho, a primera vista | Un compuesto es un solo grado en la Fase 5 |
| Verificar desde dentro de un compuesto | El control de ruta pasa desapercibido | Esquina inferior izquierda: si hay dos nombres, estás dentro |
| Etalonar con el adjustment clip | La tentación es fuerte y funciona | Es la Semana 21 |
| Entregar con los subrayados rojos encendidos | No se sabe que se pueden apagar | `View > Show Spelling Errors on Viewer` |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 10](../../week-10-velocidad_transformaciones_y_estabilizacion/3-proyecto/README.md) | **Proyecto Semana 11** | [Semana 12](../../week-12-multicam_subtitulos_y_gestion_de_timeline/README.md) |

← [Volver a la Semana 11](../README.md)
