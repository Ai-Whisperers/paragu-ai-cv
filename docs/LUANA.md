# Luana — flyer + página

Dos trabajos, en este repo:

1. **Flyer** (carteleras FASEN/FADA + Instagram) — copy cerrado abajo; vos diseñás.
2. **Hermosear** `templates/page/` (y si da, `templates/card/`) — una plantilla que se rellena por cada estudiante.

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
| CTA | Escaneá y escribí. Mandá tu CV y en pocos días tenés la página. |
| Contacto | +595 991 501444 |
| Marca | AI Whisperers / paragu-ai CV (no “Erebus”) |

**Viñetas (máx. 4):**

- Página CV (un link para tu Instagram / LinkedIn)
- Mismo CV en PDF para postular
- Tarjeta descargable con QR de **tu** link (vos la imprimís)
- 12 meses de hosting incluidos

**Qué tienen que mandar (tiene que estar en el flyer):**

1. CV actual en PDF  
2. Foto de perfil (se tiene que ver la cara)  
3. Cómo quiere que figure el nombre  
4. Carrera / a qué se postula  
5. WhatsApp  

**QRs en el flyer**

| QR | Destino | Etiqueta |
|---|---|---|
| 1 | WhatsApp — PNG en [`flyer/qr-whatsapp.png`](flyer/qr-whatsapp.png) | Escribime |
| 2 | **Un** CV demo (una página, no un listado). Hoy: `demos/ana-duarte/` cuando esté online | Mirá un ejemplo |

URL del QR 1 (ya está en el PNG):

`https://wa.me/595991501444?text=Hola%2C%20quiero%20un%20CV%20web`

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

Demo de cómo se ve rellenada: [`demos/ana-duarte/`](../demos/ana-duarte/).

**Tiene que quedar (no sacar):**

- Nombre, título/objetivo, foto (o iniciales si no hay foto)
- Botón **Escribime por WhatsApp** (link `wa.me` del estudiante)
- Secciones: objetivo, educación, experiencia/proyectos, habilidades
- Enlace o botón para **descargar el CV en PDF**
- Enlace o botón para **descargar la tarjeta** (PDF)

**Podés cambiar:** color, tipo, layout, foto, detalles. Una plantilla para todos; no un diseño distinto por alumno en el v1 (si un caso lo pide, se habla).

**No hace falta:** menú, login, “volver al listado”, blog, SEO pesado.

La tarjeta: [`templates/card/`](../templates/card/) — 90×50 mm, nombre + rol + QR del **link de esa persona**. El QR lo genera el script; vos definís cómo se ve la tarjeta alrededor.

---

Plazo que mencionaste para el flyer: ~2 días una vez cerrado este brief.
