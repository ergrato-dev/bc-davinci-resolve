# 🎞️ Pack de medios

> No puedes aprender a etalonar sin material que necesite etalonaje, ni a limpiar
> diálogo sin diálogo sucio. Este documento te dice exactamente qué descargar.

El bootcamp usa **dos fuentes de material** a la vez:

1. **El pack común**: material libre y curado que descargas una vez. Es el que usan
   las prácticas y el que verifica el autograder, porque así todos partimos de lo mismo.
2. **Tu material propio**: lo que grabes tú. Es el que alimenta tu
   [proyecto hilo conductor](proyecto-hilo-conductor.md), porque un bootcamp de nueve
   meses sobre material ajeno se abandona en el mes tres.

> [!WARNING]
> **Nada de material con copyright.** Ni un tráiler descargado, ni un videoclip, ni
> una canción de tu biblioteca "solo para practicar". Todo lo que se lista aquí tiene
> licencia explícita —Creative Commons, dominio público o samples oficiales— y en la
> Semana 15 se explica por qué eso importa incluso cuando el vídeo no se publica.

---

## 1. Estructura de carpetas

Créala antes de descargar nada. Las prácticas la asumen:

```
00-medios-bootcamp/
├── 01-basicos/          # clips cortos variados: cámara en mano, trípode, día, noche
├── 02-entrevista/       # plano fijo de alguien hablando, con audio imperfecto
├── 03-multicamara/      # una escena rodada desde 3-4 ángulos con audio común
├── 04-log-y-raw/        # material log y Blackmagic RAW para las semanas de color
├── 05-croma/            # tomas sobre fondo verde para el keying de la Semana 25
├── 06-audio/
│   ├── musica/
│   ├── efectos/
│   └── ambientes/
├── 07-graficos/         # PNG con transparencia y logotipos para composición
└── MANIFIESTO.sha256    # huellas de integridad, generadas por ti (sección 4)
```

Apunta la variable `BC_MEDIOS` a esta carpeta para que el doctor la compruebe:

```bash
export BC_MEDIOS="<ruta-a-medios>/00-medios-bootcamp"   # macOS y Linux
setx BC_MEDIOS "<ruta-a-medios>\00-medios-bootcamp"     # Windows
```

---

## 2. De dónde sale cada cosa

> [!NOTE]
> No se enlazan archivos concretos porque las URL directas de estos sitios cambian.
> Se enlaza la **fuente**, y se dice qué buscar dentro. Descarga lo que encaje con la
> descripción; las prácticas están escritas para funcionar con cualquier material que
> cumpla la especificación, no con un archivo concreto.

### Vídeo general — carpetas `01-basicos/` y `02-entrevista/`

