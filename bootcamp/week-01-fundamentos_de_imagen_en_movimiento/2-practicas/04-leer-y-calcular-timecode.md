# Práctica 04 — Leer y calcular timecode

> Al terminar sabrás convertir entre timecode, frames y segundos sin dudar, y tendrás
> creada la timeline `BC-Montaje-v1` donde vivirá tu pieza durante 36 semanas.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 02](02-crear-el-proyecto-del-bootcamp.md), [Teoría 06](../1-teoria/06-timecode.md)

## Contexto

El timecode es la única forma exacta de señalar un frame. Vas a usarlo para dar notas,
para sincronizar, para automatizar en la Semana 33 y para hablar con cualquier otra
persona que trabaje con vídeo.

Esta práctica tiene dos mitades: primero calculas con papel y lápiz, después creas la
timeline del proyecto y compruebas los cálculos contra Resolve.

Trabajas sobre `BC-Bootcamp-Resolve`, a **24 fps**.

---

## Paso 1: Convertir timecode a frames

**Por qué**: es la conversión que hace el verificador, la que hacen los scripts de la
Semana 33 y la que necesitas cuando alguien te da una nota y tú trabajas en frames.

La fórmula, a 24 fps:

```
frames = (horas × 3600 + minutos × 60 + segundos) × 24 + campo de frames
```

Resuelve estos cuatro, **a 24 fps**:

| # | Timecode | Frames |
| - | -------- | ------ |
| 1 | `00:00:01:00` | ? |
| 2 | `00:00:10:12` | ? |
| 3 | `00:01:30:12` | ? |
| 4 | `01:00:00:00` | ? |

<details>
<summary>📝 Respuestas</summary>

1. `00:00:01:00` → 1 × 24 = **24 frames**
2. `00:00:10:12` → 10 × 24 + 12 = **252 frames**
3. `00:01:30:12` → (60 + 30) × 24 + 12 = 2160 + 12 = **2172 frames**
4. `01:00:00:00` → 3600 × 24 = **86 400 frames**

El cuarto es el que conviene recordar: **una hora a 24 fps son 86 400 frames**. Es el
desplazamiento que verás en cualquier timeline que empiece en `01:00:00:00`.

</details>

**Verifica**: los cuatro resultados coinciden. Si alguno falla, revisa si estás usando
60 en el campo de frames en lugar de 24.

---

## Paso 2: Convertir al revés

**Por qué**: cuando un script te devuelva `duration_frames`, tendrás que traducirlo a
algo que un humano entienda.

| # | Frames a 24 fps | Timecode | Segundos |
| - | --------------- | -------- | -------- |
| 1 | 48 | ? | ? |
| 2 | 1000 | ? | ? |
| 3 | 86 412 | ? | ? |

<details>
<summary>📝 Respuestas</summary>

1. 48 ÷ 24 = 2 s exactos → `00:00:02:00`, **2 s**
2. 1000 ÷ 24 = 41,67 s → 41 s y 16 frames → `00:00:41:16`, **41,67 s**
3. 86 412 − 86 400 = 12 frames sobre una hora → `01:00:00:12`, **3600,5 s**

</details>

**Verifica**: los tres coinciden.

---

## Paso 3: El mismo timecode en otra cadencia

**Por qué**: es el error más común al automatizar. Un timecode no significa nada sin su
frame rate.

`00:00:10:12` a distintas cadencias:

| Frame rate | Frames totales | Segundos |
| ---------- | -------------- | -------- |
| 24 fps | ? | ? |
| 25 fps | ? | ? |
| 30 fps | ? | ? |

<details>
<summary>📝 Respuestas</summary>

| Frame rate | Frames totales | Segundos |
| ---------- | -------------- | -------- |
| 24 fps | 10 × 24 + 12 = **252** | 10,50 s |
| 25 fps | 10 × 25 + 12 = **262** | 10,48 s |
| 30 fps | 10 × 30 + 12 = **312** | 10,40 s |

El mismo timecode apunta a **tres frames distintos** y a **tres instantes distintos**.
Y una pregunta más: ¿es `00:00:10:26` un timecode válido? Solo a 30 fps o más. A 24 y a
25 es imposible, porque el campo de frames no llega a 26.

</details>

**Verifica**: entiendes por qué anotar un timecode sin decir la cadencia es información
incompleta.

---

