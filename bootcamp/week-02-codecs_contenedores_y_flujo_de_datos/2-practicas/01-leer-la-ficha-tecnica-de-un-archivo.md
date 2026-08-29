# Práctica 01 — Leer la ficha técnica de un archivo

> Al terminar sabrás decir, de cualquier archivo de vídeo, qué contenedor es, qué codec
> lleva dentro, con cuántos bits y cuánto color guarda. Sin adivinar y sin abrir Resolve.

**Duración estimada**: 45 min
**Prerrequisitos**: [Teoría 01](../1-teoria/01-contenedor-y-codec.md), [Teoría 03](../1-teoria/03-chroma-subsampling.md), [Teoría 04](../1-teoria/04-profundidad-de-bits.md)

## Contexto

Antes de importar nada conviene saber qué se va a importar. Diez segundos de lectura de
ficha técnica evitan la mayoría de las sorpresas: el clip que no entra, el que va a
tirones, el que suena desincronizado.

Esta práctica no toca Resolve. Se hace con **MediaInfo**, que es gratuito, de código
abierto y existe para Windows, macOS y Linux. Es la herramienta que dice lo que Resolve
no dice.

---

## Paso 1: Instalar MediaInfo

**Por qué**: Resolve muestra el contenedor, el codec y el bit depth, pero **no muestra el
chroma subsampling** ni el bitrate. Sin una segunda herramienta te faltan dos datos de
los seis que importan.

Descárgalo de <https://mediaarea.net/MediaInfo>. Elige la versión con interfaz gráfica
(*GUI*), no la de línea de comandos, salvo que prefieras la terminal.

> [!NOTE]
> Al instalarlo en Windows, revisa las casillas del instalador y desmarca cualquier
> software adicional que ofrezca. El programa en sí es limpio; el instalador a veces
> propone extras.

**Verifica**: abres MediaInfo y arrastras cualquier vídeo dentro. Aparece una ficha.

---

## Paso 2: Ponerlo en vista *Tree*

**Por qué**: la vista por defecto resume y esconde justo los campos que necesitas. La
vista de árbol lo muestra todo, agrupado por pista.

En el menú `View`, elige **`Tree`**.

Verás tres bloques:

| Bloque | Qué describe |
| ------ | ------------ |
| **General** | El contenedor: formato, tamaño, duración, bitrate total |
| **Video** | La pista de vídeo: codec, resolución, fps, chroma, bit depth |
| **Audio** | La pista de audio: codec, frecuencia de muestreo, canales, bit depth |

**Verifica**: ves los tres bloques con el archivo cargado.

---

## Paso 3: Leer los seis campos que importan

**Por qué**: una ficha de MediaInfo tiene más de cien campos y la mayoría no sirven para
decidir nada. Estos seis, sí.

Con uno de tus clips cargado, localiza:

| # | Campo en MediaInfo | Bloque | Qué te dice |
| - | ------------------ | ------ | ----------- |
| 1 | `Format` | General | El **contenedor** (`MPEG-4`, `QuickTime`, `Matroska`) |
| 2 | `Format` | Video | El **codec** de vídeo (`AVC` es H.264, `HEVC` es H.265) |
| 3 | `Format settings` o `Format profile` | Video | Si es long-GOP, y con qué perfil |
| 4 | `Chroma subsampling` | Video | `4:2:0`, `4:2:2` o `4:4:4` |
| 5 | `Bit depth` | Video | `8 bits`, `10 bits` |
| 6 | `Sampling rate` | Audio | `48.0 kHz` o `44.1 kHz` |

> [!TIP]
> `AVC` y `H.264` son el mismo codec con dos nombres: *Advanced Video Coding* es el
> nombre del estándar y H.264 el de la recomendación de la UIT. Igual con `HEVC` y H.265.
> Verlos escritos de las dos maneras no significa que sean cosas distintas.

**Verifica**: sabes decir los seis valores de tu clip en voz alta.

---

## Paso 4: Calcular el bitrate a mano

**Por qué**: el bitrate que muestra MediaInfo es el del archivo. Saber calcularlo tú
sirve para estimar cuánto va a ocupar algo que **todavía no existe**, que es la pregunta
útil al planificar disco.

La cuenta, de la [teoría 08](../1-teoria/08-flujo-de-datos.md):

