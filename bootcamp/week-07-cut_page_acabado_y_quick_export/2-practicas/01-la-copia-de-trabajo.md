# Práctica 01 — La copia de trabajo

> Al terminar tendrás `BC-Montaje-v2`: una copia del montaje bruto con la escena multicámara
> ya dentro, sin flash frames, sin huecos y con una lista escrita de lo que hay que acabar.
> Es el punto de partida de las otras tres prácticas.

**Duración estimada**: 50 min
**Prerrequisitos**: [Semana 06](../../week-06-cut_page_edicion_veloz/README.md) cerrada, [Teoría 01](../1-teoria/01-que-se-acaba-en-cut.md), [Teoría 08](../1-teoria/08-el-detector-de-aburrimiento.md)

## Contexto

Esta práctica no acaba nada: **prepara**. Hace todo lo que mueve material —incorporar la
escena multicámara, quitar basura, quitar silencios— antes de que en las prácticas 02 y 03
empieces a poner cosas ancladas a un instante.

Ese orden es el que evita repetir trabajo, y es el argumento entero de la
[teoría 01](../1-teoria/01-que-se-acaba-en-cut.md).

> [!WARNING]
> Antes de empezar, comprueba que tienes el respaldo de la semana pasada:
> `04-respaldos/BC-Bootcamp-Resolve-semana06.drp`. Si no está, expórtalo ahora con
> `File > Export Project`. Esta práctica hace operaciones con ripple y borrados, y el
> respaldo es lo que convierte un error en un archivo que ya tenías.

---

## Paso 0: Arrancar el puente y comprobar el punto de partida

**Por qué**: los nueve checks de la semana leen el proyecto abierto a través del puente. Si
no está lanzado, fallan todos y no sabrás si es tu trabajo o el entorno.

1. Abre `BC-Bootcamp-Resolve` desde el Project Manager
2. `Workspace > Scripts > Utility > resolve_bridge`
3. Doble clic en `BC-Montaje-v1` para abrirla

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check proyecto-abierto
```

Si falla aquí, no sigas: revisa el puente antes de tocar la timeline.

---

## Paso 1: Mirar el bruto una vez más, entero

**Por qué**: vas a congelar esta versión para siempre. Conviene saber qué estás congelando,
y es la última ocasión de verlo con los ojos de la semana pasada.

1. Cabezal al principio de `BC-Montaje-v1`
2. **Fast Review** de la pieza entera, sin parar
3. Anota en un papel las tres cosas que más te chirríen

**Verifica**: tienes tres líneas escritas. No hace falta que sean profundas; hace falta que
existan antes de empezar a tocar.

---

## Paso 2: Duplicar, no renombrar

**Por qué**: `BC-Montaje-v1` es la evidencia del montaje bruto y la única forma de comparar
el antes con el después. El acabado va sobre una copia.

1. **Clic derecho sobre `BC-Montaje-v1`** en el media pool
2. **`Duplicate Timeline`**
3. La copia aparece con un nombre automático. **Renómbrala** como `BC-Montaje-v2`
4. **Doble clic** en `BC-Montaje-v2` para abrirla

> [!WARNING]
> Duplicar no es renombrar. Si renombras `v1` como `v2` no tienes dos versiones: tienes una
> con otro nombre, y el montaje bruto de la Semana 06 ha desaparecido. Comprueba que **las
> dos** aparecen en el media pool antes de seguir.

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check montaje-v1-conservada
python scripts/verificar-semana.py 07 --check montaje-v2-existe
python scripts/verificar-semana.py 07 --check montaje-v2-activo
```

Los tres en verde. El nombre es exacto: `BC-Montaje-v2`, con guiones y la uve minúscula.

---

## Paso 3: La pasada de detección, entera y sin arreglar nada

**Por qué**: si arreglas según encuentras, cambias las duraciones mientras el detector
analiza y acabas persiguiéndote la cola. Detectar primero, arreglar después.

1. **`Timeline Options > Boring Detector`**
2. En la ventana `Analyze Timeline Edits`, pon los dos umbrales según tu formato:

   | Tu pieza | `Boring Clips` | `Jump Cuts` |
   | -------- | -------------- | ----------- |
   | Videoclip | 4 s | 2 fotogramas |
   | Tutorial o vlog | 8 s | 2 fotogramas |
   | Documental o entrevista | 12 s | 2 fotogramas |
   | Ficción | 8 s | 2 fotogramas |

3. Pulsa **`Analyze`**
4. **Mira la timeline de arriba** y anota, sin tocar nada:
   - Dónde hay **rojo** (clips demasiado cortos)
   - Dónde hay **gris claro** aislado (un plano largo)
   - Dónde hay **racimos de gris** (un tramo que se hace largo)

