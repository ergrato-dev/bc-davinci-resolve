# Práctica 03 — Copias de seguridad de verdad

> Al terminar tendrás las cuatro protecciones de Resolve configuradas, habrás visto con
> tus ojos el archivo de respaldo que genera solo, y habrás **probado** que tu `.drp` se
> puede restaurar. Un respaldo sin probar es una suposición.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 02](02-project-manager-y-dos-proyectos.md), [Teoría 04](../1-teoria/04-copias-de-seguridad.md), [Teoría 02](../1-teoria/02-bibliotecas-de-proyectos.md)

## Contexto

Vas a estar nueve meses trabajando sobre el mismo proyecto. La pregunta no es si algo
saldrá mal, es cuándo. Esta práctica se hace una vez y cubre el resto del bootcamp.

Lo importante no es el paso de configurar —eso son tres casillas— sino el último: abrir
el respaldo y comprobar que dentro está tu trabajo. Casi nadie lo hace, y por eso casi
todo el mundo descubre que su respaldo no servía justo el día que lo necesitaba.

---

## Paso 1: Live Save y respaldos automáticos

**Por qué**: son dos protecciones distintas. Live Save evita perder lo hecho; los
respaldos permiten volver atrás. Hacen falta las dos.

1. `Ctrl+,` (Win) / `Cmd+,` (Mac), pestaña **`User`**, sección
   **`Project Save and Load`**
2. Comprueba que **Live Save** está activado (lo dejaste así en la Semana 01)
3. Activa los **respaldos de proyecto**, si no lo estaban
4. Mira los tres escalones de conservación —copias recientes, por horas y por días— y
   **sube el número de copias diarias** de 2 a **7** como mínimo

**Verifica**: las dos casillas están activadas y las copias diarias son 7 o más.

> [!NOTE]
> Con los valores de fábrica —copia cada 10 minutos conservando 8, más 2 horarias y 2
> diarias— tu ventana de recuperación es de dos días. Para un proyecto de nueve meses
> eso es poco, y subirla cuesta unos megabytes. *Valores por defecto verificados en
> 21.0.4.5, agosto de 2026.*

---

## Paso 2: Mover los respaldos a tu disco de trabajo

**Por qué**: por defecto caen en el disco del sistema. Es el disco que se llena y el que
se pierde cuando hay que reinstalar. Un respaldo en el mismo sitio que se rompe no es un
respaldo.

1. En ese mismo panel, localiza la **ruta de los respaldos de proyecto**
2. Cámbiala a:

```
<ruta-a-BC-Resolve>/04-respaldos/backups-automaticos/
```

3. Crea antes la carpeta si no existe
4. Guarda y cierra Preferences

**Verifica**: el panel muestra la ruta nueva. Anótala en tu `mapa-de-instalacion.md`.

> [!WARNING]
> Los respaldos que ya existían **no se mueven solos** a la carpeta nueva. Se quedan en
> la antigua. No los borres todavía: hasta que la carpeta nueva tenga contenido, la
> vieja es tu única red.

---

## Paso 3: Provocar un respaldo y encontrarlo

**Por qué**: hasta que no ves el archivo, esto es una casilla marcada. Verlo es lo que
convierte la configuración en confianza.

1. Abre `BC-Bootcamp-Resolve`
2. Haz un cambio pequeño y reversible en la timeline `BC-Montaje-v1`: añade un marcador
   con `M`, por ejemplo
3. `File > Save Project` (`Ctrl+S` / `Cmd+S`)
4. Sigue trabajando —o espera— hasta pasar el intervalo de respaldo que configuraste
5. Abre en tu explorador de archivos la carpeta del paso 2

Dentro verás carpetas con nombres largos de identificador, y en el último nivel archivos
así:

```
Timeline.20260829081835
```

Es `Timeline.` seguido de `AAAAMMDDHHMMSS`. *Formato verificado en 21.0.4.5, agosto de
2026.*

**Verifica**: existe al menos un archivo con ese nombre y su fecha es de hoy.

> [!TIP]
> Si la carpeta sigue vacía después del intervalo, casi siempre es que Resolve todavía
> no ha tenido que guardar nada: haz un cambio de verdad —mueve un clip, añade un
> marcador— y guarda. Un proyecto que no cambia no genera respaldos.

---

## Paso 4: Exportar el `.drp` de la semana

**Por qué**: es el punto de retorno de la Semana 03, y el que de verdad usarás. Los
respaldos automáticos son la red del día a día; el `.drp` semanal es tu historial.

1. `File > Export Project`
2. Guárdalo como:

```
<ruta-a-BC-Resolve>/04-respaldos/BC-Bootcamp-Resolve-semana03.drp
```

**Verifica**: el archivo existe y pesa más de 0 bytes. Van a ser unos pocos megabytes:
son tus decisiones, no tu vídeo.

---

## Paso 5: Probar el respaldo en una biblioteca aparte

**Por qué**: este es el paso que separa esta práctica de un tutorial cualquiera. Vas a
restaurar el `.drp` **sin tocar** tu proyecto real, en una biblioteca nueva y vacía.

> [!IMPORTANT]
> Se hace en una biblioteca aparte por dos motivos: no puede colisionar con el proyecto
> original, que se llama igual, y así compruebas de paso cómo se crea y se cambia de
> biblioteca, que es la [teoría 02](../1-teoria/02-bibliotecas-de-proyectos.md).

1. Crea antes en tu disco la carpeta
   `<ruta-a-BC-Resolve>/04-respaldos/biblioteca-de-pruebas/`
2. Ve al **Project Manager** y abre la **barra lateral de bibliotecas**
3. Pulsa el botón de añadir (`+`), elige el tipo de biblioteca en **disco**, nómbrala
   `BC-Pruebas-DB` y apunta a la carpeta del paso 1
