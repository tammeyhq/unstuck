"""Builds a page for every post that has a cleaned body in _source/posts/.
Run from the repo root:  python3 _source/build_posts.py
(then python3 _source/build_resources.py so the cards point to the new pages)
"""
import os, re, json, html, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_resources import SECTIONS

BOOK = "https://calendar.app.google/PtwzU3Zmm2dFBqB67"
FIXES = {"Oject": "Object"}


def shell():
    src = open("index.html").read()
    head = src[:src.index("<title>")]
    header = src[src.index('<header class="site-header">'):src.index("</header>") + 9]
    header = header.replace('<header class="site-header">', '<header class="site-header solid">')
    footer = src[src.index('<footer class="site-footer">'):]
    return head, header, footer


def related_cards(key, slug, posts):
    others = [p for p in posts if p[0] != slug]
    idx = [p[0] for p in posts].index(slug)
    picks = (others[idx:] + others[:idx])[:3]
    out = []
    for s, title, summary, site in picks:
        href = f"/{s}" if os.path.exists(f"_source/posts/{s}.html") else f"{site}/{s}/"
        out.append(f'''        <a class="post-card" href="{href}">
          <div class="post-thumb"><img src="/images/posts/{s}.jpg" alt="" loading="lazy" width="640" height="400"></div>
          <div class="post-body">
            <h3>{html.escape(title)}</h3>
            <p>{html.escape(summary)}</p>
          </div>
        </a>''')
    return "\n".join(out)


def build():
    head, header, footer = shell()
    built = 0
    for key, section_title, _intro, posts in SECTIONS:
        for slug, short_title, summary, _site in posts:
            body_path = f"_source/posts/{slug}.html"
            if not os.path.exists(body_path):
                continue
            meta = json.load(open(f"_source/posts/{slug}.json"))
            title = html.unescape(meta["title"])
            for a, b in FIXES.items():
                title = title.replace(a, b)
            body = open(body_path).read()
            dup = meta.get("hero_in_body")
            if dup:
                # the big image at the top already shows this picture
                body = re.sub(r'<figure>\s*<img[^>]*src="' + re.escape(dup) + r'"[^>]*/?>\s*(?:<figcaption>.*?</figcaption>)?\s*</figure>', "", body, count=1, flags=re.S)
            hero = ""
            if os.path.exists(f"images/posts/{slug}-wide.jpg"):
                hero = f'''    <div class="wrap post-hero"><img src="/images/posts/{slug}-wide.jpg" alt="" width="1200" height="700"></div>\n'''
            disclosure = ""
            if meta.get("amazon"):
                disclosure = '''      <p class="disclosure">This post contains Amazon affiliate links. If you buy through them, I may earn a small commission at no extra cost to you. Thank you for supporting Inspiration to Unstuck!</p>\n'''
            page = f'''{head}<title>{html.escape(title)} | Inspiration to Unstuck</title>
  <meta name="description" content="{html.escape(summary)}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(summary)}">
  <meta property="og:image" content="/images/posts/{slug}-wide.jpg">
  <link rel="icon" href="/images/favicon-48.png" type="image/png">
  <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Lato:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/site.css">
</head>
<body>

{header}

<main>
  <article class="post">
    <header class="post-head wrap narrow">
      <a class="crumb" href="/resources#{key}">&larr; {html.escape(section_title)}</a>
      <h1>{html.escape(title)}</h1>
      <p class="lede">{html.escape(summary)}</p>
      <p class="byline"><img src="/images/tammey-sm.jpg" alt="" width="44" height="44"> By Tammey</p>
    </header>
{hero}    <div class="wrap narrow">
{disclosure}      <div class="prose">
{body}
      </div>
    </div>
  </article>

  <section class="section paths related">
    <div class="wrap">
      <div class="center">
        <span class="eyebrow">Keep exploring</span>
        <h2>More on {html.escape(section_title.lower())}</h2>
      </div>
      <div class="post-grid">
{related_cards(key, slug, posts)}
      </div>
      <p class="center more-link"><a class="btn btn-plum" href="/resources">See all resources</a></p>
    </div>
  </section>

  <section class="section classes center">
    <div class="wrap">
      <h2>Ready for your next step?</h2>
      <p class="lede">Classes and workshops are coming soon. In the meantime, I'd love to hear what you want to learn.</p>
      <div class="hero-actions center-actions">
        <a class="btn btn-gold" href="{BOOK}" target="_blank" rel="noopener">Book a time</a>
        <a class="btn btn-ghost" href="/classes">About classes</a>
      </div>
    </div>
  </section>
</main>

{footer}'''
            open(f"{slug}.html", "w").write(page)
            built += 1
    print("built", built, "post pages")


if __name__ == "__main__":
    build()
