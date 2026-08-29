# Proyecto — Semana 07: la pieza sale del programa

> Hasta ahora tu pieza existía dentro de Resolve. Esta semana se acaba en lo grueso y sale
> convertida en un archivo que se puede ver en un móvil, mandar por un enlace o enseñar a
> alguien que no sabe qué es DaVinci Resolve. Es la primera vez que tu trabajo existe fuera
> de tu ordenador.

## 📦 Qué añade esta semana

La séptima capa: **el acabado grueso y la primera entrega**.

Son dos cosas distintas y las dos cierran la Fase 2:

1. **`BC-Montaje-v2`**, el montaje bruto con lo que la Cut page acaba bien: transiciones con
   motivo, saltos reparados, duraciones ajustadas, sonido audible y rótulos en su pista.
2. **Un archivo de vídeo**, exportado, visto entero fuera de Resolve y reimportado al
   proyecto como evidencia de la fase.

> [!IMPORTANT]
> `BC-Montaje-v1` **no se toca**. El acabado va sobre una copia, y las dos versiones se
> quedan en el proyecto. Es la convención de versionado de
> [`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md), y a partir de
> aquí se repite en cada fase: `BC-Montaje-v3` en la Semana 09, `BC-Color-v1` en la 17,
> `BC-Master` en la 28.

Y una tercera cosa que no ocupa espacio en disco pero vale más que las otras dos: **el dato
de cuánta cola tiene tu material**. Es el número que decide si la Semana 09 va a ser cómoda o
imposible, y sale del paso 1 de la práctica 02.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca
carácter a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` del proyecto sigue siendo **24**
3. **`BC-Montaje-v1`** sigue existiendo
4. Existe la timeline **`BC-Montaje-v2`**
5. **`BC-Montaje-v2`** es la timeline abierta
6. Su pista de vídeo principal tiene **dieciocho clips o más**
7. `Video 1` **no tiene huecos ni solapes**
8. Tiene **tres pistas de vídeo o más**
9. El bin **`12-Entregas`** tiene al menos un archivo

```bash
python scripts/verificar-semana.py 07
```

Con el proyecto abierto, **`BC-Montaje-v2` como timeline activa** y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!NOTE]
> Los checks 5 a 8 usan `timeline_probe` y `timeline_detect_gaps`, que leen **la timeline
> activa**. Si te quedaste comparando en `BC-Montaje-v1` o mirando `BC-Sync-Cut-v1`, fallan
> los cuatro de golpe aunque el trabajo esté perfecto. Doble clic en `BC-Montaje-v2` y repite.
> *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de 2026.*

El mínimo del check 6 —dieciocho clips— es el suelo: son los quince de la Semana 06 más los
planos de la escena multicámara. Si tu pieza tenía veinticinco, ahora tiene veintiocho o más.

---

## 📝 El entregable escrito

### `notas-de-montaje.md`, apartado `## Acabado — Semana 07`

En `BC-Resolve/04-respaldos/`, en el mismo archivo que abriste en la Semana 06.

Se abre en la práctica 01 con cuatro listas de trabajo y se cierra en la práctica 04 con seis
puntos:

> **Cifras finales**: duración, número de clips en `Video 1`, número de pistas.
>
> **Qué se acabó**: cuántas disolvencias, cuántos `Smooth Cut`, cuántos cambios de velocidad,
> cuántos rótulos.
>
> **Cuánta cola tiene mi material**: el número del paso 1 de la práctica 02, en fotogramas.
>
> **Qué vi al mirar el archivo**: la lista del visionado fuera de Resolve, sin suavizar.
>
> **Qué falta grabar**: material recortado, planos repetidos por falta de material, huecos que
> taparías si tuvieras un plano más.
>
> **Qué pasa a la Fase 3**: lo que has visto y no toca todavía, con la semana al lado.

Los dos que más valen son el tercero y el cuarto. El de las colas porque condiciona la Semana
09 entera; el del visionado porque es la única vez en toda la fase en la que ves tu pieza como
la ve otra persona, y esa lista no se puede reconstruir después.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver, y que es la mitad del valor de la semana:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| Cada transición tiene un motivo | Se pregunta por una: hay una respuesta de las tres |
| Las transiciones no se acumulan | Entre dos y cinco en una pieza de cinco minutos |
| Ningún `Smooth Cut` se nota | Se reproduce a velocidad normal: no hay deformación |
| Los saltos están todos decididos | Reparados, tapados, o dejados a propósito |
| Los cambios de velocidad se justifican | Duración, legibilidad o compresión de un proceso |
| La cámara lenta no va a tirones | Se reproduce el plano: el movimiento es continuo |
| La pieza se escucha entera sin tocar el volumen | Se reproduce con auriculares, de principio a fin |
| Los recursos no ensucian la voz | Se entiende cada palabra sin esfuerzo |
| Los rótulos se leen | También en una pantalla pequeña |
| Los rótulos no tapan caras | Se reproduce cada uno |
| `Video 3` contiene solo títulos | Se desactiva: solo desaparecen rótulos |
| La atribución del material está puesta | Rótulo de cierre con las licencias del pack |
| El archivo exportado se ha visto entero | Hay una lista escrita de lo que se vio |
| No hay nada que todavía no toque | Ni música, ni subtítulos, ni color, ni animación |

