# Semana 06 — Cut page: edición veloz

> El material está dentro, ordenado y se reproduce fluido. Esta semana pasa lo que llevas
> cinco semanas esperando: **la pieza empieza a existir**. Fea, larga y con planos que vas
> a cambiar, pero de principio a fin.

Con esta semana se abre la **Fase 2**. Al terminarla, tu proyecto tiene un montaje bruto
completo, que es lo que sostiene las once semanas siguientes.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Explicar** qué problema resuelve la Cut page y en qué se diferencia de la Edit page
- **Navegar** por una timeline larga sin tocar el zoom, con la timeline doble y el cabezal
  fijo
- **Revisar** un bin entero como una sola cinta continua, sin abrir un solo archivo
- **Recorrer** un montaje completo con Fast Review y saber qué detecta y qué no
- **Predecir** dónde va a caer una edición antes de pulsar, leyendo el indicador
  inteligente
- **Construir** un montaje bruto de principio a fin usando solo Append
- **Corregir** ese montaje con Smart Insert y Ripple Overwrite, sin dejar huecos
- **Tapar** un salto de entrevista con un plano de recurso, conservando el audio
- **Distinguir** las tres herramientas que cambian la duración de la pieza de las tres que
  no
- **Montar** una escena de tres cámaras con el sync bin y Source Overwrite
- **Comprobar** en treinta segundos si el material de varias cámaras se puede montar así

---

## 📋 Prerrequisitos

- [Semana 05](../week-05-proxies_cache_y_sincronizacion/README.md) cerrada: los siete
  checks en verde, el material optimizado, los subclips creados y `rendimiento.md` escrito
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde
  `Workspace > Scripts > Utility`
- El bin **`03-Multicamara`** de la Semana 05, con tres ángulos de la misma escena. Si no
  lo tienes, el paso 0 de la [práctica 04](2-practicas/04-el-sync-bin.md) explica cómo
  grabarlo en quince minutos
- Los **subclips** de `11-Subclips`: son el material con el que se monta más rápido
- **La reproducción, fluida.** Si tu material va a saltos, montar es imposible: vuelve a
  activar los optimizados o los proxies de la Semana 05 antes de empezar
- **Material nuevo**: ninguno. Esta semana se monta con lo que ya tienes

> [!IMPORTANT]
> Antes de empezar necesitas una decisión tomada, no un archivo: **cómo termina tu pieza**.
> El paso 0 de la [práctica 02](2-practicas/02-la-primera-pasada.md) lo pide en tres líneas,
> y saber el final es lo que ordena todo el desarrollo.

---

## 🗂️ Estructura de la Semana

