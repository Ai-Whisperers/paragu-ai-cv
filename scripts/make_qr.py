"""Generate a print-ready QR PNG from a public page URL."""

from __future__ import annotations

import argparse
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_H


def write_qr(url: str, dest: Path) -> Path:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=12,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest)
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="QR PNG for a paragu-ai CV page URL (same URL as the client's public link)."
    )
    parser.add_argument("url", help="Public page URL, e.g. https://host/ana-duarte/")
    parser.add_argument("-o", "--output", default="qr.png", help="Output PNG path")
    args = parser.parse_args()
    path = write_qr(args.url, Path(args.output))
    print(f"Wrote {path} ({path.stat().st_size} bytes)")
    print(f"URL: {args.url}")


if __name__ == "__main__":
    main()
