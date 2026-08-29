# Práctica 02 — El Project Manager y dos proyectos

> Al terminar tendrás dos proyectos en tu biblioteca con ajustes distintos, y habrás
> comprobado en pantalla —no leído— que los Project Settings son de cada proyecto y las
> Preferences son de la máquina. Es la práctica que fija el concepto de la semana.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 01](01-el-mapa-de-tu-instalacion.md), [Teoría 03](../1-teoria/03-el-project-manager.md), [Teoría 06](../1-teoria/06-project-settings-los-ajustes-de-tu-video.md)

## Contexto

La regla "Preferences es tu ordenador, Project Settings es tu vídeo" se entiende en diez
segundos y se olvida en tres días. La forma de que no se olvide es verla: dos proyectos
abiertos, uno a 24 fps y otro a 25, con las mismas preferencias de máquina.

De paso aprendes a moverte por el Project Manager, que es la pantalla que más vas a ver
y la que menos se enseña.

---

## Paso 1: Volver al Project Manager sin cerrar nada

**Por qué**: mucha gente cierra el proyecto para volver a la lista, y luego espera medio
minuto a que se vuelva a cargar. No hace falta.

Con `BC-Bootcamp-Resolve` abierto:

1. Pulsa el **icono de casa** de la esquina inferior derecha, o usa
   `File > Project Manager`
2. Fíjate en que tu proyecto aparece marcado como abierto
3. Pulsa `Escape`, o haz doble clic sobre él, para volver

**Verifica**: has vuelto a la página en la que estabas, sin barra de carga. El proyecto
nunca se cerró.

---

## Paso 2: Identificar tu biblioteca

**Por qué**: es el contenedor de todo. Antes de crear nada conviene saber dentro de qué
lo estás creando.

1. Vuelve al Project Manager
2. Abre la **barra lateral de bibliotecas** con el botón de su esquina inferior
   izquierda. Se rotula `Project Libraries`
3. Localiza la biblioteca resaltada: esa es la activa

**Verifica**: la biblioteca activa es la misma cuya carpeta localizaste en la
[práctica 01](01-el-mapa-de-tu-instalacion.md), paso 3. Añade su **nombre** a tu
`mapa-de-instalacion.md`.

> [!NOTE]
> Si solo tienes una biblioteca, es la local que Resolve creó al instalarse, y está
> bien: es la que vas a usar las 36 semanas. No hace falta crear ninguna más.

---

## Paso 3: Crear el proyecto de pruebas

**Por qué**: necesitas un sitio donde romper cosas. Cada vez que en el bootcamp quieras
probar algo que no te atreves a hacer en tu pieza, este es el proyecto.

1. En el Project Manager, asegúrate de estar en la **raíz** de la biblioteca, no dentro
   de una carpeta
2. Pulsa **`New Project`**
3. Nómbralo exactamente:

```
BC-Pruebas-semana03
```

4. Acepta. Resolve lo crea y lo abre

> [!IMPORTANT]
> **En la raíz, no dentro de una carpeta.** El verificador lista los proyectos de la
> carpeta que estés viendo en el Project Manager. Si lo creas dentro de una carpeta, el
> check no lo encontrará aunque el proyecto exista.

**Verifica**: el título de la ventana y el Project Manager coinciden: estás dentro de
`BC-Pruebas-semana03`.

---

## Paso 4: Darle unos ajustes distintos

**Por qué**: aquí es donde se ve la diferencia. Este proyecto está **vacío**, así que su
frame rate todavía se puede cambiar. El tuyo no.

Dentro de `BC-Pruebas-semana03`:

1. `File > Project Settings` (`Shift+9`), categoría **`Master Settings`**
2. En el bloque `Timeline Format`, pon `Timeline frame rate` a **25**
3. Fíjate en que el campo **se deja cambiar**: no hay ni un clip en el media pool
4. Guarda los ajustes

**Verifica**: el proyecto de pruebas está a 25 fps. Y anota la sensación: es la última
vez en el bootcamp que vas a ver ese campo activo.

---

## Paso 5: Comprobar que tu proyecto no se ha enterado

**Por qué**: es el punto entero de la práctica.

1. Vuelve al Project Manager
2. Abre `BC-Bootcamp-Resolve`
3. `Shift+9`, `Master Settings`, bloque `Timeline Format`

**Verifica** dos cosas a la vez:

- `Timeline frame rate` sigue diciendo **24**
- Y aparece **atenuado**, porque este proyecto sí tiene clips dentro

Ahora por script, con el puente lanzado:

```bash
python scripts/verificar-semana.py 03 --check frame-rate-de-proyecto
python scripts/verificar-semana.py 03 --check playback-frame-rate
```

> [!TIP]
> `Playback frame rate` es el vecino de abajo y no es lo mismo: define a cuántos frames
> por segundo **se reproduce en tu pantalla**, no cuántos tiene tu pieza. En un proyecto
> a 24 fps los dos valen 24, y así es como se queda. La [teoría 06](../1-teoria/06-project-settings-los-ajustes-de-tu-video.md)
> explica cuándo tiene sentido que difieran.

