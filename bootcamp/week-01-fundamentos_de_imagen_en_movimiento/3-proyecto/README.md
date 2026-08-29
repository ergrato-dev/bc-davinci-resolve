# Proyecto — Semana 01: elegir tu pieza y fundar el proyecto

> Al terminar esta semana tendrás decidido qué vas a hacer durante nueve meses, y el
> proyecto de Resolve donde lo vas a hacer, configurado con criterio.

## 📦 Qué añade esta semana

La capa cero: **la decisión**.

Todo lo que hagas de aquí a la Semana 36 se aplica sobre una misma pieza. Esta semana la
eliges, justificas sus parámetros técnicos y creas el contenedor donde vivirá.

Va aquí y no después porque el frame rate es irreversible: en cuanto entre el primer
clip en el media pool, la cadencia queda fijada para siempre. Elegirla con criterio en
la semana uno es la única oportunidad que hay.

Lee [`docs/proyecto-hilo-conductor.md`](../../../docs/proyecto-hilo-conductor.md) antes
de decidir nada.

---

## 📋 Requisitos verificables

Estos son los mismos que declara `checks.json`. Los nombres son literales: el
verificador los busca carácter a carácter.

1. Existe el proyecto **`BC-Bootcamp-Resolve`**
2. Ese proyecto está **abierto** cuando ejecutas el verificador
3. `Timeline frame rate` = **24**
4. `Timeline resolution` = **1920 × 1080**
5. `Color science` = **DaVinci YRGB**
6. Existe la timeline **`BC-Montaje-v1`**
7. `BC-Montaje-v1` es la timeline **activa**
8. `BC-Montaje-v1` va a **24 fps**

```bash
python scripts/verificar-semana.py 01
```

---

## 📝 El entregable escrito

Además del proyecto en Resolve, esta semana entrega **un documento de una página**.
Guárdalo como `BC-Resolve/04-respaldos/ficha-de-proyecto.md`. Contiene:

### 1. Qué vas a hacer

- **Formato**: documental corto, videoclip, ficción, tutorial o pieza de viaje
- **Tema**: una frase. "Un día en el taller de mi tío", no "algo sobre oficios"
- **Duración objetivo**: entre 3 y 12 minutos
- **Quién habla**: tiene que haber al menos una persona hablando. Di quién

### 2. Por qué esos parámetros

Una frase justificando cada uno. No vale "porque lo dice el bootcamp":

- **24 fps** — por qué esa cadencia y no 25, 30 o 60, para **tu** pieza
- **1920 × 1080** — qué ganas y qué pierdes frente a UHD
- **16:9** — o por qué tu pieza pide otro aspect ratio, y qué harías al respecto
- **Dónde se va a ver** — YouTube, redes, proyección, portfolio. Determina la Semana 29

### 3. Qué vas a grabar

Una lista de 8 a 12 planos que necesitas. No un guion: una lista de la compra. Es lo
que grabarás antes de la Semana 04, cuando toque ingestar.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver, evaluado con criterios observables:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| El formato es realista para una persona sola | ¿Necesitas actores, permisos o equipo que no tienes? Si sí, no es realista |
| La duración objetivo está entre 3 y 12 minutos | Está escrita en la ficha |
| Hay al menos una persona hablando | Está identificada en la ficha |
| La justificación del frame rate menciona el aspecto o el destino, no solo "es el estándar" | Se lee en la ficha |
| La justificación de la resolución menciona el reencuadre o el rendimiento | Se lee en la ficha |
| La lista de planos tiene entre 8 y 12 entradas concretas | Se cuentan |
| Existe el respaldo `.drp` de la semana | El archivo está en `04-respaldos/` |

---

## 💡 Adaptación a tu pieza

Cómo se concreta esta semana según lo que hayas elegido:

**Documental corto** · Tu lista de planos incluye la entrevista, planos de recurso del
lugar y detalles. Justifica 24 fps: te dará aspecto narrativo y te obliga a mover la
cámara despacio, que es justo lo que un documental necesita.

**Videoclip** · Necesitas la canción **antes** de grabar nada, y con licencia. Anótalo
como primer plano de la lista. Si vas a hacer cámara lenta, ese es el único caso en que
plantearte grabar a 48 o 60 fps y entregar a 24; déjalo escrito en la ficha.

**Cortometraje de ficción** · La lista de planos es un desglose de una escena, no de la
película entera. Empieza por una sola escena de dos o tres minutos con dos personajes.

**Tutorial o vídeo formativo** · Tu pieza tendrá multicámara (cámara + captura de
pantalla) y gráficos. Si vas a capturar pantalla, comprueba a qué cadencia graba tu
software: si es 60 fps, apúntalo, porque conformarlo a 24 es trabajo de la Semana 10.

**Pieza de viaje** · El riesgo es acumular material sin criterio. Tu lista de 8-12 planos
es justamente la disciplina que lo evita: grábalos, y solo después lo que surja.

---

## 🚦 Cómo entregarlo

1. Proyecto `BC-Bootcamp-Resolve` creado y configurado
2. Timeline `BC-Montaje-v1` creada y activa
3. `python scripts/verificar-semana.py 01` en verde, ocho de ocho
4. `ficha-de-proyecto.md` escrita en `04-respaldos/`
5. Respaldo del proyecto: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana01.drp`

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Elegir una pieza demasiado ambiciosa | Suena mejor por escrito que un documental de cinco minutos | Reduce el alcance ahora. Nueve meses son largos y la ambición se paga en la semana 12 |
| Elegir algo sin nadie hablando | Parece más fácil de grabar | Te quedas sin la mitad de la Fase 4. Añade aunque sea una locución en off |
| Justificar los parámetros con "porque lo dice el bootcamp" | Es el camino corto | El objetivo del entregable escrito es que puedas defender la decisión sin el bootcamp delante |
| Configurar el proyecto después de importar algún clip de prueba | La tentación de "probar" el programa | El frame rate se bloquea con el primer clip. Crea otro proyecto y configúralo antes de importar |
| No hacer el respaldo `.drp` | Parece innecesario en la semana uno | Es el hábito que te salva en la semana veinte. Diez segundos |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **Proyecto Semana 01** | [Semana 02](../../week-02-codecs_contenedores_y_flujo_de_datos/README.md) |

← [Volver a la Semana 01](../README.md)
