# Semana 04 — Media page: ingesta y organización

> Esta semana entra el material. Y entra bien: copiado con verificación, en una
> estructura pensada, descrito con un vocabulario que tú decides y marcado para que se
> lea de un vistazo. Es la semana que decide si la Semana 12 va a ser cómoda o va a ser
> una búsqueda del tesoro.

Con esta semana se abre la **Fase 1**. Al terminarla, tu proyecto tiene por primera vez
material propio dentro, organizado y consultable.

---

## 🎯 Objetivos de la Semana

Al finalizar esta semana serás capaz de:

- **Explicar** qué hace Resolve al importar, y deducir de ahí por qué existen los clips
  *offline*
- **Copiar** material con verificación por huella, a dos destinos, sin perder un byte
- **Sellar** tu pack de medios y detectar una corrupción silenciosa en treinta segundos
- **Distinguir** Media Storage del media pool, y saber qué destruye borrar en cada uno
- **Diseñar** una estructura de bins que aguante nueve meses y treinta y dos semanas
- **Construir** smart bins que se mantienen solos, y saber por qué salen vacíos
- **Compartir** material entre proyectos con un power bin, sabiendo qué no viaja
- **Describir** cuarenta clips en quince minutos, con selección múltiple y vocabulario
  cerrado
- **Elegir** entre keyword, flag y clip color sin dudar
- **Detectar** el material que se sale del estándar antes de montar ni un corte
- **Recuperar** los planos de un archivo ya montado con Scene Cut Detection

---

## 📋 Prerrequisitos

- [Semana 03](../week-03-resolve_21_anatomia_bases_de_datos_y_preferencias/README.md)
  cerrada: los siete checks en verde, Working Folders puestas y respaldos configurados
- `BC-Bootcamp-Resolve` abierto y el puente lanzado desde `Workspace > Scripts > Utility`
- La estructura `BC-Resolve/` en tu disco, con `02-cache/` y `04-respaldos/`
- **Material, esta semana sí**, y es lo que más tiempo lleva conseguir:

| Carpeta | Qué | Cuánto |
| ------- | --- | ------ |
| `01-basicos/` | Clips cortos y variados | **15-20** |
| `02-entrevista/` | Alguien hablando, 60 s o más | **1** |
| `08-material-montado/` | Un cortometraje completo con cortes | **1** |
| `BC-Propio/` | Planos tuyos, de tu pieza | **10** |

- **Un segundo soporte** —disco externo, otra unidad o una carpeta de nube— para la copia
  de tu material propio
- Espacio libre: entre 5 y 15 GB según el material que descargues

> [!TIP]
> Consigue el material **antes** del lunes. Descargar quince clips y grabar diez planos
> es una tarde entera, y no es el trabajo de esta semana: es el requisito. Todo está en
> [`docs/pack-de-medios.md`](../../docs/pack-de-medios.md).

---

## 🗂️ Estructura de la Semana

