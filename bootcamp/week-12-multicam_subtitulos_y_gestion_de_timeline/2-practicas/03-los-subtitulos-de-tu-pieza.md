# Práctica 03 — Los subtítulos de tu pieza

> Al terminar `BC-Montaje-v6` tendrá una pista de subtítulos con nombre de idioma, ocho subtítulos o
> más escritos con criterio, un estilo guardado como preajuste, y el archivo `.srt` exportado y
> comprobado.

**Duración estimada**: 60 min
**Prerrequisitos**: [Práctica 01](01-la-copia-y-el-clip-multicamara.md), [Teoría 04](../1-teoria/04-la-pista-de-subtitulos.md), [Teoría 05](../1-teoria/05-escribir-y-estilar-subtitulos.md), [Teoría 06](../1-teoria/06-los-formatos-de-subtitulo.md)

## Contexto

Esta es la práctica que toca tu pieza. Vuelve a `BC-Montaje-v6`, la que duplicaste en la práctica 01,
y le añade la capa de subtítulos.

El orden de los pasos no es arbitrario: **la pista se crea, se nombra y se estila antes de escribir
nada**. Al revés funciona, pero se escribe leyendo un texto que luego cambia de tamaño.

> [!IMPORTANT]
> Si tu pieza **no tiene voz** —un videoclip instrumental, por ejemplo— haz la práctica igual, pero
> con subtítulos descriptivos: los rótulos de sección, las letras de la canción, la información
> sonora. El check pide ocho subtítulos con su pista nombrada, no una transcripción.

---

## Paso 1: Volver a la pieza

1. Doble clic sobre **`BC-Montaje-v6`** en el media pool
2. Comprueba el control de ruta de la esquina inferior izquierda: **un solo nombre**

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check montaje-v6-activa
```

---

## Paso 2: Crear la pista de subtítulos y nombrarla

**Por qué**: el nombre de la pista **viaja al archivo exportado**. No es una etiqueta interna.

1. Clic derecho **en cualquier cabecera de pista** de la timeline `>` **`Add Subtitle Track`**
2. La pista aparece arriba del todo, llamada `Subtitle 1`
3. **Doble clic sobre su nombre** y escribe el código de idioma de tu pieza: **`es-ES`**, o
   `es-MX`, `en-US`, el que sea
4. Comprueba que su **control de destino** `ST1` está activo

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check subtitulos-pista-con-nombre
```

