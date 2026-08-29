# Práctica 03 — Metadata, keywords y marcas

> Al terminar, los treinta y tantos clips de tu proyecto estarán descritos, etiquetados
> y marcados, y tendrás escrito el vocabulario que usaste. Es la práctica menos vistosa
> de la semana y la que más veces vas a agradecer a partir de la Semana 08.

**Duración estimada**: 50 min
**Prerrequisitos**: [Práctica 02](02-la-estructura-de-bins.md), [Teoría 06](../1-teoria/06-metadata.md), [Teoría 07](../1-teoria/07-keywords-flags-y-colores.md)

## Contexto

Esta práctica no tiene ni un solo check automático, y no es un descuido. La API de
scripting de Resolve puede leer si un bin tiene quince clips; no puede juzgar si tus
keywords sirven para algo. Eso lo evalúa la rúbrica, con criterios observables.

Lo que sí es medible, y lo vas a comprobar tú mismo en el paso 6: si la metadata está
bien escrita, los smart bins de la práctica 04 funcionan a la primera. Si no, salen
vacíos. Ese es el examen real.

---

## Paso 1: Escribir el vocabulario antes de tocar nada

**Por qué**: sin una lista cerrada acabas con `noche`, `nocturno` y `de noche`, y
ninguna búsqueda te devuelve el conjunto entero. La disciplina se rompe siempre en el
mismo sitio: improvisando una palabra nueva sobre la marcha.

Crea `BC-Resolve/04-respaldos/vocabulario-keywords.md` con **diez o quince palabras**.
Punto de partida, a adaptar a tu pieza:

```
Lugar      interior · exterior
Luz        dia · noche · contraluz
Contenido  voz · paisaje · detalle · gente
Camara     fija · mano · movimiento
Estado     bueno · revisar · descarte
```

Tres reglas, y son las que hacen que funcione: **minúsculas, sin acentos, en singular**.

**Verifica**: el archivo existe y no tiene más de quince palabras. Si tiene treinta, no
es un vocabulario: es un texto libre con formato de lista.

---

## Paso 2: Las keywords comunes, de una tanda

**Por qué**: es el paso que convierte dos horas de trabajo en quince minutos. Todo lo
que comparte un grupo entero se escribe **una vez**.

1. Página **Media**, abre el bin `01-Basicos`
2. Muestra el panel **`Metadata`** desde la barra de la página
3. En su desplegable de conjuntos, elige el de **plano y escena** (`Shot & Scene`)
4. Selecciona **todos** los clips del bin (`Ctrl+A` con el media pool enfocado)
5. En el campo `Keywords`, escribe lo que sea cierto para todos. Si son clips del pack,
   por ejemplo `pack`
6. Aplica

**Verifica**: añade la columna `Keywords` en la vista de lista. Los quince clips tienen
la palabra.

> [!IMPORTANT]
> Si al escribir con varios clips seleccionados solo cambia uno, es que la selección se
> perdió al pinchar en el panel. Vuelve a seleccionar en el media pool y escribe sin
> deseleccionar por el camino.

---

## Paso 3: Las keywords por bloques

**Por qué**: aquí es donde la metadata empieza a valer. Un mismo bin tiene grupos
distintos, y cada grupo comparte dos o tres palabras.

Trabaja por **selecciones medianas**, no clip a clip:

1. Selecciona todos los clips de exterior → `exterior`
2. De esos, los de noche → `noche`
3. Los que tengan a alguien hablando → `voz`
4. Los planos fijos → `fija`; los de cámara en mano → `mano`

Repite lo mismo en `08-Propio` con tu material.

**Verifica**: ordena la lista por la columna `Keywords`. Ningún clip debe quedarse con
la palabra común y nada más; todos tienen al menos dos o tres.

---

## Paso 4: Las descripciones, solo donde hagan falta

**Por qué**: `Description` es prosa y no se filtra bien. Solo merece la pena en los
clips que te vayan a costar de reconocer dentro de cuatro meses.

1. Recorre el bin en vista de miniaturas
2. En los cinco o seis clips que no se identifiquen por la miniatura, escribe una frase
   corta en `Description`: `calle mojada de noche, contraluz`
3. Si un clip tiene un problema —audio saturado, foco perdido a mitad—, anótalo en
   `Comments`

**Verifica**: menos de la mitad de los clips tienen `Description`. Si los tienes todos,
has invertido tiempo donde no rendía.

---

## Paso 5: Colores y flags

**Por qué**: es la capa que se lee de un vistazo, sin abrir ningún panel. Y es la que
más se estropea si no se decide primero qué significa cada color.

