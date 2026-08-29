# ⚙️ Preparar el entorno

> Una hora bien invertida aquí ahorra treinta semanas de fricción.

Este documento se hace **una vez**, antes de la Semana 01. Al terminar tendrás Resolve
21 instalado, una estructura de carpetas que no se te desmontará en el mes cuatro, y el
verificador del bootcamp funcionando.

---

## 1. Antes de instalar

Lee [hardware-y-rendimiento.md](hardware-y-rendimiento.md). Si tu GPU tiene menos de
4 GB de VRAM o tu disco de trabajo es mecánico, no es que no puedas hacer el bootcamp:
es que la Semana 05 (proxies) pasa de ser útil a ser obligatoria, y conviene saberlo antes.

---

## 2. Instalar DaVinci Resolve 21

1. Ve a la página de soporte de Blackmagic Design:
   <https://www.blackmagicdesign.com/support/family/davinci-resolve-and-fusion>
2. Elige **DaVinci Resolve 21** para tu sistema operativo. La descarga es gratuita y
   pide un formulario con nombre y correo; no hace falta comprar nada.
3. Instala y **reinicia** antes de abrir el programa. En Windows, el instalador
   registra componentes que no cargan hasta el reinicio.
4. Actualiza el driver de tu GPU antes del primer arranque. Es la causa número uno de
   cierres inesperados en una instalación nueva.

> [!TIP]
> Descarga **DaVinci Resolve**, no **DaVinci Resolve Studio**. Studio es la versión de
> pago y no la necesitas: ver [free-vs-studio.md](free-vs-studio.md).

### Primer arranque

En el primer arranque Resolve te ofrece una guía rápida y crea su base de datos por
defecto. Acepta ambas cosas; la Semana 03 explica qué es esa base de datos y cómo
gestionarla.

Comprueba la versión en `DaVinci Resolve > About DaVinci Resolve` (macOS) o
`Help > About DaVinci Resolve` (Windows). Debe empezar por **21**.

---

## 3. La estructura de carpetas

Resolve **no guarda tus vídeos dentro del proyecto**. Un proyecto de Resolve es una
lista de instrucciones que apunta a archivos que viven en tu disco. Si mueves o
renombras esos archivos, el proyecto se queda *offline* y hay que reconectarlo a mano.

Por eso la estructura se decide **antes** de importar el primer clip:

```
BC-Resolve/
├── 00-medios-bootcamp/     # el pack común descargado (ver pack-de-medios.md)
├── 01-material-propio/     # lo que grabes tú
│   ├── video/
│   ├── audio/
│   └── graficos/
├── 02-cache/               # caché y medios optimizados de Resolve
├── 03-entregas/            # todo lo que renderices
└── 04-respaldos/           # exportaciones .drp del proyecto
```

Crea esa estructura ahora, en el disco más rápido que tengas. Las rutas del bootcamp
se escriben siempre como `<ruta-a-medios>`; sustitúyelo mentalmente por la tuya.

> [!WARNING]
> No pongas `00-medios-bootcamp` dentro de una carpeta que sincronice sola con la nube
> (OneDrive, Dropbox, iCloud Drive). La sincronización puede mover o descargar bajo
> demanda un archivo mientras Resolve lo está leyendo, y Resolve lo marcará como
> perdido en mitad de una sesión.

---

## 4. Configuración inicial de Resolve

Se hace una vez y sirve para las 36 semanas. La Semana 03 explica el porqué de cada una.

### Caché y medios optimizados

`DaVinci Resolve > Preferences > System > Media Storage`

Añade tu carpeta `02-cache/` y súbela al primer puesto de la lista. Resolve escribe
ahí los medios optimizados y la caché de render; conviene que no compartan disco con
los medios originales si puedes evitarlo.

### Copias de seguridad del proyecto

`Preferences > User > Project Save and Load`

Activa **Live Save** y **Project Backups**. Live Save guarda continuamente; los backups
guardan versiones anteriores por si necesitas volver atrás. En 36 semanas de bootcamp,
esto se agradece al menos una vez.

### Idioma de la interfaz

Déjalo en **inglés**. Todo el material del bootcamp, todos los tutoriales del mundo y
toda la documentación oficial usan los nombres en inglés. Cada semana trae su glosario
español-inglés en `5-glosario/`.

---

## 5. Python para el módulo de scripting

Lo necesitas para el **verificador del bootcamp desde ya**, y para las Semanas 31-34.

### Instalar Python

Instala **Python 3.10 o superior, de 64 bits**, *para todos los usuarios*:

- **Windows**: desde <https://www.python.org/downloads/>. Marca **Add python.exe to PATH**
  en la primera pantalla del instalador.
- **macOS**: desde python.org, o `brew install python`.
- **Linux**: el Python del sistema sirve si es 3.10 o superior.