## Paso 4: Crear la timeline del proyecto

**Por qué**: es donde vivirá tu pieza durante 36 semanas. El nombre importa: el
verificador la busca por su nombre exacto.

Con `BC-Bootcamp-Resolve` abierto, ve a la página **Edit** (`Shift+4`) y usa
`File > New Timeline` — atajo `Ctrl+N` (Win) / `Cmd+N` (Mac).

En el cuadro de diálogo:

| Campo | Valor |
| ----- | ----- |
| `Timeline Name` | **BC-Montaje-v1** |
| `Start Timecode` | `01:00:00:00` |
| `No. of Video Tracks` | 1 |
| `No. of Audio Tracks` | 1 |
| `Use Project Settings` | **activado** |

Dejar `Use Project Settings` activado es lo que hace que la timeline herede los 24 fps y
los 1920×1080 que configuraste en la práctica 02. Si lo desactivas, aparece una pestaña
de ajustes propios y puedes desviarte de la configuración del proyecto sin querer.

**Verifica**:

```bash
python scripts/verificar-semana.py 01 --check timeline-existe
```

---

## Paso 5: Comprobar tus cálculos contra Resolve

**Por qué**: hasta ahora has calculado en papel. Ahora compruebas que el programa hace
exactamente lo mismo.

Con la timeline `BC-Montaje-v1` abierta:

1. Mira el contador de timecode encima del viewer de timeline. Debe marcar
   `01:00:00:00`.
2. **Clic derecho sobre ese contador** y cambia a número de frames. Debe marcar
   **86 400**, exactamente lo que calculaste en el paso 1.
3. Vuelve a timecode con otro clic derecho.
4. Con la timeline enfocada, **escribe `+240` y pulsa `Enter`**. El cursor avanza 240
   frames: 10 segundos exactos a 24 fps. El contador debe marcar `01:00:10:00`.
5. Escribe `-12` y `Enter`. Debe marcar `01:00:09:12`.
6. Escribe `01:00:00:00` y `Enter` para volver al inicio.

**Verifica**: los cuatro valores del contador coinciden con lo que has calculado.

> [!TIP]
> Escribir el timecode directamente, sin abrir ningún diálogo, es el atajo que más vas a
> usar a partir de la Semana 08. Los saltos relativos con `+` y `−` también funcionan.

---

## Paso 6: Confirmar la semana entera

**Por qué**: es el momento de comprobar que los ocho checks de la Semana 01 pasan antes
de pasar al proyecto.

```bash
python scripts/verificar-semana.py 01
```

**Verifica**: salida en verde, ocho de ocho.

---

## ✅ Resultado

- [ ] Convierto timecode a frames sin ayuda
- [ ] Convierto frames a timecode y a segundos
- [ ] Sé que una hora a 24 fps son 86 400 frames
- [ ] Entiendo por qué el mismo timecode apunta a instantes distintos según la cadencia
- [ ] Timeline `BC-Montaje-v1` creada, a 24 fps, empezando en `01:00:00:00`
- [ ] Sé alternar el contador entre timecode y frames
- [ ] Sé saltar a un timecode y hacer saltos relativos con `+` y `−`
- [ ] `verificar-semana.py 01` pasa los ocho checks

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `timeline-existe` falla | El nombre no coincide carácter a carácter | Clic derecho sobre la timeline en el media pool > Rename Timeline |
| `timeline-activa` falla | La timeline existe pero hay otra abierta | Haz doble clic en `BC-Montaje-v1` en el media pool para activarla |
| `timeline-frame-rate` devuelve algo distinto de 24 | Creaste la timeline con `Use Project Settings` desactivado | Bórrala y créala de nuevo con la casilla activada |
| El contador no cambia a frames con clic derecho | Estás sobre el viewer de origen, no el de timeline | Usa el contador del viewer de la derecha |
| Escribir el timecode no salta a ningún sitio | El foco no está en la timeline | Haz clic en la timeline y vuelve a escribirlo |
| El contador empieza en `00:00:00:00` y no en `01:00:00:00` | Dejaste el `Start Timecode` por defecto | Clic derecho en el media pool > Timelines > Starting Timecode |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Recorrido por las siete páginas](03-recorrido-por-las-siete-paginas.md) | **04 · Leer y calcular timecode** | — |

← [Volver a la Semana 01](../README.md)
