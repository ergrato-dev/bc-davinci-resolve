# Práctica 04 — Quick Export y cierre de la Fase 2

> Al terminar tendrás un archivo de vídeo de tu pieza, lo habrás visto fuera de Resolve, lo
> habrás reimportado al proyecto y habrás cerrado la Fase 2 con su respaldo. A partir de aquí
> tu montaje deja de ser una promesa.

**Duración estimada**: 45 min
**Prerrequisitos**: [Práctica 03](03-velocidad-audio-y-titulos.md), [Teoría 09](../1-teoria/09-quick-export.md)

## Contexto

Exportar es la parte fácil: son cuatro clics. La parte que enseña es **ver el archivo**, que
es la primera vez en siete semanas que ves tu trabajo como lo va a ver otra persona: sin
caché, sin proxies, sin la timeline delante y sin saberte lo que viene.

Prepárate para que te decepcione un poco. Es normal, y esa decepción es información: es la
lista de trabajo de la Fase 3.

---

## Paso 1: La revisión final dentro de Resolve

**Por qué**: encontrar aquí lo que se puede arreglar en dos minutos sale más barato que
exportar, ver, arreglar y volver a exportar.

1. Cabezal al principio de `BC-Montaje-v2`
2. **Fast Review** de la pieza entera
3. Mira la **timeline de arriba** con el Boring Detector activado: ¿queda algún rojo? ¿algún
   racimo de gris?
4. Arregla solo lo que sea de dos minutos. Lo demás, a la lista

**Verifica**: no queda ninguna marca roja de uno o dos fotogramas.

---

## Paso 2: Comprobar que la timeline está en condiciones

**Por qué**: exportar una timeline con un hueco produce un archivo con un parpadeo a negro, y
lo vas a descubrir a mitad del visionado.

**Verifica**:

```bash
python scripts/verificar-semana.py 07
```

Ocho de nueve en verde antes de exportar. El noveno, `bin-entregas`, es el paso 6.

---

## Paso 3: Quitar las marcas de la timeline

**Por qué**: si quedan un punto de entrada y uno de salida puestos, Quick Export exporta
**solo ese tramo**, y vas a pensar que el archivo está roto.

1. Comprueba si hay marcas `I` / `O` en la timeline
2. Si las hay, quítalas

**Verifica**: la barra de la timeline no muestra ningún rango marcado.

---

## Paso 4: Exportar

**Por qué**: es el objetivo de la semana y son cuatro pasos.

1. **`File > Quick Export`**
2. Elige el preset **`H.264 Master`**, que es el que abre en cualquier sitio
3. Pulsa **`Export`**
4. Navega hasta `BC-Resolve/03-entregas/` y llámalo:

   ```
   BC-Montaje-v2-semana07.mp4
   ```

5. **`Save`**, y espera a la barra de progreso

> [!NOTE]
> No uses esta semana las opciones de **subida directa** a YouTube, Vimeo o Dropbox, aunque
> estén ahí. Lo que acabas de montar no tiene mezcla, ni color, ni créditos completos: no es
> material para publicar. La publicación es la **Semana 36**.

**Verifica**: el archivo existe en `03-entregas/`. Mira su tamaño: una pieza de cinco minutos
a 1080p sale del orden de **100-300 MB**. Si te salen 5 MB, exportaste un tramo marcado
—vuelve al paso 3.

---

## Paso 5: Verlo fuera de Resolve

**Por qué**: es la mitad del valor de la práctica. Dentro del programa estás viendo la caché,
los proxies y lo que tu ordenador pueda ese día; fuera estás viendo el archivo.

1. Ábrelo con el **reproductor de tu sistema**, no con Resolve
2. Ponte auriculares
3. Ve la pieza **entera**, sin parar, sin adelantar y sin la timeline delante
4. Anota, sin parar la reproducción, lo que vayas viendo

Cuatro cosas concretas que hay que comprobar:

| Qué mirar | Qué debería pasar |
| --------- | ----------------- |
| **Principio y final** | Empieza y acaba donde tenía que hacerlo, sin negro de sobra |
| **Parpadeos a negro** | Ninguno, en toda la pieza |
| **Diálogo** | Se entiende todo sin tocar el volumen |
| **Rótulos** | Se leen, no tapan caras, y duran lo justo |

5. Si puedes, **míralo también en el móvil**. Los rótulos que se leen en un monitor de 27
   pulgadas a veces no se leen en seis.

**Verifica**: tienes una lista escrita de lo que has visto. Si aparece un parpadeo a negro o
un rótulo ilegible, arréglalo en Resolve y **vuelve a exportar** sobrescribiendo el archivo.

---

## Paso 6: Reimportar la entrega al proyecto

**Por qué**: dos razones que no son burocráticas. Si Resolve abre y reproduce el archivo,
está bien escrito. Y en la Semana 36 vas a auditar tu progreso, y tener las entregas de cada
fase dentro del proyecto es lo que hace posible esa auditoría.

