![Martin Poinsinet de Sivry-Houle — Computational physicist, scientific software developer](assets/banner.svg)

I build tools that help researchers and engineers understand optical systems—from numerical simulation to signal analysis and instrument calibration.

I’m interested in roles and collaborations that combine numerical modeling, reliable software, and experimental measurement, particularly in photonics, biomedical optics, and optical instrumentation.

[**View my CV (PDF)**](assets/Martin-Poinsinet-de-Sivry-Houle-CV.pdf) · [GitHub](https://github.com/MartinPdeS) · [Contact me](mailto:martin.poinsinet.de.sivry@gmail.com)

## Selected projects

### [PyMieSim](https://github.com/MartinPdeS/PyMieSim) · Light scattering

**The challenge.** A scattering calculation must connect particle properties to what a detector actually collects. Exploring source, particle, and detector parameters together adds a computational challenge: many optical configurations need to be evaluated consistently.

**My contribution.** I developed a Python interface around a compiled scattering backend, bringing particle solvers, illumination, detector coupling, and parameter sweeps into one configurable workflow. This connects Lorenz–Mie calculations to questions about an optical measurement.

**Publication.** [PyMieSim: an open-source library for fast and flexible far-field Mie scattering simulations](https://doi.org/10.1364/OPTCON.473102). Martin Poinsinet de Sivry-Houle, Nicolas Godbout, and Caroline Boudoux. *Optics Continuum* **2**(3), 520–534 (2023).

The paper demonstrates applications to flow cytometry geometry and few-mode optical coherence tomography.

**Python · C++ · pybind11 · Computational optics**

### [SuPyMode](https://github.com/MartinPdeS/SuPyMode) · Fiber component design

**The challenge.** Designing a fiber component requires understanding how its geometry changes the modes it supports and how power transfers between them. A useful design tool must connect these local modal properties to propagation through the component.

**My contribution.** I developed a Python/C++ toolkit combining eigenmode expansion and coupled-mode theory for fiber component analysis. It supports exploration of mode coupling and component geometry, including mode-selective photonic lanterns.

**Publication.** [SuPyMode: an open-source library for design and optimization of fiber optic components](https://doi.org/10.1364/OPTCON.513562). Martin Poinsinet de Sivry-Houle, Rodrigo Itzamna Becerra Deana, Stéphane Virally, Nicolas Godbout, and Caroline Boudoux. *Optics Continuum* **3**(2), 242–255 (2024).

The paper presents the mathematical framework, validation against analytical solutions, and a photonic-lantern design study.

**Python · C++ · Eigenmode expansion · Coupled-mode theory**

### [FlowCyPy](https://github.com/MartinPdeS/FlowCyPy) · Flow cytometry simulation

**The challenge.** A measured cytometry pulse reflects the particle, illumination, fluidics, detector, electronics, and noise together. Studying these stages in isolation makes it difficult to understand which part of the instrument limits detection.

**My contribution.** I developed an end-to-end simulation framework connecting particle events and scattering physics to detector response, electronics, noise, and signal processing. This provides a controlled setting for exploring instrument configurations and testing analysis pipelines with simulated measurements.

**Publication coming soon.**

**Physical modeling · Detector simulation · Signal processing**

### [LightWave2D](https://github.com/MartinPdeS/LightWave2D) · Electromagnetic wave propagation

**The challenge.** Studying propagation and diffraction means translating optical geometries into a numerical field problem, while keeping sources, spatial discretization, and boundary conditions consistent.

**My contribution.** I developed a two-dimensional FDTD simulation tool with configurable sources and optical components, backed by compiled computation. Field visualizations let users inspect how waves interact with waveguides, scatterers, gratings, and resonators.

**Python · C++ · FDTD · Numerical simulation**

### [PackLab](https://github.com/MartinPdeS/PackLab) · Particle structure and correlations

**The challenge.** Particle arrangements affect correlations and scattering, but equilibrium mixtures and irreversible deposition describe different physical processes. Treating their configurations as interchangeable can lead to misleading interpretations.

**My contribution.** I developed complementary workflows for analytical equilibrium correlations, random sequential adsorption, and Metropolis Monte Carlo sampling. They connect physical mixture inputs to particle structure and structure-aware scattering while keeping the assumptions of each method explicit.

**Publication coming soon.**

**Statistical physics · Monte Carlo · Scientific computing**

### [RosettaX](https://github.com/MartinPdeS/RosettaX) · Measurement calibration

**The challenge.** Calibration becomes difficult to reproduce when data loading, peak selection, reference values, fits, and exported settings are spread across disconnected tools. Users need to inspect both the fitted result and the choices behind it.

**My contribution.** I developed a graphical workflow bringing FCS loading, histogram inspection, peak identification, and fluorescence and scattering calibration together. Reusable profiles and calibration exports carry those choices into subsequent analysis.

**Scientific interfaces · Calibration · Reproducible analysis**

### [DeepPeak](https://github.com/MartinPdeS/DeepPeak) · Events in noisy signals

**The challenge.** Overlapping pulses and noise can obscure individual events. A cleaner-looking signal alone does not establish better detection; evaluation must also consider event counts, arrival times, amplitudes, and widths.

**My contribution.** I developed tools for synthetic signal generation, classical peak detection, and optional neural deconvolution. Comparison workflows evaluate direct and deconvolved detection on the same traces, including dilution-series analysis.

**Signal analysis · CNNs · Neural deconvolution**

## Scientific software foundations

| Project | Focus |
| --- | --- |
| [PyOptik](https://github.com/MartinPdeS/PyOptik) | Optical material properties, refractive index, and dispersion |
| [TypedUnit](https://github.com/MartinPdeS/TypedUnit) | Physical quantities with type validation |
| [MPSPlots](https://github.com/MartinPdeS/MPSPlots) | Scientific plotting tools |

## Research background

**Amsterdam UMC · Biomedical optics research · 2024–**

Simulation and computational tools for flow cytometry and optical measurement, including signal processing and neural approaches to particle detection.

**Polytechnique Montréal · PhD in Engineering Physics · 2018–2024**

Optical imaging, fiber photonics, and numerical modeling of light propagation. Developed experimental and computational workflows for microscopy and optical coherence tomography.

Earlier experience includes industrial-camera characterization at **Matrox** and detector characterization for the **ALICE experiment at CERN**.

## How I work

I start with the physical assumptions and the quantity we need to understand, then translate the model into a numerical implementation. My software combines accessible Python interfaces with compiled computation where appropriate, supported by tests, examples, packaging, and documentation.

**Scientific computing:** Python, C++, NumPy, SciPy, pybind11, OpenMP.

**Software engineering:** CMake, Git, GitHub Actions, Pytest, Sphinx.

## Get in touch

Working on an optical simulation, a scientific computing tool, or a measurement pipeline? I’m interested in scientific software engineering and computational optics roles, as well as research collaborations that bring physical models into practical use.

**[martin.poinsinet.de.sivry@gmail.com](mailto:martin.poinsinet.de.sivry@gmail.com)** · **[GitHub / MartinPdeS](https://github.com/MartinPdeS)**
