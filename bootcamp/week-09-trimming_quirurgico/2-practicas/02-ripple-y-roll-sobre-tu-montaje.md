# Práctica 02 — Ripple y roll sobre tu montaje

> Al terminar, tu pieza durará menos que al empezar, no tendrá ni un hueco, y sabrás decir cuántos
> segundos le has quitado y de dónde. Es la práctica donde el montaje deja de ser un borrador.

**Duración estimada**: 60 min
**Prerrequisitos**: [Práctica 01](01-la-copia-y-el-mapa-de-problemas.md), [Teoría 02](../1-teoria/02-el-modo-trim-frente-al-modo-seleccion.md), [Teoría 03](../1-teoria/03-ripple-y-roll.md), [Teoría 05](../1-teoria/05-trimming-con-el-teclado.md), [Teoría 07](../1-teoria/07-sync-lock-y-las-reglas-del-ripple.md)

## Contexto

Vas a atacar tu lista de marcadores en el orden de la práctica 01: primero los amarillos —lo que
sobra— y luego los rojos —lo que hay que afinar—.

La regla de la práctica: **todo se hace con el teclado**. Puedes usar el ratón para colocar el
cabezal, pero el trim en sí es `V`, `U`, `,` y `.`. Al principio es más lento; a la mitad de la
práctica ya no lo es.

---

## Paso 1: Comprobar los `Sync Lock` antes de tocar nada

**Por qué**: vas a hacer ripples sobre una pieza con varias pistas. El `Sync Lock` decide qué se
mueve con qué, y comprobarlo cuesta diez segundos.

1. Mira las cabeceras de las cinco pistas de `BC-Montaje-v3`
2. **Todas deben tener el `Sync Lock` activado** — es el icono que está a la derecha del candado
3. Si alguna lo tiene apagado, enciéndelo

**Verifica**: los cinco iconos están en el mismo estado. Para poner varios de golpe, clic sobre
uno y arrastra hacia arriba o hacia abajo por las demás cabeceras.

> [!NOTE]
> Tu pieza todavía no tiene música ni rótulos colocados al fotograma, así que el estado correcto
> hoy es «activado en todas». La teoría 07 explica en qué casos se apaga, y esa decisión llega de
> verdad en la Semana 15.

---

## Paso 2: Los amarillos — quitar lo que sobra

**Por qué**: es el trabajo con mejor relación entre esfuerzo y resultado de toda la semana.
Quitar tres planos que no aportan mejora la pieza más que afinar quince cortes.

Filtra el `Marker Index` por amarillo y ve uno a uno. Para cada uno, decide entre dos cosas:

**A · El plano sobra entero.**

1. Clic sobre el clip para seleccionarlo
2. La tecla `Forward Delete` —`Supr` en Windows, `Fn+Supr` en un Mac sin bloque numérico—: borra
   el clip **y cierra el hueco**
3. Comprueba que no ha quedado hueco donde estaba

> [!WARNING]
> `Supr` a secas —`Delete`/`Backspace`— **borra el clip y deja el hueco**. Es la tecla que produce
> el parpadeo a negro que luego encuentra el verificador y tú no. La que cierra el hueco es
> `Forward Delete`.

**B · El plano dura demasiado, pero se queda.**

1. **`T`** — modo trim
2. Pon el cabezal cerca del corte que quieres mover y **`V`**
3. **`U`** hasta tener seleccionada la mitad que quieres recortar
4. **`,`** y **`.`** para ripplear un fotograma, **`Shift+,`** y **`Shift+.`** para cinco
5. **`/`** para escuchar cómo queda

Repite hasta que no queden amarillos.

**Verifica**: mira la **duración total** de la pieza. Ha bajado. Anota cuánto.

---

## Paso 3: Los rojos — afinar entradas y salidas

**Por qué**: es el trabajo de precisión de la semana, y es lo que separa un montaje que se
entiende de uno que se sigue sin esfuerzo.

Filtra por rojo. Para cada marcador, la pregunta es una:

> **¿La pieza tiene que durar lo mismo después de arreglar esto?**

| Respuesta | Operación | Cómo |
| --------- | --------- | ---- |
| No importa que se acorte | `Ripple` | `T` · `V` · `U` hasta una mitad · `,` y `.` |
| Sí, tiene que durar igual | `Roll` | `V` · `U` hasta el **centro** · `,` y `.` |

Para al menos **cinco** de los marcadores rojos:

1. Colócate en el corte y decide la operación
2. Hazla con el teclado
3. **`/`** después de cada ajuste
4. Cuando esté bien, cambia ese marcador a **azul** en el `Marker Index`, o bórralo

**Verifica**: cinco marcadores rojos menos, y la pieza se reproduce mejor por esos cinco cortes.

---

## Paso 4: Afinar un corte con la reproducción en bucle

**Por qué**: es la técnica más rápida para los cortes en los que no sabes cuántos fotogramas
sobran, y hay que hacerla una vez para entenderla.

Elige un corte que se te resista:

1. Cabezal cerca, **`V`**
2. **`U`** para elegir la mitad; **`Alt+U`** (Win) / **`Opt+U`** (Mac) si quieres tocar solo la
   imagen o solo el sonido
3. **`Ctrl+/`** (Win) / **`Cmd+/`** (Mac) — activa el bucle
4. **`/`** — empieza a reproducir alrededor del corte, y no para
5. **Mientras suena**, `,` y `.`. Si lo haces durante la cola del bucle, la vuelta empieza
   inmediatamente
