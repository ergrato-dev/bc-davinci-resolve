# Semana 01 — Fundamentos de imagen en movimiento

> Antes de tocar un solo botón de DaVinci Resolve hay que entender qué es exactamente
> lo que el programa manipula. Cuatro conceptos —frame, cadencia, obturador y
> resolución— explican el 80 % de las decisiones que tomarás las 35 semanas siguientes.

Esta semana no montas nada. Esta semana entiendes **qué es un vídeo**, instalas
DaVinci Resolve 21 y creas el proyecto que te va a acompañar nueve meses. Si alguna vez
te has preguntado por qué un vídeo se ve "raro" y no sabías nombrar el porqué, aquí
está la respuesta.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Explicar** qué es un frame y por qué una sucesión de imágenes fijas produce
  movimiento
- **Elegir** el frame rate de un proyecto con un criterio, no por costumbre
- **Distinguir** 24, 25, 29.97 y 30 fps, y saber por qué existen esos decimales
- **Calcular** cuánto obturador necesita una toma para tener el desenfoque de
  movimiento correcto
- **Distinguir** resolución, aspect ratio y formato de entrega, que no son lo mismo
- **Leer y escribir** timecode, y saber qué es un timecode drop frame
- **Instalar y configurar** DaVinci Resolve 21 desde cero
- **Navegar** las siete páginas del programa sin usar el ratón
- **Crear** un proyecto con los ajustes correctos y saber cuáles no se pueden cambiar
  después

---

## 📋 Prerrequisitos

- Ninguna semana anterior: esta es la primera.
- Un ordenador que cumpla los mínimos de
  [`docs/hardware-y-rendimiento.md`](../../docs/hardware-y-rendimiento.md).
- Conexión a internet para descargar Resolve (unos 3 GB).
- **No hace falta material de vídeo todavía.** Esta semana no se importa ningún clip.

---

## 🗂️ Estructura de la Semana

```
week-01-fundamentos_de_imagen_en_movimiento/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 8 diagramas
├── 1-teoria/                    # 8 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # la primera capa de tu pieza
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · Qué es el vídeo](1-teoria/01-que-es-el-video.md) | Frames, muestreo del tiempo y por qué vemos movimiento | 30 min |
| [02 · Frame rate](1-teoria/02-frame-rate.md) | 24, 25, 30, 50, 60 fps, los decimales de NTSC y cómo elegir | 30 min |
| [03 · Obturador y desenfoque de movimiento](1-teoria/03-obturador-y-desenfoque-de-movimiento.md) | La regla de los 180°, el *judder* y el *rolling shutter* | 30 min |
| [04 · Resolución](1-teoria/04-resolucion.md) | Píxeles, HD, UHD, 4K DCI, escalado y sobremuestreo | 30 min |
| [05 · Aspect ratio y encuadre seguro](1-teoria/05-aspect-ratio-y-encuadre-seguro.md) | 16:9, 2.39:1, 9:16, *safe areas* y píxeles no cuadrados | 30 min |
| [06 · Timecode](1-teoria/06-timecode.md) | `HH:MM:SS:FF`, *drop frame* y el timecode de origen | 30 min |
| [07 · Instalar DaVinci Resolve 21](1-teoria/07-instalar-davinci-resolve-21.md) | Descarga, instalación, primer arranque y qué versión tienes | 30 min |
| [08 · Anatomía de Resolve](1-teoria/08-anatomia-de-resolve.md) | Las siete páginas, el Project Manager y la lógica del programa | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · Instalar y primer arranque](2-practicas/01-instalar-y-primer-arranque.md) | Instalas Resolve 21 y lo dejas configurado para nueve meses | 45 min |
| [02 · Crear el proyecto del bootcamp](2-practicas/02-crear-el-proyecto-del-bootcamp.md) | Creas `BC-Bootcamp-Resolve` con los ajustes correctos | 45 min |
| [03 · Recorrido por las siete páginas](2-practicas/03-recorrido-por-las-siete-paginas.md) | Navegas el programa entero sin ratón y recuperas layouts | 45 min |
| [04 · Leer y calcular timecode](2-practicas/04-leer-y-calcular-timecode.md) | Conviertes entre timecode, frames y segundos, y creas tu primera timeline | 45 min |

### Proyecto

Eliges la pieza que vas a construir durante 36 semanas y creas su timeline vacía con
los ajustes que has decidido con criterio.
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

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Cambiar de página sin ratón | `Shift+2` a `Shift+8`, en el orden de los botones de abajo: Media, Cut, Edit, Fusion, Color, Fairlight, Deliver |
| Ver la versión exacta que tienes | `Help > About DaVinci Resolve`. Si pone solo "DaVinci Resolve" y no "Studio", tienes la gratuita |
| Buscar cualquier atajo por el nombre del comando | `DaVinci Resolve > Keyboard Customization` y escribe en el buscador. Más rápido que memorizar tablas |
| Saber el frame rate real de un archivo antes de importarlo | Página Media, selecciona el clip y mira la columna *Frame Rate* del media pool, o abre el panel de Metadata |
| Cambiar de unidades de tiempo | Clic derecho sobre el contador de timecode del viewer para alternar entre timecode y número de frames |
| Recuperar un layout que has destrozado | `Workspace > Reset UI Layout`. No toca tu proyecto, solo la disposición de los paneles |
| Live Save, para no volver a perder trabajo | `Preferences > User > Project Save and Load > Live Save`. Guarda continuamente mientras trabajas |

---

## 📌 Entregables

1. ✅ DaVinci Resolve 21 instalado, arrancando sin errores, con Live Save activado
2. ✅ Proyecto **`BC-Bootcamp-Resolve`** creado y abierto
3. ✅ Timeline frame rate fijado a **24 fps**
4. ✅ Resolución de timeline **1920×1080**
5. ✅ Ciencia de color en **DaVinci YRGB**
6. ✅ Timeline vacía **`BC-Montaje-v1`** creada, a 24 fps
7. ✅ Formato de tu pieza elegido y justificado por escrito en `3-proyecto/`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 01
```

Con Resolve abierto, el proyecto `BC-Bootcamp-Resolve` cargado y el puente lanzado desde
`Workspace > Scripts > Utility`. Si algo falla antes de eso:

```bash
python scripts/verificar-semana.py --doctor
```

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **Semana 01** | [Semana 02](../week-02-codecs_contenedores_y_flujo_de_datos/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
