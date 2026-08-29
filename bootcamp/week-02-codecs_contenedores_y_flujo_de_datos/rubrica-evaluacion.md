# 📊 Rúbrica de evaluación — Semana 02

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en
la tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 02` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Explica la diferencia entre contenedor y codec sin usar la palabra "formato". ¿Por qué
   Resolve muestra `QuickTime` en el campo `Format` de un archivo `.mp4`?
2. ¿Qué diferencia hay entre remuxear y transcodificar? ¿Cuál de las dos pierde calidad, y
   por qué renombrar la extensión de un archivo no es ninguna de las dos cosas?
3. ¿Qué son los frames I, P y B, y qué es un GOP? Explica con eso por qué arrastrar la
   cabeza lectora sobre un clip H.264 va a tirones aunque la reproducción normal vaya bien.
4. ¿Cuánta información de color guarda un `4:2:0` frente a un `4:2:2`? Nombra tres
   situaciones concretas en las que la diferencia se nota.
5. ¿Cuántos tonos por canal dan 8 bits y cuántos 10 bits? ¿Por qué el etalonaje empeora el
   banding en lugar de arreglarlo?
6. ¿Qué se ve cuando Resolve interpreta como `Video` un archivo que es `Full`? ¿Y al revés?
   ¿Cuál de los dos errores destruye información?
7. ¿Por qué un clip log se ve gris y lavado? ¿Por qué grabar log con una cámara de 8 bits
   es mala combinación?
8. En Blackmagic RAW, ¿qué comprime más, `3:1` o `12:1`? ¿Qué tiene más calidad, `Q0` o
   `Q5`? Nombra tres parámetros que sigan siendo ajustables después de grabar.
9. ¿Por qué el vídeo trabaja a 48 kHz y no a 44,1? ¿Por qué el máster de audio se guarda en
   PCM y no en AAC?
10. Un clip ocupa 240 MB y dura 80 segundos. ¿Cuál es su bitrate en Mbps? ¿Cuántos GB
    ocuparía una hora de ese material? ¿Cuántos MB/s tiene que entregar el disco para
    reproducir cuatro clips como ese a la vez?

<details>
<summary>📝 Respuestas</summary>

**1.** El **contenedor** es la estructura de archivo que guarda varias pistas juntas —vídeo,
audio, subtítulos, metadata— y dice cómo están ordenadas y dónde empieza cada frame. No
comprime nada. El **codec** es el método con el que se comprimieron los datos de **una**
pista concreta; cada pista tiene el suyo, y en un `.mp4` de móvil conviven H.264 para vídeo
y AAC para audio.

Resolve muestra `QuickTime` para un `.mp4` porque **reconoce la familia del contenedor, no
la extensión**: MP4 y MOV descienden los dos del *ISO Base Media File Format*, que nació del
formato QuickTime de Apple. No es un error de Resolve.

**2.** **Remuxear** saca las pistas de una caja y las mete en otra sin tocarlas: tarda
segundos y **no pierde calidad**, porque los bits del vídeo son idénticos.
**Transcodificar** descomprime y vuelve a comprimir con otro codec: tarda mucho más y, con
un codec con pérdida, **degrada**.

Renombrar la extensión no es ninguna de las dos porque **no mueve un solo byte del
archivo**: un `.mkv` renombrado a `.mp4` sigue siendo Matroska por dentro, y Resolve lo
sigue rechazando.

**3.** Un frame **I** guarda la imagen completa y se decodifica solo. Un frame **P** guarda
las diferencias respecto a un frame anterior. Un frame **B**, respecto a uno anterior y uno
posterior. Un **GOP** es un frame I con todos los P y B que dependen de él.

El scrubbing va a tirones porque para mostrar un frame cualquiera hay que decodificar
primero el frame I de su grupo y todos los intermedios. La reproducción normal hacia
delante es barata porque ya se llevan decodificados; saltar o ir hacia atrás obliga a
reconstruir la cadena entera cada vez.

**4.** `4:2:2` guarda el **50 %** de la información de color y `4:2:0` el **25 %**. El
brillo se guarda entero en los dos casos.

Tres situaciones donde se nota: **croma/keying**, porque el borde se calcula sobre color de
menos resolución; **subir mucho la saturación**, porque los bloques de 2 × 2 se hacen
visibles; y **texto o gráficos de color saturado**, cuyos bordes se emborronan. Valen
también los qualifiers de secundarias y el escalado grande.

**5.** 8 bits dan **256 tonos** por canal; 10 bits dan **1024**, cuatro veces más.

El etalonaje empeora el banding porque **no inventa tonos intermedios**: al subir el
contraste separa valores que ya eran escalones. Los once tonos que había en una zona de
cielo siguen siendo once, pero ahora ocupan el doble de rango, así que cada franja se ve
el doble de ancha.

**6.** Si interpreta como `Video` (16-235) algo que es `Full` (0-255), la imagen se ve
**lavada**: los negros se levantan y los blancos se apagan. Al revés, se ve **recortada**.

El que destruye información es el segundo: interpretar `Full` lo que es `Video` **recorta**
sombras y altas luces reales, y eso no se recupera. El primero es reversible, porque los
valores siguen ahí.

**7.** Se ve lavado porque la curva log **levanta los negros y contiene los blancos** para
conservar rango dinámico: guarda detalle en la sombra y en el cielo del mismo plano, a
cambio de no estar listo para mirarse. Se convierte con una LUT o con la gestión de color.

Log en 8 bits es mala combinación porque el log reparte los mismos 256 tonos en un rango
mucho más ancho: al aplicar la LUT, esos escalones se separan y aparece banding.

**8.** **`12:1` comprime más** que `3:1` —el ratio dice cuántas veces se reduce—.
**`Q0` tiene más calidad** que `Q5`: la numeración va al revés de lo que parece.

Siguen ajustables después de grabar: **balance de blancos y tinte**, **ISO**,
**exposición** (con margen), **curva y espacio de color**, y el **sharpening y la reducción
de ruido** de cámara. No son ajustables el encuadre, el foco ni el movimiento: eso no es
RAW, es rodaje.

**9.** 48 kHz es el estándar del vídeo; 44,1 kHz viene del CD y del mundo de la música.
Mezclarlos obliga a remuestrear, y si algo en la cadena lo hace mal aparece deriva de
sincronía a lo largo de la toma.

El máster va en PCM porque **AAC es compresión con pérdida** y cada reexportación acumula
pérdida generacional. Además, la limpieza de diálogo trabaja peor sobre material al que ya
se le ha quitado información. El AAC es la copia de reparto, no el máster.

**10.** Bitrate: `240 MB × 8 = 1920 Mb`, y `1920 ÷ 80 = ` **24 Mbps**.

GB por hora: `24 ÷ 8 = 3 MB/s`, `3 × 3600 = 10 800 MB`, es decir unos **10,5 GB por hora**
(el atajo de dividir los Mbps entre 2 da 12 GB, que es la estimación conservadora correcta).

Cuatro clips a la vez: `3 MB/s × 4 = ` **12 MB/s**. Cualquier disco lo aguanta; el problema
llega con intermedios de montaje, que piden unos 20 MB/s por pista.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **14,29 puntos**.

```bash
python scripts/verificar-semana.py 02
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 03 | `proyecto-abierto` | 14,29 |
| 03 | `frame-rate-intacto` | 14,29 |
| 03 | `bin-formatos-activo` | 14,29 |
| 03 | `banco-completo` | 14,29 |
| 03 | `banco-nombres` | 14,29 |
| 03 | `video-h264` | 14,29 |
| 03 | `contenedor-quicktime` | 14,29 |

