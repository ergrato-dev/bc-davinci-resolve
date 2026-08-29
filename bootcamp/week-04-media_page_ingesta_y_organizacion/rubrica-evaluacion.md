# 📊 Rúbrica de evaluación — Semana 04

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 %
en la tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 04` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Explica qué hace Resolve exactamente cuando importas un clip, y deduce de ahí por qué
   importar 200 archivos es instantáneo y por qué mover la carpeta de material los deja
   *offline*.
2. Diferencia el panel Media Storage del media pool. ¿Qué pasa si borras algo en cada
   uno?
3. ¿Qué es una huella y qué detecta que el tamaño y la fecha no detectan? Describe un
   caso concreto en el que un archivo llegue mal sin dar ningún error.
4. Nombra los cinco pasos de la ingesta en orden. ¿Cuáles son irreversibles y por qué?
5. ¿Qué es el bin activo y qué tres operaciones distintas dependen de él?
6. Diferencia bin, smart bin y power bin: quién los llena, cuál es su alcance y qué pasa
   al borrar cada uno.
7. Un smart bin sale vacío. Nombra las tres causas posibles, en orden de frecuencia, y
   di cómo se descarta cada una.
8. Diferencia `Description` de `Keywords`. ¿Por qué meterlo todo en la primera hace que
   los smart bins no funcionen?
9. ¿Qué pregunta responde una keyword, cuál un flag y cuál un clip color? Clasifica
   estos cuatro casos: "este clip es material propio", "este plano es de noche", "a este
   le falta arreglar el audio", "este es un descarte".
10. Explica cómo detecta un corte Scene Cut Detection, y deduce de ese mecanismo sus dos
    fallos característicos. ¿Qué llega al media pool al aceptar?

<details>
<summary>📝 Respuestas</summary>

**1.** Importar escribe una **referencia**: la ruta del archivo en el disco, más lo que
Resolve ha leído de él (duración, codec, resolución, frame rate). **No copia ni un byte
de vídeo.**

De ahí las dos consecuencias: es instantáneo porque no se mueven datos, y mover o
renombrar la carpeta rompe la ruta, con lo que el clip queda *offline*. No se pierde
trabajo —cortes, grados y metadata siguen ahí—, se ha roto un enlace.

**2.** **Media Storage** muestra **tu disco**; el **media pool** muestra **tu proyecto**.

Borrar en Media Storage borra el archivo del disco. Quitar un clip del media pool borra
solo la referencia: el archivo se queda, pero **se pierde todo lo que hubieras escrito
encima** —keywords, descripción, color, flags, grados—, y eso no vuelve al reimportar.

**3.** Una **huella** es un número calculado a partir de **todos los bytes** del archivo.
El mismo archivo da siempre la misma huella y un solo bit distinto la cambia entera.

El tamaño detecta una copia truncada; la fecha, una sustitución evidente. Ninguno de los
dos detecta un cambio **interno**. Caso concreto: un sector del disco falla durante la
copia, el archivo llega con el tamaño y la fecha correctos, se abre, se reproduce, y
tiene un trozo destrozado en el minuto tres. Eso es la **corrupción silenciosa**.

**4.** Copiar → comprobar → importar → organizar → describir.

Los irreversibles son los dos primeros, y por un motivo externo a Resolve: una vez
formateada la tarjeta, lo que no se copió bien no vuelve. Los pasos 4 y 5 se pueden
rehacer siempre, aunque cuesten diez veces más con el proyecto avanzado.

**5.** El **bin activo** es el bin seleccionado en la lista del media pool. De él
dependen: dónde caen los clips que **importas**, dónde caen los que **arrastras** desde
Media Storage, y dónde caen los **subclips** que genera Scene Cut Detection.

**6.**

| | Bin | Smart Bin | Power Bin |
| --- | --- | --------- | --------- |
| Quién lo llena | Tú, arrastrando | Una regla | Tú, arrastrando |
| Alcance | Este proyecto | Este proyecto | **La biblioteca entera** |
| Al borrarlo | Se van las referencias que contiene | No pasa nada: solo se borra la regla | Se borra para todos los proyectos a la vez |

Ninguno de los tres copia archivos: los tres guardan referencias.

**7.** En orden de frecuencia:

1. **La metadata no está escrita.** Se descarta mirando la columna `Keywords` de dos o
   tres clips que deberían salir.
2. **Variantes de la palabra**: `Noche`, `nocturno`, `de noche`. Se descarta comparando
   lo escrito con el vocabulario cerrado.
3. **La condición es más estricta de lo que creías**: dos reglas combinadas con "todas"
   en vez de "cualquiera". Se descarta relajando la regla y viendo si aparece algo.

**8.** `Description` es **prosa**: se lee, sirve para acordarte. `Keywords` son
**etiquetas**: se buscan, se filtran y alimentan los smart bins.

Meterlo todo en `Description` rompe los smart bins porque una regla sobre `Keywords` no
encuentra nada si el campo está vacío, y filtrar prosa devuelve resultados imprecisos:
"noche" dentro de "no era de noche" también coincide.

**9.** Keyword: **¿de qué es este plano?** — permanente. Flag: **¿qué me falta por
hacer?** — temporal. Clip color: **¿qué clase de plano es?** — clasificación visible de
un vistazo.

| Caso | Capa |
| ---- | ---- |
| Material propio | **Clip color** (azul) |
| Plano de noche | **Keyword** (`noche`) |
| Falta arreglar el audio | **Flag**, con el detalle en `Comments` |
| Descarte | **Clip color** (rojo) y bin `10-Descartes` |

**10.** Compara **cada fotograma con el anterior** y marca un corte donde la diferencia
se dispara por encima de un umbral.

Sus dos fallos salen directamente de ahí: **se le escapan los fundidos encadenados**,
porque la imagen cambia poco a poco y nunca hay un salto grande; y **se cree cortes los
flashes**, porque un relámpago sí produce un salto enorme entre dos fotogramas
consecutivos. Por eso la lista se revisa siempre antes de aceptar.

Lo que llega al media pool son **subclips**: referencias al mismo archivo, cada una con
su punto de entrada y de salida. No se crea ni un archivo nuevo en el disco.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **14,29 puntos**.

```bash
python scripts/verificar-semana.py 04
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 02 | `proyecto-abierto` | 14,29 |
| 02 | `frame-rate-bloqueado` | 14,29 |
| 02 | `bin-basicos` | 14,29 |
| 02 | `bin-entrevista` | 14,29 |
| 02 | `bin-propio` | 14,29 |
| 02 | `master-limpio` | 14,29 |
| 04 | `bin-escenas` | 14,29 |

