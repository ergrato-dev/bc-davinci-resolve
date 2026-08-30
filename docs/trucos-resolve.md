# 🎩 Trucos y atajos, todos juntos

> Cada semana termina con su sección `🎩 Trucos y atajos`. Aquí están todos,
> agrupados por semana, para poder buscarlos sin abrir treinta y seis archivos.

Criterio de admisión: un truco entra si **ahorra tiempo real** o **revela algo que la
interfaz esconde**, y si es estable —un atajo, una ruta de menú, un modificador—. No
entran los consejos genéricos de productividad ni nada que dependa de plugins de
terceros.

---

## Semana 01 — Fundamentos de imagen en movimiento

| Truco | Cómo |
| ----- | ---- |
| Cambiar de página sin ratón | `Shift+2` a `Shift+8`, en el orden de los botones de abajo: Media, Cut, Edit, Fusion, Color, Fairlight, Deliver |
| Ver la versión exacta que tienes | `Help > About DaVinci Resolve`. Si pone solo "DaVinci Resolve" y no "Studio", tienes la gratuita |
| Buscar cualquier atajo por el nombre del comando | `DaVinci Resolve > Keyboard Customization` y escribe en el buscador. Es más rápido que memorizar tablas |
| Saber el frame rate real de un archivo antes de importarlo | Página Media, selecciona el clip y mira la columna *Frame Rate* del media pool, o abre el Metadata panel |
| Cambiar de unidades de tiempo | Clic derecho sobre el contador de timecode del viewer para alternar entre timecode y número de frames |
| Recuperar un layout que has destrozado | `Workspace > Reset UI Layout`. No toca tu proyecto, solo la disposición de los paneles |
| Live Save, para no volver a perder trabajo | `Preferences > User > Project Save and Load > Live Save`. Guarda continuamente mientras trabajas |

---

## Semana 02 — Codecs, contenedores y flujo de datos

| Truco | Cómo |
| ----- | ---- |
| Ver el codec sin salir del media pool | Vista de lista del media pool, clic derecho sobre la cabecera de columnas para añadir las que te interesen |
| Leer el chroma subsampling, que Resolve no muestra | MediaInfo en vista `Tree`, campo `Chroma subsampling`; o `ffprobe` y su campo `pix_fmt` |
| Cambiar de contenedor sin perder calidad | `ffmpeg -i entrada.mkv -c copy salida.mp4`. `-c copy` copia las pistas sin recomprimir |
| Que OBS deje de grabar en `.mkv`, que Resolve no abre | En OBS, `Ajustes > Avanzado > Grabación`, activa el remuxeado automático a `.mp4` |
| Comprobar qué codecs escribe **tu** instalación | Página Deliver, `Render Settings`, desplegables `Format` y `Codec`. Lo que veas ahí es la verdad de tu máquina |
| Saber si el frame rate ya está bloqueado | `File > Project Settings > Master Settings`: si el campo `Timeline frame rate` aparece atenuado, hay clips en el media pool |
| Ver dónde escribe Resolve por defecto | `Preferences > System > Media Storage`. El primer disco de la lista es el que se usa |
| Recuperar espacio de disco sin perder trabajo | `Playback > Delete Render Cache > All`. La caché es regenerable por definición |

---

## Semana 03 — Resolve 21: anatomía, bases de datos y preferencias

| Truco | Cómo |
| ----- | ---- |
| Volver al Project Manager sin cerrar el proyecto | El icono de casa de la esquina inferior derecha, o `File > Project Manager` |
| Copiar una timeline o un nodo de un proyecto a otro | `File > Dynamic Project Switching`, copia en uno, salta y pega en el otro. Apágalo al terminar |
| No volver a pulsar `Ctrl+S` nunca más | `Preferences > User > Project Save and Load`, activa Live Save |
| Darte una semana de historia en vez de dos días | En ese mismo panel, sube el número de copias diarias de respaldo a 7 o más |
| Comprobar que un respaldo sirve de verdad | Crea una biblioteca de disco aparte, importa ahí el `.drp` y ábrelo. Un respaldo sin probar es una suposición |
| Recuperar decenas de GB en diez segundos | `Playback > Delete Render Cache > All`. La caché es regenerable por definición |
| Reconocer un disco donde ha trabajado Resolve | Busca las carpetas `CacheClip` y `.gallery` |
| Volver a las preferencias de fábrica sin perder nada | Con Resolve **cerrado**, renombra la carpeta `Preferences`. Si no era eso, deshaz el renombrado |
| Que los proyectos nuevos nazcan bien configurados | `Project Settings > Presets`: guarda el tuyo y ponlo por defecto |

