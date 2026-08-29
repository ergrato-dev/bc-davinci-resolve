# 📊 Rúbrica de evaluación — Semana 05

Tres evidencias, con un **mínimo del 70 % en cada una**. Sacar un 95 % en dos y un 40 % en
la tercera no aprueba la semana.

| Evidencia | Peso | Quién corrige |
| --------- | ---- | ------------- |
| 🧠 Conocimiento | 30 % | Tú, con el cuestionario de abajo |
| 💪 Desempeño | 40 % | `python scripts/verificar-semana.py 05` |
| 📦 Producto | 30 % | Tú, con los criterios observables |

---

## 🧠 Conocimiento (30 %)

Diez preguntas, 10 puntos cada una. Respóndelas **antes** de mirar las respuestas.

1. Explica por qué un H.264 de móvil se reproduce sin problemas en el móvil y a saltos en
   Resolve. Usa las palabras *long-GOP*, *intra-frame* y *GOP*.
2. Nombra los tres cuellos de botella de la reproducción, su síntoma característico y la
   herramienta de esta semana que arregla cada uno.
3. Diferencia un medio optimizado de un proxy: dónde vive cada uno, quién lo gestiona y
   cuál de los dos viaja a otro equipo.
4. ¿Qué guarda exactamente la caché de render, y por qué no sirve para arreglar un codec
   pesado?
5. Explica por qué la caché se invalida sola y qué consecuencia práctica tiene eso sobre
   *cuándo* conviene cachear.
6. ¿Qué hay dentro de la carpeta de trabajo de Resolve? ¿Qué se pierde si la borras entera
   con el programa cerrado?
7. Diferencia sincronizar por timecode de sincronizar por forma de onda: qué necesita cada
   método y cuándo no puede funcionar.
8. Un clip cuadra al principio y va desplazado al final. ¿Cómo se llama eso, cuáles son
   sus dos causas habituales y qué se puede hacer con material ya grabado?
9. ¿Por qué un subclip no ocupa espacio en disco? ¿Qué son las colas y por qué se dejan?
10. Un proyecto abre con toda la timeline en rojo. Enumera las cinco causas posibles en
    orden de frecuencia, di qué se ha perdido y explica por qué el relink no arregla un
    archivo renombrado.

<details>
<summary>📝 Respuestas</summary>

**1.** H.264 es un codec **long-GOP**: guarda un fotograma completo cada cierto número de
fotogramas y, entre medias, solo las diferencias. El **GOP** es el bloque que va de un
fotograma completo al siguiente. Para mostrar un fotograma cualquiera hay que reconstruir
toda la cadena desde el último completo: diez o quince descompresiones para una imagen.

Un codec **intra-frame** guarda cada fotograma entero y por su cuenta: para mostrar el
1.000 se lee el 1.000. Ocupa mucho más y se descomprime casi sin coste.

El móvil puede porque tiene un circuito dedicado a ese codec y porque solo reproduce hacia
delante, sin efectos. Montar pide saltar, ir hacia atrás y calcular encima.

**2.**

| Cuello | Síntoma | Solución |
| ------ | ------- | -------- |
| Descompresión | Va mal desde el primer día, sin efectos | Medios optimizados o proxies |
| Disco | Un clip va bien, cuatro pistas van mal | Proxies |
| Efectos | Empezó a ir mal al añadir una corrección | Caché de render |

**3.** El **optimizado** vive en la carpeta de caché de Resolve, con nombres internos, y
lo gestiona el programa entero: cero trabajo, cero control. El **proxy** vive en una
carpeta que eliges tú, se puede generar con otra herramienta y se vincula con
`Link Proxy Media`.

El que viaja es el **proxy**: se copia a otro equipo y se vincula allí. El optimizado hay
que regenerarlo.

**4.** Guarda **el resultado ya calculado** de un tramo de la timeline: el clip con sus
efectos, su color y su composición de pistas, escrito en disco como vídeo.

No arregla un codec pesado porque el problema entonces está en el primer eslabón de la
cadena —descomprimir el clip—, y la caché guarda la salida del último. Si el clip solo,
sin efectos, ya va a saltos, tocan optimizados o proxies.

**5.** Se invalida porque el resultado guardado depende de la cadena entera: si cambias la
corrección, el efecto o la posición del clip, lo cacheado ya no es el resultado correcto y
Resolve lo descarta.