4. Haz clic sobre `BC-Pruebas-DB`: el Project Manager se queda **vacío**. Es correcto,
   una biblioteca nueva nace sin proyectos
5. Clic derecho sobre el área vacía > importar proyecto, y elige tu
   `BC-Bootcamp-Resolve-semana03.drp`
6. Ábrelo

**Verifica**, dentro del proyecto restaurado:

- La timeline `BC-Montaje-v1` existe
- El bin `BC-Formatos` de la Semana 02 existe con sus cuatro clips
- Los clips **no** están en rojo: el `.drp` no lleva medios, pero las rutas siguen
  siendo válidas porque el material no se ha movido de sitio

Eso último es la lección de la semana entera hecha experimento: el proyecto guarda
referencias; los medios siguen donde estaban.

---

## Paso 6: Volver a la biblioteca de siempre

**Por qué**: si te quedas en la de pruebas, los checks no encontrarán nada y el resto
del bootcamp se hará en el sitio equivocado.

1. Barra lateral de bibliotecas > haz clic sobre tu biblioteca **original**
2. Abre `BC-Bootcamp-Resolve`
3. Comprueba que estás en la **raíz** de la biblioteca y ves los dos proyectos

```bash
python scripts/verificar-semana.py 03
```

**Verifica**: los siete checks en verde.

> [!TIP]
> La biblioteca `BC-Pruebas-DB` se queda ahí, y está bien: es donde probarás los
> respaldos de las siguientes fases sin arriesgar nada. Anótala en tu
> `mapa-de-instalacion.md`.

---

## Paso 7: El archivo completo, con medios

**Por qué**: el `.drp` no lleva vídeo. Para llevarte el trabajo entero a otra máquina, o
para archivarlo cuando termines, hace falta un *Project Archive*.

1. Ve al Project Manager, a tu biblioteca original
2. Clic derecho sobre `BC-Bootcamp-Resolve` > la opción de **archivar el proyecto**
3. Guárdalo en `<ruta-a-BC-Resolve>/04-respaldos/`

> [!WARNING]
> Un *Project Archive* copia **todos los medios que usa el proyecto**. Ahora mismo son
> cuatro archivos y pesará poco. En la Semana 12, con el montaje entero, pesará lo que
> pese tu material: decenas de gigabytes. **No es una operación semanal**: se hace al
> cerrar un trabajo o antes de cambiar de máquina.
>
> Si ahora mismo vas justo de disco, sáltate este paso y anótalo como pendiente. Los
> checks no dependen de él.

**Verifica**: existe una carpeta con extensión `.dra` en `04-respaldos/`, y dentro hay
una copia de tus cuatro clips del banco de formatos.

> [!NOTE]
> Un `.dra` es una **carpeta**, no un archivo. En macOS el sistema la presenta como si
> fuera un paquete único; en Windows y Linux se ve como lo que es.

---

## Paso 8: Completar el mapa

Añade a `mapa-de-instalacion.md` la sección que dejaste pendiente en la práctica 01:

```markdown
## Qué tendría que rehacer a mano en una máquina nueva

- Live Save: activado
- Respaldos de proyecto: activados, N copias diarias
- Ruta de respaldos: <la tuya>
- Biblioteca de pruebas: BC-Pruebas-DB en <ruta>
```

**Verifica**: las cuatro líneas están rellenas con tus valores.

---

## ✅ Resultado

- [ ] Live Save activado
- [ ] Respaldos de proyecto activados, con 7 o más copias diarias
- [ ] Ruta de respaldos en mi disco de trabajo, no en el del sistema
- [ ] He encontrado un archivo `Timeline.<fecha>` generado hoy
- [ ] `BC-Bootcamp-Resolve-semana03.drp` existe en `04-respaldos/`
- [ ] He restaurado ese `.drp` en `BC-Pruebas-DB` y he comprobado que dentro está todo
- [ ] He vuelto a mi biblioteca original y los siete checks siguen en verde
- [ ] El `.dra` existe, o está anotado como pendiente con su motivo
- [ ] `mapa-de-instalacion.md` tiene la sección de preferencias rellena

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| La carpeta de respaldos sigue vacía | No ha habido cambios que guardar, o no pasó el intervalo | Cambia algo de verdad, guarda y espera al intervalo |
| Los respaldos viejos no aparecen en la carpeta nueva | Resolve no mueve lo que ya existía | Se quedan en la antigua. Consérvala hasta que la nueva tenga contenido |
| El `.drp` importado sale con todos los clips en rojo | Los medios se han movido desde la Semana 02 | El proyecto está bien; lo que falla es la ruta. El relink masivo es Semana 30 |
| No encuentro la opción de importar en la biblioteca nueva | Estás pulsando sobre un proyecto en vez de sobre el área vacía | Clic derecho **sobre el fondo** de la rejilla |
| Los checks fallan después del paso 5 | Te quedaste en `BC-Pruebas-DB` | Vuelve a tu biblioteca original desde la barra lateral |
| El archivado se queda a medias o llena el disco | El `.dra` copia todos los medios | Sáltalo por ahora y anótalo como pendiente |
| No sé cuál era mi biblioteca original | No la anotaste en la práctica 02 | Es la que contiene `BC-Bootcamp-Resolve`; haz clic en cada una hasta verlo |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · El Project Manager y dos proyectos](02-project-manager-y-dos-proyectos.md) | **03 · Copias de seguridad de verdad** | [04 · Preferences y carpetas de trabajo](04-preferences-y-carpetas-de-trabajo.md) |

← [Volver a la Semana 03](../README.md)
