# 🤖 Instrucciones para GitHub Copilot

## 📋 Contexto del Bootcamp

Este es un **Bootcamp DaVinci Resolve 21 Zero to Master**: 36 semanas sobre
**post-producción completa en DaVinci Resolve 21** (no sobre "editar vídeos", y no
sobre una sola página del programa). Lleva a alguien que **nunca ha editado vídeo**
hasta un perfil de **postproductor completo**: capaz de ingestar, montar, mezclar,
etalonar, componer, entregar y **automatizar** por scripting.

### 📊 Datos del Bootcamp

- **Duración**: 36 semanas (~9 meses)
- **Dedicación semanal**: 10 horas
- **Total de horas**: 360 horas
- **Modalidad**: autoestudio asincrónico con verificación automática por la API de Resolve
- **Nivel de entrada**: **cero absoluto**. No se asume ni edición, ni fotografía, ni
  audio, ni programación
- **Nivel de salida**: postproductor autónomo — ingesta, montaje, sonido, color, VFX,
  entrega y automatización por Python
- **Versión objetivo**: **DaVinci Resolve 21** (verificado contra 21.0.4.5)
- **Licencia asumida**: **Resolve Free**. Las funciones de **Studio** se marcan con
  badge y siempre llevan la ruta alternativa en Free
- **Idioma de la UI**: **inglés** (los menús se citan en inglés; la prosa es española)
- **Sistema operativo**: Windows y macOS como primarios, Linux mencionado donde difiere

---

## 🎯 Objetivos de Aprendizaje

Al finalizar el bootcamp, los estudiantes serán capaces de:

- ✅ Explicar qué es un frame, un codec, un espacio de color y un nivel de audio sin analogías vagas
- ✅ Ingestar material con integridad verificada y organizarlo para que escale
- ✅ Montar con soltura quirúrgica en Cut y en Edit (ripple, roll, slip, slide, dynamic trim)
- ✅ Construir títulos, efectos y compuestos sin salir de Resolve
- ✅ Editar multicámara y gestionar subtítulos y versiones de timeline
- ✅ Mezclar diálogo, música y efectos a un target de loudness concreto
- ✅ Limpiar audio problemático y diseñar el sonido de una pieza
- ✅ Etalonar con gestión de color explícita, leyendo scopes y no "a ojo"
- ✅ Dominar el grafo de nodos: serial, paralelo, layer, key mixer, outside
- ✅ Aislar con qualifiers, windows y tracking; igualar planos; diseñar un look
- ✅ Componer en Fusion: máscaras, paint, tracking, keying, motion graphics y 3D
- ✅ Entregar a cualquier destino con el codec, el bitrate y el loudness correctos
- ✅ Gestionar, archivar y colaborar sobre proyectos de Resolve
- ✅ Automatizar Resolve con la API de scripting de Python y herramientas propias

---

## 📚 Estructura del Bootcamp

### Distribución por Fases

#### **Fase 0 · Fundamentos audiovisuales y setup (Semanas 1-3)** — 30 horas

- Imagen en movimiento: frame, fps, obturador, resolución, aspect ratio, timecode
- Codecs y contenedores, chroma subsampling, bit depth, RAW/log/Rec.709, almacenamiento
- Anatomía de Resolve 21: las 7 páginas, bases de datos, preferencias, caché, Free vs Studio

#### **Fase 1 · Media e ingesta (Semanas 4-5)** — 20 horas

- Media Storage, clone tool con checksum, bins, smart bins, metadata, keywords
- Optimized media, proxies, render cache, sincronización, subclips, relink

#### **Fase 2 · Cut page (Semanas 6-7)** — 20 horas

- Dual timeline, source tape, sync bin, las cinco herramientas de edición rápida
- Transiciones, velocidad, títulos rápidos, dupe detection, quick export

#### **Fase 3 · Edit page (Semanas 8-12)** — 50 horas

- Anatomía, edición de tres puntos, modos de edición, timeline settings
- Trimming quirúrgico: ripple, roll, slip, slide, dynamic trim, JKL
- Velocidad, transformaciones, keyframes, estabilización
- Títulos, Text+, ResolveFX, adjustment clips, compound clips
- Multicam, subtítulos, versiones de timeline, media management, intercambio XML/AAF/EDL/OTIO

#### **Fase 4 · Fairlight (Semanas 13-15)** — 30 horas

