# Semana 02 — Codecs, contenedores y flujo de datos

> Un archivo de vídeo es una caja con cosas comprimidas dentro. Saber qué caja, qué cosas
> y con cuánta compresión explica por qué un clip va fluido y otro se arrastra, por qué un
> croma sale limpio y otro con halo, y por qué el disco se llena cuando nadie lo esperaba.

Esta semana no montas nada todavía, pero sí importas por primera vez. Al terminar sabrás
leer la ficha técnica de cualquier archivo, saber qué te va a dar problemas antes de
dárselos a Resolve, y tendrás calculado el disco que necesitas para nueve meses.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Distinguir** contenedor de codec, y leer los dos en cualquier archivo
- **Diferenciar** remuxear de transcodificar, y saber cuál de las dos destruye calidad
- **Explicar** por qué un codec long-GOP se reproduce bien y se monta mal
- **Leer** la notación `4:2:0`, `4:2:2` y `4:4:4`, y saber cuándo la diferencia importa
- **Reconocer** el banding y relacionarlo con la profundidad de bits del material
- **Identificar** material log y RAW, y saber por qué el log se ve lavado
- **Describir** qué es Blackmagic RAW y qué queda ajustable después de grabar
- **Elegir** frecuencia de muestreo y codec de audio con criterio
- **Calcular** el bitrate, el espacio en disco y la velocidad de lectura que pide tu material
- **Configurar** dónde escribe Resolve su caché, y por qué no debe ser el disco del sistema

---

## 📋 Prerrequisitos

- [Semana 01](../week-01-fundamentos_de_imagen_en_movimiento/README.md) cerrada: proyecto
  `BC-Bootcamp-Resolve` creado, a 24 fps, con sus ocho checks en verde
