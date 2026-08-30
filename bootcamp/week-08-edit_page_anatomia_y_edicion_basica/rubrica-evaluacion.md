# 📊 Rúbrica de evaluación — Semana 08

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en la
tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 08` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Enuncia la regla que decide si algo se hace en la Cut page o en la Edit page. Pon un ejemplo
   de cada lado.
2. ¿Qué diferencia hay entre **bloquear** una pista y **apagarla**? ¿Cuál de las dos impide que
   esa pista salga en la exportación?
3. ¿Qué hace el `Sync Lock` y qué pasa en tu pieza si lo desactivas en la pista de títulos?
4. En el `Source Track Selector`, ¿qué representa la columna azul y qué la roja? ¿Cómo se edita
   un plano sin su audio?
5. Enumera los cuatro puntos de una edición. Si marcas entrada y salida en el origen y pones el
   cabezal en la timeline, ¿cuál se calcula y cómo?
6. ¿Qué es una edición hacia atrás (*backtiming*)? Describe un caso concreto en el que sea la
   forma correcta de montar.
7. Explica la diferencia entre `Overwrite`, `Insert` y `Ripple Overwrite` en términos de qué le
   pasa al resto de la timeline.
8. ¿Cuál es el único modo de edición que cambia la velocidad del clip y por qué lo hace? ¿Qué hay
   que comprobar después de usarlo?
9. ¿Qué hace `Place on Top` que ningún otro modo hace? ¿Por qué no hace caso al destino que
   tengas puesto?
10. ¿Qué pasa si desmarcas `Empty Timeline` al crear una timeline nueva? ¿Y si desmarcas
    `Use Project Settings`?

<details>
<summary>📝 Respuestas</summary>

**1.** La regla: **¿puedo decir lo que quiero sin nombrar una pista y un fotograma?** Si sí, Cut
page, que es más rápida. Si no, Edit page, que es la única que te deja decirlo.

Ejemplo de Cut: «este plano después de aquel». Ejemplo de Edit: «este plano en `Video 2`,
empezando justo cuando ella dice su nombre».

**2.** **Bloquear** (`Lock Track`) impide mover, sustituir o editar nada en esa pista, pero la
pista **se sigue viendo, se sigue etalonando y se sigue exportando**.

**Apagar** (`Enable Track`) hace lo contrario: los clips se pueden seguir editando, pero la pista
**no se ve en el visor, no llega a la Color page y no entra en el render**.

La que impide la exportación es **apagarla**, y no hay ningún aviso cuando eso pasa.

**3.** El `Sync Lock` decide si una pista **se desplaza junto con las demás cuando otra hace
ripple**.

Si lo desactivas en la pista de títulos y luego borras un plano de `Video 1` con ripple, todo el
montaje se recoloca hacia la izquierda pero **el rótulo se queda donde estaba**: ahora rotula el
plano equivocado. Con el `Sync Lock` activado, el rótulo se desplaza con el montaje y sigue
cayendo donde tenía que caer.

**4.** La columna **azul** son las pistas que trae el **clip de origen**; la **roja**, las pistas
de **tu timeline**. La fila donde coinciden dice qué componente del clip entra en qué pista.

Para editar un plano sin su audio: **apagar el icono de audio del origen** con un clic. Un icono
apagado no recibe ni entrega nada.

**5.** Los cuatro puntos: **entrada y salida del origen** (dónde empieza y acaba el trozo del
clip) y **entrada y salida de la timeline** (dónde empieza y acaba el hueco).

Si marcas los dos del origen y pones el cabezal en la timeline, el cabezal actúa como **entrada
de destino** y el que se calcula es la **salida de destino**: es la entrada más la duración de lo
que marcaste en el origen.

**6.** Es marcar **solo el final**: pones la salida en la timeline y Resolve alinea ahí la salida
del origen, colocando el clip hacia atrás desde ese punto.

Caso concreto: un recurso que tiene que **terminar** justo cuando entra una frase que ya está
montada. Cuándo empiece da igual; lo que no puede pasar es que siga después. Se marca la `O` en
ese fotograma y el plano se coloca solo.

**7.** **`Overwrite`** pisa: borra lo que hubiera donde cae el clip nuevo y **la pieza dura
igual**.

**`Insert`** parte y empuja: todo lo que venía detrás se desplaza a la derecha y **la pieza se
alarga** la duración del clip nuevo. Los clips de otras pistas que se solapan hacia la izquierda
del punto de inserción **no** se mueven.

**`Ripple Overwrite`** sustituye un clip por otro de duración distinta y **recoloca lo de detrás
para que no queden ni huecos ni solapes**: a la derecha si el nuevo es más largo, a la izquierda
si es más corto. La pieza se alarga o se acorta.

**8.** **`Fit to Fill`**, y lo hace porque es el único que usa los cuatro puntos: estira o
comprime el rango marcado del origen para que llene exactamente el rango marcado de la timeline.

Después hay que comprobar en el **Inspector** a qué porcentaje ha quedado el clip. Por debajo del
**80 %** con material grabado a 24 fps la cámara lenta se ve a tirones, y `Fit to Fill` no avisa
del porcentaje.

**9.** **Crear pistas.** Sube el clip a la primera pista libre por encima de lo que haya —o por
debajo, si es audio— y si no hay ninguna, la crea.

No hace caso al destino porque su función es precisamente **superponer**: se usa para títulos,
recursos y versiones de un plano que quieres conservar debajo, y en todos esos casos lo que
importa es que quede encima, no en qué número de pista.

**10.** Si desmarcas **`Empty Timeline`**, la timeline nace con **todo el material de todos los
bins del media pool** dentro, uno detrás de otro. Es útil para revisar dailies y una sorpresa
desagradable si no lo esperabas.

Si desmarcas **`Use Project Settings`** —o pulsas `Use Custom Settings`— aparecen los paneles
`Format`, `Monitor`, `Output` y `Color`, y esa timeline pasa a tener sus propios ajustes de
resolución, frame rate y gestión de color, independientes del proyecto. Un frame rate distinto
del proyecto desincroniza el audio poco a poco y el problema no aparece hasta pasados unos
minutos de montaje.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **11,11 puntos**.

```bash
python scripts/verificar-semana.py 08
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 01 | `proyecto-abierto` | 11,11 |
| 01 | `frame-rate-bloqueado` | 11,11 |
| 01 | `montaje-v2-conservada` | 11,11 |
| 02 | `escena-v1-existe` | 11,11 |
| 02 | `escena-v1-activa` | 11,11 |
| 02 | `escena-v1-pistas` | 11,11 |
| 02 | `escena-v1-pistas-con-nombre` | 11,11 |
| 03 | `escena-v1-clips` | 11,11 |
| 04 | `escena-v1-sin-huecos` | 11,11 |

