# ⌨️ Atajos de teclado

> El ratón sirve para descubrir dónde están las cosas. El teclado sirve para trabajar.
> La diferencia entre montar con ratón y montar con teclado es un factor de tres.

Este documento crece con el bootcamp: cada semana añade los atajos que ha enseñado,
verificados en la instalación. Aquí está lo transversal.

---

## 1. Antes de memorizar nada: el panel que manda

`DaVinci Resolve > Keyboard Customization` (macOS) ·
`Help`/`DaVinci Resolve > Keyboard Customization` (Windows)

Es un panel buscable con **todos** los comandos y su atajo actual. Cuando el material
diga un atajo y en tu instalación haga otra cosa, esta es la fuente de verdad: busca el
comando por nombre y mira qué tecla tiene asignada.

> [!TIP]
> Úsalo también al revés: busca una acción que hagas mucho con el ratón y comprueba si
> ya tiene atajo. Casi siempre lo tiene.

---

## 2. Si vienes de otro programa: los presets

Resolve trae **esquemas de teclado completos** de otros editores. En la esquina superior
del panel de Keyboard Customization hay un desplegable con, entre otros:

- **DaVinci Resolve** (el propio)
- **Premiere Pro**
- **Final Cut Pro 7**
- **Avid Media Composer**

Cambiar a uno de esos remapea el programa entero a los atajos que ya conoces.

> [!WARNING]
> **No lo hagas si eres cero absoluto.** Si nunca has editado, el esquema de Resolve es
> el que verás en todos los tutoriales, en toda la documentación y en este bootcamp.
> Aprender el nativo desde el principio te ahorra traducir para siempre.
>
> Y si vienes de Premiere o Final Cut: úsalo los primeros días si te desbloquea, pero
> ponte una fecha para volver al nativo. Un editor que solo sabe su esquema importado
> no puede sentarse en la máquina de nadie más.

---

## 3. Los transversales

Estos funcionan en casi todas las páginas.

| Acción | Windows | macOS |
| ------ | ------- | ----- |
| Reproducir / parar | `Espacio` | `Espacio` |
| Retroceder / parar / avanzar (shuttle) | `J` `K` `L` | `J` `K` `L` |
| Un frame atrás / adelante | `←` `→` | `←` `→` |
| Marcar entrada / salida | `I` / `O` | `I` / `O` |
| Añadir marcador | `M` | `M` |
| Deshacer / rehacer | `Ctrl+Z` / `Ctrl+Shift+Z` | `Cmd+Z` / `Cmd+Shift+Z` |
| Guardar proyecto | `Ctrl+S` | `Cmd+S` |

### Cambiar de página

| Página | Atajo |
| ------ | ----- |
| Media | `Shift+2` |
| Cut | `Shift+3` |
| Edit | `Shift+4` |
| Fusion | `Shift+5` |
| Color | `Shift+6` |
| Fairlight | `Shift+7` |
| Deliver | `Shift+8` |

Van en el orden en que aparecen los botones abajo, de izquierda a derecha. Es el único
atajo que conviene memorizar el primer día.

---

## 4. Montaje (páginas Cut y Edit)

| Acción | Atajo | Qué hace |
| ------ | ----- | -------- |
| Insert | `F9` | Mete el clip empujando lo que había a la derecha |
| Overwrite | `F10` | Mete el clip machacando lo que había |
| Replace | `F11` | Sustituye el clip bajo el cursor conservando su duración |
| Place on top | `F12` | Coloca el clip en la pista de encima |
| Modo selección | `A` | El cursor normal |
| Modo trim | `T` | El cursor de recorte |
| Cuchilla | `B` | Cortar clips |
| Alternar imán (*snapping*) | `N` | Que los clips se peguen entre sí o no |

Se explican uno por uno en las Semanas 06, 08 y 09.

### En la Cut page

La Cut page tiene sus **seis** herramientas de edición como botones siempre visibles en la
barra de herramientas: `Smart Insert`, `Append`, `Ripple Overwrite`, `Close Up`,
`Place on Top` y `Source Overwrite`. Se pulsan con el ratón, y sus comandos aparecen por
nombre en `DaVinci Resolve > Keyboard Customization`, que es donde comprobar qué tecla
tiene cada uno en tu instalación.

| Acción | Atajo | Qué hace |
| ------ | ----- | -------- |
| Ir a la Cut page | `Shift+3` | La timeline es la misma que en Edit |
| Marcar entrada / salida | `I` / `O` | Funciona igual sobre un clip y sobre el source tape |
| Alternar el imán | `N` | Déjalo activado toda la primera pasada |
| Recorrer material | `J` `K` `L` | Pulsar `L` o `J` varias veces multiplica la velocidad |

Se explican en la Semana 06.

Y los del acabado, que se explican en la Semana 07:

| Acción | Windows | macOS | Qué hace |
| ------ | ------- | ----- | -------- |
| Seleccionar el punto de corte más cercano | `V` | `V` | El cabezal no tiene que estar exactamente encima |
| Añadir la transición estándar | `Ctrl+T` | `Cmd+T` | Por defecto, un `Cross Dissolve` de un segundo |
| Alternar la alineación del corte | `U` | `U` | Principio, centro o final; pulsado antes de añadir la transición |
| Dividir un clip en el cabezal | `Ctrl+\` | `Cmd+\` | Añade un punto de corte en medio de un clip |
| Copiar / cortar / pegar clips | `Ctrl+C` `Ctrl+X` `Ctrl+V` | `Cmd+C` `Cmd+X` `Cmd+V` | **Pegar sobrescribe** lo que haya en el cabezal |

> [!WARNING]
> En la Cut page, pegar coloca los clips en el fotograma del cabezal, en la misma pista de
> la que se copiaron, y **machaca lo que haya ahí**. Si no quieres perder nada, pega después
> del último clip.

*Verificados en el DaVinci Resolve 21 Reference Manual, capítulos 36 y 38, agosto de 2026.
Gana siempre lo que diga `DaVinci Resolve > Keyboard Customization` en tu instalación.*

---

## 5. Color

| Acción | Windows | macOS | Qué hace |
| ------ | ------- | ----- | -------- |
| Añadir nodo serie | `Alt+S` | `Opt+S` | El nodo nuevo va detrás del actual |
| Añadir nodo paralelo | `Alt+P` | `Opt+P` | El nodo nuevo trabaja en paralelo |
| Añadir nodo layer | `Alt+L` | `Opt+L` | Mezcla por capas en lugar de en serie |

El grafo de nodos entero es la Semana 18.

---

## 6. Cómo se aprenden

No memorizando listas. El método que funciona:

1. Elige **tres** atajos por semana, no más.
2. Prohíbete el ratón para esas tres acciones durante esa semana.
3. La semana siguiente, otros tres. Los anteriores ya son automáticos.

En 36 semanas son más de cien atajos, sin haber memorizado nunca una tabla.

---

> [!NOTE]
> **Si un atajo no coincide con tu instalación**, gana tu instalación: búscalo en
> `Keyboard Customization`. Los esquemas se pueden haber importado, personalizado o
> cambiado entre versiones, y el material puede quedarse atrás antes que el programa.

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
