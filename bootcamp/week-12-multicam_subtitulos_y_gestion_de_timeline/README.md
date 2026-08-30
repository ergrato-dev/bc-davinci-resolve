# Semana 12 — Multicámara, subtítulos y gestión de timeline

> Tu pieza está montada, afinada y rotulada. Y sigue sin estar disponible: no para quien no puede
> oírla, no para quien no habla tu idioma, y no para el programa de al lado. Esta semana cierra la
> Fase 3 quitando esas tres barreras, y añade la única forma de montar que se hace a la velocidad de
> la vida: el multicámara.

Quinta y última semana de la **Fase 3**. La Semana 11 te enseñó a poner encima la información que la
imagen no da; esta te enseña a **elegir entre varias imágenes a la vez**, a poner el texto que se
puede apagar, y a sacar tu trabajo de Resolve sin perderlo por el camino.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Explicar** qué es un clip multicámara y por qué no tiene archivo en disco
- **Elegir** entre los cuatro métodos de `Angle Sync` según lo que tu rodaje te haya dejado
- **Comprobar** la sincronía al fotograma **antes** de montar, y corregirla si está mal
- **Montar** con el Multicam Viewer en tiempo real, con las teclas y sin soltar el teclado
- **Distinguir** cortar de conmutar, y arreglar un ángulo sin deshacer el ritmo
- **Crear** una pista de subtítulos y nombrarla como manda la entrega
- **Escribir** subtítulos que se lean: longitud, velocidad, corte de línea y resumen
- **Dar** estilo a una pista entera de una vez y guardarlo como preajuste
- **Elegir** entre archivo aparte, quemado e incrustado, con un criterio y no por costumbre
- **Versionar** una timeline con las cuatro redes de seguridad, sabiendo qué salva cada una
- **Leer** la ventana de Media Management y saber qué casilla es la peligrosa
- **Exportar** e importar una timeline, y anticipar qué se pierde en el salto

---

## 📋 Prerrequisitos

- [Semana 11](../week-11-titulos_texto_plus_efectos_y_compuestos/README.md) cerrada: los diez checks
  en verde
- **`BC-Montaje-v5` terminada**: montada, rotulada y con sus transiciones. Esta semana subtitula una
  pieza acabada, no un montaje a medias
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde `Workspace > Scripts > Utility`
- El respaldo **`04-respaldos/BC-Bootcamp-Resolve-semana11.drp`**. Si no está, expórtalo antes de
  empezar
- **El bin `03-Multicamara` con tres clips o más**, de la Semana 05. Si está vacío, el paso 0 de la
  [Práctica 03 de la Semana 05](../week-05-proxies_cache_y_sincronizacion/2-practicas/03-sincronizar-y-preparar-multicamara.md)
  explica cómo grabar el material con un móvil en quince minutos
- **Espacio libre en disco**: la práctica 04 abre la ventana de Media Management. No se ejecuta, pero
  conviene no tener el disco al límite mientras se toca
- **Material nuevo**: ninguno

> [!IMPORTANT]
> Esta semana **no se remonta**. El check `montaje-v6-clips` pide quince clips o más en la pista de
> vídeo 1, y hay una forma nueva de perderlos: **importar el XML de la práctica 04 encima de tu
> timeline** en vez de como timeline nueva. El paso 2 de esa práctica lleva su aviso.

---

## 🗂️ Estructura de la Semana

