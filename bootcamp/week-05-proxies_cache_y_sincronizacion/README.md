# Semana 05 — Proxies, caché y sincronización

> El material ya está dentro y ordenado. Esta semana se vuelve **trabajable**: se
> reproduce fluido, lo bueno queda acotado en trozos, la imagen y el sonido de dos
> aparatos van pegados al fotograma, y la timeline roja de `Media Offline` deja de dar
> miedo para siempre.

Con esta semana se cierra la **Fase 1**. Al terminarla, tu proyecto está listo para
montar, que es exactamente lo que empieza el lunes siguiente en la Cut page.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Explicar** por qué un H.264 se reproduce a saltos, con las palabras long-GOP,
  intra-frame y GOP
- **Diagnosticar** cuál de los tres cuellos de botella es el tuyo, con tres pruebas de un
  minuto y un número
- **Generar** medios optimizados configurando antes el formato y la resolución
- **Elegir** entre optimizados y proxies con tres preguntas, y saber cuál viaja a otro
  equipo
- **Cachear** un tramo de la timeline, leer la barra de estado y saber por qué la caché se
  invalida sola
- **Localizar** la carpeta donde vive todo lo generado, y vaciarla sin perder trabajo
- **Sincronizar** imagen y sonido de doble sistema por forma de onda, y comprobarlo al
  fotograma
- **Reconocer** una deriva de sincronía y saber de dónde sale
- **Construir** un clip multicámara con la fuente de audio fija en el micrófono bueno
- **Acotar** material largo en subclips con colas, nombrados y descritos
- **Reenlazar** un proyecto con todo el material offline, en menos de un minuto

---

## 📋 Prerrequisitos

- [Semana 04](../week-04-media_page_ingesta_y_organizacion/README.md) cerrada: los siete
  checks en verde, los diez bins creados, el material descrito y `notas-de-ingesta.md`
  escrito
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde
  `Workspace > Scripts > Utility`
- El smart bin `SB-Revisar` de la Semana 04, que es la lista de trabajo de la práctica 01
- **Espacio libre en disco**: al menos **el doble** de lo que pesa tu material. Es el
  prerrequisito que más gente descubre tarde
- **Material nuevo**, y esta semana es poco pero muy concreto:

| Carpeta | Qué | Cuánto |
| ------- | --- | ------ |
| `03-multicamara/` | Una escena grabada desde 3 ángulos, **todos con audio** | **3 clips** |
| `03-multicamara/` | Un par de doble sistema: un vídeo con audio de cámara y una grabación de sonido del mismo momento | **1 par**, 60 s o más |

> [!TIP]
> Si el pack no te llenó `03-multicamara/`, **grábalo tú**: el paso 0 de la
> [práctica 03](2-practicas/03-sincronizar-y-preparar-multicamara.md) lo explica en quince
> minutos con un móvil y cualquier aparato que grabe sonido. Y da la palmada al empezar:
> es una claqueta gratis.

---

## 🗂️ Estructura de la Semana

