# 💠 Free frente a Studio

> La versión gratuita de DaVinci Resolve no es una demo con marca de agua ni un
> programa capado a las bravas. Es un programa de post-producción completo del que se
> han quitado, casi siempre, cosas que aceleran el trabajo profesional. Se puede
> aprender post-producción entera con ella, y eso es exactamente lo que hace este
> bootcamp.

**Ningún entregable evaluable del bootcamp depende de Studio.** Cuando una semana
toca una función de pago, se explica igual —porque en un trabajo real te la vas a
encontrar— y se da la ruta alternativa en Free.

---

## 1. Cómo leer este documento

Blackmagic Design cambia el reparto entre versiones de vez en cuando. La **fuente de
verdad** es la página oficial de comparación:

<https://www.blackmagicdesign.com/products/davinciresolve/studio>

Este documento resume lo que afecta al bootcamp, con la marca de en qué semana
aparece. Si algo no coincide con tu instalación, gana tu instalación: comprueba
abriendo el panel correspondiente en Resolve y observando si el control está
atenuado o si aparece el aviso de Studio.

> [!NOTE]
> Cómo saber qué versión tienes: `Help > About DaVinci Resolve`. Si pone
> **DaVinci Resolve Studio**, tienes la de pago. Si pone solo **DaVinci Resolve**,
> tienes la gratuita, que es la que asume este bootcamp.

---

## 2. Lo que la versión gratuita hace igual de bien

Merece la pena decirlo primero, porque la lista sorprende:

- Las **siete páginas** completas: Media, Cut, Edit, Fusion, Color, Fairlight, Deliver
- El **grafo de nodos entero**: serie, paralelo, layer mixer, key mixer, outside
- **Todas las herramientas de corrección primaria**: ruedas, log wheels, curvas, offset
- **Qualifiers, power windows y tracking** de puntos
- **Gestión de color completa**: DaVinci YRGB, YRGB Color Managed y **ACES**
- **Fusion completo** en su parte de composición 2D y 3D: máscaras, paint, tracker,
  planar tracker, keying con Delta Keyer, partículas, Text3D, renderer 3D
- **Fairlight** con su mezclador, buses, EQ, dinámica y automatización
- **Multicámara**, subtítulos, versiones de timeline, intercambio XML/AAF/EDL/OTIO
- **Render hasta 4K UHD (3840×2160)** con los codecs habituales de entrega
- **Scripting desde dentro del programa**: `Workspace > Scripts` y la consola de Fusion

Con eso se hace un cortometraje, un documental, un videoclip y un canal de YouTube
entero. Lo que falta acelera; casi nunca habilita.

---

## 3. Lo que Studio añade, por dónde te lo vas a encontrar

### 🎨 Color — Semanas 16-22

| Función | Qué hace | Alternativa en Free |
| ------- | -------- | ------------------- |
| **Noise Reduction** temporal y espacial | Quita ruido de sensor conservando detalle | Grabar con menos ISO; un `Median` suave en Fusion; aceptar el ruido y no subir tanto las sombras |
| **Motion Blur** artificial | Añade desenfoque de movimiento donde no lo hay | Grabar con el obturador correcto (Semana 01) |
| **Magic Mask** y **Object Mask** | Aísla una persona u objeto automáticamente | Power windows con tracking manual y rotoscopia (Semana 19) |
| **Depth Map** | Genera un mapa de profundidad de la toma | Windows con degradado, separando por planos a mano |
| **Face Refinement** | Retoque de piel y rasgos con detección facial | Qualifier de tono de piel + window seguida + un blur muy suave |
| **Super Scale** | Escalado inteligente por encima de la resolución original | `Scale` normal, asumiendo la pérdida de nitidez |
| **HDR** (Dolby Vision, HDR10+) | Etalonaje y metadatos para entrega HDR | Trabajar y entregar en Rec.709 (Semana 22) |

### ✂️ Edit — Semanas 08-12

| Función | Qué hace | Alternativa en Free |
| ------- | -------- | ------------------- |
| **Speed Warp** | Cámara lenta generando frames nuevos con IA | `Optical Flow` estándar, que ya está en Free y da buen resultado hasta ~50 % |
| **Buena parte de ResolveFX** | Efectos como Patch Replacer, Object Removal, Beauty, Deflicker, Film Grain, Film Look Creator | Free trae un subconjunto de ResolveFX suficiente para el bootcamp; lo demás se resuelve en Fusion o no se usa |
| **Transcripción automática** de diálogo a subtítulos | Genera los subtítulos solo | Escribirlos a mano en la página Edit (Semana 12) o importar un `.srt` generado fuera |
| **Smart Reframe** | Reencuadra a vertical siguiendo la acción | Reencuadre manual con keyframes (Semana 10) |

