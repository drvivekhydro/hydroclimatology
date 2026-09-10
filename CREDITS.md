# Credits and provenance

This book is adapted, with gratitude, from open teaching material. The
CC BY-SA 4.0 licence under which that material is released requires us to name
the sources, link the licence, indicate that changes were made, and release the
adaptation under the same licence. This file does that; see [`LICENSE`](LICENSE)
for the licence terms.

**Blanket statement of changes.** Every notebook marked "adapted" below has been
modified from its source — re-framed for hydroclimatology, re-numbered, given new
or Indian/Himalayan examples, extended with additional theory, data, figures or
exercises, and in places rewritten. Lecture 9 is the one exception: it is used
essentially unchanged.

## Principal sources

### MIT *Introduction to Computational Thinking* (18.S191 / 18.S190)

Alan Edelman, David P. Sanders and Fons van der Plas; the climate lectures are by
**Henri F. Drake**.

- Course site: <https://computationalthinking.mit.edu>
- Repository: <https://github.com/mitmath/18S191>
- Licence: **code MIT, text CC BY-SA 4.0** (© Edelman, Sanders & van der Plas, 2021)
- Julia originals for the climate model: <https://github.com/hdrake/simplEarth>

The energy-balance model, Snowball Earth, 1-D advection–diffusion, and 2-D
heat-transport notebooks (Lectures 4, 5, 9, 11) derive from this course. Because
its text is CC BY-SA 4.0, this whole book is released under CC BY-SA 4.0.

### *Climate of the Ocean*

H. E. Markus Meier, Florian Börgel and Sven Karsten — Leibniz Institute for Baltic
Sea Research Warnemünde (IOW) / University of Rostock.

- Website: <https://florianboergel.github.io/climateoftheocean>
- Repository: <https://github.com/florianboergel/climateoftheocean>

Several notebooks reached this course *by way of* Climate of the Ocean, which is
itself a Python adaptation of the MIT material above. The Climate of the Ocean
repository carries no explicit licence; reuse here rests on the CC BY-SA 4.0
licence of the upstream MIT material, with attribution to all parties. We are
grateful to the authors and will gladly adjust this attribution at their request.

### Brian E. J. Rose — *The Climate Laboratory*

An open, interactive textbook on climate modelling in Python.
<https://brian-rose.github.io/ClimateLaboratoryBook/> — CC BY 4.0.
Consulted for Lecture 4.

## Per-lecture provenance

| Lecture | Origin | Status |
|---|---|---|
| 1 — Course introduction | Vivek Gupta, from the CE524 lecture slides | original |
| 2 — Components of the climate system | Vivek Gupta, from the CE524 lecture slides | original (figures individually credited in the notebook) |
| 3 — Introduction to Python | *Climate of the Ocean* → MIT 18.S191 | adapted |
| 4 — Zero-dimensional energy balance model | Henri Drake, MIT 18.S191, via *Climate of the Ocean*; Brian Rose | adapted |
| 5 — Snowball Earth and the ice–albedo feedback | Henri Drake, MIT 18.S191, via *Climate of the Ocean* | adapted |
| 6 — Vegetation and hydrology in a 0-D climate model | Svirezhev & von Bloh (1998); notebook via *Climate of the Ocean* | adapted |
| 7 — A lumped hydrological model | Vivek Gupta | original |
| 8 — Calibrating a hydrological model | Vivek Gupta | original |
| 9 — Advection and diffusion in 1-D | MIT 18.S191, via *Climate of the Ocean* | used essentially unchanged |
| 10 — Advection and diffusion in a river | Vivek Gupta (reuses the Lecture 9 solver) | original |
| 11 — Heat transports (2-D advection–diffusion) | MIT 18.S191, via *Climate of the Ocean* | adapted (renumbered; equation typography fixed) |
| Exercises 1–3 | *Climate of the Ocean* | adapted |

## Datasets and figures

Individually credited where they appear. The main external datasets:

- **SSP CO₂ concentrations** — RCMIP v5.1.0 (Nicholls et al. 2020; Meinshausen et
  al. 2020), CC BY 4.0.
- **CMIP6 multi-model-mean warming** — [`mathause/cmip_temperatures`](https://github.com/mathause/cmip_temperatures),
  CC BY-SA 4.0.
- **Streamflow** — U.S. Geological Survey, National Water Information System
  (public domain).
- **Meteorological forcing** — Daymet v4, ORNL DAAC (public domain; Thornton et
  al. 2022). PET after Oudin et al. (2005).
- **CO₂ and temperature records** — NOAA GML Mauna Loa; NASA GISTEMP (public
  domain).
- **Reference catchments** — CAMELS (Newman et al. 2015; Addor et al. 2017).

Embedded figures in Lectures 1–2 are from Wikimedia Commons, the USGS, NASA, NOAA
and the US EPA, under Creative Commons licences or as US-government public-domain
works; each is captioned with its author and licence in the notebook.

## Adaptation

Adaptation for **CE524 Applied Hydroclimatology at IIT Mandi** by Vivek Gupta,
School of Civil and Environmental Engineering. Corrections and licensing questions:
open an issue at <https://github.com/drvivekhydro/hydroclimatology>.