> [!TIP]
> Los códigos son los de la norma **ISO 639-1** para el idioma —dos letras— y la **ISO 3166-1** para
> el país —dos letras, en mayúsculas—. La [tabla oficial](http://www.loc.gov/standards/iso639-2/php/code_list.php)
> está enlazada desde la Teoría 04.

---

## Paso 3: Fijar los umbrales de calidad

**Por qué**: son los que ponen el CPS en rojo cuando un subtítulo no da tiempo a leerse. Sin ellos,
el aviso no llega.

1. `File > Project Settings > Subtitles`
2. Comprueba los tres valores:

| Umbral | Valor de partida razonable |
| ------ | -------------------------- |
| `Characters Per Line` | **42** |
| `Minimum Caption Duration` | **1 segundo** |
| `Maximum Characters Per Second` | **15** |

3. `Save`

**Verifica**: los valores están puestos. Los vas a ver en acción en el paso 5.

> [!NOTE]
> Estos números son los del rango habitual de las guías de subtitulado para adulto general. No son
> una norma de Resolve: son el punto de partida sensato, y se ajustan si tu pieza pide otra cosa.

---

## Paso 4: El estilo, antes de escribir

**Por qué**: cambiar la fuente de ciento cincuenta subtítulos es un ajuste si el estilo es de la
pista, y ciento cincuenta ediciones si no.

1. Clic en la **cabecera** de la pista de subtítulos
2. `Inspector > Track`
3. En `Style and Position`:
   - `Font` — una sans-serif legible, con un corte medio
   - `Size` — que se lea con el visor reducido a un cuarto
   - `Position Y` — abajo, dentro del **título seguro** de la Semana 11
   - `Alignment` — centrado
4. En **`Stroke`**: un contorno oscuro fino
5. En **`Drop Shadow`**: una sombra negra desplazada, alrededor del 50 %
6. Menú de **tres puntos** de la esquina superior derecha del Inspector `>` **`Save Track as Preset`**
7. Nómbralo `BC-Subtitulos`

**Verifica**: el preajuste aparece en el menú de tres puntos. Enciende `View > Safe Area > Title` y
comprueba que la posición cae dentro.

> [!TIP]
> Contorno **y** sombra, no uno de los dos. Es la misma lección de legibilidad de la Semana 11: el
> fondo se mueve, y un subtítulo se juzga reproduciendo, no en un fotograma.

---

## Paso 5: Escribir los subtítulos

**Por qué**: es el trabajo de verdad de la práctica, y donde se aplica el criterio de la Teoría 05.

Repite este ciclo **ocho veces o más**:

1. Cabezal en el fotograma donde **empieza** la frase
2. `Inspector > Captions` `>` **`Create Caption`** —o **`Add New`** a partir del segundo
3. Escribe el texto
4. Arrastra el borde derecho del clip hasta donde **termina** la frase

Las reglas, mientras escribes:

- **Dos líneas como máximo**
- **Se resume**: fuera las muletillas, las repeticiones y los titubeos
- La línea se corta **antes** de una preposición o una conjunción, nunca separando artículo y
  sustantivo
- Entra con la voz, sale con la voz
- **Ningún subtítulo cruza un corte a otra escena**

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check pista-de-subtitulos
```

El check pide **ocho subtítulos o más** en una pista de subtítulos.

---

## Paso 6: Revisar los rojos

**Por qué**: un subtítulo que se pasa de velocidad no se lee, y el aviso ya está puesto desde el
paso 3.

1. Selecciona la cabecera de la pista y abre `Inspector > Captions`
2. Baja hasta la **lista** de todos los subtítulos
3. Busca los **CPS en rojo**
4. Arregla cada uno por una de estas dos vías:
   - **Acorta el texto** — casi siempre es lo correcto
   - **Alarga el clip** — solo si hay silencio detrás

**Verifica**: no queda ningún CPS en rojo, o los que quedan están anotados con su motivo.

---

## Paso 7: La excepción con `Customize Caption`

**Por qué**: hay que haber usado la puerta de atrás una vez para saber qué cuesta.

1. Elige **un** subtítulo que pida un tratamiento distinto: una palabra en otro idioma, un texto que
   no es diálogo, el nombre de una canción
2. Selecciónalo y marca **`Customize Caption`** en `Inspector > Captions`
3. Cámbiale lo que necesite —`Font Face` a cursiva, por ejemplo
4. **Anótalo en las notas**: ese subtítulo se queda fuera de los cambios de estilo futuros

**Verifica**: ese subtítulo se ve distinto y los demás no han cambiado.

---

## Paso 8: Buscar y reemplazar

**Por qué**: en toda transcripción hay un nombre propio escrito de dos maneras.

1. Icono de **búsqueda** de la esquina superior derecha del Inspector de subtítulos
2. Busca una palabra que aparezca varias veces en tu pieza
3. Comprueba el contador de coincidencias y navega con las flechas
4. Si hay algo que corregir de verdad, marca `Replace` y usa `Replace All`

**Verifica**: sabes usar la herramienta aunque no hayas tenido que corregir nada.

---

## Paso 9: Exportar el `.srt` y leerlo

**Por qué**: el archivo es el entregable real de esta capa, y hay que ver lo que sale.

1. Clic derecho sobre la **cabecera** de la pista de subtítulos `>` **`Export Subtitle`**
2. Guarda en `BC-Resolve/04-respaldos/` como **`BC-Montaje-v6.es-ES.srt`**
3. **Ábrelo con un editor de texto** —el Bloc de notas sirve
4. Comprueba las cuatro partes de cada bloque: número, tiempos con **coma** en los milisegundos,
   texto, y línea en blanco

**Verifica**: el archivo existe, los números van seguidos desde 1, y los tiempos cuadran con lo que
ves en la timeline.

---

## Paso 10: Reimportarlo al bin de intercambio

**Por qué**: cierra el círculo —el `.srt` sale y vuelve— y deja en el media pool uno de los dos
elementos que pide el check del bin.

1. Media pool: crea el bin **`14-Intercambio`** colgando de `Master`, si no existe
2. **Selecciónalo**
3. Clic derecho en el media pool `>` **`Import Subtitle`**, y elige el `.srt` que acabas de exportar
4. Aparece como un clip con su distintivo de subtítulo

**Verifica**: el clip está en `14-Intercambio`. El check `bin-de-intercambio` pide **dos elementos**;
el segundo llega en la práctica 04.

> [!TIP]
> **No lo arrastres a la timeline.** Ya tienes esos subtítulos puestos; el clip está ahí como
> evidencia del viaje de ida y vuelta. Si lo sueltas encima, tendrás dos juegos superpuestos.

---

## Paso 11: Cerrar la práctica

1. `Ctrl+S` / `Cmd+S`
2. Añade a `notas-de-montaje.md`:

```markdown
### Subtítulos — práctica 03
- Nombre de la pista: __ · idioma: __
- Subtítulos escritos: __ · duración media: __ s
- Umbrales: CPL __ · duración mínima __ · CPS máximo __
- CPS en rojo al terminar: __ · qué hice: __
- Subtítulo con Customize Caption: __ · por qué: __
- Archivo exportado: __
```

**Verifica**:

```bash
python scripts/verificar-semana.py 12
```

Ocho de los diez checks deberían pasar ya. Los dos que faltan son de la práctica 04.

---

## ✅ Resultado

- [ ] Pista de subtítulos creada en `BC-Montaje-v6`
- [ ] Renombrada con su código de idioma
- [ ] Umbrales de calidad fijados en `Project Settings > Subtitles`
- [ ] Estilo dado en `Inspector > Track` y guardado como preajuste
- [ ] Ocho subtítulos o más, escritos con criterio
- [ ] Ningún CPS en rojo sin justificar
- [ ] Un subtítulo con `Customize Caption`, anotado
- [ ] `.srt` exportado y leído con un editor de texto
- [ ] `.srt` reimportado al bin `14-Intercambio`
- [ ] `notas-de-montaje.md` con el bloque de la práctica 03

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| No encuentro la pista de subtítulos | La zona de subtítulos está oculta | `Timeline View Options` `>` el botón de subtítulos |
| Escribo y no aparece nada en el visor | La pista está deshabilitada, o es otra la visible | Solo una pista de subtítulos se ve a la vez |
| Los subtítulos caen en la pista equivocada | El control de destino `ST` apunta a otra | Clic en el `ST` de la pista buena |
| No encuentro `Font` en `Captions` | El estilo está en `Track`, no en `Captions` | Selecciona la **cabecera** y abre `Track` |
| Cambio la fuente y algunos no cambian | Tienen `Customize Caption` marcado | Es lo que hace esa casilla; desmárcala si no la querías |
| `subtitulos-pista-con-nombre` falla | La pista sigue llamándose `Subtitle 1` | Doble clic sobre el nombre |
| `pista-de-subtitulos` falla con subtítulos visibles | Los pusiste en otra timeline | Comprueba que la activa es `BC-Montaje-v6` |
| El `.srt` exportado sale vacío | No estaba seleccionada la pista correcta | Exporta desde la cabecera de la pista |
| El `.srt` tiene los tiempos corridos | Tu timeline no empieza en 00:00:00:00 | Es normal: el `.srt` es relativo al inicio del programa |
| `bin-de-intercambio` falla | El bin no existe, o solo tiene un elemento | El segundo elemento llega en la práctica 04 |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · Cortar en multicámara](02-cortar-en-multicamara.md) | **03 · Los subtítulos de tu pieza** | [04 · Intercambio, gestión y cierre](04-intercambio-gestion-y-cierre.md) |

← [Volver a la Semana 12](../README.md)
