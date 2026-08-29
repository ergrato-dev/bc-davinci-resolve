# 📖 Glosario — Semana 03

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre
> paréntesis el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **Archivo de proyecto** (*Project Archive*, `.dra`) — Una carpeta que contiene el
  proyecto **y** una copia de todos los medios que usa, con las rutas ya arregladas. Es
  la caja de mudanza: pesa lo que pese tu material. No confundir con el `.drp`.
- **Atenuado** (*greyed out*) — Un control visible pero desactivado. En Resolve suele
  significar una de dos cosas: que el ajuste ya no se puede cambiar —el
  `Timeline frame rate` con clips dentro— o que es una función de Studio.

## B

- **Base de datos** (*database*) — El nombre que Resolve daba hasta la versión 17 a lo
  que hoy se llama **biblioteca de proyectos**. Mucha documentación y muchos tutoriales
  siguen usando esta palabra.
- **Biblioteca de proyectos** (*Project Library*) — El contenedor donde viven todos tus
  proyectos. Puede ser **local** (carpetas en tu disco), **en red** (sobre PostgreSQL) o
  **en la nube** (Blackmagic Cloud). El Project Manager siempre muestra el contenido de
  una biblioteca.

## C

- **`CacheClip`** — La carpeta que Resolve crea, con ese nombre literal, para guardar la
  caché de render. Se puede borrar entera: es regenerable.
- **Caché de render** (*render cache*) — Trozos de timeline ya calculados y guardados en
  disco para que la reproducción vaya fluida. Puede ocupar decenas de gigabytes y se
  regenera sola. A fondo en la Semana 05.
- **`config.dat`** — El archivo de texto donde Resolve guarda las preferencias de la
  pestaña `System`, entre ellas las rutas de Media Storage. Se lee, no se edita.
- **`config.user.xml`** — El archivo donde Resolve guarda las preferencias de la pestaña
  `User`: Live Save, respaldos, ajustes de edición.

## D

- **`.dra`** — Ver **archivo de proyecto**.
- **`.drp`** (*DaVinci Resolve Project*) — El archivo que produce `Export Project`.
  Contiene el proyecto entero —timelines, grados, media pool— y **ningún medio**. Pesa
  unos pocos megabytes y es el formato de intercambio del día a día.
- **Dynamic Project Switching** (*Dynamic Project Switching*) — Modo que permite tener
  varios proyectos abiertos a la vez y saltar entre ellos al instante. Sirve para copiar
  timelines o nodos de uno a otro. Consume memoria: se enciende para una tarea y se
  apaga.

## F

- **Free** (*DaVinci Resolve*) — La versión gratuita. Se distingue de Studio en
  `Help > About DaVinci Resolve`: si el nombre no lleva la palabra `Studio`, es Free.
  Ningún entregable evaluable del bootcamp depende de Studio.

## G

- **Galería** (*Gallery*) — El almacén de stills de la página Color. Cada still guarda un
  fotograma **con su grado**. No es caché: es trabajo, y no se regenera.
- **`.gallery`** — La carpeta, oculta por empezar por punto, donde Resolve guarda los
  stills de la galería. Nunca se borra para hacer sitio.
- **`guest`** — El usuario por defecto de una biblioteca local. Si nunca has creado
  usuarios en Resolve, todos tus proyectos cuelgan de él.

## L

- **Layout** (*layout*) — La disposición completa de los paneles de la interfaz: cuáles
  están visibles y qué tamaño tiene cada uno. Es de la máquina, no del proyecto.
- **Layout preset** (*Layout Preset*) — Un layout guardado con un nombre, para poder
  volver a él. Se gestiona en `Workspace > Layout Presets`.
- **Live Save** (*Live Save*) — Preferencia que hace que Resolve guarde el proyecto
  continuamente mientras trabajas. Evita perder trabajo por un cierre inesperado; **no**
  permite volver atrás en el tiempo. Para eso están los respaldos.

## M

- **Master Settings** (*Master Settings*) — La primera categoría de `Project Settings`, y
  la que más se usa: formato de timeline, monitorización, medios optimizados y carpetas
  de trabajo.
- **Media Storage** (*Media Storage*) — La lista ordenada de carpetas de las que Resolve
  lee, en `Preferences > System`. La **primera entrada** es la ubicación por defecto de
  todo lo que el programa escribe.

## O

- **Offline** (*Media Offline*) — El estado de un clip cuyo archivo no está donde el
  proyecto dice que está. Se ve en rojo en el media pool y con un aviso en el viewer. No
  es trabajo perdido: es un enlace roto.

## P

- **Panel** (*panel*) — Cada zona de la interfaz: media pool, viewer, inspector,
  timeline, scopes, mezclador, editor de nodos. Se muestran y se ocultan desde el menú
  `Workspace`.