**Necesitas 70 / 100**, es decir **al menos 7 de los 9 checks**.

> [!TIP]
> Cinco de los nueve —`escena-v1-activa`, `escena-v1-clips`, `escena-v1-sin-huecos`,
> `escena-v1-pistas` y `escena-v1-pistas-con-nombre`— leen **la timeline activa**. Si te quedaste
> comparando en `BC-Montaje-v2`, fallan los cinco de golpe aunque el trabajo esté perfecto. Doble
> clic en `BC-Escena-v1` y repite: es lo primero que hay que descartar.
>
> Si fallan **todos**, el puente no está lanzado: `Workspace > Scripts > Utility`.

---

## 📦 Producto (30 %)

Tu escena y las decisiones que la construyeron. Se evalúa con criterios observables.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| La escena se reproduce entera y se entiende sin que la expliques | 15 |
| No hay ningún parpadeo a negro en toda la reproducción | 10 |
| Los nombres de las cinco pistas describen lo que hay dentro | 5 |
| `BC-Montaje-v2` conserva su contenido y tiene sus pistas nombradas | 5 |
| `notas-de-montaje.md` tiene el apartado `## Edit page — Semana 08` con sus cinco puntos | 5 |
| Las cifras del apartado son cifras, incluido el porcentaje del `Fit to Fill` | 5 |
| `BC-Bootcamp-Resolve-semana08.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Cada uso de un modo de edición tiene su motivo escrito, con el corte concreto | 15 |
| El `Replace` hace coincidir de verdad una acción con un fotograma | 10 |
| El `Fit to Fill` no se ve a tirones y su porcentaje está por encima del 80 % | 5 |
| Los recursos de `Recursos` tapan lo que tenían que tapar, y solo eso | 5 |
| El sonido de los recursos está en `Ambiente`, no mezclado con la voz | 5 |
| La comparación entre la versión de Cut y la de Edit está contestada con ejemplos | 10 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| El media pool | `BC-Montaje-v2` y `BC-Escena-v1`, las dos, colgando de `Master` |
| Las cinco cabeceras de `BC-Escena-v1` | Nombre propio, ninguna apagada, ninguna en solo |
| Cabecera de `Recursos`, desactivándola | La escena sigue entendiéndose, solo desaparecen los insertos |
| Cabecera de `Ambiente`, desactivándola | La voz sigue entera |
| `Dialogo` en solo | Solo se oye voz |
| El plano del `Fit to Fill`, en el Inspector | El porcentaje de `Speed` está escrito en las notas |
| El plano del `Replace`, a velocidad normal | La acción cae donde tenía que caer |
| La pista `Reserva` | Vacía: la música es la Fase 4 |
| La escena entera | Ni música, ni títulos diseñados, ni color, ni efectos |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| `BC-Montaje-v2` ha desaparecido o se ha remontado | −20 |
| La escena tiene un parpadeo a negro | −15 |
| Todos los planos se montaron con `Overwrite`: no se practicaron los modos | −15 |
| El sonido de los recursos está en `Dialogo` | −10 |
| Hay música, títulos diseñados, color o efectos | −10 |
| Las pistas conservan su nombre por defecto en `BC-Montaje-v2` | −5 |
| Un plano de `Fit to Fill` por debajo del 40 % con material a 24 fps | −5 |
| Alguna pista quedó apagada o en solo al cerrar la semana | −10 |
| El apartado de notas describe con adjetivos y no con cifras y cortes concretos | −10 |
| Se empezó a afinar cortes al fotograma, que es la Semana 09 | −5 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

Esta semana abre la Fase 3 y es la base de las cuatro siguientes. Un `Fit to Fill` regular no
bloquea nada, pero no entender el control de destino sí: la Semana 09 entera lo da por sabido.

- **Si fallan `escena-v1-activa` y los cuatro siguientes**: tienes abierta otra timeline. Doble
  clic en `BC-Escena-v1`. Es lo primero que hay que descartar, siempre.
- **Si falla `montaje-v2-conservada`**: renombraste el montaje en vez de crear una timeline
  aparte. Recupéralo del respaldo `BC-Bootcamp-Resolve-semana07.drp`, importándolo con otro
  nombre para no machacar lo que tienes.
- **Si falla `escena-v1-clips`**: la escena está montada en la pista de arriba. El check mira la
  primera pista de vídeo. Vuelve a montarla en `Continuidad`.
- **Si falla `escena-v1-sin-huecos`**: hay un hueco o un solape. Activa el imán con `N`, recorre
  la pista en `Detail Zoom` y bórralo con ripple. Suele estar donde usaste `Fit to Fill`.
- **Si falla `escena-v1-pistas`**: faltan pistas. Clic derecho en una cabecera `> Add Track`.
- **Si falla `escena-v1-pistas-con-nombre`**: alguna conserva su nombre por defecto, casi siempre
  `Reserva`, que está vacía y se olvida. Para poder editar el nombre, la pista tiene que ser lo
  bastante alta.
- **Si el cuestionario va por debajo de 70**: las preguntas 3, 5 y 7 son las que más gente falla,
  y las tres son el mismo tema de fondo —qué se mueve cuando algo cambia de duración—. Vuelve a
  las teorías 04, 07 y 08.
- **Si el producto va por debajo de 70**: casi siempre es una de dos. O montaste todo con
  `Overwrite` y la semana se quedó en teoría, o no escribiste la comparación mientras la tenías
  fresca. Lo primero se arregla rehaciendo tres ediciones con el modo correcto; lo segundo, solo
  se arregla hoy.
- **Si te faltó tiempo**: prioriza las prácticas 02 y 03. La 01 es reconocimiento de terreno y se
  puede recuperar sobre la marcha; el control de destino y los modos de edición, no.

---

← [Volver a la Semana 08](README.md)
