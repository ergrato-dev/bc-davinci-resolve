# Práctica 01 — La Edit page sobre tu montaje

> Al terminar habrás recorrido la Edit page entera con tu propia pieza delante, habrás
> comprobado con tus ojos que es la misma timeline que en la Cut page, y tus pistas tendrán
> nombre. Nada de lo que hagas aquí cambia un solo corte.

**Duración estimada**: 50 min
**Prerrequisitos**: [Teoría 01](../1-teoria/01-por-que-existe-la-edit-page.md), [Teoría 02](../1-teoria/02-anatomia-de-la-edit-page.md), [Teoría 04](../1-teoria/04-la-timeline-y-sus-pistas.md)

## Contexto

La primera vez que se abre la Edit page con una pieza de verdad delante, la reacción normal es
buscar el botón de siempre y no encontrarlo. Esta práctica es para que eso pase hoy, sin prisa y
sin nada en juego, en vez de pasar el martes que viene con una escena a medias.

Es la práctica más tranquila de la semana. Léela con Resolve abierto y ve haciendo.

---

## Paso 1: El punto de partida

**Por qué**: las prácticas 02 y 03 crean y montan una timeline nueva. Si algo sale mal, quieres
poder volver al estado de la Semana 07 sin rehacer nada.

1. Abre **`BC-Bootcamp-Resolve`** desde el Project Manager
2. Comprueba que existe **`04-respaldos/BC-Bootcamp-Resolve-semana07.drp`**. Si no está,
   expórtalo ahora con `File > Export Project`
3. Lanza el puente: `Workspace > Scripts > Utility > resolve_bridge`

**Verifica**:

```bash
python scripts/verificar-semana.py 08 --check proyecto-abierto
```

---

## Paso 2: Entrar en la Edit page y comprobar que no ha pasado nada

**Por qué**: el archivo 01 de teoría afirma que las dos páginas trabajan sobre la misma
timeline. Comprobarlo con las manos vale más que leerlo.

1. Abre **`BC-Montaje-v2`** con doble clic en el media pool
2. Ve a la **Cut page** con `Shift+3`
3. Deja el cabezal en un sitio reconocible: un corte concreto, hacia la mitad de la pieza
4. Selecciona un clip
5. Pasa a la **Edit page** con `Shift+4`

**Verifica**: el cabezal está en el mismo fotograma, el mismo clip sigue seleccionado, y la
timeline tiene los mismos cortes en el mismo orden. No ha habido importación, ni conversión, ni
diálogo alguno.

Vuelve a `Shift+3` y a `Shift+4` un par de veces para que se te quede.

---

## Paso 3: Reconocer las cinco zonas

**Por qué**: para no buscar cosas durante las tres semanas siguientes.

Con `BC-Montaje-v2` abierta, localiza y di en voz alta qué es cada cosa:

| Zona | Dónde mirar |
| ---- | ----------- |
| Media pool | Arriba a la izquierda: están tus bins `01-Basicos` … `12-Entregas` |
| Source Viewer | Arriba al centro, a la izquierda. Ahora mismo vacío |
| Timeline Viewer | Arriba al centro, a la derecha. Enseña tu pieza |
| Inspector | Arriba a la derecha. Si no está, ábrelo desde la barra de interfaz |
| Timeline | Abajo, con tus tres pistas de vídeo |

Ahora abre y cierra, uno a uno, los botones de la barra de interfaz: `Media Pool`, `Effects`,
`Index`, `Sound Library`, `Mixer`, `Metadata`, `Inspector`.

**Verifica**: sabes cuál es cuál sin dudar, y la timeline crece cuando cierras paneles.

> [!TIP]
> Si la pantalla se te queda rara en cualquier momento de la semana:
> `Workspace > Reset UI Layout`. No toca el proyecto, solo coloca los paneles.

---

## Paso 4: Ajustar cómo se ve la timeline

**Por qué**: la vista por defecto no es la más útil para trabajar, y cambiarla es lo primero
que hace cualquiera que use esta página a diario.

1. Abre **`Timeline View Options`**, el desplegable del extremo izquierdo de la barra de
   herramientas
2. Prueba las tres formas de dibujar los clips: tira de imágenes, miniatura, minimizado
3. Activa las **ondas de audio**
4. Sube la altura de las **pistas de vídeo** hasta que veas la imagen de los clips
5. Deja las de **audio** a una altura media, donde se lea el nombre de la pista

**Verifica**: ves miniaturas en los clips de vídeo, ondas en los de audio, y los nombres de
todas las pistas.

Prueba también los zoom: `Full Extent Zoom`, `Detail Zoom`, y `Shift+Z` para alternar entre la
pieza entera y el zoom anterior. `Shift+Z` es el atajo que más vas a usar.

---

## Paso 5: Las cabeceras de pista, con tu pieza

**Por qué**: son siete controles y cuatro de ellos tienen consecuencias que no se ven hasta el
render.

Sobre `Video 2` de tu montaje —la de los recursos—, prueba en este orden y **deshaz cada cosa
antes de la siguiente**:

