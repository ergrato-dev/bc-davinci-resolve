# 📖 Glosario — Semana 04

> Los términos que introduce esta semana, A-Z. En negrita el término en español; entre
> paréntesis el nombre real en la interfaz de Resolve o en la industria, en inglés.

---

## A

- **`Add Folder into Media Pool`** — La opción del menú contextual de Media Storage que
  mete en el bin activo el contenido de una carpeta, sin bajar a sus subcarpetas.
- **`Add Folder and SubFolders into Media Pool`** — La misma operación recorriendo todo
  lo que cuelga de la carpeta y **creando un bin por cada subcarpeta**. Es lo que
  convierte el orden de tu disco en el orden de tu proyecto de un solo clic, y la razón
  de que ordenar el disco antes de importar no sea trabajo perdido.

## B

- **Bin** (*bin*) — Una carpeta **dentro del proyecto**, no en el disco. Contiene
  referencias a clips, y timelines. Mover un clip de un bin a otro no toca ningún
  archivo. La palabra viene del cajón donde el montaje de cine colgaba los trozos de
  película recortados.
- **Bin activo** (*current bin*) — El bin seleccionado en la lista del media pool. Es
  donde cae todo lo que importes y todo lo que genere una operación como Scene Cut
  Detection. Comprobarlo antes de importar es el hábito que más tiempo ahorra de la
  semana.
- **Bin Master** (*Master*) — La raíz del media pool. Siempre existe y todo lo demás
  cuelga de él. La regla de oficio es no dejar material suelto aquí: solo bins y
  timelines.

## C

- **Clip Color** (*Clip Color*) — Un color asignado a un clip, visible en el media pool
  y también en la timeline cuando lo montas. Un clip tiene **uno solo**: asignar otro
  sustituye al anterior. Se pone con clic derecho > `Clip Color`.
- **Clone Tool** (*Clone Tool*) — El panel de la página Media que copia carpetas
  **verificando** cada archivo por su huella, y que admite varios destinos en un mismo
  trabajo. Es la única herramienta de la página que escribe en el disco.
- **Corrupción silenciosa** (*silent corruption*, *bit rot*) — Un daño en un archivo que
  no produce ningún mensaje de error: el archivo tiene el tamaño correcto, se abre y se
  reproduce, y tiene un trozo destrozado. Solo la detecta una huella.

## D

- **`Description`** (*Description*) — El campo de metadata donde va **prosa**: una frase
  que describa lo que se ve. Se lee, para acordarte. No confundir con `Keywords`, que
  son etiquetas y sí se filtran bien.
- **Descartes, bin de** — La convención de mover a un bin `10-Descartes` el material que
  no sirve, en vez de quitarlo del media pool. Quitarlo pierde sus keywords, su color y
  sus comentarios; moverlo no cuesta nada.

## F

- **Flag** (*Flags*) — Una marca de color sobre un clip que señala **algo pendiente**.
  Un clip puede llevar varios a la vez, y se quitan desde el mismo menú. Es temporal por
  definición: se pone, se cumple y se quita. No confundir con un **marcador**
  (*marker*), que se pega a un punto concreto dentro del clip y lleva texto; los
  marcadores son materia de la Semana 09.

## G

- **`Good Take`** (*Good Take*) — El campo de metadata que marca la toma buena de una
  serie. Se puede usar como regla de smart bin, lo que lo hace especialmente útil en las
  piezas con muchas tomas del mismo plano.

## H

- **Huella** (*checksum*, *hash*) — Un número calculado leyendo todos los bytes de un
  archivo. El mismo archivo da siempre la misma huella, y cambiar un solo bit la cambia
  entera. Es lo que permite comprobar que una copia es idéntica al original. Familias
  habituales: `MD5`, `SHA-1`, `SHA-256`, `xxHash`.

## I

- **Ingesta** (*ingest*) — El proceso completo de meter material en un proyecto: copiar
  del origen a un sitio seguro, comprobar la copia, importar, organizar y describir.
  Cinco pasos, y arrastrar archivos es solo uno de ellos.
- **Importar** (*import*) — Escribir en el media pool una **referencia** a un archivo del
  disco. No copia nada, es instantáneo, y por eso mover la carpeta de material después
  deja los clips *offline*.

## K

- **Keyword** (*Keywords*) — Una etiqueta de texto que escribes sobre un clip en el
  panel Metadata. Se busca, se filtra y alimenta los smart bins. Se escriben en
  minúsculas, sin acentos y en singular, de un vocabulario cerrado.

## M

