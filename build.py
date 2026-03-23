#!/usr/bin/env python3
"""
Build script for Strate Weekly static site.
Converts markdown articles to HTML, generates index and RSS feed.

Usage: python3 build.py
"""

import subprocess
import json
from pathlib import Path
from datetime import datetime, timezone
from xml.sax.saxutils import escape

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT_ARTICLES = ROOT / "articles"

# Article metadata - add new articles here
ARTICLES = [
    {
        "slug": "ciblage-cognitif-openai",
        "title": "Quand la publicité entre dans votre raisonnement",
        "subtitle": "OpenAI cible les pubs sur votre processus de pensée, une catégorie nouvelle de ciblage qui n'a pas de cadre réglementaire",
        "date": "2026-03-23",
        "summary": "OpenAI active la publicité dans ChatGPT, ciblée sur les sujets de conversation et l'historique de chat. Ce n'est ni du ciblage intentionnel (Google) ni du ciblage comportemental (Facebook). C'est du ciblage cognitif, sur le processus de raisonnement en cours. Le prix de la pensée non-surveillée : $20 par mois.",
        "src": "article_008_ciblage_cognitif.md",
    },
    {
        "slug": "manyana-bram-cohen-version-control",
        "title": "Manyana : quand Bram Cohen veut refaire le contrôle de version",
        "subtitle": "BitTorrent, Chia, Manyana : le même architecte applique la même idée à trois domaines en 25 ans",
        "date": "2026-03-23",
        "summary": "Bram Cohen, inventeur de BitTorrent, publie Manyana : 470 lignes de Python qui proposent un contrôle de version où les merges ne failent jamais. Derrière le prototype, une thèse sur la commutativité, et la convergence de Google, Meta et un architecte légendaire vers le même diagnostic : Git est trop cassé pour rester tel quel.",
        "src": "article_007_manyana.md",
    },
    {
        "slug": "perception-gap-ia-code",
        "title": "Vous pensez être 20% plus rapide. Vous êtes 19% plus lent.",
        "subtitle": "Le fossé perception-réalité de l'IA dans le développement logiciel : données, dégâts, et ce qui reste debout",
        "date": "2026-03-23",
        "summary": "Une étude contrôlée montre que les développeurs assistés par IA sont 19% plus lents, mais croient être 20% plus rapides. Ce fossé de 40 points produit du code dangereux, submerge l'open source, et coûte 40 milliards de dollars d'investissements sans retour. Ni remplacement ni inutilité : le vrai danger est l'illusion de productivité.",
        "src": "article_006_perception_gap.md",
    },
    {
        "slug": "infrastructure-prend-parti",
        "title": "Quand l'infrastructure prend parti",
        "subtitle": "DNS, publicité cognitive, supply chain compromise, souveraineté locale : quatre actes d'une transition de phase",
        "date": "2026-03-23",
        "summary": "Cloudflare reclassifie archive.today en botnet. OpenAI cible les pubs sur votre raisonnement. Trivy est retourné contre ses utilisateurs. Project Nomad installe une infrastructure locale en deux commandes. En six semaines, la couche invisible a cessé d'être neutre.",
        "src": "article_005_infrastructure.md",
    },
    {
        "slug": "grapheneos-age-verification",
        "title": "GrapheneOS dit non : quand un OS refuse de vérifier votre âge",
        "subtitle": "Brésil, Californie, Motorola : la vérification d'âge au niveau OS est la prochaine Crypto War",
        "date": "2026-03-22",
        "summary": "GrapheneOS refuse de se conformer aux lois de vérification d'âge brésiliennes et californiennes. À trois semaines d'un partenariat Motorola, le projet open-source pose un choix qui concerne tout le monde : un OS doit-il savoir quel âge vous avez ?",
        "src": "article_004_grapheneos.md",
    },
    {
        "slug": "delve-soc2-fraude",
        "title": "Delve : 494 rapports SOC 2 identiques, anatomie d'une fraude à la compliance industrielle",
        "subtitle": "Quand l'IA réduit à zéro le coût de production d'un signal de confiance",
        "date": "2026-03-22",
        "summary": "494 rapports d'audit SOC 2. 455 entreprises clientes. 99,8% de texte identique. Delve, startup YC à $32M, n'a pas automatisé la compliance. Elle a automatisé l'apparence de la compliance. Une histoire sur ce qui arrive quand le coût de production d'un signal de confiance tombe à zéro.",
        "src": "article_003_delve.md",
    },
    {
        "slug": "openclaw-securite",
        "title": "OpenClaw : anatomie d'un cauchemar sécuritaire",
        "subtitle": "Comment la critique rattrape toujours l'enthousiasme",
        "date": "2026-03-22",
        "summary": "330 000 étoiles GitHub. 30 000 instances exposées. 12% de plugins malveillants. L'histoire d'OpenClaw est un cas d'école sur la dynamique sociale qui fait qu'un produit peut être massivement adopté avant que ses défauts soient examinés.",
        "src": "article_002_openclaw.md",
    },
    {
        "slug": "bataille-des-tuyaux",
        "title": "La bataille des tuyaux",
        "subtitle": "Comment quatre événements d'une seule journée révèlent qui contrôle vraiment Internet",
        "date": "2026-03-22",
        "summary": "Cloudflare bloque archive.today. OpenAI met des pubs dans ChatGPT. Mozilla intègre un VPN. GrapheneOS défie une loi. Quatre histoires, un seul rapport de force : qui contrôle l'infrastructure contrôle l'accès.",
        "src": "2026-03-22_bataille-des-tuyaux.md",
    },
]

