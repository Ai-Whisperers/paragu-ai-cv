# Operativa — WhatsApp, cobro, entrega

Uso interno. No va en el flyer.

## Canal

Número que ve el estudiante: **0985 724 135** (Kyrian Weiss) · internacional **+595 985 724135**  
(Erebus puede ruteear atrás; en el papel y en el chat sale un solo número.)

## Flujo

1. Escribe (QR del flyer o número).
2. Reply con precio, qué mandar, alias.
3. Recibe sobre todo el **PDF del CV** + WhatsApp. Foto solo si la del PDF no sirve. Nombre y carrera salen del PDF.
4. Transfiere y manda comprobante (`CV web — [apellido]`).
5. Se arma una **página estática** en `people/<slug>/` a partir del PDF (ver [`PRODUCTION.md`](PRODUCTION.md)). Se publica esa carpeta. No se agrega a ningún index.
6. Se manda por WhatsApp: link + PDF CV + PDF tarjeta + PNG del QR.

Pago: **100% antes de producir**. Entrega propuesta: 2–4 días hábiles con materiales completos.

## Alias (provisorio)

| Dato | Valor |
|---|---|
| Titular | Kyrian Weiss van der Pol |
| Alias | CI 5991039 |

## Reply modelo

```
Hola — es el CV web de AI Whisperers.

Gs. 200.000, un solo pago. Incluye:
• tu página (un link para Instagram, LinkedIn, etc.)
• el mismo CV en PDF
• tarjeta de presentación para descargar, con QR de tu link
• 12 meses de hosting

Para arrancar, mandame:
1. tu CV en PDF (el que ya tenés)
2. tu WhatsApp

Si la foto del PDF no se ve bien, te pido una aparte.

Alias: CI 5991039
Titular: Kyrian Weiss van der Pol
Referencia: CV web — [tu apellido]

Cuando esté el comprobante + el PDF, armamos una página con ese CV y te paso el link, el PDF y la tarjeta.
```

## Cómo armar un cliente

```text
# 1. Guardar people/<slug>/cv.pdf (el archivo del alumno)
# 2. Extraer contenido del PDF → rellenar templates/page/
# 3. Publicar la carpeta (URL final = PAGE_URL)
# 4. QR de esa URL:
python scripts/make_qr.py "PAGE_URL" -o people/<slug>/qr.png
# 5. Meter qr.png en la tarjeta y exportar PDF
```

Detalle: [`PRODUCTION.md`](PRODUCTION.md). Slug: minúsculas, sin tildes. Un CV = una carpeta. No crear usuario.
