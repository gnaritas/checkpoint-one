#!/usr/bin/env python3
"""Generate the Checkpoint One site (template v2 T1, 2026-11-16).
Roseway sports-bar identity: night-asphalt ground, checkered-flag motif, racing-gold
accents, Impact display caps over Georgia body. Zero third-party JS, one local stylesheet.
Copy ONLY from verified card facts + field re-verify 2026-11-16:
- Bridgetown Bites 2026-11-10 (soft-open date, menu, owners, address 7325, building 1926/2023 remodel, tagline)
- Hoodline recap 2026-11-11 (corroborates address/menu/tagline; prior tenant Blue Fin closed)
- shop's own FB page profile.php?id=61595513881400 (address claim, $$ range, 'golden fish and chips' intro, email)
No published phone, no verified hours, no owner names on client pages, no GBP claims."""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(ROOT, "public")
os.makedirs(PUB, exist_ok=True)
ORIGIN = "https://checkpoint-one-demo.up.railway.app"
NAME = "Checkpoint One"
STREET = "7325 NE Sandy Blvd"
CITYZIP = "Portland, OR 97213"
NAP = f"{STREET}, {CITYZIP}"
EMAIL = "check@checkpoint-one.org"
LAT, LON = 45.54903, -122.58754
FB = "https://www.facebook.com/profile.php?id=61595513881400"
Q = STREET.replace(" ", "%20") + "%2C%20" + CITYZIP.replace(" ", "%20").replace(",", "%2C")
DIR = f"https://www.google.com/maps/dir/?api=1&destination={Q}"
MAPSRC = f"https://www.google.com/maps?q={Q}&amp;output=embed"
MAPQ = f"https://www.google.com/maps?q={Q}&output=embed"
OG = ORIGIN + "/og.png"
esc = lambda s: html.escape(s, quote=True)

def flag(sz, fill_a="#F2ECDF", fill_b="#E2A733", pole="#F2ECDF"):
    """Mini checkered flag on a pole, 2x2-ish grid — the identity motif."""
    c = 4  # squares across
    r = 3
    sq = 24.0 / c
    rects = []
    for i in range(r):
        for j in range(c):
            f = fill_a if (i + j) % 2 == 0 else fill_b
            rects.append(f'<rect x="{j*sq:.1f}" y="{i*sq:.1f}" width="{sq:.1f}" height="{sq:.1f}" fill="{f}"/>')
    return (f'<svg class="flag" width="{sz}" height="{sz}" viewBox="0 0 32 32" aria-hidden="true">'
            f'<rect x="1.6" y="1.5" width="2.6" height="29" rx="1.3" fill="{pole}"/>'
            f'<g transform="translate(4.2 1.5)">{"".join(rects)}</g></svg>')

FLAG16 = flag(16)
FLAG13 = flag(13, pole="#E2A733", fill_b="#15181E")

BRAND = ('<a class="brand" href="/">'
         '<svg viewBox="0 0 34 34" aria-hidden="true">'
         '<rect x="1.8" y="2" width="3" height="30" rx="1.5" fill="#F2ECDF"/>'
         '<g transform="translate(4.8 2)">'
         '<rect x="0" y="0" width="9" height="9" fill="#F2ECDF"/><rect x="9" y="0" width="9" height="9" fill="#E2A733"/><rect x="18" y="0" width="9" height="9" fill="#F2ECDF"/><rect x="27" y="0" width="4.4" height="9" fill="#E2A733"/>'
         '<rect x="0" y="9" width="9" height="9" fill="#E2A733"/><rect x="9" y="9" width="9" height="9" fill="#F2ECDF"/><rect x="18" y="9" width="9" height="9" fill="#E2A733"/><rect x="27" y="9" width="4.4" height="9" fill="#F2ECDF"/>'
         '<rect x="0" y="18" width="9" height="9" fill="#F2ECDF"/><rect x="9" y="18" width="9" height="9" fill="#E2A733"/><rect x="18" y="18" width="9" height="9" fill="#F2ECDF"/><rect x="27" y="18" width="4.4" height="9" fill="#E2A733"/>'
         '</g></svg>Checkpoint One</a>')

NAV = ('<nav aria-label="Main">'
       '<a href="/kitchen">The Kitchen</a>'
       '<a href="/game-days">Game Days</a>'
       '<a href="/eats-and-drinks">Eats &amp; Drinks</a>'
       '<a href="/contact">Contact</a>'
       '</nav>')

FOOTER = f"""<footer>
  <div class="checkerline" aria-hidden="true"></div>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <h4>Checkpoint One</h4>
        <address class="nap">Sports bar &amp; Louisiana fried seafood<br>
        {STREET}<br>{CITYZIP}<br>
        <a href="mailto:{EMAIL}">{EMAIL}</a></address>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/kitchen">The Kitchen</a></li>
          <li><a href="/game-days">Game Days</a></li>
          <li><a href="/eats-and-drinks">Eats &amp; Drinks</a></li>
          <li><a href="/contact">Contact &amp; Directions</a></li>
          <li><a href="/privacy">Privacy</a></li>
        </ul>
      </div>
      <div>
        <h4>Find Us</h4>
        <ul>
          <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
          <li><a href="{DIR}" target="_blank" rel="noopener">Get directions</a></li>
          <li><a href="/eats-and-drinks">See the spread</a></li>
        </ul>
      </div>
    </div>
    <div class="footline"><span>© 2026 {NAME} · {NAP} · {EMAIL}</span><span>{FLAG13} Your neighborhood finish line</span></div>
  </div>
</footer>"""

def head(title, desc, path, noindex=False, utility=False):
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    canonical = f'{ORIGIN}{path}'
    meta = ""
    if not utility:
        meta = (f'\n  <meta property="og:type" content="website">'
                f'\n  <meta property="og:site_name" content="{NAME}">'
                f'\n  <meta property="og:title" content="{esc(title)}">'
                f'\n  <meta property="og:description" content="{esc(desc)}">'
                f'\n  <meta property="og:image" content="{OG}">'
                f'\n  <meta property="og:url" content="{esc(canonical)}">'
                f'\n  <meta name="twitter:card" content="summary_large_image">'
                f'\n  <meta name="twitter:title" content="{esc(title)}">'
                f'\n  <meta name="twitter:description" content="{esc(desc)}>')
    return f"""<!DOCTYPE html>
<!-- BUILT-2026-11-16 -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{esc(canonical)}">{robots}{meta}
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/style.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site">
    <div class="bar">
      {BRAND}
      {NAV}
    </div>
  </header>
<main id="main">
"""