- **Media pool** (*Media Pool*) — El panel que muestra **el proyecto**: sus bins, sus
  clips y sus timelines. Es lo único de la página Media que viaja dentro del `.drp`.
  Está disponible también en Cut, Edit, Fusion y Fairlight.
- **Media Storage** (*Media Storage*) — Dos cosas con el mismo nombre: el **panel** de la
  página Media que navega tu disco con miniaturas, y la **lista** de
  `Preferences > System > Media Storage` que declara de qué carpetas lee Resolve. La
  primera entrada de la lista es donde el programa escribe por defecto.
- **Metadata** (*metadata*) — La información que describe un clip. Se divide en dos: la
  que **trae el archivo** (codec, resolución, frame rate, fecha, cámara) y la que
  **escribes tú** (`Description`, `Keywords`, `Scene`, `Shot`, `Take`, `Comments`). La
  segunda se guarda en el proyecto, no dentro del `.mp4`, y se pierde si quitas el clip
  del media pool.

## P

- **Pase de diagnóstico** — Nombre que este bootcamp da a la revisión del material recién
  importado en vista de lista, ordenando por `Frame Rate`, `Resolution`, `Video Codec` y
  `Duration` para detectar lo que se sale del estándar antes de empezar a montar.
- **Power Bin** (*Power Bin*) — Un bin cuyo alcance es la **biblioteca de proyectos
  entera**: lo que metas dentro está disponible en todos tus proyectos. Se muestra con
  `View > Show Power Bins`. No viaja dentro del `.drp`, porque pertenece a la
  biblioteca y no al proyecto.

## R

- **Referencia** (*reference*) — La anotación de dónde está un archivo, no una copia de
  él. Es lo que guarda el media pool, y la razón de que un proyecto pese megabytes y de
  que existan los clips *offline*.
- **Remuxear** (*remux*) — Cambiar un archivo de contenedor sin recomprimir el vídeo. Es
  lo que hace falta con los `.mkv` de OBS, que Resolve no importa:
  `ffmpeg -i entrada.mkv -c copy salida.mp4`. Se explicó en la Semana 02.
- **Regla 3-2-1** — La convención de respaldo del oficio: tres copias del material, en
  dos tipos de soporte distintos, y una de ellas fuera del edificio.

## S

- **Scene Cut Detection** (*Scene Cut Detection*) — La operación que analiza un archivo
  ya montado buscando los cortes entre planos, comparando cada fotograma con el
  anterior. Detecta bien los cortes secos, se le escapan los fundidos encadenados y se
  cree cortes los flashes. El resultado son subclips, no archivos nuevos.
- **Smart Bin** (*Smart Bin*) — Una **búsqueda guardada** con forma de bin. No contiene
  clips: muestra los que cumplen sus reglas, en tiempo real. Los clips siguen viviendo
  en su bin de siempre. Sale vacío si la metadata no está escrita.
- **Subclip** (*subclip*) — Una referencia al mismo archivo de siempre, con un punto de
  entrada y uno de salida propios. Cuarenta subclips de un archivo de 500 MB siguen
  ocupando 500 MB en el disco. A fondo en la Semana 05.

## V

- **Vista de lista** (*List View*) — La presentación del media pool con una fila por clip
  y una columna por propiedad. Es donde se comparan clips, se ordena y se detecta el
  material que no encaja. Las columnas se eligen con clic derecho sobre su cabecera.
- **Vista de miniaturas** (*Thumbnail View*) — La presentación con la imagen de cada
  clip. Sirve para reconocer un plano, y para leer de un vistazo los colores y los flags
  de un bin bien marcado.
- **Vocabulario de keywords** — La lista cerrada de diez o quince palabras que usas para
  etiquetar, escrita **antes** de empezar. Sin ella aparecen variantes de la misma
  palabra y ninguna búsqueda devuelve el conjunto completo.

---

## 📚 Ver también

- [`docs/glosario-global.md`](../../../docs/glosario-global.md) — el glosario acumulado
  de todo el bootcamp, con los términos de las semanas anteriores.
- [Glosario de la Semana 03](../../week-03-resolve_21_anatomia_bases_de_datos_y_preferencias/5-glosario/README.md) —
  bibliotecas, Project Manager, respaldos, Preferences y Project Settings.
- [Glosario de la Semana 02](../../week-02-codecs_contenedores_y_flujo_de_datos/5-glosario/README.md) —
  contenedores, codecs, chroma, bit depth y flujo de datos.

---

← [Volver a la Semana 04](../README.md)
