# Práctica 03 — Recorrido por las siete páginas

> Al terminar sabrás moverte por Resolve sin ratón, reconocerás qué hace cada página y
> tendrás guardado tu propio layout.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 02](02-crear-el-proyecto-del-bootcamp.md), [Teoría 08](../1-teoria/08-anatomia-de-resolve.md)

## Contexto

Resolve intimida la primera vez porque enseña mucha interfaz de golpe. Esta práctica
desmonta esa sensación: vas a visitar las siete páginas una por una, con el proyecto
vacío, sin la presión de tener que hacer nada.

El objetivo no es aprender a usarlas —eso son 35 semanas— sino **saber dónde está cada
cosa** y perder el miedo a tocar.

Trabajas sobre `BC-Bootcamp-Resolve`, todavía sin ningún clip.

---

## Paso 1: Aprender el único atajo obligatorio de la semana

**Por qué**: cambiarás de página cientos de veces al día durante nueve meses. Medio
segundo cada vez, con el ratón, son horas al final del bootcamp.

Los atajos van en el orden de los botones de abajo, de izquierda a derecha:

| Página | Atajo |
| ------ | ----- |
| Media | `Shift+2` |
| Cut | `Shift+3` |
| Edit | `Shift+4` |
| Fusion | `Shift+5` |
| Color | `Shift+6` |
| Fairlight | `Shift+7` |
| Deliver | `Shift+8` |

Recorre las siete de arriba abajo tres veces seguidas, solo con el teclado, sin
detenerte a mirar nada.

**Verifica**: puedes ir de Media a Deliver y volver sin mirar los botones de abajo.

---

## Paso 2: Media — dónde entra el material

**Por qué**: es la primera página del flujo y la que más determina si un proyecto grande
será manejable.

`Shift+2`. Localiza, sin tocar nada:

- **Media Storage**, arriba a la izquierda: el navegador de tus discos
- **Media Pool**, abajo a la izquierda: los clips **del proyecto**. Ahora está vacío
- Los dos **viewers**, arriba en el centro
- El panel de **Metadata**, a la derecha

> [!IMPORTANT]
> Media Storage y Media Pool parecen lo mismo y no lo son. Media Storage es tu **disco**.
> Media Pool es tu **proyecto**. Arrastrar de uno a otro es "importar", y no copia
> nada: solo crea una referencia.

**Verifica**: sabes decir en qué panel verías un archivo que está en tu disco pero no
en tu proyecto.

---

## Paso 3: Cut y Edit — las dos formas de montar

**Por qué**: son la misma tarea con dos filosofías distintas, y mucha gente ignora Cut
por creerla la versión simplificada.

`Shift+3` para **Cut**. Fíjate en lo que la distingue:

- **Dos timelines a la vez**: arriba el proyecto entero, abajo la zona de trabajo
- Menos paneles, botones más grandes
- Una fila de herramientas de edición rápida en el centro

`Shift+4` para **Edit**. Compara:

- **Una sola timeline**, con más pistas visibles
- **Inspector** a la derecha, con los parámetros de lo seleccionado
- **Effects** a la izquierda
- Barra de herramientas con los modos de selección, trim y cuchilla

**Verifica**: puedes nombrar dos diferencias visibles entre Cut y Edit sin volver a
mirar.

---

## Paso 4: Fusion y Color — las dos páginas de nodos

**Por qué**: son las dos páginas que no funcionan con capas apiladas sino con un grafo,
y ese es el cambio mental más grande del bootcamp. Verlas hoy, aunque estén vacías,
hace que en la semana 16 no parezcan tan ajenas.

`Shift+5` para **Fusion**. Verás el **Flow** (el área del grafo, ahora casi vacía) y,
abajo, el **Inspector** y el editor de splines. Con la timeline vacía solo hay dos nodos:
`MediaIn` y `MediaOut`.

`Shift+6` para **Color**. Localiza:

- La tira de **miniaturas** de clips, arriba
- El **viewer**
- El **Node Graph**, arriba a la derecha: el grafo de este clip
- Las **paletas** de herramientas, abajo: ruedas, curvas, qualifier, windows, tracker
- Los **scopes**, que se abren desde el icono de la esquina inferior derecha

> [!TIP]
> Abre los scopes ahora aunque no haya nada que medir: `Workspace > Video Scopes`, o el
> icono de la esquina. Acostúmbrate a que estén ahí desde el primer día.

**Verifica**: sabes dónde está el Node Graph en Color y dónde el Flow en Fusion.

