"""Builds about.html, classes.html and contact.html using the header and
footer from index.html, so all pages stay in sync.
Run from the repo root:  python3 _source/build_pages.py
"""

BOOK = "https://calendar.app.google/PtwzU3Zmm2dFBqB67"
EMAIL = "tammey@inspirationtounstuck.com"
PHONE = "701-261-9066"
SOCIAL = [
    ("Facebook", "https://www.facebook.com/tammey.brown"),
    ("LinkedIn", "https://www.linkedin.com/in/tammeybrown/"),
    ("Instagram", "https://www.instagram.com/tammeybrown/"),
]

PAGES = {
"about": ("About Tammey | Inspiration to Unstuck",
"Meet Tammey, founder of Inspiration to Unstuck: where creativity and technology meet, for women over 50 ready to find their purpose again.",
f"""
  <section class="page-intro">
    <div class="wrap center">
      <span class="eyebrow">About</span>
      <h1>Hi, I'm Tammey.</h1>
      <p class="lede">Where creativity and technology meet, and where you can find your way forward again.</p>
    </div>
  </section>

  <section class="section meet">
    <div class="wrap meet-grid">
      <div class="meet-photo">
        <img src="/images/tammey.jpg" alt="Tammey, founder of Inspiration to Unstuck">
      </div>
      <div>
        <span class="eyebrow">My story</span>
        <h2>I know how it feels to be stuck.</h2>
        <p>For years I felt stuck in a rut, unsure how to move forward, unfulfilled in my career and completely drained of creativity. Through self-reflection, personal growth work and finding the right resources, I was able to break free and rediscover my passion and purpose.</p>
        <p>I grew up near Salt Lake City with a camera in my hand, then moved to Montana as a teenager and fell in love with hiking, fishing, archery and riding horses. After earning a technology degree from the University of Montana, I moved to Fargo, North Dakota, and built a career in tech.</p>
        <p>To balance all that screen time, I took up scrapbooking. That turned into co-founding the online ScrapbookingClasses group, which grew to over 1,500 members, where I designed and taught new layouts every week.</p>
        <p>Today I'm combining both sides: years of tech experience and a love of teaching.</p>
      </div>
    </div>
  </section>

  <section class="section paths">
    <div class="wrap narrow">
      <div class="center">
        <span class="eyebrow">Why Inspiration to Unstuck</span>
        <h2>You still have so much to give</h2>
      </div>
      <p class="lede center">I created this site for women over 50 who gave years to raising a family or to a career, and now feel exhausted, overwhelmed and all used up. You carry a lifetime of knowledge. You want your next chapter to have purpose, and maybe even leave a legacy. You just need a place to start.</p>
      <p class="center">Here you'll find journaling prompts, creative challenges, personal growth tips and friendly how-tos for tech and AI. It's everything I would have found helpful on my own journey.</p>
      <div class="believe">
        <p class="you-close center">"We all have the power within us to create the life we want. Sometimes we just need a little guidance, inspiration and accountability to take that first step forward."</p>
        <h3 class="center">I'm here to help you</h3>
        <ul class="you-list">
          <li>Overcome limiting beliefs and self-doubt</li>
          <li>Discover your true passions and purpose</li>
          <li>Build the confidence to make big changes</li>
          <li>Feel at home with technology and AI, so you can share what you know</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section classes center">
    <div class="wrap">
      <h2>Ready to take your first step?</h2>
      <p class="lede">Start with the free resources, or book a time to talk with me.</p>
      <div class="hero-actions center-actions">
        <a class="btn btn-gold" href="/resources">Explore resources</a>
        <a class="btn btn-ghost" href="{BOOK}" target="_blank" rel="noopener">Book a time</a>
      </div>
    </div>
  </section>
"""),

"classes": ("Classes & Workshops | Inspiration to Unstuck",
"Classes, how-tos and workshops for women over 50, including tech and AI made simple. Coming soon.",
f"""
  <section class="page-intro">
    <div class="wrap center">
      <span class="eyebrow">Classes &amp; workshops</span>
      <h1>Learn it together, one step at a time</h1>
      <p class="lede">I'm creating classes, how-tos and workshops for women who are ready to move forward.</p>
      <span class="badge badge-dark">Coming soon</span>
    </div>
  </section>

  <section class="section paths">
    <div class="wrap">
      <div class="center">
        <span class="eyebrow">What to expect</span>
        <h2>Built around the three paths</h2>
        <p class="lede">Friendly, step-by-step learning at your own pace, with no question too basic.</p>
      </div>
      <div class="cards">
        <article class="card">
          <div class="card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.2 3.8a5.5 5.5 0 0 0-7.8 0L5 11.2V19h7.8l7.4-7.4a5.5 5.5 0 0 0 0-7.8z"/><path d="M16 8 2 22"/><path d="M17.5 15H9"/></svg></div>
          <h3>Rediscover your creativity</h3>
          <p>Hands-on ways to refill the well and make creating part of your life again.</p>
        </article>
        <article class="card">
          <div class="card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2.1 6.3-6.3 2.1 2.1-6.3z"/></svg></div>
          <h3>Find your purpose</h3>
          <p>Gentle guidance for figuring out what you want this next chapter to hold.</p>
        </article>
        <article class="card">
          <div class="card-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/><path d="m9.5 9.5 2 2 3.5-3.5"/></svg></div>
          <h3>Share what you know</h3>
          <p>Tech and AI made simple, so your knowledge can reach the people who need it.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section touch tight">
    <div class="wrap">
      <div class="touch-grid">
        <div class="touch-box">
          <h3>Tell me what you want to learn</h3>
          <p>Your questions shape what I teach first. Book a time or send me a note.</p>
          <a class="btn btn-gold" href="{BOOK}" target="_blank" rel="noopener">Book a time</a>
        </div>
        <div class="touch-box">
          <h3>Start now, for free</h3>
          <p>While classes are on the way, explore free guides, prompts and how-tos.</p>
          <a class="btn btn-plum" href="/resources">Explore resources</a>
        </div>
      </div>
    </div>
  </section>
"""),

"contact": ("Contact | Inspiration to Unstuck",
"Get in touch with Tammey at Inspiration to Unstuck. Book a time, email or call.",
f"""
  <section class="page-intro">
    <div class="wrap center">
      <span class="eyebrow">Contact</span>
      <h1>Let's connect</h1>
      <p class="lede">Have a question, or want to hear when classes open? Reach out any way that works for you.</p>
    </div>
  </section>

  <section class="section touch">
    <div class="wrap">
      <div class="touch-grid three">
        <div class="touch-box">
          <h3>Book a time</h3>
          <p>Pick a time that suits you for a friendly chat.</p>
          <a class="btn btn-gold" href="{BOOK}" target="_blank" rel="noopener">See available times</a>
        </div>
        <div class="touch-box">
          <h3>Email or call</h3>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          <p><a href="tel:+1{PHONE.replace('-', '')}">{PHONE}</a></p>
        </div>
        <div class="touch-box">
          <h3>Follow along</h3>
          <ul class="social">
{chr(10).join(f'            <li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in SOCIAL)}
          </ul>
        </div>
      </div>
      <div class="touch-box list-box center">
        <h3>Join the list</h3>
        <p>Encouragement, new how-tos and first word on classes, sent straight to your inbox.</p>
        <span class="badge">Coming soon</span>
      </div>
    </div>
  </section>
"""),
}


def build():
    src = open("index.html").read()
    head = src[:src.index("<title>")]
    header = src[src.index('<header class="site-header">'):src.index("</header>") + 9]
    header = header.replace('<header class="site-header">', '<header class="site-header solid">')
    footer = src[src.index('<footer class="site-footer">'):]
    for slug, (title, desc, body) in PAGES.items():
        page = f'''{head}<title>{title}</title>
  <meta name="description" content="{desc}">
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
{body}
</main>

{footer}'''
        open(f"{slug}.html", "w").write(page)
        print("built", slug + ".html")


if __name__ == "__main__":
    build()
