# Proyecto — Semana 09: el montaje afinado

> Tu pieza contaba la historia. A partir de esta semana la cuenta **sin que se note el montaje**,
> que es una cosa distinta y bastante más difícil. El entregable no es un archivo nuevo: es la
> misma pieza, más corta, más limpia y con una lista escrita de por qué.

## 📦 Qué añade esta semana

La novena capa: **`BC-Montaje-v3`, el montaje afinado**.

Concretamente, cuatro cosas:

1. **`BC-Montaje-v3`**, duplicada de `BC-Montaje-v2` y afinada de principio a fin: sin planos que
   sobren, sin huecos, con las entradas y las salidas colocadas.
2. **Dos split edits o más**, hechos con trim asimétrico, en los sitios donde la pieza los pedía.
3. **Ocho marcadores o más** con nombre propio: los que quedan son la lista de trabajo con la que
   arranca la Semana 10.
4. **La comparación escrita** entre `BC-Montaje-v2` y `BC-Montaje-v3`, con cifras.

> [!IMPORTANT]
> `BC-Montaje-v2` **no se toca**. Es la referencia contra la que se mide la semana, y la
> comparación del paso 8 de la práctica 04 la necesita entera. Es la convención de versionado de
> [`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md): cada fase duplica
> y trabaja sobre la copia.

Y una cosa que no es un archivo: **el hábito de trimar con el teclado**. De la Semana 10 a la 36
vas a afinar cortes todas las semanas. Hacerlo con `V`, `U`, `,` y `.` en vez de con el ratón es
la diferencia entre afinar la pieza entera y afinar los tres primeros minutos.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca carácter
a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` del proyecto sigue siendo **24**
3. **`BC-Montaje-v2`** sigue existiendo
4. Existe la timeline **`BC-Montaje-v3`**
5. **`BC-Montaje-v3`** es la timeline abierta
6. **Ninguna pista** conserva su nombre por defecto
7. Su pista de vídeo principal conserva **quince clips o más**
8. Esa pista **no tiene huecos ni solapes**
9. Hay **dos split edits o más** en la primera pista de audio
10. Hay **ocho marcadores o más**, todos con nombre propio

```bash
python scripts/verificar-semana.py 09
```

Con el proyecto abierto, **`BC-Montaje-v3` como timeline activa** y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!NOTE]
> Los checks 5 a 10 leen **la timeline activa**. Si te quedaste comparando en `BC-Montaje-v2` en el
> paso 8 de la práctica 04, fallan los seis de golpe aunque el trabajo esté perfecto. Doble clic en
> `BC-Montaje-v3` y repite.
> *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de 2026.*

El suelo del check 7 —quince clips— es la señal de que has afinado y no remontado. El montaje de la
Semana 07 tenía dieciocho o más; quitar dos o tres planos enteros es afinar, quitar ocho es otra
cosa.

El check 9 mira **la primera pista de vídeo y la primera de audio**. Si tus split edits los hiciste
sobre `Ambiente` o sobre una pista de vídeo de arriba, no los ve, aunque estén bien hechos.

---

## 📝 El entregable escrito

### `notas-de-montaje.md`, apartado `## Trimming — Semana 09`

En `BC-Resolve/04-respaldos/`, en el mismo archivo de las Semanas 06, 07 y 08.

Se abre en la práctica 01 y se cierra en la práctica 04. Al final tiene que llevar seis bloques:

> **Las cifras de partida**: duración de `BC-Montaje-v2`, marcadores puestos y cuántos de cada
> color.
>
> **Las cifras de llegada**: duración de `BC-Montaje-v3`, segundos quitados y en qué porcentaje,
> planos borrados enteros, cortes afinados con ripple y con roll.
>
> **El corte que más ha mejorado**: cuál es, con qué operación, y por qué esa y no otra.
>
> **Teclado frente a dynamic trim**: qué tres cortes afinaste con cada técnica, en cuál tardaste
> menos y en cuál quedó mejor el corte.
>
> **Los split edits**: dónde están, si son en L o en J, y cuántos fotogramas separaste en cada uno.
>
> **Qué pasa a la Semana 10**: lo que queda sin afinar y por qué lo dejaste, con el minuto
> aproximado de cada cosa.

Los dos que más valen son el cuarto y el sexto. El de teclado frente a dinámico porque decide cómo
vas a trabajar las veintisiete semanas que quedan; el de la Semana 10 porque los marcadores que
dejes en 🔵 azul con nota son literalmente el plan de la semana que viene.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| La pieza se sigue sin esfuerzo | Se reproduce entera: no hay ningún momento en que te distraigas |
| Ningún plano se hace largo | Se reproduce: no hay ningún sitio donde esperes al corte siguiente |
| Los cortes de acción continúan el movimiento | Se miran esos cortes a cámara lenta con `K`+`L` |
| Los split edits suenan intencionados | Se escuchan: parecen naturales, no un error de sincronía |
| Ninguna voz va desincronizada con su imagen | Se reproduce con auriculares mirando los labios |
| Los recursos siguen tapando lo que tapaban | Los ripples no descolocaron nada de las pistas de encima |
| El sonido de ambiente sigue bajo su imagen | Se desactiva `Ambiente`: la voz sigue entera |
| No hay parpadeos a negro | Se reproduce entera |
| Los marcadores que quedan describen trabajo real | Se lee uno al azar: se entiende qué hay que hacer |
| Ninguna pista quedó apagada, en solo o sin `Sync Lock` | Se miran las cinco cabeceras |
| No estás en `Dynamic Trim Mode` | El cabezal no está amarillo |
| Nada de lo que todavía no toca | Ni música, ni títulos diseñados, ni color, ni estabilización |

