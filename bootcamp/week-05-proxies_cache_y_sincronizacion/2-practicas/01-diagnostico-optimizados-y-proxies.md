# Práctica 01 — Diagnóstico, medios optimizados y proxies

> Al terminar sabrás qué parte de tu equipo es la que se atasca, tendrás medios
> optimizados para el material problemático que anotaste la semana pasada, y proxies para
> tu material propio. Y, sobre todo, tendrás un número antes y otro después: sin eso, no
> sabes si has arreglado algo.

**Duración estimada**: 55 min
**Prerrequisitos**: [Teoría 01](../1-teoria/01-por-que-el-material-no-va-fluido.md), [Teoría 02](../1-teoria/02-medios-optimizados.md), [Teoría 03](../1-teoria/03-proxies.md), Semana 04 cerrada

## Contexto

La Semana 04 terminó con dos archivos escritos: `notas-de-ingesta.md`, con el material
que se sale del estándar, y el smart bin `SB-Revisar`, que lo mantiene a la vista. Esta
práctica es la que le da salida a esa lista.

Ten los dos a mano: vas a trabajar exactamente sobre esos clips y no sobre todo el media
pool.

---

## Paso 1: Comprobar el espacio libre antes de generar nada

**Por qué**: todo lo de hoy escribe archivos, y bastantes. Generar hasta llenar el disco
deja el proyecto en un estado incómodo y la generación a medias.

1. Mira el espacio libre del disco donde declaraste la *Working Folder* en la Semana 03
2. Mira lo que ocupa tu carpeta de material
3. Anota los dos números

**Verifica**: tienes libre **al menos el doble** de lo que pesa tu material. Si no, no
sigas todavía: vacía espacio, o usa las resoluciones bajas de los pasos 3 y 6, que es
justamente para lo que están.

---

## Paso 2: El diagnóstico, con un número

**Por qué**: sin medir antes no puedes saber si lo que generes sirve de algo. Y la
mayoría de la gente genera cincuenta gigabytes para un problema que no era ese.

1. Abre `BC-Bootcamp-Resolve` y ve a la página **Edit**
2. Abre la timeline `BC-Montaje-v1`
3. Arrastra a la timeline dos o tres de los clips que `SB-Revisar` tiene dentro
4. Reproduce y **mira el contador de fotogramas por segundo del visor**. Anota el número
5. Ahora las tres pruebas de la [teoría 01](../1-teoria/01-por-que-el-material-no-va-fluido.md):
   un clip solo, cuatro pistas a la vez, y un clip con un cambio de escala en el
   `Inspector` (pestaña `Transform`, campo `Zoom`)

**Verifica**: tienes tres números anotados y sabes cuál de los tres cuellos es el tuyo.
Si el clip solo ya cae por debajo del frame rate de tu timeline, es descompresión y los
pasos siguientes son para ti.

> [!TIP]
> Si con tu material no cae nunca —hay equipos que reproducen H.264 de 1080p sin
> despeinarse—, haz la práctica igual. La generación funciona igual y la vas a necesitar
> en la Semana 22 con material RAW, que no perdona a ningún equipo.

---

## Paso 3: Configurar antes de generar

**Por qué**: los ajustes por defecto pueden producir archivos varias veces más grandes de
lo que necesitas. Un minuto aquí ahorra gigabytes y minutos de generación.

1. `File > Project Settings > Master Settings > Optimized Media and Render Cache`
2. En el ajuste de **resolución de los medios optimizados**, elige **un cuarto**
3. En el de **formato**, elige un codec intra-frame de calidad media de los que ofrezca
   tu sistema
4. Guarda los ajustes

**Verifica**: los dos desplegables muestran lo que has elegido al volver a abrir la
ventana.

> [!NOTE]
> La lista exacta de codecs depende de tu sistema operativo y **no se puede comprobar por
> la API de scripting**. El capítulo *Optimized Media and Render Cache* del
> [manual oficial](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion)
> recoge las opciones de tu versión. Si dudas entre dos calidades del mismo codec, elige
> la media: esta semana no vas a etalonar sobre ellos.

---

## Paso 4: Generar medios optimizados para lo problemático

**Por qué**: se optimiza lo que da guerra, no todo. El material que ya iba fluido no gana
nada y ocupa igual.

1. Página **Media**, y abre el smart bin **`SB-Revisar`**
2. Selecciona **todos** sus clips
3. Menú contextual > `Generate Optimized Media`
4. Deja que trabaje. Puedes seguir usando el programa mientras

