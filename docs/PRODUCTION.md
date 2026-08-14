# Producción — el PDF es la página

El estudiante **ya tiene un CV en PDF**. No lo reescribimos: la página **muestra ese PDF** y un botón de WhatsApp.

```
PDF del alumno  +  su WhatsApp
        →  HTML estático (barra con nombre + WhatsApp, PDF a pantalla)
        →  QR / tarjeta apuntan a ese link
```

No hay formulario. No hay cuenta. No se transcribe el CV a secciones HTML.

## Qué pedimos

| Pedir | ¿Por qué | Obligatorio |
|---|---|---|
| **CV en PDF** | Es lo que se ve en la página | Sí |
| **WhatsApp** | El botón de contacto | Sí |

## Pasos

1. Guardar `people/<slug>/cv.pdf`.
2. Copiar `templates/page/` a esa carpeta. Poner nombre y `wa.me` del estudiante.
3. Publicar la carpeta. URL = su link público.
4. `python scripts/make_qr.py "URL" -o people/<slug>/qr.png` → tarjeta.

QA: el PDF se ve en el link; el botón abre el WhatsApp **de ellos**.

## Qué no hacer

- Pedirles que reescriban el CV en un form.
- Un listado / CMS de todos los alumnos.
- Login. Si hay que cambiar el PDF, lo mandan por WhatsApp y se reemplaza el archivo.