1. Pulsa **`Lock Track`**. Intenta mover un clip de esa pista: no se deja. Míralo en el visor:
   se sigue viendo. Desbloquea
2. Pulsa **`Enable Track`** para apagarla. El visor ahora no enseña los recursos. Vuelve a
   encenderla
3. En `Audio 1`, pulsa **`S`** de solo y reproduce: solo suena esa pista. Quítalo

**Verifica**: puedes explicar con tus palabras la diferencia entre bloquear y apagar, y sabes
cuál de las dos impide que la pista salga en la exportación.

> [!WARNING]
> Antes de terminar el paso, comprueba que **todas** las pistas están encendidas y ninguna en
> solo. Una pista apagada no se exporta, y no hay ningún aviso cuando eso pasa.

---

## Paso 6: El Index

**Por qué**: en una pieza de treinta cortes, buscar a ojo es la forma lenta.

1. Abre **`Index`** desde la barra de interfaz
2. Ve a la pestaña **`Edit Index`**: ahí está la lista de todos los cortes de tu montaje
3. Haz doble clic en una línea de la mitad de la lista: el cabezal salta ahí
4. Ve a la pestaña **`Tracks`**: ahí están todas tus pistas con sus controles

**Verifica**: sabes ir a un corte concreto por su número, sin buscarlo con el ratón.

---

## Paso 7: Los tres interruptores

**Por qué**: cambian el comportamiento de todo lo que hagas después, y se olvidan puestos.

En la barra de herramientas, localiza **`Snapping`**, **`Linked Selection`** y
**`Position Lock`**.

1. Comprueba que `Snapping` está **activado**. Atajo `N`
2. Comprueba que `Linked Selection` está **activado**
3. Comprueba que `Position Lock` está **desactivado**

**Verifica**: ese es el estado con el que se trabaja esta semana. Si algo no se deja mover en
los próximos días, este paso es lo primero que hay que mirar.

---

## Paso 8: Ponerle nombre a las pistas de tu montaje

**Por qué**: es el primer trabajo de verdad de la semana, y el que te va a servir en la Fase 4.
Un nombre de pista se ve en el mezclador y en Fairlight; `Audio 1` no dice nada, `Dialogo` sí.

Con las pistas lo bastante altas para que se lea el nombre:

1. Clic sobre el nombre `Video 1` y escribe **`Continuidad`**, `Return`
2. `Video 2` → **`Recursos`**
3. `Video 3` → **`Titulos`**
4. `Audio 1` → **`Dialogo`**
5. Si tienes más pistas de audio, ponles nombre según lo que lleven: `Ambiente`, `Efectos`

**Sin acentos y sin espacios.** Estos nombres viajan a los archivos de intercambio de la Semana
12, y ahí los acentos dan problemas.

**Verifica**: ninguna pista de `BC-Montaje-v2` se llama ya `Video N` ni `Audio N`.

---

## Paso 9: Guardar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**: la pieza sigue exactamente igual que al empezar la práctica. Lo único que ha
cambiado son los nombres de las pistas y cómo se ve la timeline.

---

## ✅ Resultado

- [ ] `BC-Bootcamp-Resolve` abierto y el puente lanzado
- [ ] El respaldo de la Semana 07 existe en `04-respaldos/`
- [ ] He comprobado con el cabezal que Cut y Edit son la misma timeline
- [ ] Reconozco las cinco zonas sin dudar
- [ ] La timeline se ve con miniaturas, ondas y pistas altas
- [ ] Sé la diferencia entre bloquear y apagar una pista
- [ ] Todas las pistas quedan encendidas y ninguna en solo
- [ ] Sé saltar a un corte desde el `Edit Index`
- [ ] `Snapping` y `Linked Selection` activados, `Position Lock` desactivado
- [ ] Las pistas de `BC-Montaje-v2` tienen nombre propio
- [ ] El montaje no ha cambiado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| No veo el visor de origen | `Single Viewer Mode` está activado | `Workspace > Single Viewer Mode` para quitarlo |
| Ha desaparecido un panel | Está cerrado, no roto | `Workspace > Reset UI Layout` |
| No se leen los nombres de las pistas | La vista está en minimizado, o las pistas son bajas | `Timeline View Options`: tira de imágenes y más altura |
| No puedo mover ningún clip | `Position Lock` activado, o la pista bloqueada | Míralo en la barra y en la cabecera |
| Falta un recurso en el visor | Apagaste `Video 2` y no lo encendiste | Enciende todas las pistas |
| Cada clic corta un clip | Te quedaste en `Blade Edit Mode` | `A` para volver a `Selection Mode` |
| El proyecto abierto no es el mío | Otro proyecto de la biblioteca | Ábrelo desde el Project Manager |
| `proyecto-abierto` falla | El puente no está lanzado | `Workspace > Scripts > Utility > resolve_bridge` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 08](../README.md) | **01 · La Edit page sobre tu montaje** | [02 · La timeline de la escena](02-la-timeline-de-la-escena.md) |

← [Volver a la Semana 08](../README.md)
