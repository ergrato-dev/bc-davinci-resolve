# Semana 09 — Trimming quirúrgico

> Tu montaje cuenta la historia. Lo que todavía se nota es el montaje: planos que entran tarde,
> planos que salen tarde, cortes que saltan y una imagen y un sonido que cambian siempre en el
> mismo fotograma. Esta semana no vas a poner ni un plano nuevo: vas a mover bordes. El manual de
> Resolve abre su capítulo de trimming diciendo que es **la mitad del trabajo de montar**.

Segunda semana de la **Fase 3**. La Semana 08 te enseñó a decidir dónde entra un plano; esta te
enseña a decidir en qué fotograma exacto empieza y acaba.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Distinguir** montar de afinar, y saber en qué fase de un montaje estás
- **Nombrar** las cinco operaciones de trimming y decir qué mueve cada una
- **Saber** en qué modo estás sin mirar la barra, y qué significa cada gesto en cada modo
- **Hacer** `Ripple`, `Roll`, `Slip` y `Slide` con el ratón, con el teclado y escribiendo timecode
- **Afinar** un corte con la reproducción en bucle, sin pararla
- **Trimar** con la pieza en marcha usando `J`, `K` y `L` y el `Dynamic Trim Mode`
- **Predecir** qué se mueve en un ripple, y controlarlo con el `Sync Lock` y los selectores de pista
- **Construir** split edits —cortes en L y en J— con trim asimétrico, sin desincronizar nada
- **Anotar** una pieza entera con marcadores de colores y trabajar con el `Marker Index`

---

## 📋 Prerrequisitos

- [Semana 08](../week-08-edit_page_anatomia_y_edicion_basica/README.md) cerrada: los nueve checks en
  verde
- **`BC-Montaje-v2` acabada de principio a fin.** Esta semana se trabaja sobre el montaje de verdad,
  no sobre una timeline de prueba. Un montaje incompleto no se puede afinar
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde `Workspace > Scripts > Utility`
- El respaldo **`04-respaldos/BC-Bootcamp-Resolve-semana08.drp`**. Si no está, expórtalo antes de
  empezar
- **Auriculares.** No son opcionales esta semana: la mitad de las decisiones se toman oyendo
- **Material nuevo**: ninguno

> [!IMPORTANT]
> Si tu montaje de la Semana 07 no llega al final, cierra primero aquella semana. Afinar los tres
> primeros minutos de una pieza incompleta es trabajo que se va a tirar: cuando montes el resto, la
> duración cambia y las decisiones de esta semana se rehacen.

---

## 🗂️ Estructura de la Semana