**Necesitas 70 / 100**, es decir **al menos 5 de los 7 checks**. Pero `frame-rate-intacto`
es eliminatorio: si falla, tu proyecto ha cambiado de cadencia con clips ya dentro y hay
que rehacerlo antes de seguir a la Semana 03.

> [!TIP]
> Cuatro de los siete checks leen el **bin activo**: `banco-completo`, `banco-nombres`,
> `video-h264` y `contenedor-quicktime`. Si fallan en bloque, o con un mensaje raro en vez
> de un `KO` limpio, casi siempre es que el bin seleccionado en el media pool no es
> `BC-Formatos`. Haz clic sobre él y repite.

---

## 📦 Producto (30 %)

Tu ficha técnica, el pack sellado y el respaldo. Se evalúa con criterios observables.

### Verificable a simple vista (55 puntos)

| Criterio | Puntos |
| -------- | ------ |
| `ficha-tecnica-material.md` existe en `04-respaldos/` | 5 |
| La tabla comparativa está completa: 12 filas × 3 archivos | 15 |
| Las casillas vacías explican por qué lo están | 5 |
| Los tres archivos son de naturaleza distinta, no tres clips del mismo móvil | 5 |
| La tabla "Lo que dice Resolve" está rellena para los cuatro clips del banco | 10 |
| `MANIFIESTO.sha256` existe y `preparar-medios.sh` verifica en verde | 10 |
| Existe `BC-Bootcamp-Resolve-semana02.drp` en `04-respaldos/` | 5 |

### Calidad de las decisiones (45 puntos)

| Criterio | Puntos |
| -------- | ------ |
| El presupuesto de disco tiene números medidos, no adjetivos | 10 |
| La velocidad del disco está medida por ti, no copiada de la caja | 5 |
| La decisión de rodaje nombra dispositivo **y** modo concreto (resolución, fps, codec) | 10 |
| Esa decisión está justificada con lo aprendido esta semana, no con "es lo que uso" | 10 |
| La tabla de Resolve señala al menos una diferencia con lo que decía MediaInfo | 5 |
| `Cache files location` apunta a `02-cache/` y no al disco del sistema | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en el panel Metadata en diez segundos:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| `BC-formato-audio`, campo `Sample Rate` | `48000` |
| `BC-formato-alpha`, campo `Alpha mode` | Algo distinto de `None` |
| `BC-formato-h264`, campo `Bit Depth` | `8` en material de consumo |
| `BC-formato-h264`, campo `Data Level` | `Auto` |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| El presupuesto de disco no tiene ni un número | −20 |
| La ficha describe material genérico de internet en vez del tuyo | −20 |
| Hay un `.mkv` sin convertir dentro del pack de medios | −10 |
| El material del banco se movió después de importarlo y los clips están *offline* | −10 |
| No hay respaldo `.drp` | −10 |
| La decisión de rodaje se queda en "grabo con el móvil" | −10 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

No pases a la Semana 03 sin haber cerrado esta. En concreto:

- **Si falla `frame-rate-intacto`**: es lo único irreversible. Crea el proyecto de nuevo,
  configúralo con los ajustes de la Semana 01 e importa **después**.
- **Si fallan los checks del banco**: repite la práctica 03, pasos 2 a 4. Casi siempre es
  una errata en un nombre de archivo.
- **Si el cuestionario va por debajo de 70**: las preguntas 3, 5, 6 y 8 son las que más
  gente falla. Vuelve a las teorías 02, 04 y 06.
- **Si el producto va por debajo de 70**: casi siempre es el presupuesto de disco sin
  medir. Medir cuesta diez minutos y es la mitad de la nota de esta parte.

---

← [Volver a la Semana 02](README.md)
