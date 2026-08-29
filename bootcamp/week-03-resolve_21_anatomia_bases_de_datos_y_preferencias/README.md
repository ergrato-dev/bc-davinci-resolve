# Semana 03 — Resolve 21: anatomía, bases de datos y preferencias

> Tu trabajo vive en tres sitios distintos, y ninguno es el que crees. Esta semana
> averiguas cuáles son, dónde están en tu disco, cómo se respaldan y qué pasa el día que
> algo se rompa. Es la semana menos vistosa del bootcamp y la que más veces vas a
> agradecer.

Con esta semana se cierra la **Fase 0**. Al terminarla, tu proyecto tiene identidad
técnica, entorno configurado y red de seguridad, y está listo para recibir material de
verdad a partir de la Semana 04.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Explicar** las tres capas —biblioteca, proyecto y medios— y qué guarda cada una
- **Localizar** en tu disco tu biblioteca de proyectos, tus preferencias y tus respaldos
- **Distinguir** los tres tipos de biblioteca y saber cuándo hace falta cada uno
- **Manejar** el Project Manager: carpetas, búsqueda, exportar, archivar y borrar
- **Diferenciar** `Export Project`, *Project Archive* y *Project Backups*
- **Configurar** Live Save y los respaldos automáticos con criterio, no por defecto
- **Aplicar** sin dudar la regla que separa Preferences de Project Settings
- **Colocar** las tres carpetas de trabajo del proyecto donde tú decidas
- **Recuperar** espacio en disco sin perder ni una decisión
- **Comprobar** en tu propia instalación qué es Free y qué es Studio

---

## 📋 Prerrequisitos

- [Semana 02](../week-02-codecs_contenedores_y_flujo_de_datos/README.md) cerrada: bin
  `BC-Formatos` con sus cuatro clips y los siete checks en verde
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde `Workspace > Scripts > Utility`
- La estructura `BC-Resolve/` en tu disco de trabajo, con `02-cache/` y `04-respaldos/`
- Espacio libre suficiente para un *Project Archive* del material que tengas ahora
  mismo, que son cuatro archivos. Si vas muy justo, ese paso es opcional
- **No hace falta material nuevo** esta semana

---

## 🗂️ Estructura de la Semana