```
week-05-proxies_cache_y_sincronizacion/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu material queda listo para montar
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · Por qué el material no va fluido](1-teoria/01-por-que-el-material-no-va-fluido.md) | Long-GOP frente a intra-frame, y los tres cuellos de botella | 30 min |
| [02 · Medios optimizados](1-teoria/02-medios-optimizados.md) | Qué generan, cómo se configuran y cómo se comprueba que se usan | 30 min |
| [03 · Proxies](1-teoria/03-proxies.md) | La copia que sí viaja, el vínculo manual y el ajuste que arruina una entrega | 30 min |
| [04 · La caché de render](1-teoria/04-la-cache-de-render.md) | Qué guarda, los modos `None`, `Smart` y `User`, y por qué se invalida sola | 30 min |
| [05 · Dónde vive la caché](1-teoria/05-donde-vive-la-cache.md) | La carpeta de trabajo, cuánto ocupa y cómo se vacía sin perder nada | 30 min |
| [06 · Sincronizar audio y vídeo](1-teoria/06-sincronizar-audio-y-video.md) | Doble sistema, timecode, forma de onda y la deriva | 30 min |
| [07 · Preparar el material multicámara](1-teoria/07-preparar-el-material-multicamara.md) | Ángulos, método de sincronización y la fuente de audio | 30 min |
| [08 · Subclips](1-teoria/08-subclips.md) | Acotar sin duplicar, las colas y por qué el nombre importa | 30 min |
| [09 · Medios offline y relink](1-teoria/09-medios-offline-y-relink.md) | Las cinco causas, el relink por nombre y las tres reglas de prevención | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · Diagnóstico, medios optimizados y proxies](2-practicas/01-diagnostico-optimizados-y-proxies.md) | Mides tu cuello de botella, optimizas lo problemático y generas proxies de tu material | 55 min |
| [02 · La caché de render y el disco](2-practicas/02-la-cache-de-render-y-el-disco.md) | Ves la caché trabajar, cacheas a mano y vacías espacio sin perder nada | 45 min |
| [03 · Sincronizar y preparar multicámara](2-practicas/03-sincronizar-y-preparar-multicamara.md) | Sincronizas un par de doble sistema, lo compruebas al fotograma y construyes el multicámara | 55 min |
| [04 · Subclips y relink](2-practicas/04-subclips-y-relink.md) | Acotas cinco subclips, y rompes y arreglas un proyecto de pruebas | 50 min |

### Proyecto

El material queda listo para montar: fluido, acotado, sincronizado y con el rendimiento
documentado.
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
> El **tiempo de generación no está contado aquí**, y puede ser mucho: optimizar treinta
> clips lleva lo que lleva. Lanza las generaciones al principio de la sesión y sigue con la
> teoría mientras trabajan en segundo plano.

---

## 💠 Qué necesita Studio esta semana

**Nada.** Los medios optimizados, los proxies, la caché de render, la sincronización
automática de audio, los clips multicámara, los subclips y el relink funcionan todos en
DaVinci Resolve Free.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| Algunos **formatos de codificación** de la lista de optimizados y proxies | Práctica 01, pasos 3 y 6 | La lista varía por sistema operativo y por versión. Elige cualquier codec intra-frame de los que te ofrezca tu instalación: el criterio de la teoría 02 vale igual |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free. Es lo que hace el bootcamp |

Ningún entregable evaluable de esta semana depende de Studio.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Saber en tres minutos cuál de los tres cuellos tienes | Clip solo, cuatro pistas, y clip con un cambio de `Zoom`. Mira el contador de fps en cada prueba |
| Comprobar que los optimizados se usan de verdad | Activa y desactiva `Playback > Use Optimized Media if Available` mientras reproduces |
| Comprobar que los proxies se usan | Cambia de opción en `Playback > Proxy Handling` mientras reproduces |
| Estimar el espacio antes de una tanda grande | Genera un clip, mira lo que ocupa y multiplica |
| Salir del paso sin generar ningún archivo | `Playback > Timeline Proxy Mode` a media o un cuarto de resolución |
| Ver si la caché está trabajando | La franja fina bajo la regla de tiempo de la timeline |
| Cachear solo lo pesado | `Playback > Render Cache > User` y marca los tramos |
| Hacer sitio sin perder lo que usas | `Playback > Delete Render Cache`, opción de borrar solo lo no usado |
| Sincronía a prueba de todo, gratis | Da una palmada delante de las cámaras al empezar cada toma |
| Comprobar la sincronía al fotograma | Busca una "p" o una "t": el pico de audio y el cierre de labios, en el mismo fotograma |
| Diagnosticar una deriva en diez segundos | Comprueba el principio y el final del mismo clip |
| Conservar la referencia sin que moleste | Añade el audio bueno como pista extra y silencia la de cámara |
| Marcar entrada y salida sin ratón | `I` y `O` en el visor de origen, en cualquier página |
| Comprobar que un subclip no duplica nada | Vista de lista, columna `File Path`: comparte la ruta del padre |
| Reenlazar cien clips de una vez | Relink sobre toda la selección y señala la carpeta raíz: busca dentro por nombre |
| Practicar el relink sin riesgo | En un proyecto de pruebas, desenlazando a propósito |

---

## 📌 Entregables

1. ✅ `rendimiento.md` en `04-respaldos/`, con las cinco líneas y sus cifras
2. ✅ `notas-de-ingesta.md` actualizado: lo resuelto y la deriva encontrada
3. ✅ Medios optimizados generados para los clips de `SB-Revisar`
4. ✅ Proxies generados para `08-Propio`
5. ✅ `Playback > Render Cache` en `Smart`, y la caché no usada borrada
6. ✅ **3+** clips en `03-Multicamara`
7. ✅ Timeline **`BC-Sync-v1`**, abierta, con **dos pistas de audio o más**
8. ✅ Un clip multicámara con la fuente de audio fija en un ángulo
9. ✅ **5+** subclips en `11-Subclips`, con colas y con nombre propio
10. ✅ El simulacro de relink hecho en `BC-Pruebas-semana05`
11. ✅ Respaldo `BC-Bootcamp-Resolve-semana05.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 05
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Sync-v1` como timeline abierta**,
el Project Manager en la raíz de tu biblioteca original y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!TIP]
> Si falla **solo** `timeline-sync-audio`, casi seguro tienes abierta otra timeline: el
> check lee la activa. Doble clic en `BC-Sync-v1` y repite.
>
> Si fallan **todos**, o el puente no está lanzado, o te quedaste en
> `BC-Pruebas-semana05` después del simulacro de la práctica 04.

Si algo falla antes de eso:

```bash
python scripts/verificar-semana.py --doctor
```

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 04](../week-04-media_page_ingesta_y_organizacion/README.md) | **Semana 05** | [Semana 06](../week-06-cut_page_edicion_veloz/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
