# Práctica 02 — El título principal y los rótulos

> Al terminar tendrás el título de entrada de tu pieza, dos rótulos de identificación con el mismo
> estilo, y ese estilo guardado en el media pool para no volver a construirlo nunca. Los tres,
> legibles sobre cualquier fondo y dentro del título seguro.

**Duración estimada**: 60 min
**Prerrequisitos**: [Práctica 01](01-la-copia-y-el-mapa-de-rotulos.md), [Teoría 02](../1-teoria/02-text-frente-a-text-plus.md), [Teoría 03](../1-teoria/03-los-cuatro-paneles-de-text-plus.md), [Teoría 05](../1-teoria/05-legibilidad-safe-areas-y-contraste.md)

## Contexto

El orden de esta práctica no es casual: **primero se construye un rótulo bien, y después se copia
quince veces**. Al revés —quince rótulos y luego arreglarlos— son quince arreglos.

Y la decisión de generador se toma una vez, con la pregunta de la teoría 02: **¿este rótulo
necesita varios estilos en el mismo bloque, o necesita animarse?**

---

## Paso 1: Crear el bin de títulos

**Por qué**: el título con tu estilo y el compuesto de la práctica 04 son elementos del media pool
sin archivo en disco. Si no tienen bin propio, acaban sueltos en `Master`.

1. En el media pool, clic derecho sobre **`Master`** `>` `Add Bin`
2. Renómbralo exactamente **`13-Titulos`** — sin tilde, con el 13 delante y la T mayúscula

**Verifica**: el bin cuelga de `Master` y está vacío.

---

## Paso 2: El título de entrada

**Por qué**: es el rótulo que más se mira y el único que se ve sin nada más en pantalla. Vale la
pena hacerlo con calma.

Ve al primer marcador **amarillo** de la práctica 01.

1. `Effects Library > Toolbox > Titles`
2. Arrastra **`Text+`** a la pista **`V2`**, sobre el tramo donde va
3. `Inspector > Title > Styled Text`: escribe el título de tu pieza
4. **`Font`**: una sans-serif de peso medio o negrita. Si dudas, la que ya tenga tu sistema y sea
   legible
5. **`Size`**: que se lea al reducir el visor a un cuarto
6. **`Color`**: blanco o el color de tu pieza
7. Colócalo **dentro del rectángulo `Title`**

**Verifica**: reduce el visor a un cuarto de su tamaño. Si el título se lee, está bien
dimensionado.

> [!TIP]
> Si tu título necesita **dos estilos** —el nombre grande y un subtítulo pequeño debajo—, `Text+` no
> te lo va a dar: comparte un solo estilo. Usa `Text`, que sí admite rich text, o pon dos `Text+`,
> uno en la `V2` y otro en la `V3`. La decisión está en la teoría 02.

---

## Paso 3: Hacerlo legible con contorno y sombra

**Por qué**: un rótulo sin contorno se lee mientras el fondo sea oscuro. En cuanto el plano se abre
a un cielo, desaparece.

1. `Inspector > Title > Shading`
2. Desplegable **`Shading Element`** `>` elemento **`2`**
3. Marca **`Enabled`**
4. Apariencia: **contorno**
5. `Color` negro, `Thickness` bajo, y marca **`Outside Only`**
6. Elemento **`3`**, `Enabled`, apariencia **sombra**, negro, opacidad alrededor del 50 %,
   `Position Y` desplazada un poco
7. Ponle nombre a cada elemento en su campo `Name`: `contorno` y `sombra`

**Verifica**: **reproduce el tramo entero** del título. Si en algún fotograma se pierde, sube el
grosor del contorno o la opacidad de la sombra.

---

## Paso 4: Animar la entrada y la salida

**Por qué**: un rótulo que aparece y desaparece de golpe da un salto visual. Y esta es la parte que
`Text+` hace y `Text` no.

Elige **una** de las dos vías:

**A · Fundido, que vale para cualquier rótulo**

1. `Inspector > Settings > Composite`
2. Cabezal al primer fotograma. `Opacity` a `0`, pulsa su **rombo**
3. Doce fotogramas después, `Opacity` a `100`
4. Al final, al revés

**B · `Write On`, que es el propio de `Text+`**

1. `Inspector > Title > Write On`
2. Cabezal al primer fotograma. El **final** del rango a `0`, y pulsa su rombo
3. Un segundo después, el final del rango a `1`
4. Para que salga: el **principio** del rango, de `0` a `1`, al final del clip

**Verifica**: reproduce con `/`. El título entra y sale sin dar un salto.

---

## Paso 5: Guardar el estilo en el media pool

**Por qué**: aquí es donde se ahorra la semana. Todo lo que acabas de construir —tipografía,
contorno, sombra, posición y keyframes— se guarda de una vez y se reutiliza.

