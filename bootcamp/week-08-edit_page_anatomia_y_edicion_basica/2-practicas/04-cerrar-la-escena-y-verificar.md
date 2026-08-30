# Práctica 04 — Cerrar la escena y verificar

> Al terminar `BC-Escena-v1` estará limpia de huecos, tus decisiones estarán escritas, el
> proyecto respaldado y los nueve checks en verde. Y tendrás una comparación que enseña más que
> toda la semana junta: la misma escena montada en Cut y montada en Edit.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-tres-puntos-y-los-modos-de-edicion.md)

## Contexto

Cerrar una semana no es guardar y ya está. Es dejar el trabajo en un estado del que se pueda
partir dentro de siete días sin acordarse de nada, y comprobar que lo que crees que has hecho es
lo que hay de verdad en el proyecto.

---

## Paso 1: La revisión con los ojos

**Por qué**: lo que se arregla ahora cuesta dos minutos; lo mismo descubierto en la Semana 12
cuesta rehacer una escena.

1. Cabezal al principio de `BC-Escena-v1`
2. Reprodúcela entera, con auriculares, sin parar
3. Mira estas cinco cosas:

| Qué mirar | Qué debería pasar |
| --------- | ----------------- |
| Parpadeos a negro | Ninguno |
| Los recursos | Tapan lo que tienen que tapar, y solo eso |
| El plano del `Fit to Fill` | El movimiento es continuo, no escalonado |
| El sonido | Se entiende la voz con el ambiente puesto |
| El final | Acaba donde tenía que acabar, sin negro de sobra |

**Verifica**: tienes una lista escrita de lo que has visto.

---

## Paso 2: Huecos y solapes

**Por qué**: un hueco de dos fotogramas no se ve en la timeline y sale como un parpadeo a negro
en cualquier exportación. Es el fallo más silencioso de la Fase 3.

1. Activa el imán si no está: **`N`**
2. Recorre `Continuidad` en `Detail Zoom`, de principio a fin
3. Donde encuentres un hueco, selecciónalo y bórralo con ripple

> [!NOTE]
> El sitio donde más aparecen los huecos es donde usaste `Fit to Fill`: si el rango del origen
> no llenaba el hueco del todo, puede quedar un fotograma suelto en un extremo.

**Verifica**:

```bash
python scripts/verificar-semana.py 08 --check escena-v1-sin-huecos
```

---

## Paso 3: Comprobar las pistas antes de cerrar

**Por qué**: una pista apagada no se exporta, y a partir de esta semana tus timelines tienen
cinco pistas. Comprobarlo se convierte en parte del procedimiento de cierre.

1. Recorre las cinco cabeceras de `BC-Escena-v1`
2. Comprueba que **ninguna está apagada** y que **ninguna está en solo**
3. Comprueba que ninguna está bloqueada sin motivo
4. Haz lo mismo en `BC-Montaje-v2`

**Verifica**: las cinco cabeceras de la escena y todas las de tu montaje están en su estado
normal.

---

## Paso 4: La comparación que enseña

**Por qué**: es el ejercicio con más valor de la semana y solo se puede hacer hoy, con las dos
versiones recientes en la cabeza.

Abre `BC-Montaje-v2` y busca el tramo equivalente a la escena que has montado. Compara los dos y
contesta por escrito, con una o dos frases cada una:

1. **¿Cuál de las dos versiones cuenta mejor la escena?** No siempre gana la de Edit, y si gana
   la de Cut, el motivo es información valiosa.
2. **¿Qué has podido hacer en la Edit page que no podías hacer en Cut?** Con un ejemplo concreto
   de tu escena, no en general.
3. **¿Cuánto has tardado de más?** Aproximado. Es el precio de la precisión y conviene saberlo.
4. **¿Qué operaciones de tu montaje deberían rehacerse en la Edit page?** Es la lista de trabajo
   de las Semanas 09 a 12.

**Verifica**: las cuatro respuestas mencionan planos y momentos concretos de tu escena.

---

## Paso 5: Las notas de montaje

**Por qué**: la Semana 09 empieza leyendo esto. Lo que no escribas hoy lo vas a redescubrir con
tres semanas de retraso.

En `04-respaldos/notas-de-montaje.md`, el mismo archivo de las Semanas 06 y 07, abre el apartado
**`## Edit page — Semana 08`** con cinco puntos:

> **Qué escena monté**: cuál es, cuánto dura, cuántos planos tiene.
>
> **Qué modo usé y por qué**: una línea por cada uso de `Insert`, `Replace`, `Fit to Fill` y
> `Place on Top`. Las que escribiste en la práctica 03.
>
> **A qué velocidad quedó el `Fit to Fill`**: el porcentaje exacto.
>
> **La comparación**: las cuatro respuestas del paso 4.
>
> **Qué pasa a la Semana 09**: los cortes de tu montaje que hay que afinar al fotograma, con el
> minuto aproximado de cada uno.