---

## Paso 6: Comprobar que las Preferences sí son compartidas

**Por qué**: la otra mitad de la regla. Un ajuste de máquina afecta a los dos proyectos
a la vez.

1. Con `BC-Bootcamp-Resolve` abierto, `Ctrl+,` (Win) / `Cmd+,` (Mac)
2. Pestaña **`User`**, sección **`UI Settings`**
3. Cambia algo inofensivo y reversible: el brillo del tema de la interfaz
4. Guarda y cierra Preferences
5. Vuelve al Project Manager y abre `BC-Pruebas-semana03`

**Verifica**: el cambio de apariencia está también aquí. No lo has configurado dos
veces: es un ajuste de la máquina.

Déjalo como más cómodo te resulte y sigue.

---

## Paso 7: Dynamic Project Switching

**Por qué**: es la forma de copiar una timeline, un nodo o un clip de un proyecto a
otro. Sin esto, hay que exportar e importar.

1. Menú **`File`**, activa **`Dynamic Project Switching`**
2. Abre `BC-Bootcamp-Resolve` desde el Project Manager
3. Abre también `BC-Pruebas-semana03`
4. En el menú `File`, salta entre los dos: el cambio es inmediato, sin barra de carga

**Verifica**: puedes ir y volver entre los dos proyectos sin esperar.

> [!WARNING]
> Cada proyecto abierto ocupa memoria. Con estos dos, vacío uno y pequeño el otro, no
> pasa nada; con cuatro proyectos grandes, Resolve se arrastra o se cierra solo.
>
> **Apágalo ahora**: `File > Dynamic Project Switching` otra vez. Se enciende para una
> tarea concreta y se apaga al terminarla.

> [!TIP]
> Si no lo encuentras en el menú `File`, escribe su nombre en el buscador de
> `Keyboard Customization`: te dirá dónde está en tu versión. Es el método general para
> cualquier comando que se haya movido de sitio.

---

## Paso 8: Terminar con el proyecto correcto abierto

**Por qué**: los checks leen **el proyecto abierto**. Si terminas en el de pruebas,
fallan todos y no será culpa del trabajo que has hecho.

1. Abre `BC-Bootcamp-Resolve`
2. Comprueba en el Project Manager que estás en la **raíz** de la biblioteca y que ves
   los dos proyectos
3. Ejecuta la semana entera:

```bash
python scripts/verificar-semana.py 03
```

**Verifica**: en este punto deberían estar en verde `proyecto-abierto`, `resolve-es-21`,
`bootcamp-en-la-biblioteca`, `proyecto-de-pruebas`, `frame-rate-de-proyecto`,
`playback-frame-rate` y `timeline-intacta`. Los siete de la semana.

---

## ✅ Resultado

- [ ] Sé volver al Project Manager sin cerrar el proyecto
- [ ] Sé cuál es mi biblioteca activa y la he anotado en el mapa
- [ ] `BC-Pruebas-semana03` existe, en la raíz de la biblioteca, a 25 fps
- [ ] `BC-Bootcamp-Resolve` sigue a 24 fps y el campo aparece atenuado
- [ ] He comprobado que un ajuste de Preferences afecta a los dos proyectos
- [ ] He usado Dynamic Project Switching y lo he vuelto a apagar
- [ ] Termino con `BC-Bootcamp-Resolve` abierto y los siete checks en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `proyecto-de-pruebas` falla | El proyecto está dentro de una carpeta del Project Manager | Vuelve a la raíz de la biblioteca; el verificador lee la carpeta que estás viendo |
| `proyecto-abierto` falla | Terminaste con el proyecto de pruebas abierto | Abre `BC-Bootcamp-Resolve` y repite |
| El nombre del proyecto de pruebas no coincide | Una errata, o mayúsculas distintas | Clic derecho > renombrar. Se compara carácter a carácter |
| No puedo cambiar el frame rate del proyecto de pruebas | Le has metido algún clip sin querer | Bórralo del media pool; si el campo sigue atenuado, crea el proyecto de nuevo |
| `frame-rate-de-proyecto` da 25 | Cambiaste el frame rate en el proyecto equivocado | Comprueba en qué proyecto estás. Si tocaste el del bootcamp y tenía clips, no habrá pasado nada: está bloqueado |
| Resolve va lento después del paso 7 | Dynamic Project Switching sigue encendido | `File > Dynamic Project Switching` para apagarlo |
| `timeline-intacta` falla | No estás en `BC-Bootcamp-Resolve`, o la timeline se renombró | La timeline de la Semana 01 se llama `BC-Montaje-v1` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · El mapa de tu instalación](01-el-mapa-de-tu-instalacion.md) | **02 · El Project Manager y dos proyectos** | [03 · Copias de seguridad de verdad](03-copias-de-seguridad-de-verdad.md) |

← [Volver a la Semana 03](../README.md)
