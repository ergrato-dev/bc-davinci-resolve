# 🔒 Política de Seguridad

Este repositorio es **material educativo**, no un producto en producción. Aun así
contiene scripts que hablan con DaVinci Resolve y con un puente HTTP local, así que
trata los reportes de seguridad con seriedad.

## Qué reportar

| Tipo | Ejemplo | Canal |
| ---- | ------- | ----- |
| Secreto expuesto en este repo | Un token del puente commiteado por error | **Privado** (ver abajo) |
| Fallo en `verificar-semana.py` o en `preparar-medios.sh` que pueda dañar datos | Un script que escribe donde no debe | **Privado** |
| Ejemplo que enseña una práctica insegura | Un script que expone el puente a la red sin advertirlo | Issue público |
| Enlace de descarga que apunta a algo que no es lo que dice | Una fuente del pack de medios comprometida | **Privado** |
| Errata, ruta de menú equivocada, enlace roto | Cualquier error de contenido | Issue público |

Regla: si publicarlo aumenta el daño, va en privado. Si publicarlo solo mejora el
material, va en issue público.

## Cómo reportar en privado

1. **Preferido**: pestaña `Security` → `Report a vulnerability` (private vulnerability
   reporting) del repositorio.
2. Alternativa: correo a **elparcheti@gmail.com** con asunto
   `[SECURITY] bc-davinci-resolve`.

Incluye: archivo y línea, impacto concreto, y pasos para reproducirlo.

**Tiempo de respuesta esperado**: primer acuse en 7 días naturales.

## Seguridad del puente de scripting

El verificador del bootcamp habla con un puente HTTP que corre **dentro** de Resolve.
Dos cosas que conviene tener claras y que se explican a fondo en la Semana 34:

1. **El puente escucha en `127.0.0.1`, no en la red.** Si lo expones a la red local,
   cualquiera en esa red puede pedirle que haga cosas en tu Resolve. No lo hagas sin
   saber exactamente lo que implica.
2. **El token del puente es una credencial.** Vive en un archivo de tu perfil de
   usuario, y `.gitignore` ya lo excluye. Si alguna vez acaba en un commit, rótalo
   —borra el archivo del token y relanza el puente, que generará uno nuevo— **antes**
   de limpiar la historia. El orden importa: borrar el commit sin rotar el token solo
   da una falsa sensación de seguridad.

El propio Resolve avisa de esto: su documentación de scripting recomienda pensárselo
dos veces antes de permitir scripting desde fuera de la máquina.

## Fuera de alcance

- Fallos de DaVinci Resolve como producto → repórtalos a Blackmagic Design a través de
  su [página de soporte](https://www.blackmagicdesign.com/support/), no aquí.
- Fallos del servidor MCP de terceros que uses para conectarte a Resolve → repórtalos a
  ese proyecto.
- Problemas con las plataformas que alojan el material de práctica → a esas plataformas.