**Verifica**: tienes una lista de posiciones. Deja el detector encendido: va a seguir
analizando el resto de la semana.

---

## Paso 4: Los fotogramas duplicados

**Por qué**: un mismo trozo usado dos veces se reconoce aunque el espectador no sepa por
qué, y es la señal de que vas corto de material.

1. Abre el menú **`View`** y busca **`Show Duplicate Frames`**
2. Actívalo y mira si aparecen barras de color sobre algún clip
3. Anota los tramos marcados

> [!NOTE]
> El manual documenta esta opción en el capítulo de la **Edit page**. `View` es un menú
> global, pero si desde la Cut page no la encuentras, pasa a Edit con `Shift+4`, actívala,
> mira lo que marca, y vuelve con `Shift+3`. La timeline es la misma en las dos páginas:
> cambiar de página no exporta ni convierte nada.

**Verifica**: sabes si tu pieza repite material o no. Si repite, apunta cada caso en la lista
del paso 8 con una de las dos etiquetas: *«cambiar uno de los dos»* o *«falta material que
grabar»*.

---

## Paso 5: Quitar los flash frames

**Por qué**: es el arreglo más barato de la semana. Un clip de dos fotogramas es un fogonazo
en pantalla y basura en la timeline: no hay nada que decidir.

Para cada marca **roja de uno o dos fotogramas**:

1. Amplía la vista de detalle sobre ese punto hasta ver el clip
2. Selecciónalo
3. **Bórralo con ripple**, el borrado que cierra el hueco arrastrando el resto hacia la
   izquierda

Las marcas rojas de cinco fotogramas o más **no** son basura automáticamente: reprodúcelas y
decide. Un corte muy rápido puede ser intencionado.

**Verifica**: ya no queda ninguna marca roja de uno o dos fotogramas en la timeline de
arriba. El Boring Detector se actualiza solo.

---

## Paso 6: Traer la escena multicámara

**Por qué**: `BC-Sync-Cut-v1` lleva desde la Semana 06 montada aparte, esperando. Es material
de tu pieza y tiene que estar dentro.

> [!WARNING]
> **Pegar en la Cut page machaca.** El manual lo dice sin rodeos: los clips se pegan en el
> fotograma del cabezal, en la misma pista de la que se copiaron, y **sobrescriben lo que
> haya ahí**. Por eso los pasos siguientes pegan **después del último clip**, donde no hay
> nada que machacar.

1. Doble clic en **`BC-Sync-Cut-v1`** para abrirla
2. Selecciona **todos los clips** de su pista de vídeo
3. **`Ctrl+C`** (Win) / **`Cmd+C`** (Mac)
4. Doble clic en **`BC-Montaje-v2`** para volver
5. Comprueba que el **imán está activado** (`N`)
6. Coloca el cabezal **justo después del último clip** de `Video 1`
7. **`Ctrl+V`** (Win) / **`Cmd+V`** (Mac)

**Verifica**: la escena entra completa al final, `Video 1` es más largo, y **nada de lo que
había antes se ha movido**. Comprueba que los recursos de `Video 2` siguen donde estaban.

---

## Paso 7: Colocar la escena en su sitio

**Por qué**: la escena está dentro, pero al final. Si su sitio es otro, hay que moverla, y en
la Cut page eso se hace desde la timeline de arriba.

- Si el sitio de la escena **es el final**, no toques nada y pasa al paso siguiente.
- Si no lo es: **arrastra el bloque desde la timeline de arriba** hasta su posición. La
  timeline superior está pensada para reordenar a lo largo de toda la pieza sin tocar el
  zoom.

> [!IMPORTANT]
> Mover un bloque hace ripple: todo lo que venía después se recoloca, y **los recursos de
> `Video 2` que estuvieran a la derecha se descolocan**. Es exactamente el aviso de la
> Semana 06, y es el motivo de que esta práctica vaya antes que las otras tres. Si mueves la
> escena, repasa los recursos posteriores antes de seguir.

**Verifica**: la escena está donde tiene que estar, y reproduces un tramo antes y otro
después sin encontrar nada descolocado.

---

## Paso 8: Quitar los silencios largos de la entrevista

**Por qué**: las pausas de tres segundos entre respuestas no aportan nada y se comen el
ritmo. Y es una operación de duración: toca ahora, no después.

Elige un clip de entrevista **que no tenga ningún recurso encima**, para que el ripple no
descoloque nada.

> [!WARNING]
> `Ripple Delete Silence` borra **imagen y sonido a la vez**, acorta la pieza y recoloca todo
> lo que viene detrás. Además crea saltos de montaje donde antes no los había: son
> exactamente los que vas a reparar en la práctica 02. Antes de lanzarla, `Ctrl+S` (Win) /
> `Cmd+S` (Mac).