### 🔊 Fairlight — Semanas 13-15

| Función | Qué hace | Alternativa en Free |
| ------- | -------- | ------------------- |
| **Voice Isolation** | Separa la voz del ruido de fondo | EQ paramétrico + gate + compresor (Semana 14): peor con ruido variable, suficiente para diálogo grabado con cuidado |
| **Dialogue Leveler** | Iguala el volumen del diálogo automáticamente | Compresor manual y automatización de fader (Semana 14) |
| **Music Remixer** | Separa una canción en pistas de instrumentos | No hay equivalente; se resuelve eligiendo música con stems disponibles |

### 📤 Deliver — Semanas 28-29

| Función | Qué hace | Alternativa en Free |
| ------- | -------- | ------------------- |
| **Render por encima de 4K UHD** | Salidas 8K y similares | Entregar a 3840×2160 como máximo, que cubre todas las plataformas del bootcamp |
| **Render en red** (*remote rendering*) | Repartir el render entre varias máquinas | Renderizar en la tuya |

### 👥 Colaboración y automatización — Semanas 30-34

| Función | Qué hace | Alternativa en Free |
| ------- | -------- | ------------------- |
| **Collaboration mode** multiusuario | Varias personas sobre el mismo proyecto a la vez | Pasarse el proyecto exportado como `.drp` (Semana 30) |
| **Scripting externo** | Ejecutar un script desde una terminal contra Resolve | Ejecutar el script **dentro** de Resolve (`Workspace > Scripts`), que sí funciona en Free. Es la vía que usa el verificador del bootcamp |

> [!IMPORTANT]
> **Este es el punto que más confunde.** Que el scripting externo sea de Studio no
> significa que en Free no puedas automatizar Resolve: significa que tu script tiene
> que arrancar desde el menú `Workspace > Scripts` en vez de desde una terminal. Toda
> la API de objetos —proyectos, timelines, media pool, render— es la misma. Las
> Semanas 31-34 se hacen enteras en Free.

---

## 4. Cómo está marcado en el material

Cada vez que una semana toque una función de pago, verás este bloque:

> [!IMPORTANT]
> **Studio** · `Nombre exacto de la función`.
> En Free, la ruta equivalente es *(alternativa concreta)*; el resultado es
> *(en qué se nota la diferencia)*, y es suficiente para los entregables de esta semana.

Si un ejercicio no se puede hacer en Free, **no es un entregable evaluable**: aparece
como lectura y como demostración, nunca como requisito.

---

## 5. ¿Merece la pena comprar Studio?

Depende de qué te esté costando tiempo, no de qué te falte en la lista.

Compensa si:

- Trabajas a menudo con material rodado con poca luz: la **reducción de ruido** por sí
  sola te ahorra horas.
- Haces contenido hablado y el sonido se graba en sitios ruidosos: **Voice Isolation**.
- Necesitas aislar personas del fondo con frecuencia: **Magic Mask**.
- Entregas en HDR o por encima de 4K.
- Colaboras con más gente sobre los mismos proyectos.

No compensa todavía si estás aprendiendo. **Haz el bootcamp entero en Free.** En la
Semana 22 sabrás con criterio propio si alguna de esas cinco cosas es tu cuello de
botella real, y en ese momento la decisión se toma sola.

---

## 📚 Recursos adicionales

- [Comparativa oficial DaVinci Resolve y DaVinci Resolve Studio](https://www.blackmagicdesign.com/products/davinciresolve/studio) — la tabla canónica, y la única que Blackmagic actualiza con cada versión. Cuando este documento y esa página discrepen, gana la página.
- [Foro oficial de DaVinci Resolve](https://forum.blackmagicdesign.com/) — donde se aclaran los casos límite ("¿esto concreto está en Free?") con respuestas de gente que lo ha probado en ambas versiones.

## ✅ Checklist de verificación

- [ ] Sé qué versión tengo instalada (`Help > About DaVinci Resolve`)
- [ ] Entiendo que puedo hacer el bootcamp completo en Free
- [ ] Sé que el scripting **dentro** de Resolve funciona en Free, y el externo no
- [ ] Sé reconocer el bloque de aviso de Studio en el material
- [ ] He mirado la página oficial de comparación al menos una vez

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
