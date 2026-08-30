# Semana 10 — Velocidad, transformaciones y estabilización

> Tu montaje está afinado al fotograma. Lo que todavía no está decidido es **cuánto tiempo ocupa
> cada plano de verdad, qué parte del cuadro se ve, y si tiembla**. Esas tres son las tres capas de
> esta semana, y van en ese orden porque cada una cambia la imagen sobre la que trabaja la
> siguiente.

Tercera semana de la **Fase 3**. La Semana 09 te enseñó a decidir en qué fotograma empieza y acaba
un plano; esta te enseña a decidir a qué velocidad transcurre, qué encuadre enseña y con cuánto
pulso.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Calcular** el techo de cámara lenta de un plano con una división, antes de tocar nada
- **Distinguir** *judder*, *ghosting* y *warping* al verlos, y saber a qué método bajar
- **Elegir** entre las cuatro formas de cambiar la velocidad según el problema que tengas
- **Predecir** si un cambio de velocidad va a recolocar tu pieza o a pisar un plano
- **Congelar** un fotograma exacto y **invertir** un plano, sabiendo qué le pasa al audio
- **Construir** una rampa de velocidad con puntos y afinarla en la curva
- **Decidir** el `Retime Process` de cada clip mirando el tipo de movimiento que tiene
- **Reencuadrar** dentro del margen que da la resolución, y saber cuál es ese margen
- **Animar** cualquier parámetro con keyframes, y controlar su aceleración
- **Estabilizar** un plano eligiendo modo y `Strength`, y saber cuándo un plano no se estabiliza

---

## 📋 Prerrequisitos

- [Semana 09](../week-09-trimming_quirurgico/README.md) cerrada: los diez checks en verde
- **`BC-Montaje-v3` afinada de principio a fin.** Esta semana trabaja sobre el montaje afinado, no
  sobre una timeline de prueba
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde `Workspace > Scripts > Utility`
- El respaldo **`04-respaldos/BC-Bootcamp-Resolve-semana09.drp`**. Si no está, expórtalo antes de
  empezar
- **Espacio en disco para el caché.** `Optical Flow` calcula fotogramas nuevos y el
  `Render Cache` los guarda; cuenta con unos cuantos gigas
- **Material nuevo**: ninguno

> [!IMPORTANT]
> Si tu material está todo grabado a 24 o 25 fps, **no has hecho nada mal** y la semana funciona
> igual. Significa que tu trabajo va a ser de acelerados, freezes, transformaciones y
> estabilización, y que la cámara lenta la vas a usar poco. Ninguno de los diez entregables
> depende de tener material sobrecadenciado.

---

## 🗂️ Estructura de la Semana

