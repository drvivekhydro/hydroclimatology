# Applied Hydroclimatology (CE524)

Interactive computational notebooks for **CE524 — Applied Hydroclimatology**, a
graduate elective at the **School of Civil and Environmental Engineering, Indian
Institute of Technology Mandi**, taught by **Vivek Gupta**. A companion lab course,
**CE524P — Computational Hydroclimatology Lab**, is built on the same toolchain.

📖 **Read the book:** <https://drvivekhydro.github.io/hydroclimatology/>

## About the course

Water availability is set by the climate system, and under climate change the
statistics of rainfall, snowmelt, evapotranspiration and streamflow can no longer be
assumed stationary. *Hydroclimatology* is the systematic study of how the climate
system controls the space and time variability of the hydrological cycle. CE524 covers
the climatic drivers of hydrology and trains students to acquire, process and analyse
large climate datasets for water-resources planning, with a recurring focus on the
**Himalayan and Indian context** — snow- and glacier-fed rivers, the monsoon, data
scarcity in mountain catchments, and exposure to hydroclimatic extremes.

| | |
|---|---|
| Course number | CE524 (3–0–0–3) |
| Offered by | School of Civil and Environmental Engineering, IIT Mandi |
| Intended for | Final-year undergraduate, postgraduate, and Ph.D. students |
| Prerequisite | None; familiarity with any programming language helps |

The syllabus has seven modules: **(1)** introduction to hydroclimatology, **(2)**
modeling, **(3)** observation, **(4)** data processing and analysis, **(5)** impacts on
hydrology, agriculture and ecosystems, **(6)** droughts, and **(7)** floods. The full
outline is on the [book's home page](https://drvivekhydro.github.io/hydroclimatology/).

## What's in this repository

This repository holds the **notebook collection** for the course — currently the
conceptual introduction and the modeling module (Module 2). Rather than only describing
models, the notebooks build them in Python, from a zero-dimensional energy balance model
of the Earth up to advection and diffusion in space and a calibrated catchment model.

| | |
|---|---|
| **Lectures 1–2** | What hydroclimatology is; the climate system, energy balance, feedbacks, tipping points |
| **Lecture 3** | A short introduction to Python for data analysis |
| **Lectures 4–6** | Zero-dimensional climate models: energy balance, ice–albedo feedback, a coupled vegetation–hydrology model |
| **Lectures 7–8** | A lumped rainfall–runoff model and how to calibrate it, using real catchment data |
| **Lectures 9–11** | Advection and diffusion: in 1-D, applied to river flood routing and transport, and in 2-D |
| **Exercises** | One scaffolded exercise notebook per hands-on lecture (3–5, 7–10); Exercise 9 analyses real Indian Ocean SST data |

Material for the observation, data-processing, impacts and extremes modules will be
added through the semester.

## Running the notebooks

Every notebook has a 🚀 launch button on the [website](https://drvivekhydro.github.io/hydroclimatology/)
that opens it in **Google Colab** or **Binder** — no installation needed.

To run them locally:

```bash
python -m venv .venv && . .venv/Scripts/activate     # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Building the book

```bash
pip install "jupyter-book<2" sphinx-proof
jupyter-book build .          # output in _build/html/
```

Pushes to `main` trigger [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml),
which builds the book and publishes it to the `gh-pages` branch.

## Credits and licence

Several lectures are adapted from the open course **[*Climate of the Ocean*](https://github.com/florianboergel/climateoftheocean)**
(H. E. Markus Meier, Florian Börgel, Sven Karsten; IOW / University of Rostock), which
is itself a Python adaptation of **Henri Drake's climate lectures in
[MIT *Introduction to Computational Thinking*](https://computationalthinking.mit.edu)**;
Brian Rose's *[The Climate Laboratory](https://brian-rose.github.io/ClimateLaboratoryBook/)*
was also consulted. Lectures 1, 2, 7, 8 and 10 are original to this course.

Teaching content is licensed **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**
and code additionally under the **MIT License**. Full per-lecture provenance is in
[`CREDITS.md`](CREDITS.md); licence terms are in [`LICENSE`](LICENSE).