**Necesitas 70 / 100**, es decir **al menos 5 de los 7 checks**.

> [!TIP]
> Si falla **un solo check de bin**, la causa es casi siempre el nombre: una tilde en
> `01-Basicos`, una minúscula en `08-Propio`, o el bin creado dentro de otro en vez de
> colgando de `Master`. El verificador no distingue "bin vacío" de "bin que no existe":
> comprueba las dos cosas.
>
> Si fallan **todos**, no es el trabajo: o el puente no está lanzado, o el proyecto
> abierto no es `BC-Bootcamp-Resolve`.

---

## 📦 Producto (30 %)

Tu material ingestado, organizado y descrito. Se evalúa con criterios observables.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| `vocabulario-keywords.md` existe en `04-respaldos/` | 5 |
| Tiene 15 palabras o menos, y todas en minúsculas, sin acentos y en singular | 10 |
| Incluye el código de colores, con un significado por color | 5 |
| `notas-de-ingesta.md` existe y responde a las cuatro preguntas del pase | 10 |
| Los diez bins existen, con el nombre exacto y colgando de `Master` | 5 |
| Los tres smart bins existen: `SB-Noche`, `SB-Revisar`, `SB-Sin-describir` | 5 |
| El power bin `BC-Recursos` existe y se ve desde otro proyecto | 5 |
| `BC-Bootcamp-Resolve-semana04.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| La mayoría de los clips tiene **dos o más** keywords, no solo la común de la tanda | 10 |
| Todas las keywords escritas salen del vocabulario: ninguna palabra suelta | 10 |
| `Description` está solo en los clips que la necesitan, no en todos | 5 |
| Las marcas de color son excepciones: menos de la mitad del bin las tiene | 5 |
| `SB-Noche` devuelve clips de **más de un bin** | 5 |
| `SB-Sin-describir` está casi vacío | 5 |
| `notas-de-ingesta.md` nombra clips concretos, no "algunos" | 5 |
| El material propio tiene una segunda copia en otro soporte | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| Media pool en vista de lista, columna `Keywords` | Ningún clip de `01-Basicos` ni de `08-Propio` la tiene vacía |
| Media pool en vista de miniaturas | Se distingue de un vistazo tu material del material del pack |
| `SB-Noche` abierto, y después `01-Basicos` | Los clips aparecen en el smart bin **y siguen en su bin original** |
| `09-Escenas` en vista de lista, columna `File Path` | Todos los subclips comparten la misma ruta, con duraciones distintas |
| Tamaño de `08-material-montado/` en el explorador | No ha cambiado después de la detección de escenas |
| `Preferences > System > Media Storage` | `BC-Resolve/` sigue siendo la primera entrada |
| El buscador del media pool | Vacío |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| Material con copyright en el proyecto | −30 |
| El material propio no tiene segunda copia | −15 |
| El pack no está sellado con `MANIFIESTO.sha256` | −10 |
| Las keywords se improvisaron: hay variantes de la misma palabra | −15 |
| El vocabulario se escribió **después** de etiquetar | −10 |
| Colores puestos sin un código escrito | −10 |
| Más de la mitad del media pool con la misma marca de color | −5 |
| Los cortes de la detección se aceptaron sin revisar | −10 |
| Hay clips sueltos en `Master` | −5 |
| Se borraron clips del media pool en vez de moverlos a `10-Descartes` | −5 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

No pases a la Semana 05 sin haber cerrado esta. La 05 genera proxies y medios
optimizados **a partir de los bins que has creado**, y trabaja sobre la lista de
material problemático que has escrito en `notas-de-ingesta.md`. Sin eso, la 05 no tiene
de dónde partir.

- **Si falla un check de bin**: es el nombre, casi seguro. Compara carácter a carácter
  con `checks.json`, y comprueba que el bin cuelga de `Master`.
- **Si fallan todos**: puente sin lanzar, o proyecto equivocado abierto. No repases
  siete cosas: repasa una.
- **Si el cuestionario va por debajo de 70**: las preguntas 7, 8 y 10 son las que más
  gente falla. Vuelve a las teorías 05, 06 y 09.
- **Si el producto va por debajo de 70**: casi siempre es la metadata hecha a medias.
  Un vocabulario escrito después de etiquetar no es un vocabulario, es una lista de lo
  que ya habías improvisado. Reescríbelo y repasa las keywords con selecciones grandes;
  son quince minutos.
- **Si te faltó tiempo**: prioriza el paso 4 de la práctica 01, la copia del material
  propio. Es lo único de la semana que no se puede rehacer más tarde.

---

← [Volver a la Semana 04](README.md)
