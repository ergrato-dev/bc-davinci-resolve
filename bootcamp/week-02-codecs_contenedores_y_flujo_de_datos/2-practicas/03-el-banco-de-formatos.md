# Práctica 03 — El banco de formatos

> Al terminar tendrás cuatro archivos de naturaleza distinta dentro de tu proyecto de
> Resolve, en un bin propio, y habrás leído en la interfaz lo que la teoría de esta
> semana explica. Es también la primera vez que importas algo al proyecto del bootcamp.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 02](02-preparar-y-sellar-el-material.md), [Teoría 01](../1-teoria/01-contenedor-y-codec.md), [Teoría 04](../1-teoria/04-profundidad-de-bits.md), [Teoría 07](../1-teoria/07-audio-digital.md)

## Contexto

Hasta ahora has leído fichas técnicas desde fuera. Resolve tiene su propia lectura de
cada archivo, y no siempre dice lo mismo con las mismas palabras: llama `QuickTime` a un
`.mp4`, no menciona el chroma en ningún sitio y reparte el bit depth de vídeo y el de
audio en dos campos distintos con nombres casi idénticos.

Esta práctica pone los dos mundos uno al lado del otro.

> [!WARNING]
> **Esta es la práctica que bloquea el frame rate de tu proyecto.** El
> `Timeline frame rate` deja de poder cambiarse en cuanto entra el primer clip en el media
> pool. Antes de importar nada, comprueba en el paso 1 que sigue a 24. Si estuviera mal,
> este es literalmente el último momento para arreglarlo.

---

## Paso 1: Comprobar el proyecto antes de tocar nada

**Por qué**: es lo irreversible de la semana y solo cuesta un comando comprobarlo.

Abre Resolve, abre `BC-Bootcamp-Resolve` y lanza el puente desde
`Workspace > Scripts > Utility`. Después:

```bash
python scripts/verificar-semana.py 01
```

**Verifica**: los ocho checks de la Semana 01 en verde. Especialmente `frame-rate`. Si
alguno falla, arréglalo **antes** de seguir: en cuanto importes, el frame rate se congela.

---

## Paso 2: Reunir los cuatro archivos con su nombre exacto

**Por qué**: el verificador busca estos archivos por su nombre, carácter a carácter. Y se
copian en vez de moverse para no invalidar el `MANIFIESTO.sha256` que sellaste en la
práctica anterior.

Crea la carpeta `BC-Resolve/01-material-propio/BC-banco-de-formatos/` y **copia** ahí
cuatro archivos, renombrando las copias así:

| Nombre exacto | Qué debe ser | De dónde sale |
| ------------- | ------------ | ------------- |
| `BC-formato-h264.mp4` | Un vídeo `.mp4` con codec H.264 | Tu móvil, o un clip de Pexels |
| `BC-formato-segundo.mp4` | Un segundo vídeo `.mp4`, de **otra fuente** | El otro clip de `01-basicos/` |
| `BC-formato-audio.wav` | Un audio WAV, PCM, a 48 kHz | `06-audio/efectos/`, ya convertido en la práctica 02 |
| `BC-formato-alpha.png` | Un PNG con canal alfa | `07-graficos/` |

> [!IMPORTANT]
> **Renombra el archivo, no la extensión.** Cambiar `.mkv` por `.mp4` en el nombre no
> convierte nada: el archivo sigue siendo Matroska y Resolve lo seguirá rechazando. Si tu
> vídeo no era `.mp4` de origen, remuxéalo de verdad con `ffmpeg -c copy` (práctica 02,
> paso 3).

Comprueba con MediaInfo que `BC-formato-h264.mp4` lleva de verdad `AVC` / H.264. Si tu
móvil grabó en H.265, usa el clip de Pexels para este y el del móvil para el segundo.

**Verifica**: los cuatro archivos existen, con esos nombres exactos, en esa carpeta.

---

## Paso 3: Crear el bin `BC-Formatos`

**Por qué**: un **bin** es una carpeta dentro del media pool de Resolve. No existe en el
disco: organiza el proyecto, no los archivos. El verificador busca este bin por su nombre.

1. Ve a la página **Media** (`Shift+2`)
2. En la lista de bins, arriba a la izquierda, clic derecho sobre un área vacía
3. Elige **`Add Bin`**
4. Sobre el bin nuevo, clic derecho > **`Rename Bin`**, y escribe exactamente:

```
BC-Formatos
```

5. **Haz clic sobre él** para dejarlo seleccionado. El bin seleccionado es el "bin
   activo", y es donde entra lo que importes

**Verifica**: el bin aparece en la lista con el nombre exacto y está resaltado.

---

## Paso 4: Importar los cuatro archivos

**Por qué**: importar en Resolve **no copia nada**. Añade al proyecto una referencia a un
archivo que sigue viviendo en tu disco. Por eso mover carpetas después deja los clips
*offline*, y por eso decidiste la estructura en la Semana 01.

1. En el navegador **Media Storage** (arriba a la izquierda, encima de la lista de bins),
   navega hasta `BC-Resolve/01-material-propio/BC-banco-de-formatos/`
2. Selecciona los cuatro archivos
3. Clic derecho > **`Add into Media Pool`**

