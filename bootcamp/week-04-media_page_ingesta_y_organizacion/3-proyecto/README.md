# Proyecto — Semana 04: el material entra

> Al terminar esta semana tu proyecto deja de estar vacío. Entran los primeros treinta y
> tantos clips, y entran organizados, descritos y marcados. Es la primera capa que ya no
> es infraestructura: es tu pieza empezando a existir.

## 📦 Qué añade esta semana

La cuarta capa: **el material**.

La Fase 0 dejó el proyecto con identidad técnica, entorno y red de seguridad, y sin un
solo clip de tu pieza. Esta semana abre la **Fase 1** metiendo el material dentro, con
la estructura ya hecha y con la metadata escrita desde el primer día.

El orden importa y es deliberado. Casi todo el mundo hace esto al revés: importa
primero, ordena si acaso, y describe nunca. El resultado es el mismo proyecto que
tendrás tú, con una diferencia: en la Semana 12, encontrar un plano concreto le costará
veinte minutos y a ti dos segundos.

> [!IMPORTANT]
> Lo que se organiza mal esta semana **no se arregla más adelante**: se arrastra. Cada
> semana siguiente añade decisiones encima del material, y reorganizar en la Semana 12
> significa tocar un proyecto que ya tiene montaje, marcadores y color. Ahora cuesta una
> tarde; entonces, tres.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los
busca carácter a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` del proyecto sigue siendo **24**
3. El bin **`01-Basicos`** tiene **15 clips o más**
4. El bin **`02-Entrevista`** tiene **al menos uno**
5. El bin **`08-Propio`** tiene **10 clips propios o más**
6. El bin **`09-Escenas`** tiene **tres subclips o más**
7. El bin **`Master`** no tiene **ningún clip suelto**

```bash
python scripts/verificar-semana.py 04
```

Con el proyecto abierto, en la raíz de tu biblioteca original, y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!NOTE]
> El check 7 cuenta solo los elementos que tienen ruta de archivo. La timeline
> `BC-Montaje-v1` no tiene ninguna, así que puede quedarse en Master sin hacer fallar
> nada. *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de 2026.*

---

## 📝 Los entregables escritos

Dos archivos, los dos en `BC-Resolve/04-respaldos/`, junto al mapa de instalación y el
plan de continuidad de la Semana 03.

### 1. `vocabulario-keywords.md` (práctica 03)

Tu lista cerrada de keywords, **quince palabras o menos**, y debajo tu código de
colores.

No es documentación por documentar: es lo que evita que dentro de un mes tengas `noche`,
`nocturno` y `de noche` etiquetando el mismo concepto, con lo que ninguna búsqueda te
devolverá el conjunto entero.

La prueba de que está bien hecho: **abre el archivo dentro de un mes, etiqueta veinte
clips nuevos siguiendo la lista, y comprueba que los smart bins de la práctica 04 los
recogen sin tocar ninguna regla.**

### 2. `notas-de-ingesta.md` (práctica 02, paso 8)

El resultado del pase de diagnóstico. Cuatro líneas bastan, y son las cuatro preguntas
que se responden ordenando por columna:

> **Frame rate.** ¿Cuántos clips no van a 24 fps, y a cuánto van?
>
> **Resolución.** ¿Cuántos no son 1920×1080, y de qué tamaño son?
>
> **Codec.** ¿Cuántos están en un codec que mi ordenador reproduce con esfuerzo?
>
> **Duración.** ¿Cuántos pasan de un minuto y van a pedir subclips?

Una respuesta buena es "tres clips a 60 fps: `plano-07`, `plano-12` y `plano-19`". Una
respuesta mala es "algunos van a otro frame rate".

Este archivo es además la **lista de trabajo de la Semana 05**, que es donde se resuelve
todo lo que aparezca aquí.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver, y que es justo la mitad del valor de la semana:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| Los clips tienen keywords, no solo una común de la tanda | Columna `Keywords` en vista de lista: la mayoría tiene dos o más |
| Las keywords salen del vocabulario escrito | Se comparan las columnas con el archivo. Ninguna palabra suelta |
| Están en minúsculas, sin acentos y en singular | Se lee la columna |
| `Description` solo donde hacía falta | Menos de la mitad de los clips la tienen |
| El código de colores está escrito | El archivo lo dice, y lo que se ve en pantalla coincide |
| Las marcas son excepciones | Si más de la mitad del bin tiene color, no informan |
| Los smart bins devuelven algo | `SB-Noche` no está vacío, y `SB-Sin-describir` casi sí |
| Los subclips son subclips | Comparten `File Path` y el tamaño en disco no ha cambiado |
| Los cortes se revisaron | Se pregunta y se responde: qué corte se borró y por qué |
| El material propio tiene segunda copia | La práctica 01 lo pide; se comprueba mirando el otro disco |

---

## 💡 Adaptación a tu pieza

**Documental corto** · Vas a acumular material durante meses, de fuentes que no se
parecen. Tu keyword más valiosa no es de contenido: es de **origen** —`camara-a`,
`archivo`, `movil`—, porque de ahí saldrán después los problemas de igualado de color.
Añade ese eje al vocabulario.

**Videoclip** · Tu material se rueda casi todo de una vez, así que las keywords de
contenido rinden poco. Lo que sí rinde es `Take` y `Good Take`: vas a tener muchas tomas
del mismo plano y necesitas encontrar la buena sin verlas todas.

**Cortometraje de ficción** · Aquí `Scene`, `Shot` y `Take` no son opcionales: son el
sistema entero. Rellénalos desde el primer día con la nomenclatura de tu guion, y el
montaje de la Semana 08 se hará solo.

**Tutorial o vídeo formativo** · Grabas pantalla y cámara, y son dos tipos de material
muy distintos. Un `01-Basicos` mezclado no te sirve: usa el clip color desde el primer
día para separar pantalla de cámara, que es la distinción que vas a hacer cien veces.

**Pieza de viaje** · Volumen alto y muchos clips parecidos. El eje que te salva es el de
**lugar**: una keyword por sitio. Y el bin `10-Descartes` te va a ahorrar más tiempo que
a nadie, porque vas a descartar mucho.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 04` en verde, siete de siete
2. `vocabulario-keywords.md` en `04-respaldos/`, con keywords y código de colores
3. `notas-de-ingesta.md` en `04-respaldos/`, con las cuatro respuestas concretas
4. Los tres smart bins creados y devolviendo lo que deben
5. `BC-Propio/` copiado a un segundo soporte, y el pack sellado con su
   `MANIFIESTO.sha256`