---

## Semana 04 — Media page: ingesta y organización

| Truco | Cómo |
| ----- | ---- |
| Heredar la estructura de carpetas del disco en bins | Clic derecho sobre la carpeta en Media Storage > `Add Folder and SubFolders into Media Pool` |
| Copiar a dos discos en una sola pasada, con verificación | Añade dos destinos al mismo trabajo del Clone Tool |
| Comprobar en treinta segundos si un archivo se ha corrompido | `./scripts/preparar-medios.sh`, con el pack ya sellado con `--sellar` |
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

## Semana 05 — Proxies, caché y sincronización

| Truco | Cómo |
| ----- | ---- |
| Saber en tres minutos cuál de los tres cuellos de botella tienes | Clip solo, cuatro pistas, y clip con un cambio de `Zoom`. Mira el contador de fps en cada prueba |
| Comprobar que los medios optimizados se usan de verdad | Activa y desactiva `Playback > Use Optimized Media if Available` mientras reproduces |
| Comprobar que los proxies se usan | Cambia de opción en `Playback > Proxy Handling` mientras reproduces |
| Estimar el espacio antes de una tanda grande | Genera un clip, mira lo que ocupa y multiplica por el número de clips |
| Salir del paso sin generar ningún archivo | `Playback > Timeline Proxy Mode` a media o a un cuarto de resolución |
| Ver si la caché está trabajando | La franja fina bajo la regla de tiempo de la timeline |
| Cachear solo lo pesado | `Playback > Render Cache > User` y marca los tramos que quieras |
| Hacer sitio sin perder lo que estás usando | `Playback > Delete Render Cache`, con la opción de borrar solo lo no usado |
| Que la caché no compita con tu material | La carpeta de trabajo, en un disco distinto del material |
| Sincronía a prueba de todo, y gratis | Da una palmada delante de las cámaras al empezar cada toma |
| Comprobar la sincronía al fotograma | Busca una "p" o una "t": el pico de la onda y el cierre de labios, en el mismo fotograma |
| Diagnosticar una deriva en diez segundos | Comprueba el principio y el final del mismo clip |
| Conservar el audio de referencia sin que moleste | Añade el audio bueno como pista extra y silencia la pista de cámara |
| Sincronizar cuando no hubo relojes igualados | Método por sonido o por forma de onda: es el que funciona con material de aficionado |
| Marcar entrada y salida sin ratón | `I` y `O` en el visor de origen. Funciona en todas las páginas |
| Comprobar que un subclip no duplica nada | Vista de lista, columna `File Path`: comparte la ruta de su clip padre |
| Encontrar un subclip dentro de un mes | Nómbralo con la frase que dice, no con el número que le pone Resolve |
| Reenlazar cien clips de una vez | Relink sobre toda la selección y señala la carpeta raíz: busca dentro por nombre de archivo |
| Practicar el relink sin riesgo | En un proyecto de pruebas, desenlazando clips a propósito |
| Saber si el problema son los proxies y no el equipo | Si el material está online y aun así va a saltos, mira el vínculo de los proxies |

---

## Semana 06 — Cut page: edición veloz