- La estructura `BC-Resolve/` creada en tu disco de trabajo
- **MediaInfo** instalado (gratuito, <https://mediaarea.net/MediaInfo>)
- **FFmpeg** recomendado, imprescindible si tienes archivos `.mkv`
  (<https://ffmpeg.org/download.html>)
- Cuatro archivos: dos vídeos de fuentes distintas, un audio y un PNG con transparencia.
  Ver [`docs/pack-de-medios.md`](../../docs/pack-de-medios.md)

---

## 🗂️ Estructura de la Semana

```
week-02-codecs_contenedores_y_flujo_de_datos/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 8 diagramas
├── 1-teoria/                    # 8 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # la ficha técnica de tu material
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · Contenedor y codec](1-teoria/01-contenedor-y-codec.md) | La caja y lo que lleva dentro, remux frente a transcode, el caso `.mkv` | 30 min |
| [02 · Compresión: intra-frame y long-GOP](1-teoria/02-compresion-intra-frame-y-long-gop.md) | Frames I, P y B, GOP, y por qué el montaje va a tirones | 30 min |
| [03 · Chroma subsampling](1-teoria/03-chroma-subsampling.md) | `4:4:4`, `4:2:2`, `4:2:0` y cuándo la diferencia se nota | 30 min |
| [04 · Profundidad de bits](1-teoria/04-profundidad-de-bits.md) | 8 y 10 bits, banding, y los niveles de datos `Full` y `Video` | 30 min |
| [05 · Log, RAW y Rec.709](1-teoria/05-log-raw-y-rec709.md) | Curvas de transferencia, por qué el log se ve lavado, qué es revelar | 30 min |
| [06 · Blackmagic RAW](1-teoria/06-blackmagic-raw.md) | Debayer parcial, modos de compresión y qué queda ajustable | 30 min |
| [07 · Audio digital](1-teoria/07-audio-digital.md) | Muestreo, 48 kHz, PCM frente a AAC | 30 min |
| [08 · El flujo de datos](1-teoria/08-flujo-de-datos.md) | Bitrate, velocidad de disco, presupuesto de espacio y carpetas | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · Leer la ficha técnica de un archivo](2-practicas/01-leer-la-ficha-tecnica-de-un-archivo.md) | Diseccionas tres archivos con MediaInfo y calculas su bitrate a mano | 45 min |
| [02 · Preparar y sellar el material](2-practicas/02-preparar-y-sellar-el-material.md) | Montas el pack de medios, remuxeas lo que Resolve no acepta y lo sellas con `sha256` | 45 min |
| [03 · El banco de formatos](2-practicas/03-el-banco-de-formatos.md) | Importas cuatro archivos distintos a `BC-Formatos` y lees lo que dice Resolve de cada uno | 45 min |
| [04 · Medir el flujo de datos](2-practicas/04-medir-el-flujo-de-datos.md) | Mides tu disco, calculas el presupuesto del bootcamp y colocas la caché | 45 min |

### Proyecto

Averiguas qué clase de archivos va a producir tu pieza, cuánto van a ocupar y con qué vas
a grabar, y lo dejas escrito.
→ [3-proyecto/README.md](3-proyecto/README.md)

---

## ⏱️ Distribución del Tiempo (10 horas)

| Actividad | Tiempo |
| --------- | ------ |
| Teoría (8 archivos × 30 min) | 4 h |
| Prácticas (4 × 45 min) | 3 h |
| Proyecto | 2 h |
| Recursos y glosario | 30 min |
| Autoevaluación | 30 min |
| **Total** | **10 h** |

---

## 💠 Qué necesita Studio esta semana

**Nada.** Todo lo de esta semana funciona en DaVinci Resolve Free, incluida la lectura de
Blackmagic RAW, que es nativa en las dos versiones.

Hay dos límites que conviene conocer desde ya, aunque no afecten a ningún entregable:

| Límite | Dónde aparece | Qué hacer en Free |
| ------ | ------------- | ----------------- |
| El render está limitado a **4K UHD** (3840 × 2160) | Semanas 28-29 | Entregar a 3840 × 2160, que cubre todas las plataformas del bootcamp |
| La lista de codecs que Resolve **escribe** depende de la versión **y del sistema operativo** | Página Deliver | Comprueba tus propios desplegables `Format` y `Codec`; para **leer**, Resolve es mucho más generoso que para escribir |

Detalle completo en [`docs/free-vs-studio.md`](../../docs/free-vs-studio.md).

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Ver el codec sin salir del media pool | Vista de lista del media pool, clic derecho sobre la cabecera de columnas para añadir las que te interesen |
| Leer el chroma subsampling, que Resolve no muestra | MediaInfo en vista `Tree`, campo `Chroma subsampling`; o `ffprobe` y su campo `pix_fmt` |
| Cambiar de contenedor sin perder calidad | `ffmpeg -i entrada.mkv -c copy salida.mp4`. `-c copy` copia las pistas sin recomprimir |
| Que OBS deje de grabar en `.mkv`, que Resolve no abre | En OBS, `Ajustes > Avanzado > Grabación`, activa el remuxeado automático a `.mp4` |
| Comprobar qué codecs escribe **tu** instalación | Página Deliver, `Render Settings`, desplegables `Format` y `Codec`. Lo que veas ahí es la verdad de tu máquina |
| Saber si el frame rate ya está bloqueado | `File > Project Settings > Master Settings`: si el campo `Timeline frame rate` aparece atenuado, hay clips en el media pool |
| Ver dónde escribe Resolve por defecto | `Preferences > System > Media Storage`. El primer disco de la lista es el que se usa |
| Recuperar espacio de disco sin perder trabajo | `Playback > Delete Render Cache > All`. La caché es regenerable por definición |

---

## 📌 Entregables

1. ✅ Pack de medios con sus nueve carpetas y `MANIFIESTO.sha256` verificando en verde
2. ✅ Ningún `.mkv` sin convertir en el pack
3. ✅ Bin **`BC-Formatos`** creado y activo en `BC-Bootcamp-Resolve`
4. ✅ Cuatro clips dentro, con los nombres `BC-formato-h264`, `BC-formato-segundo`,
   `BC-formato-audio` y `BC-formato-alpha`
5. ✅ `Timeline frame rate` intacto a **24 fps** después de importar
6. ✅ `Cache files location` apuntando a `BC-Resolve/02-cache/`
7. ✅ `ficha-tecnica-material.md` con sus cuatro partes, en `04-respaldos/`
8. ✅ Respaldo `BC-Bootcamp-Resolve-semana02.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 02
```

Con Resolve abierto, el proyecto `BC-Bootcamp-Resolve` cargado, el bin `BC-Formatos`
seleccionado y el puente lanzado desde `Workspace > Scripts > Utility`. Si algo falla antes
de eso:

```bash
python scripts/verificar-semana.py --doctor
```

Y para el pack de medios, que no pasa por Resolve:

```bash
./scripts/preparar-medios.sh
```

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 01](../week-01-fundamentos_de_imagen_en_movimiento/README.md) | **Semana 02** | [Semana 03](../week-03-resolve_21_anatomia_bases_de_datos_y_preferencias/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
