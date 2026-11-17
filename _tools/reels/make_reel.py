"""DotCom by Arshees – render a 1080x1920 Instagram Reel (silent) from a JSON spec.

Usage: python3 make_reel.py spec.json out.mp4 [--frames-only]
spec = {"scenes": [{"dur": 4.2, "html": "<inner html>"}, ...]}
Scene HTML can use the classes defined in CSS below. Elements with class "in" animate in;
set style="--d:.4s" for a delay. Every scene fades in/out automatically.
"""
import base64, json, pathlib, subprocess, sys, os
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
NM = ROOT / "node_modules/@fontsource"
W, H, FPS = 1080, 1920, 30


def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()


def fonts():
    css = ""
    for w in (400, 500, 700, 800):
        css += f"@font-face{{font-family:Rubik;font-weight:{w};src:url(data:font/woff2;base64,{b64(NM / f'rubik/files/rubik-latin-{w}-normal.woff2')})}}"
    for w in (400, 700, 800):
        css += f"@font-face{{font-family:NotoML;font-weight:{w};src:url(data:font/woff2;base64,{b64(NM / f'noto-sans-malayalam/files/noto-sans-malayalam-malayalam-{w}-normal.woff2')})}}"
    return css


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;font-family:Rubik,NotoML,sans-serif;color:#F3F2FF;background:#07070F;overflow:hidden;position:relative}
.ml{font-family:NotoML,Rubik,sans-serif}
.bg{position:absolute;inset:-200px;background:
 radial-gradient(900px 800px at 85% 5%,rgba(124,92,255,.55),transparent 60%),
 radial-gradient(900px 800px at 0% 95%,rgba(0,212,255,.35),transparent 60%),#07070F;animation:drift 12s ease-in-out both}
@keyframes drift{from{transform:translate(0,0) scale(1)}to{transform:translate(-60px,40px) scale(1.06)}}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:60px 60px}
.wrap{position:absolute;inset:0;padding:150px 84px 420px;display:flex;flex-direction:column;animation:fadein .35s ease both}
@keyframes fadein{from{opacity:0}to{opacity:1}}
.logo{display:flex;align-items:center;gap:16px;font-weight:700;font-size:38px;font-family:Rubik}
.mk{width:66px;height:66px;border-radius:18px;background:linear-gradient(135deg,#00D4FF,#7C5CFF);display:grid;place-items:center}
.logo small{font-weight:400;font-size:28px;color:#A3A1BF}
.mid{margin:auto 0;display:flex;flex-direction:column}
.kick{font-family:monospace;letter-spacing:.16em;text-transform:uppercase;font-size:30px;color:#2BE3A1}
.kick.ml{font-family:NotoML,sans-serif;letter-spacing:0;text-transform:none;font-size:34px;font-weight:700}
h1{font-size:104px;line-height:1.05;font-weight:800;letter-spacing:-.02em;margin-top:26px}
h1.ml{font-size:84px;line-height:1.3;letter-spacing:0}
h2{font-size:80px;line-height:1.08;font-weight:800;letter-spacing:-.02em}
h2.ml{font-size:66px;line-height:1.35;letter-spacing:0}
.grad{background:linear-gradient(90deg,#00D4FF,#7C5CFF 55%,#FF4F9A);-webkit-background-clip:text;background-clip:text;color:transparent}
p.lead{font-size:46px;line-height:1.4;color:#C9C7E3;margin-top:34px}
p.lead.ml{font-size:42px;line-height:1.55}
.big{font-size:300px;font-weight:800;line-height:1}
.li{display:flex;gap:30px;align-items:center;margin-top:38px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:32px;padding:34px 38px}
.li .ic{width:86px;height:86px;border-radius:24px;flex:none;display:grid;place-items:center;font-size:44px;background:linear-gradient(135deg,#00D4FF,#7C5CFF)}
.li b{font-size:48px;font-weight:700;line-height:1.25}
.li b.ml{font-size:42px;line-height:1.45}
.pill{display:inline-block;padding:30px 50px;border-radius:999px;background:linear-gradient(90deg,#00D4FF,#7C5CFF);color:#fff;font-weight:800;font-size:58px;margin-top:50px;align-self:flex-start}
.frame{border-radius:30px;overflow:hidden;border:1px solid rgba(255,255,255,.14);box-shadow:0 60px 100px -40px rgba(124,92,255,.75);background:#111;margin-top:50px}
.bar{height:56px;background:#16152B;display:flex;align-items:center;gap:12px;padding:0 24px;font-family:monospace;font-size:24px;color:#A3A1BF}
.bar i{width:15px;height:15px;border-radius:50%;background:#FF5F57}.bar i+i{background:#FEBC2E}.bar i+i+i{background:#28C840;margin-right:16px}
.frame img{display:block;width:100%}
.foot{position:absolute;left:84px;right:84px;bottom:330px;font-size:32px;color:#A3A1BF;font-family:Rubik}
.in{animation:up .7s cubic-bezier(.2,.8,.2,1) both;animation-delay:var(--d,0s)}
@keyframes up{from{opacity:0;transform:translateY(60px)}to{opacity:1;transform:none}}
.pop{animation:pop .6s cubic-bezier(.2,1.4,.4,1) both;animation-delay:var(--d,0s)}
@keyframes pop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:none}}
.zoom{animation:zoom 8s ease-out both}
@keyframes zoom{from{transform:scale(1)}to{transform:scale(1.08)}}
"""

BOLT = '<svg width="34" height="34" viewBox="0 0 24 24"><path d="M13.5 2 6 13.5h5L9.5 22 18 9.5h-5.5z" fill="#fff"/></svg>'
LOGO = f'<div class="logo"><span class="mk">{BOLT}</span>DotCom <small>by Arshees</small></div>'


def page(inner, font_css):
    return (f'<html><head><meta charset="utf-8"><style>{font_css}{CSS}</style></head><body>'
            f'<div class="bg"></div><div class="grid"></div><div class="wrap">{LOGO}<div class="mid">{inner}</div></div>'
            f'<div class="foot">arshees.com/dotcom</div></body></html>')


def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    out = pathlib.Path(sys.argv[2]).resolve()
    frames_only = "--frames-only" in sys.argv
    work = out.with_suffix("")
    work.mkdir(parents=True, exist_ok=True)
    fc = fonts()
    parts = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.route("http*://**", lambda r: r.abort())
        for i, sc in enumerate(spec["scenes"]):
            html = page(sc["html"], fc)
            hp = work / f"s{i}.html"
            hp.write_text(html)
            pg.goto(hp.as_uri())
            pg.evaluate("document.fonts.ready")
            dur = float(sc["dur"])
            n = max(1, round(dur * FPS))

            def seek(t):
                pg.evaluate("t=>{for(const a of document.getAnimations()){a.pause();a.currentTime=t*1000}}", t)
                # fade-out in last .3s
                op = max(0.0, min(1.0, (dur - t) / 0.3)) if i < len(spec["scenes"]) - 1 else 1.0
                pg.evaluate("o=>document.body.style.opacity=o", op)

            if frames_only:
                for t in (0.5, min(dur - 0.4, 2.5)):
                    seek(t)
                    pg.screenshot(path=str(work / f"preview_s{i}_{t:.1f}.png"))
                continue
            tmp = work / f"s{i}.tmp.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                                   "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                                   "-pix_fmt", "yuv420p", "-r", str(FPS), str(tmp)], stdin=subprocess.PIPE)
            for f in range(n):
                seek(f / FPS)
                ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close()
            if ff.wait() != 0:
                sys.exit(f"ffmpeg failed on scene {i}")
            final = work / f"s{i}.mp4"
            os.replace(tmp, final)
            parts.append(final)
        b.close()
    if frames_only:
        return
    lst = work / "list.txt"
    lst.write_text("".join(f"file '{x}'\n" for x in parts))
    tmp = out.with_name(out.stem + ".tmp.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    "-movflags", "+faststart", str(tmp)], check=True)
    os.replace(tmp, out)
    print(out)


if __name__ == "__main__":
    main()
