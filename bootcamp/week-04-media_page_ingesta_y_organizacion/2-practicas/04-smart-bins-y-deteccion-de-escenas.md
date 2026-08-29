# Práctica 04 — Smart bins y detección de escenas

> Al terminar tendrás tres smart bins que se mantienen solos y un cortometraje entero
> troceado en sus planos sin haber tocado el disco. Son las dos funciones de la semana
> que parecen magia y son, las dos, consecuencia directa de lo que hiciste en la
> práctica 03.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-metadata-keywords-y-marcas.md), [Teoría 05](../1-teoria/05-los-bins-que-no-son-bins.md), [Teoría 09](../1-teoria/09-scene-cut-detection.md)

## Contexto

Un smart bin no guarda clips: guarda una pregunta. Si la metadata está escrita, la
pregunta se responde sola cada vez que la abres. Si no lo está, sale vacío y parece que
la función no funciona.

Esa es la razón de que esta práctica vaya la última de la semana, y el examen de si la
práctica 03 se hizo bien.

---

## Paso 1: El smart bin que responde una pregunta que te haces de verdad

**Por qué**: la trampa habitual es crear diez smart bins el primer día y no abrir
ninguno. Se crean los que responden preguntas que ya te estás haciendo.

1. Página **Media**, en la lista de bins del media pool
2. Clic derecho sobre un área **vacía** de la lista > opción de añadir un smart bin
3. Nómbralo **`SB-Noche`**
4. Añade una regla: campo `Keywords`, condición `contiene`, valor `noche`
5. Acepta

**Verifica**: el smart bin muestra los clips de noche del proyecto entero, tanto los de
`01-Basicos` como los de `08-Propio`. Y comprueba lo importante: **ábre `01-Basicos` y
mira que esos clips siguen ahí**. No se han movido a ningún sitio.

> [!IMPORTANT]
> Si `SB-Noche` sale vacío, el problema no está aquí: está en la metadata. Vuelve a la
> [práctica 03](03-metadata-keywords-y-marcas.md), paso 3, y comprueba que la palabra
> escrita es exactamente `noche` y no `Noche` ni `nocturno`.

---

## Paso 2: El smart bin de vigilancia

**Por qué**: el pase de diagnóstico de la práctica 02 encontró material que se sale del
estándar. Un smart bin lo mantiene a la vista sin que tengas que acordarte.

1. Crea un smart bin llamado **`SB-Revisar`**
2. Regla: campo `Frame Rate`, condición `no es`, valor `24`

**Verifica**: aparecen exactamente los clips que anotaste en `notas-de-ingesta.md`. Si
aparecen más de los que anotaste, el pase de diagnóstico se te quedó corto: actualiza el
archivo.

> [!TIP]
> Este smart bin no se vacía nunca del todo, y está bien: es una lista de vigilancia, no
> de tareas. En la Semana 05 le darás salida a lo que hay dentro con proxies y medios
> optimizados.

---

## Paso 3: El smart bin de lo que falta por hacer

**Por qué**: es el que de verdad se usa a diario, y el que casi nadie construye.

1. Crea un smart bin llamado **`SB-Sin-describir`**
2. Regla sobre `Keywords`, con la condición que en tu versión signifique **vacío** o
   **no contiene** una de tus palabras comunes

**Verifica**: si la práctica 03 se hizo entera, este bin debería estar **casi vacío**.
Lo que aparezca es tu lista de pendientes; descríbelo ahora, que son dos minutos.

> [!NOTE]
> Las condiciones disponibles para cada campo dependen de la versión y no se han podido
> confirmar por la API de scripting. Abre el desplegable de condiciones y elige la que
> exprese "sin keywords" en tu instalación; si ninguna lo hace, usa `no contiene` con la
> palabra común que pusiste a toda la tanda en el paso 2 de la práctica 03, que da el
> mismo resultado práctico.

---

## Paso 4: Preparar la detección de escenas

**Por qué**: los subclips caen en el **bin activo**. Elegirlo antes es la diferencia
entre cuarenta subclips ordenados y cuarenta subclips en medio de tu material bueno.

1. Selecciona el bin **`09-Escenas`**
2. Desde `Media Storage`, navega a `08-material-montado/` y arrastra el cortometraje al
   media pool. Cae en `09-Escenas`
3. Compruébalo: el clip está ahí y dura varios minutos

**Verifica**: `09-Escenas` tiene un clip largo dentro y sigue siendo el bin
seleccionado.

---

## Paso 5: Detectar los cortes

**Por qué**: es el caso legítimo de la función: te llega la pieza montada y necesitas el
material.

