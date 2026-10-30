"""NOTE: the posts already moved have been hand-edited in _source/posts/.
Re-running this on those slugs would overwrite the edits; use it only for new imports.

Converts posts from a WordPress export (.xml) into clean HTML bodies.

  python3 _source/convert_wp.py <export.xml> <uploads-folder> [slug ...]

For each published post (or only the slugs given) it writes:
  _source/posts/<slug>.html      the cleaned post body (edit this to change a post)
  _source/posts/<slug>.json      title + notes found while converting
  images/posts/<slug>/...        the post's pictures, resized for the web

Cleaning rules:
  * WordPress block comments, share buttons and inline styles are removed
  * Rubi affiliate links (checkoutrubi.com, myflex.ai) are removed; image
    credits become "Image created by Tammey"
  * Amazon links are kept, marked sponsored, and the post is flagged so the
    page shows an affiliate disclosure
  * Links to old posts/pages on inspirationtounstuck.com or migrated
    tammeybrown.com posts point to the new pages
  * Year tags like "[2024 Guide]" are dropped
"""
import sys, os, re, json, xml.etree.ElementTree as ET
from bs4 import BeautifulSoup, Comment
from PIL import Image

NS = {"wp": "http://wordpress.org/export/1.2/",
      "content": "http://purl.org/rss/1.0/modules/content/"}
RUBI = re.compile(r"checkoutrubi|myflex\.ai|rubi", re.I)
DATED = re.compile(r"\s*\[20\d\d (?:Update|Guide)\]")
PAGE_MAP = {"about": "/about", "contact": "/contact", "blog": "/resources",
            "offerings": "/classes", "shop": "/classes", "": "/"}
# old links that pointed at pages which never existed -> the post they meant
ALIASES = {"daily-photo-challenge": "/photo-a-day-challenge",
           "daily-creative-writing-prompts": "/the-power-of-creative-writing-prompts"}
# stock photos that have since been removed from Pexels
GONE = {"7898126", "9360199"}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def migrated_slugs():
    sys.path.insert(0, os.path.join(ROOT, "_source"))
    from build_resources import SECTIONS
    return {p[0] for s in SECTIONS for p in s[3]}


def find_upload(uploads, rel):
    """Locate an uploaded file, falling back to the full-size original."""
    p = os.path.join(uploads, rel)
    if os.path.exists(p):
        base = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", p)
        return base if os.path.exists(base) else p
    base = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", p)
    return base if os.path.exists(base) else None


def save_web_image(src, dest):
    im = Image.open(src)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 253, 249))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    if im.width > 1100:
        im = im.resize((1100, round(im.height * 1100 / im.width)), Image.LANCZOS)
    im.save(dest, quality=80, optimize=True, progressive=True)


def rewrite_href(href, slugs):
    h = href.strip()
    key = re.sub(r"^(?:https?://)?(?:www\.)?(?:inspirationtounstuck\.com)?/?", "", h, flags=re.I).strip("/").lower()
    if key in ALIASES:
        return ALIASES[key]
    m = re.match(r"^(?:https?://)?(?:www\.)?(inspirationtounstuck|tammeybrown)\.com/?([^?#]*)(#.*)?$", h, re.I)
    if not m:
        return None
    site, path, frag = m.group(1).lower(), m.group(2).strip("/"), m.group(3) or ""
    first = path.split("/")[0]
    if first in slugs:
        return "/" + first + frag
    if site == "inspirationtounstuck" and first in PAGE_MAP:
        return PAGE_MAP[first] + frag
    return None