```
week-12-multicam_subtitulos_y_gestion_de_timeline/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # tu pieza subtitulada
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · El clip multicámara](1-teoria/01-el-clip-multicamara.md) | ISO y ángulo, las tres fases, el distintivo y la pila vertical | 30 min |
| [02 · Sincronizar los ángulos](1-teoria/02-sincronizar-los-angulos.md) | Los cuatro métodos de `Angle Sync`, el audio del clip y la palmada | 30 min |
| [03 · Cortar y conmutar](1-teoria/03-cortar-y-conmutar.md) | El Multicam Viewer, las teclas, el arreglo y el aplanado | 30 min |
| [04 · La pista de subtítulos](1-teoria/04-la-pista-de-subtitulos.md) | Un tipo de pista propio, el control `ST`, el nombre y las regiones | 30 min |
| [05 · Escribir y estilar subtítulos](1-teoria/05-escribir-y-estilar-subtitulos.md) | `Captions` frente a `Track`, los preajustes y las reglas de escritura | 30 min |
| [06 · Los formatos de subtítulo](1-teoria/06-los-formatos-de-subtitulo.md) | Qué hay dentro de un `.srt`, cómo entra y las tres salidas del render | 30 min |
| [07 · Versionar timelines](1-teoria/07-versionar-timelines.md) | Duplicar, respaldar, comparar, desactivar y el `.drt` | 30 min |
| [08 · Media Management](1-teoria/08-media-management.md) | Alcance, operación, colas, y la casilla que cambia el proyecto | 30 min |
| [09 · Intercambio: XML, AAF, EDL y OTIO](1-teoria/09-intercambio-xml-aaf-edl-otio.md) | Los cinco formatos, a dónde va cada uno y qué se pierde | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · La copia y el clip multicámara](2-practicas/01-la-copia-y-el-clip-multicamara.md) | Creas `BC-Montaje-v6`, enciendes los respaldos y sincronizas los ángulos | 45 min |
| [02 · Cortar en multicámara](2-practicas/02-cortar-en-multicamara.md) | Montas una escena entera con el Multicam Viewer y la corriges | 60 min |
| [03 · Los subtítulos de tu pieza](2-practicas/03-los-subtitulos-de-tu-pieza.md) | Pista, estilo, ocho subtítulos, exportación del `.srt` y vuelta | 60 min |
| [04 · Intercambio, gestión y cierre](2-practicas/04-intercambio-gestion-y-cierre.md) | El viaje de ida y vuelta, la limpieza del proyecto y el cierre de la Fase 3 | 45 min |

### Proyecto

Tu pieza subtitulada, con la pista nombrada y el estilo guardado; la escena multicámara montada; y la
timeline exportada, reimportada y comparada.
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
> La práctica que más se desborda es la 03, y siempre por lo mismo: se empieza a transcribir. Un
> subtítulo no es una transcripción — se resume. El check pide **ocho**, no la pieza entera. Escribe
> ocho bien cortados, con su estilo y dentro del título seguro, y sigue. Los ciento cuarenta que
> falten se hacen otro día, y se hacen el triple de rápido con el estilo ya guardado.

---

## 💠 Qué necesita Studio esta semana

Tres funciones al otro lado de la línea. **Ninguna es un entregable.**

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **`Create Subtitles from Audio`** | Teoría 05 · `Timeline > AI Tools` | Escribir los subtítulos a mano, que es la práctica 03. O transcribir con una herramienta externa que dé un `.srt` e importarlo, como explica la Teoría 06 |
| **`Multicam SmartSwitch`** | Teoría 03 | Cortar con el Multicam Viewer, que es la práctica 02. Es más lento y es lo que enseña el criterio |
| **Subtítulos animados** (`Animated`, plantillas de título) | Teoría 05 | Los subtítulos normales, con el estilo de `Inspector > Track` |
| **`Create New Timeline Using Composition Playlist`** (DCP e IMF) | Teoría 07, de pasada | No hace falta: el bootcamp no entrega DCP |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free |

El entregable de subtítulos de esta semana se hace escribiendo, y el archivo `.srt` que sale es
idéntico al que saldría con la transcripción automática. La comparativa oficial de funciones está en
<https://www.blackmagicdesign.com/products/davinciresolve/studio>.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Crear un clip multicámara | Selecciona los ángulos `>` clic derecho `>` `Create Multicam Clip Using Selected Clips` |
| Decidir en qué bin cae | Selecciona el bin **antes** de crearlo |
| Sincronizar sin timecode | `Angle Sync > Sound` |
| Sincronizar sin audio útil | `Angle Sync > In`, con el punto de entrada en la palmada |
| Garantizar la sincronía en cualquier rodaje | Una palmada delante de todas las cámaras, con todas grabando |
| Que los ángulos se llamen como tus archivos | `Angle Name > Clip Name` |
| Unir en un ángulo los trozos de una misma cámara | `Detect clips from same camera` |
| Usar una grabadora externa como audio de todos | Impórtala como un ángulo más y elige `Reference Audio` |
| Comprobar la sincronía en diez segundos | Un sonido seco, ampliar a fotogramas, comparar |
| Abrir el clip multicámara | Clic derecho en el media pool `>` `Open in Timeline` |
| Corregir un fotograma de desfase | Dentro del clip abierto, con `.` y `,` |
| Renombrar un ángulo | Doble clic sobre el nombre de su pista, dentro del clip abierto |
| Reordenar los ángulos | `Move Track Up` / `Move Track Down` en la cabecera |
| Saber si estás dentro de un clip | El control de ruta de la esquina inferior izquierda |
| Poner marcadores que valgan para todos los ángulos | Ponlos en el clip multicámara: los comparten |
| Encender el Multicam Viewer | Desplegable de modo del visor de origen `>` `Multicam` |
| Elegir cuántos ángulos ver | Desplegable de la esquina inferior derecha: `1x1`, `1x2`, `2x2`, `3x3`, `4x4` |
| Cortar y conmutar sin ratón | Teclas `1` a `9` |
| Solo conmutar | `Alt`+clic, o `Alt`+`1` a `9` |
| Cambiar solo la imagen | `Alt+Shift+]` (Win) / `Opt+Shift+]` (Mac) |
| Cambiar solo el sonido | `Alt+Shift+\` |
| Cambiar los dos | `Alt+Shift+[` |
| Saltar al ángulo anterior o siguiente | `Ctrl+Shift+←` / `Ctrl+Shift+→` (Win) · `Cmd+Shift` en Mac |
| Pasar a otro grupo de ángulos | `Alt+Shift+←` / `Alt+Shift+→` (Win) · `Opt+Shift` en Mac |
| Cambiar el ángulo desde la timeline | Clic derecho `>` `Switch Multicam Clip Angle` |
| Quitar un cambio de cámara | Selecciona el punto de edición con `V` y pulsa `Supr` |
| Encontrar el ISO de un plano | `Clip > Match Frame to Source Clip` |
| Cambiar el timecode de inicio de un clip | Clic derecho en el media pool `>` `Starting Timecode` |
| Crear una pista de subtítulos | Clic derecho en cualquier cabecera de pista `>` `Add Subtitle Track` |
| Elegir en qué pista caen los subtítulos nuevos | El control de destino `ST1`, `ST2`… |
| Añadir un subtítulo en el cabezal | `Inspector > Captions >` `Create Caption` |
| Añadirlo desde la timeline | Clic derecho en la pista `>` `Add Subtitle` |
| Ver la lista de todos los subtítulos | Selecciona la cabecera y abre `Inspector > Captions` |
| Ganar sitio para leerla | Pon el Inspector a altura completa |
| Ocultar la zona de subtítulos | `Timeline View Options` `>` el botón de subtítulos |
| Poner dos subtítulos a la vez en pantalla | Clic derecho dentro de la pista `>` `Add Subtitle Region` |
| Mover un subtítulo de región | Arrástralo arriba o abajo dentro de la pista |
| Dar estilo a todos los subtítulos de una pista | Selecciona la **cabecera** y abre `Inspector > Track` |
| Sacar un subtítulo del estilo de la pista | `Captions >` casilla `Customize Caption` |
| Guardar tu estilo de subtítulos | Menú de tres puntos `>` `Save Track as Preset` |
| Llevártelo a otro equipo | Menú de tres puntos `>` `Export Preset` |
| Corregir un nombre en toda la pista | Icono de búsqueda `>` `Replace All` |
| Saber si un subtítulo es ilegible | El CPS se pone rojo |
| Importar un archivo de subtítulos | Clic derecho en el media pool `>` `Import Subtitle` |
| Colocarlo respetando su timecode | Clic derecho sobre el clip `>` `Insert Selected Subtitles to Timeline Using Timecode` |
| Crear la pista y colocarlo de una vez | Arrástralo a la zona gris de encima de las pistas de vídeo |
| Exportar los subtítulos rápido | Clic derecho en la cabecera de la pista `>` `Export Subtitle` |
| Elegir cómo salen al renderizar | Deliver `>` `Video` `>` `Subtitle Settings` |
| Duplicar la timeline abierta | `Ctrl+4` / `Cmd+4` y `Edit > Duplicate Timeline` |
| Marcar un punto antes de una prueba | `Alt+Ctrl+S` (Win) / `Opt+Cmd+S` (Mac) |
| Volver a un punto anterior | Clic derecho `>` `Restore Timeline Backup` |
| Ver qué cambió respecto a ayer | Clic derecho `>` `Compare with Timeline Backup` |
| Recuperar una timeline borrada | Menú de opciones del media pool `>` `Deleted Timeline Backups` |
| Aligerar un proyecto con muchas timelines | `Disable Timeline` en las cerradas |
| Agrupar las desactivadas | Smart bin con `MediaPool Properties > Timeline` `is Disabled` |
| Llevar una timeline a otro proyecto | Exporta `.drt` y haz doble clic en el archivo |
| Exportar la timeline abierta a XML o AAF | `Ctrl+Shift+O` (Win) / `Cmd+Shift+O` (Mac) |
| Importar una timeline | `Ctrl+Shift+I` (Win) / `Cmd+Shift+I` (Mac) |
| Exportar la pista que quieres en una EDL | Asígnale el control de destino antes |
| Que no te cambien los ajustes del proyecto al importar | Desmarca `Automatically set project settings` |
| Saber si Media Management cabe antes de empezar | La estimación de tamaño, debajo de las opciones |
| Comprobar cualquier atajo en tu instalación | `Alt+Ctrl+K` (Win) / `Opt+Cmd+K` (Mac) |

---

## 📌 Entregables

1. ✅ **`BC-Montaje-v5`** conservada e intacta
2. ✅ Timeline **`BC-Montaje-v6`**, abierta, duplicada de la anterior
3. ✅ **15+** clips en la pista de vídeo 1, sin huecos ni solapes
4. ✅ Una **pista de subtítulos** con **8+** subtítulos
5. ✅ Esa pista **renombrada** con su código de idioma
6. ✅ Un estilo de subtítulos guardado como preajuste
7. ✅ Clip **`BC-Multicam-01`** en `03-Multicamara`, sincronizado y con los ángulos nombrados
8. ✅ Timeline **`BC-Multicam-v1`** montada con el Multicam Viewer, **sin aplanar**
9. ✅ Timeline **`BC-Intercambio-v1`**, con la lista escrita de lo que se perdió
10. ✅ Bin **`14-Intercambio`** con el `.srt` y la timeline reimportada
11. ✅ `BC-Montaje-v1` a `v4` desactivadas
12. ✅ `notas-de-montaje.md` con el apartado `## Multicámara y subtítulos — Semana 12` cerrado
13. ✅ Respaldo `BC-Bootcamp-Resolve-semana12.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 12
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, **`BC-Montaje-v6` como timeline abierta** y el
puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si fallan **cinco checks a la vez** —`montaje-v6-activa`, `montaje-v6-clips`,
> `montaje-v6-sin-huecos`, `pista-de-subtitulos` y `subtitulos-pista-con-nombre`—, la timeline activa
> no es la que crees. Tres causas esta semana, todas fáciles:
>
> 1. Te quedaste en **`BC-Multicam-v1`** al terminar la práctica 02
> 2. **Abriste el clip multicámara con `Open in Timeline` y no volviste.** Mira el control de ruta de
>    la esquina inferior izquierda: si hay dos nombres, estás dentro
> 3. Abriste **`BC-Intercambio-v1`** para compararla en la práctica 04 y ahí se quedó
>
> Si falla solo **`pista-de-subtitulos`**, dos causas: los subtítulos cayeron en otra pista —mira el
> control de destino `ST`— o son menos de ocho.
>
> Si falla solo **`subtitulos-pista-con-nombre`**, la pista sigue llamándose `Subtitle 1`. Doble clic
> sobre su nombre.
>
> Si falla **`bin-de-intercambio`**, el bin no existe o le falta un elemento. Tienen que estar los
> dos: el `.srt` de la práctica 03 y la timeline de la 04.
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
| [Semana 11](../week-11-titulos_texto_plus_efectos_y_compuestos/README.md) | **Semana 12** | [Semana 13](../week-13-fairlight_anatomia_y_mezcla_base/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
