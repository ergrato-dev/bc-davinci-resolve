# Práctica 03 — Sincronizar y preparar multicámara

> Al terminar tendrás el bin `03-Multicamara` lleno, una timeline con imagen y sonido de
> dos aparatos distintos pegados al fotograma, y un clip multicámara listo para la Semana
> 12. Es la práctica que más depende del material, así que empieza leyendo el paso 0.

**Duración estimada**: 55 min
**Prerrequisitos**: [Teoría 06](../1-teoria/06-sincronizar-audio-y-video.md), [Teoría 07](../1-teoria/07-preparar-el-material-multicamara.md), Semana 04 cerrada

## Contexto

Dos aparatos, un momento. Es la situación de cualquier entrevista con micrófono de solapa
y de cualquier escena rodada con dos cámaras, y es la base de la Semana 12 y de media
Fase 4.

Si el pack de medios no te llenó `03-multicamara/`, el paso 0 te dice cómo grabarlo en
quince minutos con lo que tienes en casa.

---

## Paso 0: Conseguir material que sirva

**Por qué**: sin dos grabaciones del mismo momento no hay nada que sincronizar, y el
material de banco de vídeo casi nunca viene en pares.

Necesitas dos cosas:

| Qué | Para qué | Mínimo |
| --- | -------- | ------ |
| **Un par doble sistema**: un clip de vídeo con audio de cámara, y una grabación de audio del mismo momento hecha aparte | Pasos 1 a 4 | 60 s |
| **Tres ángulos** de la misma escena, todos con audio | Pasos 5 a 7 | 60 s |

Si no lo tienes, grábalo. Con un móvil y cualquier otro aparato que grabe sonido:

1. Pon el móvil en un sitio fijo, grabando a alguien hablando durante un minuto
2. Grábale el sonido a la vez con otro aparato, cerca de la persona
3. **Da una palmada al empezar**, delante de los dos. Es tu claqueta
4. Para los tres ángulos: repite con tres aparatos que graben a la vez, o graba tres veces
   la misma escena si no tienes tres cámaras —para practicar el flujo sirve, aunque los
   ángulos no cuadren de verdad

**Verifica**: en `<ruta-a-medios>/03-multicamara/` hay al menos tres archivos de vídeo, y
tienes localizado el par de doble sistema.

---

## Paso 1: Importar al bin correcto

**Por qué**: el bin activo decide dónde cae todo, y esto es la Semana 04 otra vez.

1. Página **Media**, y selecciona el bin **`03-Multicamara`**
2. Desde el panel `Media Storage`, arrastra los archivos de `03-multicamara/` al media
   pool
3. Arrastra también el par de doble sistema

**Verifica**:

```bash
python scripts/verificar-semana.py 05 --check bin-multicamara
```

El check pide **tres clips o más** en `03-Multicamara`.

---

## Paso 2: Sincronizar el par de doble sistema

**Por qué**: es el caso más común de todos y el que vas a repetir en cada entrevista del
resto del bootcamp.

1. En el media pool, selecciona **a la vez** el clip de vídeo y el de audio
2. Menú contextual > `Auto Sync Audio`
3. Elige el método por **forma de onda**
4. Elige la opción que **añade** el audio como pista extra, en lugar de sustituir el de
   cámara

**Verifica**: el clip resultante tiene dos pistas de audio. Se ve al abrirlo en el visor
de origen, y se verá con claridad en el paso 4.

> [!TIP]
> Si el método por forma de onda falla, la causa casi siempre es que el audio de la cámara
> es demasiado distinto del bueno: mucho ruido, mucha distancia o viento. Vuelve a grabar
> el par con la palmada del paso 0, que da a los dos archivos un pico idéntico e
> inconfundible.

---

## Paso 3: Comprobar la sincronía como se hace de verdad

**Por qué**: un fotograma de desfase no se ve en una escucha rápida y sí se nota en la
mezcla de la Semana 14. Comprobar cuesta un minuto.

1. Abre el clip sincronizado y busca una **consonante explosiva**: una "p" o una "t"
2. Colócate ahí y avanza **fotograma a fotograma** con las flechas
3. Comprueba que el pico de la onda y el cierre de labios caen en el mismo fotograma
4. Vete al **final** del clip y repite la comprobación

**Verifica**: cuadra al principio **y** al final. Si cuadra al principio y no al final,
es **deriva**: apunta el clip y sigue —la práctica 04 te dará la herramienta para
salvarlo, que es partirlo en subclips.

---

## Paso 4: La timeline `BC-Sync-v1`

**Por qué**: es el entregable verificable de esta práctica, y la prueba de que el clip
lleva las dos pistas de audio.

1. Con el clip sincronizado seleccionado en el media pool, crea una timeline nueva a
   partir de él: `File > New Timeline`, o el menú contextual del media pool
2. Nómbrala exactamente **`BC-Sync-v1`**
3. Asegúrate de que el clip sincronizado está dentro y de que se ven **dos pistas de
   audio**: la buena y la de referencia de cámara
