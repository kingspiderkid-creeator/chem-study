# Compound Builder

A study tool for chemistry and biology students. Drag elements from the periodic table onto the bench, bond atoms by moving them together, and discover molecules and compounds. Hovering any element shows a picture and description. Discoveries are saved in the Collection tab (in the visitor's browser).

It is a plain static site: no build step, no framework, no server code.

```
index.html              the whole app
data/elements.json      descriptions, photos and colors for the 118 elements
data/compounds.json     the molecule and compound library
images/elements/        put element photos here (Cu.jpg, Au.png, ...)
tools/sync_images.py    optional helper that links photos into elements.json
```

## Publish it with GitHub Pages

1. Create a new public repository on GitHub and upload everything in this folder (keep the folder structure). Dragging files into the web interface works.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, pick the `main` branch and the `/ (root)` folder, then save.
4. After a minute or two the site is live at `https://YOUR-USERNAME.github.io/YOUR-REPO/`.

Every commit you make afterwards republishes the site automatically.

## Run it on your own computer

Browsers block a page from reading local files, so double-clicking `index.html` shows an error message. Start a small local server instead:

```
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Add or change element descriptions, photos and colors

Open `data/elements.json`. Each element looks like this:

```json
"Cu": {
  "name": "Copper",
  "description": "A reddish metal and excellent conductor, used in wiring.",
  "color": "#c8743c",
  "image": "images/elements/Cu.jpg",
  "credit": "Photo by Jane Doe, CC BY-SA 4.0"
}
```

| Field | What it does |
| --- | --- |
| `description` | Text on the hover card. If empty, a general description for the element's category is shown. |
| `color` | Typical color used for the drawn illustration (any hex color). Only used when there is no photo. |
| `image` | Path to a photo. If empty or the file is missing, the drawn illustration is shown instead. |
| `credit` | Shown under the photo. Fill this in whenever the license requires attribution. |

**Adding photos, the quick way:**

1. Save a square-ish photo (about 200 to 400 pixels wide is plenty) into `images/elements/`, named by symbol: `Cu.jpg`, `Au.png`, and so on.
2. Run `python3 tools/sync_images.py`. It fills in the `image` field for every photo it finds.
3. Add the `credit` text for each photo in `elements.json`.
4. Commit and push.

You can also edit the `image` field by hand, and it can point to a full web address if you host photos elsewhere.

Photos from Wikimedia Commons are a good source. Check each file's license and credit the photographer when it requires it.

## Add or change compounds

Open `data/compounds.json`. Each entry looks like this:

```json
{
  "formula": "H2O",
  "name": "Water",
  "type": "polar covalent",
  "description": "Bent, 104.5°. Hydrogen bonds give it a high boiling point."
}
```

- `formula` is written with element symbols and counts, like `CaCO3` or `C2H5OH`. The app matches a build by counting atoms, so `CH3OH` and `CH4O` mean the same thing. Two compounds with the same atom counts (isomers) can't both be in the library.
- `type` must be `nonpolar covalent`, `polar covalent` or `ionic`.
- Keep the file valid JSON: commas between entries, no comma after the last one.

## Notes

- A molecule is recognized by the atoms that are touching, not by checking that the bonds are chemically valid. Anything not in `compounds.json` shows as "Not in this library".
- Electron shells use the standard filling order, with corrections for common exceptions such as Cr, Cu, Ag and Au. A few heavy elements may still differ slightly from measured configurations.
- On touch screens, tap an element to add it (dragging from the table would conflict with scrolling).
- The Collection tab uses the browser's local storage, so progress stays on that device and browser.
