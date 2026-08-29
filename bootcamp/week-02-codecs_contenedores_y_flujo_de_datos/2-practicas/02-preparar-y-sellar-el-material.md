# Práctica 02 — Preparar y sellar el material

> Al terminar tendrás la carpeta de medios creada, el material que Resolve no acepta ya
> convertido, y una huella criptográfica de cada archivo para saber si alguno se corrompe
> dentro de seis meses.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 01](01-leer-la-ficha-tecnica-de-un-archivo.md), [Teoría 01](../1-teoria/01-contenedor-y-codec.md), [Teoría 08](../1-teoria/08-flujo-de-datos.md)

## Contexto

Un bootcamp de nueve meses acumula gigabytes. Los discos fallan poco, pero fallan, y una
copia corrupta no avisa: el archivo sigue ahí, sigue pesando lo mismo y un día Resolve lo
abre con un frame verde en medio.

Un **checksum** —una huella criptográfica— resuelve eso. Es un número calculado a partir
del contenido del archivo: si cambia un solo bit, el número cambia. Sellar hoy cuesta dos
minutos y convierte "creo que está bien" en "sé que está intacto".

---

## Paso 1: Crear la estructura del pack de medios

**Por qué**: las prácticas del bootcamp asumen estos nombres. Si los cambias, cada
práctica que mencione una carpeta te obligará a traducir mentalmente, y en la Semana 05,
con proxies de por medio, eso se paga.

Dentro de `BC-Resolve/00-medios-bootcamp/` (creada en la Semana 01), crea:

```
00-medios-bootcamp/
├── 01-basicos/
├── 02-entrevista/
├── 03-multicamara/
├── 04-log-y-raw/
├── 05-croma/
├── 06-audio/
│   ├── musica/
│   ├── efectos/
│   └── ambientes/
└── 07-graficos/
```

El detalle de qué va en cada una y de dónde sacarlo está en
[`docs/pack-de-medios.md`](../../../docs/pack-de-medios.md).

**Verifica**:

```bash
export BC_MEDIOS="<ruta-a-medios>/00-medios-bootcamp"   # macOS y Linux
./scripts/preparar-medios.sh
```

La sección `== Estructura ==` tiene que dar `OK` en las nueve carpetas.

---

## Paso 2: Descargar lo mínimo para esta semana

**Por qué**: no hace falta el pack entero todavía. Descargarlo todo el primer día es la
forma más común de no descargar nada.

Para cerrar la Semana 02 necesitas cuatro archivos, y ninguno es exigente:

| Carpeta | Qué | De dónde |
| ------- | --- | -------- |
| `01-basicos/` | Dos clips de vídeo de 5-20 s, **de fuentes distintas** | Uno grabado por ti, otro de [Pexels](https://www.pexels.com/videos/) |
| `06-audio/efectos/` | Un archivo de audio, a poder ser WAV | [Freesound](https://freesound.org/) |
| `07-graficos/` | Un PNG con canal alfa (fondo transparente) | Exportado de cualquier editor de imagen |

**Canal alfa** (*alpha channel*) es un cuarto canal, además de rojo, verde y azul, que
guarda la transparencia de cada píxel. Un JPG no lo tiene; un PNG sí. La Semana 23 lo
desarrolla.

**Verifica**: los cuatro archivos están en su carpeta y MediaInfo los abre.

---

## Paso 3: Convertir lo que Resolve no acepta

**Por qué**: Resolve **no importa `.mkv`**. Si tienes grabaciones de OBS o material
descargado en Matroska, el momento de arreglarlo es ahora, no cuando estés montando.

> [!NOTE]
> Si no tienes ningún `.mkv`, salta al paso 4. No necesitas crear uno para practicar.

Necesitas **FFmpeg**, de <https://ffmpeg.org/download.html>. Después:

```bash
ffmpeg -i grabacion.mkv -c copy grabacion.mp4
```

`-c copy` es lo importante: copia las pistas tal cual, sin recomprimir. Tarda segundos y
**no pierde calidad**, porque no toca los datos de vídeo.

> [!WARNING]
> **No borres el `.mkv` original hasta comprobar que el `.mp4` se reproduce entero.** Un
> remux mal terminado produce un archivo que abre y se corta a la mitad, y el síntoma no
> aparece hasta que llegas a ese punto. Reprodúcelo hasta el final antes de borrar nada.

Y si el origen es OBS, arréglalo de raíz: `Ajustes > Avanzado > Grabación`, activa el
remuxeado automático a `.mp4`. Así no vuelves a tener el problema.

**Verifica**: el `.mp4` resultante se reproduce completo, y MediaInfo muestra el mismo
codec de vídeo que tenía el `.mkv`. Si el codec ha cambiado, no has remuxeado: has
transcodificado.

---

## Paso 4: Poner el audio a 48 kHz

**Por qué**: el vídeo trabaja a 48 kHz. Un archivo a 44,1 kHz obliga a remuestrear y, si
algo va mal en la cadena, produce deriva de sincronía a lo largo de la toma.

Comprueba con MediaInfo el campo `Sampling rate` de tu archivo de audio. Si dice
`44.1 kHz`:

```bash
ffmpeg -i sonido.wav -ar 48000 sonido-48k.wav
```

**Verifica**: MediaInfo muestra `48.0 kHz` en el archivo resultante.

> [!TIP]
> La música descargada casi siempre viene a 44,1 kHz, porque viene del mundo del CD y del
> streaming musical. Conviértela al llegar, no cuando estés mezclando en la Semana 15.

---

## Paso 5: Sellar el pack

**Por qué**: a partir de aquí, cualquier corrupción silenciosa se detecta con un comando.
Sin el sello, se detecta cuando ya es tarde.

```bash
./scripts/preparar-medios.sh --sellar
```

El script recorre la carpeta, calcula el `sha256` de cada archivo y escribe
`MANIFIESTO.sha256`.

**SHA-256** es una función que reduce cualquier archivo a un número de 64 caracteres
hexadecimales. Dos archivos distintos no comparten ese número en la práctica, así que si
la huella coincide, el contenido está intacto.

**Verifica**:

```bash
./scripts/preparar-medios.sh
```

Debe decir `OK  los N archivos del manifiesto siguen intactos.`

---

## Paso 6: Comprobar que el sello detecta un cambio

**Por qué**: una comprobación que nunca ha fallado no está probada. Rómpela a propósito
una vez, para saber qué aspecto tiene un fallo de verdad.

1. Copia uno de tus archivos pequeños a `01-basicos/` con otro nombre
2. Ejecuta `./scripts/preparar-medios.sh`
3. El script avisará de que hay un archivo nuevo sin sellar
4. Vuelve a sellar: `./scripts/preparar-medios.sh --sellar`

**Verifica**: has visto el aviso de archivo sin sellar y, después de volver a sellar,
todo vuelve a estar en verde.

> [!TIP]
> Repite el sellado cada vez que añadas material al pack. Es un comando, y a cambio
> tienes una respuesta exacta a "¿se ha estropeado algo?" durante nueve meses.

---

## ✅ Resultado

- [ ] Las nueve carpetas del pack existen y `preparar-medios.sh` las ve
- [ ] Dos clips de vídeo de fuentes distintas en `01-basicos/`
- [ ] Un archivo de audio en `06-audio/efectos/`, a 48 kHz
- [ ] Un PNG con canal alfa en `07-graficos/`
- [ ] Ningún `.mkv` sin convertir en el pack
- [ ] `MANIFIESTO.sha256` generado y verificando en verde
- [ ] He visto cómo se comporta el script cuando algo cambia

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `No sé dónde está tu pack de medios` | La variable `BC_MEDIOS` no está definida | `export BC_MEDIOS="<ruta-a-medios>/00-medios-bootcamp"`, o pasa la ruta como argumento |
| El script marca `KO` en una subcarpeta | Falta esa carpeta, o tiene otro nombre | Créala con el nombre exacto, en minúsculas y con el guion |
| El remux produce un archivo que no se reproduce | El `.mkv` de origen estaba truncado | Vuelve a grabarlo o a descargarlo; un origen roto no se arregla remuxeando |
| `ffmpeg: command not found` | FFmpeg no está instalado o no está en el `PATH` | Instálalo desde ffmpeg.org y reabre la terminal |
| La verificación falla en archivos que no he tocado | O el disco está fallando, o los movió una sincronización de nube | Comprueba que el pack no esté dentro de OneDrive, Dropbox ni iCloud Drive |
| El sellado tarda muchísimo | Estás sellando decenas de gigabytes desde un disco lento | Es normal: se lee cada byte. Déjalo terminar y no lo repitas sin motivo |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · Leer la ficha técnica de un archivo](01-leer-la-ficha-tecnica-de-un-archivo.md) | **02 · Preparar y sellar el material** | [03 · El banco de formatos](03-el-banco-de-formatos.md) |

← [Volver a la Semana 02](../README.md)