4. Silencia la pista de referencia con su botón `M` en la cabecera de la pista
5. Deja `BC-Sync-v1` como la timeline **abierta**

**Verifica**:

```bash
python scripts/verificar-semana.py 05 --check timeline-sync-existe
python scripts/verificar-semana.py 05 --check timeline-sync-audio
```

> [!IMPORTANT]
> El segundo check lee **la timeline activa**. Si tienes abierta `BC-Montaje-v1`, va a
> fallar aunque `BC-Sync-v1` esté perfecta. Ábrela con doble clic en el media pool antes
> de verificar.

---

## Paso 5: Construir el clip multicámara

**Por qué**: es la preparación de la Semana 12, y se hace ahora porque ahora es cuando
tienes todo el material de la escena ingestado.

1. En `03-Multicamara`, selecciona los **tres ángulos**
2. Menú contextual > la opción de crear un clip multicámara con la selección
3. En el diálogo:
   - **Método de sincronización**: por **sonido**
   - **Orden de los ángulos**: el plano más abierto primero
   - **Fuente de audio**: fíjala en el ángulo con el mejor sonido, **no** que siga al
     ángulo activo
4. Acepta

**Verifica**: en `03-Multicamara` aparece un elemento nuevo, el clip multicámara. Los tres
ángulos originales siguen ahí: no se han movido ni se han consumido.

> [!NOTE]
> Los rótulos exactos del diálogo **no se pueden comprobar por la API de scripting**. El
> capítulo *Multicam Editing* del
> [manual oficial](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion)
> los recoge con las capturas de tu versión.

---

## Paso 6: Comprobar los ángulos

**Por qué**: un multicámara mal sincronizado no avisa. Se descubre montando, en la Semana
12, con el montaje ya hecho.

1. Abre el clip multicámara
2. Ve a un punto con habla y **cambia de ángulo** mientras reproduces: la voz no debe
   saltar ni repetir sílabas
3. Busca un **gesto brusco** —una palmada, una puerta— y compruébalo en los tres ángulos,
   fotograma a fotograma

**Verifica**: los tres ángulos coinciden. Si uno se desvía, casi seguro grabó a otro
frame rate: anótalo en `notas-de-ingesta.md`.

---

## Paso 7: Describir lo nuevo

**Por qué**: todo lo que has creado hoy son clips del media pool como cualquier otro, y la
Semana 04 dejó dicho que un clip sin keywords no aparece en ningún smart bin.

1. Selecciona el clip sincronizado y el multicámara
2. Panel `Metadata`, y escribe las keywords que toquen de tu vocabulario —`entrevista`,
   `multicamara`, el lugar—
3. Ponles el clip color que tu código asigne al material propio

**Verifica**: abre `SB-Sin-describir` de la Semana 04. Los elementos nuevos no están
dentro.

---

## ✅ Resultado

- [ ] `03-Multicamara` tiene tres clips o más
- [ ] El par de doble sistema está sincronizado por forma de onda
- [ ] El audio de cámara se conservó como pista de referencia
- [ ] He comprobado la sincronía en una explosiva, al principio y al final
- [ ] `BC-Sync-v1` existe, tiene dos pistas de audio y es la timeline abierta
- [ ] El clip multicámara existe, con la fuente de audio fija
- [ ] He comprobado los tres ángulos con un punto de habla y un gesto brusco
- [ ] Lo nuevo tiene keywords y color

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `Auto Sync Audio` no encuentra la sincronía | La cámara no grabó audio, o es demasiado distinto | Regraba con la palmada, o sincroniza por puntos de entrada |
| El audio va un poco adelantado | Un fotograma de desfase | Ajústalo a mano: prefiere dejarlo atrasado antes que adelantado |
| Cuadra al principio y no al final | Deriva por frecuencias o frame rates distintos | Práctica 04: pártelo en subclips y sincroniza por trozos |
| `timeline-sync-audio` falla con dos pistas visibles | La timeline activa es otra | Abre `BC-Sync-v1` con doble clic y repite |
| `timeline-sync-existe` falla | El nombre no es exacto | `BC-Sync-v1`, con el guion y la uve minúscula |
| El multicámara sale con los ángulos desplazados | El método de sincronización no era el bueno para ese material | Bórralo y rehazlo por puntos de entrada |
| El sonido cambia de sala al cambiar de ángulo | La fuente de audio sigue al ángulo activo | Rehaz el clip fijando la fuente en un ángulo |
| No encuentro la opción de crear multicámara | La selección tiene un solo clip | Selecciona los tres ángulos a la vez |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [02 · La caché de render y el disco](02-la-cache-de-render-y-el-disco.md) | **03 · Sincronizar y preparar multicámara** | [04 · Subclips y relink](04-subclips-y-relink.md) |

← [Volver a la Semana 05](../README.md)