---

## Paso 5: Fairlight y Deliver — sonido y salida

**Por qué**: son las dos páginas que la gente descubre tarde y de las que más depende que
un trabajo parezca profesional.

`Shift+7` para **Fairlight**. Localiza el **Mixer** a la derecha —con sus faders y
medidores— y la zona de pistas de audio, mucho más alta que en Edit.

`Shift+8` para **Deliver**. Localiza:

- Los **Render Settings**, arriba a la izquierda: presets de plataforma y ajustes
- La **Render Queue**, a la derecha: la cola de trabajos
- El **viewer** con la línea de tiempo de render abajo

**Verifica**: sabes en qué página cambiarías el volumen de una pista y en cuál elegirías
el codec de salida.

---

## Paso 6: Romper y arreglar el layout

**Por qué**: vas a descolocar paneles sin querer muchas veces. Saber que hay una tecla
de emergencia elimina el miedo a tocar.

1. En la página **Edit**, arrastra los separadores entre paneles hasta dejar la interfaz
   incómoda a propósito.
2. Cierra el Inspector y abre el panel de Effects.
3. Ahora recupera todo: **`Workspace > Reset UI Layout`**.

> [!NOTE]
> `Reset UI Layout` **no toca tu proyecto**. Solo la disposición de los paneles. No hay
> forma de perder trabajo con este comando.

**Verifica**: la interfaz vuelve a la disposición por defecto y tu proyecto sigue intacto.

---

## Paso 7: Guardar tu propio layout

**Por qué**: en la Semana 17 querrás los scopes colocados exactamente donde los quieres,
y recolocarlos cada sesión son minutos perdidos todos los días.

1. En la página **Color**, abre los scopes y colócalos donde te resulten cómodos.
2. `Workspace > Layout Presets > Save Layout Preset`.
3. Nómbralo `BC-Color`.

**Verifica**: el preset aparece en `Workspace > Layout Presets` y puedes aplicarlo
después de un `Reset UI Layout`.

---

## Paso 8: Encontrar cualquier atajo

**Por qué**: memorizar tablas de atajos no funciona. Saber buscarlos sí.

Abre `DaVinci Resolve > Keyboard Customization`.

Busca en el campo de búsqueda tres comandos y anota su atajo actual:

1. `Add Marker`
2. `Blade`
3. `Reset UI Layout`

Fíjate también en el desplegable de esquemas de la parte superior: ahí están los presets
de teclado de Premiere Pro, Final Cut Pro 7 y Avid.

> [!WARNING]
> **No cambies el esquema.** Si eres cero absoluto, el esquema nativo de Resolve es el
> que verás en todos los tutoriales y en todo este bootcamp. Cambiarlo ahora te obliga a
> traducir para siempre.

**Verifica**: has anotado los tres atajos y el esquema activo sigue siendo el de
DaVinci Resolve.

---

## ✅ Resultado

- [ ] Recorro las siete páginas solo con el teclado
- [ ] Distingo Media Storage de Media Pool
- [ ] Puedo nombrar dos diferencias entre Cut y Edit
- [ ] Sé dónde está el Node Graph en Color y el Flow en Fusion
- [ ] Sé abrir los scopes
- [ ] Sé en qué página se cambia el volumen y en cuál el codec de salida
- [ ] Sé resetear el layout sin miedo
- [ ] Tengo guardado un Layout Preset llamado `BC-Color`
- [ ] Sé buscar cualquier atajo en Keyboard Customization

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Los atajos `Shift+2`…`Shift+8` no hacen nada | El foco está en un campo de texto | Haz clic en el viewer o en la timeline y repite |
| Falta un panel y no sé cuál cerré | Layout descolocado | `Workspace > Reset UI Layout` |
| La página Fusion está completamente vacía | No hay ningún clip seleccionado en la timeline | Es normal con el proyecto vacío. Verás `MediaIn` y `MediaOut` cuando haya un clip |
| No encuentro `Keyboard Customization` | Está en el menú de la aplicación, no en `File` | `DaVinci Resolve > Keyboard Customization` |
| Los atajos hacen cosas distintas a las del material | El esquema de teclado no es el nativo | En Keyboard Customization, vuelve al esquema `DaVinci Resolve` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · Crear el proyecto del bootcamp](02-crear-el-proyecto-del-bootcamp.md) | **03 · Recorrido por las siete páginas** | [04 · Leer y calcular timecode](04-leer-y-calcular-timecode.md) |

← [Volver a la Semana 01](../README.md)
