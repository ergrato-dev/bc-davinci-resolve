# Proyecto — Semana 05: el material se vuelve manejable

> La semana pasada el material entró. Esta semana se vuelve **trabajable**: reproduce
> fluido, está acotado en trozos útiles, la imagen y el sonido de dos aparatos van
> pegados, y sabes qué hacer el día que todo aparezca en rojo. Con esto se cierra la Fase
> 1 y el proyecto queda listo para montar.

## 📦 Qué añade esta semana

La quinta capa: **el material preparado**.

Hasta ahora tu proyecto tenía identidad técnica (Fase 0) y material organizado (Semana
04). Le faltaba lo que separa un archivo de un material montable: que se pueda reproducir
sin pelearse, que lo bueno esté acotado, y que el sonido bueno esté pegado a la imagen.

Es la última semana antes de la Cut page. A partir de la Semana 06 se monta, y se monta
con lo que dejes aquí.

> [!IMPORTANT]
> Esta semana es la única del bootcamp que trata de **rendimiento**, y eso tiene una
> consecuencia práctica: lo que configures aquí lo vas a arrastrar treinta y una semanas.
> Un ajuste de optimizados a resolución completa que te llene el disco en la Semana 12
> significa parar el bootcamp para hacer sitio. Elige pensando en septiembre, no en el
> lunes que viene.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los busca
carácter a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. El `Timeline frame rate` del proyecto sigue siendo **24**
3. El bin **`03-Multicamara`** tiene **tres clips o más**
4. Existe la timeline **`BC-Sync-v1`**
5. **`BC-Sync-v1`** está abierta y tiene **dos pistas de audio o más**
6. El bin **`11-Subclips`** tiene **cinco subclips o más**
7. El bin **`Master`** no tiene **ningún clip suelto**

```bash
python scripts/verificar-semana.py 05
```

Con el proyecto abierto, en la raíz de tu biblioteca original, y el puente lanzado desde
`Workspace > Scripts > Utility`.

> [!NOTE]
> El check 5 usa `timeline_probe`, que lee **la timeline activa**. Abre `BC-Sync-v1` con
> doble clic antes de verificar o fallará aunque esté perfecta. *Comportamiento verificado
> por la API de scripting en 21.0.4.5, agosto de 2026.*

---

## 📝 Los entregables escritos

Uno nuevo, y uno de la semana pasada que se actualiza.

### 1. `rendimiento.md` (práctica 01, paso 8; práctica 02, paso 8)

En `BC-Resolve/04-respaldos/`, junto a `vocabulario-keywords.md` y `notas-de-ingesta.md`.

Cinco líneas, todas con un número:

> **Cuello de botella**: cuál de los tres, con los fps medidos en las tres pruebas.
>
> **Ajustes elegidos**: resolución y formato de optimizados, de proxies y de caché.
>
> **Ganancia medida**: fps con optimizados activados y desactivados.
>
> **Coste en disco**: gigabytes por minuto de material, y tamaño de la carpeta de trabajo.
>
> **Decisión**: optimizados, proxies, o los dos, y por qué.

No es documentación por documentar: es lo que te permite, en la Semana 22 con material
RAW, decidir en dos minutos en vez de en una tarde. Y es lo que te dirá si tu disco
aguanta el bootcamp entero antes de que se llene.

Una línea buena es "con optimizados a un cuarto paso de 14 a 24 fps y me cuesta 0,3 GB por
minuto". Una línea mala es "va bastante mejor".

### 2. `notas-de-ingesta.md`, actualizado (práctica 03, paso 6)

El archivo de la Semana 04 sigue vivo. Esta semana se le añaden dos cosas:

- Qué material de `SB-Revisar` ha quedado resuelto con optimizados o proxies.
- Qué material tiene **deriva de sincronía**, si lo has encontrado, y cuál es su frame
  rate o su frecuencia de muestreo real.

