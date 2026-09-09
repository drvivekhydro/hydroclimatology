# Lecture 1, Course introduction

**CE524 — Applied Hydroclimatology** &nbsp;·&nbsp; **CE524P — Computational Hydroclimatology Lab**
Vivek Gupta, School of Civil and Environmental Engineering, IIT Mandi

This first lecture sets out what the course is about, how it is organised, and what
you are expected to do in it. The conceptual lecture that follows (Lecture 2) then
introduces the climate system itself, and from Lecture 3 onward the course becomes
hands-on, building small climate and hydrological models in Python.

## What is hydroclimatology?

Hydroclimatology is the study of how the climate system and the hydrological cycle
interact and influence one another over time. It sits between two established fields:
climatology, which describes the long-term statistics of the atmosphere, and
hydrology, which describes the movement and storage of water at and below the land
surface. Hydroclimatology asks how climatic drivers — incoming solar radiation, air
temperature, atmospheric circulation, and their variability — shape precipitation,
evapotranspiration, snow accumulation and melt, soil moisture, streamflow, and
groundwater recharge, and how changes in those hydrological quantities feed back on
the climate.

## What does "applied" add?

*Applied* hydroclimatology takes that understanding and uses it to answer practical
questions about water and climate. Typical areas of application include:

- **Water-resources management** — planning sustainable water use from climate
  patterns and projections.
- **Flood and drought forecasting** — using hydroclimatic data and models to
  anticipate and mitigate extreme events.
- **Agriculture** — matching crop choice, sowing dates, and irrigation scheduling to
  local and regional hydroclimatic conditions.
- **Urban water systems** — designing water supply, stormwater, and wastewater
  infrastructure that can cope with a changing climate.
- **Ecosystems** — assessing environmental flows for rivers and wetlands under
  different climate scenarios.
- **Hydropower** — scheduling generation against seasonal and interannual
  hydroclimatic forecasts.
- **Water quality** — anticipating changes in water temperature, flow, and pollutant
  transport driven by climate.
- **Groundwater** — estimating recharge and sustainable extraction under future
  climate.
- **Adaptation and policy** — giving communities, industry, and government the
  quantitative basis for water and climate decisions.

A recurring theme is the **Himalayan and Indian context**: snow- and glacier-fed
rivers, the monsoon, data scarcity in mountain catchments, and the exposure of Indian
agriculture and infrastructure to hydroclimatic extremes.

## Course structure

The syllabus is organised into eight modules; the full module list with lecture hours
is on the [course home page](intro.md). In brief:

| Module | Theme |
|---|---|
| I | Introduction to hydroclimatology |
| II | Observation |
| III | Modeling |
| IV | Hydroclimatic data processing and analysis |
| V | Impact on hydrology, agriculture, and ecosystems |
| VII | Hydroclimatic extremes: droughts |
| VIII | Hydroclimatic extremes: floods |

```{note}
The interactive notebooks on this site currently cover **Module III (Modeling)**.
They are introduced by two conceptual lectures — this one and *Components of the
climate system* — and are then built up in Python from a zero-dimensional energy
balance model to advection–diffusion in space. Material for the other modules will be
added through the semester.
```

## Assessment

Your grade combines several components:

- Mid-term examination
- End-term examination
- Class discussion / debate
- Group project
- Quizzes
- Tutorials and assignments
- Attendance

The weighting of each component is given in the course handout distributed in class.
The companion lab course, **CE524P — Computational Hydroclimatology Lab**, is assessed
separately and is built around the same Python toolchain used here.

## Prerequisites and tools

There is no formal prerequisite. Familiarity with any programming language (Python, R,
MATLAB, …) will help, and Lecture 3 gives a short, self-contained introduction to
Python for those who need it. Every notebook can be run in the browser through the
🚀 launch button (Google Colab or Binder), so no local installation is required,
though instructions for a local setup are in the project
[README](https://github.com/drvivekhydro/hydroclimatology).

## Resources

- **Brian E. J. Rose — *The Climate Laboratory***, an open, interactive textbook on
  climate modelling in Python:
  <https://brian-rose.github.io/ClimateLaboratoryBook/>
- **MIT *Introduction to Computational Thinking*** (Henri Drake's climate lectures),
  the origin of several notebooks here:
  <https://computationalthinking.mit.edu>
- ***Climate of the Ocean*** (Meier, Börgel & Karsten, IOW), the course this notebook
  collection is adapted from:
  <https://github.com/florianboergel/climateoftheocean>
- **IPCC Assessment Reports** for the current scientific consensus:
  <https://www.ipcc.ch>

Full acknowledgements are on the [course home page](intro.md).
