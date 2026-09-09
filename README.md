# Applied Hydroclimatology (CE524) — IIT Mandi

Interactive course notebooks, built as a [Jupyter Book](https://jupyterbook.org).

**Live site:** https://drvivekhydro.github.io/hydroclimatology/

## Contents

- `lecture-0*.ipynb` — lecture notebooks (Module III: climate & hydrologic modeling)
- `exercise-0*.ipynb` — exercises
- `intro.md`, `_toc.yml`, `_config.yml` — book landing page, table of contents, settings

## Building locally

```bash
python -m venv .venv && . .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install "jupyter-book<2" sphinx-proof
pip install -r requirements.txt
jupyter-book build .
```

The rendered book appears in `_build/html/index.html`.

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the book and
publishes it to the `gh-pages` branch. GitHub Pages serves that branch.

## Credits

Adapted from the open course **"Climate of the Ocean"** by H. E. Markus Meier,
Florian Börgel, and Sven Karsten (Leibniz Institute for Baltic Sea Research
Warnemünde / University of Rostock) —
<https://github.com/florianboergel/climateoftheocean> — which in turn builds on
Henri Drake's MIT *Introduction to Computational Thinking* material and Brian Rose's
*The Climate Laboratory*. See `intro.md` for the full acknowledgements.