| Fuente | Qué buscar | Por qué vale la pena |
| ------ | ---------- | -------------------- |
| [Pexels Videos](https://www.pexels.com/videos/) | 15-20 clips de 5-20 s: cámara en mano, trípode, interior, exterior, día, noche, un plano de alguien hablando a cámara | Licencia libre, descarga directa sin cuenta, y variedad suficiente para las semanas de montaje |
| [Pixabay Videos](https://pixabay.com/videos/) | Lo mismo, si Pexels se te queda corto | Segunda fuente con la misma clase de licencia; útil para completar huecos concretos |
| [Wikimedia Commons — vídeo](https://commons.wikimedia.org/wiki/Category:Videos) | Material documental y de archivo | Es donde aparece el material feo y real: mala luz, audio de ambiente, cámaras dispares. Justo lo que necesitas para practicar corrección |

**Especificación mínima para `02-entrevista/`**: un plano fijo, una persona hablando
al menos 60 s, con audio que tenga algún problema audible (ambiente, eco, nivel bajo).
Si no encuentras uno malo, **grábalo tú**: es el ejercicio más útil de la Semana 14.

### Cortometrajes completos — para montaje, color y análisis

| Fuente | Qué buscar | Por qué vale la pena |
| ------ | ---------- | -------------------- |
| [Blender Open Movies](https://studio.blender.org/films/) | *Big Buck Bunny*, *Sintel*, *Tears of Steel*, *Cosmos Laundromat* | Creative Commons, y varios publican **material de producción** además del corto montado. *Tears of Steel* incluye tomas de acción real con croma |
| [Netflix Open Content](https://opencontent.netflix.com/) | *Meridian*, *Sol Levante*, *Cosmos Laundromat* | Material publicado expresamente para pruebas técnicas, incluido **HDR**. Es de lo poco libre que sirve para la Semana 22 |
| [Internet Archive — Moving Image](https://archive.org/details/movies) | Cine y documental en dominio público | Material antiguo, con grano, con derivas de color y con audio de época: un banco de pruebas excelente para restauración y para la Semana 21 |

### Material log y RAW — carpeta `04-log-y-raw/`

Esta es la carpeta difícil de llenar y la más importante de las Semanas 16-22.

| Fuente | Qué buscar | Por qué vale la pena |
| ------ | ---------- | -------------------- |
| [Blackmagic Design — DaVinci Resolve Training](https://www.blackmagicdesign.com/products/davinciresolve/training) | Los proyectos de práctica que Blackmagic publica junto a sus guías oficiales de formación | Es el material **oficial**: incluye Blackmagic RAW y tomas log pensadas exactamente para enseñar etalonaje, y está pensado para Resolve |
| Tu propia cámara | Si tu cámara o tu móvil puede grabar en un perfil plano o log, graba una toma con mucho rango dinámico (una ventana con exterior, una cara a contraluz) | Practicar color con tu propio material log es lo que hace que el conocimiento se quede |

> [!TIP]
> Si no consigues material RAW, **no bloquees el bootcamp por eso**. Las Semanas 16-21
> funcionan enteras con material log o incluso Rec.709. Solo la Semana 22 (RAW y HDR)
> pierde la mitad de su parte práctica, y está avisado en su README.

### Croma — carpeta `05-croma/`

| Fuente | Qué buscar | Por qué vale la pena |
| ------ | ---------- | -------------------- |
| [Pexels Videos](https://www.pexels.com/videos/) buscando *green screen* | 2-3 tomas de persona sobre fondo verde, a poder ser una bien iluminada y otra mal | Necesitas las dos: el keying fácil enseña el mecanismo, el difícil enseña el oficio (Semana 25) |
| [Blender — *Tears of Steel*](https://mango.blender.org/) | Su material de producción incluye tomas con croma | Es material de rodaje real, con los problemas de un rodaje real |

### Audio — carpeta `06-audio/`

| Fuente | Qué buscar | Por qué vale la pena |
| ------ | ---------- | -------------------- |
| [Freesound](https://freesound.org/) | Efectos puntuales (pasos, puertas, viento) y ambientes largos de 2-3 min | El banco de efectos libre más grande; cada archivo indica su licencia Creative Commons concreta, que hay que leer |
| [Free Music Archive](https://freemusicarchive.org/) | 3-4 piezas musicales de 2-4 min, de intensidades distintas | Música con licencia clara; la variedad de intensidad es lo que hace útil el ejercicio de ducking de la Semana 15 |
| [Internet Archive — Audio](https://archive.org/details/audio) | Grabaciones de dominio público, incluida palabra hablada | Para practicar restauración de audio degradado de verdad |

### Gráficos — carpeta `07-graficos/`

Bastan tres o cuatro **PNG con canal alfa** (un logotipo, un icono, una textura
recortada). Puedes exportarlos de cualquier editor de imagen. La Semana 23 explica qué
es el canal alfa y por qué un JPG no sirve aquí.

---

## 3. Cuánto material y cuándo

No descargues todo el primer día. El orden que sigue el bootcamp:

| Antes de la semana | Necesitas |
| ------------------ | --------- |
| 04 | `01-basicos/` con 15-20 clips |
| 12 | `03-multicamara/` |
| 13 | `02-entrevista/` y `06-audio/` |
| 16 | `04-log-y-raw/` |
| 25 | `05-croma/` |
| 23 | `07-graficos/` |

Total aproximado: **20-60 GB**, según cuánto material log y RAW consigas.

---

## 4. Sellar e integridad del pack

Los archivos de vídeo se corrompen en silencio: un disco externo con un cable flojo, una
copia interrumpida, un fallo de sector. Resolve no te avisa; simplemente un clip
empieza a dar artefactos en el minuto tres.

Por eso, **una vez terminada la descarga**, sella el pack:

```bash
./scripts/preparar-medios.sh --sellar
```

Eso genera `MANIFIESTO.sha256` con la huella de cada archivo. A partir de ahí, cuando
sospeches de algo —o antes de empezar una fase nueva— comprueba:

```bash
./scripts/preparar-medios.sh
```

Si un archivo cambió o se corrompió, el script te lo dice por nombre.

> [!NOTE]
> El manifiesto lo generas tú, con tus archivos. No se publica uno en el repositorio
> porque el material lo eliges tú entre las fuentes de arriba: dos personas tendrán
> packs distintos y ambos válidos. Lo que garantiza el manifiesto es que **tu** pack
> sigue siendo el mismo la semana 30 que la semana 4.

---

## 5. Tu material propio

Además del pack, cada fase te pide grabar algo. No hace falta cámara: el móvil sirve
para todo el bootcamp.

| Fase | Qué grabar | Para qué |
| ---- | ---------- | -------- |
| 1-2 | 20-30 planos de tu tema elegido | El montaje de tu pieza |
| 3 | Una escena desde 3 ángulos | Multicámara real, con tus propios problemas de sincronía |
| 4 | Una locución de 2 min en una habitación normal | El ejercicio de limpieza de diálogo más honesto que existe |
| 5 | Una toma con mucho contraste, en el perfil más plano que permita tu cámara | Etalonaje sobre material tuyo |
| 6 | Un plano fijo con algo que quitar (un cable, una señal) | Cleanup y paint en Fusion |

> [!IMPORTANT]
> Si grabas con el móvil o con OBS y el archivo sale en `.mkv`, **Resolve no lo va a
> importar**. Hay que remuxearlo a `.mp4` o `.mov` primero. La Semana 02 explica qué
> significa remuxear y por qué no pierde calidad.

---

## 📚 Recursos adicionales

- [Creative Commons — elegir una licencia](https://creativecommons.org/share-your-work/) — para entender qué te permite exactamente cada variante (BY, BY-SA, BY-NC) antes de usar un archivo en una pieza que vayas a publicar.
- [Blackmagic Design — Training](https://www.blackmagicdesign.com/products/davinciresolve/training) — además del material de práctica, las guías oficiales en PDF son gratuitas y están escritas por el equipo del producto.

## ✅ Checklist de verificación

- [ ] Estructura `00-medios-bootcamp/` creada con sus siete subcarpetas
- [ ] Variable `BC_MEDIOS` definida y detectada por `verificar-semana.py --doctor`
- [ ] Al menos 15 clips variados en `01-basicos/`
- [ ] Un plano de alguien hablando, con audio imperfecto, en `02-entrevista/`
- [ ] He comprobado la licencia de cada archivo que he descargado
- [ ] Pack sellado con `./scripts/preparar-medios.sh --sellar`

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
