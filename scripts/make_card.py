"""Render a 90 × 50 mm business-card PDF. The QR is the public CV URL."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_qr import make_qr_image, write_qr

DPI = 300
MM = DPI / 25.4
CARD_W_MM = 90
CARD_H_MM = 50
NAVY = (31, 78, 121)
INK = (26, 26, 26)
MUTED = (92, 101, 112)
WHITE = (255, 255, 255)


def _mm(value: float) -> int:
    return round(value * MM)


def _font(size_pt: float, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    size_px = max(1, round(size_pt * DPI / 72))
    names = (
        ("segoeuib.ttf", "calibrib.ttf", "arialbd.ttf")
        if bold
        else ("segoeui.ttf", "calibri.ttf", "arial.ttf")
    )
    fonts_dir = Path("C:/Windows/Fonts")
    for name in names:
        path = fonts_dir / name
        if path.exists():
            return ImageFont.truetype(str(path), size_px)
    return ImageFont.load_default()


def _wrap(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        trial = f"{current} {word}"
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def render_card(name: str, role: str, page_url: str) -> Image.Image:
    width, height = _mm(CARD_W_MM), _mm(CARD_H_MM)
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)

    pad = _mm(6)
    qr_size = _mm(28)
    border = max(1, _mm(0.35))
    draw.rectangle(
        (border, border, width - 1 - border, height - 1 - border),
        outline=NAVY,
        width=border,
    )

    qr = make_qr_image(page_url).convert("RGB")
    qr = qr.resize((qr_size, qr_size), Image.Resampling.NEAREST)
    qr_x = width - pad - qr_size
    qr_y = (height - qr_size) // 2
    img.paste(qr, (qr_x, qr_y))

    text_right = qr_x - _mm(4)
    text_width = text_right - pad
    name_font = _font(14, bold=True)
    role_font = _font(9, bold=True)
    url_font = _font(7)

    y = pad
    for line in _wrap(draw, name, name_font, text_width):
        draw.text((pad, y), line, font=name_font, fill=INK)
        y += _mm(6)
    y += _mm(1)
    for line in _wrap(draw, role, role_font, text_width):
        draw.text((pad, y), line, font=role_font, fill=NAVY)
        y += _mm(4.2)
    y += _mm(2)
    for line in _wrap(draw, page_url, url_font, text_width):
        draw.text((pad, y), line, font=url_font, fill=MUTED)
        y += _mm(3.4)

    return img


def write_card(
    name: str,
    role: str,
    page_url: str,
    dest: Path,
    qr_dest: Path | None = None,
) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    card = render_card(name, role, page_url)
    card.save(dest, "PDF", resolution=float(DPI), title=f"Tarjeta — {name}")
    if qr_dest is not None:
        write_qr(page_url, qr_dest)
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="90×50 mm card PDF. QR encodes the public CV page URL."
    )
    parser.add_argument("--name", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--url", required=True, help="Public page URL (same as Instagram link)")
    parser.add_argument("-o", "--output", default="tarjeta.pdf")
    parser.add_argument("--qr", default="", help="Optional QR PNG path")
    args = parser.parse_args()
    qr_path = Path(args.qr) if args.qr else None
    path = write_card(args.name, args.role, args.url, Path(args.output), qr_path)
    print(f"Wrote {path} ({path.stat().st_size} bytes)")
    if qr_path is not None:
        print(f"Wrote {qr_path}")
    print(f"URL: {args.url}")


if __name__ == "__main__":
    main()
