# Práctica 04 — Preferences y carpetas de trabajo

> Al terminar, Resolve leerá y escribirá donde tú decidas, no donde le tocó por defecto.
> Y habrás visto aparecer en tu disco las carpetas que el programa crea solo, que es la
> prueba de que la configuración funciona.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-copias-de-seguridad-de-verdad.md), [Teoría 05](../1-teoria/05-preferences-los-ajustes-de-tu-ordenador.md), [Teoría 07](../1-teoria/07-donde-escribe-resolve.md)

## Contexto

Esta es la práctica que evita el problema más común del bootcamp a partir de la
Semana 05: el disco del sistema lleno de caché y de medios optimizados, con el
ordenador entero yendo mal y nadie sabiendo por qué.

Se hace una vez, en una sentada, con un solo reinicio al final.

> [!TIP]
> Ten a mano tu `mapa-de-instalacion.md`: cada ajuste que cambies hoy es una línea que
> tendrías que rehacer a mano en otro ordenador, y por eso se anota.

---

## Paso 1: Poner tu disco de trabajo el primero en Media Storage

**Por qué**: la primera entrada de esa lista es la que Resolve considera su ubicación
por defecto para todo lo que escribe. Si ahí está el disco del sistema, ahí van a caer
decenas de gigabytes de caché.

1. `Ctrl+,` (Win) / `Cmd+,` (Mac), pestaña **`System`**, sección **`Media Storage`**
2. Añade tu carpeta `BC-Resolve/` si no está en la lista
3. **Súbela al primer puesto** de la lista

**Verifica**: `BC-Resolve/` es la primera entrada. Anótalo en el mapa.

> [!WARNING]
> Cambiar Media Storage **pide reiniciar Resolve**. No reinicies todavía: quedan más
> ajustes de esta pestaña y conviene hacer un solo reinicio al final. Hasta que
> reinicies, el ajuste viejo sigue en uso aunque el panel muestre el nuevo.

---

## Paso 2: Leer —no tocar— la memoria y la GPU

**Por qué**: son los dos ajustes que más gente cambia sin saber qué está cambiando, y
los que más problemas causan cuando se tocan a ciegas. Hoy solo se leen y se anotan.

1. Misma pestaña `System`, sección **`Memory and GPU`**
2. Anota en tu mapa:
   - La memoria total del sistema y cuánta tiene asignada Resolve
   - El modo de procesado de GPU y qué tarjeta aparece seleccionada

**Verifica**: las dos líneas están en el mapa. **No cambies nada.**

> [!NOTE]
> Los valores por defecto son razonables en casi todas las máquinas. Si tu reproducción
> va mal, el orden correcto es: primero proxies y caché (Semana 05), y solo después
> tocar estos ajustes con [`docs/hardware-y-rendimiento.md`](../../../docs/hardware-y-rendimiento.md)
> delante.

---

## Paso 3: Mirar las opciones de decodificación

**Por qué**: es la sección que explica por qué el mismo archivo va fluido en un
ordenador y a tirones en otro. Hoy solo la localizas.

1. Pestaña `System`, sección **`Decode Options`**
2. Mira si la aceleración por hardware para decodificar está activada y anótalo

**Verifica**: la línea está en el mapa.

Déjalo como está. Esta casilla se toca en la Semana 05, cuando ya sepas medir si tu
reproducción mejora o empeora; cambiarla ahora sería cambiar algo sin forma de saber si
ha servido.

---

## Paso 4: Reiniciar Resolve

**Por qué**: para que Media Storage se aplique de verdad.

1. `File > Save Project` (`Ctrl+S` / `Cmd+S`)
2. Cierra Resolve del todo
3. Vuelve a abrirlo y abre `BC-Bootcamp-Resolve`

**Verifica**: en la página **Media** (`Shift+2`), el navegador **Media Storage** muestra
tu carpeta `BC-Resolve/` la primera.

---

## Paso 5: Las tres carpetas de trabajo del proyecto

**Por qué**: aquí está la excepción de la semana. Los discos son cosa de Preferences,
**menos** estas tres rutas, que son de proyecto porque cada proyecto puede vivir en un
disco distinto.

1. `File > Project Settings` (`Shift+9`), categoría **`Master Settings`**
2. Baja hasta el bloque **`Working Folders`**
3. Apunta las tres a tu carpeta de caché:

| Ajuste | Ruta |
| ------ | ---- |
| `Cache files location` | `<ruta-a-BC-Resolve>/02-cache/` |
| `Gallery stills location` | `<ruta-a-BC-Resolve>/02-cache/` |
| `Proxy generation location` | `<ruta-a-BC-Resolve>/02-cache/` |

La primera ya la pusiste en la Semana 02; comprueba que sigue bien y completa las otras
dos.

4. Guarda los ajustes

**Verifica**: las tres rutas apuntan a `02-cache/` y ninguna al disco del sistema.

> [!IMPORTANT]
> Estos ajustes viajan en el `.drp`. Cuando abras este proyecto en otra máquina, la ruta
> escrita seguirá siendo esta, y en la otra máquina puede no existir. Es lo primero que
> se revisa al abrir un proyecto ajeno, y es materia de la Semana 30.

---

## Paso 6: Hacer que Resolve escriba, y encontrar lo que escribe

**Por qué**: hasta que no ves las carpetas en tu disco, esto son rutas escritas en un
panel. Ahora vas a obligar a Resolve a usarlas.

### Generar caché de render