1. Selecciona el bin **`13-Titulos`** en el media pool
2. Selecciona el título en la timeline
3. **Arrástralo desde la timeline hasta el media pool**
4. Doble clic sobre su nombre en el media pool y llámalo **`BC-Estilo-Rotulo`**

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check bin-de-titulos
```

Todavía va a fallar: pide **dos** elementos y de momento tienes uno. El segundo es el compuesto de
la práctica 04.

> [!NOTE]
> El manual lo confirma: al arrastrar un título de la timeline al media pool se guarda como un clip
> aparte, con miniatura del texto que contiene, y **si tenías keyframes, los keyframes se guardan
> también**. Es un clip del media pool sin archivo en disco, igual que una timeline.

---

## Paso 6: Los rótulos de identificación, reutilizando el estilo

**Por qué**: es la operación que vas a repetir el resto del bootcamp, y hacerla bien una vez la
convierte en treinta segundos por rótulo.

Para cada uno de los marcadores amarillos que quedan:

1. **Doble clic** sobre `BC-Estilo-Rotulo` en el media pool: se abre en el visor de origen
2. Marca `I` y `O` en la timeline sobre el tramo donde va el rótulo
3. Comprueba que el **control de destino** apunta a la **`V2`**
4. Edítalo con `Overwrite` — arrastrando al overlay del visor, o con la tecla de sobrescritura
5. Selecciona el rótulo recién puesto y **cámbiale el texto** en
   `Inspector > Title > Styled Text`: copia el nombre del marcador
6. Ajusta la posición si el fondo de ese plano lo pide

Repítelo hasta tener **al menos tres clips en la `V2`**: el título de entrada y dos rótulos.

**Verifica**:

```bash
python scripts/verificar-semana.py 11 --check rotulos-en-v2
```

> [!TIP]
> Si en algún plano el rótulo choca con algo de la imagen, **muévelo, no lo encojas**. Un rótulo
> pequeño no se lee; un rótulo colocado en el otro lado del cuadro, sí. Y `Shift` mientras arrastras
> te lo mantiene en el mismo eje.

---

## Paso 7: Probar un `Fusion Title`, y decidir

**Por qué**: hay que haber usado uno para saber qué se gana y qué se pierde. Y hay que decidir a
conciencia si se queda.

1. `Effects Library > Toolbox > Titles`, sección **`Fusion Titles`**
2. Con `Hover Scrub Preview` marcado, pasa el ratón **a lo largo** de varias miniaturas
3. Arrastra una a la `V2`, en un tramo libre
4. Mira su `Inspector`: **¿qué controles te deja tocar?**
5. Reproduce. **¿Se ha caído la reproducción?**

Y decide:

| Si… | Entonces |
| --- | -------- |
| Te da lo que necesitas y encaja con el resto | Déjalo, y anota por qué en las notas |
| Le falta un control que necesitas | Bórralo: no se arregla |
| Rompe la coherencia con tus otros rótulos | Bórralo |

Si la reproducción se te ha caído: `Playback > Render Cache > Smart`, y espera a que la barra de
encima de la timeline se ponga azul.

**Verifica**: sabes decir, con una frase, por qué se queda o por qué no.

---

## Paso 8: Repasar ortografía y cerrar

**Por qué**: una falta en un rótulo se ve más que cualquier otra cosa de la pieza, y el corrector ya
te la está señalando.

1. Reproduce la pieza mirando **solo** los rótulos
2. Clic derecho sobre cualquier palabra subrayada en rojo para ver sugerencias
3. Cuando esté limpio: `View > Show Spelling Errors on Viewer` para apagar los subrayados
4. Cierra el bloque de notas:

```markdown
### Los rótulos — práctica 02
- Generador elegido para el título de entrada: __ · por qué: __
- Fuente y cuerpo: __
- Contorno: __ · sombra: __
- Animación de entrada: Opacity / Write On
- Rótulos colocados: __
- ¿Probaste un Fusion Title? __ · ¿se queda? __ · por qué: __
```

5. `Ctrl+S` / `Cmd+S`

**Verifica**:

```bash
python scripts/verificar-semana.py 11
```

---

## ✅ Resultado

- [ ] Bin `13-Titulos` creado
- [ ] Título de entrada hecho con el generador que decidiste, y sabes por qué ese
- [ ] Contorno y sombra puestos, comprobados reproduciendo el tramo entero
- [ ] Entrada y salida animadas
- [ ] `BC-Estilo-Rotulo` guardado en `13-Titulos`
- [ ] Tres clips o más en la `V2`, todos dentro del rectángulo `Title`
- [ ] Un `Fusion Title` probado, y la decisión de si se queda escrita
- [ ] Ortografía repasada y subrayados apagados
- [ ] Bloque de notas de la práctica 02 cerrado

---

## 🧯 Si algo sale mal

| Síntoma | Causa | Solución |
| ------- | ----- | -------- |
| El título ha tapado un plano | Cayó en la `V1` | `Ctrl+Z`, comprueba el control de destino y repite en la `V2` |
| `rotulos-en-v2` falla con rótulos puestos | Están en otra pista | Arrástralos a la `V2` |
| No encuentro `Size` ni `Font` | Estás en el panel `Settings` | Pestaña `Title` |
| Cambio el color y cambia todo el texto | Es un `Text+`: un solo estilo | Es su comportamiento; usa `Text` si necesitas varios |
| Cambio el color y no cambia nada | Es un `Text` y no habías seleccionado texto | Selecciona antes de tocar el estilo |
| El rótulo se pierde sobre algunos planos | Falta contorno o sombra | Paso 3 |
| No puedo editar el texto en el visor de un `Text+` | Falta el overlay | Desplegable de overlays del visor `>` `Fusion Overlay` |
| El estilo guardado no aparece en `13-Titulos` | El bin activo era otro | Selecciona `13-Titulos` y vuelve a arrastrar |
| La reproducción va a tirones | Un `Fusion Title` | `Playback > Render Cache > Smart` |
| Cada rótulo tiene un tamaño distinto | Se hicieron uno a uno | Bórralos y colócalos desde `BC-Estilo-Rotulo` |

---

| Anterior | Actual | Siguiente |
| -------- | ------ | --------- |
| [01 · La copia y el mapa de rótulos](01-la-copia-y-el-mapa-de-rotulos.md) | **02 · El título principal y los rótulos** | [03 · Transiciones y ResolveFX](03-transiciones-y-resolvefx.md) |

← [Volver a la Semana 11](../README.md)