def page(title, desc, path, body, ld_blocks, noindex=False, utility=False):
    ld = ""
    if ld_blocks:
        blocks = "".join(f'\n  <script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
                         for b in ld_blocks)
        ld = blocks
    html_doc = head(title, desc, path, noindex=noindex, utility=utility) + body + ld + "\n</main>\n" + FOOTER + "\n</body>\n</html>\n"
    # LD goes in <head> just before </head>? No — valid in body too; put before footer for validity
    open(os.path.join(PUB, ("index.html" if path == "/" else path[1:] + ".html")), "w", encoding="utf-8").write(html_doc)

def breadcrumb(name, path):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"}]
    if path != "/":
        items.append({"@type": "ListItem", "position": 2, "name": name, "item": ORIGIN + path})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

REST = {
    "@context": "https://schema.org",
    "@type": ["Restaurant", "BarOrPub"],
    "@id": ORIGIN + "/#restaurant",
    "name": "Checkpoint One",
    "url": ORIGIN + "/",
    "image": OG,
    "description": "Roseway sports bar with a dozen screens and hot, crispy Louisiana-style fried seafood on Sandy Boulevard. Soft-opened November 7, 2026.",
    "servesCuisine": ["Louisiana-style", "Southern", "American"],
    "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": "Portland",
                "addressRegion": "OR", "postalCode": "97213", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
    "sameAs": [FB],
    "hasMenu": {"@id": ORIGIN + "/eats-and-drinks#menu"},
}

def webpage(name, path, title):
    return {"@context": "https://schema.org", "@type": "WebPage", "@id": f"{ORIGIN}{path}#webpage",
            "url": ORIGIN + path, "name": title, "inLanguage": "en-US",
            "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@id": ORIGIN + "/#restaurant"}}

WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": ORIGIN + "/#website",
           "url": ORIGIN + "/", "name": "Checkpoint One", "inLanguage": "en-US",
           "publisher": {"@id": ORIGIN + "/#restaurant"}}

def faq(qs, path):
    return {"@context": "https://schema.org", "@type": "FAQPage", "@id": f"{ORIGIN}{path}#faq",
            "isPartOf": {"@id": f"{ORIGIN}{path}#webpage"},
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}

def band(kicker, h1, lede, crumbs):
    return (f'  <div class="band">\n    <div class="wrap">\n'
            f'      <div class="crumbs">{crumbs}</div>\n'
            f'      <div class="kicker">{FLAG16} {kicker}</div>\n'
            f'      <h1>{h1}</h1>\n      <p class="lede">{lede}</p>\n'
            f'    </div>\n  </div>\n')

def faq_html(qs):
    rows = "".join(f'      <details><summary>{esc(q)}</summary><div class="a">{esc(a)}</div></details>\n'
                   for q, a in qs)
    return ('  <section class="sec paper">\n    <div class="wrap">\n'
            f'      <div class="kicker">{FLAG16} Know before you go</div>\n'
            '      <h2>Frequent questions</h2>\n'
            f'      <div class="faq">\n{rows}      </div>\n    </div>\n  </section>\n')

def cta_band(h2, lede, primary):
    return (f'  <section class="cta">\n    <div class="wrap cwrap">\n'
            f'      <div>\n        <h2>{esc(h2)}</h2>\n        <p>{esc(lede)}</p>\n      </div>\n'
            f'      <div class="acts">\n        <a class="btn invert" href="{primary[1]}">{esc(primary[0])}</a>\n'
            f'      </div>\n    </div>\n  </section>\n')

# ---------------------------------------------------------------- HOME
HOME_META = ("Checkpoint One is a new Roseway sports bar at 7325 NE Sandy Blvd, Portland OR — "
             "a dozen screens and hot, crispy Louisiana-style fried seafood: catfish, shrimp, "
             "oysters, wings, gumbo, cocktails and rotating taps. Soft-opened November 7, 2026.")
TITLE_HOME = "Checkpoint One — Sports Bar & Louisiana Fried Seafood, Portland OR"

hero = (f'  <div class="hero">\n    <div class="wrap cols">\n      <div>\n'
        f'        <div class="kicker">{FLAG16} Roseway · Portland, OR · soft-opened Nov 7, 2026</div>\n'
        '        <h1>Your neighborhood<br>finish line.</h1>\n'
        '        <p class="lede">A dozen screens and hot, crispy Louisiana fried seafood on Sandy '
        'Boulevard. Catfish, shrimp, oysters and wings off the fryer, gumbo on the stove, '
        'and a seat saved for the game.</p>\n'
        '        <div class="acts">\n'
        '          <a class="btn" href="/eats-and-drinks">See the spread</a>\n'
        f'          <a class="btn ghost" href="{DIR}" target="_blank" rel="noopener">Get directions</a>\n'
        '        </div>\n      </div>\n      <div class="heroart">\n'
        '        <svg viewBox="0 0 360 320" role="img" aria-label="Checkpoint One emblem: a checkered flag flying beside a gold race number one">\n'
        '          <g opacity=".55"><rect x="6" y="70" width="72" height="5" rx="2.5" fill="#E2A733"/><rect x="22" y="86" width="54" height="5" rx="2.5" fill="#E2A733" opacity=".75"/><rect x="40" y="102" width="36" height="5" rx="2.5" fill="#E2A733" opacity=".5"/></g>\n'
        '          <rect x="98" y="52" width="7" height="216" rx="3.5" fill="#F2ECDF"/>\n'
        '          <g>\n'
        + "".join(f'            <rect x="{104+12*i+40*j}" y="{58+40*i}" width="40" height="40" fill="{"#F2ECDF" if (i+j)%2==0 else "#E2A733"}"/>\n'
                  for i in range(4) for j in range(5)) +
        '          </g>\n'
        '          <circle cx="86" cy="238" r="37" fill="#E2A733"/>\n'
        '          <circle cx="86" cy="238" r="37" fill="none" stroke="#F2ECDF" stroke-width="5"/>\n'
        '          <text x="86" y="255" text-anchor="middle" font-family="Impact, \'Arial Narrow Bold\', sans-serif" font-size="52" fill="#15181E">1</text>\n'
        '        </svg>\n      </div>\n    </div>\n  </div>\n')

