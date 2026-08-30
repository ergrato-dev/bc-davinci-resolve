# 📊 Rúbrica de evaluación — Semana 12

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en la
tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 12` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. ¿Qué es un ISO y qué es un ángulo? ¿Dónde vive un clip multicámara en el disco duro?
2. Grabaste una charla con tres móviles. ¿Qué método de `Angle Sync` eliges y por qué se caen los
   otros tres? ¿Qué habrías hecho en el rodaje para tener las cuatro opciones abiertas?
3. Estás montando con el Multicam Viewer y te das cuenta de que hace veinte segundos cortaste a la
   cámara equivocada. El ritmo está bien. ¿Qué haces exactamente, y qué **no** haces?
4. ¿Por qué en una entrevista se conmuta `Video Only`? ¿Qué se oye si no?
5. ¿Por qué la pista de subtítulos es un tipo de pista propio y no una pista de vídeo? Da dos
   consecuencias prácticas.
6. Tienes dos pistas de subtítulos, `es-ES` y `en-US`, y quieres ver las dos a la vez para
   comprobar la traducción. ¿Se puede? ¿Y si lo que quieres es dos subtítulos simultáneos porque dos
   personajes hablan encima?
7. Has cambiado la fuente en `Inspector > Track` y once subtítulos no han cambiado. ¿Qué ha pasado?
8. Explica las tres opciones del desplegable `Format` de los `Subtitle Settings` de la página
   Deliver. ¿Cuál eliges para YouTube y cuál para una historia de Instagram? ¿Por qué?
9. Vas a mandar tu timeline al estudio que hace la mezcla, que trabaja con Pro Tools. ¿Qué formato
   exportas y por qué ese? ¿Qué le mandas además del archivo?
10. En la ventana de Media Management marcas `Copy and trim used media keeping 12 frame handles` y
    `Relink to new files`. Al día siguiente borras la carpeta original para hacer sitio. ¿Qué pasa
    con tu proyecto y por qué?

<details>
<summary>📝 Respuestas</summary>

**1.** Un **ISO** (*isolated camera*) es cada uno de los **archivos** que grabó una cámara. Un
**ángulo** es ese mismo material **una vez está dentro** del clip multicámara, ya con su número, su
nombre y su desplazamiento de sincronía. Un ISO es un archivo; un ángulo es un papel dentro de un
clip.

Un clip multicámara **no vive en ninguna parte del disco duro**. Es una estructura dentro del
proyecto: una lista de ángulos, cada uno apuntando a su ISO con su desplazamiento en fotogramas. Como
una timeline, o como un compound clip.

**2.** **`Sound`**, que compara la forma de onda del audio de cada ángulo. Solo exige que las tres
cámaras oyeran lo mismo, y un móvil siempre graba audio.

Los otros tres:

- **`Timecode`** se cae porque **un móvil no graba timecode**, y aunque lo hiciera, tres móviles no
  llevan el mismo reloj: haría falta *jam sync*
- **`In or Out`** y **`Marker`** no se caen del todo, pero exigen un **instante reconocible** en los
  tres ángulos, y si no lo preparaste puede que no lo haya

Lo que se hace en el rodaje: **una palmada delante de las tres cámaras, con las tres ya grabando**.
Se ve y se oye, y deja abiertos `Sound`, `In or Out` y `Marker` a la vez.

**3.** **`Alt`+clic sobre el ángulo bueno** en el Multicam Viewer —o clic derecho sobre el clip en la
timeline `>` `Switch Multicam Clip Angle`—. Eso **conmuta**: cambia el ángulo del tramo sin añadir
ningún corte.

Lo que **no** haces es volver a cortar. Un clic normal —o la tecla `1` a `9`— añadiría un corte nuevo
en el cabezal, y el corte que ya tenías estaba bien. El error era de ángulo, no de ritmo.

**4.** Porque **el audio bueno es uno solo**: el de la cámara mejor situada, o el de la grabadora
externa. Con `Video and Audio`, cada cambio de cámara cambia también de micrófono.

Lo que se oye es un **tropiezo en cada corte**: el ambiente, el nivel y el color del sonido saltan de
golpe. Un cambio de imagen es invisible cuando está bien hecho; un cambio de micrófono no lo es
nunca.

**5.** Porque Resolve tiene **tres tipos de pista** —vídeo, audio y subtítulos— y las cuenta por
separado, hasta en la API de scripting.

Dos consecuencias prácticas, de entre varias:

- **Solo una pista de subtítulos puede estar visible a la vez.** Encender una apaga las demás. Con
  pistas de vídeo no pasa: se superponen
- Sus clips **salen del render como texto**, en un archivo aparte o incrustados, y el espectador
  puede apagarlos. Un `Text+` en una pista de vídeo es imagen y no se apaga nunca

**6.** **No se puede** ver las dos pistas a la vez: solo una pista de subtítulos es visible en cada
momento, y encender `en-US` apaga `es-ES`. Para comprobar una traducción hay que ir alternando.

Para dos subtítulos simultáneos **sí hay solución**, y es otra: las **regiones**. Una pista de
subtítulos admite hasta tres —`R1`, `R2` y `R3`—, cada una con su lista, su estilo y su **posición en
pantalla**. Cuando dos regiones se solapan en el tiempo, se ven las dos, y poner una a la izquierda y
otra a la derecha indica quién dice qué.

**7.** Esos once tienen marcada la casilla **`Customize Caption`**. Marcarla saca un subtítulo del
estilo de la pista: a partir de ahí lleva el suyo propio y deja de seguir los cambios globales.

Es lo que hace esa casilla y por eso se usa solo para excepciones de verdad. Para que vuelvan a
seguir a la pista, hay que desmarcarla en cada uno.

**8.**

| Opción | Qué hace |
| ------ | -------- |
| **`As a separate file`** | Un archivo de subtítulos aparte, en IMSC1, DFXP, SRT o WebVTT. La imagen sale limpia |
| **`Burn into video`** | Los subtítulos se renderizan **dentro de la imagen**. Son píxeles |
| **`As embedded captions`** | Van dentro del archivo de vídeo como metadato. CEA-608 en MXF OP1A y en QuickTime |

Para **YouTube**, `As a separate file`: la plataforma ofrece el botón de subtítulos, el espectador
los apaga si quiere, y una errata se corrige subiendo otro archivo sin volver a renderizar.

Para una **historia de Instagram**, `Burn into video`: el vídeo arranca mudo, sin controles y sin
posibilidad de cargar un archivo aparte. Si no están quemados, no existen.

**9.** **AAF**. Es el formato estándar hacia Pro Tools y hacia el resto del mundo Avid, y es lo que
un estudio de sonido espera recibir.

Además del AAF le mandas dos cosas: **los medios de audio** —el intercambio lleva instrucciones, no
imágenes ni sonido— y **un vídeo de referencia**, la pieza renderizada, para que puedan mezclar
viendo lo que ven tus espectadores y comparar contra algo.

**10.** **Tu proyecto se queda offline.**

`Relink to new files` hizo que el proyecto **dejara de apuntar a los archivos originales y pasara a
apuntar a las copias**. Y `trim keeping 12 frame handles` hizo que esas copias contengan solo el
trozo usado más doce fotogramas a cada lado.

Al borrar la carpeta original no has borrado «una copia»: has borrado **lo único que quedaba del
material completo**. Los clips de la timeline siguen enlazados a las copias recortadas —que sí están,
así que la pieza se reproduce—, pero todo el material que sobraba ha desaparecido: no puedes alargar
un plano, ni rehacer una transición, ni recuperar una toma descartada.

Por eso el recorte se hace **cuando el montaje está cerrado**, y por eso los originales se conservan
hasta que la pieza está entregada.

</details>

**Puntuación**: 70 puntos o más para superar esta evidencia.

---

## 💪 Desempeño (40 %)

```bash
python scripts/verificar-semana.py 12
```

| Check | Qué comprueba | Puntos |
| ----- | ------------- | ------ |
| `proyecto-abierto` | `BC-Bootcamp-Resolve` es el proyecto abierto | 10 |
| `montaje-v5-conservada` | La pieza de la Semana 11 sigue intacta | 10 |
| `montaje-v6-activa` | `BC-Montaje-v6` existe y es la timeline abierta | 10 |
| `montaje-v6-clips` | Quince clips o más en la `V1` | 10 |
| `montaje-v6-sin-huecos` | Ni huecos ni solapes en la `V1` | 10 |
| `pista-de-subtitulos` | Una pista de subtítulos con ocho subtítulos o más | 10 |
| `subtitulos-pista-con-nombre` | Esa pista está renombrada, no es `Subtitle 1` | 10 |
| `multicam-v1-existe` | La timeline `BC-Multicam-v1` existe | 10 |
| `intercambio-v1-existe` | La timeline `BC-Intercambio-v1` existe | 10 |
| `bin-de-intercambio` | El bin `14-Intercambio` tiene dos elementos o más | 10 |

**Puntuación**: 70 puntos o más. Siete checks en verde de diez.

> [!TIP]
> Si fallan **cinco a la vez** —`montaje-v6-activa`, `montaje-v6-clips`, `montaje-v6-sin-huecos`,
> `pista-de-subtitulos` y `subtitulos-pista-con-nombre`—, la timeline activa no es la que crees.
> Tres candidatas esta semana: `BC-Multicam-v1`, `BC-Intercambio-v1`, o el interior de un clip
> multicámara abierto con `Open in Timeline`.

---

## 📦 Producto (30 %)

Los criterios observables. Cada uno vale 5 puntos: **cumple**, **cumple a medias** o **no cumple**.

### Multicámara (30 puntos)

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| Los ángulos cuadran al fotograma | Se busca un sonido seco, se amplía y se comparan los ángulos |
| Los ángulos tienen nombres que dicen algo | Se abre el clip: no son `Video 1`, `Video 2`, `Video 3` |
| Los cambios de cámara caen con la voz o con la acción | Se reproduce la escena: ninguno tropieza |
| Ningún cambio gratuito | Cada uno tiene un motivo que se puede decir en una frase |
| El audio no salta en los cortes | Se escucha con auriculares |
| El clip **no** está aplanado | Clic derecho sobre un clip: `Switch Multicam Clip Angle` sigue ahí |

### Subtítulos (40 puntos)

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| Todos dentro del rectángulo `Title` | `View > Safe Area > Title` y se reproduce |
| Entran con la voz y salen con la voz | Se reproduce mirando el pie de imagen |
| Ninguno cruza un corte a otra escena | Se mira cada corte de escena |
| Ninguno de más de dos líneas | Se recorre la lista del panel `Captions` |
| Las líneas están cortadas donde la frase respira | Se leen: no separan artículo de sustantivo |
| El texto está resumido, no transcrito | No hay muletillas ni titubeos en pantalla |
| Se leen sobre cualquier fondo de la pieza | Se reproduce entera mirando solo el texto |
| Ninguna falta de ortografía | Se repasa el `.srt` exportado, que es texto plano |

### Gestión e intercambio (20 puntos)

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| El nombre de la pista es un código de idioma real | `es-ES`, `en-US`… no «Español» |
| La comparación del intercambio nombra cosas concretas | Se lee la nota: dice qué se perdió, no «bastantes cosas» |
| Media Management se leyó y se canceló | Los tres tamaños están anotados y no hay carpeta de destino |
| Las timelines de las semanas cerradas están desactivadas | Ojo tachado en `BC-Montaje-v1` a `v4` |

### Notas escritas (10 puntos)

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| El apartado de la Semana 12 tiene sus cuatro bloques cerrados | Se lee `notas-de-montaje.md` |
| El bloque de intercambio dice **qué no sobrevivió** | Se lee: es el que más vale de la semana |

**Puntuación**: 70 puntos o más sobre 100.

---

## 📈 Cómo se calcula la nota

```
Nota = Conocimiento × 0,30 + Desempeño × 0,40 + Producto × 0,30
```

Con un mínimo del 70 % **en cada una de las tres**.

---

## 🔄 Si no llegas

| Evidencia | Qué repasar |
| --------- | ----------- |
| Conocimiento por debajo de 70 | Las teorías 02, 03 y 09: son de donde salen siete de las diez preguntas |
| Desempeño por debajo de 70 | El bloque `✅ Verificación` del README de la semana, que lista las causas por check |
| Producto por debajo de 70 | Reproduce la pieza entera con auriculares y mirando solo el pie de imagen |

Y si la pega es de tiempo: la práctica 03 es la que se queda en tu pieza. Las otras tres son
habilidades que se recuperan.

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 11](../week-11-titulos_texto_plus_efectos_y_compuestos/rubrica-evaluacion.md) | **Rúbrica Semana 12** | [Semana 13](../week-13-fairlight_anatomia_y_mezcla_base/README.md) |

← [Volver a la Semana 12](README.md)
