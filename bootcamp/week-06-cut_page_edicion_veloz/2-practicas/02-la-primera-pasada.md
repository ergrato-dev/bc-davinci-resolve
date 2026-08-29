# Práctica 02 — La primera pasada

> Al terminar tendrás tu pieza montada de principio a fin. Fea, larga y con planos que
> vas a cambiar, pero **entera**. Es el entregable más importante de la Fase 2 y el que
> desbloquea las once semanas siguientes.

**Duración estimada**: 55 min
**Prerrequisitos**: [Práctica 01](01-anatomia-de-la-cut-page.md), [Teoría 05](../1-teoria/05-el-indicador-inteligente.md), [Teoría 06](../1-teoria/06-append-la-primera-pasada.md)

## Contexto

Una sola herramienta: **Append**. Nada de recortar fino, nada de transiciones, nada de
música. El objetivo es llegar al final.

> [!IMPORTANT]
> Esta práctica tiene una regla que hay que aceptar antes de empezar: **no se para a
> arreglar**. Si algo no encaja, lo apuntas y sigues. La pieza completa vale más que
> cualquier corte perfecto, y todo lo que hoy quede mal se arregla en la práctica 03 o en
> la Semana 09.

---

## Paso 0: Escribir la estructura, en tres líneas

**Por qué**: montar sin saber a dónde vas produce piezas que no terminan. Tres líneas
bastan y se escriben en dos minutos.

En tu archivo de notas, escribe:

> **Apertura**: con qué empieza y qué tiene que quedar claro ahí.
>
> **Desarrollo**: qué se cuenta o se enseña, en qué orden aproximado.
>
> **Cierre**: cómo termina.

**Verifica**: sabes decir en voz alta cómo acaba tu pieza. Si no lo sabes, decídelo ahora:
saber el final es lo que ordena el desarrollo.

---

## Paso 1: Preparar el sitio de trabajo

**Por qué**: el ciclo de montaje de esta práctica no sale del visor. Todo lo que tengas
que ir a buscar fuera te cuesta el ritmo.

1. `BC-Montaje-v1` abierta y vacía
2. Selecciona el bin con el material del principio de tu pieza
3. Activa **`Source Tape`** en el visor
4. Comprueba que el imán está activado (`N`)

**Verifica**: reproduces la cinta y el material pasa seguido.

---

## Paso 2: El primer plano de la pieza

**Por qué**: el ciclo completo, una vez, despacio. Las siguientes cuarenta veces será
automático.

1. Recorre la cinta hasta el plano con el que quieres abrir
2. **Un segundo antes** de donde quieres que empiece: `I`
3. **Un segundo después** de donde quieres que acabe: `O`
4. Pulsa **Append**

**Verifica**: el clip aparece en `BC-Montaje-v1`, al principio, con vídeo y audio
vinculados en sus pistas.

> [!NOTE]
> Si no marcas `I` ni `O`, entra el clip entero. En bruto es aceptable con clips cortos, y
> mala idea con un clip de cuatro minutos.

---

## Paso 3: La apertura

**Por qué**: los primeros veinte segundos son los que deciden si alguien sigue mirando, y
son los que más veces vas a rehacer. Hoy basta con que existan.

Repite el ciclo del paso 2 hasta tener la apertura montada: entre el 10 % y el 20 % de la
duración prevista de tu pieza.

**Verifica**: reproduces desde el principio y la apertura sitúa: se entiende dónde
estamos, quién habla o de qué va la cosa.

---

## Paso 4: El desarrollo

**Por qué**: es el 60-80 % de la pieza y donde se decide si funciona. Y es donde más
tienta pararse a afinar.

Sigue con el mismo ciclo: recorrer, `I`, `O`, Append. Sin salir del source tape.

Tres recordatorios mientras montas:

- **Marca de sobra.** Recortar en la Semana 09 cuesta un gesto; alargar sin material, no
  se puede.
- **Si dudas entre dos planos**, mete el menos malo y sigue. Se sustituye en diez segundos
  en la práctica 03.
- **Si te falta un plano**, deja un marcador con `M` en ese punto y sigue por el siguiente
  bloque.

**Verifica**: cada pocos clips, mira la **timeline de arriba**. Deberías ver crecer la
pieza y reconocer su forma.

---

## Paso 5: El cierre

**Por qué**: una pieza sin final no está montada, está interrumpida. Y es la parte que se
queda sin hacer cuando se acaba el tiempo.