Escribe el código en el mismo `vocabulario-keywords.md`, debajo de las keywords:

| Color | Significado |
| ----- | ----------- |
| Azul | Material propio |
| Verde | Seleccionado para el montaje |
| Amarillo | Requiere trabajo extra |
| Rojo | Descarte |
| Sin color | Sin revisar |

Ahora aplícalo:

1. Selecciona **todo** `08-Propio` > clic derecho > `Clip Color` > azul
2. Los clips que el pase de diagnóstico de la práctica 02 marcó como raros —otro frame
   rate, otra resolución, codec exótico— en amarillo
3. Lo que no vayas a usar: muévelo a `10-Descartes` **y** ponlo en rojo. Doble red
4. Un flag en los dos o tres clips que tengas pendientes de algo concreto, y anota qué
   en `Comments`

> [!WARNING]
> **Marca la excepción, no la norma.** Si acabas con el 90 % del media pool en verde, el
> verde ha dejado de informar. Una marca vale porque distingue a unos pocos.

**Verifica**: en vista de miniaturas, se ve de un vistazo cuál es tu material y cuál del
pack, sin abrir ningún panel.

---

## Paso 6: El examen de verdad

**Por qué**: comprobar que la metadata sirve, antes de construir smart bins encima en la
práctica 04.

Con el buscador del media pool, y desde el bin `Master` para que alcance todo:

1. Busca `noche`. ¿Aparecen todos los planos de noche, del pack y tuyos?
2. Busca `voz`. ¿Aparece el clip de `02-Entrevista`?
3. Busca una palabra que **no** esté en tu vocabulario. ¿Devuelve cero, como debe?

**Verifica**: las tres búsquedas se comportan como esperas.

> [!IMPORTANT]
> **Borra el texto del buscador al terminar.** Un buscador con texto dentro deja los
> bins medio vacíos y es la causa número uno de "he perdido la mitad de los clips".

Si alguna búsqueda falla, el problema está en la metadata, no en el buscador. Vuelve al
paso 3 y repásalo: es más rápido ahora que en la Semana 12.

---

## Paso 7: Guardar el trabajo

**Por qué**: la metadata que acabas de escribir vive **en el proyecto**, no dentro de
los archivos de vídeo. Si el proyecto se pierde, se pierde con él.

1. `File > Save Project` (`Ctrl+S`), o nada si tienes Live Save activado desde la
   Semana 03
2. `File > Export Project` → `BC-Resolve/04-respaldos/BC-Bootcamp-Resolve-semana04.drp`

**Verifica**: el `.drp` existe y pesa unos pocos megabytes.

---

## ✅ Resultado

- [ ] `vocabulario-keywords.md` existe, con 15 palabras o menos, y con el código de colores
- [ ] Todas las palabras están en minúsculas, sin acentos y en singular
- [ ] Todos los clips de `01-Basicos` y `08-Propio` tienen keywords
- [ ] La mayoría tiene dos o más, no solo la común de la tanda
- [ ] `Description` escrita solo en los clips que la necesitan
- [ ] Código de colores aplicado, marcando excepciones y no la norma
- [ ] Las tres búsquedas del paso 6 devuelven lo esperado
- [ ] Buscador limpio y `.drp` de la semana exportado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Escribo una keyword y solo se aplica a un clip | La selección se perdió al pinchar en el panel | Selecciona en el media pool y escribe sin deseleccionar |
| No veo el campo `Keywords` | El panel está en otro conjunto de campos | Cámbialo en el desplegable superior al de plano y escena |
| Una búsqueda no devuelve todo lo que debería | Variantes de la misma palabra: `noche` y `nocturno` | Unifica según el vocabulario; por eso existe la lista |
| Medio bin ha desaparecido | Queda texto en el buscador | Bórralo |
| El color no se ve en la vista de miniaturas | El clip tiene flag pero no color: son cosas distintas | `Clip Color` tiñe; `Flags` marca |
| He puesto color a todo y ya no distingo nada | La marca dejó de ser excepción | Selecciona todo, quita el color y vuelve a marcar solo lo que destaque |
| La metadata desapareció de unos clips | Se quitaron del media pool y se reimportaron | No vuelve: la metadata vive en el proyecto. Reescríbela |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · La estructura de bins y la primera importación](02-la-estructura-de-bins.md) | **03 · Metadata, keywords y marcas** | [04 · Smart bins y detección de escenas](04-smart-bins-y-deteccion-de-escenas.md) |

← [Volver a la Semana 04](../README.md)