- Anatomía de audio, buses, ganancias, medidores, monitorización
- Limpieza de diálogo, FairlightFX, ADR, automatización de mezcla
- Diseño sonoro, música, ducking, loudness y entrega de stems

#### **Fase 5 · Color (Semanas 16-22)** — 70 horas

- Teoría del color y gestión de color (DaVinci YRGB, YRGB Color Managed, ACES)
- Scopes y corrección primaria
- El grafo de nodos a fondo
- Secundarias: qualifiers, windows, tracking, máscaras
- Curvas, Color Warper, reducción de ruido, sharpening
- Shot matching, grupos, galería, LUTs, diseño de look
- HDR, RAW, control de calidad y entrega de color

#### **Fase 6 · Fusion (Semanas 23-27)** — 50 horas

- Modelo de nodos de Fusion, Merge, canal alpha, DoD
- Transformaciones, máscaras, paint, rotoscopia
- Tracking (punto, planar, cámara) y keying
- Motion graphics, Text3D, modifiers, partículas
- Workspace 3D, cámara, renderer, optimización y macros

#### **Fase 7 · Deliver y entrega (Semanas 28-29)** — 20 horas

- Render settings, codecs, presets, cola de render, escalado, subtítulos
- Entregas por destino, loudness por plataforma, archivado y control de calidad

#### **Fase 8 · Gestión y colaboración (Semana 30)** — 10 horas

- Project Manager, PostgreSQL, archives, collaboration mode, relink masivo

#### **Fase 9 · Automatización y scripting (Semanas 31-34)** — 40 horas

- API de scripting de Resolve, entorno Python, jerarquía de objetos
- Automatizar ingesta, organización, timelines, render y entrega
- Herramientas propias, puente MCP e integración con agentes

#### **Fase 10 · Cierre (Semanas 35-36)** — 20 horas

- Proyecto final: producción completa y entrega auditada de las 35 semanas

### Contenido Semana a Semana