Monta el cierre que decidiste en el paso 0. Entre el 10 % y el 20 % de la duración.

**Verifica**: la timeline termina donde tú quieres que termine, no donde se te acabó el
material.

---

## Paso 6: Comprobar que la pasada está completa

**Por qué**: es el criterio de terminación de la práctica, y es objetivo.

1. Cabezal al principio
2. Reproduce la timeline **entera**, sin parar y sin tocar nada
3. Al llegar al final, escribe en tus notas: duración total y qué tres cosas te chirrían
   más

**Verifica**:

```bash
python scripts/verificar-semana.py 06 --check montaje-clips
python scripts/verificar-semana.py 06 --check montaje-duracion
```

El primero pide **15 clips o más** en la pista de vídeo principal; el segundo, **120
segundos o más** de duración total. Son mínimos de una primera pasada, no objetivos: tu
pieza casi seguro pide más.

> [!TIP]
> Si te quedas corto de duración, el problema casi nunca es que falte material: es que
> marcaste los planos demasiado justos. Vuelve a la cinta y añade lo que descartaste por
> rapidez, sobre todo planos de sitio y de contexto.

---

## Paso 7: Fast review sobre tu propio montaje

**Por qué**: es la primera vez que ves tu pieza como un conjunto y no como una sucesión de
decisiones. Lo que salta aquí es lo que hay que arreglar en la práctica 03.

1. Cabezal al principio
2. Pulsa **Fast Review**
3. **No pares a arreglar nada.** Apunta y sigue
4. Anota cada cosa que veas con su casilla al lado, como en la teoría 04:

| Lo que anotas | Casilla |
| ------------- | ------- |
| "Falta un plano aquí" / "sobra este" / "este va antes" | **Práctica 03** |
| "El corte cae un poco tarde" | Semana 09 |
| "Aquí hace falta un rótulo" | Semana 11 |
| "Suena bajo" / "se ve oscuro" | Fases 4 y 5 |

**Verifica**: tienes una lista escrita, con al menos tres entradas de la primera casilla.
Esa lista es el guion de la práctica 03.

---

## Paso 8: Guardar y anotar

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)
2. En `BC-Resolve/04-respaldos/`, crea **`notas-de-montaje.md`** y escribe:

> **Estructura**: las tres líneas del paso 0.
>
> **Duración de la primera pasada**: en minutos y segundos.
>
> **Número de clips**: el que diga la timeline.
>
> **Lo que hay que arreglar**: la lista del paso 7, con su casilla.
>
> **Lo que falta grabar**: si algo no lo tienes y todavía puedes conseguirlo.

**Verifica**: el archivo existe y las cinco líneas tienen contenido, no adjetivos.

---

## ✅ Resultado

- [ ] La estructura escrita en tres líneas antes de montar
- [ ] `BC-Montaje-v1` va de principio a fin
- [ ] 15 clips o más en la pista de vídeo principal
- [ ] 120 segundos o más de duración
- [ ] Montado con Append, desde el source tape
- [ ] Ningún plano recortado al fotograma: todo marcado con margen
- [ ] Ni transiciones, ni títulos, ni música
- [ ] Fast review hecho, con la lista escrita
- [ ] `notas-de-montaje.md` con sus cinco líneas

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `montaje-clips` falla | Menos de 15 clips en `Video 1` | Sigue montando: la pasada no está completa |
| `montaje-duracion` falla | Marcaste los planos demasiado justos | Añade material de contexto y alarga los que se quedaron cortos |
| `montaje-activo` falla | Tienes abierta otra timeline | Doble clic en `BC-Montaje-v1` y repite |
| El clip entra entero y no el tramo | No había `I` y `O` marcados | Márcalos en el visor antes de Append |
| El audio no entra con el vídeo | El clip no tiene audio, o la pista está bloqueada | Comprueba la cabecera de la pista de audio |
| Los clips caen en medio y no al final | No usaste Append | Append ignora el cabezal: comprueba qué botón pulsas |
| Llevas una hora y vas por la mitad | Estás afinando en vez de montando | Marca de sobra, no recortes, y sigue |
| La pieza no llega al final | Te paraste a arreglar | Apunta y sigue. La lista es para la práctica 03 |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · Anatomía de la Cut page](01-anatomia-de-la-cut-page.md) | **02 · La primera pasada** | [03 · Corregir el montaje](03-corregir-el-montaje.md) |

← [Volver a la Semana 06](../README.md)
