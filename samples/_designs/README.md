# DotCom by Arshees — sample designs

Original designs used by the "New website builder" scheduled task for portal samples.

- `base.css` — shared layout, sample banner, watermark, cards, animations.
- `modern.css`, `serene.css`, `warm.css` — the three looks (fonts, colours, hero layout).
- `template.html` — page structure with `{{PLACEHOLDERS}}` (example with 2 doctors; repeat or remove `.doc-card` blocks; with one doctor, make the doctor the hero).

To build a sample: copy `template.html` → `samples/<clientId>/index.html`, `base.css` → `base.css`, the chosen theme → `theme.css`, add the photos, fill every placeholder and remove any section whose data is missing.