```
bitrate (Mbps) = tamaño en MB × 8 ÷ duración en segundos
```

Hazlo con uno de tus clips y compara con el campo `Overall bit rate` del bloque General
de MediaInfo. Deberían parecerse mucho.

**Verifica**: tu cuenta y la de MediaInfo se diferencian en menos de un 10 %. Si no,
revisa si estás mezclando MB con Mb: la mayúscula es bytes, la minúscula bits.

---

## Paso 5: Hacer la ficha de tres archivos distintos

**Por qué**: un archivo solo no enseña nada; tres comparados enseñan la categoría. Y es
la tabla que vas a entregar esta semana.

Elige tres archivos **distintos entre sí**:

1. Un vídeo grabado con tu móvil o tu cámara
2. Un vídeo descargado del pack de medios (Pexels, Blender, Internet Archive)
3. Un archivo de audio, a poder ser un WAV

Crea `BC-Resolve/04-respaldos/ficha-tecnica-material.md` y rellena esta tabla:

```markdown
| Campo | Archivo 1 | Archivo 2 | Archivo 3 |
| ----- | --------- | --------- | --------- |
| Nombre del archivo | | | |
| Contenedor | | | |
| Codec de vídeo | | | |
| ¿Intra-frame o long-GOP? | | | |
| Chroma subsampling | | | |
| Bit depth de vídeo | | | |
| Resolución | | | |
| Frame rate | | | |
| Codec de audio | | | |
| Frecuencia de muestreo | | | |
| Bitrate total (Mbps) | | | |
| GB por hora | | | |
```

**Verifica**: las doce filas están rellenas para los tres archivos. Si alguna casilla
está vacía porque el dato no aparece, escribe **por qué** no aparece: eso también es
información. Un WAV no tiene codec de vídeo, y eso se escribe.

---

## Paso 6 (opcional): lo mismo desde la terminal

**Por qué**: cuando hay treinta archivos, la interfaz gráfica deja de ser cómoda. Si
tienes FFmpeg instalado, `ffprobe` da la misma información en una línea.

```bash
ffprobe -v error -select_streams v:0 \
        -show_entries stream=codec_name,pix_fmt,width,height,r_frame_rate,bit_rate \
        -of default=noprint_wrappers=1 tu-clip.mp4
```

El campo `pix_fmt` es el que codifica chroma y bit depth a la vez:

| `pix_fmt` | Chroma | Bit depth |
| --------- | ------ | --------- |
| `yuv420p` | 4:2:0 | 8 bits |
| `yuv420p10le` | 4:2:0 | 10 bits |
| `yuv422p10le` | 4:2:2 | 10 bits |
| `yuv444p10le` | 4:4:4 | 10 bits |

Y para una carpeta entera:

```bash
for f in *.mp4; do
  echo "== $f"
  ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,pix_fmt -of csv=p=0 "$f"
done
```

**Verifica**: la salida coincide con lo que dice MediaInfo para el mismo archivo.

---

## ✅ Resultado

- [ ] MediaInfo instalado y en vista `Tree`
- [ ] Sé localizar los seis campos clave de una ficha
- [ ] Sé calcular el bitrate a partir del tamaño y la duración
- [ ] `ficha-tecnica-material.md` creada en `04-respaldos/` con los tres archivos
- [ ] Las casillas vacías llevan escrito por qué están vacías

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| MediaInfo no muestra `Chroma subsampling` | Estás en la vista `Basic` o `Sheet` | `View > Tree` |
| El campo `Bit depth` no aparece | Algunos codecs no lo declaran en la cabecera | Escríbelo como "no declarado"; con H.264 de consumo, asume 8 bits |
| El bitrate calculado sale disparatado | Estás usando megabits donde tocan megabytes, o al revés | MB × 8 = Mb. La mayúscula es bytes |
| MediaInfo no abre el archivo | El archivo está corrupto o incompleto | Comprueba el tamaño; si la descarga se cortó, vuelve a bajarlo |
| No encuentro un WAV para el tercer archivo | Todavía no has descargado audio del pack | Baja uno de [Freesound](https://freesound.org/), o graba diez segundos con el móvil |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · Leer la ficha técnica de un archivo** | [02 · Preparar y sellar el material](02-preparar-y-sellar-el-material.md) |

← [Volver a la Semana 02](../README.md)
