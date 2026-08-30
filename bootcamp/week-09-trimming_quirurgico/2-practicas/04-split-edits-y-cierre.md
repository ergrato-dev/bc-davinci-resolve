# Práctica 04 — Split edits y cierre

> Al terminar tu pieza tendrá cortes en L y en J donde hacen falta, ni un hueco, los marcadores
> puestos al día y un respaldo. Y sabrás cuántos segundos y cuántos cortes separan `BC-Montaje-v2`
> de `BC-Montaje-v3`.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-slip-slide-y-el-dynamic-trim.md), [Teoría 08](../1-teoria/08-trim-asimetrico-y-split-edits.md)

## Contexto

Los split edits van al final por un motivo: son la única operación de la semana que **desalinea a
propósito** la imagen y el sonido. Hacerlos sobre un montaje que todavía va a cambiar de duración
es rehacerlos.

Tu montaje ya está estable. Ahora se le quita el sonido mecánico.

---

## Paso 1: Elegir dónde van

**Por qué**: un split edit en el sitio equivocado no aporta nada, y en todos los sitios es un tic.

Filtra el `Marker Index` por 🟢 verde: esos son los que apuntaste en la práctica 01. Si tienes
menos de dos, busca ahora en tu pieza los tres sitios donde casi siempre funcionan:

| Sitio | Qué corte | Por qué |
| ----- | --------- | ------- |
| De alguien hablando a un plano de recurso | **En L**: la voz sigue sonando sobre el recurso | El recurso ilustra lo que se dice, no lo interrumpe |
| Cambio de localización | **En J**: el ambiente del sitio nuevo entra antes | El espectador llega antes que la cámara |
| Antes de que alguien empiece a hablar | **En J**: se le oye empezar sobre el plano anterior | Suena a conversación, no a montaje |

Necesitas **dos como mínimo**. Cuatro o cinco es lo razonable en una pieza de cinco minutos.

**Verifica**: tienes al menos dos sitios elegidos y sabes si cada uno es en L o en J.

---

## Paso 2: Apagar el imán

**Por qué**: el imán intentará volver a pegar el borde del audio al del vídeo, que es justo lo que
no quieres mientras los separas.

1. **`N`** para apagarlo

Al terminar la práctica lo vuelves a encender. También se puede pulsar `N` **mientras** arrastras,
para saltárselo solo en ese gesto.

**Verifica**: el botón `Snapping` de la barra de herramientas ya no está resaltado.

---

## Paso 3: El primer split edit, paso a paso

**Por qué**: la mecánica del trim asimétrico tiene un paso —suspender el enlace— que si se salta
no funciona, y es el que más gente falla.

Situación: un corte en J. El sonido del plano B tiene que empezar medio segundo antes que su
imagen.

1. **`T`** — modo trim
2. **Clic sobre el lado entrante del corte de vídeo**, el de la derecha
3. **`Alt`** (Win) / **`Opt`** (Mac) **+ clic** sobre ese mismo lado, para **suspender el enlace**
   de audio y vídeo solo en este gesto
4. **`Ctrl`** (Win) / **`Cmd`** (Mac) **+ clic** sobre el **lado entrante del corte de audio** de
   B, para añadirlo a la selección
5. Arrastra, o usa **`,`** y **`.`**: los dos cortes se mueven en **sentidos contrarios**
6. **`/`** — escucha

Medio segundo son **doce fotogramas a 24 fps**. Menos de seis no se nota; más de un segundo ya no
es un split edit, es un plano de recurso mal colocado.

**Verifica**: en la timeline, el borde del clip de audio y el del clip de vídeo **ya no están
alineados**. Se ve a simple vista.

> [!WARNING]
> **No apagues `Linked Selection` desde la barra de herramientas.** Si lo apagas y se te olvida
> encenderlo, el siguiente clip que muevas se moverá sin su sonido y el desfase no lo vas a ver:
> lo vas a oír tres semanas después. `Alt` / `Opt` + clic es puntual y no deja rastro.

---

## Paso 4: El resto de los split edits

Repite el paso 3 hasta tener **al menos dos** en la pieza. Para el caso más simple —mover solo el
audio de un corte, sin tocar el vídeo— hay una versión de tres teclas:

1. **`T`**
2. **`V`** — selecciona el corte más cercano
3. **`Alt+U`** (Win) / **`Opt+U`** (Mac) hasta que la selección sea **solo audio**
4. **`,`** y **`.`**

No es un trim asimétrico de verdad —solo se mueve un lado— pero resuelve la mayoría de los casos
sin riesgo de desenlazar nada.

**Verifica**:

```bash
python scripts/verificar-semana.py 09 --check montaje-v3-split-edits
```

El check cuenta los clips de la primera pista de audio que **no empiezan en el mismo fotograma**
que ningún clip de la primera pista de vídeo. Pide dos o más.

---

## Paso 5: Volver a encender el imán y comprobar la sincronía

**Por qué**: has estado desenlazando cosas a propósito. Ahora hay que asegurarse de que no
desenlazaste ninguna sin querer.

1. **`N`** — imán otra vez encendido
2. Comprueba que `Linked Selection` sigue **activado** en la barra de herramientas
3. **Reproduce la pieza entera**, con auriculares, prestando atención a **si alguna voz va
   desincronizada con su imagen**

