"""Builds resources.html from the post list below.
Run from the repo root:  python3 _source/build_resources.py
Each post card links to its own page at /<slug>. Until a post page is
brought over, the card links to the live old post (OLD_SITE) instead.
"""
import os, html

UNSTUCK = "https://inspirationtounstuck.com"
TB = "https://tammeybrown.com"

# (slug, title, one-line summary, original site)
SECTIONS = [
  ("creativity", "Rediscover your creativity",
   "Journaling, prompts and gentle creative challenges to refill the well when you feel drained.", [
    ("7-signs-your-ideas-are-running-on-empty-and-how-to-recognize-creative-fatigue", "7 Signs Your Ideas Are Running on Empty", "How to recognize creative fatigue, and what to do about it.", UNSTUCK),
    ("recognizing-creative-burnout-and-writers-block", "Recognizing Creative Burnout and Writer's Block", "When the page stays blank, here's what may be going on.", UNSTUCK),
    ("signs-of-creative-burnout-and-actions", "10 Signs of Creative Burnout and Empowering Actions", "Spot the signs and take small, kind steps to reignite your spark.", UNSTUCK),
    ("creative-toolkit", "Revitalize Your Passion: Tools for Battling Writer's Block", "Practical tools for climbing over a creative wall.", UNSTUCK),
    ("morning-pages", "Unlock Inspiration with Morning Pages", "A simple daily writing habit that clears the clutter.", UNSTUCK),
    ("rediscovering-joy-adventurous-morning-pages-ideas", "Rediscovering Joy: Adventurous Morning Pages Ideas", "Fresh ways to make your morning pages fun again.", UNSTUCK),
    ("boost-your-creativity-with-gratitude-journaling", "Boost Your Creativity with Gratitude Journaling", "How noticing the good opens the door to new ideas.", UNSTUCK),
    ("god-box-journaling", "God Box Journaling: Empowering Ideas for You", "A gentle way to set down your worries and make room to create.", UNSTUCK),
    ("the-power-of-creative-writing-prompts", "The Power of Creative Writing Prompts", "Prompts to get your storytelling moving again.", UNSTUCK),
    ("mundane-to-marvelous-inspiring-oject-prompts", "Mundane to Marvelous: Inspiring Object Prompts", "Let your inner child play with everyday objects.", UNSTUCK),
    ("reignite-your-imagination", "Reignite Your Imagination: 5 Creative Exercises", "Easy exercises for instant inspiration.", UNSTUCK),
    ("perspective-shifting-exercises-to-reignite-creativity", "Perspective-Shifting Exercises to Reignite Creativity", "See familiar things in a new way.", UNSTUCK),
    ("cultivating-creativity-with-inspiring-ideas", "Cultivating Creativity with Inspiring Ideas", "Reconnect with your creative self as life shifts.", UNSTUCK),
    ("easy-ways-to-find-inspiration", "Easy Ways to Find Inspiration", "Simple ways to bring your creative spark back.", UNSTUCK),
    ("creative-challenges-overcome-burnout", "12 Daily Creative Challenges", "One small challenge a day to move past burnout.", UNSTUCK),
    ("photo-a-day-challenge", "Photo-A-Day Challenge", "Find inspiration in the everyday, one photo at a time.", UNSTUCK),
    ("creating-a-space-for-creativity-guide", "Creating a Safe Space for Creativity", "Make a place, inside and out, where creativity feels safe.", UNSTUCK),
  ]),
  ("purpose", "Find your purpose",
   "Make sense of this new chapter, care for yourself, and decide what the rest of your story will say.", [
    ("embracing-change", "How to Embrace Change: A Guide for Women Over 50", "Finding your footing when everything around you is shifting.", UNSTUCK),
    ("self-care-plan", "Craft Your Self-Care Plan Now", "When the weight of the world is on your shoulders, start here.", UNSTUCK),
    ("mastering-goal-setting", "Mastering Goal Setting", "Set goals that move you forward without wearing you out.", UNSTUCK),
    ("benefits-of-accountability", "Benefits of Accountability", "How I stopped doing it all alone, and why it changed everything.", TB),
    ("seeing-the-extraordinary-in-the-ordinary", "Seeing the Extraordinary in the Ordinary", "The gift of seeing your everyday life with fresh eyes.", UNSTUCK),
    ("whispers-of-the-soul-heartache-healing-and-renewal", "Whispers of the Soul: Heartache, Healing, and Renewal", "Writing your way through heartache toward something new.", UNSTUCK),
    ("ink-and-insight-unleashing-self-discovery-from-the-shadows-of-doubt", "Ink and Insight: Self-Discovery from the Shadows of Doubt", "Quiet the voice of self-doubt and hear your own again.", UNSTUCK),
  ]),
  ("share", "Share what you know",
   "Friendly, step-by-step help with tech and AI, so your knowledge can reach the people who need it.", [
    ("overcoming-writers-block-with-ai-inspiration", "Overcoming Writer's Block with AI", "How AI can help when you're staring at a blank page.", UNSTUCK),
    ("ways-bloggers-can-use-ai-for-quicker-better-content", "5 Ways to Use AI for Quicker, Better Writing", "Let AI handle the busywork so your ideas shine.", TB),
    ("how-to-write-an-engaging-blog-post-that-drives-traffic", "How to Write an Engaging Blog Post", "Write posts people actually want to read.", TB),
    ("how-to-organize-a-blogpost", "How to Organize a Blog Post", "Headings and subheadings that make your writing easy to follow.", TB),
    ("how-many-images-should-be-in-a-blog-post", "How Many Images Should Be in a Blog Post?", "Use pictures to draw readers in.", TB),
    ("what-are-keywords", "What Are Keywords?", "A plain-English guide to helping people find you.", TB),
    ("meta-descriptions-and-how-to-use-them-a-beginners-guide", "Meta Descriptions: A Beginner's Guide", "The short summary that shows up in search results.", TB),
    ("choosing-your-colors", "Choosing Your Colors", "How to pick colors that feel like you.", TB),
  ]),
]

