# DotCom by Arshees — sample designs

Used by the "New website builder (portal requests)" scheduled task for portal samples.

## The five designs (pick ONE at random for each sample, never the same as the previous sample)

| Folder | Look | Based on |
|---|---|---|
| `ammar/` | warm orange, big round photo on an orange orb, oval step cards | Dr Ammar's site |
| `anish/` | teal, arched portrait(s) — two arches when there are 2+ doctors | Dr Anish's site |
| `arun/` | teal, round portrait with ring, stats band | Dr Arun's site |
| `murshida/` | navy & sky blue, large hero card, photo grid | Dr Murshida's site |
| `vigeesh/` | deep blue, full-height hero photo, word-by-word headline, marquee | Dr Vigeesh's site |

Each folder is self-contained: `template.html` + `style.css` (the original design's CSS plus the sample protection at the end). Nothing from the original doctors is in these files — no names, photos, phone numbers, links, Cal.com or Daily.

The older generic looks (`template.html`, `base.css`, `modern.css`, `serene.css`, `warm.css` in this folder) are kept for reference only and are **not** in the random rotation.

## Building a sample

1. Copy the chosen folder's `template.html` → `samples/<clientId>/index.html` and `style.css` → `samples/<clientId>/style.css`.
2. Add photos: `doctor1.jpg`, `doctor2.jpg`, … (portraits about 560×700) and, if given, `clinic1.jpg`, `clinic2.jpg`, …
   - `murshida/` also uses `doctor1.jpg` as the CSS background of its photo boxes (`.q`).
   - No suitable photo: use the commented `<span class="initials">{{INITIALS}}</span>` instead of the `<img>`.
3. Fill every placeholder. Remove any line or section whose data is missing (never invent).
4. **One doctor:** the doctor is the hero; delete the sections marked `2+ DOCTORS ONLY` and the nav link marked `2+ doctors`.
   **2+ doctors:** use the commented `2+ doctors` hero lines (clinic name as the hero; `anish/` shows two arches — add the second arch and remove the class `solo`), keep the "Our doctors" section and repeat the block between `DOCTOR CARD START` / `DOCTOR CARD END` once per doctor (`doctor1.jpg`, `doctor2.jpg`, …). In `vigeesh/` and `murshida/` also delete the single-doctor about section, as their comments say.
5. Keep: the fixed SAMPLE banner, the SAMPLE watermark in the hero, `noindex,nofollow`, the disabled buttons ("Available after confirmation"), the reveal animations, and the "Developed by DotCom by Arshees" link.

## Placeholders

`{{SITE_NAME}}` (doctor's name for one doctor, clinic name for 2+) · `{{SITE_NAME_UPPER}}` · `{{TAGLINE}}` (e.g. "Online Homoeopathy Clinic") · `{{DOCTOR_NAME}}` · `{{FIRST_NAME}}` · `{{INITIALS}}` · `{{QUALIFICATION}}` · `{{QUAL_SHORT}}` (e.g. BHMS) · `{{SPECIALTY}}` · `{{SPECIALTY_LOWER}}` · `{{REG}}` · `{{LANGUAGES}}` · `{{LANG_COUNT}}` · `{{FEE}}` (online consultation fee only) · `{{ABOUT}}` · `{{CLINIC_NAME}}` · `{{CITY}}` · `{{ADDRESS}}` · `{{TIMINGS}}` · `{{PHONE}}` · `{{EMAIL}}` · `{{YEAR}}` · `{{LOGO_LETTER}}` · `{{PHOTO_CAPTION}}` · `{{INSTAGRAM_URL}}` (only if given) · second doctor in `anish/` hero: `{{DOCTOR_2_NAME}}`, `{{DOCTOR_2_QUALIFICATION}}`.
