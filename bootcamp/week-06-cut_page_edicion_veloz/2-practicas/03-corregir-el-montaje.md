# Práctica 03 — Corregir el montaje

> Al terminar, la lista de problemas de la práctica 02 estará resuelta y tu pieza tendrá
> dos pistas de vídeo: la continuidad abajo y los recursos encima. Es el montaje bruto que
> entra en la Semana 07.

**Duración estimada**: 55 min
**Prerrequisitos**: [Práctica 02](02-la-primera-pasada.md), [Teoría 07](../1-teoria/07-corregir-el-montaje-ya-hecho.md), [Teoría 08](../1-teoria/08-editar-sobre-la-pista-de-arriba.md)

## Contexto

Trabajas contra la lista escrita en el paso 7 de la práctica anterior, y en un orden que
no es negociable: **quitar, sustituir, añadir, y solo al final tapar**. Hecho al revés, la
pieza crece sin control y los recursos se descolocan.

> [!WARNING]
> Antes de empezar, exporta un respaldo: `File > Export Project` →
> `04-respaldos/BC-Bootcamp-Resolve-semana06-pre.drp`. Vas a hacer operaciones con ripple,
> que mueven todo lo que hay a la derecha, y tener el punto de partida guardado convierte
> un error de veinte minutos en un archivo que ya tenías.

---

## Paso 1: Releer la lista y ordenarla

**Por qué**: corregir en el orden en que se te ocurrieron las cosas duplica el trabajo.

Coge la lista de la práctica 02 y sepárala en tres grupos:

1. **Sobra**: planos que quitar
2. **No era ese**: planos que sustituir
3. **Falta**: huecos que rellenar

**Verifica**: cada línea de tu lista está en uno de los tres grupos, o marcada para otra
semana.

---

## Paso 2: Quitar lo que sobra

**Por qué**: va primero porque cada plano que quitas cambia el ritmo de su alrededor, y a
veces resuelve el problema de al lado sin que toques nada más.

Para cada plano del grupo 1:

1. Selecciónalo en la timeline
2. Bórralo **con ripple**, el borrado que cierra el hueco arrastrando el resto hacia la
   izquierda
3. Reproduce el corte resultante una vez

**Verifica**: no queda hueco. Amplía la vista de detalle sobre el punto y comprueba que
los dos clips se tocan.

> [!WARNING]
> El borrado normal deja el hueco y, en reproducción, un parpadeo a negro que en la
> timeline no se ve a esta escala. Si dudas de cuál has usado, mira si el material de la
> derecha se ha desplazado: si no se movió, quedó un hueco.

---

## Paso 3: Sustituir lo que no era

**Por qué**: es la corrección más rentable de la semana. Cambiar un plano por otro mejor
cuesta diez segundos y cambia el tramo entero.

Para cada plano del grupo 2:

1. Busca el sustituto en el source tape y márcalo con `I` y `O`
2. Coloca el cabezal sobre el plano que quieres cambiar
3. **Mira el indicador**: tiene que señalar ese corte
4. Pulsa **Ripple Overwrite**

**Verifica**: el plano nuevo está en su sitio, el viejo ha salido del montaje, y no hay
huecos ni solapes.

---

## Paso 4: Añadir lo que falta

**Por qué**: va el último porque hasta ahora no sabías del todo qué faltaba: quitar y
sustituir cambia lo que hace falta.

Para cada hueco del grupo 3:

1. Marca el material nuevo con `I` y `O`
2. Cabezal cerca del corte donde debe entrar
3. **Mira el indicador**
4. Pulsa **Smart Insert**

**Verifica**: el clip entra en el corte y todo lo que venía después se ha desplazado. La
timeline es más larga exactamente lo que mide el clip nuevo.

---

## Paso 5: Comprobar la estructura antes de tapar nada

**Por qué**: a partir del paso siguiente vas a poner cosas en la pista de encima, y
cualquier ripple posterior las descoloca. La estructura se cierra aquí.

1. Reproduce la pieza entera, una vez
2. Comprueba que ya no queda nada de los grupos 1, 2 y 3
3. Anota la nueva duración

**Verifica**: la lista de la práctica 02 está resuelta y no piensas mover más nada de
`Video 1`.

> [!IMPORTANT]
> Si después de este paso necesitas otro ripple, hazlo **antes** de seguir. Un Smart
> Insert con recursos ya colocados encima los deja todos desplazados respecto a lo que
> tapaban, y recolocarlos a mano es el peor rato de la semana.

---

## Paso 6: Tapar el primer salto con un recurso

**Por qué**: es el gesto que arregla el defecto más visible de cualquier pieza con alguien
hablando.

