# 🌐 Webgrafía — Semana 11

> Documentación oficial primero, tipografía y accesibilidad después, y la documentación transversal
> del propio bootcamp al final. Cada entrada dice **por qué** vale la pena.

---

## Documentación oficial

### Blackmagic Design — soporte y manuales

<https://www.blackmagicdesign.com/support/>

**Por qué vale la pena**: es donde vive el Reference Manual, del que salen los capítulos 50, 54,
55, 56, 103 y 154-169 de esta semana. La particularidad de la semana es que **casi todo son nombres
de controles**, y un nombre mal citado manda a buscar un ajuste que no existe.

### Comparativa oficial DaVinci Resolve Free / Studio

<https://www.blackmagicdesign.com/products/davinciresolve/studio>

**Por qué vale la pena**: esta semana toca la categoría con más funciones al otro lado de la línea
de todo el bootcamp. Muchos ResolveFX son de Studio —la categoría `Sharpen` entera lo es—, y el
manual los marca con `(Studio Version Only)` en el título de cada efecto. Esta página es la
**fuente de verdad** y se actualiza con cada versión; cualquier tabla de terceros, la del bootcamp
incluida, va por detrás.

### Foro oficial de DaVinci Resolve

<https://forum.blackmagicdesign.com/>

**Por qué vale la pena**: es donde se resuelven los casos raros de fuentes: una fuente que no
aparece en el desplegable, una que se ve distinta al abrir el proyecto en otra máquina, un
proyecto que llega con un `Text+` cuya fuente no tienes instalada. Nada de eso está en el manual y
todo está en el foro.

**Cómo buscar**: el buscador del foro es flojo. Funciona mejor buscar en un motor externo con
`site:forum.blackmagicdesign.com` y el mensaje de error literal.

---

## Tipografía y legibilidad

### Google Fonts

<https://fonts.google.com/>

**Por qué vale la pena**: es la fuente más práctica de tipografías **con licencia abierta**, que es
lo que necesitas para poder entregar tu pieza sin problemas de derechos. Se descargan, se instalan
en el sistema y aparecen en el desplegable de Resolve.

**Qué buscar para esta semana**: filtra por `Sans Serif` y por peso `500` o superior. Las familias
con muchos cortes te dan la jerarquía —nombre en negrita, cargo en regular— sin cambiar de familia.

> [!IMPORTANT]
> Las fuentes se instalan **en el sistema operativo**, no en Resolve. Si abres el proyecto en otra
> máquina que no tiene esa fuente, Resolve avisa con un aviso en el visor y sustituye la fuente. Es
> algo a tener en cuenta para el archivado de la Semana 30.

### The Font Matcherator y catálogos de identificación

<https://www.fontsquirrel.com/matcherator>

**Por qué vale la pena**: cuando has visto una rotulación que te sirve de referencia y quieres saber
qué familia usa, o al menos una parecida con licencia abierta. Font Squirrel además filtra por
licencia de uso comercial, que es lo que importa.

### Web Content Accessibility Guidelines — contraste

<https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum>

**Por qué vale la pena**: es el estándar de accesibilidad para contraste entre texto y fondo. Está
escrito para páginas web, no para vídeo, y el criterio no se traslada tal cual —el fondo de un
rótulo se mueve, el de una página no—, pero da **un umbral numérico** donde el resto de la
literatura da opiniones. Como referencia de mínimos, sirve.

**Cómo aplicarlo aquí**: el criterio de la teoría 05 —entornar los ojos, reducir el visor a un
cuarto— es la versión práctica de lo mismo. Esta página es de dónde viene la idea de que el
contraste se puede medir.

---

## Documentación del bootcamp

### [`docs/free-vs-studio.md`](../../../../docs/free-vs-studio.md)

**Por qué vale la pena**: el resumen transversal de qué está en cada versión, con las categorías de
esta semana incluidas. Recuerda que la fuente de verdad es la comparativa oficial de Blackmagic.

### [`docs/atajos-de-teclado.md`](../../../../docs/atajos-de-teclado.md)

**Por qué vale la pena**: esta semana añade atajos de transición que se usan a diario —`Ctrl+T`,
`Alt+T`, `Shift+T`, `Ctrl+D`, `V`, `U`— y el de búsqueda de efectos, `Shift+Espacio`. Todos ellos
dependen de tu instalación: `Alt+Ctrl+K` (Win) / `Opt+Cmd+K` (Mac) abre `Keyboard Customization`,
que es la única fuente fiable de qué atajo tienes tú.

### [`docs/proyecto-hilo-conductor.md`](../../../../docs/proyecto-hilo-conductor.md)

**Por qué vale la pena**: la convención de versionado —duplicar y trabajar sobre la copia— y los
nombres literales que busca el verificador. Esta semana añade el bin `13-Titulos` a la lista.

### [`docs/trucos-resolve.md`](../../../../docs/trucos-resolve.md)

**Por qué vale la pena**: todos los trucos de la semana, agrupados, junto con los de las diez
anteriores. Cuando no te acuerdes de cómo se guardaba un estilo de rótulo, está ahí.

---

## 🔗 Navegación

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [Videografía](../videografia/README.md) | **Webgrafía · Semana 11** | — |

← [Volver a la Semana 11](../../README.md)
