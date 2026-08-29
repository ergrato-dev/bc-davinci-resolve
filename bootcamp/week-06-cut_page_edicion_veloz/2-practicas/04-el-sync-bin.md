# Práctica 04 — El sync bin

> Al terminar habrás montado una escena de tres cámaras eligiendo ángulos con la vista
> puesta en el montaje, no buscándolos a mano. Y sabrás en treinta segundos si el material
> de varias cámaras que te llegue el año que viene se puede montar así o no.

**Duración estimada**: 50 min
**Prerrequisitos**: [Práctica 03](03-corregir-el-montaje.md), [Teoría 09](../1-teoria/09-el-sync-bin.md), el bin `03-Multicamara` de la [Semana 05](../../week-05-proxies_cache_y_sincronizacion/README.md)

## Contexto

Esta práctica usa el material de tres ángulos que ingestaste en la Semana 05. Se hace en
una timeline aparte, `BC-Sync-Cut-v1`, por dos razones: para no tocar el montaje de las
prácticas anteriores, y porque no todas las piezas del bootcamp tienen una escena
multicámara dentro.

> [!NOTE]
> Si tu pieza sí lleva material de varias cámaras, lo que montes aquí se incorpora a
> `BC-Montaje-v1` en la Semana 07. Si no lo lleva, esta práctica sigue siendo obligatoria:
> el sync bin aparece en cualquier trabajo con más de una cámara, y la Semana 12 lo da por
> sabido.

---

## Paso 0: Si no tienes material de tres cámaras

**Por qué**: se graba en quince minutos y sin él la práctica no se puede hacer.

Con un móvil y dos aparatos más —otro móvil, una cámara, lo que haya—:

1. Coloca los tres en sitios distintos, apuntando a la misma escena
2. Ponlos a grabar **antes** de que empiece nada, y déjalos grabando hasta el final
3. Da una palmada delante de los tres al empezar
4. Graba dos o tres minutos de algo con voz: alguien contando cualquier cosa

Importa esos tres clips en el bin **`03-Multicamara`** de tu proyecto.

**Verifica**:

```bash
python scripts/verificar-semana.py 05 --check bin-multicamara
```

Es un check de la Semana 05: el bin y su contenido son de aquella semana, y esta práctica
solo los reutiliza.

---

## Paso 1: Comprobar si la hora de grabación sirve

**Por qué**: el sync bin alinea por hora de grabación, y si esa hora no es coherente entre
cámaras alinea mal **en silencio**. Comprobarlo cuesta treinta segundos y ahorra una tarde.

1. En el media pool, vista de lista
2. Muestra la columna de **fecha y hora de grabación** de los tres clips
3. Compara: ¿coinciden en el día y en la hora aproximada?

**Verifica**: los tres clips dicen que se grabaron el mismo día, a la misma hora, con unos
minutos de diferencia como mucho.

> [!IMPORTANT]
> Si un clip dice otra hora o no dice ninguna, **no montes con el sync bin**: monta con el
> clip multicámara que creaste en la Semana 05, que se sincronizó por forma de onda y no
> depende de los relojes. Lo importante de este paso es saber distinguir los dos casos.

---

## Paso 2: Crear la timeline de la escena

1. `File > New Timeline`, vacía
2. Nómbrala exactamente **`BC-Sync-Cut-v1`**
3. Comprueba que hereda los 24 fps del proyecto

**Verifica**:

```bash
python scripts/verificar-semana.py 06 --check timeline-sync-cut-existe
```

---

## Paso 3: Montar la base con la cámara del mejor sonido

**Por qué**: el audio de la pieza sale de esta pista. La cámara del mejor sonido casi
nunca es la del plano más bonito, y elegir por la imagen es el error clásico.

1. Escucha los tres ángulos y decide cuál tiene el sonido más limpio
2. Selecciona ese clip, márcalo con `I` y `O` abarcando la escena entera
3. **Append**

**Verifica**: la timeline tiene un solo clip, con su audio, y suena bien de principio a
fin.

---

## Paso 4: Activar el sync bin

**Por qué**: es el cambio de vista que convierte el media pool en una respuesta a "qué
grababan las otras cámaras aquí".

1. Activa el **sync bin** desde el media pool de la Cut page
2. Mueve el cabezal por la timeline y observa cómo cambia lo que muestra

**Verifica**: al mover el cabezal, la vista enseña los ángulos que estaban grabando en ese
instante.

---

## Paso 5: La comprobación del punto reconocible

**Por qué**: es la prueba de que la alineación es real. Sin ella, todo lo que montes puede
estar desplazado y no lo sabrás hasta el final.

