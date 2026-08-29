# Práctica 02 — La estructura de bins y la primera importación

> Al terminar, tu proyecto tendrá los diez bins del bootcamp, el material dentro del que
> le toca, Master sin un solo clip suelto y un power bin disponible en todos tus
> proyectos. Es la práctica que decide si la semana doce va a ser cómoda o no.

**Duración estimada**: 50 min
**Prerrequisitos**: [Práctica 01](01-la-copia-verificada.md), [Teoría 04](../1-teoria/04-el-media-pool-y-los-bins.md), [Teoría 05](../1-teoria/05-los-bins-que-no-son-bins.md)

## Contexto

La estructura va **antes** que el material. Si importas primero, los clips caen donde
caigan y luego hay que moverlos; si creas los bins primero, cada cosa entra en su sitio
desde el principio.

Los nombres son literales. El verificador los busca carácter a carácter, así que un
`01-Básicos` con tilde o un `01-basicos` en minúscula no lo encuentra.

---

## Paso 1: Abrir el proyecto correcto

**Por qué**: los checks leen **el proyecto abierto**. En la Semana 03 creaste también
`BC-Pruebas-semana03`, y terminar en él hace fallar la semana entera.

1. Abre Resolve
2. Project Manager, **raíz de tu biblioteca original**
3. Abre **`BC-Bootcamp-Resolve`**
4. Lanza el puente desde `Workspace > Scripts > Utility`

**Verifica**:

```bash
python scripts/verificar-semana.py 04 --check proyecto-abierto
```

---

## Paso 2: Comprobar que el frame rate sigue bloqueado

**Por qué**: no es un trámite. Es la confirmación de que el proyecto en el que vas a
meter 40 GB de material es el que configuraste, y no uno nuevo creado por error.

`File > Project Settings` (`Shift+9`) > `Master Settings` > bloque `Timeline Format`.

**Verifica** dos cosas a la vez:

- `Timeline frame rate` dice **24**
- El campo aparece **atenuado**, porque desde la Semana 02 hay clips en el media pool

```bash
python scripts/verificar-semana.py 04 --check frame-rate-bloqueado
```

> [!IMPORTANT]
> Si el campo **no** está atenuado, no estás en el proyecto del bootcamp. Para y vuelve
> al paso 1. Importar 40 GB en el proyecto equivocado se arregla, pero cuesta una tarde.

---

## Paso 3: Crear los diez bins

**Por qué**: la estructura entera de una vez, incluidos los bins de semanas que aún no
han llegado. Un bin vacío no molesta; un bin que falta hace que el material de la
Semana 16 acabe en `01-Basicos`.

En la página **Media** (`Shift+2`), en la lista de bins del media pool:

1. Selecciona **`Master`**. Esto es lo que hace que el bin nuevo sea de primer nivel
2. `File > New Bin`
3. Nómbralo y repite

Los diez, exactamente así:

```
01-Basicos
02-Entrevista
03-Multicamara
04-Log-y-RAW
05-Croma
06-Audio
07-Graficos
08-Propio
09-Escenas
10-Descartes
```

> [!WARNING]
> **Sin tildes, con las mayúsculas tal cual y con los dos dígitos.** `01-Basicos`, no
> `01-Básicos` ni `1-Basicos`. El verificador compara carácter a carácter, y esta es la
> causa número uno de checks en rojo esta semana.

**Verifica**: los diez cuelgan directamente de `Master`, ninguno dentro de otro.

---

## Paso 4: Importar el material del pack

**Por qué**: es donde se cobra el trabajo de haber ordenado el disco. Los bins ya
existen y las carpetas se llaman igual.

1. Panel **`Media Storage`**, navega hasta `00-medios-bootcamp/`
2. Abre `01-basicos/`
3. **Selecciona el bin `01-Basicos`** en el media pool. Este paso es el que decide dónde
   cae todo
4. Selecciona los clips en Media Storage y arrástralos al media pool

Repite con `02-entrevista/` → bin `02-Entrevista`.

> [!TIP]
> La alternativa rápida, cuando el disco ya está ordenado, es clic derecho sobre la
> carpeta en Media Storage > `Add Folder and SubFolders into Media Pool`, que crea un bin
> por subcarpeta de un tirón. Aquí se hace a mano a propósito, para que veas el efecto
> del bin activo. En la Semana 05, con más material, usarás la rápida.

**Verifica**:

```bash
python scripts/verificar-semana.py 04 --check bin-basicos
python scripts/verificar-semana.py 04 --check bin-entrevista
```

---

## Paso 5: Importar tu material

**Por qué**: es el material de tu pieza. A partir de aquí el proyecto deja de ser un
ejercicio.

1. Selecciona el bin **`08-Propio`**
2. Desde Media Storage, navega a `BC-Propio/` y arrastra tus diez planos

**Verifica**:

```bash
python scripts/verificar-semana.py 04 --check bin-propio
```

---

## Paso 6: Dejar Master limpio

**Por qué**: Master es la raíz. Un clip suelto ahí es la primera grieta de un proyecto
que se desordena, y esta semana es el único momento en el que arreglarlo cuesta un
minuto.

