# 📚 Libros y manuales gratuitos — Semana 05

> Todo lo de esta lista es descargable sin pagar. El primero es la fuente de verdad de los
> ajustes que esta semana toca; los demás explican los dos oficios que hay detrás: el de
> quien decide un formato de trabajo y el de quien pega el sonido a la imagen.

---

## Imprescindible

### DaVinci Resolve 21 Reference Manual

<https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>

PDF oficial y gratuito, en la sección de documentación de la familia de productos.

**Por qué vale la pena**: dos capítulos son literalmente el temario de esta semana.
***Improving Performance*** cubre los modos de caché, la barra de estado y las opciones de
borrado; el bloque de ***Optimized Media and Render Cache*** documenta los desplegables de
formato y resolución con las opciones exactas de tu sistema operativo, que es lo que este
material no puede verificar por la API de scripting. El capítulo ***Multicam Editing***
recoge el diálogo de creación de clips multicámara.

**Cómo usarlo**: búscalo por el nombre inglés del ajuste (`Proxy Handling`,
`Render Cache`, `Optimized Media`) en vez de leer el capítulo entero. Cuando este material
y el manual discrepen, **gana el manual**.

---

## Guías oficiales de entrenamiento

### Blackmagic Design Training — guías y material de práctica

<https://www.blackmagicdesign.com/products/davinciresolve/training>

Blackmagic publica gratis los libros de sus cursos oficiales, en PDF, con el material de
vídeo para hacer los ejercicios.

**Por qué vale la pena**: sus capítulos de flujo de trabajo explican la decisión de
proxies con material de cámara real, que es donde la decisión importa de verdad. Y el
material descargable incluye tomas con audio de doble sistema, que es justo lo que cuesta
conseguir para la práctica 03.

**Además**: si aún no lo descargaste en la Semana 04, hazlo ahora. De aquí sale el material
log y RAW de las Semanas 16 a 22.

---

## Sobre codecs de trabajo

### Documentación técnica de los codecs intra-frame de post-producción

Los fabricantes publican las especificaciones de sus codecs de post-producción —familias
como DNxHR y ProRes— con sus tablas de bitrate por resolución y por calidad.

**Por qué vale la pena**: esas tablas son la respuesta exacta a la pregunta "¿cuánto me va
a ocupar esto?", que es la pregunta central de la práctica 01. Ver que un codec de
post-producción pide diez veces más bitrate que un H.264 de cámara explica de golpe por qué
un medio optimizado ocupa lo que ocupa.

**Cuánto leer**: la tabla de bitrates de tu resolución. Una página, y no vuelves a elegir
un formato de optimizados a ciegas.

---

## Sobre sonido y sincronización

### EBU R 128 — recomendación de loudness

<https://tech.ebu.ch/publications/r128>

**Por qué vale la pena**: no trata de sincronía, pero sí establece los estándares técnicos
del audio de vídeo, y ahí está la razón de que **48 kHz** sea la frecuencia de muestreo de
todo lo que se graba para imagen. Esa cifra es la que evita la deriva de la teoría 06.

**Cuánto leer**: la primera página. Es una recomendación corta, y vuelve entera en la
Semana 15.

---

## 📥 Cómo organizarlos

Los PDF, en `BC-Resolve/04-respaldos/documentacion/`, junto al Reference Manual de la
Semana 03. Ocupan poco y te evitan depender de tener internet el día que se te atasque
algo.

---

← [Volver a la Semana 05](../../README.md)
