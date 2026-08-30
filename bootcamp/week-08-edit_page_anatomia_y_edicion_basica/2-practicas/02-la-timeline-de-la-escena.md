# Práctica 02 — La timeline de la escena

> Al terminar tendrás `BC-Escena-v1`: una timeline nueva, con su estructura de pistas decidida y
> con nombre, y los tres primeros planos de una escena montados con edición de tres puntos y
> destino comprobado.

**Duración estimada**: 50 min
**Prerrequisitos**: [Práctica 01](01-la-edit-page-sobre-tu-montaje.md), [Teoría 05](../1-teoria/05-el-selector-de-pistas-de-origen.md), [Teoría 06](../1-teoria/06-crear-timelines-y-sus-ajustes.md), [Teoría 07](../1-teoria/07-la-edicion-de-tres-puntos.md)

## Contexto

A partir de aquí se monta de otra manera. En la Semana 06 marcabas y apilabas; esta semana
decides **qué trozo, a qué pista y con qué consecuencia**, y lo compruebas antes de pulsar.

Es más lento. Los tres planos de esta práctica te van a llevar más que quince en la Cut page, y
está bien que así sea: lo que se aprende es el procedimiento, no la velocidad.

---

## Paso 1: Elegir la escena

**Por qué**: no vas a remontar la pieza entera. Vas a montar **una escena** con criterio, y esa
escena tiene que dar de sí para ocho planos o más.

Elige un tramo de tu material que cumpla las tres cosas:

1. Tiene **material de sobra**: al menos ocho tomas o momentos distintos aprovechables
2. Tiene **algo que contar** de principio a fin: una acción, una explicación, un recorrido
3. Tiene **sonido propio**: voz, ambiente o los dos

Según tu formato:

| Formato | Qué escena |
| ------- | ---------- |
| **Documental corto** | Un bloque temático de la entrevista, con sus recursos |
| **Videoclip** | Un tramo de una estrofa, con varias tomas del mismo momento |
| **Cortometraje de ficción** | Una escena de diálogo o una acción con varios ángulos |
| **Tutorial** | Un procedimiento completo: preparar, hacer, comprobar |
| **Pieza de viaje** | Una localización: llegada, detalles, salida |

**Verifica**: puedes escribir en una frase qué cuenta la escena, y puedes nombrar ocho planos
que vayan dentro.

---

## Paso 2: Crear `BC-Escena-v1`

**Por qué**: es la timeline que evalúa la semana, y su nombre lo lee el verificador carácter a
carácter.

> [!IMPORTANT]
> Antes de crearla, **selecciona el bin `Master`** en el media pool. Una timeline se guarda en
> el bin que esté seleccionado, y si cae dentro de `02-Entrevista` la vas a buscar durante un
> rato. Además, la Semana 04 dejó `Master` limpio de clips sueltos a propósito: las timelines
> viven ahí.

1. Selecciona **`Master`**
2. `File > New Timeline`, atajo `Ctrl+N` (Win) / `Cmd+N` (Mac)
3. En la ventana `New Timeline Options`:

   | Campo | Valor |
   | ----- | ----- |
   | `Timeline Name` | **`BC-Escena-v1`** |
   | `No. of Video Tracks` | **2** |
   | `No. of Audio Tracks` | **3** |
   | `Audio Track Type` | El que tenga tu material (estéreo, normalmente) |
   | `Empty Timeline` | **marcado** |
   | `Use Custom Settings` | **no lo toques** |

4. **`Create New Timeline`**

> [!WARNING]
> Si desmarcas `Empty Timeline`, la timeline nace con **todo el material de todos tus bins**
> dentro. Si te pasa, bórrala y créala otra vez; no intentes vaciarla a mano.

**Verifica**:

```bash
python scripts/verificar-semana.py 08 --check escena-v1-existe
```

---

## Paso 3: Ponerle nombre a las cinco pistas

**Por qué**: mismo motivo que en la práctica 01, y aquí además el verificador lo comprueba. Una
timeline con las pistas nombradas se lee sola dentro de tres semanas.

Con las pistas lo bastante altas para que se lea el nombre:

| Pista | Nombre | Qué va a llevar |
| ----- | ------ | --------------- |
| `Video 1` | **`Continuidad`** | Los planos que sostienen la escena |
| `Video 2` | **`Recursos`** | Lo que va encima: detalles, insertos |
| `Audio 1` | **`Dialogo`** | La voz de los planos de continuidad |
| `Audio 2` | **`Ambiente`** | El sonido de los recursos y el ambiente |
| `Audio 3` | **`Reserva`** | Vacía esta semana. Es donde irá la música en la Fase 4 |

Sin acentos y sin espacios.

**Verifica**:

```bash
python scripts/verificar-semana.py 08 --check escena-v1-pistas-con-nombre
```

---

## Paso 4: El hábito de los tres segundos

**Por qué**: es el procedimiento que hace que las ediciones caigan donde quieres, y hay que
cogerlo ahora, no cuando ya llevas veinte planos mal puestos.

Antes de **cada** edición de esta semana, mira tres cosas en este orden:

1. **¿Qué hay cargado en el visor de origen?** El nombre está en su barra de título
2. **¿Dónde apuntan los destinos?** En las cabeceras: el icono azul y el rojo, en la misma fila
3. **¿Hay algo apagado?** Lo que no esté resaltado no va a entrar

Colócalo ahora para el primer plano:

- Destino de **vídeo** → `Continuidad`
- Destino de **audio** → `Dialogo`
- Los dos iconos de origen, **encendidos**

