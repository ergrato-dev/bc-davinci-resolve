# Proyecto — Semana 08: la escena montada con precisión

> Tu pieza existe y se puede ver. Lo que no sabes todavía es cuánto mejora cuando cada plano
> entra exactamente donde tú decides, con exactamente lo que tú decides que le pase al resto.
> Esta semana lo compruebas sobre una escena, y la comparación con lo que ya tenías es el
> entregable que más enseña.

## 📦 Qué añade esta semana

La octava capa: **una escena montada en la Edit page, con estructura de pistas nombrada y
decisiones escritas**.

Concretamente, tres cosas:

1. **`BC-Escena-v1`**, una timeline nueva con cinco pistas nombradas, donde una escena de tu
   pieza está montada con edición de tres puntos y los cinco modos de edición básicos.
2. **`BC-Montaje-v2` con sus pistas nombradas.** Un trabajo pequeño de hoy que paga en la Fase 4:
   `Dialogo` dice algo, `Audio 1` no.
3. **La comparación escrita** entre la escena montada en Cut y la misma escena montada en Edit.
   Es el dato que decide cuánto trabajo de tu montaje hay que rehacer en las Semanas 09 a 12.

> [!IMPORTANT]
> `BC-Montaje-v2` **no se remonta**. Esta semana no toca su contenido: solo sus nombres de pista.
> La versión siguiente del montaje, `BC-Montaje-v3`, la crea la Semana 09 para hacer trimming.
> Es la convención de versionado de
> [`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md).

Y una cosa que no es un archivo: **el hábito de comprobar el destino antes de editar**. Es lo
único de esta semana que se usa todos los días de aquí a la Semana 36.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca
carácter a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` del proyecto sigue siendo **24**
3. **`BC-Montaje-v2`** sigue existiendo
4. Existe la timeline **`BC-Escena-v1`**
5. **`BC-Escena-v1`** es la timeline abierta
6. Su pista de vídeo principal tiene **ocho clips o más**
7. Esa pista **no tiene huecos ni solapes**
8. Tiene **dos pistas de vídeo y tres de audio** o más
9. **Ninguna pista** conserva su nombre por defecto

```bash
python scripts/verificar-semana.py 08
```

Con el proyecto abierto, **`BC-Escena-v1` como timeline activa** y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!NOTE]
> Los checks 5 a 9 usan `timeline_probe` y `timeline_detect_gaps`, que leen **la timeline
> activa**. Si te quedaste comparando en `BC-Montaje-v2`, fallan los cinco de golpe aunque el
> trabajo esté perfecto. Doble clic en `BC-Escena-v1` y repite.
> *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de 2026.*

El mínimo del check 6 —ocho clips— es el suelo de una escena que se sostenga. Si la tuya tiene
doce, mejor: lo que no vale es una escena de cuatro planos, porque no da para practicar los cinco
modos de edición.

---

## 📝 El entregable escrito

### `notas-de-montaje.md`, apartado `## Edit page — Semana 08`

En `BC-Resolve/04-respaldos/`, en el mismo archivo de las Semanas 06 y 07.

Se abre en la práctica 03 anotando cada decisión de modo, y se cierra en la práctica 04 con cinco
puntos:

> **Qué escena monté**: cuál es, cuánto dura, cuántos planos tiene.
>
> **Qué modo usé y por qué**: una línea por cada uso de `Insert`, `Replace`, `Fit to Fill` y
> `Place on Top`, con el corte concreto.
>
> **A qué velocidad quedó el `Fit to Fill`**: el porcentaje exacto que enseña el Inspector.
>
> **La comparación**: las cuatro respuestas del paso 4 de la práctica 04.
>
> **Qué pasa a la Semana 09**: los cortes de tu montaje que hay que afinar al fotograma, con el
> minuto aproximado de cada uno.

Los dos que más valen son el cuarto y el quinto. El de la comparación porque solo se puede
escribir hoy, con las dos versiones frescas; el de la Semana 09 porque es literalmente la lista
de trabajo de la semana que viene.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| La escena cuenta algo de principio a fin | Se reproduce entera: se entiende sin explicación |
| Cada modo de edición tiene su motivo escrito | Se pregunta por uno: hay una respuesta concreta |
| El `Replace` hizo coincidir algo | Se reproduce el plano: la acción cae donde tenía que caer |
| El `Fit to Fill` no va a tirones | Se reproduce: el movimiento es continuo |
| Los recursos tapan lo que deben | Se desactiva `Recursos`: la escena sigue entendiéndose |
| El sonido de los recursos está en `Ambiente` | Se desactiva `Ambiente`: la voz sigue entera |
| `Dialogo` lleva solo voz | Se escucha en solo |
| Los nombres de pista describen su contenido | Se lee la cabecera y se acierta qué hay dentro |
| No hay parpadeos a negro | Se reproduce entera |
| Ninguna pista quedó apagada o en solo | Se miran las cinco cabeceras |
| Nada de lo que todavía no toca | Ni música, ni títulos diseñados, ni color, ni efectos |