El último sigue siendo el que más gente incumple. La tentación concreta de esta semana es
estabilizar un plano que se ve movido o ralentizar uno que va deprisa. Las dos cosas son la
Semana 10, y las dos rehacen el trabajo de esta si se hacen ahora.

---

## 💡 Adaptación a tu pieza

**Documental corto** · Tu semana es de **ripple y de cortes en L**. Las entrevistas siempre traen
diez o quince segundos de más repartidos en frases que empiezan tarde. Y el corte en L —la voz que
sigue sonando sobre el plano de recurso— es *el* recurso del documental: es lo que hace que un
recurso ilustre en vez de interrumpir.

**Videoclip** · Tu semana es de **roll**. La duración total está atada a la música y no se puede
tocar, así que casi todo lo que vas a hacer es mover cortes sin cambiar la duración. Y `Slip`, para
que el fotograma que cae en el golpe sea el que quieres. El `Ripple` úsalo poco y con el `Sync
Lock` de la música apagado.

**Cortometraje de ficción** · Tu semana es de **split edits y dynamic trim**. El diálogo es donde
más se nota un corte plano: cuánto silencio dejar antes de que el otro conteste no se cuenta en
fotogramas, se oye. Y los cortes en J antes de una réplica son lo que hace que una escena suene a
conversación.

**Tutorial o vídeo formativo** · Tu semana es de **ripple, sin piedad**. En material explicativo,
todo lo que sobra estorba: las dudas, las repeticiones, los silencios largos. Quita primero y
afina después. `Trim End` te va a servir para que los insertos de detalle acaben a la vez que lo
que explican.

**Pieza de viaje** · Tu semana es de **slip**. Tienes muchos planos bonitos colocados donde tocaba
pero enseñando el segundo equivocado: la ola rompe medio segundo después de donde acaba el plano,
el pájaro sale de cuadro justo antes de que entres. `Slip` arregla eso sin tocar nada más.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 09` en verde, diez de diez
2. `BC-Montaje-v3` afinada, sin huecos, con quince clips o más en la pista principal
3. `BC-Montaje-v2` intacta
4. Dos split edits o más en la primera pista de audio
5. Ocho marcadores o más, todos con nombre propio y con su color
6. `notas-de-montaje.md` con el apartado `## Trimming — Semana 09` cerrado, con sus seis bloques
7. `Linked Selection` y `Snapping` activados, y fuera del `Dynamic Trim Mode`
8. Respaldo de la semana: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana09.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza las prácticas 01 y 02. La 01 porque sin la lista de marcadores
> el resto de la semana es dar palos de ciego, y la 02 porque el ripple y el roll son el 80 % del
> trabajo real. Los split edits de la práctica 04 se pueden hacer en veinte minutos otro día; la
> pasada de visionado de la práctica 01, no, porque a la segunda vuelta ya no ves la pieza con
> ojos limpios.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Afinar encima de `BC-Montaje-v2` | Parece más práctico | Se duplica; la comparación necesita las dos |
| Saltarse la pasada de visionado | Se quiere empezar a arreglar ya | Sin la lista, arreglas lo primero que ves y olvidas el resto |
| Borrar planos con `Supr` en vez de `Forward Delete` | Es la tecla de siempre | Deja huecos que el verificador encuentra y tú no |
| Afinar solo con el ratón | Es lo cómodo el primer cuarto de hora | A los veinte cortes el teclado ya va más rápido |
| Quedarse en `Dynamic Trim Mode` | El cabezal amarillo no se mira | `W`; si no, JKL sigue trimando solo |
| Apagar `Linked Selection` desde la barra | Parece más cómodo que `Alt` / `Opt` + clic | El desfase de sincronía no se ve, se oye, y tarde |
| Ripplear sin mirar las pistas de encima | El ripple es la operación que descoloca | Mira el punto del ripple en todas las pistas |
| Hacer split edits en todos los cortes | Se le coge el gusto | Dos como mínimo, cinco o seis como máximo razonable |
| Dejar marcadores con su `Marker N` de fábrica | Se ponen deprisa y no se vuelve | El `Marker Index` los enseña juntos si ordenas por `Name` |
| Empezar a estabilizar o a retimar | «Ya que estoy» | Es la Semana 10, y rehace este trabajo |
| Verificar con `BC-Montaje-v2` abierta | Es la última que tocaste al comparar | Doble clic en `BC-Montaje-v3` |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 08](../../week-08-edit_page_anatomia_y_edicion_basica/3-proyecto/README.md) | **Proyecto Semana 09** | [Semana 10](../../week-10-velocidad_transformaciones_y_estabilizacion/README.md) |

← [Volver a la Semana 09](../README.md)
