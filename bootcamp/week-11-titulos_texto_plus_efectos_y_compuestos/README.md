# Semana 11 — Títulos, Text+, efectos y compuestos

> Tu montaje está afinado al fotograma, con la velocidad y el encuadre decididos. Y sigue sin
> entenderse del todo: nadie sabe quién habla, ni dónde estamos, ni cómo se titula esto. Esta semana
> añade **la información que la imagen no da**, y las herramientas que la sostienen: rótulos,
> transiciones, efectos y contenedores.

Cuarta semana de la **Fase 3**. La Semana 10 te enseñó a decidir cuánto dura y qué enseña cada
plano; esta te enseña a decidir **qué se lee encima**, qué separa un plano del siguiente y cómo se
trata un bloque entero de una vez.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Explicar** por qué un título es un clip y qué le pasa si lo pones en la pista equivocada
- **Elegir** entre `Text`, `Text+`, `MultiText` y un `Fusion Title` con un criterio, no por costumbre
- **Manejar** los cuatro paneles de `Text+` sin buscar: `Text`, `Layout`, `Transform` y `Shading`
- **Construir** un rótulo que se lea sobre cualquier fondo, con contorno y sombra
- **Colocar** todo el texto dentro del título seguro, y proteger otras relaciones de aspecto
- **Guardar** un estilo de rótulo y reutilizarlo en treinta segundos por rótulo
- **Decidir** si un corte pide una transición, y con qué alineación
- **Resolver** un jump cut con `Smooth Cut` y saber para qué material funciona
- **Encontrar** un efecto entre quince categorías de ResolveFX, y dosificarlo con `Blend`
- **Aplicar** un efecto a un tramo entero con un adjustment clip, sabiendo a qué afecta
- **Empaquetar** un bloque en un compound clip, y saber qué cuesta en la Fase 5

---

## 📋 Prerrequisitos

- [Semana 10](../week-10-velocidad_transformaciones_y_estabilizacion/README.md) cerrada: los diez
  checks en verde
- **`BC-Montaje-v4` terminada de principio a fin.** Esta semana rotula un montaje resuelto, no una
  timeline de prueba
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde `Workspace > Scripts > Utility`
- El respaldo **`04-respaldos/BC-Bootcamp-Resolve-semana10.drp`**. Si no está, expórtalo antes de
  empezar
