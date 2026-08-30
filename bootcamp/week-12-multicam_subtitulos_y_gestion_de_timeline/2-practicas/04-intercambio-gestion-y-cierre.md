# Práctica 04 — Intercambio, gestión y cierre

> Al terminar habrás hecho salir tu timeline de Resolve y volver a entrar, habrás visto con tus ojos
> qué se pierde en el viaje, habrás leído la ventana de Media Management sin ejecutarla, y habrás
> cerrado la Fase 3 del bootcamp.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-los-subtitulos-de-tu-pieza.md), [Teoría 07](../1-teoria/07-versionar-timelines.md), [Teoría 08](../1-teoria/08-media-management.md), [Teoría 09](../1-teoria/09-intercambio-xml-aaf-edl-otio.md)

## Contexto

Las tres primeras prácticas construyen. Esta comprueba, y es la única del bootcamp cuyo objetivo es
**descubrir lo que no funciona**: qué se pierde al exportar una timeline, y qué cuesta gestionar los
medios.

Un aviso antes de empezar: aquí se abre una ventana que **escribe en disco**. El paso 6 explica por
qué no se ejecuta.

---

## Paso 1: Exportar `BC-Montaje-v6` como XML

**Por qué**: es el formato que casi cualquier programa entiende, y el que vas a usar el día que te
pidan la timeline.

1. Media pool: selecciona **`BC-Montaje-v6`**
2. `File > Export > Export AAF, XML, DRT` — `Ctrl+Shift+O` (Win) / `Cmd+Shift+O` (Mac)
3. Guarda en `BC-Resolve/04-respaldos/` como **`BC-Montaje-v6.xml`**
4. Elige un formato XML en el desplegable de tipo de archivo

**Verifica**: el archivo existe. Ábrelo con un editor de texto y busca el nombre de uno de tus
clips: está ahí, en texto. **El archivo pesa kilobytes**, aunque tu montaje tenga gigabytes de
material. Esa es la lección entera de la Teoría 09.

---

## Paso 2: Volver a importarlo

**Por qué**: comparar lo que salió con lo que vuelve es la única forma honesta de saber qué lleva un
formato de intercambio.

1. Media pool: **selecciona el bin `14-Intercambio`**
2. `File > Import Timeline` — `Ctrl+Shift+I` (Win) / `Cmd+Shift+I` (Mac)
3. Elige `BC-Montaje-v6.xml`
4. En el diálogo:

| Campo | Qué hacer |
| ----- | --------- |
| `Timeline name` | Escribe **`BC-Intercambio-v1`** |
| `Automatically set project settings` | **Desmárcalo** |
| El resto | Déjalo como viene |

