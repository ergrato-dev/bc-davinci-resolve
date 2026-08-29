# 🤝 Cómo contribuir

Gracias por querer mejorar esto. El material se escribe para gente que empieza de cero,
así que la contribución más valiosa suele ser la más aburrida: una ruta de menú que ya
no existe, un término que se usa sin haberlo definido, un enlace roto.

---

## Qué se acepta

- **Erratas y correcciones.** Ortografía, gramática, enlaces rotos.
- **Rutas de menú y atajos que ya no coinciden** con la versión instalada. Indica **la
  versión exacta** de Resolve donde lo comprobaste.
- **Términos usados sin definir.** Si algo se explica asumiendo vocabulario que el
  bootcamp no ha enseñado todavía, eso es un fallo de contenido y se arregla.
- **Recursos nuevos** para `4-recursos/`, siempre con una línea de por qué valen la pena
  y con su licencia verificada.
- **Trucos** que cumplan el criterio de admisión: ahorran tiempo real o revelan algo que
  la interfaz esconde. Ver `.github/copilot-instructions.md`.
- **Mejoras a los scripts** de `scripts/`.

## Qué no se acepta

- Reescrituras de estilo sin cambio de contenido.
- Semanas nuevas o reordenaciones de la malla curricular sin discusión previa en un
  issue. La malla está dimensionada por horas y cambiarla afecta a las 36 semanas.
- Material con copyright ajeno como recurso de práctica.
- Claves de licencia, números de serie o vías de activación. Ver
  [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- Recomendaciones de plugins de terceros no mantenidos.
- Capturas de pantalla de la interfaz. Envejecen en cada versión; los diagramas van en
  SVG y las rutas de menú en texto. Excepción: *stills* de referencia de color, cuando
  la rúbrica los use como criterio.

---

## Antes de escribir nada

Lee **[`.github/copilot-instructions.md`](.github/copilot-instructions.md)**. Es el
molde completo: estructura de una semana, longitudes, convenciones de escritura, paleta
de los SVG y reglas de seguridad del contenido. Casi todas las revisiones que se piden
en un pull request están ya respondidas ahí.

---

## Flujo

1. **Abre un issue primero** si el cambio es de contenido, no de errata. Ahorra trabajo
   a todo el mundo.
2. Haz un *fork* y crea una rama:

   ```bash
   git switch -c fix/week-01-frame-rate-menu
   ```

   Nombre de rama en inglés, kebab-case, con la semana si aplica.

3. Escribe el cambio. Si tocas contenido de una semana, respeta su estructura.

4. **Verifica antes de abrir el pull request**:

   ```bash
   ./scripts/verificar-enlaces.sh
   ```

   Comprueba nombres de carpeta, enlaces relativos, la sección de navegación de cada
   README, SVG huérfanos y que los `checks.json` sean JSON válido. Tiene que salir
   `OK: sin problemas detectados.`

   Si has tocado un `checks.json`, verifica además que el check **falla** cuando debe:
   rompe el estado a propósito en Resolve y ejecuta

   ```bash
   python scripts/verificar-semana.py NN --check <id>
   ```

   Un check que nunca ha fallado no está probado.

5. Commit siguiendo [Conventional Commits](https://www.conventionalcommits.org/):

   ```
   <tipo>(<alcance>): <descripción>
   ```

   Ejemplos reales:

   ```
   fix(week-01): corrige la ruta de Project Settings en la práctica 02
   docs(free-vs-studio): añade Voice Isolation a la tabla de Fairlight
   feat(week-02): contenido completo de la Semana 02
   ```

   Tipos: `feat`, `fix`, `docs`, `refactor`, `chore`.

6. Abre el pull request describiendo **qué cambia y por qué**, y en qué versión de
   Resolve lo has comprobado.

---

## Checklist antes de abrir el pull request

- [ ] `./scripts/verificar-enlaces.sh` sin errores
- [ ] Las rutas de menú que menciono las he comprobado en Resolve, no deducido
- [ ] Digo en el PR con qué versión exacta de Resolve lo he verificado
- [ ] Cada término técnico nuevo queda definido donde aparece
- [ ] Si toco una función de Studio, lleva su bloque de aviso y su alternativa en Free
- [ ] Los SVG nuevos usan la paleta del bootcamp y están enlazados desde algún `.md`
- [ ] Los trucos nuevos están replicados en `docs/trucos-resolve.md`
- [ ] El commit sigue Conventional Commits

---

## Licencia de las contribuciones

Al contribuir aceptas que tu aportación se publique bajo la misma licencia del
repositorio: [CC BY-NC-SA 4.0](LICENSE).
