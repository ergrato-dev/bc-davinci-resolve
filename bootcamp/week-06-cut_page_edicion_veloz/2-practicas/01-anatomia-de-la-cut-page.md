# Práctica 01 — Anatomía de la Cut page

> Al terminar habrás recorrido la página entera, sabrás moverte por una timeline sin tocar
> el zoom, habrás revisado tu material como una cinta y tendrás creada la timeline en la
> que vas a montar las once semanas siguientes.

**Duración estimada**: 45 min
**Prerrequisitos**: [Semana 05](../../week-05-proxies_cache_y_sincronizacion/README.md) cerrada, [Teoría 01](../1-teoria/01-por-que-existe-la-cut-page.md), [Teoría 02](../1-teoria/02-la-timeline-doble.md), [Teoría 03](../1-teoria/03-source-tape.md), [Teoría 04](../1-teoria/04-fast-review.md)

## Contexto

Esta práctica no monta nada definitivo: coloca las piezas. Es corta a propósito, porque el
grueso de la semana está en la práctica 02, y conviene llegar a ella sabiendo dónde está
cada cosa.

---

## Paso 1: Abrir el proyecto y entrar en la página

**Por qué**: todo lo que hagas esta semana va al mismo proyecto de siempre. La Cut page no
es un sitio aparte: es otra vista del proyecto que ya tienes.

1. Abre **`BC-Bootcamp-Resolve`** desde el Project Manager
2. Lanza el puente desde `Workspace > Scripts > Utility`
3. Pulsa `Shift+3` para entrar en la Cut page

**Verifica**:

```bash
python scripts/verificar-semana.py 06 --check proyecto-abierto
```

---

## Paso 2: Reconocer las cuatro zonas

**Por qué**: en las cuatro semanas siguientes vas a dar cientos de instrucciones a esta
página. Perder treinta segundos buscando un control cada vez son horas al mes.

Localiza, sin tocar nada:

1. **El media pool**, arriba a la izquierda, con los bins de la Semana 04
2. **El visor**, arriba a la derecha, con sus controles de transporte
3. **La barra de herramientas**, en el centro, con los seis botones de edición
4. **La timeline doble**, abajo: la completa arriba y el detalle abajo

**Verifica**: puedes señalar las cuatro zonas sin dudar. Si algún panel no está donde
debería, `Workspace > Reset UI Layout` lo devuelve a su sitio sin tocar el proyecto.

---

## Paso 3: Crear la timeline del montaje

**Por qué**: es la timeline de tu pieza durante las once semanas siguientes. El nombre no
es decorativo: los checks lo buscan carácter a carácter, y las Semanas 08 a 12 lo dan por
supuesto.

> [!IMPORTANT]
> Comprueba antes de crearla que el proyecto sigue a **24 fps**. Una timeline hereda el
> frame rate del proyecto en el momento de crearse, y el del proyecto ya no se puede
> cambiar porque hay clips en el media pool desde la Semana 04.

1. `File > New Timeline`
2. Nómbrala exactamente **`BC-Montaje-v1`**
3. Créala **vacía**: sin marcar la opción de usar los clips seleccionados
4. Comprueba en `File > Project Settings > Master Settings` que el
   `Timeline frame rate` es **24**

**Verifica**:

```bash
python scripts/verificar-semana.py 06 --check timeline-montaje-existe
python scripts/verificar-semana.py 06 --check frame-rate-bloqueado
```

---

## Paso 4: Moverte por la timeline doble

**Por qué**: es el gesto que más veces vas a repetir esta semana, y hacerlo con el ratón
cuesta el triple.

Necesitas algo en la timeline para practicar. Mete cinco clips cualesquiera de
`01-Basicos`, arrastrándolos a la timeline; los vas a quitar en el paso siguiente.

1. Clic en distintos puntos de la timeline **de arriba** y mira cómo cambia la de abajo
2. Reproduce con `Espacio`
3. Avanza con `L`, púlsalo tres veces seguidas y observa la aceleración
4. Para con `K`, retrocede con `J`
5. Fíjate en que el cabezal de la timeline de abajo **no se mueve**: se mueve la timeline
6. Comprueba que el imán está activo alternándolo con `N` y dejándolo activado

**Verifica**: puedes ir del principio al final de la timeline y volver sin usar el ratón
más que para el primer clic.

---

## Paso 5: Vaciar la timeline

**Por qué**: los cinco clips del paso anterior eran para practicar el movimiento. El
montaje de verdad empieza en la práctica 02, y empieza desde cero.

1. Selecciona los cinco clips en la timeline
2. Bórralos
3. Comprueba que la timeline queda vacía y que sigue existiendo

**Verifica**: `BC-Montaje-v1` sigue en el media pool, sin clips dentro.

