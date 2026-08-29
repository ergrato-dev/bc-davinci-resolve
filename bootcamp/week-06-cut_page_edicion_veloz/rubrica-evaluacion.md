# 📊 Rúbrica de evaluación — Semana 06

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en
la tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 06` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Explica qué es un montaje bruto y por qué se hace antes que el acabado. ¿Cuál es el
   criterio objetivo de que está terminado?
2. Nombra cuatro diferencias entre la Cut page y la Edit page, y di qué relación tienen las
   dos páginas con la timeline del proyecto.
3. ¿Qué muestra cada una de las dos timelines de la Cut page? ¿Por qué el cabezal de la de
   abajo no se mueve?
4. ¿Qué es el source tape, qué determina el orden de la cinta y en qué se diferencia de
   abrir los clips uno a uno?
5. ¿Por qué la velocidad de Fast Review no es constante? Nombra dos problemas que detecta y
   dos que no.
6. Enuncia la regla del indicador inteligente. ¿Cómo fuerzas que una edición caiga en medio
   de un plano y no en el corte de al lado?
7. Diferencia Smart Insert de Ripple Overwrite: qué le pasa a lo que había en el destino y
   qué le pasa a la duración de la timeline.
8. ¿Qué significa que una edición sea *de ripple*, y qué consecuencia tiene sobre lo que ya
   tengas colocado en la pista de encima?
9. ¿Por qué un plano de recurso se pone con Place on Top y no con Ripple Overwrite? ¿Qué
   pasa con el audio en cada caso?
10. ¿De dónde saca el sync bin la alineación, cómo se comprueba en treinta segundos que es
    fiable, y qué se hace si no lo es?

<details>
<summary>📝 Respuestas</summary>

**1.** Un **montaje bruto** es la versión de una pieza que ya va de principio a fin pero no
está acabada por ningún lado: cortes aproximados, sin transiciones ni títulos, con el
sonido que trajo cada clip.

Se hace antes porque una pieza no es la suma de sus planos, sino su **orden** y su
**duración total**, y ninguna de las dos cosas se puede juzgar hasta que la pieza existe
entera.

El criterio de terminación es objetivo y no tiene nada que ver con el gusto: **la pieza
llega al final**. Si la reproduces entera y termina donde tenía que terminar, la pasada
está hecha.

**2.** Cuatro cualesquiera de estas: un visor en lugar de dos; timeline doble sin zoom que
gestionar; seis botones de edición siempre visibles; el source tape; el sync bin; no hay
que elegir pista de destino ni posición.

Y lo importante: **las dos páginas trabajan sobre la misma timeline del mismo proyecto**.
Cambiar de página no exporta, no convierte y no copia nada.

**3.** La de **arriba** muestra la timeline entera, siempre completa, a escala fija, con un
rectángulo que marca el tramo visible abajo. Sirve para orientarse, saltar lejos y leer la
forma de la pieza.

La de **abajo** muestra el detalle ampliado del punto donde estás.

El cabezal de la de abajo no se mueve porque **es la timeline la que se desplaza por
debajo**. La ventaja es que el sitio donde vas a trabajar está siempre en el mismo píxel de
la pantalla.

**4.** El **source tape** es el modo del visor que presenta todos los clips del bin
seleccionado como una sola cinta continua, recorrible con el transporte normal y marcable
con `I` y `O`.

El orden de la cinta es **el orden del bin**: ordenando el bin ordenas la cinta.

Frente a abrir clips uno a uno, ahorra el bucle de abrir-ver-cerrar por archivo y, sobre
todo, **no rompe el hilo**: el material pasa seguido y evalúas el conjunto, no un archivo
cada vez.

**5.** Porque reparte el **tiempo de pantalla**, no la velocidad: cada clip recibe
aproximadamente el mismo rato de revisión, de modo que los largos pasan deprisa y los
cortos casi a velocidad normal. Con una velocidad fija, o te saltas los clips cortos o los
largos siguen tardando.

Detecta: tramos que se hacen largos, planos repetidos, saltos bruscos de contenido, que
falte el cierre, material desequilibrado.

No detecta: cortes que caen tarde o pronto, problemas de audio (está silenciado), fallos
finos de continuidad, calidad del encuadre.

**6.** La regla: **si el cabezal está cerca de un punto de corte, el destino de la edición
es ese corte; si no hay ninguno cerca, el destino es la posición del cabezal**.

Para que caiga en medio de un plano, **aleja el cabezal de cualquier corte** y colócalo
exactamente donde quieres. El indicador dejará de señalar un corte.

**7.** **Smart Insert** mete el clip en el punto de corte y **desplaza hacia la derecha**
todo lo que venía después. No se pierde nada y la timeline se alarga exactamente lo que
mide el clip nuevo.

**Ripple Overwrite** **sustituye** el clip que hay en el destino, que sale del montaje, y
recoloca el resto sin huecos. La timeline se alarga o se acorta según la diferencia de
duración entre el que entra y el que sale.

La pregunta que decide es una: ¿lo que hay en el destino se queda o se va?

**8.** Una edición **de ripple** desplaza en cadena todo lo que viene detrás, para que no
queden huecos.

La consecuencia: **mueve todo lo que hay a la derecha**, incluidos los recursos y los
rótulos que tuvieras colocados en la pista de encima, que dejan de coincidir con lo que
tapaban. Por eso la estructura de `Video 1` se cierra **antes** de poner nada en `Video 2`.

**9.** Porque un plano de recurso **no sustituye a nada**: tapa la imagen y deja intacto lo
de debajo.

Con **Place on Top**, el clip va a la pista de encima: la imagen cambia y **el audio de la
entrevista sigue sonando**, porque las pistas de audio se suman en vez de taparse.

Con **Ripple Overwrite**, el clip sustituye al que había, y con él **se va su audio**: has
perdido el trozo de entrevista que querías conservar.

**10.** De la **hora de grabación** que cada cámara escribió en el archivo al grabar.

La comprobación: coloca el cabezal en un momento reconocible —una palmada, alguien que
entra— y mira si los ángulos que ofrece el sync bin enseñan **ese mismo instante**.

Si no lo es, el sync bin alinea mal en silencio. En ese caso se monta con el **clip
multicámara** de la Semana 05, que se sincronizó por forma de onda y no depende de los
relojes de las cámaras.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **12,5 puntos**.

```bash
python scripts/verificar-semana.py 06
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 01 | `proyecto-abierto` | 12,5 |
| 01 | `frame-rate-bloqueado` | 12,5 |
| 01 | `timeline-montaje-existe` | 12,5 |
| 04 | `timeline-sync-cut-existe` | 12,5 |
| 01 | `montaje-activo` | 12,5 |
| 02 | `montaje-clips` | 12,5 |
| 02 | `montaje-duracion` | 12,5 |
| 03 | `montaje-pista-superior` | 12,5 |