| Truco | Cómo |
| ----- | ---- |
| Entrar y salir de la Cut page sin ratón | `Shift+3` para Cut, `Shift+4` para Edit: la timeline es la misma |
| Saltar al minuto cuatro sin buscar | Clic directo en la timeline de arriba, a esa altura |
| Ver el ritmo de tu pieza de un vistazo | La distribución de cortes en la timeline de arriba |
| Recorrer material a tres velocidades | `L` `L` `L` acelera, `K` para, `J` hace lo mismo hacia atrás |
| No dejar huecos invisibles | Imán activado con `N` desde el primer clip |
| Trabajar siempre en el mismo punto de la pantalla | El cabezal de la timeline de detalle no se mueve: aprovéchalo |
| Revisar doscientos clips sin abrir ninguno | `Source Tape` en el visor de la Cut page |
| Reproducir la jornada en el orden en que ocurrió | Ordena el bin por hora de grabación antes de activar el source tape |
| Revisar solo un tipo de material | Selecciona un smart bin de la Semana 04 en vez de un bin |
| Volver a algo que acabas de ver | Modo `Recent 5 Mins` del visor |
| Comparar dos tomas de lo mismo | Modo `Multi Source` |
| Saltarte los silencios de una entrevista | Activa la forma de onda sobre el source tape |
| Ver un montaje de seis minutos en menos de dos | Fast Review sobre la timeline |
| Detectar planos repetidos | En fast review saltan solos: los ves casi seguidos |
| No perder lo que detectas revisando | Marcador con `M` al vuelo, sin parar la revisión |
| Saber dónde va a caer una edición | Mira el indicador inteligente antes de pulsar el botón |
| Forzar que caiga en un corte | Acerca el cabezal a ese corte |
| Forzar que caiga en medio de un plano | Aléjalo de cualquier corte |
| Montar sin miedo a romper nada | Append no desplaza ni machaca: solo añade al final |
| El ciclo más rápido de la semana | Source tape, `I`, `O`, Append, seguir |
| Meter un clip entero sin marcar | No marques `I` ni `O`: entra completo |
| Elegir herramienta de corrección sin dudar | ¿Lo que hay en el destino se queda o se va? |
| Quitar sin dejar agujeros | Borrado con ripple, y comprueba ampliando la vista de detalle |
| No descolocar lo de la pista de arriba | Cierra la estructura de `Video 1` antes de poner nada encima |
| Probar un plano sin arriesgar el montaje | Ponlo en la pista de arriba: quitarlo lo deja como estaba |
| Que un recurso tape de verdad | Que empiece antes del corte y acabe después |
| Ver qué hay debajo de un recurso | Desactiva `Video 2` desde su cabecera y reproduce |
| Comprobar que un sync bin alinea bien | Cabezal en un momento reconocible: ¿coinciden los ángulos? |
| Colocar un ángulo ya sincronizado de un botón | Source Overwrite, que alinea por hora de grabación |
| Que un multicámara no suene a eco | Suena una sola pista de audio: la de la base |
| Comprobar cualquier atajo en tu instalación | `DaVinci Resolve > Keyboard Customization`, busca el comando por nombre |

---

## Semana 07 — Cut page: acabado y quick export

| Truco | Cómo |
| ----- | ---- |
| Decidir si algo toca ahora | ¿Lo que hay debajo se va a mover todavía? Si sí, no lo hagas |
| Congelar el bruto antes de acabarlo | Clic derecho > `Duplicate Timeline`, y trabaja en la copia |
| Encontrar cualquier ajuste de la timeline | Los tres iconos: `Timeline Options`, `Timeline Actions`, `Edit Actions` |
| Saber si un clip tiene cola en dos segundos | Arrastra su borde hacia fuera: si no se mueve, no hay |
| Que una transición quepa siempre | Pídela de 12 fotogramas en vez de 24 |
| Gastar cola de un solo lado | Alineación `Start on Edit` o `End on Edit` en vez de centrada |
| Poner una disolvencia sin ratón | `V` selecciona el corte más cercano, `Ctrl+T` / `Cmd+T` la añade |
| Elegir la alineación desde el teclado | `U` alterna principio, centro y final antes de `Ctrl+T` |
| Quitar una transición | Selecciónala y `Delete`, o el botón `Cut` con el cabezal cerca |
| Ver los dos números de una duración a la vez | Clic derecho > `Change Duration`: segundos y fotogramas |
| Que el botón ponga siempre lo que tú quieres | `Timeline Options > Set Default Transition` |
| Deshacer un experimento masivo | `Timeline Actions > Clear Transition from All Edits` |
| Saber si una transición sobra | Quítala y reproduce: si no la echas de menos, sobraba |
| Que un `Smooth Cut` no se note | Cámbialo a 4 fotogramas nada más ponerlo |
| Juzgar un `Smooth Cut` | A velocidad normal, dos o tres pases, nunca parado |
| Que un plano dure exactamente lo que quieres | Escribe la duración en `Duration`, no el porcentaje |
| Comparar un efecto con y sin él | El interruptor de la izquierda de la categoría, en `Tools` |
| Ver de un vistazo qué clips llevan velocidad | `Timeline Options > Display Speed Keyframes` |
| Ralentización que no se ve | No bajes del 80 % con material grabado a 24 fps |
| Bajar el volumen de un clip | `Tools > Audio` y el deslizador |
| Comprobar si los recursos ensucian la voz | Silencia `Video 2` desde su cabecera y compara |
| Quitar pausas largas de una entrevista | `Clip > Audio Operations > Ripple Delete Silence` |
| Que no te pique el diálogo | Sube `Minimum to Trip` a 24 fotogramas o más |
| Crear la pista de títulos sin menús | Arrastra el primer título a la zona gris de encima de `Video 2` |
| Ver un título antes de colocarlo | `Hover Scrub Preview` y pasa el ratón por la miniatura |
| Escribir el texto donde se ve | Doble clic sobre el texto en el visor |
| Centrar un rótulo sin tocar números | Al arrastrarlo se pega al centro y a los tercios |
| Ver la pieza sin rótulos | Desactiva `Video 3` desde su cabecera |
| Encontrar los flash frames de golpe | `Jump Cuts` a 2 fotogramas y mira los rojos |
| Ver dónde se hace larga tu pieza | Los racimos de gris en la timeline de arriba |
| Detectar planos repetidos | `View > Show Duplicate Frames` |
| Exportar solo un minuto | Marca `I` y `O` en la timeline antes de `File > Quick Export` |
| El preset que abre en todas partes | `H.264 Master` |
| Comprobar que un archivo exportado es válido | Reimpórtalo al proyecto y reprodúcelo |
| Ver si los rótulos se leen de verdad | Míralo en el móvil, no solo en el monitor |
| Comprobar cualquier atajo en tu instalación | `DaVinci Resolve > Keyboard Customization`, busca el comando por nombre |