```
week-09-trimming_quirurgico/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu montaje afinado
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · Qué es el trimming](1-teoria/01-que-es-el-trimming.md) | Montar frente a afinar, y las cinco operaciones | 30 min |
| [02 · El modo trim frente al modo selección](1-teoria/02-el-modo-trim-frente-al-modo-seleccion.md) | El mismo gesto, dos significados; las tres partes de un corte | 30 min |
| [03 · Ripple y roll](1-teoria/03-ripple-y-roll.md) | Las dos operaciones que se hacen sobre un corte | 30 min |
| [04 · Slip y slide](1-teoria/04-slip-y-slide.md) | Las dos que se hacen sobre un clip, y el visor partido en cuatro | 30 min |
| [05 · Trimming con el teclado](1-teoria/05-trimming-con-el-teclado.md) | Las nueve teclas y el ciclo de seis pasos | 30 min |
| [06 · JKL y el dynamic trim](1-teoria/06-jkl-y-el-dynamic-trim.md) | Afinar con la pieza en marcha | 30 min |
| [07 · El sync lock y las reglas del ripple](1-teoria/07-sync-lock-y-las-reglas-del-ripple.md) | Qué se mueve exactamente, y cómo se controla | 30 min |
| [08 · Trim asimétrico y split edits](1-teoria/08-trim-asimetrico-y-split-edits.md) | Cortes en L y en J, y cómo se hacen | 30 min |
| [09 · Marcadores](1-teoria/09-marcadores.md) | La lista de trabajo, y la regla de medir | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · La copia y el mapa de problemas](2-practicas/01-la-copia-y-el-mapa-de-problemas.md) | Creas `BC-Montaje-v3`, ves la pieza entera y la anotas con marcadores | 50 min |
| [02 · Ripple y roll sobre tu montaje](2-practicas/02-ripple-y-roll-sobre-tu-montaje.md) | Quitas lo que sobra y afinas entradas y salidas, con el teclado | 60 min |
| [03 · Slip, slide y el dynamic trim](2-practicas/03-slip-slide-y-el-dynamic-trim.md) | Arreglas los cortes que no se arreglaban moviéndolos | 55 min |
| [04 · Split edits y cierre](2-practicas/04-split-edits-y-cierre.md) | Cortes en L y en J, limpieza, comparación y respaldo | 45 min |

### Proyecto

Tu montaje afinado de principio a fin, con split edits, sin huecos, y la comparación escrita entre
la versión de la Semana 07 y la de esta.
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
> La práctica que más se desborda es la 02, y siempre por lo mismo: afinar los cuarenta cortes de
> la pieza al fotograma. No hace falta. La práctica pide todos los marcadores amarillos y **cinco**
> rojos: eso es lo que enseña la técnica. El resto de los cortes se afinan solos con el tiempo, y
> algunos ni lo necesitan.

---

## 💠 Qué necesita Studio esta semana

**Nada.** Los cuatro modos de la barra de herramientas, las cinco operaciones de trimming, el
editor de trim de precisión, el `Dynamic Trim Mode`, el trim asimétrico, el `Sync Lock` y los
marcadores funcionan en DaVinci Resolve Free. El capítulo 51 del manual, que es el material de
esta semana entero, no marca ninguna de sus funciones como exclusiva de Studio.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free |

Ningún entregable evaluable de esta semana depende de Studio.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Ver la pieza sin la tentación de tocarla | `Workspace > Viewer Mode > Cinema Viewer`, atajo `P` |
| Anotar un problema sin parar la reproducción | `M` |
| Anotar y escribir la nota al momento | `Ctrl+M` (Win) / `Cmd+M` (Mac) |
| Que el marcador vaya a la timeline y no a un clip | Deselecciona antes: `Ctrl+Shift+A` / `Cmd+Shift+A` |
| Saltar de marcador en marcador | `Shift+Flecha arriba` y `Shift+Flecha abajo` |
| Borrar el marcador que hay bajo el cabezal | `Alt+M` (Win) / `Opt+M` (Mac) |
| Marcar un tramo entero | `I`, `O`, clic derecho `> Convert In and Out to Duration Marker` |
| Trabajar con todos los marcadores a la vez | `Index > Markers`; los campos `Name` y `Notes` se editan en la fila |
| Que los marcadores acompañen a los ripples | `Timeline > Ripple Timeline Markers` |
| Volver al modo seguro | `A` |
| Entrar en modo trim | `T` |
| Probar el otro modo solo para este gesto | Mantén pulsada `A` o `T` mientras arrastras |
| Seleccionar el corte más cercano y saltar a él | `V` |
| Seleccionar el clip que cruza el cabezal | `Shift+V` |
| Rotar entre saliente, centrado y entrante | `U` |
| Trimar solo la imagen o solo el sonido | `Alt+U` (Win) / `Opt+U` (Mac) |
| Alternar entre `Slip` y `Slide` | `S`; el icono del botón `Dynamic Trim Mode` dice en cuál estás |
| Mover un fotograma, o cinco | `,` y `.`, o `Shift+,` y `Shift+.` |
| Cambiar cuántos fotogramas son el salto rápido | `Preferences > User > Editing` |
| Trimar por número en vez de a ojo | Selecciona y escribe `-12` o `+1.`, y `Enter` |
| Escuchar el corte en su contexto | `/` |
| Afinar sin parar la reproducción | `Ctrl+/` (Win) / `Cmd+/` (Mac) y luego `/` |
| Reproducir solo el tramo marcado | `Alt+/` (Win) / `Opt+/` (Mac) |
| Ver solo el fotograma del cabezal mientras trimas | Mantén `Shift` |
| Apagar el visor partido del todo | `View > Enable Multiview Edit Preview` |
| Ver cuánta cola te queda al deslizar | El recuadro punteado que aparece al hacer `Slip` |
| Abrir el editor de trim de precisión | Doble clic sobre un corte |
| Abrir el clip original en el fotograma que ves | `Alt` (Win) / `Opt` (Mac) + doble clic |
| Reproducir hacia atrás, parar, hacia delante | `J`, `K`, `L` |
| Cámara lenta con sonido ralentizado | Mantén `K`+`L` |
| Avanzar un fotograma exacto | `K` pulsada y un toque de `L` |
| Trimar rápido sin cambiar de modo | `Ctrl+J` / `Ctrl+L` (Win) · `Cmd+J` / `Cmd+L` (Mac) |
| Entrar y salir del modo dinámico | `W`; el cabezal amarillo dice que estás dentro |
| Recuperar la reproducción sin salir del modo dinámico | `Ctrl+Shift+A` / `Cmd+Shift+A` |
| Borrar un clip cerrando el hueco | `Forward Delete` — `Supr` (Win), `Fn+Supr` (Mac) |
| Llevar un corte seleccionado al cabezal | `E` |
| Que varios clips superpuestos acaben a la vez | Cabezal donde toca y `Shift+]` |
| Que empiecen todos a la vez | `Shift+[` |
| Ripplear hasta el cabezal sea cual sea el modo | `Ctrl+Shift+[` / `]` (Win) · `Cmd+Shift+[` / `]` (Mac) |
| Dejar activo el selector de una sola pista | `Alt` (Win) / `Opt` (Mac) + clic sobre su selector |
| Acotar una operación a un solo clip | Selecciónalo a mano: gana sobre los selectores de pista |
| Poner todas las cabeceras en el mismo estado | Clic sobre un control y arrastra por las demás |
| Suspender el enlace de audio y vídeo solo para este clic | `Alt` (Win) / `Opt` (Mac) + clic |
| Añadir un segundo corte a la selección | `Ctrl` (Win) / `Cmd` (Mac) + clic |
| Saltarse el imán solo durante un arrastre | `N` mientras arrastras |
| Acortar un plano por los dos extremos conservando el centro | Selecciona su entrada y su salida y acércalas |
| Acortar un bloque de rótulos por una cantidad exacta | Selecciona los cortes y arrastra con `Ctrl` / `Cmd` |
| Punto seguro antes de un ripple grande | `File > Create Timeline Backup` |
| Comprobar cualquier atajo en tu instalación | `Alt+Ctrl+K` (Win) / `Opt+Cmd+K` (Mac) |

---

## 📌 Entregables

1. ✅ **`BC-Montaje-v2`** conservada e intacta
2. ✅ Timeline **`BC-Montaje-v3`**, abierta, duplicada de la anterior
3. ✅ **15+** clips en la pista de vídeo principal, sin huecos ni solapes
4. ✅ Todas las pistas con su nombre propio heredado de la Semana 08
5. ✅ **2+** split edits en la primera pista de audio, hechos con trim asimétrico
6. ✅ **8+** marcadores, todos con nombre propio y con su color
7. ✅ La comparación entre `BC-Montaje-v2` y `BC-Montaje-v3`, contestada con cifras
8. ✅ La comparación entre trimar con el teclado y trimar con `Dynamic Trim`
9. ✅ `notas-de-montaje.md` con el apartado `## Trimming — Semana 09` cerrado
10. ✅ Respaldo `BC-Bootcamp-Resolve-semana09.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 09
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Montaje-v3` como timeline abierta** y el
puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan **`montaje-v3-activa`, `montaje-v3-pistas-con-nombre`, `montaje-v3-clips`,
> `montaje-v3-sin-huecos`, `montaje-v3-split-edits` y `marcadores-anotados` a la vez**, casi seguro
> tienes abierta `BC-Montaje-v2`: los seis leen la timeline activa. Doble clic en `BC-Montaje-v3` y
> repite.
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
| [Semana 08](../week-08-edit_page_anatomia_y_edicion_basica/README.md) | **Semana 09** | [Semana 10](../week-10-velocidad_transformaciones_y_estabilizacion/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
