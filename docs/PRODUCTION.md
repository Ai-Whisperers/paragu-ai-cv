# Producción — el PDF es la página

El estudiante **ya tiene un CV en PDF**. No lo reescribimos: la página **muestra ese PDF**, WhatsApp, y descarga de tarjeta.

```
PDF del alumno  +  su WhatsApp
        →  HTML estático (barra: nombre + Tarjeta + WhatsApp, PDF a pantalla)
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
4. `python scripts/make_card.py --name "..." --role "..." --url "URL" -o people/<slug>/tarjeta.pdf --qr people/<slug>/qr.png`
5. El botón **Tarjeta** de la página apunta a `tarjeta.pdf` (mismo folder).

QA: el PDF se ve en el link; WhatsApp abre el de **ellos**; **Tarjeta** baja un PDF 90×50 mm cuyo QR abre esa misma URL.

## Qué no hacer

- Pedirles que reescriban el CV en un form.
- Un listado / CMS de todos los alumnos.
- Login. Si hay que cambiar el PDF, lo mandan por WhatsApp y se reemplaza el archivo.
