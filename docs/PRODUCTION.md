# Producción — del PDF a la página estática

El estudiante **ya tiene un CV en PDF**. No le armamos el currículum: lo pasamos a una página estática.

```
PDF del alumno  →  extraer contenido  →  templates/page/  →  HTML estático
                →  el mismo PDF se ofrece para descargar
                →  QR + tarjeta apuntan al link de esa página
```

No hay formulario largo. No hay cuenta. No se inventa experiencia que no esté en el PDF.

## Qué pedimos

| Pedir | ¿Por qué | Obligatorio |
|---|---|---|
| **CV en PDF** | Fuente de toda la página | Sí |
| **WhatsApp** | El botón de la página; casi nunca viene en el PDF | Sí |
| Foto de perfil | Si la del PDF se ve mal o no hay | Si hace falta |

Nombre, carrera, educación, experiencia, skills: salen del PDF.

## Pasos

1. Guardar el PDF en `people/<slug>/cv.pdf`.
2. Extraer bloques (objetivo, educación, experiencia, skills, links) — agente + QA humano. No agregar cosas que no estén.
3. Rellenar `templates/page/` (diseño de Luana). Foto: la del PDF o la que mandó aparte.
4. Botón WhatsApp = `wa.me` **del estudiante**, no el de ventas.
5. Publicar esa carpeta (un HTML, CSS, foto, `cv.pdf`). URL = su link público.
6. `python scripts/make_qr.py "URL" -o people/<slug>/qr.png` → tarjeta.

QA: el texto de la página coincide con el PDF; el QR abre esa URL; el WhatsApp es el de ellos.

## Qué no hacer

- Pedirles que reescriban el CV en un form si ya mandaron el PDF.
- Un listado / CMS de todos los alumnos.
- Login para “editar mi página” en el v1. Si hay un error, lo corrigen por WhatsApp y se regenera el HTML.