**Verifica**: en la cabecera de `Continuidad` hay un icono azul y uno rojo resaltados, y lo
mismo en `Dialogo`. En `Recursos`, `Ambiente` y `Reserva`, no.

---

## Paso 5: El primer plano, con tres puntos

**Por qué**: es la operación central de la semana y conviene hacerla despacio una vez.

1. En el media pool, abre en el **Source Viewer** el clip con el que empieza la escena: doble
   clic
2. Comprueba que el visor de origen tiene el foco. Si dudas, pulsa **`Q`** y mira cuál se
   resalta
3. Limpia los puntos que pudiera haber: **`Alt+X`** (Win) / **`Opt+X`** (Mac)
4. Reproduce, y marca **`I`** donde tiene que empezar el plano y **`O`** donde tiene que acabar
5. Mira el **campo de duración** del visor: te dice cuánto dura lo que has marcado
6. Pasa el foco a la **timeline** con `Q` y pon el cabezal al principio
7. Repasa el hábito de los tres segundos
8. **`F10`** — `Overwrite`

**Verifica**: el plano está en `Continuidad`, su sonido en `Dialogo`, empieza en el primer
fotograma de la timeline y dura lo que decía el campo de duración.

> [!TIP]
> Si al marcar `I` no pasa nada en el visor de origen, el foco estaba en la timeline y acabas de
> poner un punto de entrada ahí. `Alt+X` en la timeline y vuelve a empezar. Esto va a pasarte
> varias veces esta semana; es normal y se cura con la tecla `Q`.

---

## Paso 6: El segundo y el tercero

**Por qué**: repetir el procedimiento hasta que salga sin leerlo.

Para cada uno de los dos planos siguientes:

1. Doble clic en el clip → Source Viewer
2. `Q` para asegurar el foco, `Alt+X` para limpiar
3. `I` y `O`
4. Cabezal de la timeline **al final del último plano**
5. Hábito de los tres segundos
6. `F10`

> [!TIP]
> Para llevar el cabezal al final del último plano sin arrastrar: con el foco en la timeline,
> pulsa la **flecha abajo** para saltar al siguiente punto de corte. La flecha arriba salta al
> anterior.

**Verifica**:

```bash
python scripts/verificar-semana.py 08 --check escena-v1-activa
```

Y a ojo: tres planos seguidos en `Continuidad`, sin huecos entre ellos, con su sonido en
`Dialogo`.

---

## Paso 7: Probar qué pasa cuando el destino está mal

**Por qué**: entender un error a propósito, con red, cuesta dos minutos. Descubrirlo el martes
con la escena a medias cuesta media hora.

1. Cambia el destino de vídeo a **`Recursos`** — `Alt+2` (Win) / `Opt+2` (Mac)
2. Pon el cabezal encima del segundo plano
3. Carga cualquier clip y haz `F10`
4. Mira lo que ha pasado: el plano nuevo está **encima**, tapando el que había
5. **`Ctrl+Z`** (Win) / **`Cmd+Z`** (Mac)
6. Ahora apaga el icono **de audio del origen** y repite la edición en `Continuidad`
7. Mira: entró la imagen y no el sonido. **`Ctrl+Z`**
8. Vuelve a dejarlo todo como estaba: destino en `Continuidad` y `Dialogo`, todo encendido

**Verifica**: la timeline vuelve a tener exactamente tres planos, y sabes reconocer los dos
síntomas que acabas de provocar.

---

## Paso 8: Guardar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 08
```

Cinco o seis en verde. Los que faltan son de las prácticas 03 y 04.

---

## ✅ Resultado

- [ ] Tengo elegida una escena con material para ocho planos o más
- [ ] `BC-Escena-v1` existe, creada desde `Master`, vacía
- [ ] Tiene dos pistas de vídeo y tres de audio
- [ ] Las cinco pistas tienen nombre propio, sin acentos
- [ ] Tres planos montados en `Continuidad`, con su sonido en `Dialogo`
- [ ] Cada uno se montó marcando `I` y `O` en el origen
- [ ] He provocado a propósito un destino mal puesto y sé reconocerlo
- [ ] El proyecto está guardado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| La timeline nació con doscientos clips | `Empty Timeline` desmarcado | Bórrala y créala otra vez |
| No encuentro `BC-Escena-v1` | Cayó en otro bin | Búscala; arrástrala a `Master` |
| Marco `I` y no pasa nada en el origen | El foco estaba en la timeline | `Q`, y `Alt+X` para limpiar el punto que pusiste |
| El plano entró y no se ve | Entró en `Recursos` o en una pista tapada | Mira todas las pistas antes de deshacer |
| El plano entró sin sonido | El icono de audio del origen estaba apagado | Enciéndelo y repite |
| El plano no entró en ningún sitio | Todos los destinos apagados | Enciende el de `Continuidad` |
| Los planos se solapan | El cabezal no estaba al final del anterior | Flecha abajo para saltar al corte |
| Ya no sé en qué estado están los selectores | Demasiados cambios | `Timeline > Source Track Selector > Reset Track Selectors` |
| `escena-v1-pistas-con-nombre` falla | Alguna pista sigue con su nombre por defecto | Repasa las cinco, incluida `Reserva` |
| `escena-v1-activa` falla | Tienes abierta `BC-Montaje-v2` | Doble clic en `BC-Escena-v1` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · La Edit page sobre tu montaje](01-la-edit-page-sobre-tu-montaje.md) | **02 · La timeline de la escena** | [03 · Tres puntos y los modos de edición](03-tres-puntos-y-los-modos-de-edicion.md) |

← [Volver a la Semana 08](../README.md)