```
week-10-velocidad_transformaciones_y_estabilizacion/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu pieza con velocidad y encuadre
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · El techo de la cámara lenta](1-teoria/01-el-techo-de-la-camara-lenta.md) | Cadencia de rodaje frente a cadencia de proyecto, y la división que manda | 30 min |
| [02 · Las cuatro formas de cambiar la velocidad](1-teoria/02-las-cuatro-formas-de-cambiar-la-velocidad.md) | Diálogo, Inspector, `Fit to Fill`, `Retime Controls`, y la casilla `Ripple Sequence` | 30 min |
| [03 · Freeze frame y reverse](1-teoria/03-freeze-frame-y-reverse.md) | Los dos retimes que cambian de estado, y qué le pasa al audio | 30 min |
| [04 · Velocidad variable: rampas y rewind](1-teoria/04-velocidad-variable-rampas-y-rewind.md) | Puntos de velocidad, las dos asas y los dos presets | 30 min |
| [05 · Las curvas de retime](1-teoria/05-las-curvas-de-retime.md) | `Retime Frame` y `Retime Speed`, y el control fino de la aceleración | 30 min |
| [06 · Cómo Resolve inventa los fotogramas que faltan](1-teoria/06-como-resolve-inventa-fotogramas.md) | `Nearest`, `Frame Blend`, `Optical Flow`, y qué es de Studio | 30 min |
| [07 · Transform, crop y dynamic zoom](1-teoria/07-transform-crop-y-dynamic-zoom.md) | Reencuadrar dentro del margen que da la resolución | 30 min |
| [08 · Keyframes: Inspector, Keyframe Editor y Curve Editor](1-teoria/08-keyframes-inspector-y-curve-editor.md) | Los tres sitios donde se anima cualquier parámetro | 30 min |
| [09 · Estabilización en la Edit page](1-teoria/09-estabilizacion-en-la-edit-page.md) | Los tres modos, los seis controles y lo que cuesta en píxeles | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · La copia y el mapa de velocidad](2-practicas/01-la-copia-y-el-mapa-de-velocidad.md) | Creas `BC-Montaje-v4`, anotas las cadencias de tu material y marcas la pieza | 45 min |
| [02 · Retimes lineales sobre tu montaje](2-practicas/02-retimes-lineales-sobre-tu-montaje.md) | Acelerados, cámaras lentas, un freeze al fotograma y `Fit to Fill` | 60 min |
| [03 · Velocidad variable y calidad de imagen](2-practicas/03-velocidad-variable-y-calidad-de-imagen.md) | Una rampa a mano, afinada en la curva, y la comparación de los tres métodos | 55 min |
| [04 · Transformaciones, keyframes y estabilización](2-practicas/04-transformaciones-keyframes-y-estabilizacion.md) | Estabilizas, reencuadras, animas un seguimiento y cierras la semana | 50 min |

### Proyecto

Tu pieza con tres cambios de velocidad reales, una rampa justificada, los planos que temblaban
estabilizados y la comparación escrita contra la versión de la Semana 09.
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
> La práctica que más se desborda es la 03, y siempre por lo mismo: se empieza a ajustar la rampa
> fotograma a fotograma. No hace falta. La práctica pide **una** rampa y **una** comparación de
> métodos: eso es lo que enseña la técnica. Afinar la rampa hasta el último fotograma es trabajo
> que se rehace en cuanto cambies algo alrededor.

---

## 💠 Qué necesita Studio esta semana

Esta semana **sí** toca funciones de pago, y por primera vez en la Fase 3. Ninguna es un
entregable.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **`Speed Warp`** y **`AI Speed Warp Metal`** | Teoría 06, `Motion estimation mode` | `Optical Flow` con `Enhanced Better`, y quedarse por encima del techo del plano |
| **`Lens Correction`** | Teoría 09, grupo del Inspector | Recortar y ampliar el centro del cuadro, que es donde menos deforma. O rodar con menos angular |
| **`Smart Reframe`** | Teoría 07, grupo `Transform` | Reencuadre animado con keyframes: es el paso 6 de la práctica 04 |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free |

Ningún entregable evaluable de esta semana depende de Studio. La comparativa oficial de funciones
está en <https://www.blackmagicdesign.com/products/davinciresolve/studio>.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Ver la cadencia de rodaje de todo el material de golpe | `Media Pool` en vista de lista, columna `FPS`, y ordena por ella |
| Saber cuántas veces estira un plano | Cadencia de rodaje ÷ cadencia de proyecto |
| Abrir o cerrar los controles de retime | `Ctrl+R` (Win) / `Cmd+R` (Mac) |
| Cerrar los controles sin deshacer nada | `Esc` |
| Congelar el clip entero | `Shift+R` |
| Colocar el cabezal al fotograma antes de congelar | `Flecha izquierda` y `Flecha derecha` |
| Rellenar un hueco con un plano que no da | `I`, `O` y `Shift+F11` |
| Usar el hueco que cruza el cabezal como destino | Borra los puntos con `Alt+X` (Win) / `Opt+X` (Mac) antes del `Fit to Fill` |
| Cambiar la velocidad de varios clips a la vez | Selecciónalos todos y `Clip > Change Clip Speed` |
| Poner una duración exacta en vez de un porcentaje | El campo `Duration` del diálogo o del Inspector |
| Que la voz no suene grave al ralentizar | Casilla `Pitch Correction` |
| Ver de un vistazo qué clips llevan velocidad | Los distintivos de retime, a la izquierda del nombre |
| Leer la velocidad sin abrir nada | Flechas juntas rápido, separadas y amarillas lento, a la izquierda reverse, barras rojas congelado |
| Añadir un punto de velocidad donde está el cabezal | Desplegable de velocidad `> Add Speed Point` |
| Rampa de cinco tramos en un clic | `Speed Ramp >` en cualquier desplegable de velocidad |
| Rebobinado automático | `Rewind >` y el porcentaje |
| Decidir dónde empieza el rebobinado | Coloca el cabezal dentro del tramo antes de aplicarlo |
| Borrar el punto de velocidad correcto | Abre el desplegable que está a su derecha y `Clear Speed Point` |
| Volver un clip al 100 % | `Reset to 100%` en el desplegable de velocidad |
| Quitar la velocidad conservando lo demás | `Edit > Remove Attributes`, con su casilla `Ripple Sequence` |
| Copiar un retime, un reencuadre o una estabilización a otro clip | `Edit > Paste Attributes` — `Alt+V` (Win) / `Opt+V` (Mac) |
| Abrir las curvas de retime | Pestaña `Keyframes` `>` icono de curvas `>` marca `Retime Speed` y `Retime Frame` |
| Añadir un punto a una curva | `Alt` (Win) / `Opt` (Mac) + clic sobre ella |
| Saber el porcentaje exacto de un tramo | Arrástralo en `Retime Speed` y lee el rótulo emergente |
| Comparar dos métodos de relleno sin parar | Bucle con `Ctrl+/` / `Cmd+/` y `/`, y cambia el desplegable mientras suena |
| Cambiar el `Retime Process` de un clip suelto | `Inspector > Video > Retime and Scaling` |
| Cambiarlo para todo el proyecto | `Project Settings > Master Settings > Frame Interpolation` |
| Saber si un clip hereda el ajuste del proyecto | Si pone `Project Settings`, hereda |
| Recuperar la reproducción en tiempo real | `Playback > Render Cache > Smart` |
| Poner el visor al 100 % para juzgar la nitidez | `Alt+Shift+Z` (Win) / `Opt+Shift+Z` (Mac) |
| Encajar la pieza entera en el ancho de la timeline | `Shift+Z` |
| Ampliar o reducir la timeline | `Ctrl+=` / `Ctrl+-` (Win) · `Cmd+=` / `Cmd+-` (Mac) |
| Escribir un valor exacto en un parámetro | Clic sobre el número y teclea |
| Devolver un grupo del Inspector a su valor de fábrica | El icono de reinicio a la derecha del nombre del grupo |
| Ampliar hacia una cara descentrada | Mueve el `Anchor Point` a la cara y luego sube el `Zoom` |
| Estirar o achatar la imagen a propósito | Suelta el enlace entre `Zoom X` y `Zoom Y` |
| Encender los controles gráficos del visor | El botón `Transform/Crop/Dynamic Zoom`, abajo a la izquierda |
| Elegir el modo de overlay por menú | `View > Viewer Overlay` |
| Encender y apagar el overlay que tengas | ``Shift+` `` |
| Restringir un arrastre de texto a un solo eje | Mantén `Shift` |
| Invertir el sentido de un dynamic zoom | El botón `Swap` |
| Que un dynamic zoom no parezca un efecto | `Dynamic Zoom Ease` en `Ease In and Out` |
| Poner un keyframe | El rombo a la derecha del parámetro en el Inspector |
| Saber si el cabezal está sobre un keyframe | El rombo está naranja |
| Saltar al keyframe anterior o siguiente | Las flechas a los lados del rombo, o `[` y `]` |
| Poner keyframes con la pieza en marcha | `Mark > Add Keyframe`, con el atajo que indique el menú |
| Saber qué se va a animar con ese atajo | El orden: retime, curva activa, último control tocado, `Audio Gain` |
| Ver los keyframes bajo el clip sin cambiar de panel | El botón `Show Keyframe Tray` de la barra de la timeline |
| Quitarse de encima las pistas de keyframes vacías | Tres puntos `>` `Display Parameters with Keyframes` |
| Proteger una pista de keyframes terminada | Su candado |
| Dejar una sola pista de keyframes activa | `Alt` (Win) / `Opt` (Mac) + clic sobre su candado |
| Más sitio para keyframear | El icono de expandir: ventana propia, solo en la Edit page |
| Comparar un plano con y sin estabilizar | El interruptor del grupo `Stabilization` |
| Afinar la estabilización sin esperar otro análisis | `Strength` |
| Saber qué controles del estabilizador exigen reanalizar | El modo, `Cropping Ratio` y `Smooth` |
| Conservar una panorámica quitándole el temblor | `Camera Lock` apagado y `Smooth` |
| Clavar un plano como sobre un trípode | `Camera Lock` |
| Ampliar solo donde asoma el borde al estabilizar | `Zoom` apagado y keyframes de `Zoom` en `Transform` |
| Medir cuánto te ha recortado el estabilizador | Apaga y enciende el interruptor mirando un borde |
| Comprobar cualquier atajo en tu instalación | `Alt+Ctrl+K` (Win) / `Opt+Cmd+K` (Mac) |

