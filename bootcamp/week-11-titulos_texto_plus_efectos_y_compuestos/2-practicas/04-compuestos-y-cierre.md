# Práctica 04 — Compuestos y cierre

> Al terminar habrás empaquetado un bloque de tu pieza en un compound clip, lo habrás abierto,
> editado y cerrado sin perderte, y habrás cerrado la semana con la comparación escrita y el
> respaldo. Y sabrás por qué **no** hay que empaquetar más de lo necesario.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-transiciones-y-resolvefx.md), [Teoría 09](../1-teoria/09-compound-clips-y-nesting.md)

## Contexto

El compound clip es la herramienta que más orden pone en una timeline larga y la que más se usa
mal. Esta práctica hace las dos cosas: uno bien hecho, con su motivo, y la comprobación de por qué
no hay que hacer diez.

Y trae el fallo que más checks tira de toda la semana: **verificar desde dentro de un compuesto**.
El paso 6 está dedicado a eso.

---

## Paso 1: Elegir el bloque

**Por qué**: un compound clip se hace por un motivo concreto, no para ordenar. Un compuesto es **un
solo grado** en la Fase 5, y eso se paga durante once semanas.

Busca en tu pieza **uno** de estos tres casos:

| Caso | Por qué es un compuesto |
| ---- | ----------------------- |
| Un bloque de tres o cuatro planos que tiene que **entrar o salir con una sola transición** | Una transición va entre dos clips; el bloque tiene que ser uno |
| Un **rótulo compuesto** de varias capas que se mueven juntas | Un solo `Transform` para todo |
| Un tramo **terminado** que no vas a volver a tocar | Ordena y no cuesta nada |

Si no tienes ninguno de los tres, usa el primero: tres o cuatro planos seguidos que puedan entrar
con una disolución.

**Verifica**: puedes decir en una frase por qué ese bloque es un compuesto y no un adjustment clip.

> [!IMPORTANT]
> **Tres o cuatro planos como máximo.** El check `montaje-v5-clips` pide quince clips en la `V1`, y
> un compuesto cuenta como **uno**. Si empaquetas medio montaje, el check falla — y con razón:
> habrías perdido el acceso a medio montaje.

---

## Paso 2: Crear el compuesto

**Por qué**: la copia del compuesto cae en el **bin activo**, y por eso hay que elegir el bin
antes, no después.

1. En el media pool, selecciona el bin **`13-Titulos`**
2. En la timeline, selecciona los tres o cuatro clips del bloque
3. Clic derecho sobre uno `>` **`New Compound Clip`**
4. Nómbralo **`BC-Compuesto-<algo>`** — por ejemplo `BC-Compuesto-Recuerdo`
5. `Create`

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check bin-de-titulos
```

Ahora sí: dos elementos en `13-Titulos`, el estilo de rótulo y el compuesto.

> [!TIP]
> Si el compuesto ha caído en `Master` en vez de en `13-Titulos`, no hay que rehacerlo: arrástralo
> de un bin a otro en el media pool.

---

## Paso 3: La transición sobre el bloque entero

**Por qué**: es el motivo por el que existe el compuesto. Comprobarlo cierra el concepto.

1. Selecciona el punto de edición a la entrada del compuesto con **`V`**
2. **`Ctrl+T`** (Win) / **`Cmd+T`** (Mac)
3. Reproduce

**Verifica**: la disolución afecta al bloque entero, no al primer plano de dentro.

---

## Paso 4: Entrar, editar y salir

**Por qué**: hay que haberlo hecho una vez con calma para no perderse la siguiente, y para
reconocer el control de ruta cuando aparezca.

1. Clic derecho sobre el compuesto `>` **`Open in Timeline`**
2. **Mira la esquina inferior izquierda de la timeline**: ahí está el control de ruta, con dos
   nombres. El de la izquierda es `BC-Montaje-v5`; el de la derecha, tu compuesto
3. Haz un cambio pequeño dentro: mueve un corte un par de fotogramas
4. **Doble clic sobre `BC-Montaje-v5`** en el control de ruta
5. Comprueba que el control de ruta ha vuelto a enseñar **un solo nombre**

**Verifica**: estás fuera del compuesto y el cambio de dentro se ve al reproducir.

---

## Paso 5: Comprobar qué se pierde

**Por qué**: la decisión de empaquetar o no se toma sabiendo lo que cuesta, y esto se ve en diez
segundos.

1. Con el compuesto seleccionado en `BC-Montaje-v5`, cambia a la página **Color**
2. Mira la tira de miniaturas de arriba: **el bloque entero es una sola miniatura**
3. Vuelve a la página **Edit**

Eso significa que en la Semana 17 esos tres o cuatro planos son **un solo grado**. Para etalonarlos
por separado habrá que abrir el compuesto con `Open in Timeline` primero, cada vez.

**Verifica**: has visto la miniatura única, y entiendes por qué no hay que empaquetar por
comodidad.

---

## Paso 6: Volver antes de verificar

**Por qué**: este es el fallo que más checks tira de toda la semana, y merece un paso propio.

Siete de los diez checks leen **la timeline activa**. Si te quedas dentro del compuesto, la
timeline activa es el compuesto y fallan los siete de golpe, con el trabajo perfecto.

1. Mira el **control de ruta** de la esquina inferior izquierda
2. Si hay **dos nombres**, estás dentro: doble clic en el de la izquierda
3. Si hay **uno**, estás fuera

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check montaje-v5-activa
```