| Semana | Slug                                                | Tema                                                                       |
| ------ | --------------------------------------------------- | -------------------------------------------------------------------------- |
| 01     | `fundamentos_de_imagen_en_movimiento`               | Frame, fps, obturador, resolución, aspect ratio, timecode, instalación      |
| 02     | `codecs_contenedores_y_flujo_de_datos`              | Contenedor vs codec, chroma subsampling, bit depth, RAW/log, almacenamiento |
| 03     | `resolve_21_anatomia_bases_de_datos_y_preferencias` | Las 7 páginas, Project Manager, bases de datos, preferencias, Free vs Studio |
| 04     | `media_page_ingesta_y_organizacion`                 | Media Storage, clone tool, bins, smart bins, metadata, keywords             |
| 05     | `proxies_cache_y_sincronizacion`                    | Optimized media, proxies, render cache, sync, subclips, relink              |
| 06     | `cut_page_edicion_veloz`                            | Dual timeline, source tape, sync bin, herramientas de edición rápida        |
| 07     | `cut_page_acabado_y_quick_export`                   | Transiciones, velocidad, títulos rápidos, dupe detection, quick export      |
| 08     | `edit_page_anatomia_y_edicion_basica`               | Interfaz, tres puntos, insert/overwrite/replace, timeline settings          |
| 09     | `trimming_quirurgico`                               | Ripple, roll, slip, slide, dynamic trim, JKL, marcadores                    |
| 10     | `velocidad_transformaciones_y_estabilizacion`       | Retime, speed ramps, keyframes, transform, estabilización                   |
| 11     | `titulos_texto_plus_efectos_y_compuestos`           | Text vs Text+, ResolveFX, adjustment clips, compound clips                  |
| 12     | `multicam_subtitulos_y_gestion_de_timeline`         | Multicam, subtítulos, timeline versions, media management, XML/AAF/EDL/OTIO |
| 13     | `fairlight_anatomia_y_mezcla_base`                  | Pistas, mixer, buses, ganancias, medidores, monitorización                  |
| 14     | `limpieza_de_dialogo_y_fairlight_fx`                | EQ, dinámica, noise reduction, Voice Isolation, ADR, automatización         |
| 15     | `diseno_sonoro_musica_y_loudness`                   | Capas de sonido, música, ducking, loudness, stems                           |
| 16     | `teoria_del_color_y_gestion_de_color`               | Espacios de color, gamma, log, DaVinci YRGB, Color Managed, ACES            |
| 17     | `scopes_y_correccion_primaria`                      | Waveform, parade, vectorscope, lift/gamma/gain, log wheels, balance         |
| 18     | `nodos_a_fondo`                                     | Serial, paralelo, layer mixer, key mixer, outside, splitter/combiner        |
| 19     | `secundarias_qualifiers_windows_y_tracking`         | HSL qualifier, windows, tracker, Magic Mask, rotoscopia                     |
| 20     | `curvas_color_warper_y_reduccion_de_ruido`          | Curvas custom y por eje, Color Warper, noise reduction, sharpening          |
| 21     | `shot_matching_grupos_stills_y_diseno_de_look`      | Galería, stills, groups, shot match, LUTs, film emulation, versiones        |
| 22     | `hdr_raw_y_entrega_de_color`                        | HDR wheels, tone mapping, camera raw, BRAW, QC de color, entrega            |
| 23     | `fusion_page_modelo_de_nodos`                       | Flow, Merge, alpha, DoD, MediaIn/MediaOut, relación con Edit                |
| 24     | `transformaciones_mascaras_y_paint`                 | Transform, polyline/bspline, paint, cleanup, rotoscopia                     |
| 25     | `tracking_y_keying`                                 | Tracker, Planar Tracker, Camera Tracker, Delta Keyer, despill               |
| 26     | `motion_graphics_texto_3d_y_particulas`             | Text+, Text3D, Follower, modifiers, expressions, partículas                 |
| 27     | `fusion_3d_camara_y_optimizacion`                   | Workspace 3D, Camera 3D, Renderer3D, caché, macros                          |
| 28     | `deliver_page_render_y_codecs`                      | Render settings, codecs, presets, cola, data levels, escalado               |
| 29     | `entregas_por_destino_y_control_de_calidad`         | Plataformas, bitrate, loudness, master vs deliverable, QC, archivado        |
| 30     | `gestion_de_proyectos_archivado_y_colaboracion`     | Project Manager, PostgreSQL, archives, collaboration, relink masivo         |
| 31     | `api_de_scripting_de_resolve_fundamentos`           | Habilitar scripting, Python, jerarquía de objetos, primer script            |
| 32     | `automatizar_ingesta_y_organizacion`                | Recorrer carpetas, bins, importación por lotes, metadata masiva             |
| 33     | `automatizar_timelines_render_y_entrega`            | Timelines por script, marcadores, SRT, cola de render, lotes                |
| 34     | `herramientas_propias_puente_mcp_y_agentes`         | Workspace > Scripts, UI Manager, puente MCP, agentes, seguridad             |
| 35     | `proyecto_final_produccion`                         | Pieza completa: ingesta, montaje, sonido, color, VFX                        |
| 36     | `proyecto_final_entrega_y_auditoria`                | Entrega multi-destino, QC, archivado, auditoría, portfolio                  |

---

## 🗂️ Estructura de Carpetas

Cada semana sigue esta estructura estándar:

```
bootcamp/week-XX-tema_principal/
├── README.md                 # Descripción y objetivos de la semana
├── rubrica-evaluacion.md     # Criterios de evaluación detallados
├── checks.json               # Declaración de verificaciones automáticas
├── 0-assets/                 # Diagramas SVG y stills de referencia
├── 1-teoria/                 # Material teórico (archivos .md)
├── 2-practicas/              # Ejercicios guiados paso a paso
├── 3-proyecto/               # Capa semanal del proyecto hilo conductor
│   └── README.md             # Instrucciones del entregable
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/               # Términos clave de la semana (A-Z)
    └── README.md
```

### 📁 Carpetas Raíz

- **`assets/`**: recursos visuales globales (header del README)
- **`docs/`**: documentación transversal (setup, medios, hardware, atajos, autograding, glosario, trucos, Free vs Studio, proyecto)
- **`scripts/`**: `verificar-semana.py` (autograding), `verificar-enlaces.sh`, `preparar-medios.sh`
- **`bootcamp/`**: contenido semanal

---

## 🎓 Componentes de Cada Semana

### 1. **Teoría** (`1-teoria/`)