Comprueba:

```bash
python --version
```

> [!NOTE]
> El SDK de scripting de Resolve pide **Python de 64 bits, versión 3.6 o superior**
> (`Developer/Scripting/README.txt`, actualizado el 24 de julio de 2026). Cualquier
> Python moderno de 64 bits vale.

### Dónde vive el SDK

Resolve instala el SDK de scripting junto al programa. No hay que descargar nada:

| Sistema | Ruta del SDK |
| ------- | ------------ |
| Windows | `%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting` |
| macOS | `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting` |
| Linux | `/opt/resolve/Developer/Scripting` |

Dentro encontrarás `README.txt`, `Modules/DaVinciResolveScript.py` y una carpeta
`Examples/`. Ese `README.txt` es la fuente de verdad de la API; la Semana 31 lo
desmonta entero.

### Dónde se ponen tus scripts

Resolve escanea estas carpetas al arrancar y lista lo que encuentre en
`Workspace > Scripts`:

| Sistema | Carpeta de scripts del usuario |
| ------- | ------------------------------ |
| Windows | `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts` |
| macOS | `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts` |
| Linux | `~/.local/share/DaVinciResolve/Fusion/Scripts` |

Un script colocado en la subcarpeta `Utility` aparece en todas las páginas. Es la vía
que usa el verificador del bootcamp.

> [!IMPORTANT]
> **Free y el scripting.** Ejecutar un script **desde dentro** de Resolve
> (`Workspace > Scripts`, o la consola de la página Fusion) funciona en la versión
> gratuita. Lo que la versión gratuita **no** ofrece es el scripting *externo*: lanzar
> un `python mi_script.py` desde una terminal y que se conecte a Resolve desde fuera.
> Por eso el verificador del bootcamp está partido en dos piezas —un script que corre
> dentro de Resolve y un cliente que habla con él— en lugar de conectarse directamente.
> Las Semanas 31-34 enseñan las dos vías y marcan cuál necesita Studio.

---

## 6. El verificador del bootcamp

El verificador comprueba tus entregables leyendo el estado real de tu proyecto de
Resolve. No modifica nada.

### Arrancarlo

1. Abre DaVinci Resolve 21 con tu proyecto del bootcamp cargado.
2. Lanza el puente desde `Workspace > Scripts > Utility`.
3. Desde la carpeta del bootcamp:

```bash
python scripts/verificar-semana.py --doctor
```

Salida esperada:

```
  OK  Puente vivo (version 1.9.0)
  OK  DaVinci Resolve 21.0.4.5
  OK  La API de scripting responde
  OK  Proyecto abierto: BC-Bootcamp-Resolve
```

Y para verificar una semana concreta:

```bash
python scripts/verificar-semana.py 01
```

### Si el doctor falla

| Mensaje | Qué pasa | Qué hacer |
| ------- | -------- | --------- |
| `No encuentro el token del puente` | El puente nunca se ha arrancado | Lánzalo desde `Workspace > Scripts > Utility` dentro de Resolve |
| `No puedo hablar con el puente` | Resolve cerrado, o el script corre en otra máquina | Abre Resolve; si usas WSL, ejecuta el verificador con el Python de Windows |
| `DaVinci Resolve <otra versión>` | No es la 21 | El material sigue sirviendo, pero algunos menús estarán en otro sitio |
| `Proyecto abierto: ninguno` | Resolve está en el Project Manager | Abre tu proyecto del bootcamp |

Opcionalmente, apunta la variable `BC_MEDIOS` a tu carpeta del pack para que el doctor
la compruebe también:

```bash
export BC_MEDIOS="<ruta-a-medios>/00-medios-bootcamp"   # macOS y Linux
setx BC_MEDIOS "<ruta-a-medios>\00-medios-bootcamp"     # Windows
```

---

## 7. Descargar el material de práctica

Sigue [pack-de-medios.md](pack-de-medios.md). No hace falta tenerlo todo antes de
empezar: la Semana 01 no importa ni un clip. Pero conviene lanzar las descargas
grandes pronto.

---

## ✅ Checklist de verificación

- [ ] DaVinci Resolve 21 instalado y arrancando sin errores
- [ ] `Help > About DaVinci Resolve` muestra una versión que empieza por 21
- [ ] Driver de GPU actualizado
- [ ] Estructura `BC-Resolve/` creada, fuera de cualquier carpeta de sincronización en la nube
- [ ] `Preferences > System > Media Storage` apuntando a mi carpeta de caché
- [ ] Live Save y Project Backups activados
- [ ] Interfaz de Resolve en inglés
- [ ] Python 3.10+ de 64 bits instalado y en el PATH
- [ ] `python scripts/verificar-semana.py --doctor` en verde

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
