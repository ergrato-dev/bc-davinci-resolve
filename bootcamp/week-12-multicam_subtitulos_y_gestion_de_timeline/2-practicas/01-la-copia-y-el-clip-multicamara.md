# Práctica 01 — La copia y el clip multicámara

> Al terminar tendrás `BC-Montaje-v6` abierta, los respaldos automáticos encendidos, y un clip
> multicámara sincronizado y con sus ángulos nombrados, comprobado al fotograma antes de montar nada
> encima.

**Duración estimada**: 45 min
**Prerrequisitos**: [Teoría 01](../1-teoria/01-el-clip-multicamara.md), [Teoría 02](../1-teoria/02-sincronizar-los-angulos.md), [Teoría 07](../1-teoria/07-versionar-timelines.md), Semana 11 cerrada

## Contexto

Esta semana tiene dos frentes: tu pieza —que recibe subtítulos— y el multicámara, que es un ejercicio
aparte sobre el material del bin `03-Multicamara`. Esta práctica abre los dos: crea la copia de la
pieza y deja el clip multicámara listo.

El orden importa. El multicámara se comprueba **antes** de montar sobre él, porque un desfase
descubierto después son cuarenta cortes tirados.

---

## Paso 1: La copia de la semana

**Por qué**: `BC-Montaje-v5` es la pieza rotulada de la Semana 11 y es la referencia contra la que se
mide esta. Se duplica, no se sobrescribe: es la convención de
[`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md).

1. Página **Edit**, media pool
2. Clic derecho sobre **`BC-Montaje-v5`** `>` **`Duplicate Timeline`**
3. Aparece `BC-Montaje-v5 copy`
4. Doble clic lento sobre el nombre y escribe **`BC-Montaje-v6`**
5. Doble clic sobre ella para abrirla

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check montaje-v6-activa
```

> [!TIP]
> El nombre es exacto: `BC-Montaje-v6`, con guiones, `M` mayúscula, uve minúscula y el 6 sin ceros
> delante. Cinco de los diez checks de la semana leen esta timeline.

---

## Paso 2: Encender las redes de seguridad

**Por qué**: esta semana se toca `Media Management` y se importan timelines de fuera. Las dos cosas
pueden dejar el proyecto en un estado raro, y la casilla de respaldos automáticos no viene marcada en
todas las instalaciones.

1. `DaVinci Resolve > Preferences > User > Project Save and Load`
2. Marca **`Timeline Backups`** si no lo está
3. Sube **`Daily backups for the past X days`** a `14`, que cubre dos semanas de bootcamp
4. Mira **`Project backup location`** y anota la ruta
5. `Save`

**Verifica**: la ruta que anotaste existe y tiene espacio libre.

---

## Paso 3: El punto de respaldo con nombre

**Por qué**: es el «justo antes de la locura» de la [Teoría 07](../1-teoria/07-versionar-timelines.md),
y esta semana hay dos momentos de locura: la importación de la timeline y la ventana de Media
Management.

1. Con `BC-Montaje-v6` abierta: `File > Create Timeline Backup` —
   `Alt+Ctrl+S` (Win) / `Opt+Cmd+S` (Mac)
2. Nómbralo **`antes-de-la-semana-12`**

**Verifica**: clic derecho sobre `BC-Montaje-v6` `>` `Restore Timeline Backup` enseña ese nombre en
la lista. **No lo restaures ahora**; solo comprueba que está.

---

## Paso 4: Revisar el material multicámara

**Por qué**: los ISOs entraron en la Semana 05. Antes de crear nada hay que confirmar que siguen ahí
y que sirven.

1. Media pool, bin **`03-Multicamara`**
2. Comprueba que hay **tres archivos de vídeo o más**
3. Reproduce cada uno unos segundos y anota:
   - ¿Tienen audio los tres?
   - ¿Se oye la palmada, o algún sonido seco común?
   - ¿Se ve la palmada en los tres encuadres?

**Verifica**:

```bash
python scripts/verificar-semana.py 05 --check bin-multicamara
```

> [!NOTE]
> **Si no tienes material de tres ángulos**, el paso 0 de la
> [Práctica 03 de la Semana 05](../../week-05-proxies_cache_y_sincronizacion/2-practicas/03-sincronizar-y-preparar-multicamara.md)
> explica cómo grabarlo con un móvil en quince minutos. Con **dos** ángulos la práctica funciona
> igual: el Multicam Viewer no exige tres.

---

## Paso 5: Crear el clip multicámara

**Por qué**: es la fase 1 de las tres, y la que decide la sincronía para siempre.

1. En el media pool, **selecciona el bin `03-Multicamara`** — el clip cae en el bin activo
2. Selecciona los ángulos, todos a la vez
3. Clic derecho sobre la selección `>` **`Create Multicam Clip Using Selected Clips`**
4. En el diálogo `New Multicam Clip Properties`:

| Ajuste | Valor |
| ------ | ----- |
| `Multicam Clip Name` | **`BC-Multicam-01`** |
| `Angle Sync` | **`Sound`** — si tus tres ángulos tienen audio común |
| `Angle Name` | **`Clip Name`** |
| `Multicam Audio` | `Source Audio Channels`, el valor por defecto |
| `Move Source Clips to "Original Clips" Bin` | **desmarcada** |

5. `Create`, y espera al análisis de la forma de onda

**Verifica**: en `03-Multicamara` hay un elemento nuevo, `BC-Multicam-01`, con el distintivo de
multicámara en la esquina inferior izquierda de su miniatura. Los ISOs siguen ahí.

> [!IMPORTANT]
> `Move Source Clips to "Original Clips" Bin` va **desmarcada** a propósito: marcarla vacía
> `03-Multicamara` y tira el check `bin-multicamara` de la Semana 05.

---

## Paso 6: Comprobar la sincronía al fotograma

**Por qué**: este es el paso que separa una semana que sale de una que hay que rehacer. Un fotograma
de desfase en una cara hablando se nota.

1. Clic derecho sobre `BC-Multicam-01` en el media pool `>` **`Open in Timeline`**
2. Verás la pila vertical: una pista por ángulo
3. Lleva el cabezal al instante de la palmada —o al sonido seco que hayas elegido
4. Amplía con `Detail Zoom` hasta ver fotogramas sueltos
5. Avanza fotograma a fotograma con **`→`** y comprueba: **el instante en que las manos se juntan
   tiene que caer en el mismo fotograma en todos los ángulos**

**Si un ángulo está corrido**:

1. Selecciona su clip
2. **`.`** lo adelanta un fotograma, **`,`** lo atrasa
3. Vuelve a comprobar

**Si están corridos todos y por cantidades distintas**: el método era el equivocado. Sal, borra
`BC-Multicam-01` y vuelve al paso 5 con `Angle Sync > In`, poniendo `I` a mano en la palmada de cada
ISO.

**Verifica**: la palmada cae en el mismo fotograma en todos los ángulos.

---

## Paso 7: Nombrar los ángulos

**Por qué**: en la práctica 02 vas a cortar pulsando `1`, `2` y `3`. Con los ángulos llamados
`Video 1`, `Video 2` y `Video 3`, cortas por número y te equivocas.

Sigues dentro de `Open in Timeline`.

1. Doble clic sobre el nombre de cada pista
2. Escribe lo que es ese ángulo, no de dónde salió: `Plano medio`, `Primer plano`, `Recurso`
3. Si sobra algún ángulo, clic derecho en su cabecera `>` `Delete Track`
4. Si el orden no te gusta, `Move Track Up` / `Move Track Down`

**Verifica**: las cabeceras llevan nombres que dicen algo.

---

## Paso 8: Salir del clip

**Por qué**: es el fallo que más checks tira, y ya lo viste en la Semana 11 con los compound clips.

1. Mira el **control de ruta** de la esquina inferior izquierda de la timeline
2. Si hay **dos nombres**, estás dentro del clip multicámara
3. **Doble clic sobre el nombre de la izquierda** para volver
4. Comprueba que el control de ruta enseña un solo nombre
5. Si no has vuelto a `BC-Montaje-v6`, ábrela con doble clic en el media pool

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check montaje-v6-activa
```

---

## Paso 9: Abrir las notas de la semana

**Por qué**: los cuatro bloques del entregable escrito se abren aquí y se cierran en la práctica 04.

En `BC-Resolve/04-respaldos/notas-de-montaje.md`, el mismo archivo desde la Semana 06, añade:

```markdown
## Multicámara y subtítulos — Semana 12

### El clip multicámara — práctica 01
- Ángulos: __ · método de sincronía elegido: __ · por qué: __
- ¿Cuadró a la primera? __ · si no, qué hice: __
- Nombres de los ángulos: __
- Respaldos automáticos: daily backups a __ días · ruta: __
```

**Verifica**: el apartado está abierto y los cuatro campos rellenos.

---

## ✅ Resultado

- [ ] `BC-Montaje-v5` intacta
- [ ] `BC-Montaje-v6` creada, abierta y con el nombre exacto
- [ ] `Timeline Backups` encendido y `Daily backups` subido
- [ ] Punto de respaldo `antes-de-la-semana-12` creado
- [ ] `BC-Multicam-01` creado en `03-Multicamara`, con los ISOs todavía ahí
- [ ] Sincronía comprobada al fotograma en un sonido seco
- [ ] Ángulos con nombres que dicen algo
- [ ] Fuera del clip multicámara, con `BC-Montaje-v6` abierta
- [ ] `notas-de-montaje.md` con el bloque de la práctica 01

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `montaje-v6-activa` falla | El nombre no es exacto, o estás dentro del multicámara | Control de ruta; y comprueba el nombre carácter a carácter |
| No aparece `Create Multicam Clip Using Selected Clips` | Solo hay un clip seleccionado | Selecciona dos ángulos o más |
| El clip multicámara cayó en `Master` | El bin activo no era `03-Multicamara` | Arrástralo al bin correcto |
| El análisis de sonido no encuentra la sincronía | Los ángulos no oyeron lo mismo | Rehazlo con `Angle Sync > In` y la palmada |
| Un ángulo está corrido dos fotogramas | El análisis se aproximó | `Open in Timeline`, selecciónalo y ajusta con `.` y `,` |
| Los ISOs desaparecieron de `03-Multicamara` | Marcaste `Move Source Clips to "Original Clips" Bin` | Arrástralos de vuelta desde `Original Clips` |
| `bin-multicamara` de la Semana 05 falla ahora | Lo mismo | Igual |
| Los ángulos siguen llamándose `Video 1`, `Video 2` | Se renombran dentro de `Open in Timeline`, no fuera | Vuelve a entrar y renómbralos |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · La copia y el clip multicámara** | [02 · Cortar en multicámara](02-cortar-en-multicamara.md) |

← [Volver a la Semana 12](../README.md)