El último sigue siendo el que más gente incumple, y esta semana con una tentación nueva:
poner música porque «ya se ve la pieza». La mezcla es la Fase 4 y se rehace entera.

---

## 💡 Adaptación a tu pieza

**Documental corto** · Tus transiciones son casi todas de cambio de tema, entre bloques de la
entrevista. Los saltos son tu trabajo principal: alterna `Smooth Cut` y recurso para que se
vea a quien habla al menos la mitad del tiempo. El rótulo de nombre es obligatorio, y va con
la calidad en la que habla la persona, no solo con su nombre.

**Videoclip** · Casi ningún corte pide transición: el ritmo es la música, y la música todavía
no está. Lo tuyo esta semana son los cambios de velocidad, que son la herramienta expresiva
del formato. Anota a qué porcentaje se te rompe el material: en la Fase 4, cuando sincronices,
vas a necesitar ese margen.

**Cortometraje de ficción** · Las disolvencias, solo entre escenas y solo para marcar el paso
del tiempo. Nada dentro de una escena. Los rótulos, mínimos: título al principio y créditos al
final. Y una advertencia: si estás pensando en «arreglar» una toma acelerándola ligeramente,
eso es trimming y es la Semana 09.

**Tutorial o vídeo formativo** · Es el formato que más rótulos pide y donde más se nota que
estén bien: el nombre de cada paso, la tecla que se pulsa, el resultado que hay que ver. Los
cambios de velocidad te sirven para comprimir esperas —una instalación, un render— y ahí un
400 % está justificado. Los `Smooth Cut`, para los cortes de la cámara frontal.

**Pieza de viaje** · El riesgo es la disolvencia decorativa entre planos bonitos: si pones una
en cada corte, la pieza se vuelve blanda. Úsalas solo entre localizaciones. Los rótulos de
sitio son los que hacen que se entienda dónde estás, y son casi todo el valor añadido de la
semana en este formato.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 07` en verde, nueve de nueve
2. `BC-Montaje-v1` intacta y `BC-Montaje-v2` acabada, con tres pistas
3. `BC-Montaje-v2-semana07.mp4` en `03-entregas/`, visto entero fuera de Resolve
4. El mismo archivo dentro del bin `12-Entregas`
5. `notas-de-montaje.md` con el apartado `## Acabado — Semana 07` cerrado, con sus seis puntos
6. Respaldo de la fase: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana07.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza la práctica 04. Exportar y **ver** la pieza fuera de
> Resolve es lo único de esta semana que no se puede recuperar más tarde: las transiciones se
> ponen cualquier lunes y los rótulos se rehacen en la Semana 11, pero la lista de lo que ves
> la primera vez que miras tu pieza con ojos de espectador solo se escribe una vez.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Renombrar `v1` en vez de duplicarla | Parece lo mismo y es más rápido | Recupérala del `.drp` de la Semana 06 |
| Poner una disolvencia en cada corte | Está a un botón y parece que mejora | Dos a cinco, con motivo escrito |
| Dejar el `Smooth Cut` en un segundo | Es el valor por defecto | 2-6 fotogramas, siempre |
| Cambiar duraciones después de poner rótulos | El orden parecía indiferente | Velocidad primero, títulos al final |
| Mezclar rótulos y recursos en `Video 2` | Ahorra crear una pista | `Video 3`, y se apagan todos de un clic |
| Meter música | La pieza ya se parece a algo | Se rehace entera en la Semana 15 |
| Exportar y no mirar el archivo | Se da por hecho que está bien | Es la mitad del ejercicio |
| Exportar con marcas `I` / `O` puestas | Quedaron de otra operación | Quítalas y reexporta |
| Tratar el `.mp4` como el master | Es el primer archivo que sale del programa | El master es la Semana 28 |
| Verificar con otra timeline abierta | Es la última que tocaste | Doble clic en `BC-Montaje-v2` |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 06](../../week-06-cut_page_edicion_veloz/3-proyecto/README.md) | **Proyecto Semana 07** | [Semana 08](../../week-08-edit_page_anatomia_y_edicion_basica/README.md) |

← [Volver a la Semana 07](../README.md)
