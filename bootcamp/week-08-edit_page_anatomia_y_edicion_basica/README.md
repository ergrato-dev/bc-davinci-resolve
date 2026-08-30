# Semana 08 — Edit page: anatomía y edición básica

> Tu montaje existe y se puede ver. Lo que no sabes todavía es decirle a Resolve **exactamente**
> dónde va cada plano, en qué pista, y qué le tiene que pasar a todo lo demás cuando entre. Eso
> es la Edit page, y es lo que hace posible todo lo que viene después.

Con esta semana se abre la **Fase 3**. Es la base de las cuatro semanas siguientes: el trimming,
la velocidad, los títulos y el multicámara dan por sabido lo que se aprende aquí.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Decidir** en qué página se hace cada cosa, con una regla de una frase
- **Reconocer** las cinco zonas de la Edit page y los controles de su barra de herramientas
- **Trabajar** con los dos visores sin confundir dónde marcas cada punto
- **Leer** los siete controles de una cabecera de pista y saber qué rompe cada uno
- **Dirigir** un clip a la pista que quieras con el `Source Track Selector`
- **Crear** una timeline con los ajustes correctos y las pistas nombradas
- **Montar** con edición de tres puntos, incluida la edición hacia atrás
- **Elegir** entre los siete modos de edición sabiendo qué le hace cada uno a la pieza
- **Comparar** tu escena montada en la Cut page con la misma escena montada en Edit

---

## 📋 Prerrequisitos

- [Semana 07](../week-07-cut_page_acabado_y_quick_export/README.md) cerrada: los nueve checks en
  verde y `BC-Montaje-v2` acabada de principio a fin
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde `Workspace > Scripts > Utility`
- El respaldo **`04-respaldos/BC-Bootcamp-Resolve-semana07.drp`**. Si no está, expórtalo antes de
  empezar
- **Auriculares**, para la revisión de la práctica 04
- **Material nuevo**: ninguno. La escena de esta semana se monta con lo que ya tienes en los bins
  `01-Basicos` … `10-Descartes`

> [!IMPORTANT]
> Si tu montaje de la Semana 07 no llega al final, cierra primero aquella semana. Esta no lo
> bloquea —se trabaja sobre una timeline nueva—, pero la comparación de la práctica 04, que es
> medio entregable, necesita las dos versiones de la misma escena.

---

## 🗂️ Estructura de la Semana