stats = ('  <section class="sec paper">\n    <div class="wrap">\n'
         f'      <div class="kicker">{FLAG16} Why come by</div>\n'
         '      <h2>Flags up, fryer on.</h2>\n'
         '      <div class="cards">\n'
         '        <div class="card"><h3>A dozen screens</h3><p>Twelve of them, placed all through the room, with seating set up to catch the game from where you land.</p></div>\n'
         '        <div class="card"><h3>Hot and crispy</h3><p>Catfish, shrimp, oysters and wings fried the Louisiana way — plus gumbo, the &ldquo;large chicken&rdquo; and golden fish and chips.</p></div>\n'
         '        <div class="card"><h3>Ice-cold, poured</h3><p>Cocktails, beer on rotating taps, wine and soda. The full bar, run the neighborhood way.</p></div>\n'
         '      </div>\n    </div>\n  </section>\n')

board_items = ["Fried Catfish", "Fried Shrimp", "Fried Oysters", "Fried Wings",
               "Gumbo", "The &ldquo;Large Chicken&rdquo;", "Golden Fish &amp; Chips", "Slaws &amp; Potato Salad"]
board = ('  <section class="sec dark">\n    <div class="wrap">\n'
         f'      <div class="kicker">{FLAG16} On the board</div>\n'
         '      <h2>What fried us in</h2>\n'
         '      <p class="lede">The menu we soft-opened with on November 7 — ask your server what&rsquo;s coming off the fryer next.</p>\n'
         '      <ul class="board">\n'
         + "".join(f'        <li>{FLAG16} {it}</li>\n' for it in board_items) +
         '      </ul>\n'
         '      <p class="note" style="margin-top:22px">Prices and the day&rsquo;s specials live on the in-house board — just ask. This page keeps pace with the menu as it settles in.</p>\n'
         '    </div>\n  </section>\n')

quote = ('  <section class="sec paper">\n    <div class="wrap narrow">\n'
         '      <blockquote>&ldquo;We&rsquo;re bringing hot, crispy fried seafood and Louisiana flavor to Sandy Boulevard!&rdquo;</blockquote>\n'
         f'      <div class="attrib">{FLAG16} The team at Checkpoint One</div>\n'
         '    </div>\n  </section>\n')

teasers = ('  <section class="sec dark">\n    <div class="wrap">\n'
           f'      <div class="kicker">{FLAG16} Two ways to spend an evening</div>\n'
           '      <h2>Pick your lane.</h2>\n'
           '      <div class="cards">\n'
           '        <div class="card"><h3>Game days</h3><p>The room was laid out around a dozen screens — come find the matchup, the crowd and a cold one.</p>'
           '<a class="more" href="/game-days">Game days &rarr;</a></div>\n'
           '        <div class="card"><h3>The kitchen</h3><p>Fried catfish, shrimp, oysters and wings, gumbo, the &ldquo;large chicken&rdquo; and golden fish and chips — all of it hot and crispy.</p>'
           '<a class="more" href="/kitchen">Inside the kitchen &rarr;</a></div>\n'
           '      </div>\n    </div>\n  </section>\n')

HOME_FAQ = [
    ("Where exactly is Checkpoint One?",
     "7325 NE Sandy Blvd in Roseway — Sandy Boulevard near 73rd Avenue, in the 1926 storefront, freshly remodeled in 2023."),
    ("When did you open?",
     "We soft-opened on Friday, November 7, 2026. For the week's schedule, check our Facebook page or send us a note."),
    ("What kind of food do you serve?",
     "Hot, crispy Louisiana-style fried seafood — catfish, shrimp, oysters and wings — plus gumbo, the \u201clarge chicken\u201d and golden fish and chips, with coleslaw or potato salad on the side."),
    ("What can I get to drink?",
     "Cocktails, beer on rotating taps, wine and soda."),
]

mapband = (f'  <section class="sec dark">\n    <div class="wrap">\n'
           f'      <div class="kicker">{FLAG16} On the map</div>\n'
           f'      <h2>{esc(STREET)}</h2>\n'
           '      <p class="lede">Look for the 1926 storefront on Sandy near 73rd Avenue — remodeled in 2023 and easy to spot.</p>\n'
           f'      <div class="acts" style="margin-top:24px">\n        <a class="btn" href="{DIR}" target="_blank" rel="noopener">Get directions</a>\n        <a class="btn ghost" href="{FB}" target="_blank" rel="noopener">Facebook</a>\n      </div>\n'
           f'      <div class="mapcard" style="margin-top:26px">\n        <iframe src="{MAPSRC}" title="Map showing Checkpoint One at {esc(STREET)}, {esc(CITYZIP)}" loading="lazy"></iframe>\n      </div>\n'
           '    </div>\n  </section>\n')

home_body = (hero + stats + board + quote + teasers + faq_html(HOME_FAQ) + mapband +
             (f'  <section class="cta">\n    <div class="wrap cwrap">\n'
              f'      <div>\n        <h2>Game on. The fryer is lit.</h2>\n'
              f'        <p>Pick a seat before the matchup — directions, email and one short form are all one page away.</p>\n      </div>\n'
              f'      <div class="acts">\n        <a class="btn invert" href="/contact">Contact &amp; directions</a>\n      </div>\n'
              f'    </div>\n  </section>\n'))

home_ld = [REST, WEBSITE, webpage("Home", "/", TITLE_HOME), breadcrumb("Home", "/"), faq(HOME_FAQ, "/")]
page(TITLE_HOME, HOME_META, "/", home_body, home_ld)

# ---------------------------------------------------------------- EATS & DRINKS (hub)
TITLE_EATS = "Fried Seafood, Gumbo & Drinks — Checkpoint One, Portland OR"
EATS_META = ("The Checkpoint One spread: hot, crispy Louisiana fried seafood — catfish, shrimp, "
             "oysters, wings — plus gumbo, the \u201clarge chicken,\u201d golden fish and chips, sides, "
             "cocktails, rotating taps, wine and soda, on Sandy Boulevard in Portland OR.")