def clean(html, slug, uploads, slugs, notes):
    soup = BeautifulSoup(html, "html.parser")
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    # share / follow widgets
    for el in soup.select(".wp-block-uagb-social-share, .wp-block-social-links, ul.wp-block-social-links"):
        el.decompose()
    # the page template shows the title, so drop the post's own H1
    for h in soup.find_all("h1"):
        h.decompose()
    # Flickr and other embeds become a simple link
    for fig in soup.select("figure.wp-block-embed"):
        url = fig.get_text(" ", strip=True).split()[0] if fig.get_text(strip=True) else ""
        if url.startswith("http"):
            p = soup.new_tag("p")
            a = soup.new_tag("a", href=url, target="_blank", rel="noopener")
            a.string = "See the photo on Flickr" if "flickr" in url else "Open the link"
            p.append(a)
            fig.replace_with(p)
            notes.append(f"embed turned into a link: {url}")
        else:
            fig.decompose()

    # images
    os.makedirs(os.path.join(ROOT, "images/posts", slug), exist_ok=True)
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if any(f"/photos/{g}/" in src for g in GONE):
            fig = img.find_parent("figure")
            (fig or img).decompose()
            continue
        if "images.pexels.com" in src:
            # free Pexels stock photos load from Pexels itself, which stays up after the move
            img.attrs = {"src": src.split("?")[0] + "?auto=compress&cs=tinysrgb&w=1100", "alt": img.get("alt", ""), "loading": "lazy"}
            continue
        m = re.search(r"wp-content/uploads/(.+?\.(?:jpe?g|png|webp|gif))", src, re.I)
        found = find_upload(uploads, m.group(1)) if (m and uploads) else None
        if not found:
            notes.append(f"MISSING IMAGE {src}")
            fig = img.find_parent("figure")
            (fig or img).decompose()
            continue
        name = re.sub(r"[^a-z0-9-]+", "-", os.path.splitext(os.path.basename(found))[0].lower()).strip("-")
        name = re.sub(r"-?(?:made-)?(?:by-)?(?:tammey-and-)?(?:rubi|rui)(?:-ai)?|-made-by-ai", "", name).strip("-") or slug
        name += ".jpg"
        save_web_image(found, os.path.join(ROOT, "images/posts", slug, name))
        alt = img.get("alt", "")
        alt = " ".join(s for s in re.split(r"(?<=[.!?])\s+", alt) if not RUBI.search(s) and not re.search(r"created by|generated by", s, re.I))
        new = soup.new_tag("img", src=f"/images/posts/{slug}/{name}", alt=alt.strip(), loading="lazy")
        # unwrap images that were links to Rubi
        parent = img.parent
        img.replace_with(new)
        if parent.name == "a" and RUBI.search(parent.get("href", "")):
            parent.unwrap()

    # some image blocks put their credit in a plain paragraph after the image
    for p in soup.find_all("p"):
        prev = p.find_previous_sibling()
        txt = p.get_text(" ", strip=True)
        if prev is not None and prev.name == "figure" and len(txt) < 140 and re.match(r"(photo|image)\b", txt, re.I) and RUBI.search(txt):
            cap = soup.new_tag("figcaption")
            cap.string = "Image created by Tammey"
            prev.append(cap)
            p.decompose()
        elif len(txt) < 140 and re.search(r"(created|generated|photo|image)\b.*\bby\b.*rubi", txt, re.I):
            p.clear()
            p.string = "Image created by Tammey"
            p["class"] = "caption"
    for cap in soup.find_all("figcaption"):
        if RUBI.search(cap.get_text()) or RUBI.search(str(cap)):
            cap.clear()
            cap.string = "Image created by Tammey"

    # links
    amazon = False
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if RUBI.search(href):
            a.unwrap()
            continue
        if href.startswith("#"):
            continue
        if href.startswith("/") and href.strip("/").lower() in ALIASES:
            a.attrs = {"href": ALIASES[href.strip("/").lower()]}
            continue
        new = rewrite_href(href, slugs)
        if new:
            a.attrs = {"href": new}
            continue
        if re.search(r"amzn\.to|amazon\.", href, re.I):
            amazon = True
            a.attrs = {"href": href, "target": "_blank", "rel": "sponsored nofollow noopener"}
        elif href.startswith("http"):
            a.attrs = {"href": href, "target": "_blank", "rel": "noopener"}

    # strip presentation attributes, keep heading ids for the table of contents
    for el in soup.find_all(True):
        keep = {}
        for k in ("class",) if el.name == "p" and el.get("class") == ["caption"] else ():
            keep[k] = "caption"
        for k in ("href", "src", "alt", "id", "target", "rel", "loading", "colspan", "rowspan", "start", "reversed"):
            if el.has_attr(k):
                keep[k] = el[k]
        cls = el.get("class") or []
        if "wp-block-aioseo-table-of-contents" in cls or el.name in ("nav",):
            keep["class"] = "toc"
        if "wp-block-table" in cls:
            keep["class"] = "table-wrap"
        if "wp-block-quote" in cls or el.name == "blockquote":
            pass
        el.attrs = keep
    # drop layout-only wrappers
    for el in soup.find_all(["div", "span"]):
        if not el.attrs:
            el.unwrap()
    for p in soup.find_all("p"):
        if not p.get_text(strip=True) and not p.find("img"):
            p.decompose()

    out = str(soup)
    out = DATED.sub("", out)
    out = re.sub(r"\n\s*\n+", "\n", out).strip()
    left = re.findall(r"[^.>]{0,60}\bRubi[^.<]{0,60}", BeautifulSoup(out, "html.parser").get_text(" "), re.I)
    for l in left:
        notes.append("Rubi still mentioned in text: …" + " ".join(l.split()) + "…")
    return out, amazon


def main():
    xml_path, uploads = sys.argv[1], sys.argv[2]
    only = set(sys.argv[3:])
    slugs = migrated_slugs()
    os.makedirs(os.path.join(ROOT, "_source/posts"), exist_ok=True)
    for it in ET.parse(xml_path).getroot().findall("./channel/item"):
        if it.findtext("wp:post_type", namespaces=NS) != "post" or it.findtext("wp:status", namespaces=NS) != "publish":
            continue
        slug = it.findtext("wp:post_name", namespaces=NS)
        if (only and slug not in only) or slug not in slugs:
            continue
        notes = []
        body, amazon = clean(it.findtext("content:encoded", namespaces=NS) or "", slug, uploads, slugs, notes)
        title = DATED.sub("", it.findtext("title") or slug).replace("&#8217;", "'")
        open(os.path.join(ROOT, "_source/posts", slug + ".html"), "w").write(body + "\n")
        json.dump({"title": title, "amazon": amazon, "notes": notes},
                  open(os.path.join(ROOT, "_source/posts", slug + ".json"), "w"), indent=1)
        flag = " [amazon]" if amazon else ""
        print(f"{slug}{flag}")
        for n in notes:
            print("   -", n)


if __name__ == "__main__":
    main()
