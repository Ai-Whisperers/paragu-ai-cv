# Publicar un CV (GitHub Pages)

El repo **main** es privado (ops, plantillas, PDFs de clientes).
La demo pública vive en la rama `gh-pages`: solo HTML/CSS/PDF/PNG, sin `docs/OPS.md`.

**URL pública (Luana / flyer / celular):**

https://ai-whisperers.github.io/paragu-ai-cv/

GitHub Pages está en **público**. No hace falta cuenta ni invitación al repo.

## Qué hay online hoy

La página de Ana Paula Samaniego (PDF a la vista + WhatsApp + descarga de tarjeta).
No hay listado de alumnos.

## Cómo republicar después de un cambio de diseño

En una máquina con el repo:

```text
git fetch origin
git worktree add .worktrees/gh-pages gh-pages   # solo la primera vez
```

Copiá los archivos de `demos/ana-samaniego/` (o del cliente) a la raíz de `.worktrees/gh-pages/`:
`index.html`, `styles.css`, `cv.pdf`, `cv-page1.png`, `tarjeta.pdf`, más `.nojekyll`.

```text
cd .worktrees/gh-pages
git add -A
git commit -F commitmsg.txt
git push origin gh-pages
```

En 1–2 minutos: https://ai-whisperers.github.io/paragu-ai-cv/

No subas `docs/OPS.md` ni alias de cobro a `gh-pages`.