---

## 📌 Entregables

1. ✅ **`BC-Montaje-v3`** conservada e intacta
2. ✅ Timeline **`BC-Montaje-v4`**, abierta, duplicada de la anterior
3. ✅ **15+** clips en la pista de vídeo principal, sin huecos ni solapes
4. ✅ **3+** clips con la velocidad cambiada, uno de ellos con una rampa
5. ✅ Un fotograma congelado colocado al fotograma exacto
6. ✅ Los planos que temblaban, estabilizados o descartados por escrito con su razón
7. ✅ Un reencuadre animado con keyframes y un `Dynamic Zoom` con easing
8. ✅ **3+** marcadores morados y **2+** cianes, todos con nombre propio
9. ✅ La comparación de los tres métodos de relleno, contestada describiendo los artefactos
10. ✅ `notas-de-montaje.md` con el apartado `## Velocidad y transformaciones — Semana 10` cerrado
11. ✅ Respaldo `BC-Bootcamp-Resolve-semana10.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 10
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Montaje-v4` como timeline abierta** y el
puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan **`montaje-v4-activa`, `montaje-v4-clips`, `montaje-v4-sin-huecos`,
> `retimes-aplicados`, `marcadores-de-velocidad` y `marcadores-de-estabilizacion` a la vez**, casi
> seguro tienes abierta `BC-Montaje-v3`: los seis leen la timeline activa. Doble clic en
> `BC-Montaje-v4` y repite.
>
> Si falla solo **`retimes-aplicados`**, recuerda que un reverse al 100 % no cuenta: no cambia la
> correspondencia entre el rango de origen y la duración en la timeline.
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
| [Semana 09](../week-09-trimming_quirurgico/README.md) | **Semana 10** | [Semana 11](../week-11-titulos_texto_plus_efectos_y_compuestos/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
