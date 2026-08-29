# Instalar DaVinci Resolve 21

> Es el programa de post-producción más completo que se puede descargar gratis, y eso no
> es una promoción: es literalmente el mismo motor que se usa para etalonar películas de
> cine, con algunas funciones de aceleración quitadas.

## 🎯 Objetivos

- Descargar e instalar DaVinci Resolve 21 sin equivocarse de versión
- Saber qué hace el programa en su primer arranque y por qué
- Comprobar qué versión y qué edición tienes
- Entender qué es la **base de datos** de proyectos y por qué Resolve tiene una
- Dejar configuradas las cuatro preferencias que ahorran problemas durante nueve meses

---

## 1. Qué problema resuelve

Resolve no es un programa que se instale y ya está. Instala una **base de datos**, un
**SDK de scripting**, componentes de sistema para la GPU, y crea una estructura de
carpetas de caché que conviene que esté donde tú quieres y no donde el instalador
decida.

Media hora bien invertida aquí evita tres tipos de problema que aparecen semanas
después: proyectos que no se encuentran, caché llenando el disco del sistema, y trabajo
perdido por no tener las copias de seguridad activadas.

---

## 2. Descargar la versión correcta

Ve a la página de soporte oficial:

<https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>

Ahí verás dos productos con nombres casi iguales:

| Producto | Qué es |
| -------- | ------ |
| **DaVinci Resolve** | La versión **gratuita**. La que quieres |
| **DaVinci Resolve Studio** | La de pago. No la necesitas |

Descarga **DaVinci Resolve 21** para tu sistema operativo. La descarga pide un
formulario con nombre y correo; no hay que pagar ni registrar una cuenta.

Pesa alrededor de 3 GB.

> [!NOTE]
> Que sea gratuita no significa que sea una demo. No pone marcas de agua, no caduca, no
> limita la duración del proyecto y no exige conexión. Lo que Studio añade y cómo se
> sortea está en [`docs/free-vs-studio.md`](../../../docs/free-vs-studio.md).

---

## 3. Instalar

1. **Actualiza el driver de tu GPU antes de instalar.** Es la causa número uno de
   cierres inesperados en una instalación nueva. Resolve depende de la tarjeta gráfica
   para casi todo (teoría de `docs/hardware-y-rendimiento.md`).
2. Ejecuta el instalador. En Windows instalará también componentes de sistema; acéptalos.
3. **Reinicia el ordenador** antes de abrir el programa por primera vez. Algunos
   componentes no cargan hasta el reinicio.

> [!WARNING]
> Si ya tenías una versión anterior de Resolve con proyectos dentro, **haz una copia de
> la base de datos antes de actualizar**. Resolve actualiza el formato de la base de
> datos al abrirla con una versión nueva, y **esa conversión no se puede deshacer**: la
> versión antigua ya no podrá abrirla. Se copia desde el Project Manager, con el icono
> de la base de datos, opción de backup.

---

## 4. El primer arranque

La primera vez, Resolve hace tres cosas:

1. **Crea la base de datos por defecto.** Una base de datos local en tu disco donde
   vivirán todos tus proyectos.
2. **Ofrece un tour rápido.** Acéptalo; son dos minutos.
3. **Abre el Project Manager**, que es la pantalla desde la que se crean y abren
   proyectos.

### Qué es la base de datos y por qué

Casi todos los editores guardan un archivo de proyecto por trabajo: `mi_video.prproj`.
Resolve **no**. Resolve guarda todos los proyectos dentro de una base de datos.

| Ventaja | Inconveniente |
| ------- | ------------- |
| Guardado continuo sin pensarlo (*Live Save*) | No hay un archivo que puedas enviar por correo sin exportarlo antes |
| Varias personas sobre la misma base de datos | Si la base de datos se corrompe, se lleva todo por delante |
| Historial de versiones integrado | Mover el trabajo a otra máquina requiere exportar |

Para sacar un proyecto de la base de datos y llevártelo a otro sitio se exporta a un
archivo `.drp` (`File > Export Project`). Es lo que harás al final de cada fase del
bootcamp, y se ve a fondo en la Semana 30.

Hay dos tipos de base de datos: **de disco** (la de por defecto, un solo usuario) y
**PostgreSQL** (para varias personas a la vez). Para el bootcamp, la de disco.

---

## 5. Comprobar qué tienes

`Help > About DaVinci Resolve` (Windows y Linux) ·
`DaVinci Resolve > About DaVinci Resolve` (macOS)

Ahí verás dos datos que importan:

- **El número de versión.** Tiene que empezar por **21**. Ejemplo real: `21.0.4.5`.
- **El nombre del producto.** Si pone solo **DaVinci Resolve**, tienes la gratuita. Si
  pone **DaVinci Resolve Studio**, tienes la de pago.

Ese mismo dato lo devuelve el verificador del bootcamp:

```bash
python scripts/verificar-semana.py --doctor
```

```
  OK  DaVinci Resolve 21.0.4.5
```

