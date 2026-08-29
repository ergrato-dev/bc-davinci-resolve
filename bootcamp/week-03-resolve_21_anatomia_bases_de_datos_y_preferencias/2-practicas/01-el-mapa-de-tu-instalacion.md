# Práctica 01 — El mapa de tu instalación

> Al terminar sabrás dónde vive de verdad cada pieza de tu Resolve: la biblioteca de
> proyectos, las preferencias y los respaldos automáticos. Y lo tendrás escrito, que es
> lo que te va a salvar el día que cambies de ordenador.

**Duración estimada**: 45 min
**Prerrequisitos**: [Semana 02](../../week-02-codecs_contenedores_y_flujo_de_datos/README.md) cerrada, [Teoría 01](../1-teoria/01-el-modelo-de-datos-de-resolve.md), [Teoría 02](../1-teoria/02-bibliotecas-de-proyectos.md)

## Contexto

Llevas dos semanas usando Resolve sin saber dónde guarda nada. Funciona, hasta que un
día tienes que reinstalar, cambiar de disco o mandarle tu proyecto a alguien, y
descubres que no sabes qué carpeta copiar.

Esta práctica no cambia nada en tu proyecto. Solo mira, y anota. Es la práctica más
aburrida de la semana y la que más veces vas a releer.

> [!NOTE]
> Vas a mirar carpetas del sistema. **Mirar es seguro; tocar no.** No muevas, no
> renombres y no borres nada de lo que veas hoy: la [teoría 01](../1-teoria/01-el-modelo-de-datos-de-resolve.md)
> explica por qué un `Project.db` copiado a mano es un proyecto corrupto.

---

## Paso 1: Comprobar que arrancas de un sitio limpio

**Por qué**: los checks de esta semana leen el proyecto abierto. Si la Semana 02 quedó
a medias, lo que falle hoy no será culpa de hoy.

Abre Resolve, abre `BC-Bootcamp-Resolve` y lanza el puente desde
`Workspace > Scripts > Utility`. Después:

```bash
python scripts/verificar-semana.py 02
```

**Verifica**: los siete checks de la Semana 02 en verde. Si alguno falla, ciérralo antes
de seguir.

---

## Paso 2: Anotar qué versión tienes

**Por qué**: la mitad de las diferencias entre lo que lees y lo que ves en pantalla se
explican por la versión. Tenerla escrita convierte "me sale distinto" en un dato.

1. `Help > About DaVinci Resolve`
2. Anota el **nombre completo** (con o sin la palabra `Studio`) y el **número de
   versión**

Y ahora lo mismo, pero preguntándoselo al programa por script:

```bash
python scripts/verificar-semana.py 03 --check resolve-es-21
```

Ese check lee la operación `ping` del puente, que devuelve `product` y
`resolve_version`. Es el mismo dato que la ventana `About`, pero leído por la API.

**Verifica**: el check en verde, y el número que te devuelve coincide con el de la
ventana.

---

## Paso 3: Localizar tu biblioteca de proyectos

**Por qué**: es la carpeta donde vive tu trabajo de nueve meses. Si un día tienes que
reinstalar el sistema, es lo que hay que poner a salvo antes de nada.

Busca esta ruta en tu sistema:

| Sistema | Ruta |
| ------- | ---- |
| **Windows** | `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Resolve Project Library\` |
| **macOS** | `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Support/Resolve Project Library/` |
| **Linux** | Dentro del directorio de datos de DaVinci Resolve de tu usuario |

> [!TIP]
> En Windows, escribe `%APPDATA%` en la barra de direcciones del explorador y pulsa
> Intro: te lleva a la carpeta correcta sin tener que saber tu nombre de usuario. En
> macOS, la carpeta `~/Library` está oculta: `Cmd+Shift+.` en el Finder la muestra.
>
> Si tu instalación viene de Resolve 17 o anterior, la carpeta puede llamarse
> `Resolve Disk Database`. Es el nombre viejo del mismo sitio.

Dentro, navega hasta encontrar la carpeta de tu proyecto:

```
Resolve Project Library/Resolve Projects/Users/guest/Projects/BC-Bootcamp-Resolve/
```

**Verifica**: dentro hay un archivo llamado `Project.db`. Anota su **tamaño**. Van a ser
unos pocos megabytes, y esa es la lección: ahí dentro están tus dos semanas de trabajo,
y no hay ni un frame de vídeo.

---

## Paso 4: Localizar tus preferencias

**Por qué**: es lo que **no** viaja con el proyecto. El día que configures otra máquina,
esta carpeta es la lista de lo que tendrás que rehacer a mano.

En Windows, `%APPDATA%\Blackmagic Design\DaVinci Resolve\Preferences\`. En macOS y
Linux, una carpeta `Preferences` en el mismo directorio de datos del paso anterior.

Dentro deberías ver, entre otros:

| Archivo | Qué guarda |
| ------- | ---------- |
| `config.dat` | Las preferencias de la pestaña `System` |
| `config.user.xml` | Las preferencias de la pestaña `User` |
| `keyboard.preset.xml` | Tus atajos personalizados |

**Verifica**: los tres archivos existen. Ábre `config.dat` con un editor de texto **en
modo lectura** si tienes curiosidad: verás líneas del tipo `Clave = valor`, y entre
ellas las rutas de tu Media Storage.

> [!WARNING]
> Leer, sí. **Editar, no.** Un error de sintaxis en `config.dat` y Resolve arranca sin
> preferencias. Todo se cambia desde la ventana de Preferences, que es la práctica 04.

---

## Paso 5: Localizar tus respaldos automáticos

**Por qué**: es la carpeta que crece sola y que nadie mira hasta que el disco se llena.
Y es donde está la copia que te va a salvar el día que la necesites.

1. Abre `Preferences` con `Ctrl+,` (Win) / `Cmd+,` (Mac)
2. Pestaña **`User`**, sección **`Project Save and Load`**
3. Localiza la **ruta de los respaldos de proyecto** y cópiala

Por defecto está dentro de la carpeta de vídeos de tu usuario, en
`Resolve Project Backups/`.

Ve a esa carpeta en tu explorador de archivos. Dentro verás carpetas con nombres largos
de identificador —una por proyecto, y dentro otra por timeline— y, en el último nivel,
archivos llamados así:

```
Timeline.20260829062955
Timeline.20260829075505
```

Es `Timeline.` seguido de la fecha y la hora en formato `AAAAMMDDHHMMSS`.

**Verifica**: encuentras al menos una de esas carpetas. Si está vacía, es que los
respaldos automáticos no están activados: se arregla en la
[práctica 03](03-copias-de-seguridad-de-verdad.md), que es justo lo que toca después.

---

## Paso 6: Escribir el mapa

**Por qué**: nada de lo anterior sirve si vive en tu memoria. Este archivo es la
diferencia entre configurar una máquina nueva en diez minutos o en dos horas.

Crea `BC-Resolve/04-respaldos/mapa-de-instalacion.md` con esta plantilla, rellenada con
**tus** rutas:

```markdown
# Mapa de mi instalación de DaVinci Resolve

Fecha: AAAA-MM-DD
Sistema operativo:
Versión de Resolve (Help > About):
¿Free o Studio?:

## Dónde vive qué

| Qué | Ruta en mi máquina |
| --- | ------------------ |
| Biblioteca de proyectos |  |
| Carpeta del proyecto BC-Bootcamp-Resolve |  |
| Tamaño de su Project.db |  |
| Carpeta de Preferences |  |
| Carpeta de respaldos automáticos |  |
| Mi disco de trabajo (BC-Resolve/) |  |

## Qué tendría que rehacer a mano en una máquina nueva

- (lo vas completando en las prácticas 03 y 04)
```

**Verifica**: el archivo existe y las seis rutas están rellenas. Ninguna casilla vacía.

---

## Paso 7: Guardar

`File > Save Project` (`Ctrl+S` / `Cmd+S`).

No has cambiado nada del proyecto, pero es buen hábito y cuesta medio segundo.

---

## ✅ Resultado

- [ ] Los siete checks de la Semana 02 seguían en verde
- [ ] Sé qué versión tengo y si es Free o Studio
- [ ] He encontrado mi biblioteca de proyectos y el `Project.db` de mi proyecto
- [ ] He anotado el tamaño del `Project.db`
- [ ] He encontrado mi carpeta `Preferences` y sus tres archivos
- [ ] He encontrado mi carpeta de respaldos automáticos
- [ ] `mapa-de-instalacion.md` existe con las seis rutas rellenas
- [ ] No he movido, renombrado ni borrado nada de lo que he visto

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| No encuentro la carpeta `Resolve Project Library` | Instalación heredada de una versión antigua | Busca `Resolve Disk Database` en el mismo sitio |
| En macOS no veo `~/Library` | El Finder oculta esa carpeta por defecto | `Cmd+Shift+.` para mostrar los archivos ocultos |
| La carpeta de mi proyecto no está bajo `guest` | Creaste usuarios en la biblioteca | Busca bajo tu nombre de usuario de Resolve, no el del sistema |
| La carpeta de respaldos está vacía | Los Project Backups están desactivados | Se activan en la práctica 03 |
| `resolve-es-21` falla | El puente no está lanzado, o Resolve está cerrado | `Workspace > Scripts > Utility`, y `--doctor` si sigue fallando |
| `Project.db` pesa cientos de MB | Muchos stills de galería, o un proyecto con mucho historial | No es un problema todavía; anótalo y sigue |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · El mapa de tu instalación** | [02 · El Project Manager y dos proyectos](02-project-manager-y-dos-proyectos.md) |

← [Volver a la Semana 03](../README.md)
