# Operativa — WhatsApp, cobro, entrega

Uso interno. No va en el flyer.

## Canal

Número que ve el estudiante: **+595 991 501444**  
(Erebus puede ruteear atrás; en el papel y en el chat sale un solo número.)

## Flujo

1. Escribe (QR del flyer o número).
2. Reply con precio, qué mandar, alias.
3. Recibe: PDF del CV, foto, nombre, carrera, WhatsApp.
4. Transfiere y manda comprobante (`CV web — [apellido]`).
5. Se arma **una carpeta** en `people/<slug>/` (página + QR + tarjeta). Se publica esa carpeta. No se agrega a ningún index.
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
1. tu CV en PDF
2. una foto de perfil
3. cómo querés que figure tu nombre
4. carrera / a qué te postulás
5. tu WhatsApp

Alias: CI 5991039
Titular: Kyrian Weiss van der Pol
Referencia: CV web — [tu apellido]

Cuando esté el comprobante + esos archivos, te paso el link, el PDF y la tarjeta.
```

## Cómo armar un cliente

```text
# 1. Copiar plantilla
# 2. Rellenar nombre, textos, foto, wa.me del estudiante
# 3. Publicar la carpeta (URL final = PAGE_URL)
# 4. QR de esa URL:
python scripts/make_qr.py "PAGE_URL" -o people/<slug>/qr.png
# 5. Meter qr.png en la tarjeta y exportar PDF
```

Slug: minúsculas, sin tildes, un CV = una carpeta. No crear usuario.