1. Menú **`Playback > Render Cache`**, elige el modo **`Smart`**
2. Vuelve a la timeline `BC-Montaje-v1` y déjala reproducir un momento

### Guardar un still de galería

1. Ve a la página **Color** (`Shift+6`) con un clip bajo el cursor
2. Clic derecho sobre el viewer > **`Grab Still`**

> [!TIP]
> Si no ves esa opción con ese nombre, búscala por `Grab Still` en el buscador de
> `Keyboard Customization`: te dirá el atajo y el sitio exacto en tu versión.

### Mirar el disco

Abre `BC-Resolve/02-cache/` en tu explorador de archivos. Deberías ver aparecer:

```
02-cache/
├── CacheClip/     ← la caché de render
└── .gallery/      ← los stills de la galería
```

*Nombres verificados en 21.0.4.5, agosto de 2026.*

**Verifica**: las dos carpetas existen. En macOS y Linux, `.gallery` empieza por punto y
está oculta: `Cmd+Shift+.` en el Finder, o `ls -a` en la terminal.

> [!WARNING]
> Ahora que sabes dónde está: `CacheClip` se puede borrar entera cuando necesites
> espacio, y `Playback > Delete Render Cache > All` hace lo mismo desde dentro del
> programa. Es inmediato y sin deshacer, pero **no destruye trabajo**: la caché se
> regenera sola.
>
> `.gallery`, en cambio, **no se borra nunca**: son stills que guardaste tú, con su
> grado dentro. No se regeneran.

---

## Paso 7: Guardar tu layout

**Por qué**: la disposición de paneles que te resulte cómoda, guardada, deja de perderse
cada vez que tocas algo.

1. Coloca los paneles como te resulte cómodo trabajar en la página Edit
2. `Workspace > Layout Presets > Save Layout Preset`
3. Ponle un nombre: `BC-Montaje`

**Verifica**: el nombre aparece en `Workspace > Layout Presets`. Descoloca algo a
propósito, vuelve a elegirlo desde ahí y comprueba que se recupera.

> [!TIP]
> Si en cualquier momento del bootcamp la interfaz se descoloca sin remedio:
> `Workspace > Reset UI Layout`. No toca el proyecto.

---

## Paso 8: Tu mapa de Free frente a Studio

**Por qué**: cierra el tema de la semana con datos de **tu** instalación, no de una
tabla genérica.

1. `Help > About DaVinci Resolve`: anota el nombre exacto y la versión
2. Lee entero [`docs/free-vs-studio.md`](../../../docs/free-vs-studio.md)
3. Añade a tu mapa **tres** funciones de Studio que crees que echarás de menos en tu
   pieza concreta, y **cuál es la alternativa en Free** de cada una

**Verifica**: las tres líneas están escritas y cada una lleva su alternativa. No vale
"reducción de ruido": vale "reducción de ruido — alternativa: grabar con menos ISO y no
subir tanto las sombras".

---

## Paso 9: Cerrar la semana

```bash
python scripts/verificar-semana.py 03
```

Con `BC-Bootcamp-Resolve` abierto, en la raíz de tu biblioteca original, y el puente
lanzado desde `Workspace > Scripts > Utility`.

**Verifica**: los siete checks en verde.

Y el respaldo, que ya hiciste en la práctica 03. Si has cambiado cosas después, vuelve a
exportarlo: `File > Export Project` →
`04-respaldos/BC-Bootcamp-Resolve-semana03.drp`.

---

## ✅ Resultado

- [ ] `BC-Resolve/` es la primera entrada de Media Storage
- [ ] He anotado memoria, GPU y decodificación sin cambiarlas
- [ ] He reiniciado Resolve una vez, al final de los cambios de `System`
- [ ] Las tres Working Folders apuntan a `02-cache/`
- [ ] Existen `CacheClip/` y `.gallery/` en mi carpeta de caché
- [ ] Tengo guardado el layout `BC-Montaje`
- [ ] He leído `docs/free-vs-studio.md` entero
- [ ] Tres funciones de Studio anotadas con su alternativa en Free
- [ ] Los siete checks de la semana en verde
- [ ] `mapa-de-instalacion.md` completo

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El navegador Media Storage no muestra mi carpeta | No has reiniciado desde el cambio | Cierra Resolve del todo y vuelve a abrirlo |
| No aparece `CacheClip` | El modo de caché está en `Off`, o no se ha reproducido nada | `Playback > Render Cache > Smart`, y reproduce |
| No veo `.gallery` en macOS o Linux | Empieza por punto y está oculta | `Cmd+Shift+.` en el Finder, o `ls -a` |
| La caché sigue cayendo en el disco del sistema | Cambiaste Media Storage pero no las Working Folders del proyecto | Son ajustes distintos: revisa `Master Settings > Working Folders` |
| Resolve va peor después de tocar la GPU | Se cambió un ajuste sin medir antes | Devuélvelo al valor por defecto; ese ajuste es de la Semana 05 |
| No encuentro `Grab Still` | El nombre o el sitio cambian entre versiones | Búscalo en el buscador de `Keyboard Customization` |
| El disco de trabajo se llenó igualmente | El `.dra` de la práctica 03 ocupa lo que ocupa tu material | Muévelo a un disco externo; el `.dra` no vive en el disco de trabajo |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Copias de seguridad de verdad](03-copias-de-seguridad-de-verdad.md) | **04 · Preferences y carpetas de trabajo** | — |

← [Volver a la Semana 03](../README.md)