La consecuencia práctica: **cachear lo que aún estás decidiendo es tirar tiempo**. Cada
retoque manda a la basura lo generado. Se cachea lo cerrado.

**6.** Tres inquilinos: la **caché de render**, los **medios optimizados** y los
**proxies generados por Resolve**.

Si la borras entera con el programa cerrado, **no pierdes nada de tu trabajo**: los
cortes, los grados, la metadata y las timelines viven en la base de datos del proyecto.
Pierdes el tiempo de regenerarlo. Eso vale para la carpeta de trabajo y **solo** para
ella: la del material y la biblioteca de proyectos son otra cosa.

**7.** El **timecode** es la marca de tiempo que cada aparato escribe al grabar. Sincroniza
alineando las marcas iguales: es instantáneo, exacto, y funciona aunque no haya sonido. Su
condición es que **los relojes se igualaran antes de grabar**, y eso no se puede arreglar
después.

La **forma de onda** compara los dibujos del sonido y busca el desplazamiento donde
encajan. No necesita preparación, y sí necesita que los dos archivos tengan audio y que
ese audio se parezca. No funciona si la cámara no grabó sonido o si lo que grabó es
irreconocible.

**8.** Se llama **deriva**. Sus dos causas: **frecuencias de muestreo distintas** (48 kHz
frente a 44,1 kHz) y **frame rates casi iguales pero no iguales** (24 frente a 23,976 fps,
que se separan un fotograma cada 42 segundos aproximadamente).

Con material ya grabado no se arregla de raíz: se **parte la escena en subclips cortos** y
se sincroniza cada trozo por su cuenta. La solución de fondo es anterior al rodaje: 48 kHz
en todo y un solo frame rate.

**9.** Porque no es un archivo: es una **referencia** al mismo archivo del disco con dos
números más, el punto de entrada y el de salida. Veinte subclips de un archivo de 5 GB
siguen siendo 5 GB.

Las **colas** (*handles*) son los fotogramas que quedan fuera de esos dos puntos y que
siguen existiendo en el archivo. Se dejan uno o dos segundos a cada lado porque sin margen
no se puede hacer una transición ni ajustar un corte más tarde.

**10.** En orden de frecuencia: carpeta movida o renombrada; disco externo desconectado;
archivos sueltos renombrados; carpeta sincronizada en la nube que descarga bajo demanda;
proyecto abierto en otro equipo.

**No se ha perdido nada**: cortes, duraciones, grados, efectos y metadata están en el
proyecto. Se ha roto un enlace.

El relink **busca por nombre de archivo** dentro de la carpeta que le señalas. Si moviste
la carpeta, los nombres siguen siendo los mismos y reenlaza todo de una pasada; si
renombraste los archivos, no hay nada que encontrar y hay que devolverles el nombre o
reenlazar a mano, uno a uno.

</details>

**Puntuación**: 10 puntos por respuesta correcta. Necesitas **70 / 100**.

---

## 💪 Desempeño (40 %)

Lo verifica el script. Cada check vale **14,29 puntos**.

```bash
python scripts/verificar-semana.py 05
```

| Práctica | Check | Puntos |
| -------- | ----- | ------ |
| 03 | `proyecto-abierto` | 14,29 |
| 03 | `frame-rate-bloqueado` | 14,29 |
| 03 | `bin-multicamara` | 14,29 |
| 03 | `timeline-sync-existe` | 14,29 |
| 03 | `timeline-sync-audio` | 14,29 |
| 04 | `bin-subclips` | 14,29 |
| 04 | `master-limpio` | 14,29 |

**Necesitas 70 / 100**, es decir **al menos 5 de los 7 checks**.

> [!TIP]
> El check que más falla esta semana es `timeline-sync-audio`, y casi nunca por el trabajo:
> lee **la timeline activa**, así que si tienes abierta `BC-Montaje-v1` falla aunque
> `BC-Sync-v1` sea perfecta. Ábrela con doble clic y repite.
>
> Si fallan **todos**, o el puente no está lanzado, o te quedaste en
> `BC-Pruebas-semana05` después del simulacro de relink.

---

## 📦 Producto (30 %)

Tu material preparado para montar. Se evalúa con criterios observables.

