![Martin Poinsinet de Sivry-Houle — Computational physicist, scientific software developer](assets/banner.svg)

# Martin Poinsinet de Sivry-Houle

**Computational physicist · Scientific software developer · Python & C++**

I develop open-source scientific software that connects physical models to experimental questions. My work spans light scattering, optical wave propagation, flow cytometry, and signal analysis—from numerical solvers to tools for inspecting measurements and calibrating instruments.

I hold a **PhD in Engineering Physics from Polytechnique Montréal** and conduct biomedical optics research at **Amsterdam UMC**. My background combines optical modeling, experimental physics, and Python/C++ software engineering.

[**View my CV (PDF)**](assets/Martin-Poinsinet-de-Sivry-Houle-CV.pdf) · [GitHub](https://github.com/MartinPdeS) · [Contact me](mailto:martin.poinsinet.de.sivry@gmail.com)

## Selected projects

### [PyMieSim](https://github.com/MartinPdeS/PyMieSim) · Light scattering

How do particle size, material, illumination, and detector geometry affect a scattering measurement? PyMieSim brings these factors into a configurable Lorenz–Mie simulation workflow, supporting spheres, cylinders, and core–shell particles. A Python interface connects the C++ computational backend to individual studies and parameter sweeps.

**Python · C++ · pybind11 · Computational optics**

### [FlowCyPy](https://github.com/MartinPdeS/FlowCyPy) · Flow cytometry simulation

Connects particle populations to simulated detector signals through scattering, fluorescence, and instrument response. Noise sources and detector behavior make it possible to investigate how experimental conditions affect the resulting measurements.

**Physical modeling · Detector simulation · Signal processing**

### [LightWave2D](https://github.com/MartinPdeS/LightWave2D) · Electromagnetic wave propagation

A two-dimensional finite-difference time-domain simulator for studying wave propagation, diffraction, and optical components. Configurable waveguides, scatterers, gratings, and resonators connect geometry to field visualizations.

**Python · C++ · FDTD · Numerical simulation**

### [PackLab](https://github.com/MartinPdeS/PackLab) · Particle structure and correlations

Studies three-dimensional hard-sphere systems using analytical equilibrium correlations, random sequential adsorption, and Metropolis Monte Carlo sampling. These complementary methods connect particle configurations to pair correlations, structure factors, and structure-aware scattering calculations.

**Statistical physics · Monte Carlo · Scientific computing**

### [RosettaX](https://github.com/MartinPdeS/RosettaX) · Measurement calibration

Brings flow cytometry calibration into an inspectable graphical workflow: FCS loading, histogram analysis, peak identification, fluorescence and scattering fits, and reusable calibration export. The application keeps the optical model and practical measurement workflow together.

**Scientific interfaces · Calibration · Reproducible analysis**

### [DeepPeak](https://github.com/MartinPdeS/DeepPeak) · Events in noisy signals

Combines classical peak detection with optional neural deconvolution for one-dimensional signals. Synthetic data and evaluation tools support comparisons of event counts, arrival times, amplitudes, and widths, including overlapping pulses and dilution-series measurements.

**Signal analysis · CNNs · Neural deconvolution**

## Scientific software foundations

| Project | Focus |
| --- | --- |
| [SuPyMode](https://github.com/MartinPdeS/SuPyMode) | Optical supermode and coupling analysis |
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

For scientific software development, computational optics, or research collaboration:

**[martin.poinsinet.de.sivry@gmail.com](mailto:martin.poinsinet.de.sivry@gmail.com)** · **[GitHub / MartinPdeS](https://github.com/MartinPdeS)**
