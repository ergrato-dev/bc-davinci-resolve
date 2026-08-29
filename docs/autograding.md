# ✅ Autograding: cómo se corrigen los entregables

> Un entregable que nadie comprueba no es un entregable, es una intención. Este
> bootcamp comprueba lo comprobable leyendo el estado real de tu proyecto de Resolve.

---

## 1. Qué se automatiza y qué no

| Se automatiza | No se automatiza |
| ------------- | ---------------- |
| Existe una timeline llamada `BC-Montaje-v1` | Si el montaje tiene ritmo |
| La timeline va a 24 fps y 1920×1080 | Si el etalonaje está bien |
| Hay 12 clips en la pista `Video 1` | Si la mezcla suena limpia |
| Hay 4 marcadores | Si el key no tiene halo |
| El bin `01-Basicos` existe y tiene 15 clips | Si la elección de plano es acertada |
| No quedan huecos en la timeline | Si la pieza se entiende |

La columna izquierda la corrige `scripts/verificar-semana.py`. La derecha la corriges
tú, con la rúbrica de la semana, que traduce cada criterio estético a algo observable
—"los negros están en 0 sin recortar", "el diálogo promedia -12 dBFS", "el borde del
key no muestra halo verde a 200 % de zoom"— en lugar de pedirte que juzgues si algo
es bonito.

---

## 2. Cómo funciona por dentro

Son dos piezas separadas, y esa separación es deliberada:

```
   Tú, en una terminal                 DaVinci Resolve
┌────────────────────────┐         ┌──────────────────────────┐
│ verificar-semana.py    │  HTTP   │  puente (script in-app)  │
│  lee checks.json  ─────┼────────►│  Workspace > Scripts     │
│  evalúa el resultado   │◄────────┼──  habla con la API      │
└────────────────────────┘         └──────────────────────────┘
```

El **puente** es un script que corre **dentro** de Resolve. Es quien realmente habla
con la API de scripting. El **verificador** es un cliente que le hace preguntas por
HTTP en `127.0.0.1`.

> [!IMPORTANT]
> Ese reparto no es un capricho de arquitectura: **es lo que permite que el autograding
> funcione en DaVinci Resolve Free**. El scripting *externo* —conectarse a Resolve
> desde una terminal— es una función de Studio. El scripting *interno* —un script
> lanzado desde `Workspace > Scripts`— funciona en la versión gratuita. Poniendo el
> puente dentro y el cliente fuera, todo el bootcamp se corrige en Free.

El verificador **solo lee**. No crea, no borra y no modifica nada de tu proyecto.

---

## 3. Uso

```bash
# ¿Está todo en su sitio?
python scripts/verificar-semana.py --doctor

# Corregir una semana entera
python scripts/verificar-semana.py 01

# Ver qué comprobaciones tiene una semana, sin ejecutarlas
python scripts/verificar-semana.py 01 --list

# Ejecutar solo una
python scripts/verificar-semana.py 01 --check frame-rate
```

Salida típica:

```
Semana 01 — Fundamentos de imagen en movimiento

  OK  El proyecto del bootcamp existe
  KO  La timeline del proyecto va a 24 fps
      File > Project Settings > Master Settings > Timeline frame rate. Ojo: no se
      puede cambiar con clips ya importados.

  1 de 2 comprobaciones sin superar.
```

Código de salida `0` si todo pasa, `1` si algo falla. Cada fallo imprime su **pista**:
la ruta concreta para arreglarlo, nunca un "revísalo".

### Requisitos

1. Resolve 21 abierto, **con tu proyecto del bootcamp cargado**.
2. El puente lanzado desde `Workspace > Scripts > Utility`.
3. El verificador ejecutado con un Python que alcance `127.0.0.1` en la máquina donde
   corre Resolve. Si editas en Windows pero el repositorio vive en WSL, usa el Python
   de Windows:

```bash
"/mnt/c/Program Files/Python312/python.exe" scripts/verificar-semana.py 01
```

---

## 4. El formato de `checks.json`

Cada semana declara sus comprobaciones en `bootcamp/week-NN-*/checks.json`:

```json
{
  "semana": "01",
  "titulo": "Fundamentos de imagen en movimiento",
  "checks": [
    {
      "id": "proyecto-existe",
      "descripcion": "Existe el proyecto BC-Bootcamp-Resolve",
      "op": "project_list",
      "args": {},
      "expr": "'BC-Bootcamp-Resolve' in r['projects']",
      "pista": "File > New Project, y nómbralo exactamente BC-Bootcamp-Resolve."
    }
  ]
}
```

| Campo | Qué es |
| ----- | ------ |
| `id` | Identificador corto en kebab-case. Es lo que acepta `--check` |
| `descripcion` | Una línea, en positivo, describiendo el estado correcto |
| `op` | Operación del puente a invocar (tabla de la sección 5) |
| `args` | Argumentos de la operación. `{}` si no lleva |
| `expr` | Expresión de Python que devuelve verdadero o falso. `r` es el resultado de la operación |
| `pista` | La ruta concreta para arreglarlo. Se imprime solo cuando el check falla |

Reglas de escritura:

- **Una comprobación, un hecho.** Si la descripción necesita una "y", son dos checks.
- **`expr` siempre booleana.** Nada de expresiones que devuelvan un número.
- **`pista` siempre accionable**: una ruta de menú, un atajo o un nombre exacto. Nunca
  "revisa la configuración".
- **Nada destructivo.** Solo operaciones de lectura.

---

## 5. Operaciones disponibles y qué devuelven

Las formas de abajo están tomadas de respuestas reales de Resolve 21.0.4.5.

### `ping`

Estado del puente y de Resolve.

```json
{ "bridge_version": "1.9.0", "resolve_version": "21.0.4.5",
  "product": "DaVinci Resolve", "current_page": "edit",
  "project": "BC-Bootcamp-Resolve", "api_health": "ok" }
```

```python
r['resolve_version'].startswith('21.')
```

### `project_list`

Proyectos de la carpeta actual de la base de datos.

```json
{ "projects": ["BC-Bootcamp-Resolve", "New Project 1"] }
```

### `project_settings`

Ajustes del proyecto abierto.

```json
{ "project": "BC-Bootcamp-Resolve",
  "settings": { "timelineFrameRate": 24,
                "timelineResolutionWidth": "1920",
                "timelineResolutionHeight": "1080",
                "timelinePlaybackFrameRate": "24",
                "videoMonitorFormat": "HD 1080p 24",
                "colorScienceMode": "davinciYRGB",
                "timelineOutputResolutionWidth": "1920",
                "timelineOutputResolutionHeight": "1080" },
  "timeline_count": 1 }
```

> [!WARNING]
> Los tipos no son homogéneos: `timelineFrameRate` llega como número y las
> resoluciones como cadena. Convierte siempre en la expresión:
> `int(r['settings']['timelineResolutionWidth']) == 1920`.

### `timeline_list`

```json
{ "timelines": ["BC-Montaje-v1"], "count": 1 }
```

### `timeline_probe`

La timeline **activa**, con sus pistas y clips ya calculados.

```json
{ "name": "BC-Montaje-v1", "start_frame": 86400, "end_frame": 88005,
  "fps": 24, "duration_frames": 1605, "duration_seconds": 66.875,
  "resolution": "1920x1080",
  "video_tracks": 1, "audio_tracks": 1, "subtitle_tracks": 0,
  "tracks": [ { "type": "video", "index": 1, "name": "Video 1",
                "items": [ { "name": "plano-01.mp4", "start": 86400, "end": 86500,
                             "frames": 100, "duration": 100,
                             "source_start": 0, "source_end": 99, "left_offset": 0 } ] } ] }
```

```python
# al menos 12 clips en la primera pista de vídeo
len([t for t in r['tracks'] if t['type'] == 'video'][0]['items']) >= 12
```

### `media_list`

Clips de un bin. Con `args: {"bin": ["01-Basicos"]}` entra en ese bin; sin argumentos,
lista el bin activo.

```json
{ "bin": "01-Basicos",
  "clips": [ { "name": "plano-01.mp4", "duration": "00:00:26:45", "fps": 60,
               "resolution": "1920x1080", "path": "C:\\...\\plano-01.mp4" } ] }
```

### `media_clip_properties`

Todas las propiedades que Resolve conoce de un clip **del bin activo**. Lleva
`args: {"clip_name": "BC-formato-h264.mp4"}`, con el nombre tal y como aparece en el
media pool. Devuelve más de doscientos campos; estos son los que usa el bootcamp:

