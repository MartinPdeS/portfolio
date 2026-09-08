# Martin Poinsinet de Sivry-Houle

**Computational physicist · Scientific software developer · Python & C++**

I build open-source tools for computational optics, scientific measurement, and signal analysis. My work connects physical models to practical software: light scattering, wave propagation, flow cytometry simulation, and calibration.

PhD in Engineering Physics, Polytechnique Montréal (2018–2024). Biomedical optics research at Amsterdam UMC.

## Selected work

| Project | What it does |
| --- | --- |
| [PyMieSim](https://github.com/MartinPdeS/PyMieSim) | Lorenz–Mie scattering with configurable particles, sources, and detectors |
| [FlowCyPy](https://github.com/MartinPdeS/FlowCyPy) | Flow cytometry simulation, including particle events, noise, and detector response |
| [LightWave2D](https://github.com/MartinPdeS/LightWave2D) | Two-dimensional FDTD wave propagation and field visualization |
| [PackLab](https://github.com/MartinPdeS/PackLab) | Hard-sphere structure, analytical correlations, and particle sampling |
| [RosettaX](https://github.com/MartinPdeS/RosettaX) | Inspectable fluorescence and scattering calibration workflows |
| [DeepPeak](https://github.com/MartinPdeS/DeepPeak) | Peak detection, neural deconvolution, and time-series evaluation |

Explore the [project directory](projects/README.md) or the portfolio website in [index.html](index.html).

## Contact

[Email](mailto:martin.poinsinet.de.sivry@gmail.com) · [GitHub](https://github.com/MartinPdeS)

## Run the website locally

No installation or build step is needed. Open `index.html` directly, or serve the repository:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. The website uses local assets and system fonts, with no analytics or external runtime dependencies. All content and native project disclosures work without JavaScript; JavaScript adds filtering and an illustrative wavelength control.

## Publish on GitHub Pages

1. In the repository’s **Settings → Pages**, select **GitHub Actions** as the source.
2. Push the changes to `main` or `master`, or run the **Deploy portfolio** workflow manually from the default branch.
3. GitHub reports the published URL in the workflow’s deployment output (normally `https://martinpdes.github.io/portfolio/`).

The workflow stages only `index.html` and `assets/`, then deploys that directory. The site uses relative asset paths, so it also works under a repository subpath or a custom domain. This setup does not itself enable Pages or publish local changes.

## Maintain the portfolio

- **Content and case studies:** `index.html`.
- **Design and responsive layouts:** `assets/style.css`.
- **Filtering and wave illustration:** `assets/main.js`.
- **Content evidence and editorial conventions:** [CONTENT.md](CONTENT.md).
- **Local validation:** `python3 scripts/check_site.py` and `node --check assets/main.js`.

The wave field and project artwork are schematic illustrations, not numerical results or benchmarks. Add measured results only with a reproducible source. No private CV documents are included in this website.