- **Una tipografía instalada en tu sistema** que te sirva: sans-serif, con al menos un corte medio y
  uno negrita. Si no tienes ninguna clara, [Google Fonts](https://fonts.google.com/) es la fuente con
  licencia abierta
- **Material nuevo**: ninguno

> [!IMPORTANT]
> Esta semana **no se remonta**. El check `montaje-v5-clips` pide quince clips o más en la pista de
> vídeo 1, y hay dos formas de perderlos sin querer: arrastrar un título sobre la `V1`, que
> sobrescribe el plano de debajo, y empaquetar medio montaje en compound clips, que cuentan como un
> clip. Las dos tienen su aviso en su sitio.

---

## 🗂️ Estructura de la Semana

```
week-11-titulos_texto_plus_efectos_y_compuestos/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu pieza rotulada
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · El título es un clip](1-teoria/01-el-titulo-es-un-clip.md) | Generadores, canal alpha, orden de pistas y los dos paneles del Inspector | 30 min |
| [02 · Text frente a Text+](1-teoria/02-text-frente-a-text-plus.md) | Los siete generadores de título, el rich text y la pregunta que decide | 30 min |
| [03 · Los cuatro paneles de Text+](1-teoria/03-los-cuatro-paneles-de-text-plus.md) | `Text`, `Layout`, `Transform` y `Shading`, y qué vive en cada uno | 30 min |
| [04 · Fusion Titles y plantillas](1-teoria/04-fusion-titles-y-plantillas.md) | Qué es un macro, qué te deja tocar y qué le cuesta a tu reproducción | 30 min |
| [05 · Legibilidad: safe areas, tipografía y contraste](1-teoria/05-legibilidad-safe-areas-y-contraste.md) | Dónde va, con qué tipografía y contra qué fondo. Y cómo guardar el estilo | 30 min |
| [06 · Transiciones a fondo](1-teoria/06-transiciones-a-fondo.md) | Colas, las cinco formas de colocarlas, alineación, `Ease` y `Smooth Cut` | 30 min |
| [07 · Las categorías de ResolveFX](1-teoria/07-las-categorias-de-resolvefx.md) | El árbol de la `Effects Library`, las quince categorías, `Blend` y Studio | 30 min |
| [08 · Adjustment clips](1-teoria/08-adjustment-clips.md) | Un efecto en un sitio para diez planos, y a qué afecta exactamente | 30 min |
| [09 · Compound clips y nesting](1-teoria/09-compound-clips-y-nesting.md) | Empaquetar un bloque, el control de ruta, y qué cuesta en la Fase 5 | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · La copia y el mapa de rótulos](2-practicas/01-la-copia-y-el-mapa-de-rotulos.md) | Creas `BC-Montaje-v5`, preparas las pistas, enciendes las guías y marcas la pieza | 45 min |
| [02 · El título principal y los rótulos](2-practicas/02-el-titulo-principal-y-los-rotulos.md) | Construyes un rótulo legible, lo guardas y lo reutilizas | 60 min |
| [03 · Transiciones y ResolveFX](2-practicas/03-transiciones-y-resolvefx.md) | Transiciones con y sin colas, `Smooth Cut`, un filtro y un adjustment clip | 60 min |
| [04 · Compuestos y cierre](2-practicas/04-compuestos-y-cierre.md) | Un compound clip con motivo, la comparación y el respaldo | 45 min |

### Proyecto

Tu pieza rotulada, con el estilo guardado, las transiciones que pedía y ninguna más, un adjustment
clip y un compuesto con su motivo escrito.
→ [3-proyecto/README.md](3-proyecto/README.md)

---

## ⏱️ Distribución del Tiempo (10 horas)

| Actividad | Tiempo |
| --------- | ------ |
| Teoría (9 archivos × 30 min) | 4 h 30 min |
| Prácticas (4, entre 45 y 60 min) | 3 h 30 min |
| Proyecto | 1 h |
| Recursos y glosario | 30 min |
| Autoevaluación | 30 min |
| **Total** | **10 h** |

> [!NOTE]
> La práctica que más se desborda es la 02, y siempre por lo mismo: se empieza a probar fuentes. Con
> media hora de `Font Browser` no sale un rótulo mejor, sale el mismo rótulo media hora después.
> Elige una sans-serif legible, construye el rótulo entero con contorno y sombra, y **guárdalo**. Si
> luego quieres cambiar la fuente, se cambia en el estilo guardado y se recolocan los rótulos en
> cinco minutos.

---

## 💠 Qué necesita Studio esta semana

Esta semana toca la categoría con más funciones de pago de todo el bootcamp: **muchos ResolveFX son
exclusivos de Studio**. Ninguna es un entregable.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **`Resolve FX Sharpen` al completo** | Teoría 07 | Los tres son de Studio. En Free, el enfoque llega en la Semana 20 desde la paleta `Blur` de la página Color |
| **`CineFocus`, `Lens Blur`** | Teoría 07, categoría `Blur` | `Gaussian Blur` y `Box Blur`, que están en Free y son los que usa la práctica 03 |
| **`Film Grain`, `Film Look Creator`, `Halation`, `Camera Shake`** | Teoría 07, categoría `Film Emulation` | `Fast Noise` y `JPEG Damage` de `Texture`, y `Glow` de `Light`, todos en Free |
| **`Lens Flare`, `Lens Reflections`, `Aperture Diffraction`** | Teoría 07, categoría `Light` | `Glow` y `Light Rays`, que están en Free |
| **`Warper`, `Lens Distortion`** | Teoría 07, categoría `Warp` | `Dent`, `Ripples`, `Vortex` y `Waviness`, en Free |
| **`Match Move`, `Surface Tracker`** | Teoría 07, categoría `Transform` | Keyframes de `Transform`, que es lo que hiciste en la Semana 10 |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free |

> [!NOTE]
> Un caso que conviene mirar en tu instalación: **`Smooth Cut`**. El manual **no** lo marca como
> función de Studio, pero desde la versión 20 usa un motor de `Speed Warp` con inteligencia
> artificial, y `Speed Warp` sí es de Studio cuando se usa en un retime. Su Inspector trae una
> casilla `Speed Warp` que, al desmarcarla, vuelve al método anterior por flujo óptico. Si en tu
> Free esa casilla no aparece, la transición sigue funcionando: anótalo y sigue.
>
> *Comportamiento documentado en el manual de la 21.0.4.5; no verificado en Free, agosto de 2026.*

Ningún entregable evaluable de esta semana depende de Studio: el efecto de la práctica 03 es un
`Gaussian Blur`. La comparativa oficial de funciones está en
<https://www.blackmagicdesign.com/products/davinciresolve/studio>.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Abrir el panel de efectos | El botón `Effects` de la barra de herramientas |
| Buscar cualquier efecto, título o transición por nombre | `Shift+Espacio`, y escribe |
| Buscar por categoría | Escribe el nombre de la categoría, por ejemplo `Stylize` |
| Previsualizar sin colocar | `Hover Scrub Preview` marcado, y pasa el ratón por la miniatura |
| Previsualizar una plantilla animada | Lo mismo, pero moviendo el ratón **a lo largo** de la miniatura |
| Añadir una pista de vídeo encima de otra | Clic derecho en su cabecera `>` `Add Track` |
| Añadir varias y elegir dónde | Clic derecho en la zona de cabeceras `>` `Add Tracks` |
| Quitar las pistas vacías que sobran | Clic derecho `>` `Delete Empty Tracks` |
| Colocar un generador con la duración exacta | `I`, `O`, control de destino en la pista, y arrastra al overlay del visor |
| Cambiar la duración de fábrica de los generadores | `DaVinci Resolve > Preferences > User > Editing` |
| Fundir un rótulo sin abrir el Inspector | Las asas de fundido de las esquinas superiores del clip |
| Abrir el Inspector de un generador o una transición | Doble clic sobre él en la timeline |
| Dar un estilo distinto a una línea | Selecciónala dentro del campo `Text` **antes** de tocar nada |
| Editar el texto en el visor | Doble clic sobre el texto |
| Editar un `Text+` en el visor | Desplegable de overlays del visor `>` `Fusion Overlay` |
| Restringir el arrastre de un texto a un eje | Mantén `Shift` |
| Soltar los imanes al colocar un texto | Mantén `Alt` (Win) / `Opt` (Mac) mientras arrastras |
| Cambiar la velocidad de unos créditos | Estira o acorta el clip de `Scroll` |
| Elegir fuente viendo cómo queda | El icono del `Font Browser` junto al desplegable de fuente |
| Que el tamaño del texto no dependa de la resolución | Usa `Text+`: su `Size` ya es relativo al ancho de la imagen |
| Que un contorno no engorde la letra | `Outside Only` marcado |
| Esquinas de contorno limpias en cuerpo pequeño | `Join Style > Rounded` |
| Animar la aparición del texto | El **final** del rango `Write On`, de `1` a `0` |
| Animar cada letra por su cuenta | `Transform > Transform > Characters` |
| Meter un emoji en un `Text+` | `Tecla Windows + .` (Win) / `Control+Cmd+Espacio` (Mac) |
| Guardar un rótulo con su estilo y sus keyframes | Arrástralo de la timeline al media pool |
| Quitar los subrayados del corrector antes de enseñar la pieza | `View > Show Spelling Errors on Viewer` |
| Encender y apagar todas las guías de encuadre | `View > Safe Area > On/Off` |
| Ver el borde exacto del cuadro | `View > Safe Area > Extents` |
| Proteger otra relación de aspecto | `View > Safe Area > Aspect` y `View > Select Aspect Ratio` |
| Ver qué se perdería en vertical o en cuadrado | El icono de guías de encuadre del visor `>` `Social Media` |
| Juzgar si un rótulo contrasta | Entorna los ojos mirando el visor |
| Simular cómo se ve en un móvil | Reduce el visor a un cuarto y léelo |
| Medir cuánto tiene que durar un rótulo | Léelo en voz alta dos veces |
| Seleccionar el punto de edición más cercano | `V` |
| Elegir principio, centro o final de un punto de edición | `U`, que va rotando |
| Transición estándar de vídeo y audio | `Ctrl+T` (Win) / `Cmd+T` (Mac) |
| Solo vídeo | `Alt+T` (Win) / `Opt+T` (Mac) |
| Solo audio | `Shift+T` |
| Cuatro duraciones sin abrir nada | Clic derecho sobre el punto de edición |
| La misma transición en diez cortes | Selecciona los puntos, clic derecho en la transición `>` `Add to Selected Edit Points` |
| Crear a mano el solape que falta | `Alt+Shift` (Win) / `Opt+Shift` (Mac) + arrastrar |
| Cambiar la duración de una transición con un número | `Ctrl+D` (Win) / `Cmd+D` (Mac) |
| Alargar solo un lado de la transición | `Ctrl` / `Cmd` mientras arrastras el borde |
| Copiar una transición a otro corte | `Alt` / `Opt` + arrastrar |
| Cambiar el tipo de transición sin borrarla | Arrastra otra encima |
| Seleccionar todas las transiciones | `Timeline > Select Transitions` |
| Cambiar cuál es la transición estándar | Clic derecho `>` `Set as Standard Transition` |
| Guardar tu transición ajustada | Clic derecho `>` `Create Transition Preset` |
| Que una disolución no se apague en el centro | `Style` en `Film` o en `Additive` |
| Dosificar cualquier ResolveFX | `Blend`, que lo tienen todos |
| Ver qué clips llevan efectos | Se pintan de un tono más oscuro |
| Cambiar el orden en el que se aplican dos filtros | Las flechas de la barra de título del filtro |
| Comparar un clip con y sin sus efectos | El interruptor de la barra de título del filtro |
| Abrir o cerrar todos los filtros de un clip | `Alt` (Win) / `Opt` (Mac) + clic en una barra de título |
| Encender los controles en pantalla de un efecto | Desplegable de overlays del visor `>` `OFX` |
| Copiar efectos de un clip a otros | `Ctrl+C` y `Edit > Paste Attributes` — `Alt+V` / `Opt+V` |
| Quitar efectos de varios clips | `Edit > Remove Attributes` |
| Ver los efectos retirados de versiones antiguas | Menú de tres puntos `>` `Show Legacy Resolve FX` |
| Incrustar los efectos de un clip en un archivo | Clic derecho `>` `Render in Place` |
| Deshacerlo | Clic derecho `>` `Decompose to Original` |
| Apagar y encender un clip entero | `D`, o `Clip > Enable/Disable Clip` |
| Empaquetar clips enteros | Selecciónalos `>` clic derecho `>` `New Compound Clip` |
| Empaquetar exactamente un rango | `I`, `O` `>` clic derecho `>` `Convert In and Out to Compound Clip` |
| Decidir en qué bin cae el compuesto | Selecciona el bin **antes** de crearlo |
| Entrar a editar un compuesto | Clic derecho `>` `Open in Timeline` |
| Saber si estás dentro de un compuesto | El control de ruta de la esquina inferior izquierda |
| Salir | Doble clic sobre el nombre de la timeline que lo contiene |
| Deshacer un compuesto | Clic derecho `>` `Decompose in Place` |
| Recuperar la reproducción con plantillas y efectos | `Playback > Render Cache > Smart` |
| Comprobar cualquier atajo en tu instalación | `Alt+Ctrl+K` (Win) / `Opt+Cmd+K` (Mac) |

---

## 📌 Entregables

1. ✅ **`BC-Montaje-v4`** conservada e intacta
2. ✅ Timeline **`BC-Montaje-v5`**, abierta, duplicada de la anterior
3. ✅ **15+** clips en la pista de vídeo 1, sin huecos ni solapes
4. ✅ **3+** clips en la **`V2`**: el título de entrada y dos rótulos de identificación
5. ✅ Un estilo de rótulo propio guardado en el media pool
6. ✅ Las transiciones que la pieza pedía, con su alineación decidida, y **las descartadas
   justificadas por escrito**
7. ✅ Un adjustment clip en la **`V3`** con su efecto, su nombre y su `Blend`
8. ✅ Un compound clip con nombre `BC-Compuesto-…` y su motivo escrito
9. ✅ Bin **`13-Titulos`** con el estilo de rótulo y el compuesto
10. ✅ **3+** marcadores amarillos y **2+** verdes, todos con nombre propio
11. ✅ `notas-de-montaje.md` con el apartado `## Títulos y efectos — Semana 11` cerrado
12. ✅ Respaldo `BC-Bootcamp-Resolve-semana11.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 11
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Montaje-v5` como timeline abierta** y el
puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan **siete checks a la vez** —`montaje-v5-activa`, `montaje-v5-clips`,
> `montaje-v5-sin-huecos`, `rotulos-en-v2`, `capa-de-ajuste`, `marcadores-de-rotulo` y
> `marcadores-de-efecto`—, la timeline activa no es la que crees. Dos causas, las dos frecuentes
> esta semana:
>
> 1. Te quedaste comparando en `BC-Montaje-v4`
> 2. **Abriste un compound clip con `Open in Timeline` y no volviste.** Mira el control de ruta de
>    la esquina inferior izquierda de la timeline: si hay dos nombres, estás dentro
>
> Si fallan **`rotulos-en-v2` y `montaje-v5-clips` a la vez**, pusiste los títulos en la `V1` y se
> han comido planos: `Ctrl+Z` hasta antes de eso, o restaura el respaldo `antes-de-rotular`.
>
> Si falla solo **`capa-de-ajuste`**, el adjustment clip está en la `V2` o más abajo. Tiene que
> estar por encima de todo lo que quiere afectar.
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
| [Semana 10](../week-10-velocidad_transformaciones_y_estabilizacion/README.md) | **Semana 11** | [Semana 12](../week-12-multicam_subtitulos_y_gestion_de_timeline/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