```json
{ "clip": "BC-formato-h264.mp4", "bin": "BC-Formatos",
  "properties": { "Format": "QuickTime", "Video Codec": "H.264 High L4.2",
                  "Audio Codec": "AAC", "Bit Depth": "8", "Audio Bit Depth": "32",
                  "Sample Rate": "48000", "Audio Ch": "2", "Data Level": "Auto",
                  "Alpha mode": "None", "PAR": "Square", "Resolution": "1920x1080",
                  "FPS": 60, "Type": "Video + Audio",
                  "Input Color Space": "Rec.709 (Scene)", "Input Gamma": "Rec.709" } }
```

> [!IMPORTANT]
> Lee del **bin activo**. Un check que la use depende de que el bin correcto esté
> seleccionado en el media pool, así que conviene precederlo de un check sobre
> `media_list` sin argumentos que compruebe cuál es el bin activo, y decirlo en la pista.

> [!NOTE]
> Un `.mp4` reporta `Format: QuickTime`: Resolve reconoce la familia del contenedor, no la
> extensión. Los tipos tampoco son homogéneos aquí: `Bit Depth` llega como cadena y `FPS`
> como número. *Verificado en 21.0.4.5, agosto de 2026.*

### Otras operaciones de lectura

| Operación | Para qué | Se usa a partir de |
| --------- | -------- | ------------------ |
| `media_clip_properties` | Metadata y propiedades de un clip concreto | Semana 02 |
| `marker_list` / `timeline_list_markers` | Marcadores de la timeline | Semana 09 |
| `timeline_detect_gaps` | Huecos entre clips | Semana 09 |
| `render_presets` / `render_formats` | Presets y codecs disponibles | Semana 28 |
| `render_status` | Estado de la cola de render | Semana 28 |

---

## 6. Escribir un check nuevo

1. Ejecuta la operación a mano y mira su forma real antes de escribir la expresión.
2. Escribe la `expr` contra esa forma, no contra la que supones.
3. Rompe el estado a propósito en Resolve y comprueba que el check **falla**. Un check
   que nunca ha fallado no está probado.
4. Escribe la `pista` como si se la dijeras a alguien que acaba de instalar el programa.

> [!WARNING]
> **Cuidado con las comprensiones anidadas.** La expresión se evalúa con `r` en el ámbito
> local, y una comprensión crea un ámbito nuevo que no lo ve. Solo el **primer iterable**
> de la comprensión se evalúa en el ámbito de fuera:
>
> ```python
> len([c for c in r['clips'] if c['name'] == 'x']) >= 1     # funciona
> all(n in [c['name'] for c in r['clips']] for n in NOMBRES) # NameError: name 'r'
> any(c['name'].startswith('BC-') for c in r['clips'])       # funciona
> ```
>
> Si necesitas comprobar varios nombres, encadena con `and` una expresión por nombre, cada
> una con `r` en la posición del primer iterable.

> [!TIP]
> Los ejercicios nombran proyectos, timelines y bins con el prefijo `BC-`
> (`BC-Bootcamp-Resolve`, `BC-Montaje-v1`, `BC-Color-v2`). No es decorativo: es lo que
> permite que los checks localicen tus entregables sin adivinar.

---

## 7. Los pesos de la evaluación

Cada semana pide tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 %
en dos y un 40 % en la tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario y sus respuestas en `rubrica-evaluacion.md` |
| 💪 Desempeño | 40 % | `verificar-semana.py` |
| 📦 Producto | 30 % | Tú, con los criterios observables de la rúbrica |

---

## 📚 Recursos adicionales

- `Developer/Scripting/README.txt` dentro de tu instalación de Resolve — la referencia oficial y completa de la API. Todo lo que hace el puente sale de ahí.
- [Foro oficial de DaVinci Resolve — Scripting](https://forum.blackmagicdesign.com/) — donde se documentan los comportamientos de la API que el README no cubre.

## ✅ Checklist de verificación

- [ ] `python scripts/verificar-semana.py --doctor` en verde
- [ ] Entiendo por qué el puente va dentro de Resolve y el cliente fuera
- [ ] Sé leer la forma que devuelve una operación antes de escribir una expresión
- [ ] Sé que el verificador solo lee y nunca modifica mi proyecto
- [ ] Uso el prefijo `BC-` al nombrar proyectos, timelines y bins de los ejercicios

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