1. En el media pool, **clic derecho sobre `Master` > `New Bin`**
2. Llámalo **`12-Entregas`**, con el 12 delante y la E mayúscula
3. **Selecciona ese bin** para que sea el bin activo
4. Importa `BC-Montaje-v2-semana07.mp4` desde el navegador **Media Storage**, con clic derecho
   > `Add into Media Pool`
5. Reprodúcelo en el visor unos segundos

> [!WARNING]
> Si Resolve pregunta si quieres **cambiar el frame rate del proyecto** para que encaje con el
> archivo, di que **no**. Tu proyecto va a 24 fps por una decisión de la Semana 01, y ese
> diálogo es la forma más común de perderla sin enterarse.

**Verifica**:

```bash
python scripts/verificar-semana.py 07 --check bin-entregas
```

---

## Paso 7: Cerrar las notas de montaje

**Por qué**: la Fase 2 termina aquí y la Fase 3 empieza leyendo esto. Lo que no escribas hoy
lo vas a redescubrir en la Semana 09, con tres semanas de retraso.

En `04-respaldos/notas-de-montaje.md`, cierra el apartado `## Acabado — Semana 07` con seis
puntos:

> **Cifras finales**: duración, número de clips en `Video 1`, número de pistas.
>
> **Qué se acabó**: cuántas disolvencias, cuántos `Smooth Cut`, cuántos cambios de velocidad,
> cuántos rótulos.
>
> **Cuánta cola tiene mi material**: el número del paso 1 de la práctica 02. Es el dato que
> decide si la Semana 09 va a ser cómoda o imposible.
>
> **Qué vi al mirar el archivo**: la lista del paso 5, tal cual, sin suavizarla.
>
> **Qué falta grabar**: material recortado, planos repetidos por falta de material, huecos
> que taparías si tuvieras un plano más.
>
> **Qué pasa a la Fase 3**: lo que has visto y no toca todavía, con la semana al lado.

**Verifica**: los seis puntos tienen contenido concreto. El cuarto y el sexto son los que más
valen, y son los que más gente rellena con adjetivos.

---

## Paso 8: El respaldo de la fase

**Por qué**: la Fase 2 se cierra aquí. A partir de la semana que viene se trabaja en la Edit
page y sobre otra copia de la timeline.

1. `Ctrl+S` (Win) / `Cmd+S` (Mac)
2. **`File > Export Project`** →
   `04-respaldos/BC-Bootcamp-Resolve-semana07.drp`

**Verifica**: el `.drp` existe, junto a los de las semanas 03 a 06.

---

## Paso 9: Los nueve checks

**Verifica**:

```bash
python scripts/verificar-semana.py 07
```

Nueve de nueve, con `BC-Montaje-v2` como timeline abierta y el puente lanzado.

Si algo falla antes de eso:

```bash
python scripts/verificar-semana.py --doctor
```

---

## ✅ Resultado

- [ ] Ninguna marca roja de uno o dos fotogramas antes de exportar
- [ ] Sin marcas `I` / `O` en la timeline al exportar
- [ ] `BC-Montaje-v2-semana07.mp4` existe en `03-entregas/`
- [ ] El tamaño del archivo es coherente con la duración de la pieza
- [ ] He visto la pieza entera fuera de Resolve, con auriculares y sin parar
- [ ] La he visto también en una pantalla pequeña
- [ ] El bin `12-Entregas` existe y contiene el archivo
- [ ] `notas-de-montaje.md` cerrado con sus seis puntos
- [ ] `BC-Bootcamp-Resolve-semana07.drp` exportado
- [ ] Los nueve checks en verde

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El archivo dura mucho menos que la pieza | Quedaban marcas `I` / `O` | Paso 3, y vuelve a exportar |
| El archivo ocupa 5 MB | Lo mismo | Lo mismo |
| Hay un parpadeo a negro en el archivo | Un hueco en `Video 1` | Localízalo, bórralo con ripple y reexporta |
| El diálogo se oye a saltos de volumen | Faltó nivelar | Práctica 03, paso 4 |
| Los rótulos no se leen en el móvil | Tamaño insuficiente | Súbelo en el Video Inspector y reexporta |
| Resolve pregunta por el frame rate al importar | El archivo no está a 24 fps, o Resolve lo cree | Di que **no**. Comprueba el preset que usaste |
| `bin-entregas` falla | El bin no existe o el archivo cayó en otro sitio | Nombre exacto `12-Entregas`, colgando de `Master`, y bin activo antes de importar |
| `montaje-v2-activo` falla al final | Te quedaste en `BC-Montaje-v1` comparando | Doble clic en `BC-Montaje-v2` |
| Fallan todos los checks | El puente no está lanzado | `Workspace > Scripts > Utility > resolve_bridge` |
| El archivo no se abre fuera de Resolve | Rara vez el preset, casi siempre el reproductor | Prueba con otro reproductor o con `H.264 Master` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [03 · Velocidad, audio y títulos](03-velocidad-audio-y-titulos.md) | **04 · Quick Export y cierre de la Fase 2** | [Semana 07](../README.md) |

← [Volver a la Semana 07](../README.md)
