# Proyecto — Semana 02: la ficha técnica de tu material

> Al terminar esta semana sabrás exactamente qué clase de archivos va a producir tu pieza,
> cuánto van a ocupar y qué disco necesitas. Y tu proyecto de Resolve tendrá dentro sus
> primeros clips.

## 📦 Qué añade esta semana

La segunda capa: **el conocimiento técnico de tu propio material**.

En la Semana 01 decidiste qué vas a hacer y con qué parámetros. Esta semana averiguas qué
va a salir de tu cámara cuando lo grabes: qué codec, con cuánto color, con cuánta
profundidad y a qué ritmo va a llenar el disco.

Va aquí y no después porque las tres decisiones que dependen de esto —qué cámara y qué
modo usar, qué disco comprar, si vas a necesitar proxies— hay que tomarlas **antes** de
grabar. Después ya no son decisiones: son consecuencias.

Es además la semana en la que entra el primer clip en tu proyecto, y eso congela el frame
rate para siempre. Lee la advertencia de la
[práctica 03](../2-practicas/03-el-banco-de-formatos.md) antes de importar nada.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca
carácter a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` sigue siendo **24** después de importar
3. El bin **`BC-Formatos`** es el bin activo del media pool
4. `BC-Formatos`, como bin activo, contiene **al menos cuatro clips**
5. Los cuatro llevan los nombres **`BC-formato-h264`**, **`BC-formato-segundo`**,
   **`BC-formato-audio`** y **`BC-formato-alpha`**
6. `BC-formato-h264.mp4` lleva de verdad un codec **H.264**
7. Resolve identifica su contenedor como **`QuickTime`**

```bash
python scripts/verificar-semana.py 02
```

---

## 📝 El entregable escrito

`BC-Resolve/04-respaldos/ficha-tecnica-material.md`, construido a lo largo de las cuatro
prácticas. Tiene cuatro partes.

### 1. Tabla comparativa de tres archivos (práctica 01)

Las doce filas —contenedor, codec, intra o long-GOP, chroma, bit depth, resolución, frame
rate, codec de audio, frecuencia de muestreo, bitrate y GB por hora— para tres archivos
distintos. Las casillas vacías llevan escrito **por qué** están vacías.

### 2. Tabla "Lo que dice Resolve" (práctica 03)

Los mismos archivos, leídos desde el panel Metadata de Resolve. La gracia está en la
comparación: qué campo llama Resolve de otra manera, cuál no muestra y cuál interpreta.

### 3. Presupuesto de disco (práctica 04)

Con números concretos, no con adjetivos:

- Velocidad medida de tu disco de trabajo, en MB/s
- Bitrate típico de tu material y sus GB por hora
- Horas de grabación previstas
- Total estimado del bootcamp y espacio libre actual
- Si vas a necesitar proxies desde la Semana 05, y por qué

### 4. La decisión de rodaje

Media página, y es la parte que de verdad importa:

> **Con qué voy a grabar mi pieza, en qué modo, y por qué.**

Nombra el dispositivo, el modo concreto —resolución, frame rate, codec si puedes
elegirlo— y justifica cada elección con lo que has aprendido esta semana. Si tu cámara
puede grabar en 10 bits o en `4:2:2`, di si lo vas a usar y a cambio de qué.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| La tabla comparativa está completa para los tres archivos | Se cuentan las casillas: 12 filas × 3 columnas |
| Las casillas vacías explican por qué lo están | Se leen. "No aplica: un WAV no tiene pista de vídeo" vale; una casilla en blanco no |
| Los tres archivos son de naturaleza distinta | Tres clips del mismo móvil no comparan nada |
| La tabla de Resolve señala al menos una diferencia con MediaInfo | El caso del `Format: QuickTime` cuenta, si está explicado |
| El presupuesto de disco tiene números, no adjetivos | "150 MB/s" vale; "va rápido" no |
| La decisión de rodaje nombra dispositivo y modo concreto | "Mi móvil" no es un modo. "1080p a 24 fps, H.264" sí |
| El audio del banco está a 48 kHz | Panel Metadata del clip `BC-formato-audio`, campo `Sample Rate` |
| El PNG tiene canal alfa de verdad | Panel Metadata, campo `Alpha mode` distinto de `None` |
| Existe el respaldo `.drp` de la semana | El archivo está en `04-respaldos/` |

---

## 💡 Adaptación a tu pieza

**Documental corto** · Vas a mezclar material de fuentes dispares: cámara, móvil,
grabaciones de archivo. Anota el codec y el frame rate de **cada** fuente en la tabla: la
Semana 10 te va a pedir conformar cadencias y agradecerás tenerlo escrito.

**Videoclip** · La música manda. Comprueba hoy que tu pista está a 48 kHz y en WAV, no en
MP3 a 44,1 kHz. Y si vas a rodar para ralentizar, calcula el disco con el frame rate alto,
que multiplica el bitrate.

**Cortometraje de ficción** · Si vas a etalonar con intención, esta es la semana para
averiguar si tu cámara ofrece 10 bits o `4:2:2` en algún modo. Anota qué pierdes al
activarlo: casi siempre, duración máxima de toma o recorte de sensor.

**Tutorial o vídeo formativo** · Tu captura de pantalla es el caso más delicado del
bootcamp: OBS graba en `.mkv` por defecto y Resolve no lo abre. Arréglalo hoy en los
ajustes de OBS, no el día de montar. Y comprueba a qué frame rate captura.

**Pieza de viaje** · El riesgo es el disco. Vas a grabar mucho más de lo que uses. Calcula
el presupuesto con generosidad y decide **ahora** si grabas en 4K o en 1080p: en 4K,
multiplica por cuatro todas las cifras de la tabla.

---

## 🚦 Cómo entregarlo

1. Bin `BC-Formatos` creado, activo y con los cuatro clips
2. `python scripts/verificar-semana.py 02` en verde, siete de siete
3. `ficha-tecnica-material.md` con sus cuatro partes en `04-respaldos/`
4. `MANIFIESTO.sha256` del pack de medios generado y verificando
5. Respaldo del proyecto: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana02.drp`

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Aceptar el diálogo de cambio de frame rate al importar | Aparece de golpe y el botón afirmativo es el cómodo | Di que no. Si ya dijiste que sí, hay que rehacer el proyecto: es la única forma |
| Renombrar la extensión en vez de remuxear | Parece que funciona porque el nombre cambia | El archivo no cambia. `ffmpeg -c copy`, y comprueba con MediaInfo |
| Rellenar el presupuesto de disco con adjetivos | Da pereza medir | Medir cuesta cinco minutos y evita comprar el disco equivocado |
| Copiar la tabla técnica de un tutorial en vez de medir el material propio | Los números de internet son de otras cámaras | La ficha describe **tu** material; si no, no sirve para nada |
| Dejar la decisión de rodaje en "grabo con el móvil" | Suena a respuesta | El móvil tiene modos: 1080p o 4K, 30 o 60 fps, H.264 o H.265. Elige uno y di por qué |
| Mover el material después de importarlo | Se reorganiza la carpeta "para dejarlo bonito" | Los clips se quedan *offline*. La estructura se decide antes, no después |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 01](../../week-01-fundamentos_de_imagen_en_movimiento/3-proyecto/README.md) | **Proyecto Semana 02** | [Semana 03](../../week-03-resolve_21_anatomia_bases_de_datos_y_preferencias/README.md) |

← [Volver a la Semana 02](../README.md)