- Archivos markdown con explicaciones conceptuales **en español**
- **El número de archivos de teoría es libre**: los que pida el temario, no un cupo
  fijo. Siete u ocho es lo normal; las semanas de Color y Fusion pueden pedir nueve.
  **Nunca se sacrifica profundidad para que quepa**
- **Extensión por archivo: ~250 líneas** (rango sano 200-300). Si un archivo se va de
  ahí, el problema es que mezcla dos temas: divídelo en dos archivos, no recortes
- Un archivo = un concepto. Si el título necesita una "y", sospecha
- Cada tema se explica en este orden: **qué problema resuelve → cómo se hace en
  Resolve → antipatrones → trucos**
- **Cero absoluto**: la primera vez que aparece un término técnico se define. No se
  asume vocabulario de fotografía, cine, audio ni informática
- Diagramas SVG cuando aporten (nunca ASCII art, nunca capturas de pantalla)
- Referencias al **DaVinci Resolve 21 Reference Manual** oficial como fuente de verdad

### 2. **Prácticas** (`2-practicas/`)

> ⚠️ **Diferencia clave con los bootcamps hermanos**: aquí las prácticas son
> **operaciones dentro de DaVinci Resolve**, no código en un `starter/`. El entregable
> es el **estado real de un proyecto de Resolve**, verificable por la API de scripting.

Formato de ejercicio:

```markdown
### Paso 3: Fijar el frame rate del proyecto antes de importar nada

**Por qué**: el timeline frame rate de un proyecto **no se puede cambiar** una vez
hay clips en el media pool. Si lo dejas mal ahora, la única salida es crear un
proyecto nuevo y volver a empezar.

**Ruta**: `File > Project Settings > Master Settings > Timeline frame rate`.

**Verifica**:

\`\`\`bash
python scripts/verificar-semana.py 01 --check frame-rate
\`\`\`
```

Reglas:

- Todo paso termina con una **forma de verificarlo**: un comando del verificador, una
  lectura de un panel concreto, o un valor observable en la UI
- Los pasos irreversibles llevan advertencia explícita **antes** del paso
  (frame rate del proyecto, borrar caché, `Delete Render Cache`, media management)
- Las rutas de menú se citan completas y en inglés: `Color > Nodes > Add Serial`,
  no "añade un nodo serie por ahí"
- Nunca describir la posición de un botón por píxeles ni por "arriba a la derecha"
  sin dar además la ruta de menú o el atajo, que es lo estable

En las semanas de **scripting (31-34)** sí hay código Python en `starter/`. Ahí aplica
el formato de **descomentar código** de los bootcamps hermanos:

```python
# ============================================
# PASO 2: crear el timeline vacío
# ============================================
# Descomenta las siguientes líneas:
# pool = project.GetMediaPool()
# timeline = pool.CreateEmptyTimeline("BC-Semana-33")
# print(timeline.GetName())
```

❌ No usar `# TODO:` en prácticas — eso es formato de proyecto.

### 3. **Proyecto** (`3-proyecto/`)

Cada semana añade **una capa nueva al mismo proyecto de Resolve del estudiante** (ver
`docs/proyecto-hilo-conductor.md`). Nunca un proyecto desechable por semana.

El README del proyecto incluye:

1. Qué capa se añade esta semana y por qué
2. Requisitos verificables (los mismos que declara `checks.json`)
3. Cómo verificarlo: `python scripts/verificar-semana.py NN`
4. Criterios de calidad más allá de lo automatizable

**No hay géneros asignados**: es autoestudio. El estudiante elige su pieza en la
Semana 01 (documental corto, videoclip, tutorial, vlog de viaje, cortometraje de
ficción) y la mantiene las 36 semanas. Los ejemplos deben servir para cualquiera.

### 4. **Recursos** (`4-recursos/`)

