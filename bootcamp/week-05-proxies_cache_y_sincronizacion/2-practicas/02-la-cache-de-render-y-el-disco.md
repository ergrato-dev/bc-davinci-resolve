# Práctica 02 — La caché de render y el disco

> Al terminar habrás visto la caché trabajar, habrás cacheado a mano un tramo concreto,
> habrás borrado caché sin perder nada y sabrás exactamente dónde vive todo lo que Resolve
> genera en tu disco. Es la práctica menos vistosa de la semana y la que evita el problema
> más frecuente del mes cuatro.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 01](01-diagnostico-optimizados-y-proxies.md), [Teoría 04](../1-teoria/04-la-cache-de-render.md), [Teoría 05](../1-teoria/05-donde-vive-la-cache.md)

## Contexto

La práctica anterior atacó el cuello de la descompresión. Esta ataca el de los efectos,
que es distinto y se arregla con otra herramienta. Vas a provocar el problema a propósito
—porque en la Semana 05 aún no tienes un montaje con efectos— y a resolverlo.

---

## Paso 1: Localizar la carpeta de trabajo

**Por qué**: vas a generar archivos durante toda la práctica. Saber dónde caen es la mitad
del aprendizaje de hoy.

1. `File > Project Settings > Master Settings`, sección
   `Optimized Media and Render Cache`
2. Localiza la ruta de la carpeta de trabajo, la que configuraste en la Semana 03
3. Ábrela en el explorador de archivos y **deja la ventana abierta a un lado**
4. Anota su tamaño actual

**Verifica**: la ruta que ves en Resolve y la carpeta que tienes abierta son la misma, y
dentro hay ya contenido de la práctica 01.

> [!WARNING]
> Comprueba que esa ruta **no** es `BC-Resolve/01-material/` ni la carpeta de tu
> biblioteca de proyectos. Durante esta práctica vas a borrar cosas de esta carpeta, y
> equivocarse de carpeta aquí sí destruye trabajo.

---

## Paso 2: Elegir el formato de la caché

**Por qué**: la caché escribe vídeo, y el formato decide cuánto ocupa cada minuto
cacheado.

1. En la misma sección de ajustes, localiza el ajuste de **formato de la caché de render**
2. Elige un codec intra-frame de calidad media

**Verifica**: el desplegable muestra tu elección al reabrir la ventana.

---

## Paso 3: Provocar el problema

**Por qué**: la caché arregla el coste de calcular efectos. Sin nada que calcular no hay
nada que ver.

1. Página **Edit**, timeline `BC-Montaje-v1`
2. Selecciona un clip de la timeline y abre el `Inspector`
3. En la pestaña `Transform`, sube el valor de `Zoom` a **2,0** aproximadamente
4. Reproduce ese tramo y mira el contador de fps

**Verifica**: la imagen está ampliada y el contador de fps ha bajado respecto a antes del
cambio. Si tu equipo aguanta esto sin inmutarse, añade el mismo cambio a tres o cuatro
clips seguidos.

---

## Paso 4: Modo Smart y la barra de la caché

**Por qué**: es el modo de trabajo normal, y verlo actuar es lo que te permitirá
reconocer después si está funcionando.

1. `Playback > Render Cache > Smart`
2. Deja el cursor de reproducción quieto unos segundos sobre el tramo modificado
3. Mira la **franja fina que hay bajo la regla de tiempo** de la timeline

**Verifica**: la franja cambia de estado sobre ese tramo mientras Resolve genera, y vuelve
a cambiar al terminar. En la carpeta que dejaste abierta han aparecido archivos nuevos.

4. Reproduce otra vez el tramo cacheado y mira el contador de fps

**Verifica**: los fps han subido respecto al paso 3. Eso es la caché haciendo su trabajo.

> [!NOTE]
> Los colores exactos de esa franja **no se pueden comprobar por la API de scripting**. El
> capítulo *Improving Performance* del
> [manual oficial](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion)
> los documenta con las capturas de tu versión. Lo que se ve sin manual es el cambio de
> estado, y con eso basta.

---

## Paso 5: Comprobar que la caché se invalida sola

**Por qué**: es la propiedad que hace que la caché sea fiable, y la razón de no cachear
nada que aún estés decidiendo.

1. Con el tramo ya cacheado, vuelve al `Inspector` y cambia el `Zoom` a **1,5**
2. Mira la franja de la caché sobre ese tramo

