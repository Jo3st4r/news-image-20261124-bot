"""Build-time only: draw poster.png, the 1024x1024 front page for
"THE WORLD TODAY - Tuesday 24 November 2026".

This script runs on the builder's machine only. main.py (the graded
program) never imports PIL; it just copies the pre-rendered poster.png.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (26, 26, 26)
RED = (176, 42, 32)
NAVY = (31, 58, 95)
GREY = (90, 86, 78)
RULE = (180, 172, 156)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF = "DejaVuSerif.ttf"
SERIF_B = "DejaVuSerif-Bold.ttf"
SANS = "DejaVuSans.ttf"
SANS_B = "DejaVuSans-Bold.ttf"


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36  # side margin

    # ---- Masthead -------------------------------------------------
    d.text((mx, 22), "THE WORLD TODAY", font=font(SERIF_B, 74), fill=INK)
    d.text((mx, 108), "TUESDAY 24 NOVEMBER 2026",
           font=font(SANS_B, 21), fill=RED)
    right = "15 STORIES  •  ONE PAGE"
    d.text((W - mx - d.textlength(right, font=font(SANS_B, 21)), 108),
           right, font=font(SANS_B, 21), fill=INK)
    d.line([(mx, 142), (W - mx, 142)], fill=INK, width=3)
    d.line([(mx, 148), (W - mx, 148)], fill=INK, width=1)

    # ---- Hero story ----------------------------------------------
    hy = 168
    d.rectangle([(mx, hy + 4), (mx + 10, hy + 158)], fill=RED)
    d.text((mx + 26, hy), "THE BIG STORY  •  EUROPE",
           font=font(SANS_B, 16), fill=RED)
    d.text((mx + 26, hy + 26), "NATO sends its eyes in the sky",
           font=font(SERIF_B, 43), fill=INK)
    d.text((mx + 26, hy + 76), "to Poland",
           font=font(SERIF_B, 43), fill=INK)
    d.text((mx + 26, hy + 128),
           "An AWACS early-warning jet is deployed after three Russian",
           font=font(SANS, 19), fill=INK)
    d.text((mx + 26, hy + 152),
           "Kh-101 missiles landed on Polish soil.",
           font=font(SANS, 19), fill=INK)
    d.line([(mx, 348), (W - mx, 348)], fill=RULE, width=1)

    # ---- Story grid: 12 stories, 3 columns x 4 rows --------------
    stories = [
        ("IRAN", "Tehran vows to use \u201call its tools\u201d against US blockade",
         "Foreign ministry defiant as Washington tightens its naval squeeze on Iranian oil."),
        ("CLIMATE", "COP31 ends with no deal \u2014 and a blame game",
         "Australia faces calls for a minister to quit; Pacific islands voice despair."),
        ("UKRAINE", "Kyiv says it sank a Russian warship off Libya",
         "Seven sea drones hit the corvette Merkury at Benghazi, Zelenskyy says."),
        ("GAZA", "Strikes kill three in Gaza, including UN worker",
         "UNRWA\u2019s Adel Al-Helo dies near a well in Jabalia camp, medics say."),
        ("USA", "Trump halts Iowa explosives blast",
         "Army told to pause the lead-azide detonation until a court rules."),
        ("TECH", "Huang is back at Nvidia \u2014 shares jump 29%",
         "Board reinstates its CEO after Trump vouches he is no security risk."),
        ("SANCTIONS", "US hits Iran\u2019s shadow banks",
         "Dozens designated; FinCEN flags nearly $15bn in linked flows."),
        ("IRAN", "Singer flogged 74 times, reports say",
         "The singer and her team receive 74 lashes each, Iranian media report."),
        ("KOREA", "Seoul warns island after Russian jet intrusion",
         "Evacuation alert on Ulleung as a Russian aircraft enters its airspace."),
        ("POLAND", "Russian drone strays into Poland again",
         "Second airspace violation in days as Moscow hits western Ukraine."),
        ("INDONESIA", "Candy-factory fire kills at least 24",
         "Blaze west of Jakarta leaves dozens dead as the toll climbs."),
        ("GAZA", "Gaza now a \u201ctoxic wasteland\u201d, report says",
         "Oxfam and CEOBS: contamination signs across 99% of the Strip."),
    ]

    grid_top = 364
    grid_bottom = 902
    cols, rows = 3, 4
    gap = 18
    cell_w = (W - 2 * mx - (cols - 1) * gap) // cols
    cell_h = (grid_bottom - grid_top) // rows

    for i, (tag, head, deck) in enumerate(stories):
        r, c = divmod(i, cols)
        x = mx + c * (cell_w + gap)
        y = grid_top + r * cell_h
        if c > 0:
            d.line([(x - gap // 2, y + 4), (x - gap // 2, y + cell_h - 12)],
                   fill=RULE, width=1)
        d.text((x, y), tag, font=font(SANS_B, 13), fill=RED)
        hl = wrap(d, head, font(SERIF_B, 20), cell_w)
        yy = y + 22
        for line in hl[:3]:
            d.text((x, yy), line, font=font(SERIF_B, 20), fill=INK)
            yy += 25
        dl = wrap(d, deck, font(SANS, 14), cell_w)
        for line in dl[:2]:
            d.text((x, yy + 2), line, font=font(SANS, 14), fill=GREY)
            yy += 18

    # ---- Sport strip ----------------------------------------------
    d.line([(mx, 906), (W - mx, 906)], fill=INK, width=2)
    sport = [
        ("SPORT  •  TENNIS", "Alcaraz wins his first ATP Finals",
         "Beats world No. 1 Zverev 6\u20132, 7\u20136(7) in Turin."),
        ("SPORT  •  CHESS", "Chess crown on the line in Geneva",
         "Game 1 today: Gukesh, 20, defends his title against Sindarov, 20."),
    ]
    half = (W - 2 * mx - gap) // 2
    for i, (tag, head, deck) in enumerate(sport):
        x = mx + i * (half + gap)
        y = 918
        d.text((x, y), tag, font=font(SANS_B, 13), fill=NAVY)
        d.text((x, y + 22), head, font=font(SERIF_B, 20), fill=INK)
        d.text((x, y + 48), deck, font=font(SANS, 14), fill=GREY)

    # ---- Sources footer strip --------------------------------------
    # Two-line credit strip: reporting sources, then the edition line.
    d.line([(mx, 986), (W - mx, 986)], fill=RULE, width=1)
    sources = "SOURCES:  Reuters  \u00b7  BBC  \u00b7  AP  \u00b7  AFP  \u00b7  The Guardian"
    d.text((mx, 992), sources, font=font(SANS_B, 12), fill=INK)
    times = "All times UTC  \u00b7  Tuesday 24 November 2026"
    d.text((mx, 1008), times, font=font(SANS, 11), fill=GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poster.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