---

## Semana 08 — Edit page: anatomía y edición básica

| Truco | Cómo |
| ----- | ---- |
| Decidir en qué página trabajar | ¿La frase menciona una pista o un fotograma? Si sí, Edit |
| Comprobar que Cut y Edit son la misma timeline | Mueve el cabezal en una y cambia con `Shift+3` / `Shift+4` |
| Ver la timeline entera y volver al detalle | `Shift+Z` |
| Recuperar la pantalla cuando se ha desordenado | `Workspace > Reset UI Layout` |
| Guardar tu disposición de paneles | `Workspace > Layout Presets > Save Layout As Preset` |
| Volver al modo normal desde cualquier modo | `A` |
| Encontrar un corte por su número | `Index > Edit Index`, doble clic en la línea |
| Manejar muchas pistas sin marearse | `Index > Tracks` |
| Cambiar de visor sin ratón | `Q` |
| Limpiar los puntos antes de cada edición | `Alt+X` (Win) / `Opt+X` (Mac) |
| Ver cuánto dura lo que has marcado | El campo de duración del visor |
| Marcar por sonido y no por imagen | Menú de tres puntos `> Show Full Clip Audio Waveform` |
| Ver la pieza a pantalla completa | `Workspace > Viewer Mode > Cinema Viewer`, atajo `P` |
| Recorrer un clip a la velocidad del gesto | Mantén `C` y mueve el ratón sobre el visor |
| Llevar el cabezal donde está el ratón | `C` sobre la timeline |
| Saltar de corte en corte | Flecha arriba y flecha abajo |
| Bloquear o desbloquear todas las pistas de vídeo | `Alt+Shift+9` (Win) / `Opt+Shift+9` (Mac) |
| Poner varias cabeceras en el mismo estado | Clic sobre un control y arrastra hacia arriba o abajo |
| Limpiar una timeline llena de pistas vacías | Clic derecho en la cabecera `> Delete Empty Tracks` |
| Mandar el vídeo a una pista sin ratón | `Alt+1` … `Alt+8` (Win) / `Opt+1` … `Opt+8` (Mac) |
| Mandar el audio a una pista sin ratón | `Alt+Ctrl+1` … `8` (Win) / `Opt+Cmd+1` … `8` (Mac) |
| Editar un plano sin su sonido | Apaga el icono de audio del origen |
| Elegir qué canal de audio de un clip usar | Clic derecho sobre el icono de audio azul |
| Salir de cualquier lío de destinos | `Timeline > Source Track Selector > Reset Track Selectors` |
| Crear una timeline sin menús | `Ctrl+N` (Win) / `Cmd+N` (Mac) |
| Que la timeline caiga donde quieres | Selecciona el bin **antes** de crearla |
| Tener todas las timelines a la vista | `Preferences > User > Editing > Smart Bin for Timelines` |
| Marcar un punto seguro antes de un cambio grande | `File > Create Timeline Backup` |
| Recuperar una timeline de hace dos horas | Clic derecho `> Restore Timeline Backup` |
| Llevarte solo un montaje a otro proyecto | Exporta un `.drt` |
| Colocar un plano por su final | Marca solo la `O` en la timeline |
| Llenar un hueco exacto | `I` y `O` en la timeline, solo `I` en el origen |
| Meter algo sin comerte nada | `F9`, y comprueba las pistas de encima |
| Sincronizar una acción con un fotograma | `F11`, con los dos cabezales colocados |
| Poner un rótulo encima sin crear la pista a mano | `F12` |
| Ver todos los modos a la vez | Arrastra el clip sobre el visor de timeline |
| Insertar arrastrando | `Ctrl+Shift` (Win) / `Cmd+Shift` (Mac) mientras arrastras |
| Saltarte el imán solo esta vez | `N` mientras estás arrastrando |
| Separar audio de vídeo puntualmente | `Alt` (Win) / `Opt` (Mac) al hacer clic |
| Entender la diferencia entre dos modos | Haz uno, mira, `Ctrl+Z`, haz el otro |
| Comprobar cualquier atajo en tu instalación | `DaVinci Resolve > Keyboard Customization`, busca el comando por nombre |

