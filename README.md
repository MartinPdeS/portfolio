# 👋 Welcome to Martin Poinsinet de Sivry-Houle's Portfolio

<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6&height=300&section=header&text=Computational%20Physicist%20&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Optical%20Simulations%20•%20Scientific%20Computing%20•%20Open%20Source&descAlignY=51&descAlign=62)

[![Python](https://img.shields.io/badge/Python-Expert-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![C++](https://img.shields.io/badge/C++-Advanced-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)](https://isocpp.org)
[![Scientific Computing](https://img.shields.io/badge/Scientific_Computing-Expert-FF6B6B?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![Optics](https://img.shields.io/badge/Computational_Optics-Specialist-4ECDC4?style=for-the-badge&logo=lens&logoColor=white)](#)

</div>

## About Me

I am a **Computational Physicist** specializing in **optical simulations** and **scientific computing**. My passion lies in developing cutting-edge tools and algorithms that bridge the gap between theoretical physics and practical applications in photonics and electromagnetic modeling.

### Core Expertise
- **Electromagnetic Simulations**: Advanced modeling of light-matter interactions
- **Mie Theory**: Deep expertise in scattering theory and implementation
- **Finite Element Methods**: Complex waveguide and supermode analysis
- **Scientific Software Development**: High-performance computing solutions
- **GUI Development**: User-friendly interfaces for complex scientific tools

---

## Featured Projects

<div align="center">

### Major Scientific Computing Libraries

</div>

<table>
<tr>
<td width="50%">

#### 🔬 [PyMieSim](https://github.com/MartinPdeS/PyMieSim)
**Advanced Mie Scattering Simulation Framework**

```python
# Elegant API for complex scattering calculations
from PyMieSim.experiment import Setup
from PyMieSim.experiment.source import Gaussian
from PyMieSim.experiment.scatterer import Sphere

setup = Setup(
    source=Gaussian(wavelength=632.8),
    scatterer=Sphere(diameter=1000),
    detector=Photodiode()
)
data = setup.get('Qsca')  # Scattering efficiency
```

**🎯 Key Features:**
- High-performance C++ backend with Python interface
- Interactive GUI for parameter exploration
- Comprehensive measurement capabilities
- Extensible architecture for custom experiments

</td>
<td width="50%">

#### [SuPyMode](https://github.com/MartinPdeS/SuPyMode)
**Supermode Analysis for Optical Waveguides**

```python
# Sophisticated waveguide mode analysis
from SuPyMode import FiberFactory, SuperMode

fiber = FiberFactory.load_from_catalog()
solver = SuperMode(fiber)
solver.compute_modes()

# Advanced coupling analysis
coupling = solver.get_coupling_matrix()
```

**🎯 Key Features:**
- Finite element eigenmode solver
- Adiabatic coupling analysis
- Complex geometry support
- Comprehensive visualization tools

</td>
</tr>
</table>

<table>
<tr>
<td width="50%">

#### [PyOptik](https://github.com/MartinPdeS/PyOptik)
**Comprehensive Optical Materials Database**

```python
# Extensive refractive index database
from PyOptik import Material

glass = Material.BK7
n_index = glass.get_refractive_index(wavelength=550)

# Temperature-dependent properties
n_temp = glass.get_refractive_index(
    wavelength=633, temperature=300
)
```

**🎯 Key Features:**
- Extensive material database (>400 materials)
- Temperature and wavelength dependencies
- Advanced interpolation algorithms
- Built-in visualization capabilities

</td>
<td width="50%">

#### [LightWave2D](https://github.com/MartinPdeS/LightWave2D)
**2D Wave Propagation Simulator**

```python
# Advanced electromagnetic wave simulation
from LightWave2D import Simulator, Gaussian

sim = Simulator(resolution=1024)
beam = Gaussian(waist=50e-6, wavelength=1550e-9)

# Complex propagation scenarios
field = sim.propagate_through_medium(
    beam, medium=custom_structure
)
```

**Key Features:**
- FDTD and beam propagation methods
- Complex structure modeling
- GPU acceleration support
- Real-time visualization

</td>
</tr>
</table>

---

## Technical Skills & Tools

<div align="center">

### Programming Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=flat-square&logo=mathworks&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)

### Scientific Computing
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Eigen](https://img.shields.io/badge/Eigen-FF6B6B?style=flat-square&logo=cpp&logoColor=white)

### Development Tools
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![CMake](https://img.shields.io/badge/CMake-064F8C?style=flat-square&logo=cmake&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Sphinx](https://img.shields.io/badge/Sphinx-000000?style=flat-square&logo=sphinx&logoColor=white)

### Specialized Libraries
![PyBind11](https://img.shields.io/badge/PyBind11-4285F4?style=flat-square&logo=python&logoColor=white)
![OpenMP](https://img.shields.io/badge/OpenMP-4479A1?style=flat-square&logo=openmp&logoColor=white)
![MPI](https://img.shields.io/badge/MPI-FF6B35?style=flat-square&logo=message-passing-interface&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-00D8FF?style=flat-square&logo=plotly&logoColor=white)

</div>

---

## GitHub Statistics

<div align="center">

<table>
<tr>
<td width="50%">

![Martin's GitHub Stats](https://github-readme-stats.vercel.app/api?username=MartinPdeS&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true)

</td>
<td width="50%">

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=MartinPdeS&layout=compact&theme=tokyonight&hide_border=true&langs_count=8)

</td>
</tr>
</table>

![Contribution Graph](https://github-readme-activity-graph.vercel.app/graph?username=MartinPdeS&theme=tokyo-night&hide_border=true&area=true)

</div>

---

## Research & Publications

### Academic Contributions
- **Computational Electromagnetics**: Advanced algorithms for scattering simulations
- **Optical Waveguide Theory**: Supermode analysis and coupling dynamics
- **High-Performance Computing**: Parallel algorithms for electromagnetic modeling
- **Scientific Software Engineering**: Best practices for research software development

### Impact Metrics
- **Open Source Projects**: 15+ actively maintained repositories
- **Community Reach**: 1000+ users across scientific computing tools
- **Documentation**: Comprehensive tutorials and API references
- **Code Quality**: 95%+ test coverage across major projects

---

## What Makes My Work Special

<div align="center">

<table>
<tr>
<td width="33%" align="center">

### Scientific Rigor
**Theory-Driven Development**
- Deep physics understanding
- Mathematically sound algorithms
- Peer-reviewed methodologies
- Reproducible research practices

</td>
<td width="33%" align="center">

### ⚡ Performance Focus
**High-Performance Computing**
- C++ optimized backends
- Parallel algorithm design
- Memory-efficient implementations
- GPU acceleration where beneficial

</td>
<td width="33%" align="center">

### User Experience
**Accessible Complex Science**
- Intuitive Python APIs
- Interactive GUI interfaces
- Comprehensive documentation
- Educational examples

</td>
</tr>
</table>

</div>

---

## 📫 Let's Connect!

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-MartinPdeS-181717?style=for-the-badge&logo=github)](https://github.com/MartinPdeS)
[![Email](https://img.shields.io/badge/Email-Contact_Me-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@domain.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-Follow-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white)](https://researchgate.net/profile/yourprofile)

</div>

---

<div align="center">

### "Bridging the gap between theoretical physics and practical applications through elegant code"

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6&height=100&section=footer)

</div>

## Repository Structure

```
portfolio/
├── projects/          # Detailed project showcases
├── research/          # Academic papers and presentations
├── tutorials/         # Educational content and guides
├── media/            # Screenshots, videos, demos
└── contact/          # Contact information and CV
```

---

**If you find my work interesting, please consider giving my repositories a star!**

*Last updated: August 2025*