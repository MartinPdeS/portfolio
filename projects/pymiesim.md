# PyMieSim — light scattering, made explorable

[Source and documentation](https://github.com/MartinPdeS/PyMieSim) · [Back to projects](README.md)

PyMieSim is an open-source Python package for Lorenz–Mie scattering simulations, with a C++ computational backend. It supports spheres, cylinders, and core–shell particles, configurable illumination, and detector models.

## The question

How do particle size, refractive index, illumination, and collection geometry change a scattering measurement?

## The implementation

The package connects particle solvers to plane-wave and Gaussian sources, photodiodes and coherent-mode detectors, and pandas outputs. It supports both individual studies and parametric experiments. Python provides the experimental interface, with compiled numerical code underneath.

## Why it matters

A reproducible simulation needs to describe both the particle and the measurement. Bringing sources, scatterers, and detectors together makes those assumptions explicit and allows systematic exploration.

## Explore

The upstream repository contains installation instructions, examples, documentation links, and the web GUI link. Use examples from the installed version’s documentation; APIs evolve between releases.

This showcase does not claim a measured speedup, adoption figure, or test-coverage percentage.