eats_body = (band("Eats & Drinks", "The full spread,<br>start to finish.",
                  "Everything starts at the fryer. Here&rsquo;s what the kitchen and the bar were serving the night we soft-opened — more rolls in as the menu settles.",
                  '<a href="/">Home</a> · Eats &amp; Drinks')
             + '  <section class="sec paper">\n    <div class="wrap">\n      <div class="cards">\n'
             '        <div class="card"><h3>The fryer</h3><ul><li>Fried catfish</li><li>Fried shrimp</li><li>Fried oysters</li><li>Fried wings</li></ul><a class="more" href="/kitchen">Inside the kitchen &rarr;</a></div>\n'
             '        <div class="card"><h3>Gumbo &amp; plates</h3><ul><li>Gumbo, Louisiana-style</li><li>The &ldquo;large chicken&rdquo;</li><li>Golden fish &amp; chips</li></ul><a class="more" href="/kitchen">More from the kitchen &rarr;</a></div>\n'
             '        <div class="card"><h3>Sides</h3><ul><li>Coleslaw</li><li>Potato salad</li></ul><p style="margin-top:10px">The proper company for anything crispy.</p></div>\n'
             '        <div class="card"><h3>The bar</h3><ul><li>Cocktails</li><li>Beer on rotating taps</li><li>Wine</li><li>Soda</li></ul><a class="more" href="/game-days">Game days &rarr;</a></div>\n'
             '      </div>\n'
             '      <p class="note" style="margin-top:24px">Prices and the day&rsquo;s specials live on the in-house board — just ask your server.</p>\n'
             '    </div>\n  </section>\n'
             + mapband)

MENU = {
    "@context": "https://schema.org", "@type": "Menu", "@id": ORIGIN + "/eats-and-drinks#menu",
    "name": "Checkpoint One Menu", "inLanguage": "en-US",
    "hasMenuSection": [
        {"@type": "MenuSection", "name": "The Fryer", "item": [
            {"@type": "MenuItem", "name": "Fried Catfish", "description": "Fried hot and crispy, Louisiana-style."},
            {"@type": "MenuItem", "name": "Fried Shrimp", "description": "Fried hot and crispy, Louisiana-style."},
            {"@type": "MenuItem", "name": "Fried Oysters", "description": "Fried hot and crispy, Louisiana-style."},
            {"@type": "MenuItem", "name": "Fried Wings", "description": "Fried hot and crispy, Louisiana-style."}]},
        {"@type": "MenuSection", "name": "Gumbo & Plates", "item": [
            {"@type": "MenuItem", "name": "Gumbo", "description": "Louisiana-style, on the menu from the soft opening."},
            {"@type": "MenuItem", "name": "The \u201cLarge Chicken\u201d", "description": "The big-bird headline on the menu."},
            {"@type": "MenuItem", "name": "Golden Fish and Chips", "description": "Golden, per the shop's introduction."}]},
        {"@type": "MenuSection", "name": "Sides", "item": [
            {"@type": "MenuItem", "name": "Coleslaw", "description": "On the side."},
            {"@type": "MenuItem", "name": "Potato Salad", "description": "On the side."}]},
        {"@type": "MenuSection", "name": "The Bar", "item": [
            {"@type": "MenuItem", "name": "Cocktails"},
            {"@type": "MenuItem", "name": "Beer on Rotating Taps", "description": "A rotating selection."},
            {"@type": "MenuItem", "name": "Wine"},
            {"@type": "MenuItem", "name": "Soda"}]},
    ],
}
eats_ld = [{"@context": "https://schema.org", "@type": "Restaurant", "@id": ORIGIN + "/#restaurant"},
           {"@context": "https://schema.org", **MENU},
           webpage("Eats & Drinks", "/eats-and-drinks", TITLE_EATS), breadcrumb("Eats & Drinks", "/eats-and-drinks")]
page(TITLE_EATS, EATS_META, "/eats-and-drinks", eats_body, eats_ld)

# ---------------------------------------------------------------- KITCHEN
TITLE_KITCHEN = "Louisiana Fried Seafood & Gumbo — Checkpoint One, Portland OR"
KITCHEN_META = ("Fried catfish, shrimp, oysters and wings, gumbo, the \u201clarge chicken\u201d and golden "
                "fish and chips — the fryer-first Louisiana kitchen at Checkpoint One, a sports bar on "
                "Sandy Boulevard, Portland OR.")

KITCHEN_FAQ = [
    ("What comes out of the fryer?",
     "Catfish, shrimp, oysters and wings — fried hot and crispy, Louisiana-style."),
    ("Do you have fried chicken?",
     "Yes — the menu lists it as the \u201clarge chicken.\u201d"),
    ("What sides come with the food?",
     "Coleslaw or potato salad, on the side."),
]

kitchen_body = (band("The Kitchen", "Out of the fryer,<br>the Louisiana way.",
                     "In the team&rsquo;s own words: &ldquo;hot, crispy fried seafood and Louisiana flavor&rdquo; — brought to Sandy Boulevard.",
                     '<a href="/">Home</a> · The Kitchen')
                + '  <section class="sec paper">\n    <div class="wrap">\n      <div class="kicker">' + FLAG16 + ' From the fryer</div>\n      <h2>The four that started it</h2>\n      <div class="cards">\n'
                '        <div class="card"><h3>Fried catfish</h3><p>The counter classic — fried hot and crispy, Louisiana-style.</p></div>\n'
                '        <div class="card"><h3>Fried shrimp</h3><p>Hot, crispy and straight off the fryer.</p></div>\n'
                '        <div class="card"><h3>Fried oysters</h3><p>The Gulf-coast habit, done Sandy Boulevard style.</p></div>\n'
                '        <div class="card"><h3>Fried wings</h3><p>On the menu from the first night — order them and see.</p></div>\n'
                '      </div>\n    </div>\n  </section>\n'
                + '  <section class="sec dark">\n    <div class="wrap">\n      <div class="kicker">' + FLAG16 + ' The pot &amp; the bird</div>\n      <h2>Not just the fryer</h2>\n      <div class="cards">\n'
                '        <div class="card"><h3>Gumbo</h3><p>Louisiana-style, on the menu since the soft opening.</p></div>\n'
                '        <div class="card"><h3>The &ldquo;large chicken&rdquo;</h3><p>The big-bird headline of the menu — listed exactly that big.</p></div>\n'
                '        <div class="card"><h3>Golden fish &amp; chips</h3><p>Golden, per the shop&rsquo;s own introduction — the comfort order.</p></div>\n'
                '      </div>\n      <p class="note" style="margin-top:22px">Coleslaw or potato salad, on the side. Prices live on the in-house board — just ask.</p>\n'
                '    </div>\n  </section>\n'
                + faq_html(KITCHEN_FAQ)
                + '  <section class="cta">\n    <div class="wrap cwrap">\n      <div>\n        <h2>Come hungry. Leave crispy.</h2>\n'
                '        <p>The kitchen is on Sandy Boulevard, two blocks of Roseway from everywhere else you already go.</p>\n      </div>\n'
                f'      <div class="acts">\n        <a class="btn invert" href="{DIR}" target="_blank" rel="noopener">Get directions</a>\n      </div>\n    </div>\n  </section>\n')

