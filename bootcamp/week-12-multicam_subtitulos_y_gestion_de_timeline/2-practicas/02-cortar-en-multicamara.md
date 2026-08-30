# Práctica 02 — Cortar en multicámara

> Al terminar habrás montado una escena entera cambiando de cámara en tiempo real, la habrás
> corregido sin deshacer el ritmo, y sabrás por qué esta forma de montar no se parece a ninguna otra
> del bootcamp.

**Duración estimada**: 60 min
**Prerrequisitos**: [Práctica 01](01-la-copia-y-el-clip-multicamara.md), [Teoría 03](../1-teoria/03-cortar-y-conmutar.md)

## Contexto

`BC-Multicam-01` está sincronizado y con sus ángulos nombrados. Ahora se monta.

Esta práctica **no toca `BC-Montaje-v6`**: trabaja sobre una timeline propia, `BC-Multicam-v1`, igual
que la Semana 08 hizo con `BC-Escena-v1`. El motivo es simple: no toda pieza tiene material
multicámara, y el ejercicio tiene que poder hacerse igual.

---

## Paso 1: La timeline del ejercicio

**Por qué**: una timeline aparte deja tu pieza fuera de peligro y permite equivocarse sin coste.

1. Media pool: **selecciona el bin `09-Escenas`**
2. `File > New Timeline` — `Ctrl+N` (Win) / `Cmd+N` (Mac)
3. En el diálogo `Create New Timeline`, escribe el nombre exacto **`BC-Multicam-v1`**
4. Deja **`Empty Timeline`** marcada, que es su valor de fábrica: el clip lo metes tú en el paso 2
5. `Create`

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check multicam-v1-existe
```

---

## Paso 2: Meter el clip multicámara

**Por qué**: es la fase 2 de las tres. El Multicam Viewer solo funciona sobre un clip multicámara que
está **en una timeline**, no sobre uno del media pool.

1. Media pool, bin `03-Multicamara`
2. Abre `BC-Multicam-01` en el **visor de origen** con doble clic
3. Marca **`I`** donde quieres que empiece la escena y **`O`** donde termine — entre **dos y cuatro
   minutos** es una buena talla para este ejercicio
4. Arrástralo a la `V1` de `BC-Multicam-v1`, o usa `Overwrite` con la tecla `F10`

**Verifica**: el clip está en la timeline y lleva el distintivo de multicámara a la izquierda de su
nombre.

> [!TIP]
> Si te pasas de duración, el ejercicio se hace largo y el aprendizaje es el mismo. Dos minutos de
> material dan para veinte o treinta cambios de cámara, que es de sobra.

---

## Paso 3: Marcar antes de montar

**Por qué**: montar diez minutos a ciegas es montar mal. Y los marcadores de un clip multicámara los
**comparten todos los ángulos**, así que sirven mires el ángulo que mires.

1. Reproduce la escena entera una vez, sin tocar nada
2. Vuelve al principio
3. Reprodúcela otra vez y pulsa **`M`** en cada punto donde pienses «aquí querría ver otra cámara»
4. `Index > Markers` para verlos todos

**Verifica**: tienes entre cinco y quince marcadores repartidos por la escena.

---

## Paso 4: Encender el Multicam Viewer

**Por qué**: es la fase 3, y hay tres ajustes que decidir antes de empezar a cortar.

1. Cabezal al principio del clip
2. Desplegable de modo del **visor de origen** `>` **`Multicam`**
3. Desplegable de la esquina inferior derecha del visor `>` **`2x2`**
4. **`Edit > Multicam > Video Only`** — `Alt+Shift+]` (Win) / `Opt+Shift+]` (Mac)

**Verifica**: el visor de origen enseña los ángulos en rejilla, cada uno con su nombre debajo — los
nombres que pusiste en la práctica 01.

> [!IMPORTANT]
> **`Video Only`** no es un detalle. Con `Video and Audio`, cada cambio de cámara cambia también de
> micrófono, y eso **se oye**: un tropiezo en cada corte. En una entrevista o una charla, el audio
> bueno es uno y no se toca.

---

## Paso 5: Montar

**Por qué**: es la única parte del montaje que se hace a la velocidad de la pieza, y hay que
sentirlo para entenderlo.

1. Cabezal al principio
2. **Reproduce**
3. Con la escena sonando, pulsa **`1`**, **`2`**, **`3`** según qué cámara quieras ver
4. **No pares** a corregir. Los cortes van cayendo en la timeline mientras avanza
5. Deja que llegue al final y para la reproducción

Criterio, mientras montas:

- Se cambia cuando el plano **ya ha dicho lo suyo**, no cada X segundos
- Se cambia **al empezar a hablar**, no a mitad de la frase
- Un plano general para situar; un primer plano para lo que importa
- Si dudas, no cambies

**Verifica**: la timeline tiene una fila de cortes y los clips llevan nombres de ángulo distintos.

---

## Paso 6: Ver lo que ha salido

**Por qué**: la primera pasada siempre tiene tres o cuatro cosas mal, y hay que saber cuáles antes de
tocarlas.

1. Vuelve el visor de origen a modo **`Source`**
2. Reproduce la escena entera
3. Anota, con timecode:
   - Cambios que llegan **tarde**
   - Cambios que llegan **pronto**
   - Cambios al **ángulo equivocado**
   - Cambios que **sobran**

**Verifica**: tienes una lista de tres a ocho arreglos concretos, con su momento.

---

## Paso 7: Arreglar sin deshacer el ritmo

**Por qué**: es la distinción de la semana. Cortar y conmutar son cosas distintas y se arreglan
distinto.

**Ángulo equivocado, corte en el sitio correcto** — solo hay que conmutar:

- Clic derecho sobre el clip `>` **`Switch Multicam Clip Angle`** `>` el ángulo bueno
- O, con el visor en `Multicam` y el cabezal en ese tramo: **`Alt`+clic** sobre el ángulo bueno

**El corte llega tarde o pronto** — es trimming normal, el de la Semana 09:

- Selecciona el punto de edición con **`V`** y arrástralo, o usa `,` y `.`

**El corte sobra**:

- Selecciona el punto de edición con **`V`** y pulsa **`Supr`**
- Los dos tramos se unen y queda el ángulo del primero

**Verifica**: reproduces la escena y no queda nada de la lista del paso 6.

---

## Paso 8: La comparación que cierra el concepto

**Por qué**: montar multicámara a mano es lo que harías sin estas herramientas, y hay que haberlo
tocado una vez para saber lo que te ahorran.

1. Elige **un solo** cambio de cámara de tu escena
2. Cuenta lo que habría costado hacerlo a mano: apilar los dos ángulos en dos pistas, sincronizarlos,
   cortar los dos, borrar el trozo de arriba
3. Multiplícalo por el número de cambios que has hecho

**Verifica**: puedes decir el número. Es el argumento entero de esta práctica.

> [!WARNING]
> **No apliques `Flatten Multicam Clip`.** Aplana el clip y elimina los ángulos no usados, y es
> irreversible en esa timeline. Quedan once semanas de bootcamp y en la Fase 5 puede hacer falta
> volver a otro ángulo.

---

## Paso 9: Cerrar la práctica

1. `Ctrl+S` / `Cmd+S`
2. Añade a `notas-de-montaje.md`:

```markdown
### Multicámara — práctica 02
- Duración de la escena: __ · cambios de cámara: __
- Ángulo que más he usado: __ · por qué: __
- Arreglos que hice después: __ conmutaciones, __ trims, __ cortes borrados
- Lo que habría costado a mano: __ operaciones
- ¿Video Only o Video and Audio? __ · por qué: __
```

3. **Vuelve a abrir `BC-Montaje-v6`** con doble clic en el media pool

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check montaje-v6-activa
```

