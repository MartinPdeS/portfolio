# Content notes

The portfolio was curated from neighboring project repositories and the local CV source in September 2026. These notes document provenance for future edits; neighboring files are not runtime dependencies.

| Content | Local source reviewed |
| --- | --- |
| Name, professional email, background | `../CV/shared/personal.tex`, `../CV/docs/profile.md` |
| PhD (2018–2024), Amsterdam UMC research (from 2024) | `../CV/cv/sections/01-education.tex` |
| PyMieSim, FlowCyPy, LightWave2D, PackLab, RosettaX, DeepPeak | Each project’s root `README.rst` |
| PyOptik | `../PyOptik/README.rst` |
| TypedUnit package spelling | `../TypedUnit/pyproject.toml` (README retains older TypedUnits wording) |
| SuPyMode | Local documentation gallery and existing project description; described conservatively as supermode and coupling analysis |

## Editorial conventions

- Describe concrete capabilities and workflows; avoid unsupported adoption, speed, coverage, citation, and download claims.
- Keep historical qualifications distinct from current employment. Review the research role when updating the site.
- Link to repository roots for source and documentation discovery, avoiding guessed version-specific API links.
- Do not copy street addresses, phone numbers, private career notes, or tailored CV documents into the public site.
- Treat the canvas and SVG artwork as illustrations. They are not simulations produced by the featured packages.
- Add publications only after verifying title, authors, venue, and persistent identifier.

The old placeholder publications, impact statistics, example APIs, document links, and community links were removed because their claims or targets could not be substantiated from the reviewed local material. The unused statistics script no longer modifies portfolio prose or estimates users from stars.

## Name and initials

First name: **Martin**. Last name: **Poinsinet de Sivry-Houle**. Initials: **MPdSH**, preserving this capitalization. Keep the complete last name together when splitting the name across display lines.

## Portfolio format

The README is the primary portfolio, intended to present Martin and his work directly on GitHub. Keep local setup, deployment, and maintenance instructions out of it; these belong in MAINTENANCE.md.

## Public CV

At Martin’s explicit request, `../CV/CV.pdf` is included unchanged as `assets/Martin-Poinsinet-de-Sivry-Houle-CV.pdf` and linked from the portfolio. This is a snapshot of the existing PDF, not a rebuild of the LaTeX sources.

## Verified software publications

Verified against the local CV and online records:

- **SuPyMode (2024):** author order, title, journal, volume, issue, pages, and DOI confirmed by [Polytechnique Montréal’s institutional record](https://publications.polymtl.ca/58531/). DOI: `10.1364/OPTCON.513562`.
- **PyMieSim (2023):** author order, title, journal, volume, issue, pages, and DOI confirmed by [the project’s official citation](https://martinpdes.github.io/PyMieSim/docs/latest/index.html) and [Polytechnique Montréal’s author bibliography](https://publications.polymtl.ca/view/person/Poinsinet_De_Sivry-Houle%2C_Martin.date.html). DOI: `10.1364/OPTCON.473102`.
- Article summaries reflect the publisher article text accessible through its ResearchGate full-text copies. Publisher landing pages resolve but did not expose readable text in the browser tool.
- **PackLab and FlowCyPy:** “publications coming soon” is Martin’s stated status. Do not infer a journal, publication date, acceptance, or DOI.

Publication titles and coauthor spellings follow the bibliographic records. Martin’s displayed name follows his stated capitalization.

## Professional direction and contributions

Positioning emphasizes scientific software engineering and computational optics, grounded in the CV’s scientific software, algorithm engineering, photonics, and biomedical optics experience. The portfolio expresses interest in relevant roles and collaborations without claiming an employment transition or availability date.

Project showcases distinguish the scientific/engineering challenge from Martin’s software contribution. First-person development descriptions are grounded in the local CV and project repositories; they do not assert sole authorship of collaborative research. Published examples are linked for PyMieSim and SuPyMode. Do not turn package capabilities into unsupported performance or experimental-validation claims.

## Project media

README project figures are now actual documentation assets, separate from the schematic banner and HTML artwork. Their sources and context are recorded in [media/project-assets.json](media/project-assets.json). Copies preserve the original bytes. Captions distinguish simulation output and illustrative calibration data from experimental measurements.