Lo segundo es material para la Semana 12 y para la 14: apuntarlo ahora es lo que evita
descubrirlo montando.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver, y que es la mitad del valor de la semana:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| El diagnóstico se hizo antes de generar | `rendimiento.md` tiene los tres números de fps del paso 2 |
| Se optimizó lo problemático, no todo | La columna de optimizado en vista de lista: `SB-Revisar` sí, el resto no |
| La ganancia está medida, no supuesta | Dos cifras de fps distintas en `rendimiento.md` |
| Los proxies del material propio existen | `Playback > Proxy Handling` cambia el contador de fps |
| La caché quedó en un modo sensato | `Playback > Render Cache` en `Smart` |
| El disco está bajo control | Espacio libre anotado, y sigue habiendo margen |
| La sincronía está comprobada al fotograma | Se pregunta: ¿en qué consonante lo comprobaste? |
| El audio de referencia se conservó | `BC-Sync-v1` tiene dos pistas y la de cámara está silenciada |
| El multicámara no deja saltar el audio | Se cambia de ángulo reproduciendo: la voz no salta |
| Los subclips tienen colas | Se extiende uno en la timeline: hay material a ambos lados |
| Los subclips se llaman algo | Ningún nombre acaba en `_subclip_4` |
| El relink se practicó de verdad | Se pregunta: ¿qué pasó con el archivo renombrado del paso 10? |

---

## 💡 Adaptación a tu pieza

**Documental corto** · Vas a acumular material durante meses y de fuentes distintas.
Configura los proxies **hoy** y genera cada tanda al ingestarla; si lo dejas para cuando
haya doscientos clips, es una noche entera de generación. Y tu entrevista larga es el caso
de libro de los subclips: una respuesta, un subclip.

**Videoclip** · Tu cuello no será el codec sino los efectos, porque el ritmo te va a pedir
velocidades y transformaciones. La caché de render en modo `User` es tu herramienta
principal. Los subclips te sirven para acotar las tomas buenas del playback.

**Cortometraje de ficción** · Si has rodado con sonido aparte, la práctica 03 es tu semana
entera: sincroniza **todas** las tomas ahora, no según las vayas montando. Y nombra los
subclips con la nomenclatura del guion: escena, plano, toma.

**Tutorial o vídeo formativo** · Grabación de pantalla y cámara son el par de doble
sistema más común que existe, aunque no lo parezca. Sincronízalos como tal. La captura de
pantalla suele ser el archivo más pesado y el que más pide proxies.

**Pieza de viaje** · Volumen alto y clips largos de los que solo valen segundos. Los
subclips son tu herramienta más rentable de la semana: acota primero, monta después, y no
vuelvas a abrir el clip de once minutos nunca más.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 05` en verde, siete de siete
2. `rendimiento.md` en `04-respaldos/`, con las cinco líneas y sus cifras
3. `notas-de-ingesta.md` actualizado con lo resuelto y con la deriva encontrada
4. Medios optimizados generados para el material de `SB-Revisar`
5. Proxies generados para `08-Propio`
6. `Playback > Render Cache` en `Smart` y la caché no usada borrada
7. Respaldo de la semana: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana05.drp`

> [!TIP]
> Si vas justo de tiempo, prioriza la práctica 03. La sincronización es la única de las
> cuatro que **no se puede hacer más tarde sin coste**: si montas material sin sincronizar
> en las Semanas 06 a 08, rehacerlo significa rehacer el montaje. Lo demás —optimizados,
> caché, subclips— se puede añadir cualquier lunes.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Generar optimizados de todo el media pool | Parece más completo | Solo lo de `SB-Revisar`. El resto ya iba fluido |
| Generar sin medir antes | No hay recompensa visible en medir | Tres pruebas de un minuto, y sabes qué generar |
| Optimizados a resolución completa | "Por calidad" | Un gigabyte por minuto. A un cuarto, salvo que etalones sobre ellos |
| Cachear mientras aún experimentas | La caché parece gratis | Cada cambio la invalida. Cachea lo cerrado |
| Sincronizar en la timeline en vez del media pool | Es donde estás mirando | En el media pool, antes de montar |
| Sustituir el audio de cámara | Parece más limpio | Consérvalo silenciado: es tu referencia si algo se tuerce |
| Dejar que el audio siga al ángulo activo | Es la opción que suena bien de nombre | Fíjalo en el micrófono bueno |
| Subclips ajustados al fotograma | Se quiere "solo lo bueno" | Un segundo de cola a cada lado. Semana 09 te lo agradecerá |
| Probar el relink en el proyecto del bootcamp | Da pereza crear otro | Proyecto de pruebas. Siempre |
| Renombrar archivos después de importar | Se quiere ordenar tarde | Renombrar antes de importar, nunca después |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 04](../../week-04-media_page_ingesta_y_organizacion/3-proyecto/README.md) | **Proyecto Semana 05** | [Semana 06](../../week-06-cut_page_edicion_veloz/README.md) |

← [Volver a la Semana 05](../README.md)
