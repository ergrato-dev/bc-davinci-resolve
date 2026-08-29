---
name: verificar-features-resolve
description: Comprueba contra la instalación real de DaVinci Resolve 21 que las rutas de menú, controles, efectos y métodos de la API que menciona el material existen de verdad. Úsalo sobre cualquier archivo antes de publicarlo.
---

# Verificar features de Resolve

Caza afirmaciones inventadas sobre la interfaz o la API de DaVinci Resolve 21.

Una ruta de menú equivocada hace más daño que un capítulo que falte: el estudiante
busca veinte minutos y deja de fiarse del resto del material.

## 1. Extraer las afirmaciones del archivo

```bash
# Rutas de menú
grep -oE '`[A-Z][A-Za-z0-9 +]+( > [A-Za-z0-9 .+-]+)+`' <archivo>

# Atajos
grep -oE '`(Ctrl|Cmd|Alt|Opt|Shift|F[0-9]+)[^`]*`' <archivo>

# Métodos de la API
grep -oE '\b[a-z_]+\.[A-Z][A-Za-z]+\(' <archivo>
```

## 2. Verificar cada una

### Rutas de menú, controles y efectos

Con el servidor MCP `resolve`, conectado a la instalación real:

- `resolve_status` — confirma versión y que el puente responde
- `project_settings` — nombres y valores reales de los ajustes de proyecto
- `timeline_probe`, `media_list` — formas reales de los datos
- `render_presets`, `render_formats` — presets y codecs que existen de verdad

Lo que la API no cubre (el nombre literal de un menú, dónde vive un control) se
verifica abriendo Resolve y mirando, o contra el manual oficial de Blackmagic.

### Métodos de la API

Contra el README del SDK que instala el propio Resolve:

```bash
grep -n "NombreDelMetodo" \
  "/mnt/c/ProgramData/Blackmagic Design/DaVinci Resolve/Support/Developer/Scripting/README.txt"
```

Rutas equivalentes: macOS
`/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/README.txt`,
Linux `/opt/resolve/Developer/Scripting/README.txt`.

**Un método que no está en ese README no existe.**

### Reparto Free y Studio

Contrasta con `docs/free-vs-studio.md` y con la página oficial de comparación. El caso
que más se confunde: el scripting **externo** es de Studio; el scripting **dentro** de
Resolve (`Workspace > Scripts`) funciona en Free.

## 3. Reglas

- **Nunca des por buena una ruta porque suene plausible.** Ese es exactamente el fallo
  que este skill existe para cazar.
- Si no puedes verificar algo, **dilo** y propón enlazar el manual oficial en lugar de
  afirmarlo.
- Cuando corrijas algo, di **cómo** lo verificaste y con **qué versión**.

## 4. Informe

```
ruta:línea: 🔴 inventado: "<cita literal>". No existe. Lo correcto es <X>. Verificado con <cómo>.
ruta:línea: 🟡 sin verificar: "<cita literal>". No he podido comprobarlo. Enlaza el manual o quítalo.
ruta:línea: 🔵 impreciso: "<cita literal>". Existe pero <matiz>.
```

Cita literalmente. Un hallazgo sin método de verificación no vale nada.