6. Respaldo de la semana: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana04.drp`

> [!WARNING]
> El punto 5 es el único de la lista que no se puede rehacer más tarde. Un proyecto se
> vuelve a organizar; un plano que grabaste tú y que se pierde con el disco, no. Si vas
> justo de tiempo esta semana, haz ese punto y deja para mañana cualquier otro.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Importar antes de crear los bins | Es lo que parece natural | Estructura primero: cada clip entra en su sitio y no hay que moverlo |
| Importar sin mirar qué bin está activo | El bin activo no se ve si no lo miras | Selecciona el bin, después arrastra |
| Dejar la metadata para el final de la semana | No hay recompensa inmediata, así que se pospone | Se escribe el mismo día que se importa, y por selecciones grandes |
| Un vocabulario de treinta palabras | Parece más completo | Con treinta ya estás improvisando. Quince o menos |
| Colores puestos sin decidir qué significan | La marca es rápida, la decisión no | El código va escrito antes de aplicar el primer color |
| Aceptar los cortes detectados sin revisarlos | La lista parece autoritativa | Comprueba tres o cuatro: los flashes se cuelan y los fundidos se escapan |
| Importar el material desde la carpeta de descargas | Está ahí y funciona | Se queda *offline* en cuanto ordenes el disco. Sitio definitivo primero |
| Borrar del media pool lo que no sirve | Parece limpieza | Se pierden keywords, color y comentarios. Va a `10-Descartes` |
| Saltarse la segunda copia del material propio | Cuesta dinero y tiempo | Es el único paso irreversible de la semana |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 03](../../week-03-resolve_21_anatomia_bases_de_datos_y_preferencias/3-proyecto/README.md) | **Proyecto Semana 04** | [Semana 05](../../week-05-proxies_cache_y_sincronizacion/README.md) |

← [Volver a la Semana 04](../README.md)