kitchen_ld = [{"@context": "https://schema.org", "@type": "Restaurant", "@id": ORIGIN + "/#restaurant"},
              {"@context": "https://schema.org", "@type": "Service", "@id": ORIGIN + "/kitchen#service",
               "serviceType": "Fried Seafood & Southern Plates", "name": "The Kitchen at Checkpoint One",
               "provider": {"@id": ORIGIN + "/#restaurant"},
               "areaServed": {"@type": "City", "name": "Portland"}},
              webpage("The Kitchen", "/kitchen", TITLE_KITCHEN), breadcrumb("The Kitchen", "/kitchen"),
              faq(KITCHEN_FAQ, "/kitchen")]
page(TITLE_KITCHEN, KITCHEN_META, "/kitchen", kitchen_body, kitchen_ld)

# ---------------------------------------------------------------- GAME DAYS
TITLE_GAME = "Game Days & A Dozen Screens — Checkpoint One, Portland OR"
GAME_META = ("A dozen screens and seating set up around them — game days at Checkpoint One, the new "
             "Roseway sports bar at 7325 NE Sandy Blvd, Portland OR, with Louisiana fried seafood and "
             "rotating taps.")

GAME_FAQ = [
    ("How many screens do you have?",
     "A dozen, placed all through the room with seating set up around them."),
    ("Is there room for a group?",
     "Yes — the room was built with plenty of places to sit and enjoy the game."),
    ("Do I need to be into racing to come in?",
     "No. The checkered flag is our logo and \u201cyour neighborhood finish line\u201d is our tagline — what's on your plate is pure Louisiana."),
]

game_body = (band("Game Days", "Twelve screens.<br>Plenty of seats.",
                  "The room was laid out around the screens, so the game is on no matter where you land — gumbo optional, strongly encouraged.",
                  '<a href="/">Home</a> · Game Days')
             + '  <section class="sec dark">\n    <div class="wrap cols">\n      <div>\n      <div class="kicker">' + FLAG16 + ' Built around the matchup</div>\n'
               '      <h2>Wherever you sit,<br>it&rsquo;s a good seat.</h2>\n'
               '      <p class="lede">Screens run all through the space and the seating is arranged to match — the room fills the way neighborhoods do: regulars, first-timers and somebody&rsquo;s fantasy team arguing about a lineup.</p>\n'
               '      <div class="acts">\n        <a class="btn" href="/eats-and-drinks">See what to order</a>\n        <a class="btn ghost" href="/contact">Plan a visit</a>\n      </div>\n      </div>\n'
               '      <div class="heroart">\n        <svg viewBox="0 0 360 300" role="img" aria-label="Illustration of a big screen with a checkered flag beside it">\n'
               '          <rect x="40" y="34" width="280" height="160" rx="12" fill="#20242D" stroke="#F2ECDF" stroke-width="6"/>\n'
               '          <g>' + "".join(f'<rect x="{58+34*j:.0f}" y="{52+34*i:.0f}" width="34" height="34" fill="{"#F2ECDF" if (i+j)%2==0 else "#E2A733"}" opacity=".85"/>' for i in range(4) for j in range(8)) + '</g>\n'
               '          <rect x="150" y="194" width="60" height="42" fill="#F2ECDF"/><rect x="120" y="236" width="120" height="12" rx="6" fill="#F2ECDF"/>\n'
               '          <rect x="22" y="252" width="316" height="8" rx="4" fill="#E2A733" opacity=".6"/>\n'
               '        </svg>\n      </div>\n    </div>\n  </section>\n'
             + faq_html(GAME_FAQ)
             + '  <section class="cta">\n    <div class="wrap cwrap">\n      <div>\n        <h2>Pick a seat before kickoff.</h2>\n'
               '        <p>Directions, email and the schedule on our Facebook page — all one hop away.</p>\n      </div>\n'
               f'      <div class="acts">\n        <a class="btn invert" href="{DIR}" target="_blank" rel="noopener">Get directions</a>\n      </div>\n    </div>\n  </section>\n')

game_ld = [{"@context": "https://schema.org", "@type": "Restaurant", "@id": ORIGIN + "/#restaurant"},
           {"@context": "https://schema.org", "@type": "Service", "@id": ORIGIN + "/game-days#service",
            "serviceType": "Game Day Viewing", "name": "Game Days at Checkpoint One",
            "provider": {"@id": ORIGIN + "/#restaurant"},
            "audience": {"@type": "Audience", "name": "Sports fans and neighborhood groups"},
            "areaServed": {"@type": "City", "name": "Portland"}},
           webpage("Game Days", "/game-days", TITLE_GAME), breadcrumb("Game Days", "/game-days"),
           faq(GAME_FAQ, "/game-days")]
page(TITLE_GAME, GAME_META, "/game-days", game_body, game_ld)

# ---------------------------------------------------------------- CONTACT
TITLE_CONTACT = "Contact & Directions — Checkpoint One, Portland OR"
CONTACT_META = ("Find Checkpoint One at 7325 NE Sandy Blvd, Portland OR 97213 — directions, email and "
                "a short message form. Roseway's neighborhood finish line, in the 1926 storefront.")

