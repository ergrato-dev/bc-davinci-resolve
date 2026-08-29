# 🎩 Trucos y atajos, todos juntos

> Cada semana termina con su sección `🎩 Trucos y atajos`. Aquí están todos,
> agrupados por semana, para poder buscarlos sin abrir treinta y seis archivos.

Criterio de admisión: un truco entra si **ahorra tiempo real** o **revela algo que la
interfaz esconde**, y si es estable —un atajo, una ruta de menú, un modificador—. No
entran los consejos genéricos de productividad ni nada que dependa de plugins de
terceros.

---

## Semana 01 — Fundamentos de imagen en movimiento

| Truco | Cómo |
| ----- | ---- |
| Cambiar de página sin ratón | `Shift+2` a `Shift+8`, en el orden de los botones de abajo: Media, Cut, Edit, Fusion, Color, Fairlight, Deliver |
| Ver la versión exacta que tienes | `Help > About DaVinci Resolve`. Si pone solo "DaVinci Resolve" y no "Studio", tienes la gratuita |
| Buscar cualquier atajo por el nombre del comando | `DaVinci Resolve > Keyboard Customization` y escribe en el buscador. Es más rápido que memorizar tablas |
| Saber el frame rate real de un archivo antes de importarlo | Página Media, selecciona el clip y mira la columna *Frame Rate* del media pool, o abre el Metadata panel |
| Cambiar de unidades de tiempo | Clic derecho sobre el contador de timecode del viewer para alternar entre timecode y número de frames |
| Recuperar un layout que has destrozado | `Workspace > Reset UI Layout`. No toca tu proyecto, solo la disposición de los paneles |
| Live Save, para no volver a perder trabajo | `Preferences > User > Project Save and Load > Live Save`. Guarda continuamente mientras trabajas |

---

## Semana 02 — Codecs, contenedores y flujo de datos

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

_Las semanas 03 a 36 añadirán aquí sus trucos según se publiquen._

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
