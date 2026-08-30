# 🎥 Videografía — Semana 10

> Esta es una semana que se ve mejor de lo que se lee. La diferencia entre `Frame Blend` y
> `Optical Flow` no cabe en una frase: hay que ver los dos artefactos moviéndose. Lo mismo con una
> rampa bien puesta y una mal puesta.

---

## Canal oficial

### Blackmagic Design — canal de YouTube

<https://www.youtube.com/@BlackmagicDesign>

**Por qué vale la pena**: es donde se anuncian los cambios de comportamiento entre versiones, y el
retime es una zona que ha cambiado: las opciones `Enhanced` del `Motion estimation mode` y el
`Speed Warp` con motor neuronal son relativamente recientes. Un tutorial de hace cinco años enseña
un desplegable con la mitad de opciones.

**Qué buscar para esta semana**: la presentación de la versión que tengas instalada, y cualquier
vídeo cuyo título mencione *retime*, *speed ramp*, *optical flow* o *stabilization*.

---

## Formación oficial

### Blackmagic Design Training — vídeos y cursos

<https://www.blackmagicdesign.com/products/davinciresolve/training>

**Por qué vale la pena**: los vídeos de las guías oficiales enseñan el gesto completo a velocidad
real. En los `Retime Controls` eso es justo lo que falta en el manual: ver a alguien arrastrar el
asa de arriba y luego la de abajo, sobre el mismo punto, aclara en diez segundos lo que un párrafo
no aclara.

**Qué mirar**: el bloque de *speed effects* del curso de montaje, y el de *stabilization*. Si el
índice separa *retime controls* de *retime curves*, mira los dos: son las teorías 04 y 05.

---

## Cómo aprovechar un tutorial de velocidad

Los tutoriales de retime de internet tienen un sesgo muy marcado y conviene conocerlo antes de
copiar nada:

1. **Casi todos usan material sobrecadenciado sin decirlo.** El plano del tutorial está grabado a
   120 fps y por eso el 20 % se ve perfecto. Con tu material a 24 fps, el mismo 20 % es un
   desastre. Si el tutorial no dice la cadencia de rodaje, no es replicable.
2. **Casi todos ponen la rampa encima del golpe.** Funciona en un montaje de dos planos y no
   funciona en una pieza. La rampa cae **antes**.
3. **Casi ninguno enseña el artefacto.** El plano se ve al 40 % de tamaño en la esquina de la
   pantalla, donde el *warping* no se ve. Comprueba siempre a tamaño completo.
4. **Casi ninguno menciona `Ripple Sequence`.** Trabajan con un solo clip en la timeline, donde la
   casilla da igual. En tu pieza no da igual.

Un tutorial que sí sirve dice tres cosas: **a qué cadencia se rodó, a qué porcentaje se retima y
qué `Retime Process` está puesto**. Si faltan las tres, es una demostración, no una lección.

---

## Cómo aprovechar un tutorial de estabilización

Aquí el sesgo es otro y es más fácil de detectar: **el tutorial estabiliza un plano que se
estabiliza solo**. Un plano con mucho detalle, buena luz y un temblor regular.

Lo que hay que buscar es lo contrario: un vídeo que enseñe qué pasa cuando el estabilizador falla,
y qué se hace entonces. Los términos en inglés que lo encuentran son *rolling shutter*,
*stabilization artifacts* y *warping*.

---

## Lo que no hace falta buscar

- Plugins de retime de terceros. Ni hacen falta, ni entran en un bootcamp que se hace en Free
- Tutoriales de *frame interpolation* con herramientas externas. Es otro tema y otra semana
- Tutoriales de estabilización en Fusion. Es la Fase 6, con el `Planar Tracker` y el
  `Camera Tracker`

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Libros](../ebooks-free/README.md) | **Videografía Semana 10** | [Webgrafía](../webgrafia/README.md) |

← [Volver a la Semana 10](../../README.md)
