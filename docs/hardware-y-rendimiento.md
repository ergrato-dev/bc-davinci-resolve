# 🖥️ Hardware y rendimiento

> Resolve no va lento porque tu ordenador sea viejo. Va lento porque le estás pidiendo
> algo concreto que tu ordenador no puede hacer. Saber cuál es ese algo cambia todo.

DaVinci Resolve es, de los programas de edición, el que más depende de la **GPU**.
Casi todo lo que ves en pantalla —la decodificación, cada nodo de color, cada efecto,
Fusion entero— se calcula en la tarjeta gráfica. Eso hace que el consejo genérico de
"cómprate más RAM" sea casi siempre el consejo equivocado.

## 1. Los cuatro cuellos de botella

Cuando la reproducción se entrecorta, la causa es **uno** de estos cuatro, y conviene
saber cuál antes de gastar dinero.

| Cuello de botella | Síntoma típico | Cómo se arregla |
| ----------------- | -------------- | --------------- |
| **GPU** | Va bien hasta que añades nodos, efectos o entras en Fusion | Menos nodos, caché, o una GPU mejor |
| **Decodificación de codec** | Va mal desde el primer clip, sin ningún efecto puesto | **Proxies u optimized media** (Semana 05) |
| **Disco** | Saltos con material 4K aunque la GPU esté ociosa | Disco más rápido, o proxies en un disco distinto |
| **VRAM** (memoria de la GPU) | Errores tipo *GPU memory full*, sobre todo con ruido y Fusion | Bajar la resolución de timeline, menos nodos simultáneos, más VRAM |

> [!IMPORTANT]
> El cuello de botella más frecuente en gente que empieza **no es la GPU**: es el
> **codec**. Un H.265 de móvil o de cámara de acción es dolorosamente caro de
> decodificar en tiempo real. La solución no es hardware, es la Semana 05.

## 2. Mínimos reales para este bootcamp

Estos son los mínimos para poder **completar los entregables**, no para trabajar
cómodo en producción profesional.

| Componente | Mínimo viable | Cómodo | Notas |
| ---------- | ------------- | ------ | ----- |
| **GPU** | 4 GB de VRAM | 8 GB o más | En Windows y Linux: NVIDIA o AMD con drivers actualizados. En Mac: Apple Silicon va bien desde el M1 |
| **RAM** | 16 GB | 32 GB | Con 8 GB Resolve arranca, pero Fusion y el ruido sufren |
| **CPU** | 4 núcleos | 8 núcleos o más | Importa menos de lo que la gente cree, salvo en decodificación por software |
| **Disco del sistema** | SSD | SSD NVMe | Resolve sobre disco mecánico es una mala experiencia desde el minuto uno |
| **Disco de medios** | SSD externo o interno | NVMe | Ver la tabla de la sección 4 |
| **Pantalla** | 1920×1080 | 2560×1440 o más | Resolve tiene mucha interfaz; por debajo de 1080p los paneles no caben |

> [!NOTE]
> **Sistemas operativos.** El bootcamp está escrito para Windows y macOS. Resolve
> también existe para Linux, pero la versión de Linux tiene requisitos de distribución
> concretos y soporta menos codecs de consumo (H.264 y H.265 de cámara doméstica dan
> problemas). Si trabajas en Linux, la Semana 05 (proxies) deja de ser opcional.

## 3. La VRAM y por qué se acaba

La **VRAM** es la memoria de la tarjeta gráfica. Es distinta de la RAM del sistema y
mucho más pequeña. Cada imagen que Resolve tiene "en vuelo" ocupa VRAM:

- Un frame de 1080p a 32 bits en coma flotante ocupa alrededor de **32 MB**.
- El mismo frame en 4K ocupa alrededor de **130 MB**.
- Y no hay un frame: hay el de entrada, el de salida y uno intermedio **por cada
  nodo** del grafo de color, más lo que consuma Fusion.

De ahí las dos reglas prácticas del bootcamp:

1. Si vas justo de VRAM, trabaja el color con la timeline en **proxy mode a media
   resolución** (`Playback > Timeline Proxy Mode > Half Resolution`). El grado es
   idéntico; solo se calcula sobre menos píxeles mientras editas.
2. Si Fusion se atasca, es casi siempre VRAM, no CPU.

## 4. Discos: la tabla que evita disgustos

El caudal que necesitas depende del codec, no de la resolución sola.

| Material | Caudal aproximado | ¿Aguanta un disco USB mecánico (~100 MB/s)? |
| -------- | ----------------- | ------------------------------------------ |
| H.264/H.265 1080p de móvil | 5-25 MB/s | Sí, de sobra |
| H.265 4K de móvil o dron | 12-50 MB/s | Sí, pero la decodificación te matará antes |
| ProRes 422 HQ 1080p | ~22 MB/s | Sí |
| ProRes 422 HQ 4K | ~90 MB/s | Justo, con un solo clip |
| DNxHR HQX 4K | ~110 MB/s | No |
| Blackmagic RAW 4K constant quality | 30-100 MB/s | Riesgo |
| Multicámara de 4 ángulos ProRes 4K | ~360 MB/s | **No** |

> [!TIP]
> Multiplica por el número de clips que suenan **a la vez**. Una multicámara de cuatro
> ángulos lee cuatro flujos simultáneos. Ese es el caso que revienta discos que iban
> bien con un solo clip.

## 5. Configuración que gana rendimiento sin gastar dinero

En este orden, y todos se explican a fondo en su semana:

1. **Optimized media y proxies** (Semana 05). El mayor salto de rendimiento del
   bootcamp, y es gratis.
2. **Render cache inteligente** (Semana 05): `Playback > Render Cache > Smart`.
   Resolve precalcula en segundo plano lo que sabe que es caro.
3. **Timeline proxy mode** (Semana 05): calcular a media resolución mientras trabajas.
4. **Caché en un disco rápido y separado** de los medios
   (`Preferences > Media Storage`).
5. **Cerrar Fusion** cuando no lo estés usando: una comp abierta sigue consumiendo VRAM.

## 6. Cómo saber qué te está frenando

Resolve trae su propio medidor. En la página **Color**, activa
`Workspace > Show Performance Metrics` para ver el reparto de tiempo por nodo, y usa
la barra de estado del *viewer*: si el indicador de frames caídos se dispara **sin
nodos**, tu problema es el codec o el disco, no la GPU.

- **GPU al 100 % y reproducción a saltos** → GPU o VRAM.
- **GPU baja, CPU al 100 %** → decodificación por software: haz proxies.
- **GPU y CPU bajas y aun así va a saltos** → disco.

## 7. Lo que no hace falta

- **Un panel de control físico.** Son cómodos y caros. Todo el bootcamp se hace con
  ratón y teclado.
- **Un monitor de referencia calibrado.** Deseable para colorear en serio, innecesario
  para aprender. La Semana 17 explica qué estás perdiendo y cómo compensarlo leyendo
  scopes en lugar de fiarte de tu pantalla.
- **Studio.** Ver [free-vs-studio.md](free-vs-studio.md).
- **Más RAM,** casi nunca, si ya tienes 16 GB.

---

## 📚 Recursos adicionales

- [Requisitos de sistema y notas de versión de DaVinci Resolve](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion) — la página de soporte de Blackmagic publica el documento de configuraciones soportadas de cada versión. Es la única fuente que se actualiza con cada release.
- [Foro oficial de DaVinci Resolve](https://forum.blackmagicdesign.com/) — la sección de hardware es donde se reportan las incompatibilidades reales de drivers, antes de que aparezcan en ninguna documentación.

## ✅ Checklist de verificación

- [ ] Sé cuánta VRAM tiene mi GPU
- [ ] Sé si mi disco de medios es SSD o mecánico, y su velocidad aproximada
- [ ] Entiendo la diferencia entre un problema de GPU y uno de decodificación de codec
- [ ] Sé activar `Workspace > Show Performance Metrics` en la página Color
- [ ] He localizado dónde se configura la caché en `Preferences > Media Storage`

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