Un desfase de sincronía se oye como una voz que no encaja con los labios, y aparece siempre en un
sitio: donde moviste un clip con el enlace suspendido.

**Verifica**: ninguna voz va desincronizada. Los split edits que hiciste suenan intencionados, no
a error.

---

## Paso 6: La comprobación de huecos, la definitiva

**Por qué**: los trims asimétricos pueden dejar huecos en la pista de vídeo si te pasaste de largo,
y es lo último que se comprueba antes de cerrar.

1. `Detail Zoom` y recorre `Continuidad` de principio a fin
2. Cierra cualquier hueco con `Forward Delete` sobre él, o rippleando su borde en modo trim

**Verifica**:

```bash
python scripts/verificar-semana.py 09 --check montaje-v3-sin-huecos
```

---

## Paso 7: Poner al día los marcadores

**Por qué**: los marcadores son el entregable de la semana que el verificador lee entero, y son la
lista de trabajo de la que arranca la Semana 10.

En el `Marker Index`:

1. Los problemas que has resuelto: **pásalos a azul** o bórralos
2. Los que no has resuelto: **déjalos en su color**, y añade en `Notes` por qué no
3. Añade los nuevos que hayan salido esta semana, en 🔵 azul, con la nota de a qué semana
   pertenecen: *«este plano se ve movido — estabilización, Semana 10»*

Al terminar tienen que quedar **ocho o más**, todos con nombre propio.

**Verifica**:

```bash
python scripts/verificar-semana.py 09 --check marcadores-anotados
```

---

## Paso 8: La comparación con `BC-Montaje-v2`

**Por qué**: es la parte del entregable que solo se puede escribir hoy, con las dos versiones
delante, y la que mide de verdad lo que ha dado la semana.

1. Abre `BC-Montaje-v2` y anota su duración total
2. Vuelve a `BC-Montaje-v3` y anota la suya
3. Contesta por escrito en `notas-de-montaje.md`:

> **¿Cuánto ha bajado la duración, en segundos y en porcentaje?**
>
> **¿Cuántos planos borré enteros?**
>
> **¿Qué corte concreto es el que más ha mejorado, y con qué operación?**
>
> **¿Qué operación de las cinco me ha resultado más útil en mi pieza, y por qué?**
>
> **¿Qué queda sin afinar y por qué lo dejé?**

> [!IMPORTANT]
> Después de comparar, **vuelve a abrir `BC-Montaje-v3` con doble clic**. Cinco de los diez checks
> leen la timeline activa: si te quedas en `BC-Montaje-v2`, fallan los cinco de golpe aunque el
> trabajo esté perfecto.

**Verifica**: las cinco preguntas contestadas con cifras y cortes concretos.

---

## Paso 9: Cerrar la semana

1. **`A`** — vuelve al modo seguro
2. Comprueba que **no estás en `Dynamic Trim Mode`**: el cabezal no está amarillo
3. Comprueba que **`Linked Selection` y `Snapping` están activados**
4. `Ctrl+S` (Win) / `Cmd+S` (Mac)
5. **`File > Export Project`** → `04-respaldos/BC-Bootcamp-Resolve-semana09.drp`

**Verifica**:

```bash
python scripts/verificar-semana.py 09
```

Diez de diez, con `BC-Montaje-v3` como timeline abierta.

---

## ✅ Resultado

- [ ] Dos split edits o más, hechos con trim asimétrico
- [ ] Ninguna voz desincronizada con su imagen
- [ ] `Linked Selection` y `Snapping` activados al cerrar
- [ ] Ni un hueco en `Continuidad`
- [ ] Ocho marcadores o más, al día, todos con nombre propio
- [ ] Las cinco preguntas de la comparación contestadas con cifras
- [ ] No estoy en `Dynamic Trim Mode`
- [ ] `BC-Bootcamp-Resolve-semana09.drp` exportado
- [ ] Los diez checks en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Al arrastrar se mueven los dos cortes juntos | No suspendiste el enlace | `Alt` / `Opt` + clic antes |
| Se mueven en el mismo sentido, no en contrario | Seleccionaste dos lados iguales | Uno saliente y otro entrante |
| El borde vuelve a pegarse solo | El imán sigue encendido | `N` |
| `montaje-v3-split-edits` falla con split edits hechos | Los hiciste en otra pista de audio | El check mira la **primera** pista de audio |
| Una voz va desincronizada | Moviste un clip con el enlace suspendido | Busca el sitio, `Ctrl+Z` si es reciente, o recolócalo a mano |
| Se me olvidó volver a encender `Linked Selection` | Lo apagaste desde la barra | Enciéndelo y revisa la pieza entera |
| Fallan cinco checks de golpe | Tienes abierta `BC-Montaje-v2` | Doble clic en `BC-Montaje-v3` |
| `marcadores-anotados` falla | Alguno conserva su `Marker N` de fábrica | Ordena el `Marker Index` por `Name` y los ves juntos |
| Fallan **todos** los checks | El puente no está lanzado | `Workspace > Scripts > Utility` |
| No sé qué contestar en la comparación | No anotaste las cifras al empezar | La duración de `BC-Montaje-v2` sigue ahí: ábrela y mírala |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Slip, slide y el dynamic trim](03-slip-slide-y-el-dynamic-trim.md) | **04 · Split edits y cierre** | — |

← [Volver a la Semana 09](../README.md)