```
week-04-media_page_ingesta_y_organizacion/
├── README.md                    # este archivo
├── rubrica-evaluacion.md        # cómo se evalúa la semana
├── checks.json                  # lo que comprueba el verificador
├── 0-assets/                    # 9 diagramas
├── 1-teoria/                    # 9 archivos, un concepto cada uno
├── 2-practicas/                 # 4 prácticas guiadas
├── 3-proyecto/                  # el material de tu pieza entra al proyecto
├── 4-recursos/                  # libros, vídeos y webgrafía
└── 5-glosario/                  # los términos de esta semana, A-Z
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema | Duración |
| ------- | ---- | -------- |
| [01 · La página Media](1-teoria/01-la-pagina-media.md) | Los cinco paneles, qué significa importar y el orden de la ingesta | 30 min |
| [02 · Media Storage](1-teoria/02-media-storage.md) | El panel y la lista; las tres formas de meter material; nombres de archivo | 30 min |
| [03 · El Clone Tool](1-teoria/03-el-clone-tool.md) | Huellas, corrupción silenciosa, dos destinos y la regla de las dos copias | 30 min |
| [04 · El media pool y los bins](1-teoria/04-el-media-pool-y-los-bins.md) | Bin frente a carpeta, Master, bin activo, y una estructura que aguante | 30 min |
| [05 · Los bins que no son bins](1-teoria/05-los-bins-que-no-son-bins.md) | Smart bins como búsquedas guardadas, y power bins con alcance de biblioteca | 30 min |
| [06 · Metadata](1-teoria/06-metadata.md) | Los dos orígenes, qué campo es cada uno, y el pase de veinte minutos | 30 min |
| [07 · Keywords, flags y colores](1-teoria/07-keywords-flags-y-colores.md) | Tres capas, tres preguntas; el código de colores y el flag frente al marcador | 30 min |
| [08 · Vistas, columnas y búsqueda](1-teoria/08-vistas-columnas-y-busqueda.md) | Las dos vistas, las columnas útiles y el pase de diagnóstico | 30 min |
| [09 · Scene Cut Detection](1-teoria/09-scene-cut-detection.md) | Cómo detecta un corte, qué se le escapa, y qué llega al media pool | 30 min |

### Prácticas

| Práctica | Qué haces | Duración |
| -------- | --------- | -------- |
| [01 · La copia verificada](2-practicas/01-la-copia-verificada.md) | Colocas el material, lo sellas, lo copias dos veces y practicas el Clone Tool | 55 min |
| [02 · La estructura de bins](2-practicas/02-la-estructura-de-bins.md) | Creas los diez bins, importas, dejas Master limpio y haces el pase de diagnóstico | 50 min |
| [03 · Metadata, keywords y marcas](2-practicas/03-metadata-keywords-y-marcas.md) | Escribes el vocabulario y describes treinta y tantos clips en selecciones | 50 min |
| [04 · Smart bins y detección de escenas](2-practicas/04-smart-bins-y-deteccion-de-escenas.md) | Tres smart bins que se mantienen solos, y un corto troceado en sus planos | 45 min |

### Proyecto

Entra el material de tu pieza, organizado y descrito, y queda escrita la lista de lo que
va a dar problemas.
→ [3-proyecto/README.md](3-proyecto/README.md)

---

## ⏱️ Distribución del Tiempo (10 horas)

| Actividad | Tiempo |
| --------- | ------ |
| Teoría (9 archivos × 30 min) | 4 h 30 min |
| Prácticas (4, entre 45 y 55 min) | 3 h 20 min |
| Proyecto | 1 h 10 min |
| Recursos y glosario | 30 min |
| Autoevaluación | 30 min |
| **Total** | **10 h** |

> [!NOTE]
> Conseguir el material **no está contado aquí**. Es trabajo de la semana anterior, y por
> eso aparece en los prerrequisitos y no en esta tabla.

---

## 💠 Qué necesita Studio esta semana

**Nada.** Todo lo de esta semana funciona en DaVinci Resolve Free: el Clone Tool, los
bins, los smart bins, los power bins, el panel Metadata, las columnas del media pool y
Scene Cut Detection.

| Función | Dónde aparece | Qué hacer en Free |
| ------- | ------------- | ----------------- |
| **Scripting externo**, desde una terminal | El verificador de la semana | Lanzar el puente desde `Workspace > Scripts`, que sí funciona en Free. Es lo que hace el bootcamp |

Ningún entregable evaluable de esta semana depende de Studio.

---

## 🎩 Trucos y atajos

| Truco | Cómo |
| ----- | ---- |
| Heredar la estructura de carpetas del disco en bins | Clic derecho sobre la carpeta en Media Storage > `Add Folder and SubFolders into Media Pool` |
| Copiar a dos discos en una sola pasada, con verificación | Añade dos destinos al mismo trabajo del Clone Tool |
| Comprobar en treinta segundos si un archivo se ha corrompido | `./scripts/preparar-medios.sh`, con el pack ya sellado |
| Ver un clip antes de importarlo | Selecciónalo en el panel `Media Storage`: aparece en el viewer sin entrar al proyecto |
| Distinguir una timeline de un clip en el media pool | La columna `File Path` de una timeline está vacía |
| Describir cuarenta clips en quince minutos | Selección múltiple en el media pool y escribe la keyword una sola vez |
| Encontrar el material que va a dar problemas antes de montar | Vista de lista, ordena por `Frame Rate` y por `Video Codec` |
| Elegir qué columnas ves | Clic derecho sobre la **cabecera de columnas**, en vista de lista |
| Ver los power bins, que están ocultos por defecto | `View > Show Power Bins` |
| Saber qué te falta por describir | Un smart bin con la regla de `Keywords` vacío |
| Recuperar un bin que "se ha vaciado" de golpe | Borra el texto del buscador del media pool |
| No perder nunca un descarte | Muévelo a `10-Descartes` en vez de quitarlo del media pool |

---

## 📌 Entregables

1. ✅ Pack sellado: `MANIFIESTO.sha256` generado y **comprobado**
2. ✅ `BC-Propio/` copiado a un segundo soporte
3. ✅ Los **diez bins** creados con el nombre exacto, colgando de `Master`
4. ✅ **15+** clips en `01-Basicos`, **1+** en `02-Entrevista`, **10+** en `08-Propio`
5. ✅ `Master` sin ningún clip suelto
6. ✅ **3+** subclips en `09-Escenas`, con los cortes revisados a mano
7. ✅ Tres smart bins: `SB-Noche`, `SB-Revisar` y `SB-Sin-describir`
8. ✅ Power bin `BC-Recursos`, visible desde otro proyecto
9. ✅ `vocabulario-keywords.md` en `04-respaldos/`, con keywords y código de colores
10. ✅ `notas-de-ingesta.md` en `04-respaldos/`, con las cuatro respuestas del pase
11. ✅ Respaldo `BC-Bootcamp-Resolve-semana04.drp`

---

## ✅ Verificación

```bash
python scripts/verificar-semana.py 04
```

Con Resolve abierto, `BC-Bootcamp-Resolve` cargado, el Project Manager en la **raíz de
tu biblioteca original** y el puente lanzado desde `Workspace > Scripts > Utility`.

> [!TIP]
> Si falla **un solo** check de bin, es el nombre: una tilde, una minúscula o el bin
> creado dentro de otro. El verificador no distingue un bin vacío de uno que no existe.
> Si fallan **todos**, es el puente o el proyecto abierto.

Si algo falla antes de eso:

```bash
python scripts/verificar-semana.py --doctor
```

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 03](../week-03-resolve_21_anatomia_bases_de_datos_y_preferencias/README.md) | **Semana 04** | [Semana 05](../week-05-proxies_cache_y_sincronizacion/README.md) |

← [Volver al inicio del bootcamp](../../README.md)