---

## Semana 09 — Trimming quirúrgico

| Truco | Cómo |
| ----- | ---- |
| Ver la pieza sin la tentación de tocarla | `Workspace > Viewer Mode > Cinema Viewer`, atajo `P` |
| Anotar un problema sin parar la reproducción | `M` |
| Anotar y escribir la nota al momento | `Ctrl+M` (Win) / `Cmd+M` (Mac) |
| Que el marcador vaya a la timeline y no a un clip | Deselecciona antes: `Ctrl+Shift+A` / `Cmd+Shift+A` |
| Saltar de marcador en marcador | `Shift+Flecha arriba` y `Shift+Flecha abajo` |
| Borrar el marcador que hay bajo el cabezal | `Alt+M` (Win) / `Opt+M` (Mac) |
| Marcar un tramo entero | `I`, `O`, clic derecho `> Convert In and Out to Duration Marker` |
| Trabajar con todos los marcadores a la vez | `Index > Markers`; los campos `Name` y `Notes` se editan en la fila |
| Que los marcadores acompañen a los ripples | `Timeline > Ripple Timeline Markers` |
| Volver al modo seguro | `A` |
| Entrar en modo trim | `T` |
| Probar el otro modo solo para este gesto | Mantén pulsada `A` o `T` mientras arrastras |
| Seleccionar el corte más cercano y saltar a él | `V` |
| Seleccionar el clip que cruza el cabezal | `Shift+V` |
| Rotar entre saliente, centrado y entrante | `U` |
| Trimar solo la imagen o solo el sonido | `Alt+U` (Win) / `Opt+U` (Mac) |
| Alternar entre `Slip` y `Slide` | `S`; el icono del botón `Dynamic Trim Mode` dice en cuál estás |
| Mover un fotograma, o cinco | `,` y `.`, o `Shift+,` y `Shift+.` |
| Cambiar cuántos fotogramas son el salto rápido | `Preferences > User > Editing` |
| Trimar por número en vez de a ojo | Selecciona y escribe `-12` o `+1.`, y `Enter` |
| Escuchar el corte en su contexto | `/` |
| Afinar sin parar la reproducción | `Ctrl+/` (Win) / `Cmd+/` (Mac) y luego `/` |
| Reproducir solo el tramo marcado | `Alt+/` (Win) / `Opt+/` (Mac) |
| Ver solo el fotograma del cabezal mientras trimas | Mantén `Shift` |
| Apagar el visor partido del todo | `View > Enable Multiview Edit Preview` |
| Ver cuánta cola te queda al deslizar | El recuadro punteado que aparece al hacer `Slip` |
| Abrir el editor de trim de precisión | Doble clic sobre un corte |
| Abrir el clip original en el fotograma que ves | `Alt` (Win) / `Opt` (Mac) + doble clic |
| Reproducir hacia atrás, parar, hacia delante | `J`, `K`, `L` |
| Cámara lenta con sonido ralentizado | Mantén `K`+`L` |
| Avanzar un fotograma exacto | `K` pulsada y un toque de `L` |
| Trimar rápido sin cambiar de modo | `Ctrl+J` / `Ctrl+L` (Win) · `Cmd+J` / `Cmd+L` (Mac) |
| Entrar y salir del modo dinámico | `W`; el cabezal amarillo dice que estás dentro |
| Recuperar la reproducción sin salir del modo dinámico | `Ctrl+Shift+A` / `Cmd+Shift+A` |
| Borrar un clip cerrando el hueco | `Forward Delete` — `Supr` (Win), `Fn+Supr` (Mac) |
| Llevar un corte seleccionado al cabezal | `E` |
| Que varios clips superpuestos acaben a la vez | Cabezal donde toca y `Shift+]` |
| Que empiecen todos a la vez | `Shift+[` |
| Ripplear hasta el cabezal sea cual sea el modo | `Ctrl+Shift+[` / `]` (Win) · `Cmd+Shift+[` / `]` (Mac) |
| Dejar activo el selector de una sola pista | `Alt` (Win) / `Opt` (Mac) + clic sobre su selector |
| Acotar una operación a un solo clip | Selecciónalo a mano: gana sobre los selectores de pista |
| Poner todas las cabeceras en el mismo estado | Clic sobre un control y arrastra por las demás |
| Suspender el enlace de audio y vídeo solo para este clic | `Alt` (Win) / `Opt` (Mac) + clic |
| Añadir un segundo corte a la selección | `Ctrl` (Win) / `Cmd` (Mac) + clic |
| Saltarse el imán solo durante un arrastre | `N` mientras arrastras |
| Acortar un plano por los dos extremos conservando el centro | Selecciona su entrada y su salida y acércalas |
| Acortar un bloque de rótulos por una cantidad exacta | Selecciona los cortes y arrastra con `Ctrl` / `Cmd` |
| Punto seguro antes de un ripple grande | `File > Create Timeline Backup` |
| Comprobar cualquier atajo en tu instalación | `Alt+Ctrl+K` (Win) / `Opt+Cmd+K` (Mac) |

