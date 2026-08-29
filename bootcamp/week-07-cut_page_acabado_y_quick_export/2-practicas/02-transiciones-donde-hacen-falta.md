# Práctica 02 — Transiciones donde hacen falta

> Al terminar, tu pieza tendrá entre dos y cinco disolvencias, cada una con un motivo escrito
> al lado, y los saltos de entrevista reparados. Y sabrás cuánta cola tiene tu material, que
> es la información que decide la Semana 09 entera.

**Duración estimada**: 55 min
**Prerrequisitos**: [Práctica 01](01-la-copia-de-trabajo.md), [Teoría 02](../1-teoria/02-las-colas-de-un-plano.md), [Teoría 03](../1-teoria/03-transiciones-y-disolvencias.md), [Teoría 04](../1-teoria/04-smooth-cut.md)

## Contexto

Trabajas contra dos de las cuatro listas del paso 10 de la práctica anterior: **cortes que
piden disolvencia** y **saltos que reparar**. Si esas listas están vacías o son vagas, vuelve
a escribirlas: poner transiciones a ojo es el antipatrón número uno de la semana.

Y una advertencia que ordena toda la práctica: cada transición que pongas queda **anclada a
un corte concreto**. A partir de aquí, mover un corte anterior las descoloca todas.

> [!WARNING]
> Antes de empezar: `File > Export Project` →
> `04-respaldos/BC-Bootcamp-Resolve-semana07-pre.drp`. No porque las transiciones sean
> peligrosas, sino porque el paso 2 experimenta con una operación masiva y conviene tener el
> punto de partida guardado.

---

## Paso 0: Comprobar que sigues en la timeline correcta

