# Lecture 2, Components of the climate system

Before building any model, it helps to have a shared picture of what the climate
system is made of, how its parts exchange energy and water, and why processes that
span timescales from hours to millennia can nonetheless be studied with simple models.
This lecture is descriptive; the quantitative treatment begins in Lecture 4 with a
zero-dimensional energy balance model.

## Weather and climate

**Weather** is the state of the atmosphere at a particular place and time —
temperature, humidity, precipitation, wind, cloud, and pressure — and it changes from
hour to hour and day to day. **Climate** is the statistical description of weather
over a long period, conventionally taken as 30 years: not just the average, but also
the variability and the frequency of extremes. A useful shorthand is that *climate is
what you expect and weather is what you get*.

The distinction matters for this course. Hydrological design — a spillway, a drought
plan, an irrigation schedule — depends on climate statistics, while operations depend
on weather. Climate change shifts the statistics, so design assumptions that were
based on a stationary past have to be revisited.

## Classifying climates

Because climate varies systematically with latitude, altitude, distance from the
ocean, and circulation, it can be classified into a manageable number of types. The
**Köppen–Geiger** scheme groups climates into five broad classes — **A** tropical,
**B** dry, **C** temperate, **D** continental, and **E** polar — each subdivided by
seasonal temperature and precipitation into types such as monsoon, humid subtropical,
semi-arid (steppe), subarctic, and tundra. India spans several of these, from arid
western Rajasthan to the humid subtropical Indo-Gangetic plain to the alpine and polar
climates of the high Himalaya.

```{seealso}
High-resolution present and future Köppen–Geiger maps:
Beck, H. E. et al. (2018), *Present and future Köppen-Geiger climate classification
maps at 1-km resolution*, **Scientific Data** 5, 180214.
<https://www.nature.com/articles/sdata2018214>
```

## The five components

The climate system is usually described as five interacting components:

1. **Atmosphere** — the fastest-responding component; carries heat and moisture,
   sets the radiative balance through greenhouse gases, clouds, and aerosols.
2. **Hydrosphere** — the oceans, lakes, and rivers; the ocean stores and transports
   enormous amounts of heat and carbon and has a long memory.
3. **Cryosphere** — snow, sea ice, glaciers, ice sheets, and permafrost; highly
   reflective, and a strong amplifier of change through the ice–albedo feedback.
4. **Land surface (lithosphere)** — topography, soils, and their moisture; controls
   the partitioning of rainfall into evaporation, runoff, and infiltration.
5. **Biosphere** — vegetation and soils on land, plankton in the ocean; modifies
   albedo, roughness, evapotranspiration, and the carbon cycle.

No component acts alone. Snow cover changes surface albedo and therefore air
temperature; a warmer atmosphere holds more water vapour, which is itself a greenhouse
gas; vegetation growth depends on temperature and soil moisture and in turn changes
albedo and evapotranspiration. Lectures 5 and 6 make two of these couplings —
temperature–ice and temperature–vegetation–water — quantitative.

### Earth as a system of systems

Treating the climate as a set of coupled subsystems, each with its own governing
equations and exchanging fluxes of energy, water, and carbon with the others, is the
conceptual basis of every climate model, from the zero-dimensional model of Lecture 4
to full Earth system models.

## Energy balance in one paragraph

Averaged over the globe and over a year, about **340 W m⁻²** of solar radiation
arrives at the top of the atmosphere. A fraction is reflected straight back to space;
that fraction is the **albedo**. Bright surfaces — fresh snow, thick cloud — have a
high albedo (0.5–0.9); the open ocean has a low albedo (about 0.06). Earth's overall
albedo is roughly 0.3. The remaining absorbed sunlight warms the surface and
atmosphere, which radiate in the infrared; in the long-term mean, outgoing infrared
radiation balances absorbed sunlight. Lecture 4 turns exactly this sentence into an
equation.

### The greenhouse effect

Greenhouse gases — water vapour, carbon dioxide, methane, nitrous oxide — are largely
transparent to sunlight but absorb and re-emit infrared radiation. This keeps the
lower atmosphere and surface roughly 33 K warmer than they would be otherwise, which
is what makes the planet habitable. The effect is natural; what is new is the
**enhanced** greenhouse effect from human emissions.

## What is climate change?

The IPCC defines climate change as *a change in the state of the climate that can be
identified by changes in the mean and/or the variability of its properties, and that
persists for an extended period, typically decades or longer*. The change can arise
from **natural** causes — variations in solar output, volcanic eruptions, internal
modes such as El Niño–Southern Oscillation — or from **anthropogenic** causes, chiefly
greenhouse-gas emissions and land-use change. Attribution studies separate these
contributions; at the global scale the observed warming since the mid-20th century is
overwhelmingly anthropogenic, while at regional scales natural variability can be
comparable to or larger than the forced signal.

## Timescales, scale separation, and averaging

Climate processes act on enormously different timescales:

| Process | Characteristic time |
|---|---|
| Convective cloud | hours |
| Weather systems | days |
| Seasonal cycle, El Niño | months to a few years |
| Upper-ocean adjustment | years to decades |
| Deep-ocean circulation, ice sheets | centuries to millennia |
| Tectonics, orbital variations | 10⁴–10⁸ years |

It is worth naming three different "times" that often get conflated: a **period** is
the interval between regularly recurring events (the seasons); a **response time** is
how long a system takes to adjust to a new forcing (decades for the upper ocean to
reach a new temperature); a **lifetime** is how long an individual phenomenon lasts (a
convective cloud).

This spread of timescales is what makes simple models useful. Because fast and slow
processes are **well separated**, a model aimed at one timescale can treat much faster
processes as instantaneous noise and much slower ones as fixed boundary conditions.
**Averaging** in time or space then removes the fast fluctuations and exposes the
slower behaviour of interest — the same reasoning that lets a zero-dimensional model
say something meaningful about global temperature without resolving a single weather
system. The models in the following lectures are built on exactly this idea.

## Figures and sources

The lecture slides use figures from the following open resources; they are linked here
rather than reproduced.

- **UCAR Center for Science Education** — climate system, energy budget, and albedo
  explainers: <https://scied.ucar.edu/learning-zone/how-climate-works>
- **NASA — My NASA Data** — Earth as a system, climate-system components:
  <https://mynasadata.larc.nasa.gov/>
- **IPCC AR6 Working Group I** — figures and the technical basis for climate change:
  <https://www.ipcc.ch/report/ar6/wg1/>
- **Köppen–Geiger maps** — Beck et al. (2018), *Scientific Data*:
  <https://www.nature.com/articles/sdata2018214>
- **Brian Rose — *The Climate Laboratory***, "Models, budgets, and fun" and the
  energy-balance chapters:
  <https://brian-rose.github.io/ClimateLaboratoryBook/courseware/models-budgets-fun.html>