ICONS = {
  "creativity": '<path d="M20.2 3.8a5.5 5.5 0 0 0-7.8 0L5 11.2V19h7.8l7.4-7.4a5.5 5.5 0 0 0 0-7.8z"/><path d="M16 8 2 22"/><path d="M17.5 15H9"/>',
  "purpose": '<circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2.1 6.3-6.3 2.1 2.1-6.3z"/>',
  "share": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/><path d="m9.5 9.5 2 2 3.5-3.5"/>',
}

def link(slug, site):
    # A post page brought into this site wins; otherwise point at the live old post.
    if os.path.exists(f"{slug}.html") or os.path.exists(f"{slug}/index.html"):
        return f"/{slug}"
    return f"{site}/{slug}/"

def card(key, slug, title, summary, site):
    img = f"images/posts/{slug}.jpg"
    if os.path.exists(img):
        thumb = f'<img src="/{img}" alt="" loading="lazy" width="640" height="400">'
    else:
        thumb = f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[key]}</svg>'
    return f'''        <a class="post-card" href="{link(slug, site)}">
          <div class="post-thumb thumb-{key}">{thumb}</div>
          <div class="post-body">
            <h3>{html.escape(title)}</h3>
            <p>{html.escape(summary)}</p>
          </div>
        </a>'''

def build():
    src = open("index.html").read()
    head = src[:src.index("<title>")]
    header = src[src.index('<header class="site-header">'):src.index("</header>") + 9]
    footer = src[src.index('<footer class="site-footer">'):]
    header = header.replace('<header class="site-header">', '<header class="site-header solid">')

    jump = "\n".join(f'        <a href="#{k}">{html.escape(t)}</a>' for k, t, _, _ in SECTIONS)
    body = []
    for k, t, intro, posts in SECTIONS:
        cards = "\n".join(card(k, *p) for p in posts)
        body.append(f'''  <section class="section res-section" id="{k}">
    <div class="wrap">
      <div class="res-head">
        <div class="card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg></div>
        <div>
          <h2>{html.escape(t)}</h2>
          <p class="lede">{html.escape(intro)}</p>
        </div>
      </div>
      <div class="post-grid">
{cards}
      </div>
    </div>
  </section>''')

    page = f'''{head}<title>Resources | Inspiration to Unstuck</title>
  <meta name="description" content="Free guides, prompts and how-tos for women over 50: rediscover your creativity, find your purpose, and share what you know with simple tech and AI.">
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
  <section class="page-intro">
    <div class="wrap center">
      <span class="eyebrow">Resources</span>
      <h1>Help for wherever you are today</h1>
      <p class="lede">Free guides, prompts and how-tos to help you get unstuck. Start with the path that speaks to you.</p>
      <nav class="jump" aria-label="Jump to a path">
{jump}
      </nav>
    </div>
  </section>

{chr(10).join(body)}
</main>

{footer}'''
    open("resources.html", "w").write(page)
    print("resources.html built:", sum(len(s[3]) for s in SECTIONS), "posts")

if __name__ == "__main__":
    build()
