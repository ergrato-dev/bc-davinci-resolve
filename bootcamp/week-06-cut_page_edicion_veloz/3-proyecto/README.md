# Proyecto — Semana 06: la pieza existe entera

> Hasta ahora tu proyecto tenía identidad técnica y material preparado. Esta semana pasa
> algo distinto en clase: **la pieza empieza a existir**. Fea, larga y con planos que vas a
> cambiar, pero de principio a fin. Es la primera semana en la que se puede reproducir tu
> trabajo y entender de qué va.

## 📦 Qué añade esta semana

La sexta capa: **el montaje bruto**.

Es la capa que sostiene las once semanas siguientes. Nada de lo que viene —trimming,
títulos, mezcla, color, composición, entrega— se puede hacer sobre una pieza que no está
montada de principio a fin. Por eso la Fase 2 tiene un requisito duro que no tienen las
otras:

> [!IMPORTANT]
> **El montaje bruto tiene que llegar al final.** No "los tres primeros minutos bien". Un
> montaje incompleto arrastra el problema a las ocho fases siguientes: no se puede mezclar
> lo que no está montado, ni etalonar lo que no está mezclado. Si tienes que elegir entre
> un montaje entero regular y medio montaje bueno, elige el entero. Siempre.

Y una segunda capa, más pequeña pero con futuro: la escena multicámara montada aparte, en
`BC-Sync-Cut-v1`, lista para incorporarse en la Semana 07.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca
carácter a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` del proyecto sigue siendo **24**
3. Existe la timeline **`BC-Montaje-v1`**
4. Existe la timeline **`BC-Sync-Cut-v1`**
5. **`BC-Montaje-v1`** es la timeline abierta
6. Su pista de vídeo principal tiene **quince clips o más**
7. Dura **120 segundos o más**
8. Tiene **dos pistas de vídeo o más**

```bash
python scripts/verificar-semana.py 06
```

Con el proyecto abierto, **`BC-Montaje-v1` como timeline activa** y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!NOTE]
> Los checks 5 a 8 usan `timeline_probe`, que lee **la timeline activa**. Si terminaste la
> práctica 04 y te quedaste en `BC-Sync-Cut-v1`, fallan los cuatro de golpe aunque el
> trabajo esté perfecto. Doble clic en `BC-Montaje-v1` y repite. *Comportamiento verificado
> por la API de scripting en 21.0.4.5, agosto de 2026.*

Los mínimos de los checks 6 y 7 —quince clips, dos minutos— son el suelo de una primera
pasada, no el objetivo. Una pieza de las cinco del bootcamp pide entre tres y doce minutos:
si tu montaje se queda en 120 segundos, la pasada no está completa aunque el check pase.

---

## 📝 El entregable escrito

### `notas-de-montaje.md` (práctica 02, paso 8; práctica 03, paso 10; práctica 04, paso 9)

En `BC-Resolve/04-respaldos/`, junto a `vocabulario-keywords.md`, `notas-de-ingesta.md` y
`rendimiento.md`.

Seis apartados, todos con contenido concreto:

> **Estructura**: apertura, desarrollo y cierre, en tres líneas.
>
> **Duración y número de clips**: las cifras reales de tu timeline, antes y después de la
> práctica 03.
>
> **Lo que hay que arreglar**: la lista de la revisión, con la semana en la que toca.
>
> **Lo que falta grabar**: si algo no lo tienes y todavía puedes conseguirlo.
>
> **Material multicámara**: si la hora de grabación era fiable, qué cámara lleva el mejor
> sonido y cuántos cambios de ángulo montaste.
>
> **Decisiones que dudas**: los dos o tres sitios donde no sabes si acertaste.

El apartado de "lo que falta grabar" es el que más vale de los seis. Descubrir en la Semana
06 que falta un plano de recurso te deja veintinueve semanas para grabarlo; descubrirlo en
la 22 significa montar con lo que hay.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver, y que es la mitad del valor de la semana:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| La pieza llega al final | Se reproduce entera y termina donde tenía que terminar |
| Tiene apertura, desarrollo y cierre reconocibles | Se pregunta: ¿dónde acaba la apertura? Hay una respuesta |
| El orden es una decisión, no el orden de grabación | Se compara con la hora de grabación de los clips |
| No hay huecos entre clips | Se reproduce completa: ningún parpadeo a negro |
| Los planos tienen margen para ajustar después | Se extiende un corte cualquiera: hay material a los lados |
| La continuidad vive en `Video 1` | Desactivar `Video 2` deja una pieza que sigue funcionando |
| Los recursos tapan de verdad | Empiezan antes del salto y acaban después |
| No hay recursos de más | Se ve a quien habla la mayor parte del tiempo |
| El Close Up se usó con criterio | Dos o tres como mucho, y no se ven blandos |
| El multicámara suena a una sola fuente | Se reproduce un cambio de ángulo: la voz no cambia de sala |
| No hay nada que no toque todavía | Ni títulos, ni transiciones, ni música, ni color |

Ese último criterio es el que más gente incumple, y no por descuido: por entusiasmo.
Poner un rótulo hoy significa rehacerlo en cuanto muevas un corte en la Semana 09.

---

## 💡 Adaptación a tu pieza

**Documental corto** · Tu montaje bruto sale de la entrevista: los subclips de la Semana 05
puestos en orden **temático**, no cronológico. Monta primero solo la voz, de principio a
fin, y deja los recursos para la práctica 03. Es el flujo profesional del formato y es
exactamente lo que hacen las prácticas 02 y 03 en ese orden.

**Videoclip** · Tu columna vertebral es la música, y la música todavía no toca. Monta la
imagen con la estructura de la canción en la cabeza —estrofa, estribillo, estrofa— y con
los planos que correspondan a cada parte. En la Fase 4 se sincroniza. Si metes el tema
ahora, el montaje se pega a él y ya no lo podrás mover.

**Cortometraje de ficción** · Monta por escenas, en el orden del guion, y usa la mejor toma
de cada plano sin comparar demasiado: comparar tomas es trabajo de la Semana 09. Si rodaste
con varias cámaras, la práctica 04 es tu semana entera.

**Tutorial o vídeo formativo** · La pantalla y la cámara son dos ángulos del mismo momento:
la base va con el mejor sonido, casi siempre la cámara, y la pantalla encima con Place on
Top. Estructura clara: qué vamos a hacer, lo hacemos, qué hemos hecho.

**Pieza de viaje** · El riesgo es el desfile de planos bonitos sin orden. Decide primero el
cierre —el plano con el que se acaba— y monta hacia él. Y vigila la duración: en bruto,
esta pieza se va sola a los diez minutos y tiene que quedarse en cuatro o seis.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 06` en verde, ocho de ocho
2. `BC-Montaje-v1` va de principio a fin, con dos pistas de vídeo
3. `BC-Sync-Cut-v1` con la escena multicámara montada
4. `notas-de-montaje.md` en `04-respaldos/`, con sus seis apartados
5. Respaldo de la semana: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana06.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza la práctica 02. Es la única de las cuatro cuyo resultado
> **no se puede recuperar más tarde sin rehacer trabajo**: las correcciones de la 03 se
> hacen cualquier lunes, y el sync bin de la 04 vuelve en la Semana 12. Un montaje que no
> llega al final bloquea la Fase 3 entera.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Afinar cortes en la primera pasada | Es lo que uno cree que es montar | Marca de sobra y sigue. El ajuste fino es la Semana 09 |
| Parar a arreglar durante la revisión | Ves un fallo y quieres arreglarlo ya | Apunta y sigue: la lista es el guion de la práctica 03 |
| Meter música, títulos o transiciones | Entusiasmo | Se rehace todo en cuanto muevas un corte |
| Añadir antes de quitar | Añadir es más divertido | Quitar, sustituir, añadir. En ese orden |
| Poner recursos antes de cerrar `Video 1` | No se ve el problema hasta que ocurre | Un ripple posterior los descoloca todos |
| Tapar un salto con Ripple Overwrite | Suena parecido a "poner algo encima" | Place on Top: el audio de debajo sigue |
| Montar por orden de grabación | Es el orden en que está el material | Apertura, desarrollo, cierre |
| Dejar la pieza a medias | Se acabó el tiempo en los primeros minutos | Un montaje entero regular vale más que medio bueno |
| Dos pistas de audio sonando en el multicámara | Los ángulos entran con su sonido | Silencia el audio de los ángulos de encima |
| Verificar con `BC-Sync-Cut-v1` abierta | Es la última que tocaste | Abre `BC-Montaje-v1` antes de verificar |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 05](../../week-05-proxies_cache_y_sincronizacion/3-proyecto/README.md) | **Proyecto Semana 06** | [Semana 07](../../week-07-cut_page_acabado_y_quick_export/README.md) |

← [Volver a la Semana 06](../README.md)