---

## Paso 7: La comparación con `BC-Montaje-v4`

**Por qué**: es como se aprende a ver la diferencia, y es el entregable escrito de la semana.

1. Abre **`BC-Montaje-v4`** y reprodúcela entera
2. Vuelve a **`BC-Montaje-v5`** y haz lo mismo
3. Contesta en tus notas, con planos concretos:
   - ¿Qué se entiende ahora que antes no se entendía?
   - ¿Hay algún rótulo que sobre? ¿Cuál y por qué?
   - ¿Alguna transición se nota como transición en vez de como decisión?
   - ¿Hay algún sitio donde la v4 fuera mejor?

**Verifica**: la respuesta nombra planos y minutos, no adjetivos.

> [!WARNING]
> **Vuelve a dejar `BC-Montaje-v5` como timeline abierta antes de verificar.** Es el mismo aviso del
> paso 6 por otro camino: siete checks leen la timeline activa, y si te quedas comparando en la v4
> fallan los siete.

---

## Paso 8: Cerrar la semana

1. Cierra el apartado de `notas-de-montaje.md`:

```markdown
### Compuestos y cierre — práctica 04
- Compound clip: nombre __ , __ planos dentro · por qué es un compuesto: __
- ¿Qué transición lleva? __
- Lo que verifiqué en la página Color: __
- Comparación v4 / v5: qué se entiende ahora que antes no: __
- Rótulos que sobran, si alguno: __
- Transiciones que se notan como efecto, si alguna: __
- Qué pasa a la Semana 12: __
```

2. Pasa a **azul** los marcadores amarillos y verdes que hayas resuelto, o bórralos. Los que dejes
   en amarillo o verde son trabajo pendiente
3. `Ctrl+S` / `Cmd+S`
4. `File > Export Project` → `04-respaldos/BC-Bootcamp-Resolve-semana11.drp`

**Verifica**:

```bash
python scripts/verificar-semana.py 11
```

Diez de diez, con `BC-Montaje-v5` abierta y **fuera** del compuesto.

---

## ✅ Resultado

- [ ] Un compound clip de tres o cuatro planos, con nombre `BC-Compuesto-…`
- [ ] Guardado en el bin `13-Titulos`
- [ ] Con la transición que era el motivo de empaquetarlo
- [ ] Abierto, editado y cerrado con el control de ruta
- [ ] Comprobado en la página Color que es un solo grado
- [ ] `BC-Montaje-v4` intacta y comparada con la v5, por escrito
- [ ] `BC-Montaje-v5` como timeline abierta, fuera del compuesto
- [ ] `notas-de-montaje.md` con el apartado `## Títulos y efectos — Semana 11` cerrado
- [ ] Respaldo `BC-Bootcamp-Resolve-semana11.drp` exportado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Fallan siete checks de golpe | Estás dentro del compuesto, o en la v4 | Control de ruta, y doble clic en `BC-Montaje-v5` |
| `montaje-v5-clips` falla después de crear el compuesto | Empaquetaste demasiados planos | `Decompose in Place` y empaqueta menos |
| El compuesto cayó en `Master` | El bin activo no era `13-Titulos` | Arrástralo al bin correcto |
| `bin-de-titulos` sigue fallando | Falta el estilo de rótulo de la práctica 02, o el compuesto | Los dos elementos tienen que estar en `13-Titulos` |
| No encuentro cómo salir del compuesto | El control de ruta es pequeño | Esquina inferior izquierda de la timeline, doble clic en el nombre de la izquierda |
| El compuesto se llevó clips que no quería | La selección incluía más de lo previsto | `Decompose in Place` y vuelve a seleccionar |
| Deshice el compuesto y perdí sus efectos | Estaban en el compuesto, no en los clips | Anótalos antes de deshacer la próxima vez |
| El compuesto se llevó pistas desactivadas | Lo hiciste por rango de `I`/`O`, que se lleva todas | Es su comportamiento; usa `New Compound Clip` por selección |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Transiciones y ResolveFX](03-transiciones-y-resolvefx.md) | **04 · Compuestos y cierre** | — |

← [Volver a la Semana 11](../README.md)
