# Práctica 01 — La copia verificada

> Al terminar tendrás todo tu material en su sitio definitivo, con una huella calculada
> de cada archivo, y sabrás en treinta segundos si alguno se corrompe dentro de seis
> meses. No se importa nada todavía: eso es la práctica 02, y va después por un motivo.

**Duración estimada**: 55 min
**Prerrequisitos**: [Teoría 02](../1-teoria/02-media-storage.md), [Teoría 03](../1-teoria/03-el-clone-tool.md), la estructura `BC-Resolve/` de la Semana 03

## Contexto

El orden de la ingesta es copiar, comprobar, importar, organizar y describir. Los dos
primeros pasos son los únicos irreversibles: una tarjeta formateada no vuelve, y un
archivo corrupto que se descubre en la semana doce ya no se puede recuperar del origen.

Por eso esta práctica va primero y por eso no toca Resolve hasta el paso 5.

---

## Paso 1: Dejar el material en su sitio definitivo

**Por qué**: importar escribe una **referencia**, que es la ruta del archivo. Si mueves
la carpeta después, todos los clips se quedan *offline*. El sitio definitivo se decide
ahora, no después.

Crea la estructura del pack, si no la tienes ya, siguiendo
[`docs/pack-de-medios.md`](../../../docs/pack-de-medios.md):

```
<ruta-a-medios>/00-medios-bootcamp/
├── 01-basicos/
├── 02-entrevista/
├── 03-multicamara/
├── 04-log-y-raw/
├── 05-croma/
├── 06-audio/{musica,efectos,ambientes}
├── 07-graficos/
└── 08-material-montado/     ← nueva esta semana, para la práctica 04
```

Y una carpeta más, para tu material propio, fuera del pack común:

```
<ruta-a-medios>/BC-Propio/
```

> [!IMPORTANT]
> **`00-medios-bootcamp/` es material compartido; `BC-Propio/` es tuyo.** Mantenerlos
> separados en el disco es lo que hará que dentro de treinta semanas puedas archivar tu
> pieza sin arrastrar 40 GB de pack común.

**Verifica**: las nueve carpetas existen y están donde van a quedarse para siempre.

---

## Paso 2: Meter dentro lo que hace falta esta semana

**Por qué**: esta semana necesita material real. No mucho, pero sí de verdad: quince
clips no se organizan igual que tres.

