# Luana ΓÇö flyer + p├ígina

Dos trabajos, en este repo:

1. **Flyer** (carteleras FASEN/FADA + Instagram) ΓÇö copy cerrado abajo; vos dise├▒├ís.
2. **Hermosear** `templates/page/` (y si da, `templates/card/`) ΓÇö la plantilla es barra + WhatsApp + **el PDF a la vista**. Vos no transcrib├¡s el curr├¡culum.

El flyer **no** es la p├ígina del cliente. El flyer vende. La plantilla es lo que el estudiante publica.

---

## A. Flyer promocional

Copy fijo (se puede acortar; no se cambia precio ni qu├⌐ incluye):

| Campo | Texto |
|---|---|
| Headline | Tu CV, en un link. El reclutador te escribe por WhatsApp. |
| Sub | P├ígina web + PDF + tarjeta con QR. Para estudiantes que buscan pasant├¡a o primer laburo. |
| Precio | **Gs. 200.000** ┬╖ pago ├║nico |
| Letra chica | Incluye 12 meses de hosting. Sin cuota mensual. |
| CTA | Escane├í y escrib├¡. Mand├í tu CV en PDF y en pocos d├¡as ten├⌐s la p├ígina. |
| Contacto | Kyrian Weiss ┬╖ 0985 724 135 (+595 985 724135) |
| Marca | AI Whisperers / paragu-ai CV (no ΓÇ£ErebusΓÇ¥) |

**Vi├▒etas (m├íx. 4):**

- P├ígina CV (un link para tu Instagram / LinkedIn)
- Mismo CV en PDF para postular
- Tarjeta descargable con QR de **tu** link (vos la imprim├¡s)
- 12 meses de hosting incluidos

**Qu├⌐ tienen que mandar (en el flyer, corto):**

1. **Tu CV en PDF** (el que ya ten├⌐s)
2. Tu WhatsApp  

Si la foto del PDF no se ve, se la pedimos por el chat. Nombre y carrera salen del PDF.

**QRs en el flyer**

| QR | Destino | Etiqueta |
|---|---|---|
| 1 | WhatsApp ΓÇö PNG en [`flyer/qr-whatsapp.png`](flyer/qr-whatsapp.png) | Escribime |
| 2 | CV demo de Ana Paula Samaniego ΓÇö PNG en [`flyer/qr-demo.png`](flyer/qr-demo.png) | Mir├í un ejemplo |

URL del QR 1 (ya est├í en el PNG):

`https://wa.me/595985724135?text=Hola%2C%20quiero%20un%20CV%20web`

URL del QR 2 (abrilo en el celular, sin cuenta):

https://ai-whisperers.github.io/paragu-ai-cv/

No pongas alias ni banco en el papel. No pongas Gs. 100.000. No pongas ΓÇ£ErebusΓÇ¥.

**Formatos**

- A4 (o A5) vertical ΓÇö carteleras  
- 1080 ├ù 1350 ΓÇö feed Instagram  
- QRs ΓëÑ ~3 cm de lado en papel  

Estilo: limpio, se lee a 1,5 m. AI como herramienta, no robot caricaturesco.

Entreg├í el arte en este repo (`docs/flyer/arte/`) o Drive, como te quede mejor.

---

## B. Hermosear la p├ígina

Archivos: [`templates/page/index.html`](../templates/page/index.html) y [`templates/page/styles.css`](../templates/page/styles.css).

Demo de c├│mo se ve rellenada (PDF real), **ya online**:

https://ai-whisperers.github.io/paragu-ai-cv/

Misma p├ígina en el repo: [`demos/ana-samaniego/`](../demos/ana-samaniego/).

**Tiene que quedar (no sacar):**

- El **PDF del alumno visible** en la p├ígina (no solo un link de descarga)
- Bot├│n **WhatsApp** (link `wa.me` del estudiante)
- Bot├│n **Tarjeta** (baja `tarjeta.pdf`, 90├ù50 mm, QR de esa p├ígina)

**Pod├⌐s cambiar:** barra de arriba, colores, tipo, c├│mo se ve el bot├│n. El CV en s├¡ no se redise├▒a en v1: se muestra el PDF que mandaron.

**No hace falta:** transcribir el CV a secciones, men├║, login, listado de alumnos.

La tarjeta: [`templates/card/`](../templates/card/) ΓÇö 90├ù50 mm, nombre + rol + QR del **link de esa persona**. El QR lo genera el script; vos defin├¡s c├│mo se ve la tarjeta alrededor.

---

Plazo que mencionaste para el flyer: ~2 d├¡as una vez cerrado este brief.
