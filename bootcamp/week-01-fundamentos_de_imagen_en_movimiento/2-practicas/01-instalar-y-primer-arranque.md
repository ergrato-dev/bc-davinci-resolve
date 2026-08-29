# Práctica 01 — Instalar y primer arranque

> Al terminar tendrás DaVinci Resolve 21 instalado, configurado para nueve meses de
> trabajo, y el verificador del bootcamp respondiendo en verde.

**Duración estimada**: 45 min
**Prerrequisitos**: [Teoría 07](../1-teoria/07-instalar-davinci-resolve-21.md), [`docs/hardware-y-rendimiento.md`](../../../docs/hardware-y-rendimiento.md)

## Contexto

No estás instalando un programa: estás montando un puesto de trabajo que vas a usar
360 horas. Las decisiones de esta práctica —dónde va la caché, si se guarda solo, en qué
idioma está la interfaz— no se vuelven a tocar en todo el bootcamp.

Necesitas: unos 3 GB de descarga, permisos de administrador y un reinicio.

---

## Paso 1: Preparar la estructura de carpetas

**Por qué**: Resolve **no guarda tus vídeos dentro del proyecto**. Guarda una lista de
instrucciones que apunta a archivos de tu disco. Si esos archivos se mueven, el proyecto
se queda *offline*. Decidir la estructura ahora, antes de que haya nada dentro, es la
única forma barata de hacerlo.

En el disco más rápido que tengas, crea:

```
BC-Resolve/
├── 00-medios-bootcamp/
├── 01-material-propio/
├── 02-cache/
├── 03-entregas/
└── 04-respaldos/
```

> [!WARNING]
> **No la crees dentro de una carpeta que sincronice con la nube** (OneDrive, Dropbox,
> iCloud Drive). La sincronización puede mover o descargar bajo demanda un archivo
> mientras Resolve lo está leyendo, y Resolve lo marcará como perdido en mitad de una
> sesión.

**Verifica**: las cinco carpetas existen y la ruta completa no contiene acentos ni
caracteres raros. Anótala: la vas a necesitar en el paso 5.

---

## Paso 2: Actualizar el driver de la GPU

**Por qué**: Resolve calcula casi todo en la tarjeta gráfica. Un driver antiguo es la
causa número uno de cierres inesperados en una instalación nueva, y el síntoma —el
programa se cierra sin decir nada— no apunta hacia el driver por ningún lado.

- **NVIDIA**: desde la aplicación de NVIDIA o desde su web
- **AMD**: desde el software de AMD o desde su web
- **Mac**: el driver va en el sistema operativo; basta con tenerlo actualizado

**Verifica**: el panel de control del fabricante indica que estás en la última versión
disponible para tu tarjeta.

---

## Paso 3: Descargar Resolve 21

**Por qué**: hay dos productos con nombres casi iguales y descargar el equivocado te
mete en un periodo de prueba de la versión de pago, que además confunde el reparto de
funciones durante todo el bootcamp.

Ve a <https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion> y
descarga **DaVinci Resolve 21** —el que **no** dice "Studio"— para tu sistema operativo.

Pide un formulario con nombre y correo. No hay pago ni cuenta.

**Verifica**: el archivo descargado pesa alrededor de 3 GB y su nombre contiene `21`.

---

## Paso 4: Instalar y reiniciar

**Por qué**: en Windows el instalador registra componentes de sistema que no cargan
hasta que se reinicia. Abrir el programa antes del reinicio produce errores confusos.

1. Ejecuta el instalador y acepta los componentes adicionales que ofrezca.
2. **Reinicia el ordenador.**
3. Abre DaVinci Resolve.

En el primer arranque, Resolve crea su base de datos y ofrece un tour rápido. Acepta el
tour: son dos minutos.

**Verifica**: `Help > About DaVinci Resolve` (Windows) o
`DaVinci Resolve > About DaVinci Resolve` (macOS) muestra una versión que empieza por
**21**. Anota el número completo y si pone "Studio" o no.

---

## Paso 5: Configurar las preferencias que importan

**Por qué**: cuatro ajustes que, sin tocar, producen cuatro problemas distintos en las
semanas siguientes: caché llenando el disco del sistema, trabajo perdido, y un vocabulario
que no coincide con el de ningún tutorial.

Abre `DaVinci Resolve > Preferences` — atajo `Ctrl+,` (Win) / `Cmd+,` (Mac).

