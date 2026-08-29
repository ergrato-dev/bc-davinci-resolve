# 📊 Rúbrica de evaluación — Semana 01

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 %
en la tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 01` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. ¿Qué es un frame y por qué es la unidad mínima de todo lo que harás en Resolve?
2. ¿Por qué percibimos movimiento al ver imágenes fijas sucesivas? ¿Basta con la
   persistencia de la visión para explicarlo?
3. ¿De dónde salen los frame rates de 23.976 y 29.97? ¿Qué fracción los produce?
4. ¿Cuál es el único ajuste de proyecto de esta semana que **no** se puede cambiar
   después, y qué lo bloquea?
5. Calcula la velocidad de obturación a 180° para 25 fps y para 60 fps.
6. ¿Cuántos píxeles de ancho separan UHD de 4K DCI, y cuál de los dos es lo que la gente
   suele llamar "4K"?
7. ¿Por qué reducir de 4K a 1080 mejora la imagen y ampliar de 1080 a 4K no?
8. ¿Cuántos frames son `00:01:30:12` a 24 fps? ¿Y cuántos segundos?
9. ¿Qué hace exactamente el drop frame? ¿Se pierden imágenes?
10. ¿Cuál es la regla para saber si un ajuste está en Preferences o en Project Settings?

<details>
<summary>📝 Respuestas</summary>

**1.** Un frame es cada una de las imágenes fijas que componen un vídeo. Es la unidad
mínima porque no se puede cortar, medir ni direccionar nada más pequeño: un corte ocurre
**entre** dos frames, nunca dentro de uno, y la precisión máxima de cualquier recorte es
un frame.

**2.** No basta. La persistencia de la visión explica por qué no vemos parpadear la
pantalla, pero no por qué percibimos movimiento. Eso lo hace el **movimiento aparente**
(*beta movement*): el sistema visual interpreta dos estímulos parecidos, próximos en el
tiempo y en posiciones distintas, como un mismo objeto que se ha desplazado. Como es una
interpretación, se puede romper —eso es el judder— y se puede ayudar, con desenfoque de
movimiento.

**3.** De la fracción **1000/1001**. Cuando en 1953 se añadió el color a la televisión
estadounidense en blanco y negro, hubo que bajar la velocidad de cuadro un 0,1 % para
que la portadora de color no interfiriera con el sonido. `30 × 1000/1001 = 29.97` y
`24 × 1000/1001 = 23.976`.

**4.** El **timeline frame rate**. Se bloquea en cuanto hay al menos un clip en el media
pool. A partir de ahí, la única salida es crear un proyecto nuevo.

**5.** A 180°, la velocidad de obturación es `1 / (2 × fps)`.
A 25 fps → **1/50 s**. A 60 fps → **1/120 s** (en el menú de la cámara, normalmente
`1/125`).

**6.** **256 píxeles**: UHD es 3840 × 2160 y 4K DCI es 4096 × 2160. Cuando alguien dice
"4K" a secas casi siempre quiere decir **UHD**, que es lo que usan televisores, YouTube,
móviles y todo lo que no sea una sala de cine.

**7.** Al reducir **sobra** información: cuatro píxeles se promedian para calcular uno, y
eso da un resultado más limpio y nítido que medir ese píxel una sola vez. Es el
sobremuestreo. Al ampliar **falta** información y hay que inventarla: por bueno que sea
el algoritmo, no hay detalle nuevo, solo interpolación.

**8.** `(60 + 30) × 24 + 12 = 2160 + 12 = ` **2172 frames**. Y `2172 ÷ 24 = ` **90,5
segundos**.

**9.** Se salta los **números de frame** `00` y `01` al empezar cada minuto, salvo en los
minutos múltiplos de 10. Son 2 números en 54 de los 60 minutos = 108 por hora, que es
exactamente el desfase entre contar a 30 y reproducir a 29.97. **No se pierde ninguna
imagen**: se saltan etiquetas, no frames.

**10.** Si el ajuste describe **tu ordenador**, está en Preferences (caché, GPU, idioma,
guardado). Si describe **tu vídeo**, está en Project Settings (frame rate, resolución,
ciencia de color). Consecuencia práctica: los Project Settings viajan con el proyecto a
otra máquina; las Preferences no.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale 12,5 puntos.

```bash
python scripts/verificar-semana.py 01
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 02 | `proyecto-existe` | 12,5 |
| 02 | `proyecto-abierto` | 12,5 |
| 02 | `frame-rate` | 12,5 |
| 02 | `resolucion` | 12,5 |
| 02 | `ciencia-de-color` | 12,5 |
| 04 | `timeline-existe` | 12,5 |
| 04 | `timeline-activa` | 12,5 |
| 04 | `timeline-frame-rate` | 12,5 |

**Necesitas 70 / 100**, es decir **al menos 6 de los 8 checks**. Pero `frame-rate` es
eliminatorio: si está mal, arréglalo ahora creando un proyecto nuevo. En la semana 04,
con clips dentro, ya no podrás.

---

## 📦 Producto (30 %)

Tu ficha de proyecto y el respaldo. No lo puede ver el verificador, así que se evalúa
con criterios observables.

### Verificable a simple vista (60 puntos)

| Criterio | Puntos |
| -------- | ------ |
| La ficha existe en `04-respaldos/ficha-de-proyecto.md` | 10 |
| Declara formato, tema en una frase, duración objetivo y quién habla | 15 |
| La duración objetivo está entre 3 y 12 minutos | 5 |
| Hay al menos una persona hablando, identificada | 10 |
| La lista de planos tiene entre 8 y 12 entradas concretas | 10 |
| Existe `BC-Bootcamp-Resolve-semana01.drp` en `04-respaldos/` | 10 |

### Calidad de las decisiones (40 puntos)

| Criterio | Puntos |
| -------- | ------ |
| La justificación de los 24 fps menciona el aspecto buscado o el destino, no solo "es el estándar" | 10 |
| La justificación de la resolución menciona el reencuadre o el rendimiento | 10 |
| El destino de la pieza está declarado (YouTube, redes, proyección, portfolio) | 10 |
| El proyecto es realista para una persona sola: no exige actores, permisos ni equipo que no tengas | 10 |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| La pieza no tiene a nadie hablando | −20 |
| La duración objetivo pasa de 12 minutos | −15 |
| Justificar los parámetros con "porque lo dice el bootcamp" | −10 por parámetro |
| Importar clips antes de configurar el proyecto | −20 (y probablemente tengas que rehacerlo) |
| No hay respaldo `.drp` | −10 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

No pases a la Semana 02 sin haber cerrado esta. En concreto:

- **Si falla `frame-rate`**: es lo único irreversible del bootcamp. Créalo de nuevo hoy.
- **Si fallan los checks de timeline**: repite la práctica 04, paso 4.
- **Si el cuestionario va por debajo de 70**: las preguntas 3, 4, 7 y 9 son las que más
  gente falla. Vuelve a las teorías 02, 04 y 06.
- **Si el producto va por debajo de 70**: casi siempre es la justificación. Escribir "por
  qué" es el 80 % del valor de este entregable.

---

← [Volver a la Semana 01](README.md)
