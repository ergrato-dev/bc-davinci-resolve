# Cómo Resolve inventa los fotogramas que faltan

> Le has pedido cuarenta y ocho fotogramas por segundo a un plano que tiene veinticuatro. Resolve
> tiene que poner los otros veinticuatro de algún sitio. Hay tres formas de hacerlo y la buena no
> siempre es la mejor: es la que menos se nota en **ese** plano.

## 🎯 Objetivos

- Explicar qué hace cada uno de los tres métodos de `Retime Process`
- Elegir el método por el tipo de movimiento del plano, no por «el de más calidad»
- Saber dónde se fija el método para todo el proyecto y dónde para un clip suelto
- Entender qué es el análisis de movimiento y por qué falla donde falla
- Saber qué es `Speed Warp`, por qué es de Studio y qué hacer en Free
- Reconocer un artefacto de `Optical Flow` y decidir a qué método bajar

---

## 1. Qué problema resuelve

Cuando un plano se ralentiza por debajo de su techo ([teoría 01](01-el-techo-de-la-camara-lenta.md)),
faltan fotogramas. Cuando un clip está grabado a una cadencia distinta de la de la timeline,
también faltan o sobran. En los dos casos, Resolve tiene que rellenar.

El ajuste que decide cómo se rellena se llama **`Retime Process`**, y es el mismo para las dos
situaciones. Es un ajuste que casi nadie toca porque está lejos y en inglés, y es el que separa
una cámara lenta que se ve bien de una que se ve mal.

---

## 2. Cómo funciona

![Los tres métodos de relleno enfrentados sobre el mismo movimiento: Nearest repite el fotograma anterior y produce saltos, Frame Blend mezcla dos fotogramas y produce una imagen fantasma, y Optical Flow calcula hacia dónde iba cada píxel y dibuja un fotograma nuevo](../0-assets/06-los-tres-metodos-de-relleno.svg)

### 2.1 Los tres métodos

| Método | Qué hace | Coste | Defecto típico |
| ------ | -------- | ----- | -------------- |
| **`Nearest`** | Repite el fotograma anterior, o tira los que sobran | El más barato | *Judder*: la imagen avanza a tirones |
| **`Frame Blend`** | Funde dos fotogramas contiguos para inventar el intermedio | Barato | *Ghosting*: doble imagen fantasmal |
| **`Optical Flow`** | Calcula hacia dónde se movía cada parte de la imagen y **dibuja un fotograma nuevo** | El más caro | *Warping*: los bordes se derriten |

El nombre de la tercera lo dice todo: **flujo óptico** es el nombre técnico de estimar el
movimiento comparando dos imágenes. Resolve mira el fotograma de antes y el de después, deduce que
un objeto iba de aquí a allá, y pinta el punto intermedio.

### 2.2 Cuándo cada uno

La tentación es poner `Optical Flow` en todo y olvidarse. El manual avisa de lo contrario: **la
opción de más calidad no siempre es la mejor para un plano concreto**.

| El plano tiene… | Elige | Por qué |
| --------------- | ----- | ------- |
| Un movimiento **lineal y limpio**: un travelling, alguien andando de perfil | `Optical Flow` | Es donde brilla: el movimiento es predecible |
| Dos cosas que **se cruzan** en direcciones distintas | `Frame Blend` | Optical Flow no sabe qué hay detrás de qué y derrite los bordes |
| **Agua, humo, fuego, hojas, lluvia, partículas** | `Frame Blend` | No hay un movimiento que estimar: hay mil |
| Cámara en mano con **movimiento brusco e impredecible** | `Frame Blend` | El análisis pierde el rastro entre fotograma y fotograma |
| **Ruido** de sensor visible, planos nocturnos | `Frame Blend` o `Nearest` | El ruido es aleatorio y el análisis lo interpreta como movimiento |
| Un plano que va a ser un **fondo desenfocado** | `Nearest` | No se va a mirar; ahorra tiempo de render |
| Un retime muy pequeño, del 90 % al 110 % | `Nearest` | Casi no faltan fotogramas: los otros dos no aportan |

La regla corta: **`Optical Flow` para movimiento simple, `Frame Blend` para movimiento caótico.**

### 2.3 El modo de estimación de movimiento

