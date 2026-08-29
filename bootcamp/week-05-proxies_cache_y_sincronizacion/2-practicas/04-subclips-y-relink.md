# Práctica 04 — Subclips y relink

> Al terminar tendrás la entrevista partida en trozos útiles y, sobre todo, habrás roto un
> proyecto a propósito y lo habrás arreglado. Es la práctica que convierte la timeline
> roja de `Media Offline` en un trámite de un minuto en lugar de una tarde de pánico.

**Duración estimada**: 50 min
**Prerrequisitos**: [Práctica 03](03-sincronizar-y-preparar-multicamara.md), [Teoría 08](../1-teoria/08-subclips.md), [Teoría 09](../1-teoria/09-medios-offline-y-relink.md)

## Contexto

La primera mitad es organización: acotar lo bueno dentro del material largo. La segunda es
un simulacro de incendio, y se hace **en un proyecto de pruebas**, nunca en el del
bootcamp.

---

## Paso 1: Crear el bin de subclips

**Por qué**: los subclips mezclados con el material original convierten un bin ordenado en
un revoltijo de duraciones raras.

1. Página **Media**, clic derecho sobre `Master` > crear un bin nuevo
2. Nómbralo exactamente **`11-Subclips`**
3. Comprueba que cuelga de `Master`, no de otro bin

**Verifica**: el bin aparece en la lista, al nivel de los diez de la Semana 04.

---

## Paso 2: Marcar entrada y salida

**Por qué**: `I` y `O` son dos de los atajos que más vas a usar en todo el bootcamp. Se
usan igual en Media, en Cut, en Edit y en Fairlight.

1. Abre en el visor de origen el clip de `02-Entrevista` con doble clic
2. Reprodúcelo y busca el principio de una respuesta que valga la pena
3. **Un segundo antes** de que empiece a hablar, pulsa `I`
4. **Un segundo después** de que termine la frase, pulsa `O`

**Verifica**: en la barra del visor se ve marcado el tramo entre los dos puntos.

> [!IMPORTANT]
> Ese segundo de margen a cada lado son las **colas**, y no son opcionales. Sin ellas no
> se puede hacer una transición ni ajustar un corte en la Semana 09, y recuperarlas
> significa rehacer el subclip. Un segundo a cada lado, siempre.

---

## Paso 3: Crear el subclip y nombrarlo

**Por qué**: un subclip llamado `entrevista_subclip_1` no es mejor que el archivo de
cuarenta minutos: sigues sin saber qué hay dentro.

1. Selecciona **`11-Subclips`** como bin activo
2. Con el clip y sus puntos marcados, usa `Create Subclip` en el menú contextual del clip
   en el media pool
3. Renombra el subclip inmediatamente, con lo que dice: `entrevista-por-que-empezo`,
   `entrevista-la-anecdota-del-taller`

**Verifica**: el subclip está en `11-Subclips`, con nombre propio y con la duración del
tramo que marcaste, no la del archivo entero.

---

## Paso 4: Cinco subclips

**Por qué**: el check de la semana pide cinco, y cinco es también el mínimo para que la
organización empiece a notarse.

Repite los pasos 2 y 3 hasta tener **cinco subclips**. Si tu entrevista es corta, saca
subclips también del material de `01-Basicos` que dure más de un minuto, o de los ángulos
de `03-Multicamara`.

**Verifica**:

```bash
python scripts/verificar-semana.py 05 --check bin-subclips
```

---

## Paso 5: Comprobar que no has duplicado nada

**Por qué**: es la idea que sostiene todo el media pool desde la Semana 04, y esta es la
demostración más clara que hay.

1. Vista de lista, con la columna **`File Path`** visible
2. Mira los cinco subclips

**Verifica**: todos comparten el `File Path` de su clip padre y tienen duraciones
distintas. Y en el explorador de archivos, la carpeta del material **pesa lo mismo que
antes**.

---

## Paso 6: Describir los subclips

**Por qué**: un subclip es un clip a todos los efectos, y un clip sin keywords no aparece
en ningún smart bin.

1. Selecciona los cinco
2. Panel `Metadata`, keyword común de la tanda: `entrevista`
3. Uno por uno, añade la keyword de contenido que le toque

**Verifica**: `SB-Sin-describir` de la Semana 04 no los muestra.

---

## Paso 7: Preparar el simulacro, en un proyecto aparte

**Por qué**: vas a romper un proyecto a propósito. Eso no se hace nunca en el proyecto que
te importa.

> [!WARNING]
> **Los pasos 7 a 10 se hacen en un proyecto de pruebas, no en `BC-Bootcamp-Resolve`.**
> Vas a mover una carpeta de material en el disco. Si lo haces con el proyecto del
> bootcamp abierto, dejarás offline todo lo que hiciste en la Semana 04, y aunque se
> arregla con el mismo relink que vas a aprender, no hay ninguna razón para pasar por ahí.

