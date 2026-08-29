# CLAUDE.md

Instrucciones para agentes que trabajan sobre este repositorio.

## Qué es esto

Bootcamp de **DaVinci Resolve 21**, 36 semanas, 360 horas, autoestudio. De cero
absoluto a postproductor autónomo: las siete páginas del programa más un módulo de
automatización por scripting.

## Fuente de verdad de las convenciones

**[`.github/copilot-instructions.md`](.github/copilot-instructions.md)** contiene el
molde completo: malla curricular, estructura de cada semana, reglas de longitud,
convenciones de escritura, paleta de los SVG, reglas de seguridad del contenido y el
checklist de publicación de una semana.

Léelo **antes** de generar contenido. No deduzcas el patrón mirando archivos sueltos.

## Generadores

En `.github/prompts/` hay siete plantillas ejecutables:

| Prompt | Genera |
| ------ | ------ |
| `nueva-semana.prompt.md` | El esqueleto completo de una semana |
| `nueva-teoria.prompt.md` | Un archivo de `1-teoria/` |
| `nueva-practica.prompt.md` | Un archivo de `2-practicas/` |
| `nuevo-proyecto.prompt.md` | El `3-proyecto/README.md` de una semana |
| `checks-json.prompt.md` | El `checks.json` de una semana |
| `svg-diagrama.prompt.md` | Un diagrama de `0-assets/` |
| `commit-message.prompt.md` | El mensaje de commit |

## Reglas duras

1. **No inventes nada de la interfaz.** Ni un nombre de menú, ni un ajuste, ni un
   efecto, ni un método de la API. Si no lo puedes verificar, dilo y enlaza el manual
   oficial. Las rutas de menú van completas y en inglés: `Color > Nodes > Add Serial`.

2. **Verifica contra Resolve de verdad.** Este entorno tiene DaVinci Resolve 21
   instalado y un puente MCP en marcha. Antes de afirmar algo sobre v21, compruébalo:
   `resolve_status`, `project_settings`, `timeline_probe`, `media_list`. El servidor
   MCP se llama `resolve`.

3. **Cero absoluto de verdad.** Cada término técnico se define la primera vez que
   aparece. "Log", "LUT", "codec", "alpha" y "headroom" no son vocabulario común.

4. **Free primero.** Todo entregable evaluable tiene que poder hacerse en la versión
   gratuita. Las funciones de Studio se marcan con su bloque de aviso y su alternativa
   en Free. Ojo con un caso concreto: el scripting **externo** es de Studio, el
   scripting **dentro** de Resolve (`Workspace > Scripts`) funciona en Free — por eso
   el verificador está partido en puente y cliente.

5. **Profundidad sobre cobertura.** Mejor tres controles bien explicados que veinte
   listados. Extensión de un archivo de teoría: 200-300 líneas. Si se pasa, es que
   mezcla dos temas: divídelo, no lo recortes.

6. **El porqué antes del cómo.** Ninguna instrucción sin el problema que resuelve.
   Advertencia **antes** del paso irreversible, nunca después.

7. **Todo entregable, verificable.** Por la API (`checks.json`) o por un criterio
   observable escrito en la rúbrica. "Que quede bonito" no es un criterio.

8. **Diagramas en SVG**, con la paleta del bootcamp, tema oscuro, sin degradados, con
   `role="img"` y `aria-label`. Nunca ASCII art. Nunca capturas de pantalla salvo
   stills de referencia de color.

9. **Una semana por tanda.** La Semana 01 es la plantilla de calidad.

## Antes de dar por terminada una tanda

```bash
./scripts/verificar-enlaces.sh
python scripts/verificar-semana.py --doctor
```

El primero comprueba nombres de carpeta, enlaces relativos, navegación, SVG huérfanos
y `checks.json` válido. El segundo comprueba que el entorno de Resolve responde.

## Estructura

```
bootcamp/week-NN-slug/   36 semanas, ver .github/copilot-instructions.md
docs/                    documentación transversal
scripts/                 verificar-enlaces.sh, verificar-semana.py, preparar-medios.sh
assets/                  header del README
```

## Idioma

Español para la prosa y los comentarios educativos. Inglés para la interfaz de
Resolve, los nombres de efectos, el código y los mensajes de commit
(Conventional Commits: `feat(week-01): ...`).
