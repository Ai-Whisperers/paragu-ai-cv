# Tarjeta de presentación

Medida: **90 × 50 mm**. El QR es siempre el **link público de esa persona** (el mismo que comparte en Instagram).

1. Publicar la página → anotar `PAGE_URL`.
2. `python scripts/make_qr.py "PAGE_URL" -o people/<slug>/qr.png`
3. Copiar `templates/card/index.html` a esa carpeta, reemplazar nombre/rol/URL, apuntar la imagen a `qr.png`.
4. Imprimir / exportar PDF (print to PDF, 90×50 mm). Entregar el PDF por WhatsApp.

AIW no imprime el papel. El cliente lo manda a imprimir (Rainbow, Copipunto, etc.).
