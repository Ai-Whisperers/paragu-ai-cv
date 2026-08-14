# paragu-ai CV

CV web para estudiantes: **una persona, un link, una tarjeta**. Sin cuentas, sin panel, sin lista pública de CVs.

El estudiante recibe su URL por WhatsApp. La pega en Instagram, LinkedIn o mail, o genera más QRs. Un reclutador abre el link y le escribe por WhatsApp.

**Precio de lanzamiento:** Gs. 200.000 pago único (12 meses de hosting). Sin cuota mensual.

## Quién hace qué

| Quién | Qué |
|---|---|
| **Luana** | Flyer promocional + hermosear la plantilla de la página (y la tarjeta) |
| **Kyrian / Iván** | WhatsApp, cobro, generar QR, publicar cada página, entregar al cliente |

Docs para Luana: [`docs/LUANA.md`](docs/LUANA.md)  
Producto: [`docs/PRODUCT.md`](docs/PRODUCT.md)  
Operativa WhatsApp: [`docs/OPS.md`](docs/OPS.md)

## Cómo está armado

```
templates/page/     ← plantilla de la página (Luana diseña acá)
templates/card/     ← plantilla de tarjeta 90×50 mm (QR del link)
demos/ana-duarte/   ← un CV demo (página suelta, no un directorio)
people/             ← un folder por cliente real (no se listan en un index)
scripts/make_qr.py  ← QR PNG a partir de una URL
docs/flyer/         ← copy + QR de WhatsApp para el flyer
```

No hay `index.html` de “todos los CVs”. Cada cliente es una carpeta con su `index.html`.

## Vista local de un CV

```text
cd demos/ana-duarte
python -m http.server 8765
```

Abrir http://127.0.0.1:8765/

## Generar el QR de un link

```text
pip install -r requirements.txt
python scripts/make_qr.py "https://ejemplo.com/cv/ana" -o people/ana-duarte/qr.png
```

Ese PNG es el que va en la tarjeta. El mismo link es el que el cliente comparte.

## Entrega al cliente (WhatsApp)

1. Link de su página  
2. PDF del CV  
3. PDF de la tarjeta (QR = ese link)  
4. PNG del QR  

AI Whisperers no imprime el papel.

---

AI Whisperers · paragu-ai · 2026