1. Localiza un corte donde la imagen salte: dos trozos del mismo plano pegados
2. Busca un plano de recurso en el media pool y márcalo con `I` y `O`, entre **dos y
   cuatro segundos**
3. Coloca el cabezal **un poco antes** del salto, no justo encima
4. Pulsa **Place on Top**

**Verifica**: aparece la pista `Video 2` con el recurso dentro. Reproduce: la imagen cambia
y **el audio sigue siendo el mismo**. `Video 1` no se ha movido ni un fotograma.

---

## Paso 7: Repetir con el resto de saltos

**Por qué**: una pieza con entrevista tiene varios, y taparlos es lo que la hace ver
montada en vez de recortada.

Repite el paso 6 en cada salto que hayas anotado. Como referencia: entre dos y cinco
recursos en una pieza de cinco minutos.

**Verifica**:

```bash
python scripts/verificar-semana.py 06 --check montaje-pista-superior
```

El check pide **dos pistas de vídeo o más**: es la prueba de que has editado sobre la
pista de encima.

---

## Paso 8: Probar Close Up una vez

**Por qué**: para saber qué hace y en qué se nota, que es la única manera de decidir si lo
quieres en tu pieza.

1. Elige un plano abierto de alguien hablando
2. Márcalo con `I` y `O`
3. Coloca el cabezal donde quieras el primer plano
4. Pulsa **Close Up**
5. Reproduce y mira **la nitidez** del resultado a pantalla completa

**Verifica**: el clip nuevo está en `Video 2`, reencuadrado. Decide con lo que has visto si
se queda o lo borras. Las dos respuestas son válidas; lo que no vale es no mirarlo.

> [!NOTE]
> Un reencuadre no añade detalle: recorta la imagen que ya tenías y la amplía. Cuanto más
> amplía, más blanda queda. El ajuste fino del encuadre es materia de la Semana 10.

---

## Paso 9: La comprobación de la pista de arriba

**Por qué**: es la propiedad que hace de `Video 2` una red de seguridad, y conviene
comprobarla una vez con tus propios ojos.

1. Desactiva la pista `Video 2` desde su cabecera
2. Reproduce un tramo con recursos
3. Vuelve a activarla

**Verifica**: con la pista desactivada ves el montaje exactamente como estaba antes del
paso 6, con el mismo audio y la misma duración.

---

## Paso 10: Revisión final y respaldo

1. Cabezal al principio y **Fast Review** de la pieza entera
2. Anota lo que quede: casi todo debería caer ya en "Semana 09" o más adelante
3. Actualiza `notas-de-montaje.md` con la duración final, el número de clips y lo
   pendiente
4. `Ctrl+S` (Win) / `Cmd+S` (Mac)
5. `File > Export Project` → `04-respaldos/BC-Bootcamp-Resolve-semana06.drp`

**Verifica**:

```bash
python scripts/verificar-semana.py 06
```

---

## ✅ Resultado

- [ ] Respaldo previo exportado antes de empezar a corregir
- [ ] Los tres grupos de la lista resueltos, en orden
- [ ] Ningún hueco: los borrados se hicieron con ripple
- [ ] La estructura de `Video 1` cerrada antes de tapar nada
- [ ] `Video 2` existe, con entre dos y cinco recursos
- [ ] Los recursos empiezan antes del salto y acaban después
- [ ] He probado Close Up y he decidido a la vista del resultado
- [ ] Desactivar `Video 2` devuelve el montaje a como estaba
- [ ] `notas-de-montaje.md` actualizado y respaldo exportado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Queda un parpadeo negro en un corte | Borraste sin ripple | Amplía la vista, selecciona el hueco y bórralo con ripple |
| Ripple Overwrite se llevó el plano de al lado | El indicador señalaba otro corte | `Ctrl+Z` / `Cmd+Z`, recoloca el cabezal y mira el indicador |
| El recurso no tapa el salto | Empieza justo en el corte | Que empiece antes y acabe después |
| Al poner un recurso desaparece el audio | Usaste Ripple Overwrite en vez de Place on Top | Deshaz y usa Place on Top |
| Los recursos se descolocaron de golpe | Hiciste un ripple en `Video 1` después de colocarlos | Recolócalos, y cierra la estructura antes la próxima vez |
| `montaje-pista-superior` falla | No hay ninguna edición en la pista de encima | Paso 6: Place on Top crea `Video 2` |
| El Close Up se ve blando | Es lo que hace un reencuadre | Amplía menos, o descártalo |
| La pieza ha crecido mucho de duración | Añadiste antes de quitar | Repasa el grupo 1: quitar va primero |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · La primera pasada](02-la-primera-pasada.md) | **03 · Corregir el montaje** | [04 · El sync bin](04-el-sync-bin.md) |

← [Volver a la Semana 06](../README.md)