---

## 6. Las cuatro preferencias que se configuran una vez

Resolve separa los ajustes en dos sitios, y conviene entender la diferencia desde ya:

| Dónde | Qué contiene | Alcance |
| ----- | ------------ | ------- |
| **Preferences** | Cómo se comporta el programa en **esta máquina** | Todos tus proyectos |
| **Project Settings** | Cómo es **este proyecto** | Solo ese proyecto |

Frame rate y resolución son de **proyecto**. Dónde está la caché es de **máquina**. Es
una distinción que confunde al principio y que la Semana 03 desarrolla.

Las cuatro que se tocan hoy, todas en `Preferences`:

**1. Dónde va la caché** — `System > Media Storage`

Añade tu carpeta `02-cache/` y súbela al primer puesto de la lista. Resolve escribe ahí
los medios optimizados y la caché de render, que pueden ocupar decenas de gigabytes. Si
no lo tocas, van al disco del sistema.

**2. Live Save y copias de seguridad** — `User > Project Save and Load`

Activa **Live Save** y **Project Backups**. El primero guarda continuamente; el segundo
conserva versiones anteriores. En nueve meses lo vas a agradecer al menos una vez.

**3. Idioma de la interfaz** — `User > UI Settings`

Déjalo en **inglés**. Todo el material del bootcamp, toda la documentación oficial y
todos los tutoriales del mundo usan los nombres en inglés. Cada semana trae su glosario
español-inglés en `5-glosario/`.

**4. Comprobar la GPU** — `Memory and GPU`

Aquí se ve qué tarjeta está usando Resolve y cuánta memoria le reserva. No hay que
cambiar nada; hay que **saber que está ahí** para el día que algo vaya mal.

> [!TIP]
> `Preferences` requiere reiniciar Resolve para aplicar algunos cambios, y el programa te
> avisa. Hazlo en cuanto termines de configurar los cuatro puntos, no después de haber
> empezado a trabajar.

---

## 7. Antipatrones

| Antipatrón | Por qué duele | Qué hacer |
| ---------- | ------------- | --------- |
| Instalar sin actualizar el driver de la GPU | Cierres inesperados que parecen fallos del programa | Driver primero, instalador después |
| Actualizar de versión mayor sin copiar la base de datos | La conversión no se deshace; la versión antigua ya no abre tus proyectos | Backup desde el Project Manager antes de actualizar |
| Dejar la caché en el disco del sistema | Decenas de gigabytes en el disco que menos espacio suele tener | `Preferences > System > Media Storage`, primer día |
| Poner la interfaz en español | Te desconecta del 95 % de la documentación y de los tutoriales | Inglés, con el glosario semanal al lado |
| Descargar Studio "por probar" | Es la versión de pago; se instala en modo de prueba y confunde el reparto de funciones | Descarga DaVinci Resolve a secas |
| No activar Live Save | El día que se cierre inesperadamente perderás lo que llevaras | `Preferences > User > Project Save and Load` |

---

## 8. Trucos

| Truco | Cómo |
| ----- | ---- |
| Saber en un segundo si tienes Free o Studio | `Help > About DaVinci Resolve`: si no pone "Studio", es la gratuita |
| Recuperar un layout que has destrozado | `Workspace > Reset UI Layout`. No toca el proyecto, solo los paneles |
| Ver la GPU que Resolve está usando de verdad | `Preferences > Memory and GPU` |
| Comprobar el entorno entero de una vez | `python scripts/verificar-semana.py --doctor` |

---

## 📚 Recursos Adicionales

- [Blackmagic Design — Soporte y descargas](https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion) — de aquí sale el instalador, el Reference Manual en PDF y el documento de configuraciones soportadas de cada versión.
- [Blackmagic Design Training](https://www.blackmagicdesign.com/products/davinciresolve/training) — las guías oficiales gratuitas; su primer capítulo cubre la instalación con capturas actualizadas de cada versión.
- [Foro oficial de DaVinci Resolve](https://forum.blackmagicdesign.com/) — la sección de instalación y hardware es donde aparecen las incompatibilidades de drivers antes que en ningún otro sitio.

---

## ✅ Checklist de Verificación

- [ ] He descargado DaVinci Resolve, no Studio
- [ ] Actualicé el driver de la GPU antes de instalar
- [ ] Reinicié antes del primer arranque
- [ ] `Help > About DaVinci Resolve` me dice una versión que empieza por 21
- [ ] Sé qué edición tengo, Free o Studio
- [ ] Entiendo qué es la base de datos de proyectos y por qué no hay un archivo por proyecto
- [ ] Tengo la caché apuntando a mi carpeta, no al disco del sistema
- [ ] Live Save y Project Backups están activados
- [ ] La interfaz está en inglés

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [06 · Timecode](06-timecode.md) | **07 · Instalar DaVinci Resolve 21** | [08 · Anatomía de Resolve](08-anatomia-de-resolve.md) |

← [Volver a la Semana 01](../README.md)