6. **`Espacio`** o **`K`** para parar cuando esté

**Verifica**: has ajustado el corte sin parar la reproducción ni una vez. Escribe en tus notas
cuántos fotogramas acabaste moviendo.

---

## Paso 5: Que varios planos superpuestos acaben a la vez

**Por qué**: es el uso clásico de `Trim End` y resuelve en dos teclas algo que a mano son cuatro
arrastres.

Busca un sitio de tu pieza donde haya un recurso encima de un plano y quieras que **los dos acaben
en el mismo fotograma**:

1. Pon el cabezal en el fotograma donde tienen que acabar
2. Comprueba los **selectores de pista**: solo las pistas que quieras recortar deben estar
   activadas. `Alt` (Win) / `Opt` (Mac) + clic sobre un selector lo deja en solitario
3. **`A`** para redimensionar sin ripplear, o **`T`** para ripplear
4. **`Shift+]`** — `Trim End`

**Verifica**: los clips que cruzaban el cabezal en las pistas activadas acaban ahí. Los de las
pistas apagadas, no.

> [!WARNING]
> Si se te han recortado clips que no querías, el motivo es siempre el mismo: tenías selectores de
> pista activados de más. `Ctrl+Z` y repite acotando. Recuerda que **seleccionar un clip a mano
> gana sobre todos los selectores**.

---

## Paso 6: Buscar y cerrar los huecos

**Por qué**: un hueco es un parpadeo a negro de dos o tres fotogramas. A la escala normal de la
timeline no se ve, en la reproducción casi tampoco, y en la exportación sí.

1. **`Shift+Z`** para ver la pieza entera, y luego el botón `Detail Zoom` para recorrerla al
   detalle
2. Recorre la pista `Continuidad` de principio a fin
3. Cada hueco que encuentres: clic sobre él para seleccionarlo y **`Forward Delete`**
4. Si prefieres cerrarlo trimando: **`T`** y ripplea el borde del hueco. Al hacerlo aparece el
   visor partido que enseña a la vez el plano y lo que se ve por el hueco

**Verifica**:

```bash
python scripts/verificar-semana.py 09 --check montaje-v3-sin-huecos
```

---

## Paso 7: Comprobar que no has roto nada

**Por qué**: has hecho ripples sobre una pieza con cinco pistas. El sitio donde eso se nota es en
las pistas de encima y de debajo, no en la que estabas mirando.

1. **Reproduce la pieza entera otra vez**, con `P` y auriculares
2. Fíjate específicamente en:
   - ¿Algún recurso ha dejado de tapar lo que tapaba?
   - ¿El sonido de ambiente sigue cayendo donde cae su imagen?
   - ¿Hay algún parpadeo a negro?
3. Marca en 🔴 lo que encuentres, y arréglalo

**Verifica**: la pieza se reproduce entera sin nada que te haga parar.

---

## Paso 8: Anotar y guardar

1. En `notas-de-montaje.md`, completa:

```markdown
- Duración de BC-Montaje-v3 después de la práctica 02: __:__
- Segundos quitados: __
- Planos borrados enteros: __
- Cortes afinados con ripple: __ · con roll: __
```

2. `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 09
```

Ocho de diez. Los que faltan son los split edits, de la práctica 04.

---

## ✅ Resultado

- [ ] Los cinco `Sync Lock` comprobados
- [ ] Todos los marcadores amarillos resueltos
- [ ] Cinco marcadores rojos o más resueltos, con la operación correcta
- [ ] Al menos un corte afinado con la reproducción en bucle
- [ ] `Trim End` usado una vez, acotado a las pistas correctas
- [ ] Ni un hueco en `Continuidad`
- [ ] La pieza vista entera después de afinar
- [ ] Las cifras anotadas: duración antes, duración después, segundos quitados

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Al borrar un plano queda un hueco | Usaste `Supr` en vez de `Forward Delete` | `Ctrl+Z` y repite con la tecla correcta |
| `,` y `.` no hacen nada | No hay nada seleccionado | `V` o `Shift+V` primero |
| Recorté el plano que no era | La selección era la otra mitad del corte | `U` rota entre las tres partes; mira cuál está resaltada |
| El corte no se deja mover más | Se acabó la cola de uno de los dos planos | No es un fallo: cambia de operación o de plano |
| Se me ha descolocado un recurso de arriba | Un ripple movió lo de abajo | Comprueba el `Sync Lock` de esa pista y recolócalo |
| La pieza dura lo mismo que al empezar | Hiciste solo `Roll` | Los amarillos se quitan con `Ripple` o borrando |
| `Trim End` recortó cinco clips | Selectores de pista activados de más | `Ctrl+Z`, `Alt` / `Opt` + clic para dejar uno |
| `montaje-v3-sin-huecos` falla y no encuentro el hueco | Es de dos fotogramas | `Detail Zoom` y recorrer, o `Index > Edit Index` buscando saltos de timecode |
| Se me ha ido el audio de sincronía | Trimaste solo el vídeo sin querer | `Alt+U` / `Opt+U` estaba en «solo vídeo»; `Ctrl+Z` |
| Voy lentísimo con el teclado | Es la primera hora | No vuelvas al ratón: a los veinte cortes cambia |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · La copia y el mapa de problemas](01-la-copia-y-el-mapa-de-problemas.md) | **02 · Ripple y roll sobre tu montaje** | [03 · Slip, slide y el dynamic trim](03-slip-slide-y-el-dynamic-trim.md) |

← [Volver a la Semana 09](../README.md)