1. Coloca el cabezal en la **palmada** del paso 0, o en cualquier momento reconocible
2. Mira los ángulos que ofrece el sync bin
3. Comprueba que enseñan **ese mismo instante**

**Verifica**: los tres ángulos muestran la palmada. Si uno enseña otra cosa, su hora de
grabación no es fiable: móntalo con el clip multicámara de la Semana 05 y anótalo en tus
notas.

---

## Paso 6: Colocar el primer ángulo

**Por qué**: es el ciclo entero, una vez. Los siguientes son repetición.

1. Cabezal en un momento donde otro ángulo cuente mejor lo que pasa
2. En el sync bin, selecciona ese ángulo
3. Pulsa **Source Overwrite**

**Verifica**: el ángulo aparece en la pista de encima, **sincronizado**: reproduce el
punto de unión y comprueba que la voz no salta ni se repite ninguna sílaba.

> [!WARNING]
> Si al reproducir oyes eco o la voz doblada, están sonando dos pistas de audio a la vez.
> Silencia el audio del ángulo que acabas de colocar: en un montaje de varias cámaras suena
> una sola pista, la de la base.

---

## Paso 7: Montar la escena entera

**Por qué**: un solo cambio de ángulo no enseña nada. El oficio está en decidir cuándo
cambiar.

Repite el paso 6 a lo largo de la escena. Cambia de ángulo cuando:

- Pase algo que se vea mejor desde otro sitio
- El plano lleve entre diez y veinte segundos sin cambiar, en material hablado
- Haya un salto que tapar

**Verifica**: reproduces la escena entera y el sonido es continuo, sin saltos ni ecos,
mientras la imagen cambia varias veces.

---

## Paso 8: Comprobar el resultado

1. **Fast Review** sobre `BC-Sync-Cut-v1`
2. Comprueba tres cosas: el sonido es continuo, no hay dos ángulos seguidos que enseñen lo
   mismo, y ningún ángulo dura tanto que canse

**Verifica**: puedes ver la escena entera sin que nada te chirríe en el cambio de ángulo.

---

## Paso 9: Cerrar la semana

1. Vuelve a abrir **`BC-Montaje-v1`** con doble clic: los checks leen la timeline activa
2. Actualiza `notas-de-montaje.md` con lo que hayas aprendido del material multicámara: si
   la hora de grabación era fiable, qué cámara lleva el mejor sonido, cuántos cambios de
   ángulo montaste
3. `Ctrl+S` (Win) / `Cmd+S` (Mac)
4. `File > Export Project` → `04-respaldos/BC-Bootcamp-Resolve-semana06.drp`
5. Ejecuta la semana entera:

```bash
python scripts/verificar-semana.py 06
```

**Verifica**: los ocho checks en verde.

---

## ✅ Resultado

- [ ] `03-Multicamara` tiene tres clips o más
- [ ] He comprobado la hora de grabación de los tres antes de montar
- [ ] `BC-Sync-Cut-v1` existe, a 24 fps
- [ ] La base está montada con la cámara del mejor sonido
- [ ] He hecho la comprobación del punto reconocible
- [ ] Los ángulos están colocados con Source Overwrite, en la pista de encima
- [ ] Suena una sola pista de audio: sin eco ni voz doblada
- [ ] `BC-Montaje-v1` vuelve a ser la timeline abierta
- [ ] `notas-de-montaje.md` actualizado y respaldo exportado
- [ ] Los ocho checks de la semana en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El sync bin no enseña nada | El bin seleccionado no es el del material | Selecciona `03-Multicamara` |
| Los ángulos no corresponden al instante | La hora de grabación no es coherente | Monta con el clip multicámara de la Semana 05 |
| Se oye eco o la voz doblada | Suenan dos pistas de audio a la vez | Silencia el audio de los ángulos colocados encima |
| El ángulo cae desplazado | Usaste Place on Top en vez de Source Overwrite | Deshaz: Source Overwrite alinea por hora de grabación |
| La vista está llena de material que no viene a cuento | Hay varias escenas en el mismo bin | Un bin por escena o por jornada |
| Los tres ángulos empiezan en momentos distintos | Normal: arrancaron a destiempo | El sync bin lo refleja; elige lo que haya en cada instante |
| Fallan todos los checks | El puente no está lanzado, o `BC-Sync-Cut-v1` sigue abierta | `Workspace > Scripts > Utility`, y abre `BC-Montaje-v1` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Corregir el montaje](03-corregir-el-montaje.md) | **04 · El sync bin** | — |

← [Volver a la Semana 06](../README.md)