**Por qué**: los checks leen la timeline activa, y la práctica anterior te hizo abrir
`BC-Sync-Cut-v1` en el paso 6.

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check montaje-v2-activo
```

Si falla, doble clic en `BC-Montaje-v2`.

---

## Paso 1: Medir cuánta cola tienes

**Por qué**: es la información que decide si puedes poner las transiciones que quieres, y si
la Semana 09 va a ser fácil o imposible. Se averigua en tres minutos.

Elige **tres cortes** repartidos por la pieza: uno del principio, uno del medio y uno del
final. En cada uno:

1. Amplía la vista de detalle sobre el corte
2. **Arrastra el borde derecho del clip de la izquierda** hacia fuera, un poco
3. Mira si se mueve, y cuánto
4. **`Ctrl+Z`** (Win) / **`Cmd+Z`** (Mac) para deshacer
5. Repite con el borde izquierdo del clip de la derecha

**Verifica**: sabes responder a esta pregunta con un número: *«mis cortes tienen del orden de
X fotogramas de cola por lado»*.

| Lo que has medido | Qué significa |
| ----------------- | ------------- |
| Un segundo o más por lado | Perfecto. Cualquier transición cabe |
| Media docena de fotogramas | Justo. Disolvencias de 12 fotogramas, no de 24 |
| No se mueve nada | Sin cola. No hay transiciones ni trimming posible en ese corte |

Anota el resultado en `notas-de-montaje.md`. Si la mayoría de tus cortes no tienen cola, esa
es la lección más importante de la semana y hay que cambiar el hábito al marcar, no arreglar
la pieza.

---

## Paso 2: Ver, una sola vez, por qué las transiciones masivas son mala idea

**Por qué**: es más rápido verlo que creerlo, y el respaldo del paso anterior está hecho
precisamente para esto.

1. **`Timeline Actions > Add Dissolve to All Edits`**
2. Reproduce un minuto cualquiera de la pieza
3. **`Timeline Actions > Clear Transition from All Edits`**
4. Reproduce el mismo minuto

**Verifica**: has visto las dos versiones. Escribe una línea en `notas-de-montaje.md` con lo
que has notado. La respuesta esperada es que la pieza se vuelve blanda y los cortes dejan de
significar nada, pero lo que vale es lo que hayas visto tú.

> [!IMPORTANT]
> Comprueba que el paso 3 dejó la timeline **sin ninguna transición** antes de seguir. Si
> queda alguna suelta, selecciónala y `Delete`.

---

## Paso 3: Poner la primera disolvencia, con motivo

**Por qué**: una transición sin motivo es ruido. El motivo tiene que ser uno de los tres:
paso del tiempo, cambio de sitio, cambio de tema.

Coge el primer corte de tu lista:

1. Coloca el cabezal **cerca de ese corte**
2. Pulsa **`V`**: se selecciona el punto de corte más cercano
3. Pulsa **`Ctrl+T`** (Win) / **`Cmd+T`** (Mac)

Entra un `Cross Dissolve` de un segundo.

**Verifica**: la transición está en el corte que querías, no en el de al lado. Si cayó mal,
`Ctrl+Z` / `Cmd+Z`, acerca más el cabezal y repite.

> [!TIP]
> También puedes usar el botón **`Dissolve`** junto a la media pool, que hace lo mismo. El
> camino de teclado está aquí porque los botones cambian de sitio entre versiones y los
> comandos no. Comprueba tus atajos en `DaVinci Resolve > Keyboard Customization`.

---

## Paso 4: Ajustar duración y alineación

**Por qué**: un segundo es la duración por defecto, no una decisión. Y la alineación decide
de qué clip sale la cola, que es lo que hace que quepa o no quepa.

1. **Clic derecho sobre la transición** en la timeline
2. **`Change Duration`**: pon **12 fotogramas** y reproduce
3. Prueba también **24 fotogramas** y reproduce
4. Quédate con la que se lea mejor para ese corte concreto
5. Prueba las tres alineaciones en **`Alignment Options`**: `Start on Edit`, `Center on
   Edit`, `End on Edit`

**Verifica**: la transición dura lo que tú decidiste, y sabes por qué. Si al pedir 24
fotogramas la transición sale más corta o descentrada, **no hay cola suficiente**: acórtala
o quítala.

---

## Paso 5: El resto de las disolvencias

**Por qué**: repetir el ciclo hasta acabar la lista, y ni una más.

Para cada corte restante de tu lista: cabezal cerca, `V`, `Ctrl+T` / `Cmd+T`, ajustar
duración.

Como referencia, en una pieza de cinco minutos: **entre dos y cinco disolvencias**. Si te
salen doce, vuelve a leer la lista y quita las que no tengan uno de los tres motivos.

**Verifica**: cada transición de tu pieza tiene una línea escrita al lado en
`notas-de-montaje.md` con su motivo.

---

## Paso 6: Reparar el primer salto con Smooth Cut

**Por qué**: es la reparación más rentable de una entrevista, y es la única forma de tapar un
salto sin gastar un plano de recurso.

Coge el primer salto de tu lista —incluidos los que creó `Ripple Delete Silence` en la
práctica anterior— y **míralo antes de tocar nada**:

| Mira esto | Si la respuesta es sí |
| --------- | --------------------- |
| ¿Se mueve el fondo? | No uses `Smooth Cut`: recurso |
| ¿Cambió mucho la postura? | No uses `Smooth Cut`: recurso |
| ¿Plano fijo, fondo quieto, postura parecida? | Adelante |

Si pasa el filtro:

1. Cabezal **en el corte** del salto
2. Pulsa el botón **`Smooth Cut`**
3. **Clic derecho > `Change Duration`** y ponlo en **4 fotogramas**
4. Reproduce desde unos segundos antes hasta unos segundos después, **a velocidad normal**,
   dos o tres veces

**Verifica**: no ves el salto y no ves la deformación. Si ves deformación, baja a 2
fotogramas. Si sigue, `Delete` y tapa el salto con un recurso.

> [!NOTE]
> Un `Smooth Cut` **siempre** se ve mal parado o a cámara lenta. No lo juzgues fotograma a
> fotograma: lo que importa es cómo se ve a velocidad de reproducción.

---

## Paso 7: El resto de los saltos, y el reparto con los recursos

**Por qué**: taparlo todo con recursos deja al espectador sin ver a quien habla; repararlo
todo con `Smooth Cut` acumula pequeños fallos. El oficio está en alternar.

Recorre el resto de tu lista de saltos y decide uno a uno:

- **Plano fijo, fondo quieto** → `Smooth Cut` de 2-6 fotogramas
- **Movimiento o cambio de postura** → plano de recurso en `Video 2`, como en la Semana 06
- **Formato donde el salto es lenguaje** (vlog, calle) → déjalo, y anótalo como decisión

**Verifica**: no queda ningún salto sin decidir. «Sin decidir» y «decidido dejarlo» son cosas
distintas, y solo la segunda vale.

---

## Paso 8: Comprobar que nada se ha roto

**Por qué**: `Smooth Cut` y las disolvencias consumen cola y pueden dejar cortes en un estado
raro si el material iba justo.

1. Reproduce la pieza entera, una vez, sin parar
2. Fíjate en tres cosas: parpadeos a negro, transiciones que no querías, saltos que se te
   escaparon

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check montaje-v2-sin-huecos
```

