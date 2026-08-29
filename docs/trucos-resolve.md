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

_Las semanas 07 a 36 añadirán aquí sus trucos según se publiquen._


---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
