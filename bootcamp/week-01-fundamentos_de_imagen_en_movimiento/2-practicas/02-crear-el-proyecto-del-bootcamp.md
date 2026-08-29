# Práctica 02 — Crear el proyecto del bootcamp

> Al terminar tendrás `BC-Bootcamp-Resolve` creado, a 24 fps, 1920×1080 y DaVinci YRGB.
> Es el proyecto en el que vas a trabajar las 36 semanas.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 01](01-instalar-y-primer-arranque.md), [Teoría 02](../1-teoria/02-frame-rate.md), [Teoría 04](../1-teoria/04-resolucion.md)

## Contexto

Crear un proyecto en Resolve lleva cinco segundos. Configurarlo bien lleva diez minutos
y ahorra rehacerlo entero más adelante.

Hay un ajuste en esta práctica que **no se puede cambiar después**: el timeline frame
rate. En cuanto haya un solo clip en el media pool, ese campo se bloquea. Por eso esta
práctica va antes que cualquier importación, y por eso el bootcamp no importa ni un clip
en la Semana 01.

---

## Paso 1: Entender dónde estás

**Por qué**: Resolve no guarda un archivo por proyecto. Guarda todos los proyectos
dentro de una **base de datos**. La pantalla que ves al arrancar es el **Project
Manager**, que es el navegador de esa base de datos.

Abre Resolve. Si ya tenías un proyecto abierto, vuelve al Project Manager con el icono
de casa de la esquina inferior derecha, o con `File > Project Manager`.

Fíjate en tres cosas de esa pantalla:

- Arriba a la izquierda, el nombre de la **base de datos** activa
- El área central, con los proyectos existentes
- Abajo, los botones para crear proyecto y crear carpeta

**Verifica**: sabes decir en qué base de datos estás y cuántos proyectos hay en ella.

---

## Paso 2: Crear el proyecto

**Por qué**: el nombre importa. El verificador del bootcamp busca este proyecto por su
nombre exacto; si lo escribes de otra forma, ningún check pasará.

Pulsa **New Project** y escribe **exactamente**:

```
BC-Bootcamp-Resolve
```

Con las mayúsculas y los guiones tal cual. Sin espacios al final.

**Verifica**:

```bash
python scripts/verificar-semana.py 01 --check proyecto-existe
```

Debe salir en verde. Si sale en rojo, revisa la ortografía del nombre en el Project
Manager: casi siempre es un guion bajo en vez de un guion, o una tilde de más.

---

## Paso 3: Fijar el frame rate, antes que nada

**Por qué**: es el único ajuste irreversible del proyecto. Se bloquea en cuanto entra el
primer clip en el media pool. Si lo dejas mal y te das cuenta en la semana cuatro, la
única salida es crear un proyecto nuevo y volver a empezar.

> [!WARNING]
> Este es el paso irreversible de la semana. Comprueba dos veces el valor antes de
> cerrar el cuadro de diálogo. Todavía estás a tiempo: el media pool está vacío.

Abre `File > Project Settings` — atajo `Shift+9`.

En la pestaña **Master Settings**, sección **Timeline Format**:

| Campo | Valor |
| ----- | ----- |
| `Timeline frame rate` | **24** |
| `Playback frame rate` | **24** |

24 fps es el estándar narrativo, funciona en todas las plataformas y es la cadencia con
la que más material libre de práctica te vas a encontrar. El razonamiento completo está
en la [teoría 02](../1-teoria/02-frame-rate.md).

**Verifica**:

```bash
python scripts/verificar-semana.py 01 --check frame-rate
```

---

## Paso 4: Fijar la resolución

**Por qué**: la resolución de timeline determina el coste de cada nodo y cada efecto de
aquí a la semana 36. 1920×1080 va fluido en cualquier máquina que cumpla los mínimos, y
es suficiente para aprenderlo todo.

En la misma pestaña **Master Settings**, sección **Timeline Format**:

| Campo | Valor |
| ----- | ----- |
| `Timeline resolution` | **1920 x 1080 HD** |

Justo debajo verás `Timeline output resolution`. Déjala también en 1920×1080: es la
resolución con la que saldrá el render, y de momento coinciden. En la Semana 28 verás
cuándo conviene que sean distintas.

**Verifica**:

```bash
python scripts/verificar-semana.py 01 --check resolucion
```

