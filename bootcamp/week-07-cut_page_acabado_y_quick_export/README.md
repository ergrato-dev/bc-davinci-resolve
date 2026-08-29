# Semana 07 — Cut page: acabado y quick export

> La pieza existe, pero solo tú la puedes ver. Esta semana se acaba lo que la Cut page acaba
> bien —transiciones, velocidad, sonido audible, rótulos— y sale por primera vez del programa
> convertida en un archivo que se le puede enseñar a alguien.

Con esta semana se cierra la **Fase 2**. Al terminarla, tu montaje bruto está acabado en lo
grueso y hay una entrega vista y oída fuera de Resolve.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Decidir** qué se acaba en la Cut page y qué se deja para la Edit page, con una regla
- **Medir** cuánta cola tiene tu material y saber qué transiciones caben en tus cortes
- **Colocar** transiciones con motivo, duración y alineación decididas, no por defecto
- **Reparar** un salto de entrevista con `Smooth Cut` y saber cuándo no va a funcionar
- **Ajustar** la duración de un plano cambiando su velocidad, sin romper lo que hay encima
- **Nivelar** el audio de la pieza para que se pueda escuchar entera sin tocar el volumen
- **Rotular** en su propia pista lo que la imagen no puede decir
- **Detectar** planos largos, flash frames y material repetido con el Boring Detector
- **Exportar** con `File > Quick Export` y comprobar el archivo fuera de Resolve
- **Cerrar** la Fase 2 con su entrega reimportada y su respaldo

---

## 📋 Prerrequisitos

- [Semana 06](../week-06-cut_page_edicion_veloz/README.md) cerrada: los ocho checks en verde,
  `BC-Montaje-v1` de principio a fin y `BC-Sync-Cut-v1` con la escena multicámara montada
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde
  `Workspace > Scripts > Utility`
- El respaldo **`04-respaldos/BC-Bootcamp-Resolve-semana06.drp`**. Si no está, expórtalo
  antes de empezar: la práctica 01 hace operaciones con ripple y borrados
- **Auriculares.** Los mismos toda la semana. El paso de nivelado no se puede hacer con los
  altavoces del portátil
- La carpeta **`BC-Resolve/03-entregas/`** de tu estructura de disco, vacía o no
- **Material nuevo**: ninguno. Esta semana se acaba lo que ya tienes

> [!IMPORTANT]
> Si tu montaje bruto **no llega al final**, no empieces esta semana: vuelve a la práctica 02
> de la Semana 06. Acabar media pieza es trabajo que hay que repetir entero cuando la otra
> mitad exista.

---

## 🗂️ Estructura de la Semana