- **ebooks-free/**: manuales y guías gratuitas (el Reference Manual oficial, guías de
  entrenamiento de Blackmagic, libros abiertos de color y sonido)
- **videografia/**: charlas y tutoriales
- **webgrafia/**: documentación oficial de Blackmagic primero, luego blogs de calidad

Cada recurso lleva una línea de por qué vale la pena, no solo el enlace.

### 5. **Glosario** (`5-glosario/`)

Términos A-Z **en español**, con el **término real de la UI en inglés entre
paréntesis** siempre que exista (`grado (grade)`, `nodo serie (serial node)`,
`ventana de poder (power window)`). Esta es la pieza que conecta la prosa española con
la UI inglesa; no es opcional.

### 6. **`checks.json`**

Declaración de las verificaciones automáticas de la semana. Formato en
`docs/autograding.md`. Regla: **si un entregable se puede verificar por la API de
Resolve, se declara aquí**. Lo que no se puede verificar por API (un grado de color,
una mezcla, un comp) va a la rúbrica de autoevaluación con stills de referencia.
Nunca lógica de shell específica de una semana.

---

## 🎩 Sección de Trucos

**Obligatoria en el README de cada semana**: `## 🎩 Trucos y atajos`.

Criterio de admisión de un truco:

- ✅ Ahorra tiempo real o revela algo que la UI esconde
- ✅ Es verificable y estable (un atajo de teclado, una ruta de menú, un modificador)
- ❌ No es un "tip" genérico de productividad
- ❌ No depende de plugins de terceros no mantenidos

Todo truco nuevo se replica en `docs/trucos-resolve.md`, agrupado por semana.

---

## 📝 Convenciones

### Rutas de menú y atajos

- ✅ Ruta completa en inglés con `>`: `File > Project Settings > Master Settings`
- ✅ Atajo entre backticks con las dos plataformas: `` `Ctrl+Shift+D` (Win) / `Cmd+Shift+D` (Mac) ``
- ✅ El nombre exacto del panel o control tal y como aparece en la UI de v21
- ❌ Nunca "el botón de la derecha" sin nombrar el control
- ❌ Nunca inventar un nombre de menú, un ajuste o un efecto. Si hay duda, se verifica
  contra la instalación de Resolve 21 o se enlaza el manual oficial

```markdown
✅ BIEN
`Color > Nodes > Add Serial` — atajo `Alt+S` (Win) / `Opt+S` (Mac).

❌ MAL
Añade un nodo serie desde el menú de nodos.
```

### Marcado de funciones Studio

Toda función exclusiva de la versión de pago se marca **en la propia línea** y lleva
la ruta alternativa en Free:

```markdown
> [!IMPORTANT]
> **Studio** · `Voice Isolation` solo existe en DaVinci Resolve Studio.
> En Free, la ruta equivalente es un `Noise Reduction` de FairlightFX más un EQ
> paramétrico; el resultado es peor con ruido de fondo variable, pero es suficiente
> para los entregables de esta semana.
```

Ningún entregable evaluable puede depender de Studio.

### Valores numéricos

- ✅ Unidades siempre explícitas: `-14 LUFS`, `23.976 fps`, `1/50 s`, `10 bits`, `4:2:2`
- ✅ Los targets de loudness, bitrate y resolución se citan con su fuente y su fecha
- ❌ Nunca "sube un poco las luces" sin decir qué control y en qué rango

### Nomenclatura

- **Carpetas de semana**: `week-XX-tema_en_snake_case`
- **Archivos de teoría y prácticas**: `NN-tema-en-kebab-case.md`
- **SVG**: `NN-tema-en-kebab-case.svg` en `0-assets/`, numerados por orden de aparición
- **Nombres de proyecto, timeline y bin en los ejercicios**: prefijo `BC-`
  (`BC-Semana-01`, `BC-Montaje-v1`), para que el verificador los localice sin ambigüedad
- **Idioma**: inglés para la UI de Resolve, nombres de efectos, código y commits;
  español para la documentación y los comentarios educativos

### Placeholders

- `<tu-proyecto>` para el nombre del proyecto de Resolve del estudiante
- `<ruta-a-medios>` para la carpeta local del pack de medios
- ❌ Nunca una ruta absoluta real de una máquina concreta en el material

---

## 🔐 Reglas de Seguridad y Rigor del Contenido

- ✅ Los pasos **irreversibles** llevan advertencia antes, con mención del backup:
  cambiar el frame rate del proyecto, `Delete Render Cache`, media management
  destructivo, borrar una base de datos, `Relink` masivo
- ✅ Antes de cualquier operación sobre medios que escriba en disco, recordar que
  Resolve **no importa `.mkv`**: hay que remuxear a `.mp4`/`.mov` primero
- ✅ Toda afirmación sobre una feature de v21 verificada contra la instalación real o
  contra el manual oficial, con fecha si es volátil
- ✅ Los enlaces de descarga del pack de medios llevan `sha256`; sin checksum
  verificado, el recurso no entra
- ❌ Nunca una clave de licencia, un número de serie ni una vía de activación
- ❌ Nunca enlaces a material con copyright para "practicar color"; solo material con
  licencia explícita (Creative Commons, dominio público, samples oficiales de Blackmagic)
- ❌ Nunca inventar un endpoint de la API de scripting. Los métodos se citan tal cual
  aparecen en el `README.txt` del SDK de scripting que instala Resolve

---

## 🎨 Recursos Visuales

- ✅ **SVG** para todos los diagramas (nunca ASCII art, nunca capturas de pantalla)
- ✅ PNG solo para **stills de referencia** de color (comparativas antes/después) y
  solo cuando la rúbrica los necesite como criterio visual
- 🌙 **Tema oscuro**, **sin degradados**, colores sólidos
- ✅ Paleta del bootcamp:

```
fondo             #101418      texto              #e8eef4
superficie        #191f26      texto secundario   #93a1b0
superficie alta   #232b34      acento (azul)      #4a9eff
borde             #2f3a45      ámbar (Studio)     #f5a524
éxito             #3fb950      error              #f85149
violeta (Fusion)  #a371f7
canales de color  R #ff5f56  ·  G #4ade80  ·  B #5b9cff
```

- ✅ Tipografía sans-serif exclusivamente: `Inter, Roboto, "Segoe UI", system-ui, sans-serif`
- ✅ `viewBox` siempre, `role="img"`, `<title>` y `aria-label` descriptivo
- ✅ Ancho objetivo 800-880 px, texto mínimo 12 px, sin JS ni fuentes externas
- ✅ Nombrar en orden de lectura: `01-anatomia-del-frame.svg`, `02-cadena-de-color.svg`
- ✅ Todo SVG debe estar enlazado desde al menos un `.md`; uno huérfano es un error
  que reporta `verificar-enlaces.sh`

---

## 📖 Documentación

### README.md de Semana

Debe incluir, en este orden:

1. Título `# Semana NN — Tema`
2. `## 🎯 Objetivos de la Semana`
3. `## 📋 Prerrequisitos`
4. `## 🗂️ Estructura de la Semana` (árbol de archivos)
5. `## 📝 Contenidos` (tablas de teoría y prácticas con duración)
6. `## ⏱️ Distribución del Tiempo (10 horas)`
7. `## 🎩 Trucos y atajos`
8. `## 📌 Entregables`
9. `## ✅ Verificación` (comando de `verificar-semana.py`)
10. `## 🔗 Navegación` (anterior / actual / siguiente)

Las semanas que introducen funciones de pago añaden además una sección
`## 💠 Qué necesita Studio esta semana` con la tabla de equivalencias en Free.

### Archivos de Teoría

```markdown
# Título del Tema

> Blockquote de una línea: por qué esto importa.

## 🎯 Objetivos

## 1. Qué problema resuelve

## 2. Cómo funciona

## 3. Cómo se hace en Resolve 21

## 4. Antipatrones

## 5. Trucos

## 📚 Recursos Adicionales

## ✅ Checklist de Verificación
```

---

## 📊 Evaluación

Cada semana incluye **tres tipos de evidencias**:

1. **Conocimiento 🧠** (30%): cuestionario de autoevaluación con respuestas al final
2. **Desempeño 💪** (40%): prácticas verificadas por `verificar-semana.py`
3. **Producto 📦** (30%): la capa semanal del proyecto propio

Mínimo **70%** en cada tipo. Al ser autoestudio, el cuestionario incluye sus respuestas
en una sección colapsable (`<details>`) al final de la rúbrica.

**Lo estético no se automatiza.** Un grado de color, una mezcla de audio o un comp se
evalúan con criterios observables escritos en la rúbrica (¿los negros están en 0 sin
recortar?, ¿el diálogo llega a -12 dBFS de media?, ¿el borde del key tiene halo?), no
con un script que dictamine "bonito".

---

## 🤖 Instrucciones para Copilot

### Límites de Respuesta

1. **Divide respuestas largas**
   - ❌ Nunca generar respuestas que superen los límites de tokens
   - ✅ Dividir por carpetas: teoría → prácticas → proyecto → recursos → assets
   - ✅ Indicar siempre qué parte se entregó y qué falta

2. **Una semana por tanda**, usando la Semana 01 como plantilla de calidad

### Generación de Contenido

1. **Profundidad sobre cobertura**: es preferible explicar bien tres controles que
   listar veinte. El bootcamp existe porque los tutoriales superficiales sobran.
2. **Siempre el porqué**: ninguna instrucción sin el problema que resuelve y qué pasa
   si no se hace.
3. **Cero absoluto de verdad**: cada término se define la primera vez. "Log", "LUT",
   "headroom", "alpha" y "codec" no son vocabulario común.
4. **Verificable**: todo entregable debe poder comprobarse, por la API o por un
   criterio observable escrito. Si no se puede, replantear el entregable.
5. **Fechar lo volátil**: comportamientos que dependan de la versión exacta se marcan
   con la fecha de verificación y la versión (`verificado en 21.0.4.5, agosto 2026`).
6. **No inventar menús, efectos, ajustes ni métodos de la API.** Si hay duda, decirlo y
   enlazar el manual oficial en lugar de improvisar algo plausible.

### Estado del producto

- La versión objetivo es **DaVinci Resolve 21**; el material se escribe contra ella
- **Cut page** es una página de primera clase, no un accesorio: se enseña antes de Edit
  porque monta más rápido y se aprende antes
- **Color management** se enseña **antes** que las ruedas de color: etalonar sin saber
  en qué espacio estás es adivinar
- La **API de scripting** es Python 3; el SDK y su `README.txt` vienen con la instalación

---

## 📚 Referencias Oficiales

- **Blackmagic Design — soporte y manuales**: https://www.blackmagicdesign.com/support/
- **DaVinci Resolve — página de producto**: https://www.blackmagicdesign.com/products/davinciresolve
- **Blackmagic Design Training** (guías y footage oficiales): https://www.blackmagicdesign.com/products/davinciresolve/training
- **Foro oficial de DaVinci Resolve**: https://forum.blackmagicdesign.com/
- **SDK de scripting**: incluido en la instalación de Resolve, `Developer/Scripting/README.txt`
- **EBU R 128** (loudness): https://tech.ebu.ch/publications/r128
- **ITU-R BT.709 / BT.2100**: https://www.itu.int/rec/R-REC-BT/en

---

## 🔗 Enlaces Importantes

- **Repositorio**: https://github.com/ergrato-dev/bc-davinci-resolve
- **Documentación general**: [docs/README.md](../docs/README.md)
- **Primera semana**: [bootcamp/week-01-fundamentos_de_imagen_en_movimiento/README.md](../bootcamp/week-01-fundamentos_de_imagen_en_movimiento/README.md)

---

## ✅ Checklist para Nuevas Semanas

- [ ] Estructura de carpetas completa
- [ ] `README.md` con las 10 secciones obligatorias (incluida `🎩 Trucos y atajos`)
- [ ] Teoría en `1-teoria/`, un archivo por concepto (~250 líneas cada uno)
- [ ] Cada término técnico nuevo definido en su primera aparición
- [ ] Prácticas con forma de verificación en cada paso y rutas de menú completas
- [ ] Funciones Studio marcadas con su alternativa en Free
- [ ] Proyecto que añade una capa al proyecto hilo conductor
- [ ] `checks.json` con las verificaciones automáticas
- [ ] Recursos en las tres subcarpetas, cada uno con su justificación
- [ ] Glosario A-Z con el término inglés de la UI entre paréntesis
- [ ] `rubrica-evaluacion.md` con cuestionario + respuestas en `<details>`
- [ ] Trucos replicados en `docs/trucos-resolve.md`
- [ ] SVG con la paleta del bootcamp, todos enlazados
- [ ] Navegación anterior/siguiente correcta
- [ ] `./scripts/verificar-enlaces.sh` sin errores
- [ ] Rutas de menú comprobadas contra Resolve 21 de verdad, no deducidas

---

## 💡 Notas Finales

- **Prioridad**: profundidad sobre cobertura
- **Enfoque**: operar Resolve, no leer sobre Resolve
- **Objetivo**: formar postproductores, no espectadores de tutoriales
- **Filosofía**: si no se puede verificar —por API o por un criterio observable
  escrito—, no es un entregable

---

_Última actualización: agosto de 2026_
_Versión: 1.0 · Verificado contra DaVinci Resolve 21.0.4.5_