> [!NOTE]
> A diferencia del frame rate, **la resolución sí se puede cambiar después**. Cambiarla
> reescala todo y descoloca encuadres y tamaños de texto, así que tampoco es gratis,
> pero no es irreversible.

---

## Paso 5: Fijar la ciencia de color

**Por qué**: la ciencia de color decide cómo interpreta Resolve los valores de tus
clips y cómo los muestra. Cambiarla a mitad de un proyecto cambia el aspecto de todo lo
que ya hayas etalonado.

Ve a la pestaña **Color Management**, y en `Color science` elige:

```
DaVinci YRGB
```

Es el modo manual clásico: tú decides cómo se interpreta cada cosa. No es el más
automático, pero es el que enseña, y es sobre el que se construye la Fase 5 entera.

Los otros dos modos —`DaVinci YRGB Color Managed` y `ACEScct`— existen, resuelven
problemas reales y se estudian a fondo en la
[Semana 16](../../week-16-teoria_del_color_y_gestion_de_color/README.md). Hoy no los
toques.

**Verifica**:

```bash
python scripts/verificar-semana.py 01 --check ciencia-de-color
```

---

## Paso 6: Guardar y comprobar el conjunto

**Por qué**: Live Save está activo desde la práctica 01, pero conviene forzar un guardado
explícito antes de cerrar un cuadro de diálogo importante, y comprobar que el proyecto
abierto es el que crees.

1. Cierra Project Settings con **Save**.
2. `File > Save Project` — atajo `Ctrl+S` (Win) / `Cmd+S` (Mac).
3. Comprueba el nombre del proyecto en la barra de título superior.

**Verifica**: los cinco checks que dependen del proyecto, de una vez:

```bash
python scripts/verificar-semana.py 01
```

Deben pasar `proyecto-existe`, `proyecto-abierto`, `frame-rate`, `resolucion` y
`ciencia-de-color`. Los dos de timeline todavía no: esos son de la práctica 04.

---

## Paso 7: Exportar tu primer respaldo

**Por qué**: la base de datos es cómoda hasta el día que se corrompe. Un `.drp` pesa
poco, se copia a cualquier sitio y es la única forma de sacar un proyecto de Resolve.

`File > Export Project`, y guárdalo en `BC-Resolve/04-respaldos/` como:

```
BC-Bootcamp-Resolve-semana01.drp
```

**Verifica**: el archivo existe y pesa más de 0 bytes.

> [!TIP]
> Repite esto al terminar cada fase del bootcamp. Diez segundos de trabajo que un día
> te devolverán nueve meses.

---

## ✅ Resultado

- [ ] Proyecto `BC-Bootcamp-Resolve` creado, con el nombre exacto
- [ ] `Timeline frame rate` = 24
- [ ] `Playback frame rate` = 24
- [ ] `Timeline resolution` = 1920×1080
- [ ] `Color science` = DaVinci YRGB
- [ ] Proyecto guardado
- [ ] Respaldo `.drp` en `04-respaldos/`
- [ ] `verificar-semana.py 01` pasa los cinco checks de proyecto

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `proyecto-existe` falla | El nombre no coincide carácter a carácter | Renómbralo en el Project Manager: clic derecho sobre el proyecto > Rename |
| `proyecto-abierto` falla pero `proyecto-existe` pasa | El proyecto existe pero no está abierto | Ábrelo desde el Project Manager y repite |
| El campo `Timeline frame rate` aparece atenuado | Ya hay algo en el media pool | No se puede cambiar. Crea un proyecto nuevo, configúralo primero, e importa después |
| `ciencia-de-color` falla y en la UI pone DaVinci YRGB | Elegiste `DaVinci YRGB Color Managed`, que es otro modo | En `Color Management > Color science`, elige el que pone solo `DaVinci YRGB` |
| Los checks fallan con "No puedo hablar con el puente" | El puente no está lanzado, o Resolve está cerrado | `Workspace > Scripts > Utility` dentro de Resolve |
| No encuentro `Project Settings` | Estás en el Project Manager, no dentro de un proyecto | Abre el proyecto primero; `Shift+9` solo funciona dentro |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · Instalar y primer arranque](01-instalar-y-primer-arranque.md) | **02 · Crear el proyecto del bootcamp** | [03 · Recorrido por las siete páginas](03-recorrido-por-las-siete-paginas.md) |

← [Volver a la Semana 01](../README.md)