1. `File > New Project`, nómbralo **`BC-Pruebas-semana05`**
2. Crea en tu disco una carpeta `BC-Resolve/99-pruebas/` y **copia** dentro tres clips
   cualesquiera —copia, no muevas: el original se queda donde está—
3. Importa esos tres clips al proyecto de pruebas
4. Móntalos en una timeline llamada `BC-Roto-v1`, uno detrás de otro

**Verifica**: la timeline se reproduce y los tres clips se ven.

---

## Paso 8: Romperlo

**Por qué**: ver la timeline roja en un sitio donde no importa es lo que quita el miedo el
día que aparezca donde sí importa.

1. **Cierra Resolve**
2. En el explorador de archivos, renombra la carpeta `99-pruebas/` a `99-pruebas-movida/`
3. Abre Resolve y abre `BC-Pruebas-semana05`

**Verifica**: el media pool marca los tres clips como offline y el visor muestra
`Media Offline` sobre fondo rojo. Comprueba lo importante: **la timeline sigue teniendo
sus tres cortes, con sus duraciones exactas**. No has perdido nada.

---

## Paso 9: Arreglarlo

**Por qué**: es el procedimiento entero, y dura menos de un minuto cuando se sabe.

1. En el media pool, selecciona los tres clips offline
2. Menú contextual > la opción de **relink**
3. En el selector, señala la carpeta `99-pruebas-movida/`

**Verifica**: los tres clips vuelven a estar online y la timeline se reproduce igual que
antes. Los cortes están donde estaban.

---

## Paso 10: El caso que no se arregla

**Por qué**: entender por qué este falla es lo que hace que la regla de "no renombrar
después de importar" se te quede.

1. Cierra Resolve
2. Renombra **uno** de los tres archivos: `plano-07.mp4` → `plano-07-bueno.mp4`
3. Abre el proyecto e intenta el relink señalando la misma carpeta

**Verifica**: los otros dos reenlazan y ese no. El relink busca **por nombre de archivo**,
y ese nombre ya no existe. Arréglalo de las dos maneras posibles, para ver las dos:
devolviéndole el nombre original, o reenlazándolo a mano seleccionando el archivo.

---

## Paso 11: Cerrar la semana

1. Vuelve a **`BC-Bootcamp-Resolve`** y abre la timeline **`BC-Sync-v1`**
2. Comprueba que `Master` no tiene clips sueltos
3. Ejecuta la semana entera:

```bash
python scripts/verificar-semana.py 05
```

4. Exporta el respaldo: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana05.drp`
5. Borra la carpeta `99-pruebas-movida/` y el proyecto `BC-Pruebas-semana05` si no los
   quieres conservar

**Verifica**: los siete checks en verde.

---

## ✅ Resultado

- [ ] `11-Subclips` existe y cuelga de `Master`
- [ ] Cinco subclips, con colas de un segundo a cada lado
- [ ] Todos renombrados con lo que dicen
- [ ] Comparten `File Path` y la carpeta del material pesa lo mismo
- [ ] Los subclips tienen keywords
- [ ] He roto un proyecto de pruebas a propósito y lo he visto offline
- [ ] Lo he reenlazado con relink y ha vuelto todo
- [ ] Sé por qué un archivo renombrado no se reenlaza solo
- [ ] Los siete checks de la semana en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El subclip dura lo mismo que el clip padre | No había puntos de entrada y salida marcados | Marca `I` y `O` en el visor de origen y repite |
| Los subclips caen en otro bin | `11-Subclips` no era el bin activo | Selecciónalos y arrástralos: mover no duplica |
| `bin-subclips` falla con cinco dentro | El nombre no es `11-Subclips` exacto | Compara carácter a carácter |
| No encuentro `Create Subclip` | Hiciste clic derecho en el visor, no en el clip del media pool | Menú contextual sobre el clip en el media pool |
| Tras el relink siguen offline | Señalaste la carpeta equivocada, o los archivos están renombrados | Comprueba la carpeta; si están renombrados, paso 10 |
| El relink reenlazó a un archivo que no era | Dos archivos con el mismo nombre en carpetas distintas | Reenlaza a mano y evita nombres duplicados en tu material |
| Rompí el proyecto del bootcamp sin querer | Moviste la carpeta con `BC-Bootcamp-Resolve` abierto | El mismo relink del paso 9. No has perdido nada |
| `master-limpio` falla de repente | Un subclip o el clip sincronizado cayó en `Master` | Muévelo a su bin |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Sincronizar y preparar multicámara](03-sincronizar-y-preparar-multicamara.md) | **04 · Subclips y relink** | — |

← [Volver a la Semana 05](../README.md)
