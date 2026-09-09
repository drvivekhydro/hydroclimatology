# Applied Hydroclimatology (CE524)

**Indian Institute of Technology Mandi**

Water is an essential resource for human society and natural ecosystems, and its
availability is set by the climate system. Under the uncertainty posed by climate
change, understanding how the different components of the hydrological cycle are
changing has become critically important. *Hydroclimatology* provides a systematic
framework for studying how the climate system controls the spatial and temporal
variability of precipitation, temperature, evapotranspiration, streamflow, and
snowpack.

This site collects the **interactive computational notebooks** for the course. Rather
than only describing models, we build them step by step in Python: starting from a
zero-dimensional energy balance model of the Earth, adding feedbacks, a biosphere and
a hydrological cycle, and then moving to advection and diffusion in space. Each
notebook can be run in the browser through the 🚀 launch button (Google Colab or
Binder) — no local installation required.

```{note}
The notebook collection is under active development and currently focuses on
**Module III (Modeling)**. Material for the observation, data-processing, impacts, and
hydroclimatic-extremes modules will be added over the course of the semester.
```

## Course information

| | |
|---|---|
| Course number | CE524 |
| Credit distribution | 3–0–0–3 |
| Intended for | PG and Ph.D. students |
| Prerequisite | None. Familiarity with any programming language (Python, R, MATLAB, …) is helpful. |

## Preamble

Under the uncertainty posed by climate change, understanding the changing nature of
the different components of the hydrological cycle becomes critically important, as
water is an essential resource for human society and natural ecosystems.
Hydroclimatology provides a systematic structure for studying how the climate system
influences the spatial and temporal variations in the hydrological cycle. In this
course, students explore the climatic drivers of hydrology — precipitation,
temperature, evapotranspiration, streamflow, and snowpack — and are trained to
acquire, process, and analyse large climate datasets to generate useful information
for water-resources management and planning. Students also gain exposure to current
research trends, gaps, and future directions in hydroclimatology, and to research
report writing.

## Course modules

| Module | Topics | Hours |
|---|---|---|
| **I — Introduction to hydroclimatology** | Climate change: causes and impacts; impact on the global hydrologic cycle; water management in a changing climate; concept and scope of hydroclimatology. | 4 |
| **II — Observation** | Types of research data; qualitative and quantitative data; measurement of precipitation, temperature, humidity, wind speed, radiation, evapotranspiration, snow, streamflow, sediment, snow water equivalent; missing-data handling; hydroclimatic measurements in the Himalayan regions. | 4 |
| **III — Modeling** | Fundamental principles in hydroclimatic modeling; types of climate models; simple climate models; simple energy balance climate models (zero-dimensional, single-layer, one-dimensional); general circulation models (GCM); hydrologic modeling; types and components of hydrological models; SWAT, VIC, HEC-HMS. | 8 |
| **IV — Hydroclimatic data processing and analysis** | Gridding observed data; reanalysis data; satellite-derived data; radar data; climate data; paleoclimatology data; climate indices; overview of CMIP6; downscaling and bias correction of climate data; impact-assessment studies. | 8 |
| **V — Impact on hydrology, agriculture, and ecosystem** | Climate-change impact on dams; weather and climate metrics for agriculture; heat-stress indices; impact on food security in India; energy limitation versus moisture limitation; ecosystem services; Himalayan ecosystem and climate-change impact. | 6 |
| **VII — Hydroclimatic extremes: droughts** | Drought definitions (meteorological, hydrological, agricultural, socioeconomic); drought indicators; theory of runs; severity, duration, intensity; frequency analysis; impact of climate change on droughts; drought declaration and management in India. | 6 |
| **VIII — Hydroclimatic extremes: floods** | Definitions; flood types; extreme-precipitation indices; flood analysis; flood frequency analysis; design flood; flood hazard and damage; glacial lake outburst floods (GLOF); impact of climate change on floods; flood-risk and floodplain management. | 6 |

## How the notebooks map to the syllabus

Lectures 1–2 are conceptual; Lectures 3–8 support **Module III** and are hands-on
Python notebooks.

- **Lecture 1** — Course introduction: what applied hydroclimatology is, how the
  course is organised, and how it is assessed.
- **Lecture 2** — Components of the climate system: weather vs climate, climate
  classification, the five components and their couplings, energy balance, the
  greenhouse effect, and characteristic timescales.
- **Lecture 3** — Introduction to Python for data analysis.
- **Lecture 4** — A zero-dimensional energy balance model of Earth's climate.
- **Lecture 5** — Snowball Earth, the ice–albedo feedback, and multiple equilibria.
- **Lecture 6** — Coupling vegetation and a hydrological cycle to a zero-dimensional
  climate model (after Svirezhev & von Bloh, 1998).
- **Lecture 7** — Evolution in time and space: advection and diffusion in 1-D.
- **Lecture 8** — Heat transports: two-dimensional advection–diffusion.

The accompanying exercises build a simple energy balance model, melt the Snowball
Earth, and analyse observations from the Baltic Sea.

## Acknowledgements and credits

This notebook collection is **adapted from open teaching material** and would not exist
without the work of the original authors. Please cite them when reusing this content.

- ***Climate of the Ocean*** — H. E. Markus Meier, Florian Börgel, and Sven Karsten,
  Leibniz Institute for Baltic Sea Research Warnemünde (IOW) / University of Rostock.
  Lectures 3–5 and 7–8 and the exercises are adapted from this course.
  Source: <https://github.com/florianboergel/climateoftheocean>
- ***Introduction to Computational Thinking*** (MIT 18.S191 / 18.S190) — the energy
  balance model, Snowball Earth, and the advection–diffusion notebooks derive from
  Henri Drake's lectures and the [`simplEarth`](https://github.com/hdrake/simplEarth)
  code, translated from Julia to Python. Course: <https://computationalthinking.mit.edu>
- **Brian E. J. Rose** — *The Climate Laboratory*, an open textbook.
  <https://brian-rose.github.io/ClimateLaboratoryBook/>
- **Svirezhev, Y. M., & von Bloh, W. (1998).** A zero-dimensional climate–vegetation
  model containing global carbon and hydrological cycle. *Ecological Modelling, 106*,
  119–127. (Basis for Lecture 6; further references are listed within that notebook.)

Adaptation for **CE524 Applied Hydroclimatology at IIT Mandi** by Vivek Gupta, School
of Civil and Environmental Engineering. New material developed for this course is
© its authors and shared for educational use; the adapted material retains the licence
of its original source.

## Literature

### Climate assessment
- IPCC Assessment Reports — <https://www.ipcc.ch> (open access)
- CMIP6 model output — <https://esgf-node.llnl.gov/projects/cmip6/>

### Hydroclimatology and climate dynamics
- L. J. Gordon, K. Vörösmarty et al. — hydrological-cycle and water-resources literature
- Dennis L. Hartmann — *Global Physical Climatology*, 2nd ed. (2016)
- Geoffrey K. Vallis — *Climate and the Oceans* (2011)
- Dietmar Dommenget — *Climate Dynamics* lecture notes,
  <http://users.monash.edu.au/~dietmard/teaching/dommenget.climate.dynamics.notes.pdf>

### Hydrological modeling
- SWAT — <https://swat.tamu.edu/>
- VIC — <https://vic.readthedocs.io/>
- HEC-HMS — <https://www.hec.usace.army.mil/software/hec-hms/>
