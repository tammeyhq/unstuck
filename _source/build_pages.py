"""Builds about.html, classes.html and contact.html using the header and
footer from index.html, so all pages stay in sync.
Run from the repo root:  python3 _source/build_pages.py
"""

BOOK = "https://calendar.app.google/PtwzU3Zmm2dFBqB67"
EMAIL = "tammey@inspirationtounstuck.com"
PHONE = "701-261-9066"
SOCIAL = [
    ("Facebook group", "https://www.facebook.com/groups/inspirationtounstuck"),
    ("Instagram", "https://www.instagram.com/inspirationtounstuck/"),
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
      <p class="lede">Start with the resources, or book a time to talk with me.</p>
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
          <h3>Start now</h3>
          <p>While classes are on the way, explore guides, prompts and how-tos.</p>
          <a class="btn btn-plum" href="/resources">Explore resources</a>
        </div>
      </div>
    </div>
  </section>
"""),

"journal": ("100 Creative Prompts Journal | Inspiration to Unstuck",
"Get 100 creative writing prompts, each with its own journal page, when you join Tammey's email list. For women ready to rediscover their creativity.",
f"""
  <section class="page-intro">
    <div class="wrap center">
      <span class="eyebrow">A gift for you</span>
      <h1>100 Creative Prompts</h1>
      <p class="lede">A printable journal to help you fill your creative well again, one little spark at a time.</p>
    </div>
  </section>

  <section class="section meet gift">
    <div class="wrap meet-grid">
      <div class="gift-cover">
        <img src="/images/journal-cover.jpg" alt="Cover of the Inspiration to Unstuck 100 Creative Prompts journal" width="393" height="509">
      </div>
      <div>
        <h2>Your imagination didn't go anywhere</h2>
        <p>Ever stared at a blank page and felt like your creative well had run dry? I have, more times than I can count. So I put together 100 prompts to get you writing, dreaming and playing with words again.</p>
        <ul class="you-list">
          <li>100 prompts, some fun, some thoughtful, a few that may surprise you</li>
          <li>A lined journal page for every prompt</li>
          <li>Print it, or write on it digitally. Skip around, there are no rules</li>
        </ul>
        <p>There's no cost. I hate it when I get to a site all excited to see what they offer, and instead I get tricked into getting their spam! I won't ever do that to you. This is my gift to you, my way of saying I understand and I'm here for you.</p>
        <p>Pop in your first name and email and I'll send it straight to your inbox. You'll also get my emails with encouragement, new how-tos and first word on classes. Unsubscribe any time.</p>
        <div class="kit-form">
          <script>
            (function (s, e, n, d, er) {{
              s['Sender'] = er;
              s[er] = s[er] || function () {{
                (s[er].q = s[er].q || []).push(arguments)
              }}, s[er].l = 1 * new Date();
              s[er].on = function(event, callback) {{
                s[er].listeners = s[er].listeners || {{}};
                (s[er].listeners[event] = s[er].listeners[event] || []).push(callback);
              }};
              var a = e.createElement(n),
                  m = e.getElementsByTagName(n)[0];
              a.async = 1;
              a.src = d;
              m.parentNode.insertBefore(a, m)
            }})(window, document, 'script', 'https://cdn.sender.net/accounts_resources/universal.js', 'sender');
            sender('0a2f2b8f317063')
          </script>
          <div style="text-align: left" class="sender-form-field" data-sender-form-id="bkRpYY"></div>
        </div>
        <p class="fine">Your information stays with me. See my <a href="/privacy#email-list">privacy policy</a>.</p>
      </div>
    </div>
  </section>
"""),

"privacy": ("Privacy Policy & Disclosures | Inspiration to Unstuck",
"How Inspiration to Unstuck handles your information, cookies, analytics and affiliate links.",
f"""
  <section class="page-intro">
    <div class="wrap center">
      <span class="eyebrow">Privacy policy &amp; disclosures</span>
      <h1>Your privacy matters to me</h1>
      <p class="lede">Here's what happens with your information when you visit Inspiration to Unstuck, in plain language.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow prose">
      <p><em>Last updated: November 4, 2026</em></p>

      <h2 id="who">Who I am</h2>
      <p>Inspiration to Unstuck (www.inspirationtounstuck.com) is run by me, Tammey. If you have any questions about this page or your information, email me at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

      <h2 id="what">What information is collected</h2>
      <p>You can read everything on this site without signing up or giving me any personal information.</p>
      <p>The only information collected automatically is general, anonymous information about how people use the site, through Google Analytics (see below). I don't sell, rent or trade anyone's information. Ever.</p>
      <p>If you email me or book a time with me, I'll only use what you send me to reply to you.</p>

      <h2 id="analytics">Google Analytics and cookies</h2>
      <p>This site uses Google Analytics to help me understand which pages are helpful, how people find the site, and what kind of device they're using. That helps me write more of what you actually want to read.</p>
      <p>Google Analytics uses cookies (small files saved by your browser) and collects things like the pages you visit, how long you stay, your general location (such as your city or country), and your browser and device type. It doesn't tell me who you are.</p>
      <p>Google processes this information under its own privacy policy. You can learn more about <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>. If you'd rather not be included, you can install the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">Google Analytics opt-out browser add-on</a>, or block cookies in your browser settings.</p>

      <h2 id="affiliate">Affiliate links</h2>
      <p>Some posts include affiliate links. If you click one and make a purchase, I may earn a small commission at no extra cost to you. I only share things I think are genuinely helpful, and any post with affiliate links says so near the top.</p>
      <p>Inspiration to Unstuck is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com. As an Amazon Associate I earn from qualifying purchases.</p>
      <p>Some posts may also include affiliate links for other companies, such as Canva or Creative Fabrica.</p>

      <h2 id="other-sites">Other websites and services</h2>
      <p>This site links to other places, like my Facebook group, Instagram, Google Calendar (for booking a time with me) and the stores mentioned above. Once you click over to another site, its own privacy policy applies.</p>
      <p>To look its best, this site also loads fonts from Google Fonts and some photos from Pexels, which may see basic technical information such as your IP address when your browser requests them.</p>

      <h2 id="email-list">My email list</h2>
      <p>If you sign up for my email list (for example, to get the 100 Creative Prompts journal), I collect your first name and email address. I use them only to send you the journal, encouragement, new how-tos and news about classes and workshops. I never sell or share your information.</p>
      <p>My emails are sent through <a href="https://www.sender.net/privacy-policy/" target="_blank" rel="noopener">Sender</a>, which stores your name and email address for me and may track whether emails are opened or links are clicked. Every email has an unsubscribe link at the bottom, and you can also email me any time to be removed.</p>

      <h2 id="children">Children</h2>
      <p>This site is written for adults and isn't directed to children under 13. I don't knowingly collect information from children.</p>

      <h2 id="changes">Changes to this page</h2>
      <p>If anything changes, I'll update this page and the date at the top.</p>

      <h2 id="questions">Questions?</h2>
      <p>Just email me at <a href="mailto:{EMAIL}">{EMAIL}</a>. I'm happy to help.</p>
    </div>
  </section>
"""),

"404": ("Page not found | Inspiration to Unstuck",
"Sorry, that page couldn't be found.",
f"""
  <section class="page-intro">
    <div class="wrap center">
      <span class="eyebrow">Page not found</span>
      <h1>Oops, that page has wandered off.</h1>
      <p class="lede">It may have moved when the site got its fresh new look. Let's get you back on track.</p>
      <div class="hero-actions center-actions">
        <a class="btn btn-gold" href="/resources">Browse resources</a>
        <a class="btn btn-plum" href="/">Go to the home page</a>
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
        <p>Encouragement, new how-tos and first word on classes, sent straight to your inbox. Join and I'll send you my 100 Creative Prompts journal as a thank-you.</p>
        <a class="btn btn-gold" href="/journal">Get your journal</a>
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
