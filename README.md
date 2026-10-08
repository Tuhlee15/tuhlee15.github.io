# Tully Njoroge · Projects

Personal portfolio site, hosted free on GitHub Pages.

| Field | Project | Status |
|---|---|---|
| Aerospace & ventures | **Helix Logistics**: case study + interactive flight-ops and dispatch simulator | Live |
| Data & analytics | **H-1B Employer Research**: Power BI report | In progress |
| Finance & investments | **Managing Global Portfolios**: utilities equity research | Overview |

## Structure

```
index.html                         home page (project index)
assets/site.css                    shared styles (light + dark)
assets/helix-logo.png, helix-console.jpg
projects/helix-logistics/index.html      case study (thesis & background)
projects/helix-logistics/simulator.html  the simulator (one self-contained file)
projects/h1b-employer-research/index.html
projects/global-portfolios/index.html
```

Plain HTML, CSS and JavaScript. No build step and nothing to install.

## Publish on GitHub Pages (first time, all in the browser)

1. Sign in at github.com, click **+** (top right) → **New repository**.
2. Name it exactly **`YOUR-USERNAME.github.io`** (your GitHub username). Set it to **Public** and leave every "initialize" box unchecked. Click **Create repository**.
3. On the empty repo page, click **uploading an existing file**.
4. Unzip `tully-portfolio.zip` on your computer, open the folder, select **everything inside it** (`index.html`, `README.md`, `assets`, `projects`) and drag it onto the upload area. Chrome or Edge keep the folders intact.
5. Scroll down and click **Commit changes**.
6. Go to **Settings → Pages**. Under *Build and deployment*, set Source to **Deploy from a branch**, Branch to **main** and folder **/ (root)**, then click **Save**.
7. After 1–2 minutes the site is live at **https://YOUR-USERNAME.github.io**. The simulator is at `/projects/helix-logistics/simulator.html`.

## After it's live

- **Add your links:** open `index.html` on GitHub, click the pencil icon, and replace `YOUR-LINKEDIN` and `YOUR-USERNAME` in the *About* section. Commit, and the site updates within a minute.
- **Add a project:** copy `projects/global-portfolios/` to a new folder, edit the text, then add a card for it in `index.html`.
- **Custom domain (optional):** buy a domain such as `tullynjoroge.com` (about $10–15 a year), then enter it under **Settings → Pages → Custom domain** and follow GitHub's DNS instructions.

## Disclaimer

The Helix Logistics simulator is a concept demonstration built from an MBA capstone. Its capabilities are modeled on technologies evaluated from NASA's public technology-transfer catalog; no licenses were obtained. It is not affiliated with or endorsed by NASA or Elroy Air. Aircraft performance beyond published payload and range is an assumption, geography is simplified, and facilities and traffic are fictional.
