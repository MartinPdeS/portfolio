# Portfolio visuals

All artwork is stored locally in `assets/`:

- `banner.svg`: custom README banner, pairing the name and specialization with a wave illustration.
- `social-preview.png`: browser-rendered banner for social sharing previews.
- `field.svg`: static hero illustration, replaced by the interactive canvas when JavaScript is available.
- `scatter.svg`, `signal.svg`, `wave.svg`, `pack.svg`, `calibrate.svg`, `peaks.svg`: project illustrations.
- `favicon.svg`: browser icon.

The canvas is drawn by `assets/main.js`. All these visuals are original schematic illustrations, not numerical outputs from the featured packages. The wavelength control uses arbitrary units.

For future scientific figures, include the project version, generating example, and relevant physical parameters. Optimize files and provide descriptive alternative text.

## Project results in the portfolio

The README includes existing documentation figures and GIF animations, copied unchanged into `assets/projects/`. Click a figure in the README to open the full-size asset.

| Project | Visual | Source in the project’s docs folder |
| --- | --- | --- |
| PyMieSim | [pymiesim-resonances.png](../assets/projects/pymiesim-resonances.png) | `docs/images/resonances.png` |
| SuPyMode | [supymode-mode-propagation.gif](../assets/projects/supymode-mode-propagation.gif) | `docs/images/mode_propagation.gif` (GitHub) |
| FlowCyPy | [flowcypy-detector-signals.png](../assets/projects/flowcypy-detector-signals.png) | `docs/images/signal_example.png` |
| LightWave2D | [lightwave2d-lens.gif](../assets/projects/lightwave2d-lens.gif) | `docs/images/lens.gif` |
| PackLab | [packlab-rsa-packing.png](../assets/projects/packlab-rsa-packing.png) | `docs/images/readme_rsa_packing.png` |
| RosettaX | [rosettax-fluorescence-calibration.png](../assets/projects/rosettax-fluorescence-calibration.png) | `docs/source/gallery/images/sphx_glr_fluorescence_calibration_001.png` |
| DeepPeak | [deeppeak-detection.png](../assets/projects/deeppeak-detection.png) | `docs/source/gallery/images/sphx_glr_classical_detection_pipeline_001.png` |

The [asset manifest](project-assets.json) records the exact source paths, context files, byte sizes, and SHA-256 checksums. These are historical documentation outputs, not newly generated results or a claim that the current source reproduces them byte for byte.

RosettaX’s calibration uses illustrative values. DeepPeak’s trace and FlowCyPy’s detector signals are synthetic. PackLab’s image is a slice visualization of a three-dimensional packing. The original figures retain their labels, units, and aspect ratios.

No MP4, WebM, MOV, or AVI files were found in the neighboring repositories’ docs folders during this review; LightWave2D supplied the GIF animations.

### SuPyMode animation

The [mode-propagation animation](https://github.com/MartinPdeS/SuPyMode/blob/master/docs/images/mode_propagation.gif) was downloaded from the exact GitHub path selected by Martin and copied unchanged. It is the only SuPyMode visual in the README.
