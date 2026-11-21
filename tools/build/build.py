#!/usr/bin/env python3
"""Builds posts/fan-regulator/fan-regulator.mp4 from images/ + audio/vo.mp3.

One image per spoken phrase, cut just before each phrase starts (times measured from the
ElevenLabs take with ffmpeg silencedetect), a slow sub-pixel push-in / pull-back / pan per image,
and one burnt-in Devanagari caption at a time (rendered by ./caption, CoreText). Ends on image 01
so the loop is seamless.

usage: python3 build/build.py            (from posts/fan-regulator/)
       python3 build/build.py --stills   (writes one still per shot to build/stills/ for review)
"""
import os, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS = 1080, 1920, 30
LEAD = 0.12           # picture cuts this long before the phrase starts
CAP_Y = 1250          # caption centre line (NICHE.md: ~1150–1300 px band)

# (image, speech start, speech end, motion, caption) — times from audio/vo.mp3 (35.63 s)
SHOTS = [
    ("01-wall-knob",       0.00,  2.07, "in",   "दीवार का ये छोटा-सा नॉब…"),
    ("02-fan-fast",        2.59,  4.55, "in",   "पंखे को धीमा-तेज़ कैसे करता है?"),
    ("03-old-regulator",   5.48,  7.13, "in",   "पुराने काले रेगुलेटर में…"),
    ("04-old-coil-cutaway",7.50,  9.03, "in",   "तार की कॉइल लगी होती थी।"),
    ("05-old-less-power",  9.65, 11.51, "pan",  "पंखे तक कम बिजली पहुँचती थी…"),
    ("06-old-heat",       11.96, 14.10, "up",   "बाकी गर्मी बनकर जल जाती थी।"),
    ("07-new-regulator",  14.87, 15.98, "out",  "नए रेगुलेटर में…"),
    ("08-new-capacitors", 16.35, 18.55, "in",   "कॉइल की जगह कैपेसिटर लगे होते हैं।"),
    ("09-capacitor-in",   19.04, 20.92, "in",   "कैपेसिटर बिजली को जलाते नहीं…"),
    ("10-capacitor-back", 21.26, 23.36, "out",  "बस थामकर वापस लौटा देते हैं।"),
    ("11-knob-turn",      24.04, 27.03, "in",   "नॉब घुमाते ही छोटा-बड़ा कैपेसिटर जुड़ता है…"),
    ("12-fan-slow",       27.36, 28.83, "out",  "और बदल जाती है रफ़्तार।"),
    ("13-new-saves",      29.47, 32.16, "in",   "तो 1 पर नया रेगुलेटर बिजली बचाता है…"),
    ("14-old-vs-new",     32.52, 35.41, "out",  "और पुराना वही बिजली गर्मी में उड़ा देता था।"),
]
VO_END = 35.63
LOOP = ("01-wall-knob", "settle")   # last 1.3 s returns to the opening frame
TOTAL = 36.93


def clips():
    out = []
    for i, (img, s, e, mot, cap) in enumerate(SHOTS):
        t0 = 0.0 if i == 0 else s - LEAD
        t1 = SHOTS[i + 1][1] - LEAD if i + 1 < len(SHOTS) else VO_END
        cs = max(s - 0.05, 0.5)                       # no caption in the first half-second
        ce = min(e + 0.18, t1 - 0.02)
        out.append(dict(img=img, t0=t0, t1=t1, mot=mot, cap=cap, cs=cs, ce=ce, n=i + 1))
    out.append(dict(img=LOOP[0], t0=VO_END, t1=TOTAL, mot=LOOP[1], cap=None, cs=0, ce=0, n=15))
    return out


def ease(u):
    return u * u * (3 - 2 * u)


def view(mot, u):
    """zoom (>=1) and centre offset (fraction of frame) for progress u in 0..1"""
    u = ease(u)
    if mot == "in":     return 1.0 + 0.07 * u, 0.0, 0.0
    if mot == "out":    return 1.07 - 0.07 * u, 0.0, 0.0
    if mot == "up":     return 1.03 + 0.05 * u, 0.0, -0.02 * u
    if mot == "pan":    return 1.08, -0.03 + 0.06 * u, 0.0
    if mot == "settle": return 1.04 - 0.04 * u, 0.0, 0.0
    return 1.0, 0.0, 0.0


def frame(src, z, dx, dy):
    sw, sh = src.size
    s = max(W / sw, H / sh) * z                # output px per source px
    cx = sw / 2 + dx * W / s
    cy = sh / 2 + dy * H / s
    a = 1 / s
    return src.transform((W, H), Image.AFFINE, (a, 0, cx - W / 2 * a, 0, a, cy - H / 2 * a), Image.BICUBIC)


def caption_png(n, text):
    p = os.path.join(ROOT, "build", "captions", f"{n:02d}.png")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    subprocess.run([os.path.join(ROOT, "build", "caption"), p, text, "74", "950"], check=True, capture_output=True)
    return Image.open(p).convert("RGBA")


def main():
    stills = "--stills" in sys.argv
    cl = clips()
    imgs, caps = {}, {}
    for c in cl:
        if c["img"] not in imgs:
            imgs[c["img"]] = Image.open(os.path.join(ROOT, "images", c["img"] + ".png")).convert("RGB")
        if c["cap"]:
            caps[c["n"]] = caption_png(c["n"], c["cap"])

    def render(t):
        c = next((c for c in cl if c["t0"] <= t < c["t1"]), cl[-1])
        u = (t - c["t0"]) / (c["t1"] - c["t0"])
        f = frame(imgs[c["img"]], *view(c["mot"], min(max(u, 0), 1))).convert("RGBA")
        if c["cap"] and c["cs"] <= t < c["ce"]:
            a = min(1.0, (t - c["cs"]) / 0.12, (c["ce"] - t) / 0.12)
            cp = caps[c["n"]]
            if a < 1:
                cp = cp.copy(); cp.putalpha(cp.getchannel("A").point(lambda v: int(v * a)))
            f.alpha_composite(cp, (0, CAP_Y - cp.size[1] // 2))
        return f.convert("RGB")

    if stills:
        d = os.path.join(ROOT, "build", "stills"); os.makedirs(d, exist_ok=True)
        for c in cl:
            t = (c["cs"] + c["ce"]) / 2 if c["cap"] else (c["t0"] + c["t1"]) / 2
            render(t).save(os.path.join(d, f"{c['n']:02d}.jpg"), quality=85)
        print("stills in build/stills"); return

    out = os.path.join(ROOT, "fan-regulator.mp4")
    ff = subprocess.Popen([
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-i", os.path.join(ROOT, "audio", "vo.mp3"),
        "-filter_complex", "[1:a]apad,aresample=48000[a]", "-map", "0:v", "-map", "[a]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-c:a", "aac", "-b:a", "192k", "-t", f"{TOTAL:.3f}", out], stdin=subprocess.PIPE)
    nf = round(TOTAL * FPS)
    for i in range(nf):
        ff.stdin.write(render(i / FPS).tobytes())
    ff.stdin.close(); ff.wait()
    print(out, "frames", nf)


if __name__ == "__main__":
    main()