contact_body = (band("Contact", "Come by,<br>or send a note.",
                     "Email is the fastest way to reach us while the menu is still finding its legs — and the door on Sandy Boulevard is exactly where the map says it is.",
                     '<a href="/">Home</a> · Contact')
                + '  <section class="sec paper">\n    <div class="wrap cols">\n      <div>\n'
                '        <div class="kicker">' + FLAG16 + ' The shop</div>\n'
                f'        <h2>{esc(STREET)}</h2>\n'
                '        <address class="bigaddr">' + esc(CITYZIP) + '<br>\n'
                f'        <a href="mailto:{EMAIL}">{EMAIL}</a><br>\n'
                f'        <a href="{FB}" target="_blank" rel="noopener">Facebook page</a><br>\n'
                f'        <a href="{DIR}" target="_blank" rel="noopener">Get directions</a></address>\n'
                '        <p class="note" style="margin-top:18px">The week&rsquo;s schedule goes up on Facebook first. For anything — menu questions, a crew coming out, a seat before kickoff — the form reaches the shop directly.</p>\n'
                '      </div>\n      <div>\n'
                '        <form class="cform" method="post" action="/contact">\n'
                '          <div>\n            <label for="f-name">Your name</label>\n            <input id="f-name" name="name" autocomplete="name" required>\n          </div>\n'
                '          <div class="row">\n            <div>\n              <label for="f-phone">Phone (optional)</label>\n              <input id="f-phone" name="phone" type="tel" autocomplete="tel">\n            </div>\n'
                '            <div>\n              <label for="f-email">Email</label>\n              <input id="f-email" name="email" type="email" autocomplete="email">\n            </div>\n          </div>\n'
                '          <div>\n            <label for="f-message">Your message</label>\n            <textarea id="f-message" name="message" required placeholder="Game-day plans, menu questions, or anything else — send it over."></textarea>\n          </div>\n'
                '          <button class="btn" type="submit">Send the shop a note</button>\n'
                '          <p class="small" style="margin:0">We answer between orders as fast as we can.</p>\n'
                '        </form>\n      </div>\n    </div>\n  </section>\n'
                + mapband)

contact_ld = [{"@context": "https://schema.org", "@type": "Restaurant", "@id": ORIGIN + "/#restaurant"},
              {"@context": "https://schema.org", "@type": "ContactPage", "@id": ORIGIN + "/contact#webpage",
               "url": ORIGIN + "/contact", "name": TITLE_CONTACT, "inLanguage": "en-US",
               "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@id": ORIGIN + "/#restaurant"}},
              breadcrumb("Contact", "/contact")]
page(TITLE_CONTACT, CONTACT_META, "/contact", contact_body, contact_ld)

# ---------------------------------------------------------------- PRIVACY
TITLE_PRIVACY = "Privacy — Checkpoint One, Portland OR"
PRIVACY_META = ("Privacy at Checkpoint One: no trackers, no cookies and no ad networks. The contact "
                "form simply sends your note to the shop's own mailbox.")

privacy_body = (band("Privacy", "No trackers.<br>No cookies.",
                     "This site collects nothing about you while you browse. Here is the whole policy, in plain English.",
                     '<a href="/">Home</a> · Privacy')
                + '  <section class="sec paper">\n    <div class="wrap prose">\n'
                '      <h2>The short version</h2>\n'
                '      <p>No analytics, no trackers, no cookies, no advertising networks. There is nothing to opt out of because there is nothing being collected.</p>\n'
                '      <h3>The contact form</h3>\n'
                '      <p>If you fill in the form, your name, phone, email and message are sent to the shop&rsquo;s own mailbox so somebody can answer you. Nothing is stored here on the site, nothing is sold, and nothing is added to any list.</p>\n'
                '      <h3>The map</h3>\n'
                '      <p>Directions and the embedded map are served by Google. When a page with the map loads, Google receives a standard request for the map tiles, subject to Google&rsquo;s own privacy terms.</p>\n'
                '      <h3>Questions</h3>\n'
                f'      <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and ask.</p>\n'
                '    </div>\n  </section>\n')

privacy_ld = [{"@context": "https://schema.org", "@type": "Restaurant", "@id": ORIGIN + "/#restaurant"},
              webpage("Privacy", "/privacy", TITLE_PRIVACY), breadcrumb("Privacy", "/privacy")]
page(TITLE_PRIVACY, PRIVACY_META, "/privacy", privacy_body, privacy_ld)

# ---------------------------------------------------------------- 404 + THANKS
notfound_body = ('  <section><div class="wrap prose">\n'
                 f'      <div class="kicker">{FLAG16} 404</div>\n'
                 '      <h1>This page missed the checkpoint.</h1>\n'
                 '      <p class="lede">Nothing was harmed. Get back to the racing: <a href="/">home</a>, <a href="/eats-and-drinks">eats &amp; drinks</a>, <a href="/game-days">game days</a> or <a href="/contact">contact &amp; directions</a>.</p>\n'
                 '    </div></section>\n')
page("Page Not Found — Checkpoint One",
     "That page isn't here — back to Checkpoint One, the sports bar with Louisiana fried seafood on Sandy Boulevard.",
     "/404", notfound_body, [], noindex=True, utility=True)

thanks_body = ('  <section><div class="wrap prose">\n'
               f'      <div class="kicker">{FLAG16} Message sent</div>\n'
               '      <h1>Your note is on its way.</h1>\n'
               '      <p class="lede">The shop answers from its own mailbox as soon as the fryer allows. Meanwhile: <a href="/">home</a>, <a href="/game-days">game days</a> or <a href="/eats-and-drinks">the spread</a>.</p>\n'
               '    </div></section>\n')
page("Message Sent — Checkpoint One, Portland OR",
     "Your note is on its way to Checkpoint One — the shop will get back to you as soon as it can.",
     "/thanks", thanks_body, [], noindex=True, utility=True)

# ---------------------------------------------------------------- static misc
open(os.path.join(PUB, "robots.txt"), "w", encoding="utf-8").write(
    f"User-agent: *\nAllow: /\nDisallow: /thanks\n\nSitemap: {ORIGIN}/sitemap.xml\n")

