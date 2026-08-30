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

### Trimming, en la Edit page

Los de la Semana 09. Son los que más se usan de todo el bootcamp a partir de la Fase 3, porque
afinar cortes se hace todas las semanas de aquí a la 36.

| Acción | Windows | macOS | Qué hace |
| ------ | ------- | ----- | -------- |
| Modo selección | `A` | `A` | Los bordes redimensionan y dejan hueco |
| Modo trim | `T` | `T` | Los bordes rippean y los clips deslizan |
| Modo dinámico | `W` | `W` | `J` `K` `L` trimman en vez de reproducir; el cabezal se pone amarillo |
| Alternar slip y slide | `S` | `S` | Con un clip seleccionado en modo trim |
| Seleccionar el corte más cercano | `V` | `V` | Y lleva el cabezal ahí |
| Seleccionar el clip que cruza el cabezal | `Shift+V` | `Shift+V` | O el hueco, si es un hueco |
| Rotar la parte del corte | `U` | `U` | Saliente → centrado → entrante |
| Elegir vídeo, audio o los dos | `Alt+U` | `Opt+U` | Es la puerta al trim asimétrico |
| Mover un fotograma | `,` / `.` | `,` / `.` | Sobre lo que tengas seleccionado |
| Mover cinco fotogramas | `Shift+,` / `Shift+.` | `Shift+,` / `Shift+.` | La cantidad se ajusta en `Preferences > User > Editing` |
| Reproducir alrededor de la selección | `/` | `/` | El pre-roll y el post-roll se ajustan en preferencias |
| Alternar la reproducción en bucle | `Ctrl+/` | `Cmd+/` | Combinado con `/`, permite afinar sin parar |
| Reproducir del punto de entrada al de salida | `Alt+/` | `Opt+/` | |
| Quick trim | `Ctrl+J` / `Ctrl+L` | `Cmd+J` / `Cmd+L` | Trima reproduciendo, solo a velocidad real o más |
| Extend edit | `E` | `E` | Lleva los cortes seleccionados al cabezal |
| Trim start / trim end | `Shift+[` / `Shift+]` | `Shift+[` / `Shift+]` | Redimensionan en modo `A`, rippean en modo `T` |
| Ripple start / end al cabezal | `Ctrl+Shift+[` / `]` | `Cmd+Shift+[` / `]` | Rippean siempre, en cualquier modo |
| Borrar cerrando el hueco | `Supr` | `Fn+Supr` | Es la tecla `Forward Delete`, no la de borrar normal |
| Cortar con ripple | `Ctrl+Shift+X` | `Cmd+Shift+X` | |
| Deseleccionar todo | `Ctrl+Shift+A` | `Cmd+Shift+A` | Necesario antes de anotar con marcadores |
| Selector de pista de vídeo 1 a 9 | `Alt+F1` … `F9` | `Opt+F1` … `F9` | Acota a qué clips afectan los comandos de cabezal |
| Selector de pista de audio 1 a 9 | `Ctrl+Alt+F1` … `F9` | `Cmd+Opt+F1` … `F9` | |

Y los de marcadores, que también son de la Semana 09:

| Acción | Windows | macOS | Qué hace |
| ------ | ------- | ----- | -------- |
| Poner un marcador | `M` | `M` | Va al clip si hay algo seleccionado, y a la timeline si no |
| Poner uno y abrir su diálogo | `Ctrl+M` | `Cmd+M` | Pausa la reproducción y la reanuda al cerrar |
| Editar el marcador seleccionado | `Shift+M` | `Shift+M` | |
| Borrar el marcador bajo el cabezal | `Alt+M` | `Opt+M` | |
| Saltar al marcador anterior / siguiente | `Shift+↑` / `Shift+↓` | `Shift+↑` / `Shift+↓` | Mezcla los de clip y los de timeline |

*Verificados en el DaVinci Resolve 21 Reference Manual, capítulos 48 y 51, agosto de 2026.
Gana siempre lo que diga `DaVinci Resolve > Keyboard Customization` en tu instalación.*

### Velocidad, transformaciones y keyframes, en la Edit page

Los de la Semana 10. Son pocos y los tres primeros se usan a diario.

| Acción | Windows | macOS | Qué hace |
| ------ | ------- | ----- | -------- |
| Abrir o cerrar los `Retime Controls` | `Ctrl+R` | `Cmd+R` | Con el clip seleccionado. Cerrarlos no deshace nada |
| Cerrar los `Retime Controls` | `Esc` | `Esc` | Igual, sin tocar el menú |
| Congelar el clip entero | `Shift+R` | `Shift+R` | Congela el fotograma que haya bajo el cabezal |
| `Fit to Fill` | `Shift+F11` | `Shift+F11` | Retima el clip de origen para llenar el rango de la timeline |
| Borrar los puntos de entrada y salida | `Alt+X` | `Opt+X` | Necesario para que `Fit to Fill` use el hueco del cabezal |
| Pegar atributos | `Alt+V` | `Opt+V` | Copia velocidad, transformación o estabilización a otro clip |
| Encender y apagar el overlay del visor | ``Shift+` `` | ``Shift+` `` | El overlay que tengas seleccionado en `View > Viewer Overlay` |
| Visor al 100 % | `Alt+Shift+Z` | `Opt+Shift+Z` | Para juzgar nitidez y artefactos; `Shift+Z` encaja la pieza en la timeline |
| Ampliar o reducir la timeline | `Ctrl+=` / `Ctrl+-` | `Cmd+=` / `Cmd+-` | |
| Keyframe anterior / siguiente | `[` / `]` | `[` / `]` | Alcanza incluso los keyframes que quedaron fuera del clip |

> [!NOTE]
> `Mark > Add Keyframe` y `Mark > Delete Keyframe` traen atajo asignado, pero el manual lo cita de
> forma inconsistente. **Mira el atajo al lado del comando en el propio menú `Mark`** de tu
> instalación antes de fiarte de ninguna lista, esta incluida.
>
> `Clip > Change Clip Speed` **no** trae atajo de fábrica. Si lo usas mucho, asígnale uno en
> `Keyboard Customization`.

*Verificados en el DaVinci Resolve 21 Reference Manual, capítulos 46, 57, 58 y 60, agosto de 2026.
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
