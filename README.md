# A spiky situation — interactive version

Mobile-first scroll experience of Jón Tomas Magnússon Amorós's research poster
*A spiky situation: how warming could speed up urchin grazing on Arctic kelp forests*
(Wernberg & Filbee-Dexter lab, UWA).

Live: https://spiky-situation.vercel.app

## Structure

| Path | What |
| --- | --- |
| `src/index.src.html` | The page source (HTML, CSS, JS). Images and data are placeholders (`/*P1*/`, `/*DATA*/null`…). |
| `data/data.json` | Feeding-rate curve, 95% CI band, tanks and 2090 scenarios, extracted from Jon's chart. |
| `assets/*.webp` | Images embedded into the page at build time (urchin, kelp mask, Jon's portrait, photo plates p1–p3). |
| `public/` | What Vercel serves: the built `index.html`, favicons and share image (`share-3.jpg`). |
| `design/og`, `design/qr` | Sources for the share image, favicon and the poster QR. |

## Edit and publish

1. Edit `src/index.src.html` (or swap an image in `assets/`).
2. Build: `python3 build.py` → writes `public/index.html`.
3. Commit and push to `main`. Vercel publishes automatically.

`python3 build.py --artifact` also writes `dist/artifact.html`, the version used for the claude.ai artifact.

## Photo credits

- Kelp forest — © Alexis Savard Drouin
- Urchin barren — © Thomas Wernberg
- Sugar kelp (*Saccharina latissima*) — illustration from the poster (no credit shown)
