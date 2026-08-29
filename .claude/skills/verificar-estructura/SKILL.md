---
name: verificar-estructura
description: Comprueba que una semana del bootcamp DaVinci Resolve 21 está completa y bien enlazada antes de publicarla. Úsalo al terminar una semana o antes de abrir un pull request.
---

# Verificar estructura de una semana

Comprueba que `bootcamp/week-NN-*/` cumple el molde antes de darla por terminada.

## 1. Lo automático primero

```bash
./scripts/verificar-enlaces.sh
```

Cubre: nombres de carpeta `week-NN-slug`, enlaces relativos que resuelven, sección
`Navegación` en cada README de semana, SVG huérfanos y `checks.json` como JSON válido.

Tiene que salir `OK: sin problemas detectados.` Si no, arréglalo antes de seguir.

## 2. Archivos que tienen que existir

```
week-NN-slug/
├── README.md                 ← obligatorio
├── rubrica-evaluacion.md     ← obligatorio
├── checks.json               ← obligatorio
├── 0-assets/*.svg            ← al menos uno, todos enlazados
├── 1-teoria/*.md             ← 7 u 8; en Color y Fusion pueden ser 9
├── 2-practicas/*.md          ← 4 o 5
├── 3-proyecto/README.md      ← obligatorio
├── 4-recursos/ebooks-free/README.md
├── 4-recursos/videografia/README.md
├── 4-recursos/webgrafia/README.md
└── 5-glosario/README.md      ← obligatorio
```

## 3. Las 10 secciones del README, en orden

1. `# Semana NN — Título` + blockquote gancho de una línea
2. `## 🎯 Objetivos de la Semana`
3. `## 📋 Prerrequisitos`
4. `## 🗂️ Estructura de la Semana`
5. `## 📝 Contenidos`
6. `## ⏱️ Distribución del Tiempo (10 horas)`
7. `## 🎩 Trucos y atajos`
8. `## 📌 Entregables`
9. `## ✅ Verificación`
10. `## 🔗 Navegación`

Opcional entre 6 y 7 si la semana toca funciones de pago:
`## 💠 Qué necesita Studio esta semana`.

## 4. Comprobaciones que el script no hace

- **Las horas suman 10 exactas** en la sección 6, y cuadran con las duraciones de la 5.
- **Cada teoría mide entre 200 y 300 líneas**:

  ```bash
  wc -l bootcamp/week-NN-*/1-teoria/*.md
  ```

- **Cada práctica** tiene, en cada paso, su **Por qué** y su **Verifica**.
- **Los pasos irreversibles** llevan advertencia **antes**, no después.
- **Los nombres literales** (`BC-...`) coinciden entre `3-proyecto/README.md` y
  `checks.json`, carácter a carácter.
- **La rúbrica** tiene el cuestionario con sus respuestas en `<details>`.
- **El glosario** es A-Z y da el término inglés de la interfaz entre paréntesis.
- **Los trucos** del README están replicados en `docs/trucos-resolve.md`.
- **Los recursos** llevan cada uno su línea de por qué vale la pena.
- **La navegación** apunta a las semanas contigua anterior y siguiente, y existen.

## 5. Informe

Lista de lo que falta, con la ruta. Sin elogios y sin proponer contenido: solo lo que
impide dar la semana por publicada.
