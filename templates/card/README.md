# Tarjeta de presentación

Medida: **90 × 50 mm**. El QR es siempre el **link público de esa persona** (el mismo que comparte en Instagram).

1. Publicar la página → anotar `PAGE_URL`.
2. Generar el PDF que se descarga en la página:

```text
python scripts/make_card.py --name "Nombre" --role "Rol" --url "PAGE_URL" -o tarjeta.pdf --qr qr.png
```

3. Dejar `tarjeta.pdf` junto al `index.html`. El botón **Tarjeta** de la barra lo baja.

HTML de referencia (Luana puede rediseñar acá; el PDF de entrega lo arma el script): [`index.html`](index.html).

AIW no imprime el papel. El cliente lo manda a imprimir (Rainbow, Copipunto, etc.).
