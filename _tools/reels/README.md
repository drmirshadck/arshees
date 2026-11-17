# DotCom by Arshees – Reel renderer
Used by the weekly Reels scheduled task. Not served on the site (Jekyll skips folders starting with _).
Setup: `npm i @fontsource/rubik@5 @fontsource/noto-sans-malayalam@5` in the folder you run from (make_reel.py looks for node_modules/@fontsource next to itself).
Render: `python3 make_reel.py spec.json out.mp4` (add `--frames-only` for preview PNGs).