```
week-03-resolve_21_anatomia_bases_de_datos_y_preferencias/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 8 diagramas
├── 1-teoria/                    # 8 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # el entorno de tu proyecto, y el cierre de la Fase 0
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · El modelo de datos de Resolve](1-teoria/01-el-modelo-de-datos-de-resolve.md) | Biblioteca, proyecto y medios; referencias y clips *offline* | 30 min |
| [02 · Bibliotecas de proyectos](1-teoria/02-bibliotecas-de-proyectos.md) | Local, en red sobre PostgreSQL y en la nube; cuál conviene | 30 min |
| [03 · El Project Manager](1-teoria/03-el-project-manager.md) | Carpetas, búsqueda, exportar, archivar, borrar y Dynamic Project Switching | 30 min |
| [04 · Copias de seguridad](1-teoria/04-copias-de-seguridad.md) | Live Save, respaldos automáticos, `.drp` y `.dra`; qué cubre cada uno | 30 min |
| [05 · Preferences: los ajustes de tu ordenador](1-teoria/05-preferences-los-ajustes-de-tu-ordenador.md) | `System` y `User`, Media Storage, qué pide reiniciar y dónde vive todo | 30 min |
| [06 · Project Settings: los ajustes de tu vídeo](1-teoria/06-project-settings-los-ajustes-de-tu-video.md) | Master Settings, el ajuste irreversible, y los presets de proyecto | 30 min |
| [07 · Dónde escribe Resolve](1-teoria/07-donde-escribe-resolve.md) | Caché, galería, proxies; regenerable frente a irrecuperable | 30 min |
| [08 · El espacio de trabajo](1-teoria/08-el-espacio-de-trabajo.md) | Paneles, layouts, el menú Scripts y el mapa de Free frente a Studio | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · El mapa de tu instalación](2-practicas/01-el-mapa-de-tu-instalacion.md) | Localizas tu biblioteca, tus preferencias y tus respaldos, y los anotas | 45 min |
| [02 · El Project Manager y dos proyectos](2-practicas/02-project-manager-y-dos-proyectos.md) | Creas un segundo proyecto a 25 fps y compruebas qué ajustes son de quién | 45 min |
| [03 · Copias de seguridad de verdad](2-practicas/03-copias-de-seguridad-de-verdad.md) | Configuras las cuatro protecciones y **restauras** tu respaldo para probarlo | 45 min |
| [04 · Preferences y carpetas de trabajo](2-practicas/04-preferences-y-carpetas-de-trabajo.md) | Colocas Media Storage y las Working Folders, y ves aparecer `CacheClip` | 45 min |

### Proyecto

Dejas escrito dónde vive cada pieza de tu proyecto y qué harías si mañana el disco no
arrancara. Y cierras la Fase 0.
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

**Nada.** Todo lo de esta semana funciona en DaVinci Resolve Free: las bibliotecas
locales, el Project Manager entero, los respaldos, el archivado y todas las preferencias.

Aparecen dos funciones de pago, y ninguna afecta a un entregable:

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **Modo de colaboración** multiusuario sobre una biblioteca en red | [Teoría 02](1-teoria/02-bibliotecas-de-proyectos.md) | Pasarse el proyecto exportado (`.drp`). Se trata a fondo en la Semana 30 |
| **Scripting externo**, desde una terminal | [Teoría 08](1-teoria/08-el-espacio-de-trabajo.md) | Lanzar el script desde `Workspace > Scripts`, que sí funciona en Free. Es la vía que usa el verificador del bootcamp |

Esta es además la semana en la que **lees entero**
[`docs/free-vs-studio.md`](../../docs/free-vs-studio.md) y anotas, para tu pieza
concreta, qué tres funciones de Studio echarías de menos y cuál es su alternativa. Es un
criterio de la rúbrica.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Volver al Project Manager sin cerrar el proyecto | El icono de casa de la esquina inferior derecha, o `File > Project Manager` |
| Copiar una timeline o un nodo de un proyecto a otro | `File > Dynamic Project Switching`, copia en uno, salta y pega en el otro. Apágalo al terminar |
| No volver a pulsar `Ctrl+S` nunca más | `Preferences > User > Project Save and Load`, activa Live Save |
| Darte una semana de historia en vez de dos días | En ese mismo panel, sube el número de copias diarias de respaldo a 7 o más |
| Comprobar que un respaldo sirve de verdad | Crea una biblioteca de disco aparte, importa ahí el `.drp` y ábrelo. Un respaldo sin probar es una suposición |
| Recuperar decenas de GB en diez segundos | `Playback > Delete Render Cache > All`. La caché es regenerable por definición |
| Reconocer un disco donde ha trabajado Resolve | Busca las carpetas `CacheClip` y `.gallery` |
| Volver a las preferencias de fábrica sin perder nada | Con Resolve **cerrado**, renombra la carpeta `Preferences`. Si no era eso, deshaz el renombrado |
| Que los proyectos nuevos nazcan bien configurados | `Project Settings > Presets`: guarda el tuyo y ponlo por defecto |

---

## 📌 Entregables

1. ✅ `mapa-de-instalacion.md` en `04-respaldos/`, con sus seis rutas y la lista de lo
   que no viaja
2. ✅ `plan-de-continuidad.md` con las cuatro preguntas respondidas con acciones
   concretas
3. ✅ Proyecto **`BC-Pruebas-semana03`** creado en la raíz de tu biblioteca, a 25 fps
4. ✅ `BC-Bootcamp-Resolve` intacto: **24 fps** de timeline y **24 fps** de reproducción
5. ✅ Live Save y respaldos automáticos activados, fuera del disco del sistema, con 7 o
   más copias diarias
6. ✅ Las tres **Working Folders** apuntando a `BC-Resolve/02-cache/`
7. ✅ `CacheClip/` y `.gallery/` existiendo de verdad en esa carpeta
8. ✅ El `.drp` de la semana **restaurado y comprobado** en una biblioteca aparte
9. ✅ Respaldo `BC-Bootcamp-Resolve-semana03.drp` y respaldo de cierre de fase
   `BC-Bootcamp-Resolve-fase0.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 03
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, el Project Manager en la **raíz de
tu biblioteca original** y el puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan los siete checks a la vez, no repases siete cosas: casi siempre es que te
> quedaste en la biblioteca de pruebas de la práctica 03, o con `BC-Pruebas-semana03`
> abierto.

Si algo falla antes de eso:

```bash
python scripts/verificar-semana.py --doctor
```

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 02](../week-02-codecs_contenedores_y_flujo_de_datos/README.md) | **Semana 03** | [Semana 04](../week-04-media_page_ingesta_y_organizacion/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