```
week-07-cut_page_acabado_y_quick_export/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu pieza acabada y exportada
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · Qué se acaba en Cut y qué se deja para Edit](1-teoria/01-que-se-acaba-en-cut.md) | La frontera entre las dos páginas y la regla que decide | 30 min |
| [02 · Las colas de un plano](1-teoria/02-las-colas-de-un-plano.md) | Handles, media limit y cuánta cola pide cada transición | 30 min |
| [03 · Transiciones y disolvencias](1-teoria/03-transiciones-y-disolvencias.md) | Los tres significados, las tres alineaciones y la duración | 30 min |
| [04 · Smooth Cut](1-teoria/04-smooth-cut.md) | Reparar un salto sin gastar recurso, y cuándo no se puede | 30 min |
| [05 · Cambios de velocidad](1-teoria/05-cambios-de-velocidad.md) | Velocidad y duración, cámara lenta y qué pasa con el audio | 30 min |
| [06 · Audio básico en la Cut page](1-teoria/06-audio-basico-en-la-cut-page.md) | dBFS, nivelar frente a mezclar y `Ripple Delete Silence` | 30 min |
| [07 · Títulos rápidos](1-teoria/07-titulos-rapidos.md) | Generadores, la pista de títulos y qué escribe un rótulo | 30 min |
| [08 · El detector de aburrimiento](1-teoria/08-el-detector-de-aburrimiento.md) | Boring Detector, flash frames y fotogramas duplicados | 30 min |
| [09 · Quick Export](1-teoria/09-quick-export.md) | La salida rápida, sus presets y por qué no es un master | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · La copia de trabajo](2-practicas/01-la-copia-de-trabajo.md) | Duplicas a `BC-Montaje-v2`, detectas, limpias y traes la escena multicámara | 50 min |
| [02 · Transiciones donde hacen falta](2-practicas/02-transiciones-donde-hacen-falta.md) | Mides tus colas, pones disolvencias con motivo y reparas los saltos | 55 min |
| [03 · Velocidad, audio y títulos](2-practicas/03-velocidad-audio-y-titulos.md) | Ajustas duraciones, dejas la pieza audible y creas la pista de rótulos | 60 min |
| [04 · Quick Export y cierre de la Fase 2](2-practicas/04-quick-export-y-cierre-de-fase.md) | Exportas, lo ves fuera de Resolve, lo reimportas y cierras la fase | 45 min |

### Proyecto

Tu pieza acabada en lo grueso, con tres pistas, y una entrega vista y oída fuera del programa.
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
> La práctica que más se desborda es la 02, y siempre por lo mismo: probar transiciones que
> no estaban en la lista. Si llevas media hora y no has pasado del segundo corte, es que
> estás experimentando en vez de acabar.

---

## 💠 Qué necesita Studio esta semana

**Nada.** Transiciones, `Smooth Cut`, velocidad, nivel de audio, `Ripple Delete Silence`,
títulos, Boring Detector y `Quick Export` funcionan en DaVinci Resolve Free.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **`Smart Reframe`** | El panel `Tools` del visor, junto a `Speed` y `Audio` | No se usa esta semana. El reencuadre manual con `Transform` es la Semana 10 |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free |

Ningún entregable evaluable de esta semana depende de Studio.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Decidir si algo toca ahora | ¿Lo que hay debajo se va a mover todavía? Si sí, no lo hagas |
| Congelar el bruto antes de acabarlo | Clic derecho > `Duplicate Timeline`, y trabaja en la copia |
| Encontrar cualquier ajuste de la timeline | Los tres iconos: `Timeline Options`, `Timeline Actions`, `Edit Actions` |
| Saber si un clip tiene cola en dos segundos | Arrastra su borde hacia fuera: si no se mueve, no hay |
| Que una transición quepa siempre | Pídela de 12 fotogramas en vez de 24 |
| Gastar cola de un solo lado | Alineación `Start on Edit` o `End on Edit` en vez de centrada |
| Poner una disolvencia sin ratón | `V` selecciona el corte más cercano, `Ctrl+T` / `Cmd+T` la añade |
| Elegir la alineación desde el teclado | `U` alterna principio, centro y final antes de `Ctrl+T` |
| Quitar una transición | Selecciónala y `Delete`, o el botón `Cut` con el cabezal cerca |
| Ver los dos números de una duración a la vez | Clic derecho > `Change Duration`: segundos y fotogramas |
| Que el botón ponga siempre lo que tú quieres | `Timeline Options > Set Default Transition` |
| Deshacer un experimento masivo | `Timeline Actions > Clear Transition from All Edits` |
| Saber si una transición sobra | Quítala y reproduce: si no la echas de menos, sobraba |
| Que un `Smooth Cut` no se note | Cámbialo a 4 fotogramas nada más ponerlo |
| Juzgar un `Smooth Cut` | A velocidad normal, dos o tres pases, nunca parado |
| Que un plano dure exactamente lo que quieres | Escribe la duración en `Duration`, no el porcentaje |
| Comparar un efecto con y sin él | El interruptor de la izquierda de la categoría, en `Tools` |
| Ver de un vistazo qué clips llevan velocidad | `Timeline Options > Display Speed Keyframes` |
| Ralentización que no se ve | No bajes del 80 % con material grabado a 24 fps |
| Bajar el volumen de un clip | `Tools > Audio` y el deslizador |
| Comprobar si los recursos ensucian la voz | Silencia `Video 2` desde su cabecera y compara |
| Quitar pausas largas de una entrevista | `Clip > Audio Operations > Ripple Delete Silence` |
| Que no te pique el diálogo | Sube `Minimum to Trip` a 24 fotogramas o más |
| Crear la pista de títulos sin menús | Arrastra el primer título a la zona gris de encima de `Video 2` |
| Ver un título antes de colocarlo | `Hover Scrub Preview` y pasa el ratón por la miniatura |
| Escribir el texto donde se ve | Doble clic sobre el texto en el visor |
| Centrar un rótulo sin tocar números | Al arrastrarlo se pega al centro y a los tercios |
| Ver la pieza sin rótulos | Desactiva `Video 3` desde su cabecera |
| Encontrar los flash frames de golpe | `Jump Cuts` a 2 fotogramas y mira los rojos |
| Ver dónde se hace larga tu pieza | Los racimos de gris en la timeline de arriba |
| Detectar planos repetidos | `View > Show Duplicate Frames` |
| Exportar solo un minuto | Marca `I` y `O` en la timeline antes de `File > Quick Export` |
| El preset que abre en todas partes | `H.264 Master` |
| Comprobar que un archivo exportado es válido | Reimpórtalo al proyecto y reprodúcelo |
| Ver si los rótulos se leen de verdad | Míralo en el móvil, no solo en el monitor |
| Comprobar cualquier atajo en tu instalación | `DaVinci Resolve > Keyboard Customization`, busca el comando por nombre |

---

## 📌 Entregables

1. ✅ **`BC-Montaje-v1`** conservada, sin tocar
2. ✅ Timeline **`BC-Montaje-v2`**, abierta, con el acabado de la semana
3. ✅ **18+** clips en su pista de vídeo principal, con la escena multicámara dentro
4. ✅ **Cero huecos y cero solapes** en `Video 1`
5. ✅ **3+** pistas de vídeo: continuidad, recursos y títulos
6. ✅ Transiciones y `Smooth Cut` con motivo escrito, no por defecto
7. ✅ Bin **`12-Entregas`** con la exportación reimportada
8. ✅ `BC-Montaje-v2-semana07.mp4` en `03-entregas/`, visto entero fuera de Resolve
9. ✅ `notas-de-montaje.md` con el apartado `## Acabado — Semana 07` cerrado
10. ✅ Respaldo `BC-Bootcamp-Resolve-semana07.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 07
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Montaje-v2` como timeline abierta**
y el puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan **`montaje-v2-activo`, `montaje-v2-clips`, `montaje-v2-sin-huecos` y
> `montaje-v2-pista-de-titulos` a la vez**, casi seguro tienes abierta `BC-Montaje-v1` o
> `BC-Sync-Cut-v1`: los cuatro leen la timeline activa. Doble clic en `BC-Montaje-v2` y
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
| [Semana 06](../week-06-cut_page_edicion_veloz/README.md) | **Semana 07** | [Semana 08](../week-08-edit_page_anatomia_y_edicion_basica/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