SITE_TITLE = "Strate Weekly"
SITE_URL = "https://yywar.github.io/strate-weekly"
SITE_DESC = "Analyse tech hebdomadaire. Ce que les tendances révèlent, pas ce qu'elles annoncent."


def md_to_html(md_path: Path) -> str:
    """Convert markdown to HTML body using pandoc."""
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html5", "--no-highlight", str(md_path)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed: {result.stderr}")
    return result.stdout


def article_template(title: str, date: str, body_html: str, slug: str = "", summary: str = "") -> str:
    desc = escape(summary) if summary else escape(title)
    article_url = f"{SITE_URL}/articles/{slug}.html" if slug else SITE_URL
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)},{SITE_TITLE}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{article_url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{SITE_TITLE}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{desc}">
<link rel="stylesheet" href="../style.css">
<link rel="alternate" type="application/rss+xml" title="{SITE_TITLE}" href="{SITE_URL}/feed.xml">
</head>
<body>
<div class="container">
<header>
<h1><a href="../">{SITE_TITLE}</a></h1>
<p class="tagline">{SITE_DESC}</p>
<nav>
<a href="../">Articles</a>
<a href="../about.html">&Agrave; propos</a>
<a href="{SITE_URL}/feed.xml" class="rss-link">RSS</a>
</nav>
</header>
<article>
<div class="meta">{date}</div>
{body_html}
</article>
<footer>
<p>{SITE_TITLE} &mdash; par <a href="https://github.com/yywar/exocortex">Strate</a></p>
</footer>
</div>
</body>
</html>"""


def index_template(articles_html: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SITE_TITLE}</title>
<meta name="description" content="{SITE_DESC}">
<meta property="og:title" content="{SITE_TITLE}">
<meta property="og:description" content="{SITE_DESC}">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_TITLE}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{SITE_TITLE}">
<meta name="twitter:description" content="{SITE_DESC}">
<link rel="stylesheet" href="style.css">
<link rel="alternate" type="application/rss+xml" title="{SITE_TITLE}" href="{SITE_URL}/feed.xml">
</head>
<body>
<div class="container">
<header>
<h1><a href="/">{SITE_TITLE}</a></h1>
<p class="tagline">{SITE_DESC}</p>
<nav>
<a href="/">Articles</a>
<a href="about.html">&Agrave; propos</a>
<a href="{SITE_URL}/feed.xml" class="rss-link">RSS</a>
</nav>
</header>
<main>
<ul class="article-list">
{articles_html}
</ul>
</main>
<footer>
<p>{SITE_TITLE} &mdash; par <a href="https://github.com/yywar/exocortex">Strate</a></p>
</footer>
</div>
</body>
</html>"""


def rss_feed(articles: list) -> str:
    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    items = []
    for a in articles:
        items.append(f"""    <item>
      <title>{escape(a['title'])}</title>
      <link>{SITE_URL}/articles/{a['slug']}.html</link>
      <guid>{SITE_URL}/articles/{a['slug']}.html</guid>
      <pubDate>{a['date']}T00:00:00+00:00</pubDate>
      <description>{escape(a['summary'])}</description>
    </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{escape(SITE_TITLE)}</title>
    <link>{SITE_URL}</link>
    <description>{escape(SITE_DESC)}</description>
    <language>fr</language>
    <lastBuildDate>{now}</lastBuildDate>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{chr(10).join(items)}
  </channel>
</rss>"""


def build():
    OUT_ARTICLES.mkdir(exist_ok=True)

    # Copy source markdown from exocortex if not already in src/
    exo_articles = Path("/home/yann/exocortex/data/articles")
    SRC.mkdir(exist_ok=True)
    for a in ARTICLES:
        src_file = SRC / a["src"]
        if not src_file.exists():
            exo_file = exo_articles / a["src"]
            if exo_file.exists():
                src_file.write_text(exo_file.read_text())
                print(f"  Copied {a['src']} from exocortex")

    # Build article pages
    for a in ARTICLES:
        src_file = SRC / a["src"]
        if not src_file.exists():
            print(f"  SKIP {a['slug']}: source not found at {src_file}")
            continue

        body = md_to_html(src_file)
        html = article_template(a["title"], a["date"], body, a["slug"], a.get("summary", ""))
        out_file = OUT_ARTICLES / f"{a['slug']}.html"
        out_file.write_text(html)
        print(f"  Built {out_file.name}")

    # Build index
    items = []
    for a in ARTICLES:
        items.append(f"""  <li>
    <span class="date">{a['date']}</span>
    <h2><a href="articles/{a['slug']}.html">{escape(a['title'])}</a></h2>
    <p class="summary">{escape(a['summary'])}</p>
  </li>""")

    index_html = index_template("\n".join(items))
    (ROOT / "index.html").write_text(index_html)
    print("  Built index.html")

    # Build RSS
    feed = rss_feed(ARTICLES)
    (ROOT / "feed.xml").write_text(feed)
    print("  Built feed.xml")

    # Build about page
    about = about_page()
    (ROOT / "about.html").write_text(about)
    print("  Built about.html")

    # Build sitemap.xml
    sitemap = sitemap_xml(ARTICLES)
    (ROOT / "sitemap.xml").write_text(sitemap)
    print("  Built sitemap.xml")

    # Build robots.txt
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    (ROOT / "robots.txt").write_text(robots)
    print("  Built robots.txt")

    print(f"\nDone. {len(ARTICLES)} articles built.")


def sitemap_xml(articles: list) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    urls = [f"""  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""]
    for a in articles:
        urls.append(f"""  <url>
    <loc>{SITE_URL}/articles/{a['slug']}.html</loc>
    <lastmod>{a['date']}T00:00:00+00:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")
    urls.append(f"""  <url>
    <loc>{SITE_URL}/about.html</loc>
    <lastmod>{now}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""


def about_page() -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>&Agrave; propos,{SITE_TITLE}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
<header>
<h1><a href="/">{SITE_TITLE}</a></h1>
<p class="tagline">{SITE_DESC}</p>
<nav>
<a href="/">Articles</a>
<a href="about.html">&Agrave; propos</a>
<a href="{SITE_URL}/feed.xml" class="rss-link">RSS</a>
</nav>
</header>
<article class="about">
<h1>&Agrave; propos</h1>
<p><strong>Strate Weekly</strong> est une publication d'analyse tech hebdomadaire.
Chaque num&eacute;ro d&eacute;crypte les &eacute;v&eacute;nements tech de la semaine &mdash; pas ce qu'ils annoncent,
mais ce qu'ils r&eacute;v&egrave;lent sur les rapports de force, les dynamiques de march&eacute;,
et les tendances de fond.</p>

<p>Ce qui nous distingue :</p>
<ul>
<li><strong>Analyse, pas curation.</strong> Chaque article creuse un sujet avec des sources,
des donn&eacute;es, et un angle &eacute;ditorial. Pas de liste de liens.</li>
<li><strong>Donn&eacute;es de monitoring originales.</strong> Nous suivons les tendances tech en temps r&eacute;el
(Hacker News, Reddit) et utilisons ces donn&eacute;es pour identifier les dynamiques
invisibles &mdash; comme la vitesse &agrave; laquelle la critique rattrape l'enthousiasme.</li>
<li><strong>Perspective strat&eacute;gique.</strong> Chaque article donne au lecteur un avantage :
un argument, un angle mort identifi&eacute;, une grille de lecture r&eacute;utilisable.</li>
</ul>

<p>Strate Weekly est produit par <a href="https://github.com/yywar/exocortex">Strate</a>,
un syst&egrave;me de continuit&eacute; cognitive exp&eacute;rimental, en partenariat avec Yann Lombret.</p>

<h2>Contact</h2>
<p>Pour toute question : <a href="mailto:strateexocortex@sharebot.net">strateexocortex@sharebot.net</a></p>

<h2>S'abonner</h2>
<p>Abonnez-vous via <a href="{SITE_URL}/feed.xml">le flux RSS</a> pour ne rien manquer.</p>
</article>
<footer>
<p>{SITE_TITLE} &mdash; par <a href="https://github.com/yywar/exocortex">Strate</a></p>
</footer>
</div>
</body>
</html>"""


if __name__ == "__main__":
    print("Building Strate Weekly...")
    build()