5. `OK`

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check intercambio-v1-existe
```

> [!WARNING]
> **`Automatically set project settings` puede cambiar la cadencia y la resolución de tu proyecto.**
> Tu proyecto lleva doce semanas de decisiones dentro y la cadencia de una timeline con clips no se
> cambia sin consecuencias, como llevas avisado desde la Semana 01. Desmarcado, siempre.

---

## Paso 3: Comparar lo que llegó

**Por qué**: es el entregable escrito más valioso de la semana, y no se puede hacer de memoria.

Abre las dos timelines y compáralas, punto por punto:

| Qué mirar | En `BC-Montaje-v6` | En `BC-Intercambio-v1` |
| --------- | ------------------ | ---------------------- |
| Número de clips en la `V1` | | |
| Los rótulos de la `V2` | | |
| El adjustment clip de la `V3` | | |
| Las transiciones | | |
| El compound clip de la Semana 11 | | |
| Los efectos ResolveFX | | |
| La **pista de subtítulos** | | |
| Los marcadores | | |

**Verifica**: tienes la tabla rellena, con lo que sobrevivió y lo que no.

> [!NOTE]
> No hay una respuesta única: depende de qué formato XML eligieras y de qué lleva tu pieza. Lo que
> importa no es acertar la lista, es **haberla mirado**. La conclusión que sí es universal: un
> intercambio nunca es una copia.

---

## Paso 4: El otro camino, el `.drt`

**Por qué**: para comparar hace falta un segundo punto, y `.drt` es el formato que menos pierde.

1. Selecciona `BC-Montaje-v6` en el media pool
2. `File > Export > Export AAF, XML, DRT`
3. Guarda como **`BC-Montaje-v6.drt`** en `04-respaldos/`
4. Compara el tamaño de los dos archivos, el `.xml` y el `.drt`

**Verifica**: los dos archivos existen. Anota cuál pesa más y por qué crees que es.

> [!TIP]
> No hace falta importarlo: importar un `.drt` en el mismo proyecto crea una timeline con `import`
> añadido al nombre y no aporta nada nuevo al ejercicio. El archivo está ahí para la Semana 30, la de
> archivado y colaboración.

---

## Paso 5: Desactivar las timelines cerradas

**Por qué**: llevas doce semanas y el media pool tiene ya una fila de timelines. El manual dice que
un número grande afecta al rendimiento del proyecto entero.

1. Media pool: selecciona **`BC-Montaje-v1`** a **`BC-Montaje-v4`**
2. Clic derecho `>` **`Disable Timeline`**
3. Comprueba el **ojo tachado** en la esquina inferior izquierda de sus miniaturas

**Verifica**: las timelines siguen en el media pool y ya no aparecen en los desplegables de timeline.

> [!IMPORTANT]
> **`BC-Montaje-v5` no se desactiva**: el check `montaje-v5-conservada` la busca, y desactivar una
> timeline no la borra pero conviene tenerla a mano para comparar. Y **`BC-Montaje-v6` tampoco**,
> obviamente: es la de esta semana.

---

## Paso 6: Leer la ventana de Media Management

> [!WARNING]
> **Media Management escribe archivos en disco y puede llenarlo.** Con `Relink to new files`
> marcado, además, cambia a qué archivos apunta tu proyecto: si luego borras las copias, el proyecto
> se queda offline.
>
> **En este paso la ventana se abre, se lee y se cancela.** No se pulsa `Start`. Consolidar de verdad
> es la Semana 30, cuando el montaje esté cerrado y no vayas a necesitar más colas.

**Por qué**: hay que haber visto la ventana y su estimación de tamaño antes de tener que usarla con
prisa.

1. Media pool: selecciona **`BC-Montaje-v6`**
2. **`File > Media Management`**
3. Sin tocar nada todavía, observa: el alcance ya viene en `Timelines`, porque eso es lo que tenías
   seleccionado
4. Ahora recorre las tres decisiones y **anota lo que ves**:

| Decisión | Qué elegir para mirar |
| -------- | --------------------- |
| Alcance | `Timelines`, con tu timeline marcada en `Timeline selection` |
| Operación | `Copy` |
| Cuánto material | Prueba `All media`, luego `Used media`, luego `Used media and trim keeping 12 frame handles` |

5. **Con cada opción, mira la estimación de tamaño** que aparece debajo. Anota los tres números
6. Fíjate en dónde están `Relink to new files`, `Consolidate multiple edit segments into one media
   file` y `Use project name subfolder`
7. **`Cancel`**

**Verifica**: tienes los tres números anotados. La diferencia entre el primero y el tercero es lo que
esta herramienta ahorra, y en un proyecto con muchos descartes suele ser un orden de magnitud.

---

## Paso 7: El repaso final de la Fase 3

**Por qué**: esta semana cierra la Fase 3 del bootcamp —las semanas 08 a 12— y la Fase 4 empieza
sobre lo que dejes aquí. Un montaje con huecos o con planos perdidos arrastra el problema ocho
semanas.

Con `BC-Montaje-v6` abierta:

1. Reprodúcela **entera**, de principio a fin, sin parar
2. Comprueba:
   - Ningún hueco negro entre planos
   - Los rótulos de la Semana 11 siguen ahí y en su sitio
   - Los subtítulos entran y salen con la voz
   - Ningún subtítulo cruza un corte de escena
   - Ninguna falta de ortografía en pantalla

**Verifica**:

```bash
python scripts/verificar-semana.py 12 --check montaje-v6-sin-huecos
python scripts/verificar-semana.py 12 --check montaje-v6-clips
```

---

## Paso 8: Cerrar la semana y la fase

1. Cierra el apartado de `notas-de-montaje.md`:

```markdown
### Intercambio y gestión — práctica 04
- Tamaño del .xml: __ · del .drt: __
- Qué sobrevivió al viaje de ida y vuelta: __
- Qué NO sobrevivió: __
- Timelines desactivadas: __
- Media Management, estimación: all __ · used __ · used+trim 12 __
- Qué pasa a la Fase 4: __
```

2. `Ctrl+S` / `Cmd+S`
3. **Comprueba que `BC-Montaje-v6` es la timeline abierta**
4. `File > Export Project` → `04-respaldos/BC-Bootcamp-Resolve-semana12.drp`

**Verifica**:

```bash
python scripts/verificar-semana.py 12
```

Diez de diez, con `BC-Montaje-v6` abierta y fuera de cualquier clip multicámara.

---

## ✅ Resultado

- [ ] `BC-Montaje-v6.xml` exportado y abierto con un editor de texto
- [ ] `BC-Intercambio-v1` importada en el bin `14-Intercambio`
- [ ] Tabla de comparación rellena, con lo que se perdió
- [ ] `BC-Montaje-v6.drt` exportado
- [ ] `BC-Montaje-v1` a `v4` desactivadas
- [ ] Ventana de Media Management leída, con los tres tamaños anotados, y **cancelada**
- [ ] Pieza reproducida entera y repasada
- [ ] `notas-de-montaje.md` con el apartado `## Multicámara y subtítulos — Semana 12` cerrado
- [ ] Respaldo `BC-Bootcamp-Resolve-semana12.drp` exportado
- [ ] Los diez checks en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El proyecto cambió de cadencia al importar | `Automatically set project settings` estaba marcado | `Ctrl+Z`, o restaura el respaldo `antes-de-la-semana-12` |
| `intercambio-v1-existe` falla | El nombre del campo `Timeline name` no era exacto | Bórrala y vuelve a importar con el nombre bien |
| `BC-Intercambio-v1` llegó con todo offline | Es lo esperado si los medios no se conforman solos | No pasa nada: la timeline está, y el ejercicio es comparar |
| `bin-de-intercambio` falla | La timeline importada cayó en otro bin | Arrástrala a `14-Intercambio` |
| No encuentro las timelines desactivadas | Ya no salen en los desplegables | Siguen en el media pool, con el ojo tachado |
| Desactivé `BC-Montaje-v6` sin querer | Clic derecho de más | Clic derecho `>` `Enable Timeline` |
| Media Management empezó a copiar | Pulsaste `Start` en vez de `Cancel` | Espera a que termine o cancélala; luego borra la carpeta de destino |
| El proyecto se quedó offline tras Media Management | `Relink to new files` estaba marcado | Relinka a los originales, o restaura el `.drp` de la Semana 11 |
| `montaje-v6-clips` falla | Se perdieron planos en algún paso | Restaura el respaldo `antes-de-la-semana-12` |
| Fallan cinco checks a la vez | La timeline activa no es `BC-Montaje-v6` | Ábrela con doble clic; mira el control de ruta |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Los subtítulos de tu pieza](03-los-subtitulos-de-tu-pieza.md) | **04 · Intercambio, gestión y cierre** | — |

← [Volver a la Semana 12](../README.md)
