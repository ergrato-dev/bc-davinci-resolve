# Proyecto — Semana 03: la casa de tu proyecto

> Al terminar esta semana, tu proyecto no solo estará bien configurado: sabrás **dónde
> vive cada pieza de él** y qué harías si mañana el disco dejara de arrancar. Con esto
> se cierra la Fase 0 y el proyecto queda listo para recibir material.

## 📦 Qué añade esta semana

La tercera capa: **el entorno**.

En la Semana 01 decidiste qué pieza vas a hacer y con qué parámetros. En la 02
averiguaste qué clase de archivos va a producir y cuánto van a ocupar. Esta semana
colocas la infraestructura alrededor: dónde escribe Resolve, cómo se respalda, y qué
tendrías que rehacer si cambiaras de ordenador.

Va aquí y no en la Semana 30 —que es la de gestión y archivado— por un motivo simple:
**a partir de la Semana 04 empieza a entrar material de verdad**. Cuando haya doscientos
clips, generar la caché en el disco equivocado ya no es un ajuste, es una tarde de
mover archivos. Y el día que necesites un respaldo no es el día de empezar a hacerlos.

Con esta semana se cierra la **Fase 0**. Al terminarla, tu proyecto tiene identidad
técnica, entorno y red de seguridad, y no ha entrado todavía ni un clip de tu pieza.

---

## 📋 Requisitos verificables

Los mismos que declara `checks.json`. Los nombres son literales: el verificador los
busca carácter a carácter.

1. **`BC-Bootcamp-Resolve`** es el proyecto abierto
2. La versión de Resolve que responde es una **21**
3. `BC-Bootcamp-Resolve` aparece en la carpeta que muestra el Project Manager
4. **`BC-Pruebas-semana03`** existe en esa misma carpeta
5. El `Timeline frame rate` del proyecto sigue siendo **24**
6. El `Playback frame rate` del proyecto es **24**
7. La timeline **`BC-Montaje-v1`** sigue existiendo

```bash
python scripts/verificar-semana.py 03
```

Con el proyecto abierto, en la **raíz de tu biblioteca original**, y el puente lanzado
desde `Workspace > Scripts > Utility`.

---

## 📝 Los entregables escritos

Dos archivos, los dos en `BC-Resolve/04-respaldos/`.

### 1. `mapa-de-instalacion.md` (prácticas 01, 03 y 04)

Dónde vive cada cosa **en tu máquina**. Tiene tres partes:

| Parte | Qué lleva |
| ----- | --------- |
| **Identidad** | Sistema operativo, versión exacta de Resolve, Free o Studio |
| **Rutas** | Biblioteca de proyectos, carpeta del proyecto y tamaño de su `Project.db`, carpeta `Preferences`, carpeta de respaldos, disco de trabajo, biblioteca de pruebas |
| **Lo que no viaja** | La lista de preferencias que tendrías que rehacer a mano en otra máquina: Live Save, respaldos y sus copias, Media Storage, memoria y GPU, decodificación por hardware, layout guardado |

La prueba de que está bien hecho es esta: **si te sientas mañana en un ordenador
prestado, con este archivo dejas Resolve como lo tienes ahora en menos de quince
minutos.**

### 2. `plan-de-continuidad.md` (nuevo esta semana)

Media página, y son las cuatro preguntas que nadie se hace hasta que es tarde.
Respóndelas con acciones concretas, no con intenciones:

> **1. Se muere el disco donde está mi material.** ¿Qué pierdo y de dónde lo saco?
>
> **2. Se muere el disco del sistema.** ¿Qué pierdo? ¿Dónde está mi proyecto?
> ¿Dónde están mis preferencias?
>
> **3. Destrozo la timeline y me doy cuenta tres días después.** ¿A qué punto puedo
> volver, exactamente?
>
> **4. Tengo que terminar la pieza en otro ordenador la semana que viene.** ¿Qué me
> llevo y en qué orden lo configuro?

Una respuesta buena a la pregunta 3 es "al `.drp` de la semana pasada, en
`04-respaldos/`, más los respaldos automáticos de los últimos siete días". Una respuesta
mala es "supongo que a algún backup".

Si al responder descubres un agujero —y lo normal es descubrir al menos uno—, **arréglalo
ahora**, que es exactamente para lo que sirve el ejercicio.

---

## 🎨 Criterios de calidad

Lo que el verificador no puede ver:

| Criterio | Cómo se comprueba |
| -------- | ----------------- |
| El mapa tiene rutas reales, no descripciones | "`C:\...\Resolve Project Library`" vale; "en la carpeta de Resolve" no |
| El tamaño del `Project.db` está anotado con su cifra | Un número en MB |
| Los respaldos automáticos están fuera del disco del sistema | Se lee la ruta anotada y se compara con el disco del sistema |
| Las copias diarias conservadas son 7 o más | El número está escrito en el mapa |
| Las tres Working Folders apuntan a `02-cache/` | `Project Settings > Master Settings > Working Folders` |
| Existen `CacheClip/` y `.gallery/` en la carpeta de caché | Se miran en el explorador de archivos |
| El `.drp` de la semana se ha restaurado y abierto de verdad | El plan de continuidad lo dice, y la pregunta 3 tiene una respuesta concreta |
| El plan de continuidad responde a las cuatro preguntas con acciones | Cada respuesta nombra un archivo, una carpeta o un paso |
| Las tres funciones de Studio anotadas llevan su alternativa en Free | Se leen: "Voice Isolation — alternativa: EQ + gate + compresor" vale |

---

## 💡 Adaptación a tu pieza

**Documental corto** · Vas a acumular material de fuentes dispares durante meses, y una
parte no se puede volver a grabar. La pregunta 1 del plan de continuidad es la tuya:
decide hoy dónde vive la **segunda copia** de las entrevistas.

**Videoclip** · Tu material es reproducible salvo la música y el rodaje. Lo que no puedes
rehacer es el trabajo de sincronía. Prioriza el `.drp` semanal, y guárdalo fuera del
disco de trabajo.

**Cortometraje de ficción** · Es lo más caro de repetir de las cinco opciones: un día de
rodaje con actores no se repite. Dos discos, y uno fuera de casa.

**Tutorial o vídeo formativo** · Grabas pantalla, y eso llena el disco más rápido de lo
que parece. Tu prioridad es el paso 1 de la práctica 04: que la caché no caiga en el
disco del sistema, que suele ser el mismo donde grabas.

**Pieza de viaje** · El riesgo es el volumen y el momento: el material se graba lejos de
casa. Define hoy qué haces con las tarjetas **antes** de volver, y anótalo en la
pregunta 1.

---

## 🚦 Cómo entregarlo

1. `python scripts/verificar-semana.py 03` en verde, siete de siete
2. `mapa-de-instalacion.md` completo en `04-respaldos/`
3. `plan-de-continuidad.md` con las cuatro preguntas respondidas
4. Las tres Working Folders apuntando a `02-cache/`
5. Respaldo de la semana: `File > Export Project` →
   `04-respaldos/BC-Bootcamp-Resolve-semana03.drp`
6. **Respaldo de cierre de fase**, que es lo que hace especial a esta semana:
   `04-respaldos/BC-Bootcamp-Resolve-fase0.drp`

El punto 6 no es una copia redundante del punto 5: es el punto de retorno al que
querrás volver si dentro de tres meses decides rehacer la Fase 1 desde cero. Un `.drp`
pesa unos pocos megabytes; tener uno por fase cuesta nada y vale mucho.

---

## 🧯 Errores comunes

| Error | Por qué pasa | Solución |
| ----- | ------------ | -------- |
| Dejar el mapa a medias, con casillas vacías | Se hace al final y con prisa | Se va rellenando durante las prácticas 01, 03 y 04, no después |
| Responder el plan de continuidad con intenciones | "Debería hacer copias" suena a respuesta | Cada respuesta nombra un archivo o una carpeta que existe hoy |
| Configurar los respaldos y no comprobar nunca que funcionan | Marcar una casilla parece suficiente | La práctica 03 te hace restaurar el `.drp` de verdad. Hazlo |
| Quedarse trabajando en `BC-Pruebas-DB` | Se cambia de biblioteca y se olvida volver | Los checks fallan en bloque: es la primera causa a descartar |
| Poner las Working Folders en un disco de red o en un USB lento | Parece que ahorra espacio en el disco bueno | La caché existe para ir rápido; en un disco lento estorba más de lo que ayuda |
| Hacer un *Project Archive* cada semana | Se confunde con el `.drp` | El `.dra` copia todos los medios. Se hace al cerrar un trabajo, no cada viernes |
| Cerrar la fase sin el `.drp` de fase | Parece redundante con el semanal | En tres meses no lo parecerá |

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Semana 02](../../week-02-codecs_contenedores_y_flujo_de_datos/3-proyecto/README.md) | **Proyecto Semana 03** | [Semana 04](../../week-04-media_page_ingesta_y_organizacion/README.md) |

← [Volver a la Semana 03](../README.md)
