# Luana — flyer + página

Dos trabajos, en este repo:

1. **Flyer** (carteleras FASEN/FADA + Instagram) — copy cerrado abajo; vos diseñás.
2. **Hermosear** `templates/page/` (y si da, `templates/card/`) — la plantilla es barra + WhatsApp + **el PDF a la vista**. Vos no transcribís el currículum.

El flyer **no** es la página del cliente. El flyer vende. La plantilla es lo que el estudiante publica.

---

## A. Flyer promocional

Copy fijo (se puede acortar; no se cambia precio ni qué incluye):

| Campo | Texto |
|---|---|
| Headline | Tu CV, en un link. El reclutador te escribe por WhatsApp. |
| Sub | Página web + PDF + tarjeta con QR. Para estudiantes que buscan pasantía o primer laburo. |
| Precio | **Gs. 200.000** · pago único |
| Letra chica | Incluye 12 meses de hosting. Sin cuota mensual. |
| CTA | Escaneá y escribí. Mandá tu CV en PDF y en pocos días tenés la página. |
| Contacto | Kyrian Weiss · 0985 724 135 (+595 985 724135) |
| Marca | AI Whisperers / paragu-ai CV (no “Erebus”) |

**Viñetas (máx. 4):**

- Página CV (un link para tu Instagram / LinkedIn)
- Mismo CV en PDF para postular
- Tarjeta descargable con QR de **tu** link (vos la imprimís)
- 12 meses de hosting incluidos

**Qué tienen que mandar (en el flyer, corto):**

1. **Tu CV en PDF** (el que ya tenés)
2. Tu WhatsApp  

Si la foto del PDF no se ve, se la pedimos por el chat. Nombre y carrera salen del PDF.

**QRs en el flyer**

| QR | Destino | Etiqueta |
|---|---|---|
| 1 | WhatsApp — PNG en [`flyer/qr-whatsapp.png`](flyer/qr-whatsapp.png) | Escribime |
| 2 | CV demo de Ana Paula Samaniego — PNG en [`flyer/qr-demo.png`](flyer/qr-demo.png) | Mirá un ejemplo |

URL del QR 1 (ya está en el PNG):

`https://wa.me/595985724135?text=Hola%2C%20quiero%20un%20CV%20web`

URL del QR 2 (abrilo en el celular, sin cuenta):

https://ai-whisperers.github.io/paragu-ai-cv/

No pongas alias ni banco en el papel. No pongas Gs. 100.000. No pongas “Erebus”.

**Formatos**

- A4 (o A5) vertical — carteleras  
- 1080 × 1350 — feed Instagram  
- QRs ≥ ~3 cm de lado en papel  

Estilo: limpio, se lee a 1,5 m. AI como herramienta, no robot caricaturesco.

Entregá el arte en este repo (`docs/flyer/arte/`) o Drive, como te quede mejor.

---

## B. Hermosear la página

Archivos: [`templates/page/index.html`](../templates/page/index.html) y [`templates/page/styles.css`](../templates/page/styles.css).

Demo de cómo se ve rellenada (PDF real), **ya online**:

https://ai-whisperers.github.io/paragu-ai-cv/

Misma página en el repo: [`demos/ana-samaniego/`](../demos/ana-samaniego/).

**Tiene que quedar (no sacar):**

- El **PDF del alumno visible** en la página (no solo un link de descarga)
- Botón **WhatsApp** (link `wa.me` del estudiante)
- Botón **Tarjeta** (baja `tarjeta.pdf`, 90×50 mm, QR de esa página)

**Podés cambiar:** barra de arriba, colores, tipo, cómo se ve el botón. El CV en sí no se rediseña en v1: se muestra el PDF que mandaron.

**No hace falta:** transcribir el CV a secciones, menú, login, listado de alumnos.

La tarjeta: [`templates/card/`](../templates/card/) — 90×50 mm, nombre + rol + QR del **link de esa persona**. El QR lo genera el script; vos definís cómo se ve la tarjeta alrededor.

---

Plazo que mencionaste para el flyer: ~2 días una vez cerrado este brief.