**Verifica**: al terminar, pasa el media pool a **vista de lista** y activa con clic
derecho sobre la cabecera de columnas la que informa del estado de optimizado. Los clips
de `SB-Revisar` aparecen marcados.

---

## Paso 5: Comprobar que sirvió de algo

**Por qué**: es el paso que casi nadie hace, y sin él no sabes si estás usando los
optimizados o si has generado para nada.

1. Vuelve a la timeline con esos clips y reprodúcela
2. Con `Playback > Use Optimized Media if Available` **activado**, anota los fps
3. **Desactívalo** y vuelve a reproducir. Anota los fps
4. Vuelve a activarlo

**Verifica**: los dos números son distintos. Si son iguales, o el clip no estaba
optimizado, o tu equipo no tenía un problema de descompresión con ese material y el
cuello estaba en otro sitio.

---

## Paso 6: Proxies para tu material propio

**Por qué**: el material de `08-Propio` es el que te vas a llevar de un sitio a otro y el
que más vas a tocar durante nueve meses. Es el caso de libro del proxy.

1. En los ajustes del proyecto, configura la **resolución de proxy** a **media** o a **un
   cuarto**, y su formato
2. Página Media, bin **`08-Propio`**, selecciona todos los clips
3. Menú contextual > `Generate Proxy Media`

**Verifica**: al terminar, cambia `Playback > Proxy Handling` entre preferir proxies y
preferir el material original mientras reproduces, y comprueba que el contador de fps
cambia.

---

## Paso 7: Medir lo que ha costado

**Por qué**: es el dato que necesitas para planificar las 31 semanas que quedan, y el que
te dirá si esta configuración es sostenible en tu disco.

1. Mira ahora el tamaño de tu *Working Folder*
2. Réstale el número que anotaste en el paso 1
3. Divide entre los minutos de material que has procesado

**Verifica**: tienes una cifra en gigabytes por minuto. Con ella puedes estimar lo que
costará optimizar el resto del proyecto.

---

## Paso 8: Escribir las conclusiones

**Por qué**: dentro de tres meses no vas a acordarte de qué configuración elegiste ni por
qué, y vas a volver a decidirlo desde cero.

Crea `BC-Resolve/04-respaldos/rendimiento.md` y escribe cinco líneas:

> **Cuello de botella detectado**: descompresión / disco / efectos, con los tres números
> de fps del paso 2.
>
> **Ajustes elegidos**: resolución y formato de optimizados y de proxies.
>
> **Ganancia medida**: fps con optimizados y sin ellos, del paso 5.
>
> **Coste en disco**: los gigabytes por minuto del paso 7.
>
> **Decisión**: optimizados u optimizados y proxies, y por qué.

**Verifica**: el archivo existe y cada línea tiene un número concreto, no un adjetivo.

---

## ✅ Resultado

- [ ] Sé cuánto espacio libre tengo y cuánto pesa mi material
- [ ] Tengo tres números de fps y sé cuál es mi cuello de botella
- [ ] He configurado resolución y formato **antes** de generar
- [ ] `SB-Revisar` está optimizado entero
- [ ] He comprobado la ganancia activando y desactivando el interruptor
- [ ] `08-Propio` tiene proxies generados
- [ ] Sé cuántos gigabytes por minuto me cuesta esto
- [ ] `rendimiento.md` escrito, con cifras

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| La generación va lentísima | Resolución completa y codec de calidad alta | Cancela, baja a un cuarto y vuelve a lanzar |
| El disco se llena a mitad | El paso 1 se saltó | Borra lo generado, haz sitio y baja la resolución |
| Los fps no cambian con optimizados | El interruptor está desactivado, o el cuello no era la descompresión | Comprueba `Playback > Use Optimized Media if Available` y repasa el paso 2 |
| No encuentro `Generate Optimized Media` | Hiciste clic derecho sin selección, o fuera del media pool | Selecciona clips en el media pool y repite |
| `SB-Revisar` sale vacío | La metadata de la Semana 04 quedó a medias | Práctica 03 de la Semana 04, paso 3 |
| La imagen se ve peor que antes | Estás viendo el optimizado a un cuarto | Es lo esperado. Desactiva el interruptor para ver el original |
| Los proxies no cambian nada | `Playback > Proxy Handling` no está preferiendo proxies | Cámbialo y vuelve a reproducir |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · Diagnóstico, medios optimizados y proxies** | [02 · La caché de render y el disco](02-la-cache-de-render-y-el-disco.md) |

← [Volver a la Semana 05](../README.md)
