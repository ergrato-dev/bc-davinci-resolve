# Práctica 03 — Tres puntos y los modos de edición

> Al terminar tu escena tendrá ocho planos o más en `Continuidad`, recursos por encima, ambiente
> por debajo, y habrás usado los cinco modos de edición al menos una vez cada uno sabiendo por
> qué elegías ese y no otro.

**Duración estimada**: 65 min
**Prerrequisitos**: [Práctica 02](02-la-timeline-de-la-escena.md), [Teoría 08](../1-teoria/08-los-modos-de-edicion.md), [Teoría 09](../1-teoria/09-arrastrar-y-el-overlay-del-visor.md)

## Contexto

Los tres planos de la práctica anterior salieron todos con `Overwrite`. Eso es normal: es el
modo que se usa el 80 % del tiempo. Esta práctica es el otro 20 %, que es donde la Edit page se
gana el sueldo.

Cada paso monta algo **y** te obliga a decir por qué ese modo. Escríbelo: la rúbrica de la
semana pregunta por ello, y escribirlo es lo que convierte «probé botones» en «tomé decisiones».

---

## Paso 1: Completar la escena con `Overwrite`

**Por qué**: primero se llega al final, igual que en la Semana 06. Lo demás son ajustes sobre
algo que existe.

Sigue montando planos en `Continuidad` hasta que la escena esté entera, de principio a fin. Para
cada uno, el procedimiento de la práctica 02:

1. Doble clic en el clip → Source Viewer
2. `Q`, `Alt+X` (Win) / `Opt+X` (Mac)
3. `I` y `O` en el origen
4. Cabezal al final del último plano — flecha abajo
5. Hábito de los tres segundos
6. `F10`

Mínimo **ocho planos** en `Continuidad`. Si tu escena da para doce, mejor.

**Verifica**:

```bash
python scripts/verificar-semana.py 08 --check escena-v1-clips
```

---

## Paso 2: `Insert` — meter un plano sin comerse nada

**Por qué**: es el segundo modo más usado y el que más cosas mueve. Entenderlo en tu propia
escena vale más que cualquier explicación.

Busca un sitio donde la escena vaya demasiado deprisa: un corte donde falte un plano intermedio.

1. Carga el plano que falta en el Source Viewer, marca `I` y `O`
2. Pon el cabezal **en el corte** donde tiene que entrar
3. Comprueba el destino
4. **`F9`** — `Insert`
5. **Mira la duración total de la escena antes y después.** Ha crecido exactamente lo que dura
   el plano nuevo

**Verifica**: la escena es más larga, no se ha perdido ningún plano, y no hay huecos.

Escribe una línea: *«Insert en el corte N porque…»*.

---

## Paso 3: `Replace` — hacer coincidir un fotograma

**Por qué**: es el modo que más gente no usa por no entenderlo, y es el más rápido para
sincronizar algo con algo.

Busca un plano de la escena que puedas sustituir por otra toma del mismo momento, y un fotograma
que tenga que coincidir: un golpe, una palabra, una puerta que se cierra, un gesto.

1. Pon el cabezal de la **timeline** en ese fotograma exacto — usa `Detail Zoom` para afinar
2. Carga la otra toma en el **Source Viewer**
3. Mueve el cabezal **del visor de origen** hasta el mismo momento de la acción
4. **No marques puntos.** `Replace` no los necesita
5. Comprueba el destino
6. **`F11`** — `Replace`

**Verifica**: el plano nuevo ocupa exactamente la misma duración que el que había, la escena
dura lo mismo que antes, y la acción cae donde tenía que caer. Reprodúcelo para comprobarlo.

Escribe una línea: *«Replace en el plano N para que … coincida con …»*.

---

## Paso 4: `Fit to Fill` — llenar un hueco exacto

**Por qué**: es el único modo que retima, y hay que verlo hacerlo una vez para saber cuándo sirve
y cuándo no.

1. Busca o crea un hueco en la escena: un tramo que necesite un plano que no tienes de la
   duración justa
2. En la **timeline**, marca `I` y `O` en los dos extremos del hueco
3. En el **origen**, carga un plano y marca `I` y `O` en un rango **más corto** que el hueco
4. Comprueba el destino
5. **`Shift+F11`** — `Fit to Fill`
6. Selecciona el clip que acaba de entrar y mira el **Inspector**: en `Speed` está el porcentaje
   al que ha quedado

**Verifica**: el hueco está lleno exactamente, sin sobrar ni faltar un fotograma.

> [!WARNING]
> Si el porcentaje ha quedado por debajo del **80 %** con material grabado a 24 fps, la cámara
> lenta se va a ver a tirones. Deshazlo y marca en el origen un rango más parecido a la duración
> del hueco. La Semana 07 explica por qué; la Semana 10 lo arregla bien.

Escribe una línea con el porcentaje al que quedó.

---

## Paso 5: `Place on Top` — los recursos, sin tocar lo de abajo

**Por qué**: es el modo de todo lo que va encima, y el único que crea pistas por su cuenta.

Elige dos o tres momentos de la escena donde un recurso mejore lo que se ve: un detalle de lo
que se está contando, un plano de apoyo, un inserto.

Para cada uno:

1. Pon el cabezal sobre el plano que quieres cubrir, o marca `I` y `O` en la timeline sobre el
   tramo exacto
2. Carga el recurso en el Source Viewer y marca `I` y `O`
3. **`F12`** — `Place on Top`

**Verifica**: el recurso ha caído en `Recursos`, encima; lo de abajo no se ha movido; la escena
dura lo mismo.

> [!NOTE]
> `Place on Top` **no hace caso al destino** que tengas puesto: sube a la primera pista libre por
> encima. Si te crea una pista nueva `Video 3`, es que había algo en `Recursos` en ese tramo.
> Ponle nombre a esa pista también, o mueve el recurso a `Recursos` y borra la pista de más con
> `Delete Empty Tracks`.

---

## Paso 6: El sonido de los recursos, en `Ambiente`

**Por qué**: es el ejercicio de destino más útil de la semana. El sonido de un recurso no puede
ir en `Dialogo`, porque ahí ya está la voz y en la Fase 4 se tratan por separado.

Elige un momento donde el sonido de un recurso aporte —un ambiente, un motor, una multitud— y
llévalo a `Ambiente` **sin su imagen**:

1. Carga el clip en el Source Viewer y marca `I` y `O`
2. En el selector de pistas, **apaga el icono de vídeo del origen**
3. Pon el destino de audio en **`Ambiente`** — `Alt+Ctrl+2` (Win) / `Opt+Cmd+2` (Mac)
4. Cabezal donde tiene que entrar
5. `F10`
6. **Vuelve a encender el icono de vídeo** y devuelve el destino de audio a `Dialogo`

**Verifica**: hay un clip de solo audio en `Ambiente`, no ha entrado ninguna imagen, y `Dialogo`
sigue como estaba.

---

## Paso 7: El overlay, para verlos todos juntos

**Por qué**: mientras no te sepas los atajos, es la forma más rápida de elegir modo, y funciona
de recordatorio de qué existe.

1. Marca los puntos que necesites para una edición más
2. Arrastra el clip desde el media pool **hasta el visor de timeline**
3. Sin soltar, recorre las zonas y mira cómo se resaltan
4. Suelta sobre el modo que quieras

**Verifica**: la edición ha salido con el modo que elegiste. Si te arrepientes a mitad de un
arrastre, saca el ratón del visor antes de soltar.

---

## Paso 8: Repasar la escena entera

**Por qué**: se acaba de montar en trozos, con siete operaciones distintas. Hay que verla
seguida.

1. Cabezal al principio
2. Reprodúcela **entera**, sin parar
3. Anota lo que veas, sin parar la reproducción
4. Arregla solo lo que sea de dos minutos

**Verifica**: la escena cuenta lo que dijiste que contaba en el paso 1 de la práctica 02.

---

## Paso 9: Guardar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 08
```

Ocho de nueve. El que falta, `escena-v1-sin-huecos`, es el paso 2 de la práctica 04.

---

## ✅ Resultado

- [ ] Ocho planos o más en `Continuidad`, de principio a fin de la escena
- [ ] He usado `Insert` al menos una vez, y sé qué se movió
- [ ] He usado `Replace` para hacer coincidir un fotograma concreto
- [ ] He usado `Fit to Fill` y sé a qué porcentaje quedó el plano
- [ ] Dos o tres recursos en `Recursos`, puestos con `Place on Top`
- [ ] Un clip de solo audio en `Ambiente`
- [ ] He hecho al menos una edición con el overlay del visor
- [ ] Tengo escrita una línea de por qué usé cada modo
- [ ] He visto la escena entera, seguida

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Con `Insert` se descolocó un recurso | Es lo que hace `Insert`: empuja | Colócalo otra vez, o usa `Overwrite` |
| `Replace` no hizo nada | El cabezal no cruzaba ningún clip de la pista de destino | Ponlo encima de un plano de `Continuidad` |
| `Replace` cogió el fotograma equivocado | El cabezal del visor de origen no estaba en el momento correcto | Colócalo antes de pulsar `F11` |
| `Fit to Fill` dejó el plano al 40 % | El rango del origen era mucho más corto que el hueco | Deshaz y marca un rango más parecido |
| `Place on Top` creó una pista nueva | Había algo en `Recursos` en ese tramo | Ponle nombre, o mueve el clip y `Delete Empty Tracks` |
| Entró la imagen del recurso en `Ambiente` | El icono de vídeo del origen seguía encendido | Apágalo y repite |
| Se me quedó apagado el vídeo del origen | Es el olvido más común | Enciéndelo en cuanto acabes el bloque |
| Han aparecido huecos | Alguna operación dejó negro entre planos | Práctica 04, paso 2 |
| `escena-v1-clips` falla con ocho planos puestos | Están en `Recursos`, no en `Continuidad` | El check mira la primera pista de vídeo |
| No sé qué modo usé en cada sitio | No lo escribiste | Repásalo ahora, mientras te acuerdas |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · La timeline de la escena](02-la-timeline-de-la-escena.md) | **03 · Tres puntos y los modos de edición** | [04 · Cerrar la escena y verificar](04-cerrar-la-escena-y-verificar.md) |

← [Volver a la Semana 08](../README.md)
