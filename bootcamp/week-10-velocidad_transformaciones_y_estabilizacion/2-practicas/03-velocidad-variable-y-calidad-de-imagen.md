# Práctica 03 — Velocidad variable y calidad de imagen

> Al terminar tendrás una rampa de velocidad construida a mano, afinada en la curva, y habrás
> comparado los tres métodos de relleno sobre tus propios planos. Esta es la práctica donde se
> aprende a **juzgar** un retime, que es más difícil que hacerlo.

**Duración estimada**: 55 min
**Prerrequisitos**: [Práctica 02](02-retimes-lineales-sobre-tu-montaje.md), [Teoría 04](../1-teoria/04-velocidad-variable-rampas-y-rewind.md), [Teoría 05](../1-teoria/05-las-curvas-de-retime.md), [Teoría 06](../1-teoria/06-como-resolve-inventa-fotogramas.md)

## Contexto

Dos avisos antes de empezar, los dos de la teoría:

- **Un clip con velocidad variable se queda mudo.** Si el plano que vas a rampar tiene un sonido
  que importa, sácalo a otra pista antes: `Alt` (Win) / `Opt` (Mac) + clic para desengancharlo.
- **Los `Retime Controls` abiertos se tocan sin querer.** `Esc` en cuanto termines con cada clip.

---

## Paso 1: Elegir el plano de la rampa

**Por qué**: una rampa mal colocada es peor que ninguna. El sitio correcto tiene tres condiciones
y conviene comprobarlas antes de trabajar veinte minutos.

El plano candidato tiene que cumplir las tres:

1. **Hay un instante concreto** que merece leerse despacio: un impacto, un gesto, una mirada
2. **Hay margen antes**: unos segundos de plano a velocidad normal antes de ese instante
3. **El techo lo aguanta**: la velocidad del tramo lento está por encima del techo del plano

Si tu material es todo de 24 fps, tu rampa va a ser al **80 % o al 90 %**, no al 30 %. Sigue
funcionando: una rampa suave se nota igual, y no tiene artefactos.

**Verifica**: has escrito en tus notas qué plano es, qué instante y qué porcentaje.

---

## Paso 2: Construir la rampa a mano

**Por qué**: los presets vienen después. Primero hay que haber puesto los puntos uno a uno para
saber qué está pasando cuando el preset ponga cinco de golpe.

1. Selecciona el clip y **`Ctrl+R`** (Win) / **`Cmd+R`** (Mac)
2. Cabezal donde quieres que **empiece a frenar**. En el desplegable de velocidad —abajo, en el
   centro del clip— elige **`Add Speed Point`**
3. Cabezal donde quieres que **acabe de ir despacio**. **`Add Speed Point`** otra vez
4. Abre el desplegable **del tramo del medio** y elige el porcentaje en **`Change Speed`**
5. **`/`** para verlo en contexto

**Verifica**: la pista de retime enseña tres tramos, con las flechas amarillas y separadas en el
del medio.

> [!TIP]
> Si no encuentras el desplegable del tramo del medio: hay uno por tramo, y cada uno está centrado
> bajo su tramo. Con los tramos muy cortos se solapan; amplía la timeline con `Ctrl+=` / `Cmd+=`.

---

## Paso 3: Probar el asa de arriba y el asa de abajo

**Por qué**: es el punto donde la gente abandona los `Retime Controls`, y se entiende en un minuto
si se prueban las dos a propósito.

1. Arrastra el **asa de arriba** del segundo punto a la derecha. Mira: el tramo del medio va más
   lento y el clip se ha alargado
2. `Ctrl+Z`
3. Arrastra el **asa de abajo** del mismo punto a la derecha. Mira: el tramo del medio ocupa más
   plano, pero **a la misma velocidad**
4. `Ctrl+Z`

**Verifica**: sabes decir con tus palabras qué hace cada asa. Escríbelo.

---

## Paso 4: Afinar la rampa en la curva

**Por qué**: es lo que separa una rampa que se nota de una que funciona. El frenazo de golpe es lo
que delata el efecto.

1. Con el clip seleccionado, abre la pestaña **`Keyframes`**, arriba a la izquierda
2. Pulsa el icono de **curvas** para pasar al `Curve Editor`
3. En la lista de parámetros, marca **`Retime Speed`**
4. Verás tu rampa como una línea que baja y vuelve a subir
5. Selecciona el punto donde **empieza** a frenar y **alarga su asa**: el frenazo se suaviza
6. Reproduce y compara

**Verifica**: la rampa entra y sale sin tirón. Si la quieres seca —para un impacto—, acorta el asa
en vez de alargarla: también es una decisión válida, y es la que hay que saber tomar.

---

## Paso 5: Un preset, para saber qué colocan

**Por qué**: los presets se usan a diario en producción y hay que saber qué hacen antes de
confiar en ellos.

En un plano **distinto** del de la rampa —o en el mismo, deshaciendo después—:

1. `Ctrl+R` / `Cmd+R`
2. Coloca el cabezal dentro del tramo
3. Desplegable de velocidad `> Speed Ramp >` una de las dos opciones
4. Cuenta los tramos: son **cinco**, al 10 %, 30 %, 50 %, 70 % y 90 %
5. Arrastra los puntos para ajustar las duraciones
6. Si no te sirve: `Reset to 100%`

Y el otro:

7. `Rewind >` y un porcentaje. Mira los **dos puntos** nuevos y las flechas hacia la izquierda

**Verifica**: sabes qué coloca cada preset sin tener que probarlo otra vez.