1. Selecciona el clip
2. **`Clip > Audio Operations > Ripple Delete Silence`**
3. Pon `Minimum to Trip` en **24 fotogramas o más**: así solo se van las pausas largas y el
   ritmo del habla se conserva
4. Deja `Threshold` en su valor por defecto la primera vez
5. Acepta y **escucha el resultado entero**

**Verifica**: las pausas largas han desaparecido y el diálogo **no** suena picado ni
recortado. Si suena picado, `Ctrl+Z` / `Cmd+Z` y sube `Minimum to Trip`.

**Anota** cuántos saltos nuevos ha creado: son trabajo de la práctica 02.

---

## Paso 9: Comprobar que no queda ningún hueco

**Por qué**: entre el borrado de flash frames, el pegado y el ripple de silencios, es donde
aparecen. Un hueco es un parpadeo a negro que a esta escala no se ve.

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check montaje-v2-sin-huecos
python scripts/verificar-semana.py 07 --check montaje-v2-clips
```

El primero lee `Video 1` entera y reporta huecos y solapes. Si falla:

1. Activa el imán con `N`
2. Recorre la pieza en vista de detalle buscando el punto
3. Selecciona el hueco y bórralo con ripple

---

## Paso 10: Escribir la lista de acabado

**Por qué**: las prácticas 02 y 03 trabajan contra esta lista. Sin ella se acaba poniendo
transiciones a ojo, que es el antipatrón número uno de la semana.

Abre `04-respaldos/notas-de-montaje.md` y añade un apartado nuevo, **`## Acabado — Semana
07`**, con cuatro listas:

> **Cortes que piden disolvencia**: dónde y por qué. El «por qué» tiene que ser uno de los
> tres: paso del tiempo, cambio de sitio, cambio de tema.
>
> **Saltos que reparar**: los de la Semana 06 más los que acaba de crear el paso 8.
>
> **Planos que sobran de duración**: los grises del Boring Detector, con la posición.
>
> **Rótulos que hacen falta**: quién habla, dónde estamos, título, créditos.

1. Guarda el archivo
2. `Ctrl+S` (Win) / `Cmd+S` (Mac) en Resolve

**Verifica**: las cuatro listas tienen contenido concreto, con posiciones. «Poner
transiciones» no es una línea válida; «disolvencia en 2:14, cambio de localización» sí.

---

## ✅ Resultado

- [ ] El puente responde y `proyecto-abierto` está en verde
- [ ] `BC-Montaje-v1` sigue existiendo, sin tocar
- [ ] `BC-Montaje-v2` existe y es la timeline abierta
- [ ] El Boring Detector está activado con umbrales elegidos, no los de por defecto
- [ ] La pasada de detección se hizo entera antes de arreglar nada
- [ ] No quedan flash frames de uno o dos fotogramas
- [ ] La escena multicámara está dentro de `BC-Montaje-v2`, en `Video 1`
- [ ] `Ripple Delete Silence` probado y escuchado, sin dejar el diálogo picado
- [ ] `montaje-v2-sin-huecos` y `montaje-v2-clips` en verde
- [ ] `notas-de-montaje.md` con el apartado `## Acabado — Semana 07` y sus cuatro listas

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Fallan todos los checks | El puente no está lanzado | `Workspace > Scripts > Utility > resolve_bridge` |
| `montaje-v1-conservada` falla | Renombraste en vez de duplicar | Recupera `v1` del respaldo `.drp` de la Semana 06 |
| `montaje-v2-activo` falla | Te quedaste en otra timeline | Doble clic en `BC-Montaje-v2` |
| `montaje-v2-clips` falla | La escena multicámara no entró en `Video 1` | Paso 6: comprueba de qué pista copiaste |
| Al pegar desapareció parte del montaje | Pegaste con el cabezal en medio: sobrescribió | `Ctrl+Z` / `Cmd+Z` y pega después del último clip |
| `montaje-v2-sin-huecos` falla | Un borrado sin ripple, o el imán desactivado | `N`, localiza el hueco en vista de detalle y bórralo con ripple |
| El diálogo suena picado | `Minimum to Trip` demasiado bajo | Deshaz y súbelo a 24 fotogramas o más |
| Los recursos de `Video 2` ya no tapan nada | Moviste el bloque multicámara e hiciste ripple | Recolócalos, y hazlo antes de la práctica 03 |
| No encuentro `Show Duplicate Frames` en `View` | La opción está documentada en el capítulo de Edit | `Shift+4`, actívala, mira, y vuelve con `Shift+3` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 07](../README.md) | **01 · La copia de trabajo** | [02 · Transiciones donde hacen falta](02-transiciones-donde-hacen-falta.md) |

← [Volver a la Semana 07](../README.md)
