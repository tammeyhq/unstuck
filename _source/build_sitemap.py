"""Writes sitemap.xml and robots.txt for inspirationtounstuck.com.
Run from the repo root after building pages:  python3 _source/build_sitemap.py
"""
import glob, os, datetime

SITE = "https://inspirationtounstuck.com"
SKIP = {"404.html", "_preview.html"}

def main():
    today = datetime.date.today().isoformat()
    urls = []
    for f in sorted(glob.glob("*.html")):
        if f in SKIP:
            continue
        path = "/" if f == "index.html" else "/" + f[:-5]
        urls.append(f"  <url><loc>{SITE}{path}</loc><lastmod>{today}</lastmod></url>")
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print(len(urls), "pages in sitemap")

if __name__ == "__main__":
    main()