---

## ✅ Resultado

- [ ] `BC-Multicam-v1` creada en el bin `09-Escenas`
- [ ] El clip multicámara editado dentro, con el distintivo visible
- [ ] Marcadores puestos antes de montar
- [ ] Escena montada con el Multicam Viewer, en `Video Only`
- [ ] Repasada y corregida: conmutaciones, trims y cortes borrados
- [ ] **Sin aplanar**
- [ ] `notas-de-montaje.md` con el bloque de la práctica 02
- [ ] `BC-Montaje-v6` abierta otra vez

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El modo `Multicam` no aparece en el visor | No hay ningún clip multicámara bajo el cabezal | Lleva el cabezal sobre el clip |
| El visor enseña ángulos pero las teclas no hacen nada | El foco está en otro panel | Clic en la timeline y vuelve a intentarlo |
| Cada corte cambia también el sonido | Estás en `Video and Audio` | `Alt+Shift+]` (Win) / `Opt+Shift+]` (Mac) |
| La reproducción va a tirones | Demasiados ángulos descodificando | Baja a `1x2`, o `Playback > Render Cache > Smart` |
| Los ángulos se llaman `Video 1`, `Video 2` | No se renombraron en la práctica 01 | `Open in Timeline` sobre el clip y renómbralos |
| Un `Alt`+clic añadió un corte | Soltaste `Alt` antes de tiempo | `Ctrl+Z`, y mantén la tecla hasta después del clic |
| Quiero deshacer un cambio de cámara | Es un punto de edición como otro | `V` y `Supr` |
| `multicam-v1-existe` falla | El nombre no es exacto | `BC-Multicam-v1`, con guiones y uve minúscula |
| Perdí los ángulos y ya no puedo cambiar | Aplicaste `Flatten Multicam Clip` | `Ctrl+Z` si acabas de hacerlo; si no, restaura el respaldo |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · La copia y el clip multicámara](01-la-copia-y-el-clip-multicamara.md) | **02 · Cortar en multicámara** | [03 · Los subtítulos de tu pieza](03-los-subtitulos-de-tu-pieza.md) |

← [Volver a la Semana 12](../README.md)
