#!/usr/bin/env python3
"""og.png 1200x630 — Checkpoint One (2x supersample).
Roseway sports-bar share art: night-asphalt ground, racing-gold Impact wordmark,
checkered flag + gold race-number-one emblem, speed lines, checker base strip.
Shop identity only — no builder markers."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
S = 2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

ASPHALT = (21, 24, 30); ASPHALT2 = (32, 36, 45); CREAM = (242, 236, 223)
GOLD = (226, 167, 51); GOLD_DK = (185, 134, 31); SOFT = (169, 161, 146)

def font(paths, size):
    bases = ["/System/Library/Fonts/", "/System/Library/Fonts/Supplemental/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size * S)
                except Exception: pass
    return ImageFont.load_default()

imp = lambda s: font(["Impact.ttf", "Arial Narrow Bold.ttf"], s)
geor = lambda s: font(["Georgia.ttf"], s)
geoi = lambda s: font(["Georgia Italic.ttf", "Georgia.ttf"], s)

img = Image.new("RGB", (W * S, H * S), ASPHALT)
d = ImageDraw.Draw(img)

def px(x, y): return (int(x * S), int(y * S))

def tracked(x, y, text, fnt, fill, sp, anchor_left=True):
    """Impact caps with letter tracking — draw char by char."""
    cx = x * S
    for ch in text:
        d.text((cx, y * S), ch, font=fnt, fill=fill)
        bb = d.textbbox((0, 0), ch, font=fnt)
        cx += (bb[2] - bb[0]) + sp * S

def tracked_w(text, fnt, sp):
    wsum = 0
    for ch in text:
        bb = d.textbbox((0, 0), ch, font=fnt)
        wsum += (bb[2] - bb[0]) + sp * S
    return wsum

# --- speed lines (left, behind text) ---
for (x0, y0, ln, op) in [(72, 355, 130, 140), (110, 372, 96, 110), (150, 389, 64, 80)]:
    ov = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.rounded_rectangle([px(x0, y0), px(x0 + ln, y0 + 7)], radius=4 * S, fill=GOLD + (op,))
    img.paste(ov, (0, 0), ov)

# --- text block ---
kicker = "ROSEWAY  ·  PORTLAND, OREGON"
tracked(72, 108, kicker, imp(24), GOLD, 2.5)

word = "CHECKPOINT ONE"
size = 118
f = imp(size)
while tracked_w(word, f, 4) > 640 * S and size > 70:
    size -= 4
    f = imp(size)
tracked(72, 148, word, f, CREAM, 4)

tracked(72, 148 + size * 1.02 + 26, "YOUR NEIGHBORHOOD FINISH LINE", imp(34), GOLD, 3)

sub = geoi(26)
d.text(px(72, 148 + size * 1.02 + 86), "A dozen screens and hot, crispy Louisiana fried seafood", font=sub, fill=CREAM)
d.text(px(72, 148 + size * 1.02 + 122), "on Sandy Boulevard — soft-opened November 7, 2026.", font=sub, fill=SOFT)

# --- emblem: checkered flag + pole + gold roundel '1' ---
fx0, fy0 = 810, 120          # flag grid start
rows, cols, sq = 4, 4, 58    # 58px squares
skew = 16                    # per-row x offset for a flying-flag feel
# pole
ov = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
od.rounded_rectangle([px(fx0 - 22, fy0 - 16), px(fx0 - 10, fy0 + rows * sq + 66)], radius=6 * S, fill=CREAM + (255,))
img.paste(ov, (0, 0), ov)
for i in range(rows):
    for j in range(cols):
        col = CREAM if (i + j) % 2 == 0 else GOLD
        x0 = fx0 + i * skew + j * sq
        d.rectangle([px(x0, fy0 + i * sq), px(x0 + sq, fy0 + (i + 1) * sq)], fill=col)
# roundel with race number 1
ccx, ccy, r = fx0 + 26, fy0 + rows * sq + 34, 52
d.ellipse([px(ccx - r, ccy - r), px(ccx + r, ccy + r)], fill=GOLD, outline=CREAM, width=7 * S)
f1 = imp(64)
bb = d.textbbox((0, 0), "1", font=f1)
d.text((ccx * S - (bb[2] - bb[0]) / 2 - bb[0], ccy * S - (bb[3] - bb[1]) / 2 - bb[1]), "1", font=f1, fill=ASPHALT)

# --- checker base strip ---
strip_h, cell = 26, 13
for k in range(0, W // cell):
    col = GOLD if k % 2 == 0 else ASPHALT2
    d.rectangle([px(k * cell, H - strip_h), px((k + 1) * cell, H)], fill=col)

img = img.resize((W, H), getattr(Image, "Resampling", Image).LANCZOS)
img.save(OUT, "PNG", optimize=True)
print("og.png", img.size, os.path.getsize(OUT), "bytes")