```
week-06-cut_page_edicion_veloz/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu pieza, montada de principio a fin
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · Por qué existe la Cut page](1-teoria/01-por-que-existe-la-cut-page.md) | Montaje bruto y acabado, y qué se decide en cada pasada | 30 min |
| [02 · La timeline doble](1-teoria/02-la-timeline-doble.md) | Dos escalas a la vez, el cabezal fijo y leer la forma de una pieza | 30 min |
| [03 · Source tape](1-teoria/03-source-tape.md) | El bin como una cinta, los cuatro modos del visor y el método de revisión | 30 min |
| [04 · Fast review](1-teoria/04-fast-review.md) | Velocidad variable, qué detecta y qué hacer con lo que detectas | 30 min |
| [05 · El indicador inteligente](1-teoria/05-el-indicador-inteligente.md) | Dónde cae la edición, la pista de destino y las seis herramientas | 30 min |
| [06 · Append: la primera pasada](1-teoria/06-append-la-primera-pasada.md) | La herramienta que construye, y cómo se decide el orden montando | 30 min |
| [07 · Corregir el montaje ya hecho](1-teoria/07-corregir-el-montaje-ya-hecho.md) | Smart Insert, Ripple Overwrite y qué significa *ripple* | 30 min |
| [08 · Editar sobre la pista de arriba](1-teoria/08-editar-sobre-la-pista-de-arriba.md) | Place on Top, Close Up y los planos de recurso | 30 min |
| [09 · El sync bin](1-teoria/09-el-sync-bin.md) | Varias cámaras, Source Overwrite y el sonido de un multicámara | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · Anatomía de la Cut page](2-practicas/01-anatomia-de-la-cut-page.md) | Recorres la página, creas `BC-Montaje-v1` y revisas tu material como una cinta | 45 min |
| [02 · La primera pasada](2-practicas/02-la-primera-pasada.md) | Montas tu pieza entera con Append y la revisas con Fast Review | 55 min |
| [03 · Corregir el montaje](2-practicas/03-corregir-el-montaje.md) | Quitas, sustituyes, añades y tapas los saltos con planos de recurso | 55 min |
| [04 · El sync bin](2-practicas/04-el-sync-bin.md) | Montas una escena de tres cámaras eligiendo ángulos sobre el montaje | 50 min |

### Proyecto

Tu pieza existe entera: montaje bruto de principio a fin, con la continuidad abajo y los
recursos encima.
→ [3-proyecto/README.md](3-proyecto/README.md)

---

## ⏱️ Distribución del Tiempo (10 horas)

| Actividad | Tiempo |
| --------- | ------ |
| Teoría (9 archivos × 30 min) | 4 h 30 min |
| Prácticas (4, entre 45 y 55 min) | 3 h 25 min |
| Proyecto | 1 h 5 min |
| Recursos y glosario | 30 min |
| Autoevaluación | 30 min |
| **Total** | **10 h** |

> [!NOTE]
> La práctica 02 es la que más se desborda, y no por dificultad: por afinar cortes cuando
> no toca. Si a los treinta minutos no llevas montada la mitad de la pieza, es que estás
> recortando en vez de montando.

---

## 💠 Qué necesita Studio esta semana

**Nada.** La Cut page entera —timeline doble, source tape, fast review, las seis
herramientas de edición y el sync bin— funciona en DaVinci Resolve Free.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free. Es lo que hace el bootcamp |

Ningún entregable evaluable de esta semana depende de Studio.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Entrar y salir de la Cut page sin ratón | `Shift+3` para Cut, `Shift+4` para Edit: la timeline es la misma |
| Saltar al minuto cuatro sin buscar | Clic directo en la timeline de arriba, a esa altura |
| Ver el ritmo de tu pieza de un vistazo | La distribución de cortes en la timeline de arriba |
| Recorrer material a tres velocidades | `L` `L` `L` acelera, `K` para, `J` hace lo mismo hacia atrás |
| No dejar huecos invisibles | Imán activado con `N` desde el primer clip |
| Trabajar siempre en el mismo punto de la pantalla | El cabezal de la timeline de detalle no se mueve: aprovéchalo |
| Revisar doscientos clips sin abrir ninguno | `Source Tape` en el visor de la Cut page |
| Reproducir la jornada en el orden en que ocurrió | Ordena el bin por hora de grabación antes de activar el source tape |
| Revisar solo un tipo de material | Selecciona un smart bin de la Semana 04 en vez de un bin |
| Volver a algo que acabas de ver | Modo `Recent 5 Mins` del visor |
| Comparar dos tomas de lo mismo | Modo `Multi Source` |
| Saltarte los silencios de una entrevista | Activa la forma de onda sobre el source tape |
| Ver un montaje de seis minutos en menos de dos | Fast Review sobre la timeline |
| Detectar planos repetidos | En fast review saltan solos: los ves casi seguidos |
| No perder lo que detectas revisando | Marcador con `M` al vuelo, sin parar la revisión |
| Saber dónde va a caer una edición | Mira el indicador inteligente antes de pulsar el botón |
| Forzar que caiga en un corte | Acerca el cabezal a ese corte |
| Forzar que caiga en medio de un plano | Aléjalo de cualquier corte |
| Montar sin miedo a romper nada | Append no desplaza ni machaca: solo añade al final |
| El ciclo más rápido de la semana | Source tape, `I`, `O`, Append, seguir |
| Meter un clip entero sin marcar | No marques `I` ni `O`: entra completo |
| Elegir herramienta de corrección sin dudar | ¿Lo que hay en el destino se queda o se va? |
| Quitar sin dejar agujeros | Borrado con ripple, y comprueba ampliando la vista de detalle |
| No descolocar lo de la pista de arriba | Cierra la estructura de `Video 1` antes de poner nada encima |
| Probar un plano sin arriesgar el montaje | Ponlo en la pista de arriba: quitarlo lo deja como estaba |
| Que un recurso tape de verdad | Que empiece antes del corte y acabe después |
| Ver qué hay debajo de un recurso | Desactiva `Video 2` desde su cabecera y reproduce |
| Comprobar que un sync bin alinea bien | Cabezal en un momento reconocible: ¿coinciden los ángulos? |
| Colocar un ángulo ya sincronizado de un botón | Source Overwrite, que alinea por hora de grabación |
| Que un multicámara no suene a eco | Suena una sola pista de audio: la de la base |
| Comprobar cualquier atajo en tu instalación | `DaVinci Resolve > Keyboard Customization`, busca el comando por nombre |

---

## 📌 Entregables

1. ✅ Timeline **`BC-Montaje-v1`**, abierta, con el montaje bruto de principio a fin
2. ✅ **15+** clips en su pista de vídeo principal
3. ✅ **120 s** de duración o más
4. ✅ **2+** pistas de vídeo: la continuidad abajo, los recursos encima
5. ✅ Timeline **`BC-Sync-Cut-v1`** con la escena multicámara montada
6. ✅ `notas-de-montaje.md` en `04-respaldos/`, con sus seis apartados
7. ✅ Ni títulos, ni transiciones, ni música, ni color: nada que no toque todavía
8. ✅ Respaldo `BC-Bootcamp-Resolve-semana06.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 06
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Montaje-v1` como timeline
abierta** y el puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan **los cuatro últimos a la vez**, casi seguro tienes abierta `BC-Sync-Cut-v1`
> después de la práctica 04: los cuatro leen la timeline activa. Doble clic en
> `BC-Montaje-v1` y repite.
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
| [Semana 05](../week-05-proxies_cache_y_sincronizacion/README.md) | **Semana 06** | [Semana 07](../week-07-cut_page_acabado_y_quick_export/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