**Verifica**: el tramo ha dejado de estar cacheado. Nadie ha tenido que avisar a nadie:
cambiaste un eslabón de la cadena y lo cacheado dejó de valer.

---

## Paso 6: Modo User, para cachear solo lo que tú decidas

**Por qué**: es el modo del disco justo y del control fino, y el que vas a querer en las
semanas de color y de Fusion.

1. `Playback > Render Cache > User`
2. Comprueba que Resolve deja de cachear por su cuenta
3. Selecciona en la timeline el clip modificado y marca su caché desde el menú contextual
4. Espera a que la franja cambie de estado

**Verifica**: **solo** ese clip está cacheado, y el resto de la timeline no.

> [!NOTE]
> Los rótulos de las opciones de caché del menú contextual de la timeline **no se pueden
> comprobar por la API de scripting**. El manual oficial los recoge en el mismo capítulo.
> La comprobación que sí puedes hacer es la de la franja: cambia de estado sobre el clip
> que marcaste y sobre ningún otro.

---

## Paso 7: Borrar caché sin perder nada

**Por qué**: es mantenimiento normal y hay que hacerlo sin miedo, sabiendo exactamente qué
se va.

> [!WARNING]
> **Borrar la caché no se puede deshacer.** Lo que se pierde es tiempo de generación, no
> trabajo: los cortes, el `Zoom` que acabas de poner y toda tu metadata siguen intactos.
> Aun así, en un proyecto avanzado borrarlo todo puede costar media hora de regeneración.
> Por eso vas a usar primero la opción que borra solo lo que ya no se usa.

1. `Playback > Delete Render Cache`, y elige la opción que borra **lo no usado**
2. Mira el tamaño de la carpeta de trabajo
3. Comprueba que tu timeline sigue exactamente igual: los cortes, el `Zoom`, todo

**Verifica**: la carpeta ha adelgazado y no has perdido nada del proyecto.

---

## Paso 8: Dejar el proyecto en un estado razonable

**Por qué**: el `Zoom` del paso 3 era para provocar el problema, no para quedárselo.

1. Devuelve el `Zoom` a **1,0** en los clips que tocaste
2. Deja `Playback > Render Cache` en **`Smart`**, que es el punto de partida sensato
3. Anota en `rendimiento.md` el tamaño final de la carpeta de trabajo y la fecha

**Verifica**: la timeline está como estaba, el modo de caché es `Smart` y tu archivo de
notas tiene una línea más.

---

## ✅ Resultado

- [ ] Sé dónde está mi carpeta de trabajo y la distingo de la del material
- [ ] He elegido el formato de la caché de render
- [ ] He visto la franja de la caché cambiar de estado
- [ ] He medido la ganancia de fps con un tramo cacheado
- [ ] He comprobado que la caché se invalida sola al tocar el efecto
- [ ] He cacheado un clip concreto en modo `User`
- [ ] He borrado la caché no usada sin perder nada
- [ ] `rendimiento.md` tiene el tamaño final anotado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| La franja no cambia nunca | El modo está en `None`, o el tramo no le parece pesado a `Smart` | Comprueba `Playback > Render Cache` y usa el modo `User` |
| Los fps no suben con el tramo cacheado | Estabas mirando un tramo que no era el cacheado | Colócate sobre el tramo con la franja en estado de cacheado |
| La caché no para de regenerarse | Sigues tocando el efecto: cada cambio la invalida | Cierra la decisión y después cachea |
| El disco se llena en modo `Smart` | La caché crece sola hasta donde le dejes | Pasa a `User` y borra lo no usado |
| He borrado la caché y ahora va lento | Es lo esperado: se regenera al reproducir | Reproduce el tramo y espera |
| No encuentro la carpeta de trabajo | Está en los ajustes del proyecto, no en las preferencias | `Master Settings`, sección de optimizados y caché |
| Borré una carpeta y el proyecto perdió material | No era la carpeta de trabajo | Reenlaza con el relink de la práctica 04, y comprueba la ruta antes de borrar |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · Diagnóstico, medios optimizados y proxies](01-diagnostico-optimizados-y-proxies.md) | **02 · La caché de render y el disco** | [03 · Sincronizar y preparar multicámara](03-sincronizar-y-preparar-multicamara.md) |

← [Volver a la Semana 05](../README.md)