### 5.1 Caché — pestaña `System`, sección `Media Storage`

Añade tu carpeta `02-cache/` y **súbela al primer puesto** de la lista con las flechas.

### 5.2 Guardado — pestaña `User`, sección `Project Save and Load`

Activa **Live Save** y **Project Backups**.

### 5.3 Idioma — pestaña `User`, sección `UI Settings`

Déjalo en **English**.

> [!IMPORTANT]
> Si te tienta ponerlo en español: todo el material del bootcamp, toda la documentación
> oficial de Blackmagic y prácticamente todos los tutoriales del mundo usan los nombres
> en inglés. Cada semana trae su glosario español-inglés en `5-glosario/`. Poner la
> interfaz en español te obliga a traducir de vuelta cada vez que busques ayuda.

### 5.4 GPU — pestaña `Memory and GPU`

No cambies nada. **Mira** qué tarjeta aparece y cuánta memoria reserva Resolve. Es la
pantalla a la que volverás el día que el rendimiento se caiga.

Resolve pedirá reiniciarse. Hazlo ahora.

**Verifica**: al volver a abrir Preferences, los cuatro ajustes siguen como los dejaste,
y `System > Media Storage` muestra tu carpeta `02-cache/` en primera posición.

---

## Paso 6: Instalar Python y arrancar el verificador

**Por qué**: el verificador del bootcamp comprueba tus entregables leyendo el estado
real de tu proyecto. Lo necesitas desde la práctica 02, así que se deja funcionando hoy.

1. Instala **Python 3.10 o superior, de 64 bits**, *para todos los usuarios*, desde
   <https://www.python.org/downloads/>. En Windows, marca **Add python.exe to PATH** en
   la primera pantalla del instalador.

2. Comprueba:

   ```bash
   python --version
   ```

3. Con Resolve abierto, lanza el puente desde `Workspace > Scripts > Utility`.

4. Desde la carpeta del bootcamp:

   ```bash
   python scripts/verificar-semana.py --doctor
   ```

**Verifica**: salida en verde, con la versión de Resolve empezando por 21:

```
  OK  Puente vivo (version 1.9.0)
  OK  DaVinci Resolve 21.0.4.5
  OK  La API de scripting responde
```

El aviso amarillo sobre `BC_MEDIOS` es normal: todavía no has descargado el pack de
medios y esa comprobación es opcional.

---

## ✅ Resultado

- [ ] Estructura `BC-Resolve/` creada, fuera de carpetas de sincronización en la nube
- [ ] Driver de GPU actualizado
- [ ] DaVinci Resolve **21** instalado, y sé si es Free o Studio
- [ ] Caché apuntando a `02-cache/`, en primera posición de Media Storage
- [ ] Live Save y Project Backups activados
- [ ] Interfaz en inglés
- [ ] Sé dónde ver qué GPU usa Resolve
- [ ] Python 3.10+ instalado y en el PATH
- [ ] `verificar-semana.py --doctor` en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| Resolve se cierra al arrancar, sin mensaje | Driver de GPU antiguo o GPU no soportada | Actualiza el driver y reinicia. Si persiste, comprueba tu tarjeta en el documento de configuraciones soportadas de Blackmagic |
| "GPU memory full" nada más abrir | VRAM insuficiente para el layout por defecto | Cierra otras aplicaciones que usen la GPU (navegador con vídeo, juegos) y vuelve a abrir |
| No aparece `Workspace > Scripts` | El puente no está instalado en la carpeta de scripts del usuario | Revisa la ruta de la carpeta de scripts en [`docs/setup-entorno.md`](../../../docs/setup-entorno.md) |
| `No encuentro el token del puente` | El puente nunca se ha arrancado | Lánzalo desde `Workspace > Scripts > Utility` **dentro** de Resolve, y repite el doctor |
| `No puedo hablar con el puente` | Resolve cerrado, o el script corre en otra máquina | Abre Resolve. Si tu repositorio está en WSL y Resolve en Windows, ejecuta el verificador con el Python de Windows |
| `python: command not found` | Python no está en el PATH | Reinstala marcando "Add python.exe to PATH", o usa `python3` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| — | **01 · Instalar y primer arranque** | [02 · Crear el proyecto del bootcamp](02-crear-el-proyecto-del-bootcamp.md) |

← [Volver a la Semana 01](../README.md)