El último sigue siendo el que más gente incumple. Esta semana la tentación concreta es empezar a
afinar cortes al fotograma porque «ya que estoy». Eso es trimming, es la Semana 09, y hacerlo con
las herramientas de esta semana es la forma lenta.

---

## 💡 Adaptación a tu pieza

**Documental corto** · Tu escena es un bloque temático de la entrevista. El modo que más te va a
servir es `Place on Top`: los recursos que tapan los saltos, ahora colocados al fotograma en vez
de a ojo. Y `Ambiente` es donde va el sonido de esos recursos, que hasta ahora se te colaba con
la voz.

**Videoclip** · Elige un tramo con varias tomas del mismo momento y usa `Replace` a fondo: es
exactamente el modo que necesitas para que una acción caiga en un fotograma concreto. Cuando en
la Fase 4 llegue la música, ese fotograma será un golpe.

**Cortometraje de ficción** · Una escena de diálogo con dos ángulos. `Overwrite` para el
esqueleto y `Replace` para cambiar de toma sin mover nada de lo que hay alrededor. El `Insert`
úsalo solo si de verdad falta un plano: en ficción, alargar una escena cambia su ritmo.

**Tutorial o vídeo formativo** · Un procedimiento completo. Aquí `Fit to Fill` es tu modo:
comprimir una espera para que quepa en el hueco que le corresponde es media edición de un
tutorial. Y los insertos de detalle, con `Place on Top`.

**Pieza de viaje** · Una localización entera: llegada, detalles, salida. `Place on Top` para los
detalles y `Ambiente` para el sonido del sitio, que en este formato es la mitad de lo que hace
que se entienda dónde estás.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 08` en verde, nueve de nueve
2. `BC-Escena-v1` con ocho planos o más en `Continuidad`, sin huecos, con las cinco pistas
   nombradas
3. `BC-Montaje-v2` intacta, con sus pistas nombradas
4. `notas-de-montaje.md` con el apartado `## Edit page — Semana 08` cerrado, con sus cinco puntos
5. Puntos de respaldo con nombre en las dos timelines
6. Respaldo de la semana: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana08.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza las prácticas 02 y 03. La comparación del paso 4 de la
> práctica 04 se puede escribir en diez minutos, pero solo mientras te acuerdes de por qué
> elegiste cada modo: si lo dejas para la semana que viene, ya no la vas a escribir.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Montar la escena encima de `BC-Montaje-v2` | Parece más práctico | Se crea una timeline nueva; el montaje no se toca |
| Crear la timeline con otro bin seleccionado | El diálogo no lo pregunta | Selecciona `Master` antes de `File > New Timeline` |
| Desmarcar `Empty Timeline` | Está en el mismo diálogo | Bórrala y créala otra vez |
| Editar sin mirar el destino | Es el hábito que falta | Los tres segundos de la práctica 02 |
| Usar `Overwrite` para todo | Es el que ya conocías | Cada paso de la práctica 03 pide uno distinto |
| Dejar el vídeo del origen apagado | Se olvida después de un audio suelto | Enciéndelo en cuanto acabes el bloque |
| Meter el sonido de los recursos en `Dialogo` | Es la pista donde estaba el destino | `Ambiente`, y el destino se cambia con `Alt+Ctrl+2` |
| Pistas sin nombre | Parece cosmética | Es lo que vas a leer en Fairlight en la Semana 13 |
| Afinar cortes al fotograma | «Ya que estoy» | Es la Semana 09, con otras herramientas |
| Verificar con otra timeline abierta | Es la última que tocaste | Doble clic en `BC-Escena-v1` |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 07](../../week-07-cut_page_acabado_y_quick_export/3-proyecto/README.md) | **Proyecto Semana 08** | [Semana 09](../../week-09-trimming_quirurgico/README.md) |

← [Volver a la Semana 08](../README.md)