Cuando el método es `Optical Flow`, hay un segundo ajuste, `Motion estimation mode`, que decide
cuánto esfuerzo se dedica al cálculo:

| Opción | Qué es |
| ------ | ------ |
| `Standard Faster` | El clásico, rápido |
| `Standard Better` | El clásico, más cuidadoso |
| `Enhanced Faster` | Mejor que los estándar en casi todos los casos con artefactos, y más lento |
| `Enhanced Better` | La mejor opción sin motor neuronal |
| `Speed Warp Faster` · `Speed Warp Better` | Con el **DaVinci Neural Engine**. Ver 2.5 |
| `AI Speed Warp Metal` | Versión acelerada por hardware de Apple. **Solo macOS** |

Y un tercer ajuste que acompaña, `Motion range`: `Small`, `Medium` o `Large`, según cuánto se
mueven las cosas entre un fotograma y el siguiente. Un plano de un colibrí no es un plano de una
nube.

### 2.4 Dónde se fija cada cosa

Hay **dos niveles**, y saber cuál estás tocando evita media hora de confusión:

| Nivel | Ruta | Afecta a |
| ----- | ---- | -------- |
| **Proyecto** | `File > Project Settings > Master Settings > Frame Interpolation` | Todos los clips que estén en `Project Settings` |
| **Clip** | `Inspector > Video > Retime and Scaling > Retime Process` | Solo ese clip |

Todos los clips vienen de fábrica en **`Project Settings`**, que significa «lo que diga el
proyecto». Cambiar el ajuste del proyecto cambia el comportamiento de todos menos de los que hayas
puesto a mano.

El flujo de trabajo sensato:

1. Deja el proyecto en `Optical Flow` con `Enhanced Better` si tu equipo lo aguanta, o en
   `Frame Blend` si no
2. Baja **clip por clip** los que salgan con artefactos

### 2.5 `Speed Warp`: qué es y qué hacer sin él

> [!IMPORTANT]
> **Studio** · `Speed Warp` y `AI Speed Warp Metal` usan el **DaVinci Neural Engine**, el motor de
> inteligencia artificial de Resolve, que solo está en DaVinci Resolve Studio. En Free, esas
> opciones no producen el resultado del motor neuronal.
>
> **En Free**: `Optical Flow` con `Enhanced Better`, que sí está disponible, y quedarse **por
> encima del techo** del plano. Un plano a 60 fps ralentizado al 45 % con `Enhanced Better` se ve
> perfectamente. El motor neuronal se nota cuando le pides al material lo que no tiene, y eso es
> justo lo que este bootcamp te está enseñando a no hacer.
>
> *Comparativa oficial de funciones: <https://www.blackmagicdesign.com/products/davinciresolve/studio>*

### 2.6 Por qué la timeline va lenta después de retimar

`Optical Flow` calcula fotogramas nuevos **en tiempo real** mientras reproduces. Es la operación
más cara de la Edit page y, en un equipo modesto, la reproducción se cae a la mitad.

No es un fallo y no se arregla cambiando el método: se arregla **cacheando**. El `Render Cache` de
la Semana 05 calcula esos fotogramas una vez y los guarda:

- `Playback > Render Cache > Smart` — Resolve decide qué cachear, y los retimes entran
- El color de la barra sobre la timeline dice si ese tramo ya está cacheado

---

## 3. Cómo se hace en Resolve 21

### 3.1 Fijar el método para todo el proyecto

1. `File > Project Settings`
2. Panel `Master Settings`
3. Grupo `Frame Interpolation`
4. Desplegable `Retime Process`
5. Si eliges `Optical Flow`, elige también en `Motion estimation mode` y en `Motion range`

### 3.2 Cambiar el método de un clip suelto

1. Selecciona el clip
2. `Inspector > Video`, grupo **`Retime and Scaling`**
3. Desplegable `Retime Process`
4. Con `Optical Flow`, aparece también su `Motion estimation mode`

De fábrica pone `Project Settings`: eso significa que hereda. En cuanto eliges otra cosa, ese clip
deja de hacer caso al proyecto.

### 3.3 Comparar dos métodos en el mismo plano

La única forma honesta de elegir:

1. Retima el plano
2. Ponlo en `Frame Blend` y reprodúcelo en bucle: `Ctrl+/` (Win) / `Cmd+/` (Mac) y `/`
3. Sin parar, cámbialo a `Optical Flow` en el Inspector
4. Mira **los bordes de lo que se mueve**

En treinta segundos sabes cuál es. Escribe cuál elegiste y por qué: en la Semana 28, al exportar,
te va a volver a hacer falta.

### 3.4 Cachear lo retimado

`Playback > Render Cache > Smart`, y espera a que la barra de encima de la timeline cambie de
color en ese tramo. La reproducción vuelve a ir a velocidad real.

---

## 4. Antipatrones

| Antipatrón | Por qué duele | Qué hacer |
| ---------- | ------------- | --------- |
| Poner `Optical Flow` en todo el proyecto y no mirar | Los planos de agua y humo salen derretidos | Baja esos a `Frame Blend`, clip por clip |
| Elegir el método sin mirar el plano al 100 % | Los artefactos no se ven en un visor pequeño | Amplía el visor y mira los bordes |
| Culpar al método cuando el problema es el techo | Ningún método inventa treinta fotogramas de cada cuarenta | Sube el porcentaje |
| Cambiar el ajuste del proyecto para arreglar un clip | Cambias los otros cuarenta sin querer | El ajuste del clip está en el Inspector |
| Buscar `Speed Warp` en Free | No hay motor neuronal en Free | `Enhanced Better` y respetar el techo |
| Dar por hecho que la timeline va lenta por el ordenador | Es el coste del cálculo en tiempo real | `Render Cache > Smart` |
| Renderizar la entrega sin comprobar los retimes | Los artefactos se ven más en el archivo final que en el visor | Revisa los tramos retimados en la Semana 28 |

---

## 5. Trucos

| Truco | Cómo |
| ----- | ---- |
| Cambiar el método de un clip suelto | `Inspector > Video > Retime and Scaling > Retime Process` |
| Cambiarlo para todo el proyecto | `Project Settings > Master Settings > Frame Interpolation` |
| Saber si un clip hereda o tiene su propio ajuste | Si pone `Project Settings`, hereda |
| Comparar dos métodos sin parar la reproducción | Bucle con `Ctrl+/` / `Cmd+/` y cambia el desplegable mientras suena |
| Ajustar el análisis al tipo de movimiento | `Motion range`: `Small`, `Medium` o `Large` |
| Recuperar la reproducción en tiempo real | `Playback > Render Cache > Smart` |
| Saber qué tramos están cacheados | La barra de color sobre la regla de tiempo |
| Ver el artefacto donde de verdad está | Amplía el visor y mira los bordes de lo que se mueve |

---

## 📚 Recursos Adicionales

- [DaVinci Resolve Reference Manual](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion) — capítulo 58, sección «Speed Effect Processing», y capítulo 6, sección «Frame Interpolation» de los Project Settings.
- [Comparativa oficial Free / Studio](https://www.blackmagicdesign.com/products/davinciresolve/studio) — la fuente de verdad sobre qué necesita el motor neuronal.
- [Semana 05 · El render cache](../../week-05-proxies_cache_y_sincronizacion/1-teoria/04-la-cache-de-render.md) — por qué la timeline se cae y cómo se arregla.
- [docs/free-vs-studio.md](../../../docs/free-vs-studio.md) — la tabla del bootcamp, con `Speed Warp` y su alternativa.

---

## ✅ Checklist de Verificación

- [ ] Sé qué hace `Nearest`, `Frame Blend` y `Optical Flow`
- [ ] Sé elegir el método por el tipo de movimiento del plano
- [ ] Sé dónde está el ajuste del proyecto y dónde el del clip
- [ ] Sé qué significa que un clip ponga `Project Settings`
- [ ] Sé qué es `Speed Warp`, por qué es de Studio y qué usar en Free
- [ ] Sé reconocer *judder*, *ghosting* y *warping* y a qué método bajar
- [ ] Sé por qué la reproducción se cae y cómo recuperarla

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [05 · Las curvas de retime](05-las-curvas-de-retime.md) | **06 · Cómo Resolve inventa los fotogramas que faltan** | [07 · Transform, crop y dynamic zoom](07-transform-crop-y-dynamic-zoom.md) |

← [Volver a la Semana 10](../README.md)