```
week-08-edit_page_anatomia_y_edicion_basica/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu escena montada con precisión
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · Por qué existe la Edit page](1-teoria/01-por-que-existe-la-edit-page.md) | Qué añade sobre la Cut page y la regla que decide | 30 min |
| [02 · Anatomía de la Edit page](1-teoria/02-anatomia-de-la-edit-page.md) | Las cinco zonas, la barra de herramientas y los cuatro modos | 30 min |
| [03 · Los dos visores](1-teoria/03-los-dos-visores.md) | Origen y timeline, el foco, y por qué no coinciden | 30 min |
| [04 · La timeline y sus pistas](1-teoria/04-la-timeline-y-sus-pistas.md) | Los siete controles de la cabecera, y bloquear frente a apagar | 30 min |
| [05 · El selector de pistas de origen](1-teoria/05-el-selector-de-pistas-de-origen.md) | Azul y rojo: qué entra y dónde | 30 min |
| [06 · Crear timelines y sus ajustes](1-teoria/06-crear-timelines-y-sus-ajustes.md) | El diálogo campo a campo, heredar o no, y los respaldos | 30 min |
| [07 · La edición de tres puntos](1-teoria/07-la-edicion-de-tres-puntos.md) | Los cuatro puntos, las cinco reglas y el backtiming | 30 min |
| [08 · Los modos de edición](1-teoria/08-los-modos-de-edicion.md) | Los siete, y qué le hace cada uno al resto de la pieza | 30 min |
| [09 · Arrastrar y el overlay del visor](1-teoria/09-arrastrar-y-el-overlay-del-visor.md) | El overlay, el imán, el enlace y el bloqueo de posición | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · La Edit page sobre tu montaje](2-practicas/01-la-edit-page-sobre-tu-montaje.md) | Recorres la página con tu pieza delante y nombras sus pistas | 50 min |
| [02 · La timeline de la escena](2-practicas/02-la-timeline-de-la-escena.md) | Creas `BC-Escena-v1`, la estructuras y montas los tres primeros planos | 50 min |
| [03 · Tres puntos y los modos de edición](2-practicas/03-tres-puntos-y-los-modos-de-edicion.md) | Completas la escena usando los cinco modos, con motivo escrito | 65 min |
| [04 · Cerrar la escena y verificar](2-practicas/04-cerrar-la-escena-y-verificar.md) | Limpias, comparas con la versión de Cut, anotas y respaldas | 45 min |

### Proyecto

Una escena de tu pieza montada con precisión, con estructura de pistas nombrada, y la comparación
escrita entre montarla en Cut y montarla en Edit.
→ [3-proyecto/README.md](3-proyecto/README.md)

---

## ⏱️ Distribución del Tiempo (10 horas)

| Actividad | Tiempo |
| --------- | ------ |
| Teoría (9 archivos × 30 min) | 4 h 30 min |
| Prácticas (4, entre 45 y 65 min) | 3 h 30 min |
| Proyecto | 1 h |
| Recursos y glosario | 30 min |
| Autoevaluación | 30 min |
| **Total** | **10 h** |

> [!NOTE]
> La práctica que más se desborda es la 03, y siempre por lo mismo: probar modos de edición sobre
> planos que no lo necesitan. Cada paso pide **un** uso de cada modo. Si llevas veinte minutos con
> el `Fit to Fill`, estás experimentando en vez de montar.

---

## 💠 Qué necesita Studio esta semana

**Nada.** La Edit page entera, los dos visores, el selector de pistas de origen, los siete modos
de edición, los ajustes por timeline y los respaldos funcionan en DaVinci Resolve Free.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **`Text Based Editing`** | El capítulo 47 del manual, junto a los de esta semana | No se usa esta semana. Necesita transcripción, que es Studio; el montaje por tres puntos es la vía en Free |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free |

Ningún entregable evaluable de esta semana depende de Studio.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Decidir en qué página trabajar | ¿La frase menciona una pista o un fotograma? Si sí, Edit |
| Comprobar que Cut y Edit son la misma timeline | Mueve el cabezal en una y cambia con `Shift+3` / `Shift+4` |
| Ver la timeline entera y volver al detalle | `Shift+Z` |
| Recuperar la pantalla cuando se ha desordenado | `Workspace > Reset UI Layout` |
| Guardar tu disposición de paneles | `Workspace > Layout Presets > Save Layout As Preset` |
| Volver al modo normal desde cualquier modo | `A` |
| Encontrar un corte por su número | `Index > Edit Index`, doble clic en la línea |
| Manejar muchas pistas sin marearse | `Index > Tracks` |
| Cambiar de visor sin ratón | `Q` |
| Limpiar los puntos antes de cada edición | `Alt+X` (Win) / `Opt+X` (Mac) |
| Ver cuánto dura lo que has marcado | El campo de duración del visor |
| Marcar por sonido y no por imagen | Menú de tres puntos `> Show Full Clip Audio Waveform` |
| Ver la pieza a pantalla completa | `Workspace > Viewer Mode > Cinema Viewer`, atajo `P` |
| Recorrer un clip a la velocidad del gesto | Mantén `C` y mueve el ratón sobre el visor |
| Llevar el cabezal donde está el ratón | `C` sobre la timeline |
| Saltar de corte en corte | Flecha arriba y flecha abajo |
| Bloquear o desbloquear todas las pistas de vídeo | `Alt+Shift+9` (Win) / `Opt+Shift+9` (Mac) |
| Poner varias cabeceras en el mismo estado | Clic sobre un control y arrastra hacia arriba o abajo |
| Limpiar una timeline llena de pistas vacías | Clic derecho en la cabecera `> Delete Empty Tracks` |
| Mandar el vídeo a una pista sin ratón | `Alt+1` … `Alt+8` (Win) / `Opt+1` … `Opt+8` (Mac) |
| Mandar el audio a una pista sin ratón | `Alt+Ctrl+1` … `8` (Win) / `Opt+Cmd+1` … `8` (Mac) |
| Editar un plano sin su sonido | Apaga el icono de audio del origen |
| Elegir qué canal de audio de un clip usar | Clic derecho sobre el icono de audio azul |
| Salir de cualquier lío de destinos | `Timeline > Source Track Selector > Reset Track Selectors` |
| Crear una timeline sin menús | `Ctrl+N` (Win) / `Cmd+N` (Mac) |
| Que la timeline caiga donde quieres | Selecciona el bin **antes** de crearla |
| Tener todas las timelines a la vista | `Preferences > User > Editing > Smart Bin for Timelines` |
| Marcar un punto seguro antes de un cambio grande | `File > Create Timeline Backup` |
| Recuperar una timeline de hace dos horas | Clic derecho `> Restore Timeline Backup` |
| Llevarte solo un montaje a otro proyecto | Exporta un `.drt` |
| Colocar un plano por su final | Marca solo la `O` en la timeline |
| Llenar un hueco exacto | `I` y `O` en la timeline, solo `I` en el origen |
| Meter algo sin comerte nada | `F9`, y comprueba las pistas de encima |
| Sincronizar una acción con un fotograma | `F11`, con los dos cabezales colocados |
| Poner un rótulo encima sin crear la pista a mano | `F12` |
| Ver todos los modos a la vez | Arrastra el clip sobre el visor de timeline |
| Insertar arrastrando | `Ctrl+Shift` (Win) / `Cmd+Shift` (Mac) mientras arrastras |
| Saltarte el imán solo esta vez | `N` mientras estás arrastrando |
| Separar audio de vídeo puntualmente | `Alt` (Win) / `Opt` (Mac) al hacer clic |
| Entender la diferencia entre dos modos | Haz uno, mira, `Ctrl+Z`, haz el otro |
| Comprobar cualquier atajo en tu instalación | `DaVinci Resolve > Keyboard Customization`, busca el comando por nombre |

---

## 📌 Entregables

1. ✅ **`BC-Montaje-v2`** conservada, con sus pistas nombradas
2. ✅ Timeline **`BC-Escena-v1`**, abierta, creada desde `Master`
3. ✅ **2+** pistas de vídeo y **3+** de audio, todas con nombre propio
4. ✅ **8+** clips en `Continuidad`, sin huecos ni solapes
5. ✅ Recursos en `Recursos`, puestos con `Place on Top`
6. ✅ Sonido de recurso en `Ambiente`, sin su imagen
7. ✅ Un uso escrito y justificado de `Insert`, `Replace`, `Fit to Fill` y `Place on Top`
8. ✅ La comparación entre la versión de Cut y la de Edit, contestada por escrito
9. ✅ `notas-de-montaje.md` con el apartado `## Edit page — Semana 08` cerrado
10. ✅ Respaldo `BC-Bootcamp-Resolve-semana08.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 08
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Escena-v1` como timeline abierta** y el
puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan **`escena-v1-activa`, `escena-v1-clips`, `escena-v1-sin-huecos`, `escena-v1-pistas` y
> `escena-v1-pistas-con-nombre` a la vez**, casi seguro tienes abierta `BC-Montaje-v2`: los cinco
> leen la timeline activa. Doble clic en `BC-Escena-v1` y repite.
>
> Si fallan **todos**, el puente no está lanzado.

Si algo falla antes de eso:

```bash
python scripts/verificar-semana.py --doctor
```

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 07](../week-07-cut_page_acabado_y_quick_export/README.md) | **Semana 08** | [Semana 09](../week-09-trimming_quirurgico/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
