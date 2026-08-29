# 🎬 El proyecto hilo conductor

> Las prácticas semanales son ejercicios: se hacen, se comprueban y se tiran. El
> proyecto hilo conductor es lo contrario: **una sola pieza que crece durante 36
> semanas** y que al final es lo que enseñas cuando alguien te pregunta qué sabes hacer.

---

## 1. Por qué un solo proyecto

Un bootcamp de nueve meses hecho a base de ejercicios sueltos se abandona en el mes
tres. Se abandona porque nada de lo que haces sobrevive a la semana siguiente.

Aquí no. Todo lo que aprendes se aplica **a tu pieza**, la misma desde la Semana 01
hasta la 36. En la semana 12 tienes un montaje. En la 15, montaje con sonido. En la 22,
montaje con sonido y color. En la 36, una pieza terminada, entregada en varios formatos
y archivada como se archiva un trabajo real.

Además, los problemas interesantes solo aparecen cuando el proyecto es grande. Nadie
necesita bins organizados con seis clips; con doscientos, sí.

---

## 2. Elige tu pieza en la Semana 01

Antes de importar nada, decides **qué vas a hacer**. Cinco formatos que funcionan bien
con este temario:

| Formato | Duración objetivo | Qué te va a enseñar mejor |
| ------- | ----------------- | ------------------------- |
| **Documental corto** | 5-8 min | Organización de mucho material, entrevista, sonido de ambiente, corrección de material dispar |
| **Videoclip** | 3-4 min | Ritmo de montaje, sincronía con música, look de color agresivo, efectos |
| **Cortometraje de ficción** | 5-10 min | Continuidad, diálogo, ADR, etalonaje narrativo, algún plano con VFX |
| **Tutorial o vídeo formativo** | 8-12 min | Multicámara, gráficos, subtítulos, claridad de audio, entrega para plataforma |
| **Pieza de viaje o vlog** | 4-6 min | Volumen alto de material, selección, música, color de exteriores |

Reglas para elegir bien:

- **Que puedas grabarlo tú.** El móvil sirve para las cinco opciones.
- **Que te importe.** Vas a verlo doscientas veces.
- **Que sea corto.** Cinco minutos bien acabados enseñan más que veinte a medias.
- **Que tenga alguien hablando.** Si no hay voz, te pierdes media Fase 4.

> [!TIP]
> Si dudas, elige **documental corto sobre algo que tengas cerca**: un oficio, un
> lugar, una persona. Es el formato que más partes del temario activa y el que menos
> depende de tener actores o una banda.

---

## 3. Qué capa añade cada fase

| Fase | Semanas | Qué tiene tu proyecto al terminarla |
| ---- | ------- | ----------------------------------- |
| 0 · Fundamentos | 01-03 | Decidido el formato, el frame rate y la resolución. Proyecto de Resolve creado y configurado |
| 1 · Media | 04-05 | Todo el material ingestado, organizado en bins con metadata, con proxies generados |
| 2 · Cut | 06-07 | Un primer montaje bruto de principio a fin. Feo, pero completo |
| 3 · Edit | 08-12 | El montaje fino: ritmo, trimming, títulos, transiciones, subtítulos |
| 4 · Fairlight | 13-15 | Diálogo limpio, música, efectos y ambientes, mezclado a un target de loudness |
| 5 · Color | 16-22 | Etalonaje completo: balance, igualado entre planos, look, y control de calidad |
| 6 · Fusion | 23-27 | Los planos que necesitan composición: cleanup, un key, una pieza de motion graphics |
| 7 · Deliver | 28-29 | Master y entregas para al menos tres destinos distintos |
| 8 · Gestión | 30 | Proyecto archivado y reproducible en otra máquina |
| 9 · Scripting | 31-34 | Tu pipeline automatizado: ingesta, marcadores y render por script |
| 10 · Cierre | 35-36 | La pieza terminada, auditada y publicada |

> [!IMPORTANT]
> **El montaje bruto de la Fase 2 tiene que estar completo de principio a fin.** No
> "los tres primeros minutos bien". Un montaje incompleto arrastra el problema a las
> ocho fases siguientes: no se puede mezclar lo que no está montado, ni etalonar lo que
> no está mezclado.

---

## 4. Convenciones de nombres

El verificador localiza tus entregables por el nombre. No es decorativo:

| Elemento | Nombre exacto |
| -------- | ------------- |
| Proyecto de Resolve | `BC-Bootcamp-Resolve` |
| Timeline de montaje | `BC-Montaje-v1`, `BC-Montaje-v2`… |
| Timeline de color | `BC-Color-v1` |
| Timeline de entrega | `BC-Master` |
| Bins del media pool | `01-Basicos`, `02-Entrevista`, `03-Multicamara`… (igual que las carpetas del pack) |

Cada semana te dirá qué nombre concreto espera. Cuando dudes, mira el `checks.json` de
la semana: ahí está el nombre literal que se comprueba.

---

## 5. Versiona, no sobrescribas

Cuando una fase termina, **duplica la timeline** antes de empezar la siguiente
(`clic derecho sobre la timeline en el media pool > Duplicate Timeline`) y trabaja sobre
la copia. Así:

- Puedes volver atrás si una decisión de la fase 5 estropea algo de la fase 3.
- Puedes comparar el antes y el después, que es como se aprende a ver la diferencia.
- Tienes evidencia de tu progreso para la auditoría de la Semana 36.

Y exporta el proyecto entero (`File > Export Project`) a `04-respaldos/` al terminar
cada fase. Un `.drp` pesa poco y te salva de un corte de luz.

---

## 6. Si te atascas

- **No tienes material suficiente.** Grábalo. Cada fase te dice qué necesitas y el móvil
  basta. Ver [pack-de-medios.md](pack-de-medios.md).
- **Tu pieza no te gusta.** Normal en la semana 10. Cámbiala si quieres, pero solo una
  vez, y antes de la Semana 13: después, el coste de rehacer el montaje es alto.
- **Vas atrasado.** Prioriza el proyecto sobre las prácticas. Las prácticas se pueden
  recuperar; una fase del proyecto sin hacer bloquea todas las siguientes.

---

## ✅ Checklist de verificación

- [ ] He elegido formato y tema de mi pieza
- [ ] Es algo que puedo grabar yo, y me importa
- [ ] Dura entre 3 y 12 minutos
- [ ] Tiene al menos una persona hablando
- [ ] He creado el proyecto `BC-Bootcamp-Resolve` en Resolve
- [ ] Sé qué capa añade cada fase y en qué orden

---

← [Volver a la documentación](README.md) · [Volver al inicio del bootcamp](../README.md)