> [!WARNING]
> Si el frame rate de algún clip no coincide con el del proyecto, Resolve puede preguntar
> si quieres **cambiar el frame rate del proyecto** para que encaje. **Di que no.** Tu
> proyecto va a 24 fps por una decisión tomada con criterio en la Semana 01, y ese diálogo
> es la forma más común de perderla sin enterarse.

**Verifica**: los cuatro clips aparecen dentro de `BC-Formatos`, y el vídeo se ve al hacer
doble clic sobre uno.

```bash
python scripts/verificar-semana.py 02 --check banco-completo
```

---

## Paso 5: Leer lo que dice Resolve de cada uno

**Por qué**: es el objetivo de la semana. La teoría explica los conceptos; aquí se ven con
los nombres que usa la interfaz que vas a mirar los próximos nueve meses.

Con un clip seleccionado, abre el panel **Metadata** y anota, para cada uno de los cuatro:

| Campo de Resolve | Qué esperas ver |
| ---------------- | --------------- |
| `Format` | `QuickTime` en los dos `.mp4` |
| `Video Codec` | `H.264 ...` en el primero |
| `Bit Depth` | `8` en material de consumo |
| `Audio Codec` | `AAC` en los vídeos; PCM en el WAV |
| `Sample Rate` | `48000` |
| `Audio Ch` | `2` en estéreo |
| `Type` | `Video + Audio`, `Video` o `Audio` según el archivo |
| `Alpha mode` | Algo distinto de `None` en el PNG con transparencia |
| `Data Level` | `Auto` |
| `Input Color Space` / `Input Gamma` | `Rec.709` en material de consumo |

Añade estas filas a tu `ficha-tecnica-material.md`, en una tabla nueva titulada
**"Lo que dice Resolve"**, y **compárala con lo que decía MediaInfo**.

> [!NOTE]
> Que un `.mp4` aparezca como `Format: QuickTime` no es un error. MP4 y MOV descienden del
> mismo estándar, y Resolve reconoce la familia del contenedor, no la extensión. Está
> explicado en la [teoría 01](../1-teoria/01-contenedor-y-codec.md).

**Verifica**:

```bash
python scripts/verificar-semana.py 02 --check contenedor-quicktime
python scripts/verificar-semana.py 02 --check video-h264
```

> [!TIP]
> Si estos dos checks fallan con un mensaje raro, casi siempre es que el bin activo no es
> `BC-Formatos`. El puente lee las propiedades de los clips del bin seleccionado. Haz clic
> sobre `BC-Formatos` y repite.

---

## Paso 6: Comprobar que el frame rate resistió

**Por qué**: acabas de importar, que es justo lo que congela el ajuste. Toca comprobar dos
cosas a la vez: que sigue a 24, y que ahora ya no se puede cambiar.

1. Abre `File > Project Settings` (`Shift+9`), pestaña **Master Settings**
2. Mira el campo `Timeline frame rate`: debe decir **24** y aparecer **atenuado**

Eso atenuado es la prueba visual de lo que llevas dos semanas leyendo.

**Verifica**:

```bash
python scripts/verificar-semana.py 02
```

Los seis checks de la semana en verde.

---

## Paso 7: Guardar y respaldar

`File > Save Project` (`Ctrl+S` / `Cmd+S`), y después:

`File > Export Project` → `BC-Resolve/04-respaldos/BC-Bootcamp-Resolve-semana02.drp`

**Verifica**: el archivo existe y pesa más de 0 bytes.

---

## ✅ Resultado

- [ ] Los ocho checks de la Semana 01 seguían en verde antes de importar
- [ ] Los cuatro archivos copiados y renombrados con el nombre exacto
- [ ] Bin `BC-Formatos` creado y activo
- [ ] Los cuatro clips dentro del bin
- [ ] Tabla "Lo que dice Resolve" añadida a `ficha-tecnica-material.md`
- [ ] `Timeline frame rate` sigue a 24 y ahora aparece atenuado
- [ ] `verificar-semana.py 02` en verde
- [ ] Respaldo `.drp` de la semana en `04-respaldos/`

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El archivo no aparece al importarlo | Es un `.mkv`, o un formato que Resolve no lee | Remuxéalo con `ffmpeg -c copy` (práctica 02) |
| `bin-formatos-activo` falla | El bin seleccionado es otro, o el nombre no coincide | Clic sobre `BC-Formatos`; comprueba mayúsculas y el guion |
| `banco-completo` falla | Falta un archivo o el nombre tiene una errata | Compara carácter a carácter con la tabla del paso 2 |
| `video-h264` falla | El clip es H.265, no H.264 | Usa el otro vídeo, o baja uno de Pexels que sea H.264 |
| `contenedor-quicktime` falla | El archivo no es un `.mp4` real, solo lleva esa extensión | Míralo con MediaInfo: si el `Format` general no es MPEG-4 o QuickTime, remuxéalo |
| `frame-rate-intacto` falla | Dijiste que sí al diálogo de cambio de frame rate al importar | Ya no se puede deshacer: crea el proyecto de nuevo, configúralo e importa después |
| Los clips salen *offline* al día siguiente | Movidos, renombrados o en una carpeta sincronizada con la nube | Devuélvelos a su sitio; el *relink* masivo es Semana 30 |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · Preparar y sellar el material](02-preparar-y-sellar-el-material.md) | **03 · El banco de formatos** | [04 · Medir el flujo de datos](04-medir-el-flujo-de-datos.md) |

← [Volver a la Semana 02](../README.md)
