# Práctica 04 — Medir el flujo de datos

> Al terminar sabrás a qué velocidad va tu disco de verdad, cuánto espacio te va a pedir
> el bootcamp entero, y tendrás Resolve configurado para escribir la caché donde tú
> quieres y no donde le toque.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-el-banco-de-formatos.md), [Teoría 08](../1-teoria/08-flujo-de-datos.md)

## Contexto

De los tres recursos que agota un proyecto de vídeo —procesador, memoria y disco— el
disco es el único que se puede calcular con exactitud por adelantado. Es también el que
más veces para el trabajo, porque cuando se llena no hay degradación progresiva: Resolve
simplemente deja de escribir.

Esta práctica convierte "creo que tengo sitio" en dos números concretos: cuántos MB/s
entrega tu disco y cuántos GB vas a necesitar.

---

## Paso 1: Medir la velocidad real de tu disco

**Por qué**: la velocidad que anuncia el fabricante es la del mejor caso. La que importa
es la que consigues tú, con tu cable, tu puerto y tu sistema de archivos.

El método más honesto es cronometrar una copia real:

1. Busca un archivo de al menos **1 GB** (un vídeo del pack sirve)
2. Cópialo dentro del mismo disco de trabajo, a otra carpeta
3. Cronometra cuánto tarda

```
velocidad (MB/s) = tamaño en MB ÷ segundos
```

Un archivo de 1200 MB copiado en 8 segundos son 150 MB/s.

> [!NOTE]
> Copiar dentro del mismo disco lee y escribe a la vez, así que el número que sale es
> **conservador**: tu disco lee algo más rápido de lo que este método indica. Para lo que
> hace falta decidir aquí, sobra con eso.

Compara con la tabla de la [teoría 08](../1-teoria/08-flujo-de-datos.md):

| Resultado | Qué significa |
| --------- | ------------- |
| Menos de 80 MB/s | Disco mecánico o conexión lenta. Vas a necesitar proxies desde la Semana 05 |
| 80-200 MB/s | Disco mecánico decente. Suficiente para material de móvil |
| 200-600 MB/s | SSD SATA. Cómodo para todo el bootcamp |
| Más de 600 MB/s | NVMe. Sin preocupaciones |

**Verifica**: tienes un número en MB/s anotado.

---

## Paso 2: Calcular lo que ocupa tu material

**Por qué**: es la mitad del presupuesto de disco, y sale de tu propio material, no de una
tabla genérica.

Coge `BC-formato-h264.mp4` y calcula, con las fórmulas de la teoría 08:

```
bitrate (Mbps) = tamaño en MB × 8 ÷ duración en segundos
GB por hora    ≈ bitrate en Mbps ÷ 2
```

Después, estima cuántas horas vas a grabar para tu pieza. Para un documental corto de 5-8
minutos, una regla razonable es **entre 10 y 20 minutos de material por minuto de pieza
final**. Con 6 minutos de pieza, eso son entre 1 y 2 horas de grabación.

**Verifica**: tienes escrito cuántos GB ocupará tu material propio.

---

## Paso 3: Sumar el presupuesto completo

**Por qué**: el material original es la parte pequeña. Lo que llena el disco es todo lo
demás, y es precisamente lo que nadie cuenta hasta que se queda sin sitio.

Rellena esta tabla con **tus** números:

```markdown
| Concepto | Cómo se calcula | GB |
| -------- | --------------- | -- |
| Pack de medios común | descargado, mídelo | |
| Material propio | horas × GB por hora (paso 2) | |
| Optimized media y proxies | material propio × 6 | |
| Render cache | 20-50 GB, según cuánto uses | |
| Entregas (Semanas 28-29) | ~10 GB | |
| Respaldos .drp | despreciable | ~0 |
| **Total** | | |
```

**Verifica**: tienes un total, y sabes si tu disco lo aguanta. Si no lo aguanta, ahora lo
sabes con siete meses de margen para resolverlo.

---

## Paso 4: Decirle a Resolve dónde escribir

**Por qué**: por defecto, Resolve escribe la caché donde le indique la configuración de tu
máquina, que puede ser el disco del sistema. La caché crece sola, sin avisar, y llenar el
disco del sistema operativo es un problema mayor que llenar cualquier otro.

**Primero, la preferencia de tu máquina:**

