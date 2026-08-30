# 🌐 Webgrafía — Semana 10

> Documentación oficial primero, foro después, y la documentación transversal del propio bootcamp
> al final. Cada entrada dice **por qué** vale la pena.

---

## Documentación oficial

### Blackmagic Design — soporte y manuales

<https://www.blackmagicdesign.com/support/>

**Por qué vale la pena**: es donde vive el Reference Manual, del que salen los capítulos 57, 58 y
60 de esta semana. La particularidad de la semana es que **casi todo son nombres de controles y
valores por defecto**, y un nombre mal citado manda a buscar un ajuste que no existe.

### Comparativa oficial DaVinci Resolve Free / Studio

<https://www.blackmagicdesign.com/products/davinciresolve/studio>

**Por qué vale la pena**: esta semana toca dos funciones que están al otro lado de la línea
—`Speed Warp` y `Lens Correction`— y una tercera cuya alternativa en Free es el ejercicio de
keyframes de la práctica 04: `Smart Reframe`. Esta página es la **fuente de verdad** sobre qué
está en cada versión, y se actualiza con cada release. Cualquier tabla de terceros, la del
bootcamp incluida, va por detrás.

### Foro oficial de DaVinci Resolve

<https://forum.blackmagicdesign.com/>

**Por qué vale la pena**: los problemas de esta semana son de comportamiento y de percepción, no
de fallo. «Por qué mi cámara lenta va a saltos», «por qué el audio se me ha quedado mudo», «por
qué el estabilizador me deforma la imagen»: los tres están preguntados y contestados por gente con
tu misma versión, y los tres tienen una explicación que no es un error del programa.

**Cómo buscar**: por el nombre inglés del control y tu versión. `optical flow artifacts 21` da
mejores resultados que una descripción del síntoma en castellano.

---

## Referencia técnica

### ITU-R BT.709 · Recomendación de vídeo HDTV

<https://www.itu.int/rec/R-REC-BT/en>

**Por qué vale la pena**: es la recomendación donde están normalizadas las cadencias de vídeo de
las que sale el techo de cámara lenta de la teoría 01. No hace falta leerla entera —es una norma,
no un manual—, pero sí saber que las cadencias no son una convención del software: están escritas
en un estándar internacional.

---

## Documentación del bootcamp

### `docs/free-vs-studio.md`

[../../../../docs/free-vs-studio.md](../../../../docs/free-vs-studio.md)

**Por qué vale la pena**: la tabla del bootcamp con las funciones de Studio y su alternativa en
Free. Las tres entradas que tocan esta semana son `Speed Warp`, `Smart Reframe` y la corrección de
lente. Recuerda que la fuente de verdad es la comparativa oficial de arriba.

### `docs/atajos-de-teclado.md`

[../../../../docs/atajos-de-teclado.md](../../../../docs/atajos-de-teclado.md)

**Por qué vale la pena**: esta semana añade pocos atajos pero los tres que añade se usan a diario:
`Ctrl+R` / `Cmd+R` para los `Retime Controls`, `Shift+R` para el freeze y `Shift+F11` para el
`Fit to Fill`. El documento explica además cómo comprobarlos en tu instalación, que es lo que
manda: `Keyboard Customization`.

### `docs/trucos-resolve.md`

[../../../../docs/trucos-resolve.md](../../../../docs/trucos-resolve.md)

**Por qué vale la pena**: los trucos de las diez semanas publicadas, agrupados. Los de esta semana
están en su apartado, y los de la Semana 09 —el bucle con `Ctrl+/` y `/`— se usan aquí todo el
rato para juzgar un retime sin parar la reproducción.

### `docs/proyecto-hilo-conductor.md`

[../../../../docs/proyecto-hilo-conductor.md](../../../../docs/proyecto-hilo-conductor.md)

**Por qué vale la pena**: la convención de versionado que explica por qué esta semana se duplica a
`BC-Montaje-v4` en vez de trabajar encima, y por qué se exporta un `.drp` al cerrar.

---

## Lo que conviene desconfiar

Buscar «davinci resolve slow motion» en un buscador devuelve, casi entero, contenido que hace lo
mismo: coge un plano a 120 fps, lo pone al 20 %, dice «mira qué bien» y no menciona la cadencia de
rodaje. No es mentira; es que el resultado no es replicable con material normal.

El filtro es siempre el mismo: **si no dice la cadencia de rodaje, no sirve para decidir nada.**

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Videografía](../videografia/README.md) | **Webgrafía Semana 10** | [Glosario](../../5-glosario/README.md) |

← [Volver a la Semana 10](../../README.md)