> [!NOTE]
> Borrar los clips de una timeline **no borra nada del media pool ni del disco**. Una
> timeline guarda referencias a los clips, igual que un bin guarda referencias a los
> archivos. Es la misma idea de la Semana 04, un piso más arriba.

---

## Paso 6: Revisar tu material como una cinta

**Por qué**: es la pasada que hace posible montar. Sin ella, montas de memoria.

1. Selecciona el bin **`01-Basicos`** en el media pool
2. Ordénalo por hora de grabación, si tu material la tiene, o por nombre
3. Activa **`Source Tape`** en el visor
4. Recorre la cinta entera con `L`, `K` y `J`
5. Con un archivo de texto abierto al lado, apunta en dos columnas: **minuto** y **qué
   hay**

**Verifica**: has llegado al final de la cinta y tienes la lista escrita. Si tu bin es
largo, veinte minutos de material se recorren en unos cinco con `L` `L`.

> [!TIP]
> Prueba también con un **smart bin** de la Semana 04. La cinta contiene entonces solo el
> material que cumple esa regla, y esa combinación es la forma más rápida que hay en
> Resolve de revisar "todo lo que etiqueté como entrevista".

---

## Paso 7: Los otros modos del visor

**Por qué**: son tres clics que resuelven tres situaciones distintas, y no saber que
existen cuesta tiempo cada semana.

Alterna entre los cuatro modos de origen y comprueba qué hace cada uno:

| Modo | Qué esperas ver |
| ---- | --------------- |
| `Source Clip` | Solo el clip seleccionado |
| `Source Tape` | Todo el bin, seguido |
| `Multi Source` | Varios clips a la vez, en cuadrícula |
| `Recent 5 Mins` | Lo que acabas de mirar |

**Verifica**: sabes decir, para cada uno, en qué situación lo usarías.

---

## Paso 8: Probar Fast Review

**Por qué**: en la práctica 02 vas a revisar tu montaje con esta herramienta, y conviene
haberla visto funcionar antes con material que no te importa.

1. Mete otra vez en la timeline seis o siete clips de duraciones **muy distintas**: uno
   largo, varios cortos
2. Vuelve al principio de la timeline
3. Pulsa **Fast Review** en el transporte del visor
4. Observa que los clips largos pasan deprisa y los cortos casi a velocidad normal
5. Vacía la timeline otra vez al terminar

**Verifica**: has visto los siete clips en mucho menos tiempo del que dura la timeline, y
ninguno se ha saltado.

> [!TIP]
> Si no localizas el control, ábrelo por su nombre: `DaVinci Resolve > Keyboard
> Customization`, busca el comando y comprueba qué atajo tiene en tu instalación.

---

## Paso 9: Dejarlo listo para la práctica 02

1. Comprueba que **`BC-Montaje-v1`** está **abierta** y **vacía**
2. Guarda con `Ctrl+S` (Win) / `Cmd+S` (Mac)

**Verifica**:

```bash
python scripts/verificar-semana.py 06 --check montaje-activo
```

Este check pasa aunque la timeline esté vacía: comprueba que es la timeline abierta, no
lo que contiene.

---

## ✅ Resultado

- [ ] `BC-Bootcamp-Resolve` abierto y el puente lanzado
- [ ] Sé señalar las cuatro zonas de la Cut page
- [ ] `BC-Montaje-v1` creada, a 24 fps, vacía y abierta
- [ ] Me muevo por la timeline doble con `J`, `K`, `L` y clics arriba
- [ ] El imán está activado
- [ ] He revisado `01-Basicos` entero con `Source Tape`
- [ ] Tengo la lista de qué hay y en qué minuto
- [ ] He visto Fast Review funcionar
- [ ] Sé para qué sirve cada uno de los cuatro modos del visor

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `timeline-montaje-existe` falla | El nombre no es exacto | `BC-Montaje-v1`, con guiones y uve minúscula |
| `frame-rate-bloqueado` falla | El proyecto abierto no es el del bootcamp | Ábrelo desde el Project Manager, en tu biblioteca original |
| El source tape muestra un solo clip | El visor está en `Source Clip` | Cambia a `Source Tape` |
| El source tape sale desordenado | El bin no estaba ordenado | Ordena el bin: la cinta hereda su orden |
| El source tape aparece vacío | No hay ningún bin seleccionado | Selecciona un bin en el media pool |
| El cabezal no se mueve al reproducir | Es lo normal en la timeline de detalle | Se mueve la timeline por debajo |
| La reproducción va a saltos | Es el cuello de botella de la Semana 05 | Activa los optimizados o los proxies que generaste |
| No encuentro Fast Review | Está en el transporte del visor | Búscalo por nombre en `Keyboard Customization` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · Anatomía de la Cut page** | [02 · La primera pasada](02-la-primera-pasada.md) |

← [Volver a la Semana 06](../README.md)