`DaVinci Resolve > Preferences > System > Media Storage`

Ahí está la lista de discos de trabajo. El **primero de la lista** es donde Resolve
escribe por defecto. Comprueba que apunta a tu disco de trabajo, no al del sistema.

> [!IMPORTANT]
> `Media Storage` es una preferencia de **tu ordenador**, no del proyecto: no viaja con el
> `.drp`. Si algún día abres el proyecto en otra máquina, hay que revisarla allí.

**Después, la carpeta de este proyecto:**

`File > Project Settings > Master Settings > Working Folders`

| Campo | Ponlo en |
| ----- | -------- |
| `Cache files location` | `BC-Resolve/02-cache/` |
| `Gallery stills location` | `BC-Resolve/02-cache/` (o donde prefieras; ocupa poco) |

**Verifica**: los dos campos apuntan a rutas tuyas, y las carpetas existen en el disco.

---

## Paso 5: Saber vaciar la caché

**Por qué**: la caché es lo primero que se borra cuando falta espacio, y conviene haberlo
hecho una vez antes de necesitarlo con prisa.

> [!WARNING]
> `Playback > Delete Render Cache > All` borra **toda** la caché de render del proyecto.
> No pierdes trabajo —la caché es material regenerable por definición— pero Resolve tendrá
> que volver a calcularla, y eso puede llevar bastante en un proyecto grande. No lo lances
> en mitad de una sesión con prisa.

Ahora mismo tu proyecto no tiene caché que borrar, así que es el momento seguro para
localizar el menú y leer sus tres opciones sin ejecutarlas.

**Verifica**: sabes dónde está el menú y qué hace cada una de sus opciones.

---

## Paso 6: Cerrar la ficha técnica

**Por qué**: es el entregable escrito de la semana, y la parte que el verificador no puede
comprobar.

Añade a `BC-Resolve/04-respaldos/ficha-tecnica-material.md` una sección final:

```markdown
## Presupuesto de disco

- Velocidad medida de mi disco de trabajo: ___ MB/s
- Tipo de disco: ___
- Bitrate típico de mi material: ___ Mbps  (___ GB/hora)
- Horas de grabación previstas: ___
- Total estimado del bootcamp: ___ GB
- Espacio libre ahora mismo: ___ GB
- ¿Voy a necesitar proxies desde la Semana 05?: sí / no, porque ___

## Dónde escribe Resolve

- Primer disco de Media Storage: ___
- Cache files location: ___
- Gallery stills location: ___
```

**Verifica**: las nueve líneas están rellenas con números concretos, no con "suficiente".

---

## Paso 7: Pasar la semana entera

```bash
python scripts/verificar-semana.py 02
```

**Verifica**: los seis checks en verde. Si alguno falla, la columna de pistas del propio
verificador dice exactamente qué mirar.

---

## ✅ Resultado

- [ ] Velocidad de mi disco medida y anotada en MB/s
- [ ] Bitrate y GB por hora de mi propio material calculados
- [ ] Presupuesto total de disco del bootcamp estimado
- [ ] `Media Storage` apunta a mi disco de trabajo
- [ ] `Cache files location` apunta a `02-cache/`
- [ ] Sé dónde se vacía la caché y qué implica
- [ ] `ficha-tecnica-material.md` completa
- [ ] `verificar-semana.py 02` en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| La copia va absurdamente rápida | El sistema operativo la ha hecho en memoria caché | Repite con un archivo mayor que tu memoria RAM libre, o reinicia antes |
| No encuentro `Working Folders` | Estás en la pestaña equivocada de Project Settings | `Master Settings`, hay que bajar en la lista |
| No puedo elegir una carpeta en `Media Storage` | Resolve no ve el disco porque está desconectado o sin permisos | Conéctalo, y comprueba que el usuario tiene permiso de escritura |
| El total de disco me sale enorme | Estás contando proxies de material que no vas a usar | Los proxies solo hacen falta para lo que entre en la timeline, no para todo lo grabado |
| El disco del sistema se llena solo | La caché sigue escribiendo en su ubicación por defecto | Revisa los dos sitios: `Media Storage` **y** `Working Folders`. Son ajustes distintos |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · El banco de formatos](03-el-banco-de-formatos.md) | **04 · Medir el flujo de datos** | — |

← [Volver a la Semana 02](../README.md)