1. Selecciona el bin **`Master`**
2. Mira qué hay dentro **directamente**, sin contar lo que está en los subbins
3. Si ves clips de la Semana 02 —los cuatro de `BC-Formatos`— o cualquier otro, muévelos
   al bin que les corresponda arrastrándolos

> [!NOTE]
> Lo que **sí** se queda en Master es la timeline `BC-Montaje-v1`. Una timeline no es un
> clip: no tiene archivo detrás, y su columna `File Path` está vacía. El check de este
> paso cuenta solo los elementos que tienen ruta de archivo, así que la timeline no le
> molesta. *Comportamiento verificado por la API de scripting en 21.0.4.5, agosto de
> 2026.*

**Verifica**:

```bash
python scripts/verificar-semana.py 04 --check master-limpio
```

---

## Paso 7: Un power bin para lo que se repite

**Por qué**: hay material que no es de esta pieza sino de todas las tuyas. Volver a
importarlo en cada proyecto acaba con cuatro versiones del mismo logotipo.

1. `View > Show Power Bins`. Aparece una sección nueva en la lista de bins
2. Crea dentro un power bin llamado **`BC-Recursos`**
3. Mete algo que vayas a reutilizar: un PNG con tu logotipo, una cortinilla, una pieza
   de música de cabecera. Si aún no tienes nada, sirve un gráfico de `07-graficos/`

**Verifica**: vuelve al Project Manager, abre `BC-Pruebas-semana03` y comprueba que
`BC-Recursos` está también ahí, con su contenido. **Vuelve después a
`BC-Bootcamp-Resolve`.**

> [!WARNING]
> Un power bin guarda referencias como cualquier bin. Si mueves el archivo del logotipo,
> se queda *offline* **en todos tus proyectos a la vez**. Dale una carpeta estable en tu
> disco de trabajo y no la toques.

---

## Paso 8: El pase de diagnóstico

**Por qué**: es el momento de enterarse de qué material va a dar problemas. Enterarse
hoy es una tarea de la Semana 05; enterarse en la Semana 12 es una tarde perdida en
mitad del montaje.

1. Abre `01-Basicos` y pasa el media pool a **vista de lista**
2. Clic derecho sobre la **cabecera de columnas** y activa `Frame Rate`, `Resolution`,
   `Video Codec`, `Duration` y `File Path`
3. Ordena por `Frame Rate`: ¿hay clips que no van a 24 fps?
4. Ordena por `Resolution`: ¿hay 4K entre material HD?
5. Ordena por `Video Codec`: ¿hay HEVC o algo exótico?
6. Ordena por `Duration`: ¿hay clips de más de un minuto?

**Verifica**: anota en un archivo `notas-de-ingesta.md`, en `BC-Resolve/04-respaldos/`,
cuántos clips se salen del estándar y en qué. Es un entregable de la semana y la lista
de trabajo de la Semana 05.

---

## ✅ Resultado

- [ ] `BC-Bootcamp-Resolve` abierto y el puente lanzado
- [ ] `Timeline frame rate` sigue en 24 y aparece atenuado
- [ ] Los diez bins existen, con el nombre exacto, colgando de `Master`
- [ ] 15 o más clips en `01-Basicos` y al menos uno en `02-Entrevista`
- [ ] 10 o más clips propios en `08-Propio`
- [ ] Master no tiene ningún clip suelto: solo bins y la timeline
- [ ] El power bin `BC-Recursos` existe y se ve desde otro proyecto
- [ ] `notas-de-ingesta.md` escrito con el resultado del pase de diagnóstico

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| `bin-basicos` falla y el bin tiene clips | El nombre no coincide: tilde, minúscula o falta el cero | Renómbralo a `01-Basicos`, exacto |
| Un check de bin falla y el bin parece vacío | El bin no existe, o está dentro de otro | El verificador no distingue "vacío" de "no existe": comprueba que cuelga de `Master` |
| Los clips cayeron en el bin equivocado | Se importó sin mirar el bin activo | Selecciónalos y arrástralos al correcto: mover no duplica |
| `master-limpio` falla | Hay clips sueltos en la raíz | Muévelos a su bin. La timeline no cuenta |
| El campo `Timeline frame rate` **no** está atenuado | Estás en otro proyecto | Vuelve a `BC-Bootcamp-Resolve` antes de importar nada |
| No encuentro los power bins | No están visibles por defecto | `View > Show Power Bins` |
| `bin-propio` falla con 10 clips dentro | El bin se llama `08-propio` o `08-Propios` | El nombre exacto es `08-Propio` |
| Todos los checks fallan a la vez | El puente no está lanzado, o el proyecto abierto es otro | `Workspace > Scripts > Utility`, y comprueba el proyecto |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · La copia verificada](01-la-copia-verificada.md) | **02 · La estructura de bins y la primera importación** | [03 · Metadata, keywords y marcas](03-metadata-keywords-y-marcas.md) |

← [Volver a la Semana 04](../README.md)