**Verifica**: los cinco puntos tienen contenido concreto. El último es el que más vale y el que
más gente deja vacío.

---

## Paso 6: Un punto de respaldo con nombre

**Por qué**: la Semana 09 va a hacer trimming sobre tu montaje, que es la clase de trabajo del
que a veces hay que volver atrás. Dejar hoy un punto marcado, con nombre, cuesta diez segundos.

1. Selecciona **`BC-Montaje-v2`** en el media pool
2. `File > Create Timeline Backup`, atajo `Alt+Ctrl+S` (Win) / `Opt+Cmd+S` (Mac)
3. Ponle un nombre reconocible: `antes-de-la-semana-09`
4. Haz lo mismo con **`BC-Escena-v1`**

> [!NOTE]
> Restaurar un respaldo **no machaca** la timeline actual: la copia entra en el media pool como
> una timeline nueva, con `Backup` añadido al nombre. Por eso es una red segura: puedes comparar
> las dos antes de decidir cuál te quedas.
>
> Para que esto funcione, la casilla `Timeline Backups` tiene que estar marcada en
> `Preferences > User > Project Save and Load`. Compruébalo ahora si nunca lo has mirado.

**Verifica**: clic derecho sobre `BC-Montaje-v2` `> Restore Timeline Backup` enseña tu punto con
el nombre que le pusiste. **No lo restaures**: solo comprueba que está.

---

## Paso 7: El respaldo del proyecto

**Por qué**: la Semana 09 duplica `BC-Montaje-v2` y trabaja sobre la copia. Quieres poder volver
a este punto exacto.

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)
2. **`File > Export Project`** → `04-respaldos/BC-Bootcamp-Resolve-semana08.drp`

**Verifica**: el `.drp` existe, junto a los de las semanas 03 a 07.

---

## Paso 8: Los nueve checks

**Verifica**:

```bash
python scripts/verificar-semana.py 08
```

Nueve de nueve, con **`BC-Escena-v1` como timeline abierta** y el puente lanzado desde
`Workspace > Scripts > Utility`.

Si algo falla antes de eso:

```bash
python scripts/verificar-semana.py --doctor
```

---

## ✅ Resultado

- [ ] He visto la escena entera con auriculares y tengo una lista escrita
- [ ] `Continuidad` no tiene huecos ni solapes
- [ ] Las cinco pistas están encendidas, sin solo y sin bloqueos
- [ ] Las pistas de `BC-Montaje-v2` también
- [ ] Las cuatro preguntas de la comparación están contestadas por escrito
- [ ] `notas-de-montaje.md` con el apartado `## Edit page — Semana 08` cerrado
- [ ] Puntos de respaldo con nombre en las dos timelines
- [ ] `BC-Bootcamp-Resolve-semana08.drp` en `04-respaldos/`
- [ ] Los nueve checks en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `escena-v1-sin-huecos` falla | Hay un hueco o un solape en la primera pista de vídeo | `Detail Zoom` y recorre; suele estar en el `Fit to Fill` |
| `escena-v1-activa` falla | Tienes abierta `BC-Montaje-v2` | Doble clic en `BC-Escena-v1` |
| Fallan `activa`, `clips`, `sin-huecos` y `pistas` a la vez | Los cuatro leen la timeline activa | Abre `BC-Escena-v1` y repite |
| `escena-v1-pistas` falla | Faltan pistas: hacen falta 2 de vídeo y 3 de audio | Clic derecho en una cabecera `> Add Track` |
| `escena-v1-pistas-con-nombre` falla | Alguna pista conserva su nombre por defecto | Repasa las cinco, `Reserva` incluida |
| `montaje-v2-conservada` falla | Renombraste `BC-Montaje-v2` en vez de dejarla | Recupérala del `.drp` de la Semana 07 |
| `frame-rate-bloqueado` falla | El proyecto abierto no es el del bootcamp | Ábrelo desde el Project Manager |
| Fallan todos | El puente no está lanzado | `Workspace > Scripts > Utility > resolve_bridge` |
| El verificador no encuentra el puente | Lo lanzas con el Python de otra máquina | `python scripts/verificar-semana.py --doctor` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Tres puntos y los modos de edición](03-tres-puntos-y-los-modos-de-edicion.md) | **04 · Cerrar la escena y verificar** | [Semana 08](../README.md) |

← [Volver a la Semana 08](../README.md)
