# Portfolio maintenance

Notes for editing the optional HTML presentation. The public portfolio is the repository README.

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