- **`Playback frame rate`** (*Playback frame rate*) — A cuántos frames por segundo se
  **reproduce** la timeline en tu pantalla. No es lo mismo que el `Timeline frame rate`,
  que define cuántos frames tiene tu pieza, y pueden ser distintos.
- **PostgreSQL** (*PostgreSQL*) — Gestor de bases de datos que corre como servicio y
  atiende a varios clientes a la vez. Es lo que hay debajo de una biblioteca de proyectos
  en red.
- **Preferences** (*Preferences*) — Los ajustes que describen **tu ordenador**: GPU,
  memoria, discos, idioma, respaldos. No viajan con el proyecto. Atajo `Ctrl+,` (Win) /
  `Cmd+,` (Mac).
- **Preset de proyecto** (*preset*) — Una combinación guardada de Project Settings, que
  se puede aplicar por defecto a los proyectos nuevos. Es el remedio real contra el
  frame rate mal puesto.
- **`Project.db`** — El archivo SQLite donde vive un proyecto entero dentro de una
  biblioteca local. Pesa unos pocos megabytes y **no se toca a mano nunca**.
- **Project Manager** (*Project Manager*) — La pantalla donde se crean, organizan,
  exportan, archivan y borran proyectos. Se vuelve a ella con el icono de casa o con
  `File > Project Manager`, sin cerrar el proyecto abierto.
- **Project Settings** (*Project Settings*) — Los ajustes que describen **tu vídeo**:
  frame rate, resolución, ciencia de color, carpetas de trabajo. Viajan con el proyecto.
  Atajo `Shift+9`.
- **Proxy** (*proxy media*) — Una copia en baja resolución de un clip, para montar con
  fluidez en máquinas modestas. Es regenerable. A fondo en la Semana 05.

## R

- **Referencia** (*reference*) — Una anotación de dónde está un archivo, no una copia de
  ese archivo. Es lo que guarda el media pool, y explica los clips *offline*.
- **Regenerable** — Todo lo que Resolve puede volver a calcular a partir del proyecto y
  de los medios originales: caché, medios optimizados y proxies. Borrarlo cuesta tiempo
  de procesado, no trabajo.
- **Relink** (*relink*) — Volver a enlazar un clip *offline* con su archivo. La versión
  masiva es materia de la Semana 30.
- **Respaldos de proyecto** (*Project Backups*) — Las copias con fecha que Resolve hace
  solo, en tres escalones: cada pocos minutos, por horas y por días. Permiten **volver
  atrás en el tiempo**, que es lo que Live Save no hace.
- **`Reset UI Layout`** (*Reset UI Layout*) — La opción de `Workspace` que devuelve la
  interfaz a su disposición de fábrica sin tocar el proyecto. La red de seguridad de la
  semana.

## S

- **Scripts, menú** (*`Workspace > Scripts`*) — Donde Resolve lista los scripts
  instalados. El scripting lanzado desde aquí funciona en Free; el lanzado desde una
  terminal es de Studio. De ahí sale el puente del verificador del bootcamp.
- **SQLite** (*SQLite*) — El formato de base de datos en un solo archivo con el que
  Resolve guarda cada proyecto. Copiarlo a mano mientras se escribe lo corrompe.
- **Studio** (*DaVinci Resolve Studio*) — La versión de pago. Añade funciones que
  aceleran el trabajo; casi nunca habilita algo imposible de conseguir de otra forma.

## T

- **`Timeline frame rate`** (*Timeline frame rate*) — Cuántos frames por segundo tiene tu
  pieza. **El único ajuste irreversible del programa**: se congela en cuanto hay un clip
  en el media pool.
- **Timeline backups** (*timeline backups*) — Los respaldos automáticos de timelines, que
  se guardan como archivos llamados `Timeline.` seguido de la fecha y la hora en formato
  `AAAAMMDDHHMMSS`.

## W

- **Working Folders** (*Working Folders*) — El bloque de `Master Settings` que decide
  dónde escribe **este proyecto** su caché, sus stills y sus proxies. Es la excepción a
  la regla de que los discos son cosa de Preferences.
- **Workspace** (*Workspace*) — El menú desde el que se muestran y ocultan paneles, se
  gestionan los layouts, se activa la doble pantalla y se lanzan los scripts.

---

## 📚 Ver también

- [`docs/glosario-global.md`](../../../docs/glosario-global.md) — el glosario acumulado
  de todo el bootcamp, con los términos de las semanas anteriores.
- [Glosario de la Semana 02](../../week-02-codecs_contenedores_y_flujo_de_datos/5-glosario/README.md) —
  contenedores, codecs, chroma, bit depth y flujo de datos.

---

← [Volver a la Semana 03](../README.md)