### Verificable a simple vista (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| `rendimiento.md` existe en `04-respaldos/` | 5 |
| Tiene los tres números de fps del diagnóstico | 10 |
| Tiene los ajustes elegidos de optimizados, proxies y caché | 5 |
| Tiene la ganancia medida: fps con y sin optimizados | 10 |
| Tiene el coste en disco, en gigabytes por minuto | 5 |
| `notas-de-ingesta.md` actualizado con lo resuelto y con la deriva encontrada | 5 |
| Los clips de `SB-Revisar` aparecen marcados como optimizados en vista de lista | 5 |
| `BC-Bootcamp-Resolve-semana05.drp` existe en `04-respaldos/` | 5 |

### Calidad de las decisiones (50 puntos)

| Criterio | Puntos |
| -------- | ------ |
| Se optimizó el material problemático, no el media pool entero | 10 |
| La resolución elegida es coherente con el espacio libre que tienes | 5 |
| `08-Propio` tiene proxies y se nota al cambiar `Proxy Handling` | 5 |
| La caché quedó en `Smart` y la no usada, borrada | 5 |
| La sincronía se comprobó al fotograma, en una consonante explosiva | 10 |
| El audio de cámara se conservó como referencia, silenciado | 5 |
| El multicámara tiene la fuente de audio fija en un ángulo | 5 |
| Los cinco subclips tienen nombre propio y colas de un segundo | 5 |

### Comprobaciones observables en Resolve

Estas no las ve el verificador, pero se leen en un minuto:

| Qué mirar | Qué debe decir |
| --------- | -------------- |
| `Playback > Use Optimized Media if Available`, activando y desactivando | El contador de fps cambia |
| `Playback > Proxy Handling`, cambiando de opción sobre `08-Propio` | El contador de fps cambia |
| `Playback > Render Cache` | Está en `Smart` |
| La franja de caché bajo la regla de tiempo | Refleja el estado de los tramos, y no está toda cacheada |
| `BC-Sync-v1`, cabeceras de pista | Dos pistas de audio, la de cámara silenciada |
| El clip multicámara, cambiando de ángulo al reproducir | La voz no salta ni cambia de sala |
| `11-Subclips` en vista de lista, columna `File Path` | Todos comparten ruta, con duraciones distintas |
| Tamaño de la carpeta de material antes y después de los subclips | No ha cambiado |
| Espacio libre del disco de la *Working Folder* | Sigue habiendo margen para seguir el bootcamp |

### Penalizaciones

| Motivo | Puntos |
| ------ | ------ |
| Se generaron optimizados de todo el media pool sin diagnóstico previo | −15 |
| El disco quedó por debajo del tamaño del material en espacio libre | −15 |
| El simulacro de relink se hizo sobre `BC-Bootcamp-Resolve` | −10 |
| Los subclips no tienen colas: empiezan y acaban justo en la frase | −10 |
| Los subclips conservan los nombres automáticos | −10 |
| El audio de cámara se sustituyó en vez de conservarse | −5 |
| El multicámara deja que el audio siga al ángulo activo | −10 |
| `rendimiento.md` describe con adjetivos y no con cifras | −10 |
| Hay clips sueltos en `Master` | −5 |

**Necesitas 70 / 100.**

---

## 📈 Nota final

```
nota = conocimiento × 0.30 + desempeño × 0.40 + producto × 0.30
```

Con el requisito adicional de **70 mínimo en cada uno de los tres**.

---

## 🔁 Si no llegas

No pases a la Semana 06 sin haber cerrado esta. La Cut page monta a velocidad alta, y
montar a velocidad alta con material que se reproduce a saltos es imposible: la semana
entera se convierte en esperar al programa.

- **Si falla `timeline-sync-audio`**: abre `BC-Sync-v1` y repite. Es lo primero que hay que
  descartar, siempre.
- **Si falla un check de bin**: es el nombre. `03-Multicamara` sin tilde, `11-Subclips` con
  los dos dígitos, y los dos colgando de `Master`.
- **Si fallan todos**: puente sin lanzar, o sigues en `BC-Pruebas-semana05`.
- **Si el cuestionario va por debajo de 70**: las preguntas 4, 5 y 8 son las que más gente
  falla. Vuelve a las teorías 04 y 06.
- **Si el producto va por debajo de 70**: casi siempre es que se generó sin medir. Repite
  el paso 2 de la práctica 01 —tres minutos— y escribe las cifras reales en
  `rendimiento.md`.
- **Si te faltó tiempo**: prioriza la práctica 03. La sincronización es lo único que se
  vuelve caro de arreglar en cuanto empieces a montar.

---

← [Volver a la Semana 05](README.md)