---

## Semana 10 — Velocidad, transformaciones y estabilización

| Truco | Cómo |
| ----- | ---- |
| Ver la cadencia de rodaje de todo el material de golpe | `Media Pool` en vista de lista, columna `FPS`, y ordena por ella |
| Saber cuántas veces estira un plano | Cadencia de rodaje ÷ cadencia de proyecto |
| Abrir o cerrar los controles de retime | `Ctrl+R` (Win) / `Cmd+R` (Mac) |
| Cerrar los controles sin deshacer nada | `Esc` |
| Congelar el clip entero | `Shift+R` |
| Colocar el cabezal al fotograma antes de congelar | `Flecha izquierda` y `Flecha derecha` |
| Rellenar un hueco con un plano que no da | `I`, `O` y `Shift+F11` |
| Usar el hueco que cruza el cabezal como destino | Borra los puntos con `Alt+X` (Win) / `Opt+X` (Mac) antes del `Fit to Fill` |
| Cambiar la velocidad de varios clips a la vez | Selecciónalos todos y `Clip > Change Clip Speed` |
| Poner una duración exacta en vez de un porcentaje | El campo `Duration` del diálogo o del Inspector |
| Que la voz no suene grave al ralentizar | Casilla `Pitch Correction` |
| Ver de un vistazo qué clips llevan velocidad | Los distintivos de retime, a la izquierda del nombre |
| Leer la velocidad sin abrir nada | Flechas juntas rápido, separadas y amarillas lento, a la izquierda reverse, barras rojas congelado |
| Añadir un punto de velocidad donde está el cabezal | Desplegable de velocidad `> Add Speed Point` |
| Rampa de cinco tramos en un clic | `Speed Ramp >` en cualquier desplegable de velocidad |
| Rebobinado automático | `Rewind >` y el porcentaje |
| Decidir dónde empieza el rebobinado | Coloca el cabezal dentro del tramo antes de aplicarlo |
| Borrar el punto de velocidad correcto | Abre el desplegable que está a su derecha y `Clear Speed Point` |
| Volver un clip al 100 % | `Reset to 100%` en el desplegable de velocidad |
| Quitar la velocidad conservando lo demás | `Edit > Remove Attributes`, con su casilla `Ripple Sequence` |
| Copiar un retime, un reencuadre o una estabilización a otro clip | `Edit > Paste Attributes` — `Alt+V` (Win) / `Opt+V` (Mac) |
| Abrir las curvas de retime | Pestaña `Keyframes` `>` icono de curvas `>` marca `Retime Speed` y `Retime Frame` |
| Añadir un punto a una curva | `Alt` (Win) / `Opt` (Mac) + clic sobre ella |
| Saber el porcentaje exacto de un tramo | Arrástralo en `Retime Speed` y lee el rótulo emergente |
| Comparar dos métodos de relleno sin parar | Bucle con `Ctrl+/` / `Cmd+/` y `/`, y cambia el desplegable mientras suena |
| Cambiar el `Retime Process` de un clip suelto | `Inspector > Video > Retime and Scaling` |
| Cambiarlo para todo el proyecto | `Project Settings > Master Settings > Frame Interpolation` |
| Saber si un clip hereda el ajuste del proyecto | Si pone `Project Settings`, hereda |
| Recuperar la reproducción en tiempo real | `Playback > Render Cache > Smart` |
| Poner el visor al 100 % para juzgar la nitidez | `Alt+Shift+Z` (Win) / `Opt+Shift+Z` (Mac) |
| Encajar la pieza entera en el ancho de la timeline | `Shift+Z` |
| Ampliar o reducir la timeline | `Ctrl+=` / `Ctrl+-` (Win) · `Cmd+=` / `Cmd+-` (Mac) |
| Escribir un valor exacto en un parámetro | Clic sobre el número y teclea |
| Devolver un grupo del Inspector a su valor de fábrica | El icono de reinicio a la derecha del nombre del grupo |
| Ampliar hacia una cara descentrada | Mueve el `Anchor Point` a la cara y luego sube el `Zoom` |
| Estirar o achatar la imagen a propósito | Suelta el enlace entre `Zoom X` y `Zoom Y` |
| Encender los controles gráficos del visor | El botón `Transform/Crop/Dynamic Zoom`, abajo a la izquierda |
| Elegir el modo de overlay por menú | `View > Viewer Overlay` |
| Encender y apagar el overlay que tengas | ``Shift+` `` |
| Restringir un arrastre de texto a un solo eje | Mantén `Shift` |
| Invertir el sentido de un dynamic zoom | El botón `Swap` |
| Que un dynamic zoom no parezca un efecto | `Dynamic Zoom Ease` en `Ease In and Out` |
| Poner un keyframe | El rombo a la derecha del parámetro en el Inspector |
| Saber si el cabezal está sobre un keyframe | El rombo está naranja |
| Saltar al keyframe anterior o siguiente | Las flechas a los lados del rombo, o `[` y `]` |
| Poner keyframes con la pieza en marcha | `Mark > Add Keyframe`, con el atajo que indique el menú |
| Saber qué se va a animar con ese atajo | El orden: retime, curva activa, último control tocado, `Audio Gain` |
| Ver los keyframes bajo el clip sin cambiar de panel | El botón `Show Keyframe Tray` de la barra de la timeline |
| Quitarse de encima las pistas de keyframes vacías | Tres puntos `>` `Display Parameters with Keyframes` |
| Proteger una pista de keyframes terminada | Su candado |
| Dejar una sola pista de keyframes activa | `Alt` (Win) / `Opt` (Mac) + clic sobre su candado |
| Más sitio para keyframear | El icono de expandir: ventana propia, solo en la Edit page |
| Comparar un plano con y sin estabilizar | El interruptor del grupo `Stabilization` |
| Afinar la estabilización sin esperar otro análisis | `Strength` |
| Saber qué controles del estabilizador exigen reanalizar | El modo, `Cropping Ratio` y `Smooth` |
| Conservar una panorámica quitándole el temblor | `Camera Lock` apagado y `Smooth` |
| Clavar un plano como sobre un trípode | `Camera Lock` |
| Ampliar solo donde asoma el borde al estabilizar | `Zoom` apagado y keyframes de `Zoom` en `Transform` |
| Medir cuánto te ha recortado el estabilizador | Apaga y enciende el interruptor mirando un borde |
| Comprobar cualquier atajo en tu instalación | `Alt+Ctrl+K` (Win) / `Opt+Cmd+K` (Mac) |

---

_Las semanas 11 a 36 añadirán aquí sus trucos según se publiquen._


---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