CORE = ["/", "/eats-and-drinks", "/kitchen", "/game-days", "/contact", "/privacy"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for pp in CORE:
    sm.append(f'  <url><loc>{ORIGIN}{pp}</loc><lastmod>2026-11-16</lastmod></url>')
sm.append("</urlset>")
open(os.path.join(PUB, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

open(os.path.join(PUB, "favicon.svg"), "w", encoding="utf-8").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
    '<rect x="1.6" y="1.5" width="2.8" height="29" rx="1.4" fill="#F2ECDF"/>'
    '<g transform="translate(4.4 1.5)">'
    '<rect width="9.2" height="9.2" fill="#F2ECDF"/><rect x="9.2" width="9.2" height="9.2" fill="#E2A733"/><rect x="18.4" width="9.2" height="9.2" fill="#F2ECDF"/><rect x="27.6" width="4.2" height="9.2" fill="#E2A733"/>'
    '<rect y="9.2" width="9.2" height="9.2" fill="#E2A733"/><rect x="9.2" y="9.2" width="9.2" height="9.2" fill="#F2ECDF"/><rect x="18.4" y="9.2" width="9.2" height="9.2" fill="#E2A733"/><rect x="27.6" y="9.2" width="4.2" height="9.2" fill="#F2ECDF"/>'
    '<rect y="18.4" width="9.2" height="9.2" fill="#F2ECDF"/><rect x="9.2" y="18.4" width="9.2" height="9.2" fill="#E2A733"/><rect x="18.4" y="18.4" width="9.2" height="9.2" fill="#F2ECDF"/><rect x="27.6" y="18.4" width="4.2" height="9.2" fill="#E2A733"/>'
    '</g></svg>\n')

# ---------------------------------------------------------------- style.css
CSS = """/* Checkpoint One — Roseway, Portland OR. Hand-rolled stylesheet, zero third-party runtime.
   Identity: night-asphalt ground, checkered-flag motif, racing gold, Impact display caps
   over Georgia body. One local stylesheet, no builder, no runtime JS. */
:root{
  --asphalt:#15181E; --asphalt-2:#20242D; --ink:#141619;
  --cream:#F2ECDF; --paper:#F4EEE1; --card:#FBF6EA;
  --soft:#6F6656; --soft-d:#A9A192;
  --gold:#E2A733; --gold-dk:#B9861F; --red:#B3382C;
  --line:rgba(20,22,25,.18); --line-l:rgba(242,236,223,.17);
  --display:'Impact','Haettenschweiler','Arial Narrow Bold',sans-serif;
  --body:Georgia,'Iowan Old Style','Times New Roman',serif;
  --r:12px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{background:var(--asphalt);color:var(--cream);font-family:var(--body);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
.skip{position:absolute;left:-9999px}
.skip:focus{left:12px;top:12px;z-index:99;background:var(--gold);color:var(--ink);padding:10px 16px;border-radius:8px;font-family:var(--display);text-transform:uppercase;letter-spacing:.1em}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
.wrap.narrow{max-width:820px}
.wrap.prose{max-width:720px}
h1,h2,h3,h4{font-family:var(--display);font-weight:400;line-height:1.06;letter-spacing:.025em;text-transform:uppercase}
h1{font-size:clamp(34px,5.4vw,56px)}
h2{font-size:clamp(24px,3.4vw,34px);margin:0 0 18px}
h3{font-size:19px;letter-spacing:.05em}
a{color:var(--gold)}
p{overflow-wrap:break-word}
main p + p, .prose p + p, .prose h3 + p{margin-top:14px}
.prose h2{margin-top:34px}
.prose h2:first-of-type{margin-top:0}
.prose h3{margin-top:26px}
.kicker{display:flex;align-items:center;gap:10px;font-family:var(--display);text-transform:uppercase;letter-spacing:.2em;font-size:13px;color:var(--gold);margin:0 0 14px}
.lede{font-size:19px;color:var(--soft-d);max-width:58ch;margin-top:16px}
.note{font-size:14.5px;color:var(--soft-d)}
.small{font-size:13.5px;color:var(--soft)}
.flag{flex:none}
/* header */
header.site{position:sticky;top:0;z-index:50;background:var(--asphalt)}
header.site::after{content:"";display:block;height:6px;background:repeating-conic-gradient(var(--gold) 0% 25%, var(--asphalt-2) 0% 50%) 50%/12px 12px}
.bar{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px 30px;padding:14px 22px;max-width:1120px;margin:0 auto}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--cream);font-family:var(--display);text-transform:uppercase;letter-spacing:.1em;font-size:19px}
.brand svg{width:30px;height:30px;flex:none}
header.site nav{display:flex;gap:22px;flex-wrap:wrap}
header.site nav a{font-family:var(--display);text-transform:uppercase;letter-spacing:.12em;font-size:13px;color:var(--cream);opacity:.82;text-decoration:none;padding:8px 2px}
header.site nav a:hover,header.site nav a:focus{opacity:1;color:var(--gold)}
@media (max-width:760px){.bar{flex-direction:column;align-items:flex-start;gap:9px}}
/* buttons */
.btn{display:inline-block;font-family:var(--display);text-transform:uppercase;letter-spacing:.09em;font-size:14px;text-decoration:none;border-radius:9px;padding:14px 24px;background:var(--gold);color:var(--ink);border:1.5px solid var(--gold)}
.btn:hover,.btn:focus{background:var(--gold-dk);border-color:var(--gold-dk)}
.btn.ghost{background:transparent;color:var(--cream);border-color:rgba(242,236,223,.5)}
.btn.ghost:hover,.btn.ghost:focus{border-color:var(--cream);color:var(--cream)}
.btn.invert{background:var(--ink);color:var(--cream);border-color:var(--ink)}
.btn.invert:hover,.btn.invert:focus{background:var(--asphalt-2);border-color:var(--asphalt-2)}
.acts{display:flex;gap:14px;flex-wrap:wrap;margin-top:26px}
/* hero */
.hero{background:var(--asphalt);padding:76px 0 88px;position:relative;overflow:hidden}
.hero .wrap{position:relative;z-index:1}
@media (min-width:1024px){.hero::before{content:"";position:absolute;right:-80px;top:-60px;width:300px;height:300px;background:repeating-conic-gradient(var(--asphalt-2) 0% 25%, transparent 0% 50%) 50%/28px 28px;transform:rotate(8deg);opacity:.55;z-index:0}}
.cols{display:grid;grid-template-columns:1.15fr .85fr;gap:44px;align-items:center}
@media (max-width:900px){.cols{grid-template-columns:1fr;gap:36px}}
.heroart svg{width:100%;max-width:420px;height:auto;display:block;margin:0 auto}
/* sections */
.sec{padding:76px 0}
.sec.paper{background:var(--paper);color:var(--ink)}
.sec.paper .lede,.sec.paper .note{color:var(--soft)}
.sec.paper h2{color:var(--ink)}
.sec.dark{background:var(--asphalt);color:var(--cream)}
.band{background:var(--asphalt);padding:62px 0 70px;border-bottom:1px solid var(--line-l)}
.crumbs{font-family:var(--display);text-transform:uppercase;letter-spacing:.1em;font-size:13px;color:var(--soft-d);margin-bottom:18px}
.crumbs a{color:var(--gold);text-decoration:none}
/* cards */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:18px;margin-top:26px}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:26px 22px}
.sec.paper .card{background:#FFFDF7}
.sec.dark .card{background:rgba(255,255,255,.05);border-color:var(--line-l)}
.card h3{margin-bottom:10px}
.sec.paper .card p{color:var(--soft)}
.sec.dark .card p{color:var(--soft-d)}
.card p{font-size:15.5px}
.card ul{list-style:none;margin:8px 0 14px}
.card ul li{font-size:15.5px;padding:6px 0;border-bottom:1px dashed var(--line)}
.card ul li:last-child{border-bottom:0}
.card .more{display:inline-block;font-family:var(--display);text-transform:uppercase;letter-spacing:.08em;font-size:12.5px;text-decoration:none;color:var(--gold-dk);margin-top:8px}
.sec.dark .card .more{color:var(--gold)}
.card .more:hover{text-decoration:underline}
/* menu board */
.board{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0 36px;margin-top:24px}
.board li{display:flex;align-items:center;gap:12px;padding:12px 2px;border-bottom:1px solid var(--line-l);font-family:var(--display);text-transform:uppercase;letter-spacing:.05em;font-size:17.5px}
/* quote */
blockquote{font-family:var(--body);font-style:italic;font-size:clamp(23px,3.2vw,31px);line-height:1.35;color:var(--ink);position:relative;padding-left:44px}
blockquote::before{content:"\\201C";position:absolute;left:0;top:-8px;font:700 64px Georgia,serif;color:var(--gold)}
.attrib{display:flex;align-items:center;gap:10px;margin-top:18px;font-family:var(--display);text-transform:uppercase;letter-spacing:.14em;font-size:12.5px;color:var(--gold-dk)}
/* faq */
.faq{margin-top:24px;max-width:760px}
.faq details{border-bottom:1px solid var(--line)}
.faq summary{font-family:var(--display);text-transform:uppercase;letter-spacing:.05em;font-size:15px;padding:18px 44px 18px 0;position:relative;cursor:pointer;list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:6px;top:50%;transform:translateY(-54%);font-family:var(--display);font-size:24px;color:var(--gold-dk);line-height:1}
.faq details[open] summary::after{content:"\\2013"}
.faq .a{padding:0 24px 18px 0;color:var(--soft);max-width:62ch;font-size:16px}
/* CTA band */
.cta{background:var(--gold);color:var(--ink);padding:58px 0}
.cwrap{display:flex;align-items:center;justify-content:space-between;gap:26px;flex-wrap:wrap}
.cwrap h2{margin:0 0 8px;color:var(--ink)}
.cwrap p{font-size:17px;max-width:52ch;color:#3A3326}
.cwrap .acts{margin-top:0}
@media (max-width:760px){.cwrap .acts{width:100%}.cwrap .acts .btn{width:100%;text-align:center}}
/* contact */
address.bigaddr{font-style:normal;font-size:20px;line-height:2;margin-top:10px}
address.bigaddr a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--gold)}
address.bigaddr a:hover{color:var(--gold-dk)}
.cform{display:grid;gap:16px;background:#FFFDF7;border:1px solid var(--line);border-radius:var(--r);padding:28px 24px}
.cform label{display:block;font-family:var(--display);text-transform:uppercase;letter-spacing:.1em;font-size:12px;color:var(--soft);margin-bottom:6px}
.cform input,.cform textarea{width:100%;font:inherit;font-size:16px;padding:13px 14px;border:1px solid var(--line);border-radius:9px;background:#fff;color:var(--ink)}
.cform textarea{min-height:140px;resize:vertical}
.cform .row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media (max-width:560px){.cform .row{grid-template-columns:1fr}}
.cform .small{margin-top:4px}
/* map */
.mapcard{border-radius:var(--r);overflow:hidden;border:1px solid var(--line-l);margin-top:24px}
.mapcard iframe{width:100%;height:420px;border:0;display:block;background:var(--asphalt-2)}
/* footer */
footer{background:var(--asphalt);color:var(--cream);padding:0 0 42px}
footer .checkerline{height:12px;background:repeating-conic-gradient(var(--gold) 0% 25%, var(--asphalt) 0% 50%) 50%/12px 12px;margin-bottom:44px}
.fgrid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:36px}
@media (max-width:760px){.fgrid{grid-template-columns:1fr;gap:28px}}
.fgrid h4{font-size:14px;color:var(--gold);margin-bottom:12px;letter-spacing:.12em}
.fgrid address.nap{font-style:normal;line-height:1.9;color:var(--cream)}
.fgrid ul{list-style:none}
.fgrid ul li{padding:4px 0}
.fgrid a{color:var(--cream);text-decoration:none}
.fgrid a:hover{color:var(--gold);text-decoration:underline}
.footline{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;border-top:1px solid var(--line-l);margin-top:36px;padding-top:18px;font-size:13.5px;color:var(--soft-d)}
/* utility pages keep generous top space */
main > section > .wrap.prose{padding-top:70px;padding-bottom:80px}
"""
open(os.path.join(PUB, "style.css"), "w", encoding="utf-8").write(CSS)

print("pages built:", sorted(os.listdir(PUB)))