---

## Paso 9: La prueba de quitar

**Por qué**: es la única forma honesta de saber si una transición aportaba algo.

Elige **la disolvencia de la que menos seguro estés**:

1. Selecciónala y pulsa `Delete`
2. Reproduce ese corte tres veces
3. ¿La echas de menos? Vuelve a ponerla. ¿No? Se queda fuera

**Verifica**: has hecho la prueba al menos una vez y has tomado la decisión mirando, no
suponiendo.

---

## Paso 10: Guardar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)
2. Actualiza `notas-de-montaje.md`: cuántas disolvencias, cuántos `Smooth Cut`, cuántos saltos
   tapados con recurso, y cuánta cola tiene tu material

**Verifica**: el apartado `## Acabado — Semana 07` de tus notas tiene ya cifras, no adjetivos.

---

## ✅ Resultado

- [ ] Respaldo previo exportado antes de empezar
- [ ] Sé, con un número, cuánta cola tiene mi material
- [ ] He visto y deshecho el experimento de `Add Dissolve to All Edits`
- [ ] Cada disolvencia tiene uno de los tres motivos escrito al lado
- [ ] Ninguna disolvencia se quedó con la duración por defecto sin decidirla
- [ ] Todos los saltos de la lista están decididos, no solo los reparados
- [ ] Los `Smooth Cut` duran entre 2 y 6 fotogramas
- [ ] Los `Smooth Cut` se han juzgado a velocidad normal
- [ ] `montaje-v2-sin-huecos` en verde
- [ ] He hecho la prueba de quitar al menos una vez

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| La transición cae en el corte de al lado | El cabezal estaba más cerca del otro | `Ctrl+Z` / `Cmd+Z`, acerca el cabezal y repite |
| Pido 24 fotogramas y sale más corta | No hay cola suficiente | Acórtala a 12, o quítala |
| La transición sale descentrada | Solo había cola de un lado | `Alignment Options`, o acórtala |
| El clip no se deja alargar | Ha llegado al media limit del archivo | No hay más material: esa cola no existe |
| El `Smooth Cut` deforma como goma | Dura demasiado | 4 fotogramas, o 2 |
| Aparece un fantasma a medio camino | Las dos posturas son muy distintas | Recurso en `Video 2` |
| El fondo se retuerce | Hay movimiento detrás | Recurso, o prueba el modo `Faster` |
| La pieza suena blanda y sin cortes | Quedaron transiciones del experimento del paso 2 | `Clear Transition from All Edits` y empieza la lista |
| Los recursos ya no coinciden con los saltos | Un ripple posterior en `Video 1` | Recolócalos: la estructura tenía que estar cerrada |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · La copia de trabajo](01-la-copia-de-trabajo.md) | **02 · Transiciones donde hacen falta** | [03 · Velocidad, audio y títulos](03-velocidad-audio-y-titulos.md) |

← [Volver a la Semana 07](../README.md)