| Carpeta | Qué necesitas esta semana | De dónde |
| ------- | ------------------------- | -------- |
| `01-basicos/` | **15-20 clips** cortos y variados | Pexels, Pixabay o Wikimedia Commons |
| `02-entrevista/` | **1 clip** de alguien hablando, 60 s o más | Lo mismo, o grábalo tú |
| `08-material-montado/` | **1 cortometraje completo** con cortes | [Blender Open Movies](https://studio.blender.org/films/) |
| `BC-Propio/` | **10 planos tuyos** de tu pieza | Tu móvil |

> [!WARNING]
> **Nada con copyright.** Ni un tráiler, ni un videoclip, ni "una peli que tengo por
> ahí para practicar". Las cuatro fuentes de la tabla tienen licencia explícita. Es una
> regla del bootcamp y no tiene excepciones.

Si grabas con OBS y tus archivos salen en `.mkv`, **Resolve no los va a importar**:
`Ajustes > Avanzado > Grabación` en OBS, activa el remuxeado automático a `.mp4`. Lo ya
grabado se arregla con `ffmpeg -i entrada.mkv -c copy salida.mp4`.

**Verifica**: cuenta los archivos. Al menos 15 en `01-basicos/`, 1 en `02-entrevista/`,
1 en `08-material-montado/` y 10 en `BC-Propio/`.

---

## Paso 3: Sellar el pack

**Por qué**: es la huella de la [teoría 03](../1-teoria/03-el-clone-tool.md) aplicada a
tu material. A partir de aquí, cualquier corrupción se detecta en treinta segundos en
vez de descubrirse montando.

Apunta la variable al pack y sella:

```bash
export BC_MEDIOS="<ruta-a-medios>/00-medios-bootcamp"   # macOS y Linux
setx BC_MEDIOS "<ruta-a-medios>\00-medios-bootcamp"     # Windows

./scripts/preparar-medios.sh --sellar
```

**Verifica**: existe `00-medios-bootcamp/MANIFIESTO.sha256` y tiene una línea por
archivo. Ahora comprueba que la comprobación funciona:

```bash
./scripts/preparar-medios.sh
```

Debe decir que todo está en orden.

> [!TIP]
> Prueba que el sellado sirve de algo: copia un clip cualquiera a `/tmp`, ábrelo con un
> editor de texto, cambia un carácter, guárdalo, cópialo de vuelta encima del original y
> vuelve a ejecutar el script. Te dirá el nombre exacto del archivo dañado. Después,
> vuelve a poner el original bueno y sella otra vez. Un manifiesto que no has visto
> fallar es una suposición.

---

## Paso 4: La copia de seguridad del material

**Por qué**: un solo disco no es un respaldo. Es el mismo archivo esperando a que falle
ese disco. Y a diferencia del proyecto, que pesa megabytes, el material **no se puede
volver a conseguir** si era tuyo.

> [!WARNING]
> Este es el paso que más gente se salta y el único de la semana con consecuencias
> irreversibles. Tu pieza son nueve meses de trabajo sobre material que grabaste tú.
> Un disco externo barato cuesta menos que volver a rodar un fin de semana.

Copia **`BC-Propio/`** a un segundo soporte: un disco externo, otra unidad interna, o en
el peor de los casos una carpeta de nube. El pack común no hace falta: se vuelve a
descargar.

**Verifica**: sella también la copia y compara. Si tu segunda copia está en un disco
montado, apunta `BC_MEDIOS` allí y ejecuta `./scripts/preparar-medios.sh` con el
manifiesto original al lado. Los dos manifiestos tienen que coincidir línea a línea.

---

## Paso 5: El Clone Tool, aunque no tengas tarjetas

**Por qué**: el día que ingestes de una cámara de verdad, no es el día de aprender la
herramienta. Y aunque tu material venga de descargas, el flujo se practica igual.

1. Abre Resolve y ve a la página **Media** (`Shift+2`)
2. Muestra el panel **`Clone Tool`** desde la barra de la página
3. Añade un trabajo nuevo
4. Arrastra como **origen** la carpeta `BC-Propio/`
5. Arrastra como **destino** una carpeta de prueba vacía, por ejemplo
   `BC-Resolve/99-prueba-clone/`
6. Añade un **segundo destino**: esa es la razón de existir de la herramienta
7. Lanza la clonación y espera al informe

**Verifica**: los dos destinos contienen los mismos archivos que el origen, y el panel
informa de que la verificación fue correcta.

> [!NOTE]
> Los rótulos exactos del panel y de su menú de opciones no se han podido comprobar por
> la API de scripting. Si en tu instalación cambian, la operación es la misma; el
> capítulo *Media Page* del
> [manual oficial](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion)
> los recoge con las capturas de tu versión.

Cuando termines, borra `99-prueba-clone/`: era un ensayo.

---

## Paso 6: Declarar el material en Media Storage

**Por qué**: para poder navegar tu material desde dentro de Resolve, con miniaturas y
viewer, y no desde el diálogo del sistema operativo.

1. `Ctrl+,` (Win) / `Cmd+,` (Mac) para abrir **Preferences**
2. Pestaña **`System`**, sección **`Media Storage`**
3. Añade `<ruta-a-medios>/00-medios-bootcamp/`
4. Añade `<ruta-a-medios>/BC-Propio/`
5. **Comprueba el orden**: `BC-Resolve/` de la Semana 03 sigue siendo la **primera**
   entrada

> [!WARNING]
> El orden importa: la primera entrada de la lista es donde Resolve escribe caché,
> proxies y galería en los proyectos que no tengan Working Folders propias. Si al añadir
> las carpetas nuevas alguna se ha colado arriba, devuélvela abajo.

6. Guarda. Si Resolve pide reiniciar, reinícialo

**Verifica**: en la página Media, el panel `Media Storage` muestra las dos carpetas
nuevas y puedes navegarlas. Selecciona un clip de `01-basicos/` y compruébalo en el
viewer: se ve **sin haberlo importado**.

---

## ✅ Resultado

- [ ] Las nueve carpetas del pack existen y están en su sitio definitivo
- [ ] 15+ clips en `01-basicos/`, 1 en `02-entrevista/`, 1 en `08-material-montado/`
- [ ] 10 planos propios en `BC-Propio/`, todos con licencia clara o grabados por mí
- [ ] `MANIFIESTO.sha256` generado, y **comprobado** ejecutando el script sin argumentos
- [ ] He visto el manifiesto detectar un archivo alterado a propósito
- [ ] `BC-Propio/` copiado a un segundo soporte
- [ ] He hecho un trabajo del Clone Tool con **dos** destinos
- [ ] Las dos carpetas nuevas están en Media Storage, y `BC-Resolve/` sigue la primera

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `preparar-medios.sh` dice que no encuentra el pack | `BC_MEDIOS` no está definida, o apunta mal | Vuelve a exportarla; en Windows, `setx` necesita una terminal nueva |
| El manifiesto marca archivos que no he tocado | El disco o el cable están fallando | Vuelve a copiar desde el origen y sella otra vez; si se repite, cambia el cable antes que el disco |
| Resolve no ve la carpeta de medios | No está en Media Storage, o hace falta reiniciar | `Preferences > System > Media Storage`, y reinicia |
| Los clips de OBS no aparecen al navegar | Son `.mkv`, que Resolve no abre | Remuxea a `.mp4`; ver Semana 02 |
| El Clone Tool no deja arrastrar el origen | Se arrastran **carpetas**, no archivos sueltos | Arrastra la carpeta entera |
| La caché empieza a caer en el disco de medios | Una carpeta nueva se ha puesto la primera de Media Storage | Devuelve `BC-Resolve/` al primer puesto |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · La copia verificada** | [02 · La estructura de bins](02-la-estructura-de-bins.md) |

← [Volver a la Semana 04](../README.md)