1. Clic derecho sobre el clip largo > **`Scene Cut Detection…`**
2. Se abre una ventana propia. Lanza el análisis
3. Espera. En un corto de tres o cuatro minutos tarda menos de un minuto

**Verifica**: la lista de cortes se ha llenado y la gráfica de diferencias entre
fotogramas muestra picos donde están los cortes.

> [!NOTE]
> Los rótulos exactos de esta ventana no se han podido comprobar por la API de
> scripting. El capítulo *Media Page* del
> [manual oficial](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion)
> los recoge con las capturas de tu versión.

---

## Paso 6: Revisar antes de aceptar

**Por qué**: la detección compara fotogramas consecutivos. Se le escapan los fundidos y
se cree cortes los flashes. Aceptar sin mirar es aceptar esos errores.

1. Recorre la lista y comprueba **tres o cuatro** cortes: colócate en cada uno y mira si
   de verdad hay un cambio de plano ahí
2. Si encuentras uno en mitad de un plano —un flash, un relámpago—, **bórralo**
3. Si ves un fundido encadenado que la detección se saltó, **añade** el corte a mano en
   el fotograma donde tú lo pondrías
4. Cuando la lista te convenza, acepta

**Verifica**: en `09-Escenas` hay ahora varios elementos nuevos. Deben ser **al menos
tres** para que el check de la semana pase.

```bash
python scripts/verificar-semana.py 04 --check bin-escenas
```

---

## Paso 7: Comprobar que son subclips y no archivos

**Por qué**: es la idea que cierra la semana. Todo el media pool son referencias, y esto
lo demuestra de la forma más clara posible.

1. Vista de lista, con la columna **`File Path`** visible
2. Mira los subclips nuevos

**Verifica** dos cosas:

- **Todos comparten el mismo `File Path`**: el del cortometraje original
- **Sus duraciones son distintas**: cada uno es un trozo

Y la comprobación definitiva: mira el tamaño de `08-material-montado/` en tu explorador
de archivos. No ha cambiado. Cuarenta subclips de un archivo de 500 MB siguen siendo
500 MB.

---

## Paso 8: Cerrar la semana

1. Comprueba que estás en `BC-Bootcamp-Resolve` y que Master no tiene clips sueltos
2. Ejecuta la semana entera:

```bash
python scripts/verificar-semana.py 04
```

3. Exporta el respaldo si lo has cambiado desde la práctica 03:
   `File > Export Project` → `04-respaldos/BC-Bootcamp-Resolve-semana04.drp`

**Verifica**: los siete checks en verde.

---

## ✅ Resultado

- [ ] `SB-Noche` existe y muestra clips de más de un bin
- [ ] He comprobado que los clips **no** se han movido de su bin original
- [ ] `SB-Revisar` existe y coincide con `notas-de-ingesta.md`
- [ ] `SB-Sin-describir` existe y está casi vacío
- [ ] El cortometraje está importado en `09-Escenas`
- [ ] He revisado y corregido los cortes **antes** de aceptarlos
- [ ] Hay tres o más subclips en `09-Escenas`
- [ ] Todos comparten `File Path` y el tamaño en disco no ha cambiado
- [ ] Los siete checks de la semana en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El smart bin sale vacío | La metadata no está escrita, o la palabra no coincide | Práctica 03, paso 3. Comprueba mayúsculas y variantes |
| El smart bin devuelve demasiado | La condición es `contiene` donde querías `es` | Edita la regla |
| Al crear el smart bin no encuentro la opción | Hiciste clic derecho sobre un bin, no sobre el área vacía | Clic derecho en el hueco de debajo de la lista de bins |
| Los subclips cayeron en otro bin | `09-Escenas` no era el bin activo al lanzar la detección | Selecciónalos y arrástralos: mover no duplica |
| La detección propone un corte cada dos segundos | El umbral está demasiado bajo para ese material | Súbelo y vuelve a analizar |
| No detecta casi nada | El corto usa fundidos encadenados largos | Es el límite del método. Añade los cortes a mano o usa otro material |
| `bin-escenas` falla con subclips dentro | El bin no se llama `09-Escenas` exacto, o hay menos de tres | Comprueba el nombre y el número |
| Busco los archivos nuevos y no están | No hay archivos nuevos: son referencias | Es lo correcto. Míralo en la columna `File Path` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Metadata, keywords y marcas](03-metadata-keywords-y-marcas.md) | **04 · Smart bins y detección de escenas** | — |

← [Volver a la Semana 04](../README.md)