> [!WARNING]
> `Speed Ramp` **sustituye** el efecto de velocidad que ya hubiera en el clip. Si lo aplicas sobre
> la rampa del paso 2, tu trabajo desaparece. Por eso este paso va en otro plano.

---

## Paso 6: La comparación de los tres métodos

**Por qué**: es el ejercicio que enseña a ver. Sin haberlo hecho una vez, todos los retimes
parecen iguales hasta que uno sale mal en la entrega.

Elige **el plano más ralentizado** de toda tu pieza:

1. Selecciona el clip
2. `Inspector > Video > Retime and Scaling > Retime Process`
3. Reproduce en bucle: **`Ctrl+/`** / **`Cmd+/`** y **`/`**
4. Sin parar la reproducción, ve cambiando el desplegable:

| Ponlo en | Mira |
| -------- | ---- |
| `Nearest` | ¿Se ve avanzar a tirones? Eso es *judder* |
| `Frame Blend` | ¿Hay doble imagen en lo que se mueve? Eso es *ghosting* |
| `Optical Flow` | ¿Se derriten los bordes? Eso es *warping* |

5. Amplía el visor: los artefactos no se ven en un visor pequeño
6. Deja el que mejor se vea **en ese plano**

**Verifica**: escribe en tus notas cuál has elegido y **por qué**, describiendo el artefacto que
te hizo descartar los otros dos.

---

## Paso 7: Bajar a `Frame Blend` lo que lo pida

**Por qué**: el ajuste del proyecto es `Optical Flow` desde la práctica 01, y hay planos donde eso
es la elección equivocada.

Recorre los clips retimados de la pieza y baja a `Frame Blend`, en el Inspector, los que tengan:

- Agua, humo, fuego, hojas, lluvia, partículas
- Dos cosas que se cruzan en direcciones distintas
- Ruido de sensor visible
- Movimiento de cámara brusco e impredecible

**Verifica**: ningún clip retimado tiene bordes derretidos.

---

## Paso 8: Recuperar la reproducción

**Por qué**: con varios `Optical Flow` en la pieza, la reproducción se cae y las decisiones de la
práctica 04 se toman a trompicones.

1. `Playback > Render Cache > Smart`
2. Espera a que la barra de encima de la timeline cambie de color en los tramos retimados
3. Reproduce la pieza entera

**Verifica**: la pieza se reproduce a velocidad real de principio a fin.

---

## Paso 9: Cerrar los controles y guardar

1. Recorre los clips con distintivo de retime y comprueba que **ninguno tiene los
   `Retime Controls` abiertos**. Si alguno los tiene: selecciónalo y `Esc`
2. En `notas-de-montaje.md`:

```markdown
### Velocidad variable — práctica 03
- Plano de la rampa: __ · instante que subraya: __ · velocidad del tramo lento: __
- Qué hace el asa de arriba: __ · qué hace el asa de abajo: __
- La rampa quedó: (suave / seca) porque __
- Comparación de métodos en el plano __ :
  - Nearest: __
  - Frame Blend: __
  - Optical Flow: __
  - Elegido: __ porque __
- Clips bajados a Frame Blend: __
```

3. `Ctrl+S` / `Cmd+S`

**Verifica**:

```bash
python scripts/verificar-semana.py 10
```

Diez de diez, o nueve si te falta algún retime. `retimes-aplicados` pide **tres clips o más** con
la velocidad cambiada.

---

## ✅ Resultado

- [ ] Una rampa de tres tramos construida a mano
- [ ] Las dos asas probadas y entendidas
- [ ] La rampa afinada en el `Curve Editor` con una decisión escrita
- [ ] `Speed Ramp` y `Rewind` probados, y sabes qué colocan
- [ ] Los tres métodos de relleno comparados sobre un plano tuyo
- [ ] Los clips problemáticos bajados a `Frame Blend`
- [ ] Caché de render activado y la pieza reproduciéndose fluida
- [ ] Ningún clip con los `Retime Controls` abiertos

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| No pasa nada al poner un punto | Uno solo no separa nada | Hacen falta dos como mínimo |
| Arrastro el asa y la velocidad no cambia | Es el asa de abajo | La velocidad es la de arriba |
| Mi rampa ha desaparecido | Aplicaste `Speed Ramp` encima | `Ctrl+Z`; el preset sustituye |
| El audio del plano se ha ido | Es lo que hace la velocidad variable | Duplícalo en otra pista antes de rampar |
| No encuentro el desplegable de un tramo | Los tramos cortos solapan sus desplegables | Amplía la timeline con `Ctrl+=` / `Cmd+=` |
| `Clear Speed Point` borró el que no era | Borra el que está a la izquierda del desplegable que abriste | `Ctrl+Z` y ábrelo desde el desplegable correcto |
| El tramo lento va a tirones | Por debajo del techo del plano | Sube el porcentaje |
| No veo diferencia entre los tres métodos | El visor es pequeño, o el retime es mínimo | Amplía el visor y prueba en el plano más ralentizado |
| La reproducción va a trompicones | `Optical Flow` calcula en tiempo real | `Playback > Render Cache > Smart` |
| Un clip cambia de velocidad solo | Tenía los controles abiertos y lo rozaste | `Esc` en todos al terminar |
| `retimes-aplicados` falla con tres retimes hechos | Un reverse al 100 % no cuenta: no cambia la duración de origen | Ver la nota del check en el README del proyecto |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · Retimes lineales sobre tu montaje](02-retimes-lineales-sobre-tu-montaje.md) | **03 · Velocidad variable y calidad de imagen** | [04 · Transformaciones, keyframes y estabilización](04-transformaciones-keyframes-y-estabilizacion.md) |

← [Volver a la Semana 10](../README.md)