**Necesitas 70 / 100**, es decir **al menos 6 de los 8 checks**.

> [!TIP]
> Los cuatro últimos leen `timeline_probe`, que devuelve **la timeline activa**. Si
> terminaste la práctica 04 y te quedaste en `BC-Sync-Cut-v1`, fallan los cuatro de golpe
> aunque el trabajo esté perfecto. Doble clic en `BC-Montaje-v1` y repite: es lo primero
> que hay que descartar.
>
> Si fallan **todos**, el puente no está lanzado: `Workspace > Scripts > Utility`.

---

## 📦 Producto (30 %)

Tu montaje bruto. Se evalúa con criterios observables.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| La pieza se reproduce de principio a fin y termina donde tenía que terminar | 15 |
| Tiene apertura, desarrollo y cierre reconocibles | 10 |
| No hay huecos: ningún parpadeo a negro en toda la reproducción | 5 |
| `notas-de-montaje.md` existe en `04-respaldos/` con sus seis apartados | 5 |
| Las cifras de duración y número de clips son cifras, no adjetivos | 5 |
| `BC-Sync-Cut-v1` tiene la escena montada con varios cambios de ángulo | 5 |
| `BC-Bootcamp-Resolve-semana06.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| El orden es una decisión, no el orden de grabación del material | 10 |
| Los planos tienen margen a los lados para ajustar en la Semana 09 | 10 |
| La continuidad vive en `Video 1`: desactivar `Video 2` deja una pieza que funciona | 5 |
| Los recursos empiezan antes del salto y acaban después | 5 |
| Hay recursos, pero se ve a quien habla la mayor parte del tiempo | 5 |
| Close Up usado con criterio: dos o tres como mucho, y no se ven blandos | 5 |
| El multicámara suena a una sola fuente: sin eco ni voz doblada | 5 |
| No hay nada que todavía no toque: ni títulos, ni transiciones, ni música, ni color | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| La timeline de arriba, de un vistazo | Se reconoce una forma: no es un ladrillo liso ni un metrónomo |
| Reproducción completa, sin parar | Ningún parpadeo negro entre clips |
| Cabecera de `Video 2`, desactivándola | El montaje sigue funcionando, con el mismo audio y duración |
| Un corte cualquiera, extendiéndolo | Hay material a los dos lados: se marcó con margen |
| Un recurso, en reproducción | Empieza antes del salto y acaba después |
| Un Close Up, a pantalla completa | Se ve aceptable, no blando |
| Un cambio de ángulo en `BC-Sync-Cut-v1` | La voz no salta, no se repite y no cambia de sala |
| El media pool | `BC-Montaje-v1` y `BC-Sync-Cut-v1`, con esos nombres exactos |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| El montaje no llega al final de la pieza | −25 |
| Hay huecos entre clips que producen parpadeos a negro | −15 |
| Hay títulos, transiciones, música o correcciones de color | −10 |
| Los planos están recortados al fotograma, sin margen | −10 |
| Los saltos se taparon con Ripple Overwrite y se perdió audio de entrevista | −10 |
| Los recursos empiezan justo en el corte | −5 |
| Más de cinco Close Up en la pieza | −5 |
| El montaje entero está en la pista de arriba | −10 |
| En el multicámara suenan dos pistas de audio a la vez | −10 |
| `notas-de-montaje.md` describe con adjetivos y no con cifras | −10 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

No pases a la Semana 07 sin haber cerrado esta. La 07 acaba el montaje bruto —transiciones,
velocidad, títulos rápidos, exportación— y no hay nada que acabar si la pieza no llega al
final.

- **Si falla `montaje-activo` y con él los tres siguientes**: tienes abierta otra timeline.
  Doble clic en `BC-Montaje-v1`. Es lo primero que hay que descartar, siempre.
- **Si falla `montaje-clips` o `montaje-duracion`**: la primera pasada no está completa.
  Vuelve a la práctica 02 y sigue montando; no es un problema de ajuste, es que falta pieza.
- **Si falla `montaje-pista-superior`**: no has editado sobre la pista de encima. Práctica
  03, paso 6: Place on Top crea `Video 2` al colocar el primer recurso.
- **Si falla un check de timeline**: es el nombre. `BC-Montaje-v1` y `BC-Sync-Cut-v1`, con
  guiones y las uves minúsculas.
- **Si fallan todos**: el puente no está lanzado.
- **Si el cuestionario va por debajo de 70**: las preguntas 6, 8 y 9 son las que más gente
  falla. Vuelve a las teorías 05, 07 y 08.
- **Si el producto va por debajo de 70**: casi siempre es lo mismo, y es de las dos cosas
  una: la pieza no llega al final, o te pusiste a afinar cortes. Las dos se arreglan
  repitiendo la práctica 02 con la regla del paso 0: no se para a arreglar.
- **Si te faltó tiempo**: prioriza la práctica 02. Las correcciones de la 03 se hacen
  cualquier lunes y el sync bin vuelve en la Semana 12; un montaje que no llega al final
  bloquea la Fase 3 entera.

---

← [Volver a la Semana 06](README.md)
